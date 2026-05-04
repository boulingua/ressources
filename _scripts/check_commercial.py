#!/usr/bin/env python3
"""Blockiert kommerzielle Anbieter im Ressourcen-Hub.

Prueft sources_master.yml gegen hartcodierte Listen von verbotenen
Verlagen, Plattformen und Domains. Exit 1 bei jedem Treffer.
"""
from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "_resources" / "sources_master.yml"

FORBIDDEN_PUBLISHERS = [
    "klett", "cornelsen", "hueber", "schubert verlag", "pons",
    "oxford university press", "cambridge university press",
    "hachette", "cle international", "didier", "langenscheidt",
    "duden", "ernst klett",
    "babbel", "duolingo", "busuu", "lingoda", "mango languages",
    "rosetta stone", "mondly", "preply", "italki",
    "teachers pay teachers", "lehrer-online", "eduki",
    "lehrermarktplatz",
]

FORBIDDEN_DOMAINS = [
    "klett.de", "klett-sprachen.de", "cornelsen.de", "hueber.de",
    "schubert-verlag.de", "pons.com", "oup.com", "cambridge.org",
    "hachette.fr", "cle-international.com", "editionsdidier.com",
    "babbel.com", "duolingo.com", "busuu.com", "lingoda.com",
    "mangolanguages.com", "rosettastone.com", "mondly.com",
    "preply.com", "teacherspayteachers.com", "lehrer-online.de",
    "eduki.com", "lehrermarktplatz.de", "langenscheidt.com",
]


def domain_matches(host: str, forbidden: str) -> bool:
    host = host.lower().lstrip(".")
    return host == forbidden or host.endswith("." + forbidden)


def check() -> int:
    if not MASTER.exists():
        print(f"::error::Datei fehlt: {MASTER}", file=sys.stderr)
        return 1

    with MASTER.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []

    hits: list[str] = []

    for r in data:
        if not isinstance(r, dict):
            continue
        rid = r.get("id", "<unknown>")

        if r.get("license_type") == "K":
            hits.append(f"[{rid}] license_type=K ist verboten.")

        publisher = (r.get("publisher") or "").lower()
        for bad in FORBIDDEN_PUBLISHERS:
            if bad in publisher:
                hits.append(f"[{rid}] verbotener Publisher: '{r.get('publisher')}' enthaelt '{bad}'.")

        url = r.get("url") or ""
        try:
            host = urlparse(url).hostname or ""
        except ValueError:
            host = ""
        for bad in FORBIDDEN_DOMAINS:
            if domain_matches(host, bad):
                hits.append(f"[{rid}] verbotene Domain: {host} ({bad}).")

    if hits:
        for h in hits:
            print(f"::error::{h}", file=sys.stderr)
        print(f"\n{len(hits)} kommerzielle Verstoesse.", file=sys.stderr)
        return 1

    print(f"OK - {len(data)} Ressourcen, keine kommerziellen Anbieter.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
