"""Erzeugt die Daten-JSONs fuer die Uebersichts-Seite.

Pro Sprache eine Datei `assets/data/resources.<lang>.json` mit:
  - resources: Liste der Ressourcen mit lokalisierten Texten
  - labels:    Liste aller Label-Knoten (Skill / CEFR / Lizenz / Sprache / Unit)
  - edges:     Co-Occurrence-Kanten zwischen Labels (gewichtet)
  - related:   pro Ressource die drei aehnlichsten Resource-IDs (Jaccard)
  - ui:        UI-Strings fuer das Frontend
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import yaml

from i18n import LANGS, skill_label, t

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "_resources" / "sources_master.yml"
OUT = ROOT / "assets" / "data"


def _localized(r: dict, base_field: str, lang: str) -> str:
    if lang in ("en", "fr"):
        v = r.get(f"{base_field}_{lang}")
        if v:
            return v
    return r.get(base_field, "")


def tag_set(r: dict) -> set[str]:
    """Tags fuer Aehnlichkeit + Knoten im Netzwerk."""
    tags: set[str] = set()
    if r.get("language"):
        tags.add(f"lang:{r['language']}")
    if r.get("license_type"):
        tags.add(f"lic:{r['license_type']}")
    for sk in r.get("skills") or []:
        tags.add(f"skill:{sk}")
    for lvl in r.get("cefr_levels") or []:
        tags.add(f"cefr:{lvl}")
    for u in r.get("applicable_units") or []:
        tags.add(f"unit:{u}")
    return tags


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def label_display(label_id: str, lang: str) -> str:
    """label_id like 'skill:hoeren' -> lokalisiertes Label."""
    cat, _, val = label_id.partition(":")
    if cat == "skill":
        return skill_label(val, lang)
    if cat == "cefr":
        return val
    if cat == "lic":
        return val
    if cat == "lang":
        return val
    if cat == "unit":
        return val
    return label_id


def label_category(label_id: str) -> str:
    return label_id.split(":", 1)[0]


def build_for_lang(resources: list[dict], lang: str) -> dict:
    # ---- pro Resource: tags + lokalisierter Inhalt ----
    enriched = []
    tag_by_id: dict[str, set[str]] = {}
    for r in resources:
        rid = r["id"]
        tags = tag_set(r)
        tag_by_id[rid] = tags
        enriched.append({
            "id": rid,
            "title": r.get("title"),
            "publisher": r.get("publisher"),
            "url": r.get("url"),
            "language": r.get("language"),
            "license_type": r.get("license_type"),
            "cefr_levels": r.get("cefr_levels") or [],
            "skills": r.get("skills") or [],
            "skills_labels": [skill_label(s, lang) for s in (r.get("skills") or [])],
            "applicable_units": r.get("applicable_units") or [],
            "description": _localized(r, "description", lang).strip(),
            "curator_notes": _localized(r, "curator_notes", lang).strip(),
            "last_checked": str(r.get("last_checked", "")),
            "tags": sorted(tags),
        })

    # ---- Related: top-3 per resource via Jaccard ----
    related: dict[str, list[str]] = {}
    ids = list(tag_by_id.keys())
    for rid in ids:
        scored = [
            (other, jaccard(tag_by_id[rid], tag_by_id[other]))
            for other in ids if other != rid
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        related[rid] = [oid for oid, score in scored[:3] if score > 0]

    # ---- Labels (Knoten) und Co-Occurrence (Kanten) ----
    label_count: dict[str, int] = {}
    for tags in tag_by_id.values():
        for lbl in tags:
            label_count[lbl] = label_count.get(lbl, 0) + 1

    labels = [
        {
            "id": lbl,
            "label": label_display(lbl, lang),
            "category": label_category(lbl),
            "count": cnt,
        }
        for lbl, cnt in sorted(label_count.items())
    ]

    edge_weight: dict[tuple[str, str], int] = {}
    for tags in tag_by_id.values():
        for a, b in combinations(sorted(tags), 2):
            edge_weight[(a, b)] = edge_weight.get((a, b), 0) + 1
    edges = [
        {"from": a, "to": b, "weight": w}
        for (a, b), w in edge_weight.items()
        if w >= 1
    ]

    # ---- UI-Strings fuer das Frontend ----
    ui = {
        "filter_heading":   t_or(lang, "Filter nach Label", "Filter by label", "Filtrer par étiquette"),
        "filter_clear":     t_or(lang, "Alle Filter zurücksetzen", "Clear all filters", "Réinitialiser les filtres"),
        "graph_heading":    t_or(lang, "Label-Netzwerk", "Label network", "Réseau d'étiquettes"),
        "graph_hint":       t_or(lang,
            "Klicken Sie auf einen Knoten, um nach diesem Label zu filtern.",
            "Click a node to filter by that label.",
            "Cliquez sur un nœud pour filtrer par cette étiquette."),
        "results_heading":  t_or(lang, "Ressourcen", "Resources", "Ressources"),
        "results_count":    t_or(lang, "{n} Treffer", "{n} matches", "{n} résultats"),
        "no_results":       t_or(lang,
            "Keine Ressource entspricht der aktuellen Auswahl.",
            "No resource matches the current selection.",
            "Aucune ressource ne correspond à la sélection."),
        "details_open":     t_or(lang, "Details anzeigen", "Show details", "Afficher les détails"),
        "details_close":    t_or(lang, "Schließen", "Close", "Fermer"),
        "open_resource":    t_or(lang, "Ressource öffnen", "Open resource", "Ouvrir la ressource"),
        "related_heading":  t_or(lang,
            "Weiterführende Ressourcen",
            "Further reading",
            "Pour aller plus loin"),
        "related_back":     t_or(lang,
            "Zurück zur Netzwerk­grafik",
            "Back to network graph",
            "Retour au réseau"),
        "category_lang":    t_or(lang, "Sprache", "Language", "Langue"),
        "category_lic":     t_or(lang, "Lizenz", "Licence", "Licence"),
        "category_skill":   t_or(lang, "Fertigkeit", "Skill", "Compétence"),
        "category_cefr":    t_or(lang, "Niveau", "Level", "Niveau"),
        "category_unit":    t_or(lang, "Unit", "Unit", "Unité"),
        "publisher_label":  t_or(lang, "Anbieter", "Publisher", "Fournisseur"),
        "last_check":       t_or(lang, "Letzter Link-Check", "Last link check", "Dernière vérification"),
    }

    return {
        "lang": lang,
        "ui": ui,
        "labels": labels,
        "edges": edges,
        "resources": enriched,
        "related": related,
    }


def t_or(lang: str, de: str, en: str, fr: str) -> str:
    return {"de": de, "en": en, "fr": fr}.get(lang, de)


def main():
    with MASTER.open(encoding="utf-8") as fh:
        resources = yaml.safe_load(fh) or []

    OUT.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        data = build_for_lang(resources, lang)
        out = OUT / f"resources.{lang}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)} "
              f"({len(data['resources'])} resources, "
              f"{len(data['labels'])} labels, "
              f"{len(data['edges'])} edges)")


if __name__ == "__main__":
    main()
