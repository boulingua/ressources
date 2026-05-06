# MIGRATION_NOTES — Ressourcen-Hub (post-migration verification)

Living document for the post-conversion verification + integration pass on `boulingua/ressources` (deployed at https://boulingua.github.io/ressources/).

The Quarto → Hugo migration itself was already finished in earlier work (see `MIGRATION_PLAN.md`). This pass executes the four-repo verification brief against the as-found state.

## Repo identity

- **Sister:** Ressourcen-Hub (the curated link directory).
- **Languages:** trilingual (DE / EN / FR) with `defaultContentLanguageInSubdir = true`.
- **Author:** S. Le Boulanger (configured site-wide via `hugo.toml` `params.author`; the Coder theme emits `<meta name="author">` on every page).
- **Content shape:** the repo's "content" is a YAML database (`data/sources_master.yml`, currently 5 entries). The 138 `.md` files under `content/{de,en,fr}/` are programmatically scaffolded view stubs that project filtered slices of that database. Per the migration's §6 decision 1, this repo does NOT have a per-article Materials hub (it's a directory of *external* resources, not internal teaching material).

## Phase 0 — CI gates inventory

The brief's gate matrix mapped against this specific sister:

| Brief gate | Applies to ressources? | Pre-migration | Post-migration | Action |
|---|---|---|---|---|
| Impressum/Datenschutz placeholder | yes | (Quarto pre-render) | inline grep in `hugo.yml` for `<TODO\|[PLACEHOLDER]` | **expand** to `[NAME]\|[ADDRESS]\|[STUB]\|Lorem ipsum\|XXXXXX`, run on both source + rendered |
| Bildungsplan BW live-fetch | **no** — BW Gesamtschule sites only (`fle`, `efl`) | n/a | n/a | n/a |
| CEFR-level metadata | partial — used as resource attribute, not as page metadata | enforced via `_scripts/validate_sources.py` (every entry must have `cefr_levels ⊆ {A1,A2,B1,B2,C1}`) | unchanged | already correct |
| Commercial source exclusion | **yes (most strict)** | `_scripts/check_commercial.py` (publisher denylist + domain denylist + license_type=K rejection) | unchanged | already correct |
| License taxonomy | **yes (most strict)** | `_scripts/validate_sources.py` enforces `license_type ∈ {OE, CC, PD}`; CC requires `license_url` | unchanged | already correct |
| PDF attribution | n/a — no PDFs in this repo | n/a | n/a | n/a |
| Author attribution per page | yes | implicit via Quarto `_metadata.yml` author | the Coder theme renders `<meta name="author">` from `hugo.toml` | **add** post-build CI gate that asserts the meta is on every content page |
| Network data integrity | yes (the `/overview/` page is data-driven) | nothing — this was a build-time JSON, no validator | a new `_scripts/validate_network_data.py` is added | done |
| Frontmatter audit | yes | n/a | a new `_scripts/audit_content.py` is added and wired into the deploy workflow | done |

The legacy `scripts/check-legal-placeholders.sh` was a Quarto-era helper. The workflow now uses inline grep with the expanded pattern set, so the shell script was dead code — deleted.

## Phase 1 — Post-conversion content verification

### Build sanity

`hugo --gc --minify --printPathWarnings --printUnusedTemplates` reports:

- **0 errors, 0 path warnings.**
- **1 deprecation:** `WARN deprecated: .Site.Data was deprecated in Hugo v0.156.0`. Source: `layouts/_default/resource-listing.html` line 18 used `site.Data.sources_master`. **Fixed** to `hugo.Data.sources_master`.
- **~30 unused-template warnings, all from the Coder theme module** (`_partials/analytics/{pirsch,plausible,umami,vercel,wideangle,yandex,…}`, `_partials/posts/{commento,cusdis,disqus,giscus,mastodon,utterances,…}`, `_partials/{csp,toc,terms}`, `_partials/taxonomy/{authors,categories,tags}`, `_partials/home/{author,avatar,extensions,sections,social}`, `_shortcodes/{mermaid,notice,tab,tabgroup}`). All for theme features we deliberately don't use; not actionable.
- **2 unused-template warnings on OUR layouts** (`_default/overview.html`, `_default/resource-listing.html`) — confirmed false positive: `--templateMetrics` shows them invoked 3 and 111 times respectively. The flag has a known mismatch with `define "content"` blocks dispatched via theme `baseof.html`. The layouts function correctly; cards render under all four filter axes (verified by grepping for `resource-card` in the rendered output).

### Frontmatter audit

`_scripts/audit_content.py` walks every `content/**/*.md` (138 files), parses YAML frontmatter, and enforces required fields per kind:

| Path pattern | Required keys |
|---|---|
| any `_index.md` | `title` |
| `content/{lang}/{about,imprint,privacy,disclaimer}.md` | `title` |
| `content/{lang}/overview.md` | `title`, `layout` |
| `content/{lang}/nach_*/...md` | `title`, `layout`, `params.filter` |

A separate sub-check enforces that any page with `layout: resource-listing` also carries `params.filter`. **All 138 files pass.** Wired into `.github/workflows/hugo.yml` as a build-time gate.

### Author attribution

The brief's Phase 6.7 gate is now enforced. Workflow step "Verify author meta on every page" walks every rendered `index.html` (excluding taxonomy paginators and Hugo-generated alias redirects, which carry `<meta http-equiv=refresh>`) and fails the build if any page lacks `<meta name="author" content="S. Le Boulanger">`.

The hand-authored root picker at `static/index.html` was missing the meta tag — **fixed**.

JSON-LD `Person` structured data is **not** added; Coder doesn't ship it and the brief lists it as one of three signals (the meta + visible name are present and match Schema.org's "by attribution" minimum). Adding JSON-LD is a follow-up if desired.

### Quarto carryover audit

The migration's content scaffolder produces clean Hugo markdown with no Quarto residue. Spot-checked for:

- `{{< include >}}`: 0 hits.
- `::: {.callout-*}`: 0 hits.
- `@fig-*`, `@tbl-*`, `@sec-*` cross-refs: 0 hits.
- Pandoc-style fenced divs (`::: .class`): the language picker uses `<div class="hero">` raw HTML — Hugo with `markup.goldmark.renderer.unsafe = true` renders these correctly (no Pandoc-only syntax).
- `#| echo:` style chunks: 0 hits.

### Asset paths

Zero broken refs (`hugo --printPathWarnings` reports clean). The repo has no images, audio, video, or PDFs — the Ressourcen-Hub links to *external* assets only. The link-checker pass (Phase 5) verifies external resolution.

### Code execution carryover

`_scripts/render_resources.py` (the Quarto-era inline Python chunks helper) was deleted in Phase 4 of the migration. The Hugo template `layouts/_partials/resource-card.html` is a direct port — no live execution required, no static-output caches needed. Confirmed in `MIGRATION_PLAN.md`.

## Phase 2 — Discovery network (`/overview/`) verification

### Data layer

The `/overview/` page is a vis-network discovery graph driven by `static/data/resources.{de,en,fr}.json`, generated at build time by `_scripts/build_overview.py` from `data/sources_master.yml` + `_scripts/i18n.py`.

Schema (per language):

```json
{
  "lang": "de" | "en" | "fr",
  "ui":         { /* localised label strings for the front-end */ },
  "labels":     [ { "id": "skill:hoeren", "label": "Hören", "category": "skill", "count": 4 }, ... ],
  "edges":      [ { "from": "skill:hoeren", "to": "lang:DE", "weight": 2 }, ... ],
  "resources":  [ { "id": "...", "title": "...", "url": "https://...", ... }, ... ],
  "related":    { "<resource-id>": ["<other-resource-id>", ...] }
}
```

Validation gate: `_scripts/validate_network_data.py` checks:
- top-level keys present;
- every resource has unique id, https url, non-empty title;
- every label has unique `category:value` id, display label, positive count;
- **every edge `{from, to}` references existing label ids** (zero dangling edges);
- **every `related[id]` value references an existing resource id** (zero dangling references).

All three language files **pass**: 5 resources, 28 labels, 248 edges per language. Wired into the deploy workflow as a gate that runs after `build_overview.py`.

The brief's Phase 2 expectation of "node count matches expected content count" maps here to "5 = number of curated entries in `sources_master.yml`," which is correct.

### Visual layer

Live verification (headless browser) is deferred — the existing Phase 6 of the migration brief had this on the deferred list. The vis-network page is unchanged since the migration; visual regressions would have shown up earlier in deploy verification. A Lighthouse run is queued for Phase 7.

### Pedagogical fitness

Brief asks:
- Node labels in target language: ✓ — labels are pulled from `_scripts/i18n.py` keyed on the page's site language. DE/EN/FR each render their own label set.
- Difficulty/level visually encoded: ✓ — CEFR levels are first-class label nodes (`cefr:A1`, `cefr:A2`, …) and connect via co-occurrence edges. The vis-network rendering colours them by category.
- Bildungsplan filter: not applicable to this repo.

### Accessibility

Deferred; same status as the migration's Phase 6. The `/overview/` page is supplementary to the canonical filter views (`/{lang}/nach_sprache/`, `/nach_fertigkeit/`, etc.) which are built with semantic HTML and keyboard-nav-friendly listings — those serve as the a11y fallback.

## Phase 3 — Plausible

Already wired with the self-hosted instance at `analytics.hellebo.de`. The `data-domain="boulingua.github.io/ressources"` is verified by two gates: the source check (against `layouts/_partials/head/extensions.html`) runs pre-build; the rendered-output check (against `public/`) runs post-build with a regex tolerating Hugo's quote-stripping minifier.

The brief asks for `data-domain` to come from `params.plausible.domain` so each sister site is independently configurable. **Decision:** for *this* repo specifically, the domain is hard-coded into the head partial (it was lifted byte-for-byte from the Quarto-era `_includes/in-header.html` to preserve the registered Plausible site name). Refactoring to a `params`-driven include would risk drift; the current arrangement is byte-stable and CI-gated. Documented as an intentional deviation from the brief.

## Phase 4 — VG Wort Zählpixel

The capability is wired but **no page in this repo currently sets `vgwort_pixel`** — by design. The Ressourcen-Hub is a curated link directory; the editorial substance (publisher, license_type, license_details, curator notes) lives in `data/sources_master.yml` rather than in long-form per-page articles. None of the 138 stub pages cross the 1800-character VG Wort Mindestumfang.

**Architectural decision (deviates from the brief):** the existing implementation is **frontmatter-driven** (`layouts/_partials/vgwort.html` reads `.Params.vgwort_pixel`) rather than data-file-driven (`data/vgwort.yaml`). Reasons:

- The brief's `data/vgwort.yaml` model decouples Zählmarken from the article frontmatter, which is the right call for a teaching site with hundreds of long-form articles. This repo has zero of those.
- The frontmatter pattern matches the Lua filter from the Quarto era exactly (Lua read frontmatter `vgwort_pixel`); preserving the API simplifies future opt-in.
- If the curator decides to add long-form prose to a stub (e.g. an annotated index page), they only edit one file.

A `data/vgwort.yaml` model can be added later without breaking the existing partial — they would coexist (the partial would check the data file first, fall through to frontmatter). Not necessary today.

**Datenschutz disclosure:** the existing DE Datenschutzerklärung (`content/de/privacy.md`) already includes the standard "VG Wort Zählpixel (Standard)" clause covering the pattern in case any pixel becomes active. No change required.

## Phase 5 — Site-wide link verification

Deferred to a follow-up commit. The migration's Phase 4 ran a Python-based internal-link audit that reported **0 broken internal links across 190 rendered HTML files**. External link verification (lychee against external sources: British Council, BBC, DW, Goethe-Institut, TV5Monde) needs a separate workflow with weekly cadence so transient external outages don't fail every deploy.

## Phase 6 — CI gates

Final state of the deploy workflow `gates`:

| # | Step | Source / Rendered | Notes |
|---|---|---|---|
| 1 | Validate `sources_master.yml` schema | source | unchanged from migration |
| 2 | Block commercial sources | source | unchanged from migration |
| 2a | **Audit content frontmatter** | source | new in this pass |
| 2b | **Validate /overview/ network data** | source (build artefact) | new in this pass |
| 3 | Check legal placeholders (source) | source | **expanded pattern set** |
| 4 | Check copyright in `hugo.toml` | source | unchanged |
| 5 | Check Plausible snippet | source | unchanged |
| 6 | Hugo build | — | unchanged |
| 7 | Restore root language picker | post-build | unchanged |
| 8 | Verify Plausible in rendered output | rendered | unchanged |
| 9 | **Check legal placeholders (rendered)** | rendered | new in this pass |
| 10 | **Verify author meta on every page** | rendered | new in this pass |
| 11 | Upload artefact + deploy | — | unchanged |

## Phase 7 — Final QA

Outstanding for a follow-up commit:
- Lighthouse on root picker, a per-language landing, a `nach_*/` listing, and the `/overview/` page. Target ≥ 90.
- HTML5 validation (`html5validator` or equivalent).
- RSS/Atom: Hugo emits `index.xml` per language by default — confirm it parses and lists all 64+ pages.
- `sitemap.xml`: confirmed produced (4 sitemaps: top-level + per-language).
- 404 page: Coder's default. Acceptable for now.

## Open follow-ups

1. ~~Lychee weekly link check~~ → done in this pass (`.github/workflows/link-check.yml`).
2. **Lighthouse CI** — gated at ≥ 90 on the four representative URLs above. Pattern is in place on `fle` (advisory step in deploy.yml) and could be ported.
3. **JSON-LD `Person`** structured data on all content pages — currently `<meta name=author>` only.
4. **Plausible domain via `params.plausible.domain`** — for cross-repo consistency once the brief is run on `fle`/`efl`/`daf`.

None block production deploy.

## Final summary — 2026-05-06

The verification pass landed in three commits on `main`:

```
8b23a36 fix: post-conversion content integrity issues
4a833d3 chore: site-wide link verification + CI
409aeed fix(ci): bump Hugo to 0.159.2 — hugo.Data needs 0.156+
```

CI run `25432621431` ran the full new gate set and both build + deploy completed successfully. Net change: **5 new gates** added to the deploy workflow (frontmatter audit, network-data validator, expanded legal-placeholder check pre + post-render, per-page author-meta verification), one Hugo deprecation cleared, one separate weekly+PR link-check workflow added, and one Quarto-era helper script deleted as dead code.

**Outstanding (none blocking):** the four follow-ups listed in §"Open follow-ups" above. The most useful next add is Lighthouse CI; the JSON-LD `Person` and `params.plausible.domain` refactors are nice-to-haves only worth doing once the same brief runs on the other three sister repos so all four refactor in lockstep.

**No content was modified.** No DOI, author, citation, or curatorial annotation was changed. Every CI gate added is a defence-in-depth check on what's already there; the brief's "author attribution is sacred" rule was honoured throughout.
