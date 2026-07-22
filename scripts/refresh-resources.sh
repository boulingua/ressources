#!/usr/bin/env bash
#
# refresh-resources.sh — idempotent (re-)build of the local, non-redistributable
# resource cache under resources/_downloads/, driven by resources/registry.yml.
#
# Only openly-licensed sources (public-domain / CC*) that carry a committed
# `downloads:` list in the registry are fetched; a file is downloaded only when
# it is missing or its SHA-256 no longer matches the committed value. Reserved-
# rights ("all-rights-reserved") sources are catalogued in the registry but are
# NEVER downloaded — the site links to them instead ("verlinkbar, nicht kopierbar").
#
# Usage:
#   scripts/refresh-resources.sh              # fetch missing/changed open files
#   scripts/refresh-resources.sh --dry-run    # show what would happen
#   scripts/refresh-resources.sh --only ID    # a single source
#   scripts/refresh-resources.sh --force      # re-fetch everything
#
# Requires: python3 + pyyaml  (pip install pyyaml)
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$here"

if ! command -v python3 >/dev/null 2>&1; then
  echo "error: python3 not found" >&2
  exit 1
fi
if ! python3 -c 'import yaml' 2>/dev/null; then
  echo "error: pyyaml not installed — run: pip install pyyaml" >&2
  exit 1
fi
if [ ! -f resources/registry.yml ]; then
  echo "error: resources/registry.yml not found" >&2
  exit 1
fi

exec python3 _scripts/refresh_resources.py "$@"
