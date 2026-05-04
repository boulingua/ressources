#!/usr/bin/env python3
"""Schema-Validator fuer _resources/sources_master.yml.

Prueft Pflichtfelder, Wertebereiche und Eindeutigkeit.
Exit 1 bei jedem Fehler.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "_resources" / "sources_master.yml"

REQUIRED = [
    "id", "title", "publisher", "url", "language",
    "license_type", "license_details", "cefr_levels",
    "skills", "description", "last_checked",
]

LANGUAGES = {"EN", "FR", "DE"}
LICENSE_TYPES = {"OE", "CC", "PD"}
CEFR = {"A1", "A2", "B1", "B2", "C1"}
SKILLS = {
    "hoeren", "lesen", "schreiben", "sprechen",
    "grammatik", "wortschatz", "landeskunde",
}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def err(rid: str, msg: str, errors: list) -> None:
    errors.append(f"[{rid}] {msg}")


def validate() -> int:
    if not MASTER.exists():
        print(f"::error::Datei fehlt: {MASTER}", file=sys.stderr)
        return 1

    with MASTER.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []

    if not isinstance(data, list):
        print("::error::sources_master.yml muss eine Liste sein.", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen_ids: set[str] = set()

    for i, r in enumerate(data):
        rid = r.get("id", f"<index {i}>") if isinstance(r, dict) else f"<index {i}>"

        if not isinstance(r, dict):
            err(rid, "Eintrag ist kein Objekt.", errors)
            continue

        for field in REQUIRED:
            if field not in r or r[field] in (None, "", []):
                err(rid, f"Pflichtfeld fehlt oder leer: {field}", errors)

        if "id" in r:
            if not isinstance(r["id"], str) or not ID_RE.match(r["id"]):
                err(rid, "id ist nicht kebab-case (a-z, 0-9, -).", errors)
            elif r["id"] in seen_ids:
                err(rid, "id ist nicht eindeutig.", errors)
            else:
                seen_ids.add(r["id"])

        if r.get("language") not in LANGUAGES:
            err(rid, f"language muss eines von {sorted(LANGUAGES)} sein.", errors)

        lt = r.get("license_type")
        if lt not in LICENSE_TYPES:
            err(rid, f"license_type muss eines von {sorted(LICENSE_TYPES)} sein (kein K).", errors)
        if lt == "CC" and not r.get("license_url"):
            err(rid, "Bei license_type=CC ist license_url Pflicht.", errors)

        levels = r.get("cefr_levels") or []
        if not isinstance(levels, list) or not levels:
            err(rid, "cefr_levels muss eine nicht-leere Liste sein.", errors)
        else:
            for lvl in levels:
                if lvl not in CEFR:
                    err(rid, f"Ungueltiges CEFR-Niveau: {lvl}", errors)

        skills = r.get("skills") or []
        if not isinstance(skills, list) or not skills:
            err(rid, "skills muss eine nicht-leere Liste sein.", errors)
        else:
            for sk in skills:
                if sk not in SKILLS:
                    err(rid, f"Ungueltiger Skill: {sk}", errors)

        url = r.get("url", "")
        if not isinstance(url, str) or not url.startswith("https://"):
            err(rid, "url muss mit https:// beginnen.", errors)

        lc = r.get("last_checked")
        if isinstance(lc, date):
            pass
        elif isinstance(lc, str):
            try:
                date.fromisoformat(lc)
            except ValueError:
                err(rid, f"last_checked ist kein ISO-Datum: {lc}", errors)
        else:
            err(rid, "last_checked fehlt oder hat falschen Typ.", errors)

    if errors:
        for e in errors:
            print(f"::error::{e}", file=sys.stderr)
        print(f"\n{len(errors)} Fehler in sources_master.yml.", file=sys.stderr)
        return 1

    print(f"OK - {len(data)} Ressourcen, Schema gueltig.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
