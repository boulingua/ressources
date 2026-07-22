#!/usr/bin/env bash
#
# verify-media-links.sh — periodic link-checker for resources/media-registry.yml
#
# Walks every entry in the media registry, issues a HEAD/GET request per URL and
# classifies the result. Intended for periodic re-validation (e.g. quarterly or
# in CI), not one-shot research.
#
# Classification:
#   ok        2xx / 3xx            — live (redirects followed)
#   protected 401 / 403 / 429 / 5xx — up but bot-protected, rate-limited, or a
#                                     transient/server-side error; NOT dead,
#                                     needs a manual/browser check before trusting
#   dead      404 / 410 / other 4xx — broken; fix the URL or drop the entry
#   unreach   000 / timeout        — DNS failure, TLS error, or no response
#                                     (if DNS resolves, usually a datacenter-IP /
#                                     geo block rather than genuine breakage)
#
# Exit status: number of `dead` links (0 = all resolvable). `protected` and
# `unreach` are reported but do NOT fail the run, since they routinely reflect
# anti-bot / geo measures rather than genuine breakage. Pass --strict to also
# fail on `unreach`.
#
# Usage:
#   scripts/verify-media-links.sh                 # check the default registry
#   scripts/verify-media-links.sh path/to.yml     # check a specific file
#   scripts/verify-media-links.sh --strict        # also fail on unreachable
#   FILTER=fr scripts/verify-media-links.sh        # only ids/urls matching FILTER

set -uo pipefail

STRICT=0
REGISTRY=""
for arg in "$@"; do
  case "$arg" in
    --strict) STRICT=1 ;;
    *) REGISTRY="$arg" ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REGISTRY="${REGISTRY:-$ROOT/resources/media-registry.yml}"
FILTER="${FILTER:-}"
TIMEOUT="${TIMEOUT:-25}"
UA="Mozilla/5.0 (compatible; boulingua-link-check/1.0)"

if [[ ! -f "$REGISTRY" ]]; then
  echo "error: registry not found: $REGISTRY" >&2
  exit 2
fi

# Colour only when writing to a terminal.
if [[ -t 1 ]]; then
  C_OK=$'\033[32m'; C_WARN=$'\033[33m'; C_BAD=$'\033[31m'; C_DIM=$'\033[2m'; C_RST=$'\033[0m'
else
  C_OK=""; C_WARN=""; C_BAD=""; C_DIM=""; C_RST=""
fi

# Extract "id<TAB>url" for every entry. Prefer a real YAML parse (matches the
# repo's other tooling which relies on PyYAML); fall back to grep if python is
# unavailable.
extract() {
  if command -v python3 >/dev/null 2>&1; then
    python3 - "$REGISTRY" <<'PY'
import sys, yaml
with open(sys.argv[1], encoding="utf-8") as fh:
    data = yaml.safe_load(fh) or []
for e in data:
    if isinstance(e, dict) and e.get("url"):
        print(f"{e.get('id','?')}\t{e['url']}")
PY
  else
    # Fallback: assumes one `id:` then a later `url:` per entry block.
    awk '
      /^- +id:/         { id=$0; sub(/^- +id: */,"",id); gsub(/"/,"",id) }
      /^[[:space:]]+id:/{ id=$0; sub(/^[[:space:]]+id: */,"",id); gsub(/"/,"",id) }
      /^[[:space:]]+url:/{ u=$0; sub(/^[[:space:]]+url: */,"",u); gsub(/"/,"",u); print id "\t" u }
    ' "$REGISTRY"
  fi
}

n_ok=0; n_protected=0; n_dead=0; n_unreach=0; n_total=0
dead_list=(); unreach_list=(); protected_list=()

echo "Checking links in: ${REGISTRY#$ROOT/}"
[[ -n "$FILTER" ]] && echo "Filter: $FILTER"
echo

while IFS=$'\t' read -r id url; do
  [[ -z "${url:-}" ]] && continue
  if [[ -n "$FILTER" && "$id$url" != *"$FILTER"* ]]; then continue; fi
  n_total=$((n_total+1))

  # Try HEAD first; some servers reject HEAD, so fall back to a bodyless GET.
  code=$(curl -sS -o /dev/null -A "$UA" -w '%{http_code}' -I -L --max-time "$TIMEOUT" "$url" 2>/dev/null)
  if [[ "$code" == "000" || "$code" == "405" || "$code" == "501" ]]; then
    code=$(curl -sS -o /dev/null -A "$UA" -w '%{http_code}' -r 0-0 -L --max-time "$TIMEOUT" "$url" 2>/dev/null)
  fi

  case "$code" in
    2*|3*)           tag="${C_OK}ok       ${C_RST}"; n_ok=$((n_ok+1)) ;;
    401|403|429|5*)  tag="${C_WARN}protected${C_RST}"; n_protected=$((n_protected+1)); protected_list+=("$id ($code) $url") ;;
    000)             tag="${C_BAD}unreach  ${C_RST}"; n_unreach=$((n_unreach+1)); unreach_list+=("$id $url") ;;
    *)               tag="${C_BAD}dead     ${C_RST}"; n_dead=$((n_dead+1)); dead_list+=("$id ($code) $url") ;;
  esac
  printf '%s %s %-30s %s%s%s\n' "$tag" "$code" "$id" "$C_DIM" "$url" "$C_RST"
done < <(extract)

echo
echo "── summary ─────────────────────────────────"
printf '  total     %d\n' "$n_total"
printf '  %sok        %d%s\n' "$C_OK" "$n_ok" "$C_RST"
printf '  %sprotected %d%s  (up but bot-protected/rate-limited/5xx — verify manually)\n' "$C_WARN" "$n_protected" "$C_RST"
printf '  %sunreach   %d%s  (no response / DNS / TLS — often a geo/datacenter block)\n' "$C_BAD" "$n_unreach" "$C_RST"
printf '  %sdead      %d%s\n' "$C_BAD" "$n_dead" "$C_RST"

if (( n_dead > 0 )); then
  echo; echo "Dead links:"; printf '  - %s\n' "${dead_list[@]}"
fi
if (( n_unreach > 0 )); then
  echo; echo "Unreachable:"; printf '  - %s\n' "${unreach_list[@]}"
fi

exit_code=$n_dead
(( STRICT == 1 )) && exit_code=$((n_dead + n_unreach))
exit "$exit_code"
