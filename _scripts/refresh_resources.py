#!/usr/bin/env python3
"""Idempotent (re-)acquisition of the open-licensed resource cache.

Driven by ``resources/registry.yml``. Only entries that carry a committed
``downloads:`` list (concrete file URLs + expected SHA-256) are fetched — these
are exactly the openly-licensed, redistributable sources. Everything else in the
registry is link-only and is never downloaded.

Idempotent: a file is fetched only if it is missing or its SHA-256 no longer
matches the value committed in the registry. Re-running after a clone rebuilds
``resources/_downloads/`` byte-for-byte and re-verifies integrity.

Usage:
    python _scripts/refresh_resources.py [--dry-run] [--force] [--only ID] [--rate 2.0]

Requires: pyyaml.
"""
from __future__ import annotations
import argparse, hashlib, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "resources", "registry.yml")
DL = os.path.join(ROOT, "resources", "_downloads")
UA = ("Mozilla/5.0 (X11; Linux x86_64) boulingua-resource-bot/0.1 "
      "(+https://boulingua.github.io/ressources; local study cache)")
# Licences we are willing to write to disk. Reserved-rights material stays
# link-only regardless of free-to-access status.
OPEN_LICENCES = ("public-domain", "cc0", "cc-by", "cc-by-sa", "cc-by-nc",
                 "cc-by-nc-sa", "cc-by-nd", "open-access")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def is_open(licence: str) -> bool:
    lic = (licence or "").strip().lower()
    return any(lic.startswith(p) for p in OPEN_LICENCES)


def fetch(url: str, dest: str, timeout: int = 60) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    h = hashlib.sha256(); n = 0
    with urllib.request.urlopen(req, timeout=timeout) as r, open(tmp, "wb") as f:
        while True:
            chunk = r.read(65536)
            if not chunk:
                break
            n += len(chunk); h.update(chunk); f.write(chunk)
    os.replace(tmp, dest)
    return n, h.hexdigest()


def load_registry() -> list:
    try:
        import yaml
    except ImportError:
        sys.exit("error: pyyaml is required — pip install pyyaml")
    with open(REGISTRY, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="show what would happen; fetch nothing")
    ap.add_argument("--force", action="store_true", help="re-fetch even if the local hash matches")
    ap.add_argument("--only", metavar="ID", help="restrict to a single registry id")
    ap.add_argument("--rate", type=float, default=2.0, help="seconds to wait between network fetches (default 2)")
    args = ap.parse_args()

    entries = load_registry()
    fetchable = [e for e in entries if e.get("downloads")]
    if args.only:
        fetchable = [e for e in fetchable if e.get("id") == args.only]

    tot_new = tot_skip = tot_fail = tot_bytes = 0
    for e in fetchable:
        sid, lang = e.get("id"), e.get("language")
        if not is_open(e.get("licence", "")) and not e.get("redistributable"):
            print(f"[skip] {sid}: not openly licensed — link-only, refusing to download")
            continue
        print(f"\n== {sid} ({lang}) — {e.get('source','')} ==")
        got = []
        for d in e["downloads"]:
            url, rel, want = d["url"], d["path"], d.get("sha256")
            dest = os.path.join(ROOT, rel)
            name = os.path.basename(rel)
            if os.path.exists(dest) and want and not args.force and sha256_file(dest) == want:
                print(f"  skip  {name} (unchanged)"); tot_skip += 1
                got.append((dest, want, lang)); continue
            if args.dry_run:
                print(f"  fetch {name}  <-  {url}  (dry-run)"); continue
            try:
                n, sha = fetch(url, dest)
            except Exception as exc:
                print(f"  FAIL  {name}: {exc}"); tot_fail += 1; continue
            if want and sha != want:
                print(f"  WARN  {name}: sha256 mismatch (registry {want[:12]} != got {sha[:12]}) — kept, verify source")
            print(f"  new   {name}  {n}B  {sha[:12]}"); tot_new += 1; tot_bytes += n
            got.append((dest, sha, lang))
            time.sleep(args.rate)  # be polite to servers
        # regenerate the local (gitignored) sha256 manifest for this source
        if got and not args.dry_run:
            man = os.path.join(DL, lang, "metadata", f"{sid}.sha256")
            os.makedirs(os.path.dirname(man), exist_ok=True)
            with open(man, "w") as f:
                for dest, sha, lg in got:
                    f.write(f"{sha}  {os.path.relpath(dest, os.path.join(DL, lg))}\n")

    print(f"\nsummary: {tot_new} fetched, {tot_skip} unchanged, {tot_fail} failed, "
          f"{tot_bytes} new bytes across {len(fetchable)} fetchable source(s).")
    return 1 if tot_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
