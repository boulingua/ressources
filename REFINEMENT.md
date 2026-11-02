# Refinement record — 30 October 2026

This is a local engineering candidate on `refine/2026-10-30`. No hosted CI,
published release or production deployment of these changes has been observed.
The suite strategy and integration order live in the organisation repository,
`docs/refinement-2026-10-30.md` and `docs/release-candidate-2026-10-30.md`.

## Findings, implementation and verification

The catalogue contains 48 resources, 38 discovery labels and 439 network edges in German, English and French.

- High: project-prefix fetches and external graph dependencies made discovery fragile. The graph library is now pinned, installed through the lockfile, fingerprinted and served locally; it loads only when requested. Failed fetches are visible.
- Medium: derived discovery data could be stale without failing validation. `build_overview.py --check` is read-only and compares the generated data with the source. New kit gate A22 runs schema, source-policy, derived-data and network checks for catalogue repositories.
- Medium: contrast, control state and small text impaired use. Semantic design tokens, pressed/expanded states, keyboard-operable controls and readable graph labels now cover the discovery view.

Strict Hugo build and the complete local gate battery passed after the final graph-label adjustment. The advisory C4 registration warning remains; no counting mark was invented. Real browser journeys exercise all three language overviews, filtering 48 entries down to a subset, resetting, expanding details and loading the graph on request. No third-party licence grant or link availability is inferred from a passing structural check; the scheduled link workflow reports external link failures separately.

README.md gives exact dependency installation, catalogue validation, build and preview commands. Next: review the catalogue/source policies, publish a compatible platform/workflow set, then observe hosted CI and deployment. No deployment has been performed.


## Analytics notice consistency — 31 October 2026

Plausible remains disabled. The privacy notice explicitly says so; copied claims of active Plausible collection were removed. This does not remove or make claims about separately documented hosting or other services.

Privacy pages declare their analytics policy, language and built URL. New kit gate C9 checks actual HTML scripts and visible notices against configuration; it rejects missing, duplicate or mismatched scripts and contradictory notices. Six gate regressions and three scaffold tests passed. Representative strict builds/C9 passed for website, nsf, nvt, gfl, Scriptlibrary and all three resource-hub notice languages; the suite integration run verifies the remaining sites. This is configuration/content evidence, not certification of the remote server or legal compliance.


## Explicit release dependencies — 31 October 2026

The shared workflow caller now names the same immutable org commit in `uses` and
`org_ref`; `release-pins.json` records the actual historical kit/framework pins.
These historical pins are explicitly not the remediated release. The new org
workflow rejects absent/malformed versions, mismatched source commits and schema
bytes, and nonconforming course manifests; hubs pin dependencies without claiming
course conformance. The coordinated updater prepares exact published foundation
sets, updates consumers/checksums together and retains rollback inputs. Separate
read-only candidate CI can validate immutable pre-release commits without release
tags or deployment rights. Hosted execution and new foundation publication remain
unobserved. See the org `docs/release-pins.md`.


## Local verification — 2 November 2026

The strict candidate-kit Hugo build and complete configured gate battery passed
locally. Declined gates, warning ramps and external checks remain listed in the
battery output; this is not hosted CI or deployment evidence. The historical
release pins have not been promoted to new foundation releases.
