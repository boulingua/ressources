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
