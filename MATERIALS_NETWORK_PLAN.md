# Materials Network Plan — `boulingua/ressources`

**Status:** Phase 0 audit only. **Blocking decision needed before any further work.**

---

## 0. Headline finding (read this first)

The prompt assumes a Materials hub with per-article `presentation:` / `worksheet:` frontmatter exists in the repo. **It does not exist here, by design.**

This was explicitly settled in `MIGRATION_PLAN.md` §6 decision 1 and confirmed in the Phase 4 log:

> Phase 3 (Materials hub) **skipped** per §6 decision 1. `ressources` is a curated link directory; no per-article teaching materials exist to attach.

The other three sister repos (`fle`, `efl`, `daf`) are unit/lesson sites where each `.md` page **is** a teaching artefact and gets a paired `.pptx` + `.pdf`. This repo is structurally different: every "card" on this site is a pointer to an *external* resource (British Council, BBC, Deutsche Welle, Goethe-Institut, TV5Monde). There is nothing internal to attach materials to.

The prompt's own rule fires here:

> **Never invent content, taxonomy, or tags. Stop and ask if data is missing.**

So I'm stopping and asking. No code changes, no commits.

---

## 1. Phase 0 audit results

### 1.1 Migration is complete

| Check | Status |
|---|---|
| `_quarto.yml` absent | ✓ removed in Phase 4 |
| `hugo.toml` present | ✓ |
| All articles in `content/` as `.md` | ✓ 138 `.md` files |
| Materials hub working | ✗ **does not exist** |
| Plausible verified | ✓ post-build CI gate passes |
| VG Wort verified | ✓ capability ships, zero pixels active |

### 1.2 Material-bearing pages

Grep across `content/` for `^presentation:` and `^worksheet:` frontmatter keys: **zero matches across zero files**. There is no `content/materials/` directory.

### 1.3 Tag taxonomy

Grep across `content/` for `^tags:` frontmatter: **zero matches**. None of the 138 stub `.md` files set tags. The discoverability axes of this site live in **`data/sources_master.yml`**, not in page frontmatter:

| Field in `sources_master.yml` | Plays the role of |
|---|---|
| `language` (EN / FR / DE) | (no clean equivalent — this is the target language of the resource, not a topic) |
| `cefr_levels` (A1…C1) | "level" facet |
| `skills` (hoeren / lesen / schreiben / sprechen / grammatik / wortschatz / landeskunde) | the closest thing to "topic" |
| `applicable_units` (efl_kl7, daf_a1, …) | "course" facet |
| `license_type` (OE / CC / PD) | (no equivalent in the prompt's schema) |
| `media_types` (video / audio / text / interaktiv) | (no equivalent) |
| `publisher` | (no equivalent — the prompt assumes single-author content) |

The prompt's required `data/topics.yml` file does not exist and has no obvious source. The prompt explicitly forbids inventing one.

### 1.4 The site already has a discovery network

Worth flagging because it changes the framing of this entire phase: **a vis-network discovery graph already exists at `/{de,en,fr}/overview/`**, fed by `static/data/resources.{lang}.json` (produced at build time by `_scripts/build_overview.py`). It includes:

- One node per resource (5 today; will grow as the YAML grows)
- Label nodes for every `language`, `license_type`, `skill`, `cefr_level`, and `applicable_unit`
- Co-occurrence edges between labels (weighted)
- Top-3 related-resource suggestions per item via Jaccard similarity
- Filter chips for each label category

So the *spirit* of the prompt — interactive discovery network with multi-faceted filtering — is already implemented, just on a smaller dataset and with a different stack (vis-network + plain JS, not Cytoscape + Pagefind).

---

## 2. Decisions needed before any code changes

I see four coherent paths. **(a) is my recommendation.**

### (a) Skip Phase 5 entirely for `ressources`

Same logic as skipping Phase 3 (Materials hub) in the migration:

- The prompt is structurally wrong for a link-directory site. There is no internal corpus to network.
- The existing `/overview/` page already does the network-discovery thing for the *real* corpus (the curated link list).
- Apply Phase 5 to `fle` / `efl` / `daf` as the prompt describes, leave `ressources` alone.

### (b) Reinterpret Phase 5 as "upgrade `/overview/` to a Cytoscape-based discovery hub"

Treat each entry in `data/sources_master.yml` as a node, treat the existing overview page as the target, and apply the prompt's design system + interaction patterns (search via Pagefind, facet rail, list↔graph sync, URL state, accessibility nav, mobile fallback) to it. Map the prompt's vocabulary onto this repo's reality:

| Prompt term | This repo's analogue |
|---|---|
| "article" / "presentation" / "worksheet" node types | a single `resource` node type (no `.pptx` / `.pdf` because we don't host teaching materials) |
| `topic` registry | `skills` registry (already in `_scripts/i18n.py`) |
| `course` facet | `applicable_units` |
| `tags` facet | re-purposed for `media_types` and/or `license_type` |
| `data/topics.yml` | does not need to exist; `i18n.py` skill labels are the SOT |
| Materials hub at `/materials/` | the existing `/overview/` page upgraded in place |

This is a real piece of work — probably 1–2 days — but it ports the prompt's design system to a page that already exists and gets used. Risks: Cytoscape replaces vis-network (some visual drift), Pagefind needs to be added (currently no full-text search), `noUiSlider` adds a dependency. Worth doing only if you actively want a more polished `/overview/`.

### (c) Build the Materials hub from scratch as the prompt describes

Pick a topic taxonomy out of thin air, generate ~120 placeholder `.pptx` / `.pdf` files (one per by-unit page), attach them to the view stubs, then build the network on top.

This is what the migration prompt §6 decision 1 explicitly rejected because it violates "never invent content." I do **not** recommend it. Listing it for completeness only.

### (d) Wait until the YAML database is much larger

Today `data/sources_master.yml` has **5 entries**. A force-directed graph of 5 nodes with co-occurrence edges is not a "discovery network" — it's an over-engineered bullet list. The prompt is calibrated for hundreds of nodes (it specifies a 500–2000 node performance budget). At 5 nodes, the existing vis-network on `/overview/` already over-delivers.

If the curation effort grows the YAML to ~50+ entries, revisit this decision then.

---

## 3. What I will NOT do without a decision

- Create `data/topics.yml` (would invent a taxonomy).
- Generate placeholder `.pptx` / `.pdf` files attached to the view stubs (would invent content).
- Replace `/overview/` with Cytoscape (would silently change UX).
- Add Pagefind, `noUiSlider`, or any new dependency.
- Touch any layout, content, or workflow file.

---

## 4. Migration log

- **2026-05-06** — Phase 0 audit complete. No code changes.
- **2026-05-06** — Decision: **(a) skip Phase 5 for this repo.** Same reasoning as the migration's §6 decision 1: `ressources` is a curated external-link directory, has no internal teaching materials, and already has an equivalent vis-network discovery page at `/{de,en,fr}/overview/`. Phase 5 should be applied to `fle` / `efl` / `daf` instead. This file is committed so future runs of the Phase 5 prompt against this repo find the prior decision and don't re-litigate it.
