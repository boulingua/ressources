#!/usr/bin/env python3
"""Validate the /overview/ discovery-network JSON files.

Checks each static/data/resources.{de,en,fr}.json produced by
_scripts/build_overview.py for:

  - Top-level keys: lang, ui, labels, edges, resources, related.
  - resources: every entry has unique id, https url, non-empty title.
  - labels: every entry has unique id ("category:value"), display
    label, category, count > 0.
  - edges: every {from, to} references existing label ids — zero
    dangling edges.
  - related: every value in each related[rid] list references an
    existing resource id — zero dangling references.

Exit 1 on any violation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "static" / "data"
LANGS = ("de", "en", "fr")


def fail(errors: list[str]) -> int:
    for e in errors:
        print(f"::error::{e}", file=sys.stderr)
    print(f"\n{len(errors)} error(s) in static/data/resources.*.json",
          file=sys.stderr)
    return 1


def validate_one(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path.name}: file missing"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{path.name}: invalid JSON ({e})"]

    for key in ("lang", "ui", "labels", "edges", "resources", "related"):
        if key not in data:
            errors.append(f"{path.name}: missing top-level key '{key}'")

    # ----- resources -----
    res_ids: set[str] = set()
    for r in data.get("resources", []):
        rid = r.get("id")
        if not rid:
            errors.append(f"{path.name}: resource missing id")
            continue
        if rid in res_ids:
            errors.append(f"{path.name}: duplicate resource id '{rid}'")
        res_ids.add(rid)
        if not (r.get("title") or "").strip():
            errors.append(f"{path.name}: resource '{rid}' has empty title")
        url = r.get("url") or ""
        if not url.startswith("https://"):
            errors.append(f"{path.name}: resource '{rid}' url is not https: {url!r}")

    # ----- labels -----
    lbl_ids: set[str] = set()
    for lbl in data.get("labels", []):
        lid = lbl.get("id")
        if not lid:
            errors.append(f"{path.name}: label missing id")
            continue
        if lid in lbl_ids:
            errors.append(f"{path.name}: duplicate label id '{lid}'")
        lbl_ids.add(lid)
        if ":" not in lid:
            errors.append(f"{path.name}: label id '{lid}' is not 'category:value' shape")
        if not (lbl.get("label") or "").strip():
            errors.append(f"{path.name}: label '{lid}' has empty display label")
        if not isinstance(lbl.get("count"), int) or lbl.get("count", 0) <= 0:
            errors.append(f"{path.name}: label '{lid}' count is not a positive int")

    # ----- edges -----
    for i, e in enumerate(data.get("edges", [])):
        a, b = e.get("from"), e.get("to")
        if not a or not b:
            errors.append(f"{path.name}: edge[{i}] missing from/to")
            continue
        if a not in lbl_ids:
            errors.append(f"{path.name}: edge[{i}] references unknown label '{a}'")
        if b not in lbl_ids:
            errors.append(f"{path.name}: edge[{i}] references unknown label '{b}'")

    # ----- related -----
    related = data.get("related", {})
    if isinstance(related, dict):
        for rid, suggestions in related.items():
            if rid not in res_ids:
                errors.append(f"{path.name}: related[{rid!r}] keyed by unknown resource")
            if not isinstance(suggestions, list):
                errors.append(f"{path.name}: related[{rid!r}] is not a list")
                continue
            for s in suggestions:
                if s not in res_ids:
                    errors.append(f"{path.name}: related[{rid!r}] points to unknown resource '{s}'")
    return errors


def main() -> int:
    if not DATA_DIR.exists():
        print("::error::static/data/ does not exist — run "
              "_scripts/build_overview.py first.", file=sys.stderr)
        return 1
    all_errors: list[str] = []
    counts = {}
    for lang in LANGS:
        path = DATA_DIR / f"resources.{lang}.json"
        errs = validate_one(path)
        all_errors.extend(errs)
        if not errs:
            data = json.loads(path.read_text(encoding="utf-8"))
            counts[lang] = (len(data.get("resources", [])),
                            len(data.get("labels", [])),
                            len(data.get("edges", [])))
    if all_errors:
        return fail(all_errors)
    for lang, (nr, nl, ne) in counts.items():
        print(f"OK - resources.{lang}.json: "
              f"{nr} resources, {nl} labels, {ne} edges")
    return 0


if __name__ == "__main__":
    sys.exit(main())
