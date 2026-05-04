"""Rendering-Helfer fuer Ressourcen-Karten (mehrsprachig).

Wird von allen View-Seiten via Python-Chunk importiert.
Sprachparameter `lang` steuert die UI-Texte (Badge-Labels,
"Passt zu:", "Letzter Link-Check:" usw.) sowie die Auswahl
der lokalisierten Beschreibungs-Felder
(description_en / description_fr / curator_notes_en / ...).
"""
from __future__ import annotations

import html
from pathlib import Path

import yaml
from IPython.display import HTML, display

from i18n import skill_label, t

MASTER_PATH = Path(__file__).resolve().parent.parent / "_resources" / "sources_master.yml"


def load_resources():
    with MASTER_PATH.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or []


def filter_resources(resources, language=None, skill=None,
                     cefr_level=None, unit_prefix=None):
    results = resources
    if language:
        results = [r for r in results if r.get("language") == language]
    if skill:
        results = [r for r in results if skill in (r.get("skills") or [])]
    if cefr_level:
        results = [r for r in results if cefr_level in (r.get("cefr_levels") or [])]
    if unit_prefix:
        results = [
            r for r in results
            if any((u or "").startswith(unit_prefix)
                   for u in (r.get("applicable_units") or []))
        ]
    return sorted(
        results,
        key=lambda r: (
            r.get("language", ""),
            (r.get("cefr_levels") or [""])[0],
            r.get("title", ""),
        ),
    )


def _esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def _localized(r: dict, base_field: str, lang: str) -> str:
    """Suche description_en / description_fr; falls fehlend, deutsche Fassung."""
    if lang in ("en", "fr"):
        suffixed = r.get(f"{base_field}_{lang}")
        if suffixed:
            return suffixed
    return r.get(base_field, "")


def render_card(r: dict, lang: str = "de") -> str:
    type_code = r.get("license_type", "")
    badges = (
        f'<span class="type-badge type-{type_code.lower()}">{_esc(type_code)}</span>'
        f'<span class="lang-badge">{_esc(r.get("language", ""))}</span>'
    )
    for lvl in r.get("cefr_levels") or []:
        badges += f'<span class="cefr-badge cefr-{lvl.lower()}">{_esc(lvl)}</span>'
    for sk in r.get("skills") or []:
        badges += f'<span class="skill-badge">{_esc(skill_label(sk, lang))}</span>'

    units_html = ""
    if r.get("applicable_units"):
        units_html = (
            f'<p class="resource-units"><strong>{t("passt_zu", lang)}</strong> '
            + _esc(", ".join(r["applicable_units"])) + "</p>"
        )

    notes = _localized(r, "curator_notes", lang)
    notes_html = (
        f'<p class="resource-notes"><em>{_esc(notes).strip()}</em></p>'
        if notes else ""
    )

    description = _localized(r, "description", lang)
    open_label = t("ressource_open", lang)
    last_check = t("letzter_check", lang)

    return f"""
<div class="resource-card">
  <h3>{_esc(r.get('title'))}</h3>
  <p class="resource-publisher">
    {_esc(r.get('publisher'))} ·
    <a href="{_esc(r.get('url'))}">{open_label}</a>
  </p>
  <div class="resource-badges">{badges}</div>
  <p class="resource-description">{_esc(description).strip()}</p>
  {units_html}
  {notes_html}
  <p class="resource-checked">
    {last_check} {_esc(r.get('last_checked'))}
  </p>
</div>
""".strip()


def render_filtered(language=None, skill=None,
                    cefr_level=None, unit_prefix=None,
                    lang: str = "de"):
    resources = load_resources()
    filtered = filter_resources(
        resources, language=language, skill=skill,
        cefr_level=cefr_level, unit_prefix=unit_prefix,
    )
    if not filtered:
        display(HTML(
            f'<p class="no-resources">{t("no_resources", lang)}</p>'
        ))
        return
    display(HTML("\n".join(render_card(r, lang) for r in filtered)))
