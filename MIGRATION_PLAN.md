# Migration Plan — `boulingua/ressources` → Hugo + Coder

**Branch target:** `migration/hugo-coder` (not yet created)
**Author identity for all commits:** `s-leboulanger <277736839+s-leboulanger@users.noreply.github.com>`
**Plan author:** Phase 0 — orientation only, no code changes, no commits.

---

## 0. Headline finding (read this first)

This repo is **not** a hand-authored Quarto site. It is a **YAML-driven generator**:

- The single source of content truth is `_resources/sources_master.yml` — a curated database of external resources (currently **5 entries**).
- `_scripts/build_pages.py` runs as a Quarto **pre-render** step and emits the entire trilingual `de/`, `en/`, `fr/` `.qmd` tree on the fly. None of those `.qmd` files live in git.
- `_scripts/build_overview.py` produces `assets/data/resources.{de,en,fr}.json` consumed by an interactive vis-network graph on the `/overview` page.
- `_scripts/render_resources.py` is imported by Python code chunks inside the generated `.qmd` files; it filters and renders resource cards as HTML.
- All UI strings live in `_scripts/i18n.py`.

**Implication for the prompt's instructions:**

| Prompt instruction | Applies here? |
|---|---|
| Inventory every `.qmd`, copy each one to `.md` | **No** — only `index.qmd` is hand-authored. The rest is generated. |
| Per-file word-count diff after conversion | **No** — there are no per-file canonical sources to diff against. The canonical content is the YAML. |
| Materials hub: Presentations + Worksheets, per-article `.pptx`/`.pdf` placeholders | **No** — `ressources` is a curated link directory, not a unit-based teaching site. The other three sister repos (`fle`, `efl`, `daf`) have units; this one *points at* their units. There are no "articles" to attach materials to. |
| Plausible Analytics preservation | **Yes** — currently in `_includes/in-header.html`, self-hosted at `analytics.hellebo.de`. |
| VG Wort Zählpixel preservation | **Conditionally yes** — implementation exists (`_scripts/vgwort.lua`, reads `vgwort_pixel` from frontmatter), but **no page in this repo currently sets `vgwort_pixel`**. Manifest will be empty. |

→ **Decisions needed from you before Phase 1.** See §6.

---

## 1. Repo identity & tracking inventory

- **Repo:** `https://github.com/boulingua/ressources.git` (origin/main, clean tree at start)
- **Site title:** `#ressources`
- **Site URL:** `https://boulingua.github.io/ressources/`
- **Languages:** trilingual (DE / EN / FR) — language picker at root, `/de/`, `/en/`, `/fr/` subtrees
- **Author / Imprint identity:** S. Le Boulanger, Albert-Einstein-Straße 47, 02977 Hoyerswerda, DE
- **Current deploy:** GitHub Pages via `actions/upload-pages-artifact` + `actions/deploy-pages` (single workflow, on push to `main`)

### Plausible (in use)

```html
<script defer
        data-domain="boulingua.github.io/ressources"
        src="https://analytics.hellebo.de/js/script.file-downloads.outbound-links.js"></script>
<script>window.plausible = window.plausible || function() {
  (window.plausible.q = window.plausible.q || []).push(arguments) }</script>
```

Loaded via `_quarto.yml` → `format.html.include-in-header: _includes/in-header.html`. Tracks file downloads + outbound links. Self-hosted in DE (named in `de/privacy.qmd` text). **Must port verbatim** — do not change `data-domain`, the script `src`, or any attribute.

### VG Wort

- **Filter:** `_scripts/vgwort.lua` — emits a 1×1 invisible `<img>` from `vgwort_pixel` frontmatter (full URL, partial host+path, or bare 32-hex token defaulting to `vg08.met.vgwort.de/na/`).
- **Wired in:** `_quarto.yml` → `filters: [_scripts/vgwort.lua]`.
- **Currently used by:** **zero pages.** Grep across the repo for `vgwort_pixel` / `vgwort-pixel` returns matches only inside the Lua filter and inside `de/privacy.qmd`'s informational text. The build_pages.py generators do **not** set the key on any generated page.
- **Manifest (`vgwort-manifest.csv`) — to be committed in Phase 0.5 if you approve:** zero rows, but the equivalent Hugo capability must still be ported (a Hugo partial that reads `.Params.vgwort_pixel` and renders the same `<img>`), so the existing `de/privacy.qmd` description remains accurate and so a future article that opts in works without further plumbing.

---

## 2. Inventory

### 2.1 Hand-authored content (everything that lives in git)

| Path | Type | Notes |
|---|---|---|
| `index.qmd` | Quarto page | Trilingual language-picker landing page using `.hero`, `.kicker`, `.card-grid`, `.entry-card` Quarto fenced divs. ~30 lines. |
| `_quarto.yml` | Quarto config | navbar, footer, theme (flatly/darkly + custom SCSS), pre-render hooks, vgwort filter. |
| `_metadata.yml` | Quarto metadata | sets `author: "S. Le Boulanger"`. |
| `_resources/sources_master.yml` | **Content database** | 5 entries × ~25 fields each (id, title, publisher, url, language, license_type, license_details, cefr_levels, skills, media_types, description{,_en,_fr}, applicable_units, curator_notes{,_en,_fr}, target_age, last_checked). |
| `_scripts/build_pages.py` | Generator | 862 lines. Emits all `de/`, `en/`, `fr/` `.qmd` files including landing, overview, about, imprint, privacy, disclaimer, by-language, by-skill, by-level, and by-unit (EFL kl5–13, FLE kl6–13, DaF a1–c1) views. |
| `_scripts/i18n.py` | Generator | 273 lines. Single source of truth for all UI strings in DE/EN/FR. |
| `_scripts/render_resources.py` | Runtime helper | 124 lines. Imported from generated Python chunks; produces HTML for resource cards. |
| `_scripts/build_overview.py` | Generator | 205 lines. Produces `assets/data/resources.{de,en,fr}.json` (resources, labels, edges, related top-3 by Jaccard). |
| `_scripts/validate_sources.py` | CI gate | Schema validation of `sources_master.yml`. |
| `_scripts/check_commercial.py` | CI gate | Blocks commercial publishers from being added. |
| `_scripts/vgwort.lua` | Quarto filter | See §1. |
| `_includes/in-header.html` | Head injection | Plausible. |
| `_includes/after-body.html` | Body injection | Sub-navbar JS (entry-points). |
| `assets/light.scss`, `dark.scss`, `_shared.scss` | Theme | ~540 lines total. Custom palette, hero, card-grid, resource-card, entry-subnav, overview filter/graph styles. Overrides flatly/darkly. |
| `assets/js/entrypoints.js` | JS | 128 lines. Builds the four-group sub-navbar (Sprache/Fertigkeit/Niveau/Unit). |
| `assets/js/overview.js` | JS | 230 lines. Drives the vis-network overview page (filter chips, graph, related). |
| `scripts/check-legal-placeholders.sh` | local dev gate | 50 lines. |
| `.github/workflows/deploy.yml` | CI | Quarto build + 4 gates → upload-pages-artifact → deploy-pages. |
| `LEGAL.md`, `LICENSE`, `LICENSE-content`, `README.md` | docs | leave untouched. |

### 2.2 Generated content (NOT in git, produced at build time)

For each `lang ∈ {de, en, fr}`, `build_pages.py` emits **41 pages**:

- `{lang}/index.qmd` (landing)
- `{lang}/overview.qmd` (interactive graph)
- `{lang}/about.qmd`, `imprint.qmd`, `privacy.qmd`, `disclaimer.qmd` (legal — these are **the only legally substantial prose in the project**, and they are large; full text lives inside `build_pages.py` as Python string literals)
- `{lang}/nach_sprache/{englisch,franzoesisch,deutsch}.qmd` (3)
- `{lang}/nach_fertigkeit/{hoeren,lesen,schreiben,sprechen,grammatik,wortschatz,landeskunde}.qmd` (7)
- `{lang}/nach_niveau/{a1,a2,b1,b2,c1}.qmd` (5)
- `{lang}/nach_unit/efl/index.qmd` + `kl05.qmd` … `kl13.qmd` (10)
- `{lang}/nach_unit/fle/index.qmd` + `kl06.qmd` … `kl13.qmd` (9)
- `{lang}/nach_unit/daf/index.qmd` + `{a1,a2,b1,b2,c1}.qmd` (6)

Total: **3 × 41 = 123** generated pages, all of which embed a Python code chunk that calls `render_resources.render_filtered(...)` to produce the resource card list.

### 2.3 Quarto-specific constructs in active use

| Construct | Where | Hugo equivalent (proposed) |
|---|---|---|
| Fenced divs `:::{.hero}`, `:::{.kicker}`, `:::{.card-grid}`, `:::{.entry-card}` | `index.qmd`, generated landings | Markdown wrapped in raw `<div class="...">` — Hugo with `markup.goldmark.renderer.unsafe = true`. Or shortcodes if we want them sigil-free. |
| Python code chunks `{python}` calling `render_filtered(...)` | All 123 generated view pages | **Replace mechanism entirely.** Hugo template renders cards from a data source (see §3). No runtime Python. |
| Raw HTML pass-through `{=html}` block (overview page: vis-network) | Generated `overview.qmd` | Native Hugo — raw HTML in markdown is allowed under `unsafe = true`. Move script tags to a partial. |
| Quarto navbar (`website.navbar.left/right`, `tools`, dropdown menus) | `_quarto.yml` | Hugo `[menus]` config in `hugo.toml`, or Coder's `params.menu`. |
| Color-scheme toggle (flatly ↔ darkly) | Quarto-builtin | Coder ships a built-in light/dark toggle. Port both palettes to its CSS variables. |
| Frontmatter `aliases:` (legal pages) | imprint, privacy, disclaimer (DE) | Hugo native: `aliases:` works identically. |
| `pagetitle:` | landing pages | Hugo: set `title` + use site `params` for title-template. |
| Lua filter (vgwort) | `_quarto.yml` filters | Hugo partial `layouts/partials/vgwort.html` reading `.Params.vgwort_pixel`, included from `single.html` and `list.html` heads/bodies as appropriate. |
| Pre-render hook (`build_pages.py`, `build_overview.py`) | `_quarto.yml` | Replace with: (a) Hugo data-driven templates that read YAML/JSON at build time, eliminating `build_pages.py` entirely; (b) a CI step that runs `build_overview.py` to produce the JSON consumed by `overview.js` (or port that to Hugo too). |

---

## 3. Proposed Hugo architecture

The natural Hugo translation drops `build_pages.py` entirely and instead uses Hugo's data-driven page generation:

1. **Data:** copy `_resources/sources_master.yml` to `data/sources_master.yml`. Hugo reads it via `site.Data.sources_master`.
2. **i18n:** translate `_scripts/i18n.py` → `i18n/de.toml`, `en.toml`, `fr.toml` (Hugo's native i18n) plus `data/labels.yml` for the label dictionaries used by `build_overview.py`.
3. **Page generation:** Hugo doesn't have native "emit N pages from data," but it has two clean options:
   - **(a) Section template + per-language list pages.** Create one `content/{de,en,fr}/_index.md` per language plus stub `content/{de,en,fr}/nach_sprache/_index.md`, etc. — small set (~120 stubs) committed to git, each with frontmatter `params.filter: {...}`. The list template reads the filter, slices `site.Data.sources_master`, and renders cards.
   - **(b) Single template with URL parameters / `view` types.** More elegant, but Hugo's static-build model means we still need one stub per URL. Stubs are 3 lines each.
   Recommendation: **(a)**. Stubs are mechanical and explicit; what they produce is one Hugo template (`layouts/_default/resource-listing.html`) plus card partial.
4. **Card partial:** `layouts/partials/resource-card.html` — direct port of `render_card()` in `render_resources.py`. Receives a resource dict + the current site language.
5. **Overview page:** keep `build_overview.py` as a CI pre-build step (it's pure data shaping). Output goes to `static/data/resources.{de,en,fr}.json`. `overview.js` keeps working unchanged.
6. **Plausible:** `layouts/partials/head/plausible.html`, included from a head override of the Coder theme. Snippet copied verbatim.
7. **VG Wort:** `layouts/partials/vgwort.html` reading `.Params.vgwort_pixel`, included at end of `single.html` and `list.html`. Same fallback logic as the Lua filter (full URL / host+path / bare token).
8. **Sub-navbar (entry-points):** `assets/js/entrypoints.js` is keyed off URL paths and is theme-agnostic — port unchanged into Hugo's `assets/`. Update the `<script>` include to use Hugo's `resources.Get` + fingerprinting.
9. **Theme:** Coder via Hugo Modules. Both `light.scss` and `dark.scss` palettes ported into Coder's CSS-variable hooks; the trilingual badge styles (`.type-badge.type-oe`, `.cefr-badge.cefr-*`, etc.) port verbatim.
10. **CI gates retained:** `validate_sources.py`, `check_commercial.py`, the `<TODO>` placeholder check, the `S. Le Boulanger` copyright check. The placeholder check needs to point at the new files (e.g., `content/de/imprint.md`) instead of `de/imprint.qmd`.

### Proposed top-level layout (after migration)

```
hugo.toml
go.mod                                # hugo-coder via modules
i18n/{de,en,fr}.toml                  # ports _scripts/i18n.py
data/sources_master.yml               # moved from _resources/
content/
  _index.md                           # language picker (root, hand-authored)
  de/_index.md                        # landing (DE)
  de/overview/_index.md
  de/about.md, imprint.md, privacy.md, disclaimer.md
  de/nach_sprache/_index.md, englisch.md, franzoesisch.md, deutsch.md
  de/nach_fertigkeit/...
  de/nach_niveau/...
  de/nach_unit/efl/_index.md, kl05.md … kl13.md
  de/nach_unit/fle/...
  de/nach_unit/daf/...
  en/...                              # mirror of de/
  fr/...                              # mirror of de/
layouts/
  _default/baseof.html, single.html, list.html
  _default/resource-listing.html
  partials/head/plausible.html
  partials/vgwort.html
  partials/resource-card.html
  partials/entry-subnav.html          # or keep as JS, included via assets/
  shortcodes/hero.html, card-grid.html, entry-card.html, kicker.html
assets/
  scss/light.scss, dark.scss, _shared.scss     # ported from assets/
  js/entrypoints.js, overview.js               # unchanged
static/
  data/resources.{de,en,fr}.json      # produced by CI step (build_overview.py)
.github/workflows/hugo.yml            # new
```

### Navigation plan

The Quarto navbar is reproducible 1:1:

- Left: DE / EN / FR (language switcher, fixed).
- Right: About menu (DE/EN/FR), Legal menu (Impressum DE/EN/FR — Datenschutz DE/EN/FR — Haftungsausschluss DE/EN/FR), GitHub icon.

The four-group sub-navbar (Sprache / Fertigkeit / Niveau / Unit) ports as-is via the existing JS — it's already built dynamically from URL inspection.

**No "Materials" navbar entry will be added.** See §6, decision 1.

---

## 4. Risk list

| # | Risk | Mitigation |
|---|---|---|
| R1 | Quarto pre-render emits files that `quarto render` consumes — Hugo has no equivalent step and instead reads data at build time. The translation requires committing ~120 stub `.md` files plus a listing template. Stub filenames and URL paths must match Quarto output exactly so old links don't 404. | Phase 4 parity check against deployed sitemap. Hugo `aliases:` for any URL-shape changes. |
| R2 | The Quarto Python chunk model means cards are produced by Python at render time. Hugo has no Python — we re-implement `render_card()` and `filter_resources()` in Go templates. Risk: the rendered HTML drifts from the Quarto version. | Phase 2 includes a side-by-side render comparison: build current Quarto site → diff resource-card HTML for one URL per category against the Hugo build. Diff must be cosmetic-only (whitespace, attribute ordering). |
| R3 | The vis-network overview page reads JSON from a relative path (`../assets/data/resources.{lang}.json`). After migration the path is `/data/resources.{lang}.json`. | Update the `data-json` attribute in the overview page template. |
| R4 | `quarto-color-scheme-toggle` selector is referenced heavily in `_shared.scss`. Coder uses different DOM. | Replace those selectors with Coder's toggle classes when porting SCSS. |
| R5 | Plausible's `data-domain="boulingua.github.io/ressources"` includes a path segment (non-standard but supported by Plausible). Easy to typo when porting. | Phase 4 view-source check on five rendered pages; CI grep gate. |
| R6 | `_includes/in-header.html` is included on **every** page including non-content (e.g., listing roots). The Hugo `head` partial must do the same — Coder's default `head.html` does load partials site-wide, but verify. | Phase 4 view-source check covers this. |
| R7 | Legal text (Impressum, Datenschutz, Haftungsausschluss) currently lives **inside `build_pages.py`** as Python triple-quoted string literals. It must be extracted verbatim to the corresponding Hugo `content/{lang}/{imprint,privacy,disclaimer}.md` files. Any character drift = legal exposure. | Phase 2 will copy these strings byte-for-byte (Python source → markdown body, frontmatter rebuilt manually). Diff with `diff -w` against the Quarto-rendered HTML for sanity. |
| R8 | `_metadata.yml` `author: "S. Le Boulanger"` propagates to every Quarto page. Hugo equivalent is `params.author` in `hugo.toml`. | Set in Phase 1. CI gate already greps for "S. Le Boulanger" — point it at `hugo.toml`. |
| R9 | `i18n.py.t()` falls back to DE if a key is missing. Hugo's `i18n` falls back to the default content language. Set `defaultContentLanguage = "de"` in `hugo.toml` to match. | Configured in Phase 1. |
| R10 | The "Materials hub" instruction in the prompt does not fit this repo. Misapplying it would create 100+ junk `.pptx`/`.pdf` placeholders for "articles" that are actually link cards — i.e., dummies that have no relationship to any teaching material. | **Stop and ask** (see §6, decision 1). |

---

## 5. File-by-file migration order (proposed for Phase 1–3)

**Phase 1 (skeleton):** create branch; add `hugo.toml`, `go.mod`, base layouts, theme module, CI workflow. No content. Empty home page + working build only.

**Phase 2 (content & generators):**

1. Move `_resources/sources_master.yml` → `data/sources_master.yml`. **Source of truth, no edits.**
2. Port `_scripts/i18n.py` → `i18n/{de,en,fr}.toml` + `data/labels.yml`. Mechanical.
3. Port the legal text from `build_pages.py` literals → `content/{de,en,fr}/{about,imprint,privacy,disclaimer}.md`. **Byte-exact prose.**
4. Hand-author the language picker → `content/_index.md` (was `index.qmd`).
5. Generate the 120 view-page stubs via a one-shot Python helper `scripts/scaffold_hugo_stubs.py` (committed). Each stub = ~5 lines of frontmatter (`title`, `params.filter`).
6. Implement `layouts/_default/resource-listing.html` + `layouts/partials/resource-card.html` — direct port of `render_filtered()` + `render_card()`.
7. Implement `layouts/_default/list.html` for the entry-point index pages.
8. Port `_includes/in-header.html` → `layouts/partials/head/plausible.html`.
9. Port `_includes/after-body.html` → `layouts/partials/footer-extra.html` (or move JS to `assets/js/entrypoints.js` already there + Hugo `resources.Get` include).
10. Port `_scripts/vgwort.lua` → `layouts/partials/vgwort.html`. Reads `.Params.vgwort_pixel`, same URL-building logic.
11. Port the three SCSS files → `assets/scss/`. Update theme-toggle and Quarto-specific selectors.
12. Port the two JS files → `assets/js/` (entrypoints unchanged; overview.js: update its data path).
13. Replace `_scripts/build_overview.py` invocation in CI to write to `static/data/resources.{lang}.json`.
14. Build, browse, smoke-test.

**Phase 3 (Materials hub):** **Skip pending decision 1 in §6.** If the decision is "do it anyway," scope is much narrower than for sister sites — at most one "Materials" entry per *source category* (lang/skill/level/unit) and the placeholder generation needs explicit go-ahead.

**Phase 4 (cleanup, parity, deploy):** delete Quarto remnants, run sitemap diff, lychee link check, view-source check on Plausible, vgwort manifest verification, screenshots, open PR.

---

## 6. Decisions needed before Phase 1

I need answers to these before scaffolding the migration branch. None are blocking the report itself, but I should not start writing code while any are open.

**Decision 1 — Materials hub (Presentations + Worksheets).** The prompt prescribes a `/materials/` section with per-article `.pptx` and `.pdf` placeholders, and frontmatter-driven listing pages. The `ressources` repo has **no per-article teaching materials** to attach — it is a curated link directory whose entries are *external* resources (British Council, BBC, DW, Goethe-Institut, TV5Monde). Three options:

- **(a) Skip Materials hub for this repo.** It applies only to `fle` / `efl` / `daf`. (My recommendation.)
- **(b) Add a Materials hub but populate it with downloadable bundles per category** (e.g. one `.pdf` "EFL Klasse 7 — link sheet" per by-unit page). This is *new content*, not a migration, and the prompt says "Never invent content."
- **(c) Add the Materials hub with empty placeholders** as the prompt literally says, knowing it will create ~120 dummy `.pptx`/`.pdf` files attached to pages that conceptually shouldn't have them.

**Decision 2 — content stubs vs. true generator.** Given Hugo doesn't natively emit pages from data, do you prefer:

- **(a) ~120 committed stub `.md` files** (each ~5 lines), produced once by a scaffolding script. Simple, explicit, easy to grep, easy to extend. (My recommendation.)
- **(b) Keep `build_pages.py` as a Hugo pre-build CI step**, emitting `.md` instead of `.qmd`. Closer to current architecture; means `git diff` on data triggers no content churn but adds a Python CI dependency.

**Decision 3 — VG Wort plumbing.** Currently the Lua filter is wired up but **no page sets `vgwort_pixel`**. Confirm:

- **(a) Port the capability (Hugo partial + frontmatter convention) but ship zero pixels** — matches current state. (My recommendation.)
- **(b) Add pixels now to specific pages.** Which pages and what tokens?

**Decision 4 — overview.js data path.** `assets/js/overview.js` currently fetches `../assets/data/resources.{lang}.json`. In Hugo I'd serve from `/data/resources.{lang}.json` (absolute). Confirm it's OK to change the JS to read from an absolute path.

**Decision 5 — analytics domain attribute.** Plausible's `data-domain="boulingua.github.io/ressources"` includes the path. After migration the URL stays the same (`https://boulingua.github.io/ressources/`), so the attribute should also stay verbatim. Confirm.

---

## 7. Migration log

- **2026-05-06** — Phase 0 complete. No code changes, no commits.
- **2026-05-06** — Phase 1 (skeleton) complete on branch `migration/hugo-coder`. Decisions in §6 applied with my recommended defaults (skip Materials hub; commit stubs in Phase 2; port VG Wort capability with zero active pixels; absolute JSON path; Plausible verbatim).
  - Created `hugo.toml`, `go.mod`, `go.sum` pinned to the same Coder commit as the reference repo.
  - Quarto workflow renamed to `.github/workflows/deploy.yml.disabled` so it does not fire.
  - New CI workflow `.github/workflows/hugo.yml` with five build-time gates (schema, commercial, legal placeholders, copyright sentinel, Plausible source) plus a post-build gate that greps the rendered HTML for Plausible.
  - `layouts/_partials/head/extensions.html` ports the Plausible snippet verbatim from `_includes/in-header.html`.
  - Stub `content/_index.md` and per-language `content/{de,en,fr}/_index.md` so Hugo builds cleanly. Phase 2 replaces these with the real picker + generated views.
  - Local `hugo --minify` build succeeds (15 / 8 / 8 pages DE / EN / FR). Plausible verified present in rendered `public/de/index.html` (note: minifier strips attribute quotes — CI gate updated to accept both quoted and unquoted forms).
  - Quarto sources (`_quarto.yml`, `_resources/`, `_scripts/`, `_includes/`, `assets/_shared.scss`, etc.) **kept in place** alongside Hugo until Phase 4.
- **2026-05-06** — Phase 2 (content + generators) complete on `migration/hugo-coder`.
  - Moved `_resources/sources_master.yml` → `data/sources_master.yml`. Updated `_scripts/{render_resources,validate_sources,check_commercial,build_overview}.py` to point at the new path; existing Quarto build still works.
  - Repointed `_scripts/build_overview.py` output from `assets/data/` → `static/data/` so Hugo serves the JSON natively.
  - Added `scripts/scaffold_hugo_content.py` — one-shot generator that imports `_scripts/i18n.py` and `_scripts/build_pages.py`, emits `i18n/{de,en,fr}.toml` (~80 keys each, Python `{name}` → Go `{{ .name }}`) plus all content files. Reruns are idempotent.
  - **Legal text byte-exact:** about / imprint / privacy / disclaimer for DE / EN / FR — 12 files extracted from the Python triple-quoted literals in `build_pages.py` without prose modification. Quarto-style `aliases` for `/de/legal/{impressum,privacy,disclaimer}/` preserved (with the leading `/de/` stripped because Hugo prepends the language code automatically).
  - **Per-language landings + overview pages** (6 files) generated from i18n keys.
  - **120 view stubs** generated under `content/{lang}/{nach_sprache,nach_fertigkeit,nach_niveau,nach_unit/{efl,fle,daf}}/...md`. Each stub is ~6 lines: title, description, `layout: resource-listing`, `params.filter` (YAML map). Hand-edits go into the stubs directly; the scaffolder is a one-shot.
  - **Hugo multilingual config:** `[languages.{de,en,fr}]` with per-language `contentDir = "content/{lang}"`. `defaultContentLanguageInSubdir = true` so URLs are `/de/...`, `/en/...`, `/fr/...`. Hugo auto-emits a `/index.html` redirect to `/de/`; we overwrite it with the trilingual picker via a post-build `cp static/index.html public/index.html` (CI step).
  - **Layouts:**
    - `layouts/_default/resource-listing.html` — direct port of `render_filtered()`, slices `site.Data.sources_master` by `language` / `skill` / `cefr_level` / `unit_prefix`.
    - `layouts/_partials/resource-card.html` — direct port of `render_card()`, with German fallback for missing `description_{en,fr}` / `curator_notes_{en,fr}` matching the Python helper.
    - `layouts/_default/overview.html` — vis-network host page, points at `/data/resources.{lang}.json`.
    - `layouts/_partials/vgwort.html` — port of `_scripts/vgwort.lua` (full URL / host-path / bare-token forms all supported). Currently unused (no page sets `vgwort_pixel`); the capability is wired so an opt-in just works.
    - `layouts/index.html` — root home content block (currently unused at runtime; static/index.html overrides).
    - All templates use Coder's `{{ define "content" }}` block, not `main`.
  - **CSS:** `assets/css/ressources.css` ports the relevant rules from `_shared.scss` + light/dark `:root` blocks. Bootstrap-targeted SASS variables and Quarto-only selectors (`#TOC`, `.aa-*`, `.quarto-*`) dropped.
  - **JS:** `static/js/{entrypoints,overview}.js` copied verbatim. Entry-points sub-navbar JS loaded site-wide via head/extensions; it self-checks the URL path and noops outside `/{de,en,fr}/`.
  - **CI:** `_scripts/build_overview.py` runs as a pre-build step; `static/data/resources.{lang}.json` is produced before `hugo --minify`. Post-build, the root picker is restored. The five gates from Phase 1 still fire.
  - **Build verified locally:** 65 / 64 / 64 pages DE / EN / FR. Resource cards render under all four filter axes (verified DE/EN/FR samples). Plausible script intact in head (post-minify form). Three legal-page aliases emitted at `/{lang}/legal/{impressum,privacy,disclaimer}/`. Localized strings render correctly via Hugo's `{{ i18n }}` helper.
  - **Decisions §6 confirmed in the build:** Materials hub omitted; stubs (not generator) chosen; VG Wort partial ships, zero pixels active; overview JSON served at absolute `/data/...`; Plausible verbatim.
- **2026-05-06** — Phase 3 (Materials hub) **skipped** per §6 decision 1. `ressources` is a curated link directory; no per-article teaching materials exist to attach.
- **2026-05-06** — Phase 4 (cleanup, parity, deploy prep) complete locally on `migration/hugo-coder`.
  - **Quarto removed:** deleted `_quarto.yml`, `_metadata.yml`, `index.qmd`, `_includes/{in-header,after-body}.html`, `_scripts/{build_pages.py,render_resources.py,vgwort.lua}`, `assets/{_shared,light,dark}.scss`, `assets/js/{entrypoints,overview}.js` (now in `static/js/`), `.github/workflows/deploy.yml.disabled`, and the one-shot `scripts/scaffold_hugo_content.py`.
  - **Kept in `_scripts/`:** `validate_sources.py`, `check_commercial.py`, `build_overview.py`, `i18n.py` — all four are used by the Hugo CI workflow.
  - **`.gitignore`** trimmed of Quarto entries (`_site/`, `_freeze/`, `.quarto/`, `**/*.quarto_ipynb`, `/de/`, `/en/`, `/fr/`, `/assets/data/`); `static/data/` added (build-time output). The three previously-committed `static/data/resources.{lang}.json` files are now untracked.
  - **README.md** updated for the Hugo build (`hugo --minify` + `cp static/index.html public/index.html`); `LICENSE-content` repointed to `data/sources_master.yml`.
  - **Bug found and fixed during cleanup:** Coder's per-language menu rendering treats `menu.main.url` as language-relative; absolute paths like `/de/about/` were doubled to `/ressources/de/ressources/de/about/`. Fixed by changing menu URLs to bare `about/`, `imprint/`, etc. — Hugo prepends the per-language root automatically.
  - **`site.webmanifest`** added at `static/site.webmanifest` (minimal PWA manifest) — Coder's `<head>` references it.
  - **Parity check (sitemap diff vs. live Quarto site):**
    - 139 URLs in https://boulingua.github.io/ressources/sitemap.xml
    - 156 URLs across the three Hugo per-language sitemaps
    - **0 URLs from the live Quarto site missing in Hugo.** New URLs in Hugo are auto-generated `nach_*/` section indexes plus Coder's empty `categories/` and `tags/` taxonomy pages — harmless, no inbound links from the old site.
  - **Internal-link audit:** Python rglob over all 190 rendered HTML files, parsing every absolute `href`. **0 broken internal links.** (Lychee not installed on this Windows host; the equivalent grep+resolve pass was used.)
  - **Tracking gates dry-run on rendered output:** Plausible `data-domain` regex matches; Plausible `src` matches; VG Wort: zero pixel URLs anywhere in `public/` (no page opts in — capability ships, manifest is empty).
  - **Smoke check on five representative pages:**
    - `/` — trilingual language picker (hand-authored static HTML)
    - `/de/index.html` — landing with hero / 4 entry cards / criteria block, Plausible in head
    - `/de/imprint/index.html` — full Impressum prose verbatim from `build_pages.py`; alias at `/de/legal/impressum/` redirects correctly
    - `/de/nach_unit/efl/kl07/index.html` — 1 resource card (LearnEnglish Teens), correctly filtered by `unit_prefix`
    - `/en/nach_fertigkeit/hoeren/index.html` — 5 resource cards, EN-localized labels and descriptions
  - **Two non-trivial decisions taken during cleanup, documented for the PR:**
    1. EN/FR legal pages do not get the `/legal/...` alias (the source Python literals only set `aliases:` for DE) — preserves Quarto behaviour.
    2. The `static/data/resources.{lang}.json` files are gitignored, not committed — they are pure derivatives of `data/sources_master.yml` and regenerate cleanly in CI.
  - **Did NOT do:** push branch, open PR, deploy. Awaiting explicit OK because pushing is a visible-to-others action.
