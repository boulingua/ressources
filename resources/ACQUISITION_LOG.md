# Acquisition log

_Run 2026-07-22. Host: sandboxed CI-style environment with **partial** outbound network._

## Outcome summary

- **88** sources catalogued in `resources/registry.yml` (48 from the curated `data/sources_master.yml`, 40 newly researched from the brief).
- **24** are openly licensed (public-domain / CC / open-access) — the only ones eligible to be cached.
- **8** sources actually fetched this run → **16 files, 37,757,711 bytes**, each SHA-256 verified.
- **64** sources are `redistributable: false` (reserved rights) → **link-only, never downloaded** ('verlinkbar, nicht kopierbar').
- **1** paid sources skipped: `es-ave-cervantes`.

## Host / network caveats

The acquisition host could not reach every provider. Recorded honestly so a re-run from an unrestricted host (via `scripts/refresh-resources.sh`) can complete the open subset:

- `directory.doabooks.org` (DOAB REST API) — unreachable/DNS from this host; `www.doabooks.org` front page is reachable.
- `irodori.jpf.go.jp` — DNS did not resolve from this host.
- `apprendre.tv5monde.com` — returns HTTP 403 to non-browser clients (reserved-rights anyway → link-only).
- `downloads.tatoeba.org` — reachable, but the English corpus exceeded the 16 MB session cap (fetch via the refresh script, which has no cap).

## Per-source outcomes (by language)

### Arabic (`ar`)

- **COERLL Arabic (Aswaat/Awebic etc.)** (`ar-coerll-arabic`) — mixed, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Madinah Arabic** (`ar-madinah-arabic`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Chinese (`zh`)

- **Chinese Plus (CLEC)** (`zh-chineseplus`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Chinese for HSK 1–6 (Peking University)** (`zh-coursera-pku-hsk`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### English (`en`)

- **BBC Learning English** (`bbc-learning-english`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **LearnEnglish Teens** (`bc-learnenglish-teens`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Breaking News English** (`breaking-news-english`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Discovering Literature (British Library)** (`british-library-discovering-literature`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Wikimedia Commons — Englische Aussprache-Audios** (`commons-en-pronunciation`) — CC-BY-SA-4.0, free — ✅ **success** — 3 file(s), 1,079,067 B cached
- **ELLLO – English Listening Lesson Library Online** (`elllo-listening`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Randall's ESL Cyber Listening Lab** (`esl-lab-randall`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **ESOL Courses** (`esolcourses-english`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Project Gutenberg — Englischsprachige Literatur** (`gutenberg-en`) — public-domain, free — ✅ **success** — 1 file(s), 174,311 B cached
- **LibriVox — Kostenlose Hörbücher (Internet Archive)** (`librivox-en`) — public-domain, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **ManyThings.org** (`manythings-esl`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Purdue OWL (Online Writing Lab)** (`purdue-owl`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Smithsonian Learning Lab** (`smithsonian-learning-lab`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Standard Ebooks** (`standard-ebooks`) — public-domain, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **Tatoeba — Beispielsätze mit Übersetzungen** (`tatoeba-en`) — CC-BY-2.0, free — 🟡 **staged** — open but not fetched this run: exceeds 16MB session cap (~full corpus larger); fetch via refresh-resources.sh (no cap)
- **TED-Ed Lessons** (`ted-ed`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **English Wikisource — Freie Quellentextbibliothek** (`wikisource-en`) — public-domain, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **ASCCC-OERI ESL OER list** (`en-asccc-oeri-esl`) — mixed, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **British Council LearnEnglish** (`en-britishcouncil-learnenglish`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### French (`fr`)

- **Bonjour de France** (`bonjour-de-france`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Wikimedia Commons — Französische Aussprache-Audios** (`commons-fr-prononciation`) — CC-BY-SA-4.0, free — ✅ **success** — 3 file(s), 101,641 B cached
- **DELF / DALF / TCF – France Éducation international** (`fei-delf-dalf`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **France Bienvenue** (`france-bienvenue`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Gallica** (`gallica-bnf`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Project Gutenberg — Littérature francophone** (`gutenberg-fr`) — public-domain, free — ✅ **success** — 1 file(s), 234,120 B cached
- **Le Point du FLE** (`lepointdufle`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Lumni (Collège)** (`lumni-college`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **1jour1actu** (`milan-1jour1actu`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Podcast Français Facile** (`podcast-francais-facile`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **franceinfo (Radio France)** (`radiofrance-franceinfo`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Le français facile avec RFI** (`rfi-le-francais-facile`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Apprendre le français** (`tv5monde-apprendre`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Vikidia (français)** (`vikidia-fr`) — CC-BY-SA-3.0, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **Wikisource en français** (`wikisource-fr`) — public-domain, free — 🟡 **staged** — open but not fetched this run: exact page node not resolved in session; PD text otherwise covered by gutenberg-fr. Stage specific works via refresh script.
- **France Éducation international — DELF/DALF/TCF** (`fr-fei-delf-dalf`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Liberté (T. Angelo)** (`fr-liberte-angelo`) — CC-BY-SA-4.0, free — ✅ **success** — 1 file(s), 31,139,159 B cached
- **RFI Savoirs** (`fr-rfi-savoirs`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Russian (`ru`)

- **State Pushkin Institute** (`ru-pushkin-institute`) — all-rights-reserved, free-registration — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Spanish (`es`)

- **AVE Global** (`es-ave-cervantes`) — all-rights-reserved, paid — ⛔ **paid** — skipped (demo/preview only)  ·  ⚠️ `redistributable: false`
- **Centro Virtual Cervantes** (`es-cvc-cervantes`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **RTVE Aprender español** (`es-rtve-aprenderespanol`) — all-rights-reserved, unknown — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Turkish (`tr`)

- **Yunus Emre Enstitüsü — Turkce** (`tr-yunus-emre`) — all-rights-reserved, free-registration — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Japanese (`ja`)

- **Irodori: Japanese for Life in Japan (free PDF)** (`ja-irodori`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Japan Foundation Marugoto / Minato** (`ja-jf-marugoto-minato`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Persian (`fa`)

- **COERLL Persian Online** (`fa-coerll-persian`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Norwegian (`no`)

- **NTNU — Learn NoW** (`no-ntnu-learnnow`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Polish (`pl`)

- **e-polish.eu** (`pl-epolish`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Polonicum, University of Warsaw** (`pl-polonicum`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Ukrainian (`uk`)

- **Igor Sikorsky KPI — Ukrainian MOOCs** (`uk-kpi-mooc`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Ukrainian Lessons** (`uk-ukrainianlessons`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Italian (`it`)

- **RAI — Italiano per stranieri** (`it-rai-italiano`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Greek (`el`)

- **Filoglossia** (`el-filoglossia`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Portal for the Greek Language (greek-language.gr)** (`el-greek-language`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Portuguese (`pt`)

- **Brazilpod / Tá Falado (COERLL)** (`pt-coerll-brazilpod`) — CC-BY-4.0, free — ✅ **success** — 3 file(s), 4,343,042 B cached
- **Centro Virtual Camões** (`pt-instituto-camoes`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Latin (`la`)

- **Legentibus** (`la-legentibus`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Perseus Digital Library** (`la-perseus`) — mixed, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script

### Dutch (`nl`)

- **NedBox.be** (`nl-nedbox`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Oefenen.nl** (`nl-oefenen`) — all-rights-reserved, free-registration — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Taalunie — Nederlands leren** (`nl-taalunie`) — all-rights-reserved, mixed — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### German (`de`)

- **Wikimedia Commons — Deutsche Aussprache-Audios** (`commons-de-aussprache`) — CC-BY-SA-4.0, free — ✅ **success** — 3 file(s), 126,206 B cached
- **DeutschAkademie – Online-Deutschkurs & Grammatiktrainer** (`deutschakademie-grammatiktrainer`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **deutschland.de** (`deutschland-de-landeskunde`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **nachrichtenleicht** (`dlf-nachrichtenleicht`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Nicos Weg** (`dw-nicos-weg`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Deutsch für dich** (`goethe-deutsch-fuer-dich`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Project Gutenberg — Deutschsprachige Literatur** (`gutenberg-de`) — public-domain, free — ✅ **success** — 1 file(s), 560,165 B cached
- **Klexikon – Das Kinderlexikon** (`klexikon-kinderlexikon`) — CC-BY-SA-4.0, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **mein-deutschbuch.de** (`mein-deutschbuch-daf`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Planet Schule** (`planet-schule-swr-wdr`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Projekt Gutenberg-DE** (`projekt-gutenberg-de`) — public-domain, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **vhs-Lernportal – Deutsch** (`vhs-lernportal-deutsch`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Wikibooks – Deutsch als Fremdsprache** (`wikibooks-deutsch-als-fremdsprache`) — CC-BY-SA-4.0, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **Deutsches Wikisource — Quellensammlung** (`wikisource-de`) — public-domain, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **logo! – Die Kindernachrichten des ZDF** (`zdf-logo-kindernachrichten`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **ZUM Deutsch Lernen** (`zum-deutsch-lernen`) — CC-BY-4.0, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **Aber hallo! (vhs Passau)** (`de-aberhallo-passau`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **DW Learn German** (`de-dw-learngerman`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Goethe-Institut — Deutsch üben** (`de-goethe-deutsch-ueben`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`
- **Schubert-Verlag Online-Aufgaben** (`de-schubert-verlag`) — all-rights-reserved, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

### Multilingual/OER (`mul`)

- **Cambridge University Language Centre — Open Courseware** (`meta-cambridge-lc-oer`) — CC-BY-NC-ND-2.0-UK, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **COERLL (meta-repository)** (`meta-coerll`) — mixed, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **Directory of Open Access Books — language teaching** (`meta-doab`) — mixed, free — 🟡 **open, not yet cached** — eligible; add to downloads and run refresh script
- **OER Commons — Language Textbooks collection** (`meta-oercommons-458`) — mixed, free — 🔗 **link-only** — reserved rights, catalogued but not downloaded  ·  ⚠️ `redistributable: false`

## Every `redistributable: false` item (storage-policy flag)

These are free to **access and link**, but their materials are **all-rights-reserved** (or paid). They are catalogued only; nothing is mirrored into the repo. Decide storage policy per item if you ever want a *personal, local* copy — it must stay out of git.

- **Arabic**: COERLL Arabic (Aswaat/Awebic etc.) (`ar-coerll-arabic`), Madinah Arabic (`ar-madinah-arabic`)
- **Chinese**: Chinese Plus (CLEC) (`zh-chineseplus`), Chinese for HSK 1–6 (Peking University) (`zh-coursera-pku-hsk`)
- **English**: BBC Learning English (`bbc-learning-english`), LearnEnglish Teens (`bc-learnenglish-teens`), Breaking News English (`breaking-news-english`), Discovering Literature (British Library) (`british-library-discovering-literature`), ELLLO – English Listening Lesson Library Online (`elllo-listening`), Randall's ESL Cyber Listening Lab (`esl-lab-randall`), ESOL Courses (`esolcourses-english`), ManyThings.org (`manythings-esl`), Purdue OWL (Online Writing Lab) (`purdue-owl`), Smithsonian Learning Lab (`smithsonian-learning-lab`), TED-Ed Lessons (`ted-ed`), British Council LearnEnglish (`en-britishcouncil-learnenglish`)
- **French**: Bonjour de France (`bonjour-de-france`), DELF / DALF / TCF – France Éducation international (`fei-delf-dalf`), France Bienvenue (`france-bienvenue`), Gallica (`gallica-bnf`), Le Point du FLE (`lepointdufle`), Lumni (Collège) (`lumni-college`), 1jour1actu (`milan-1jour1actu`), Podcast Français Facile (`podcast-francais-facile`), franceinfo (Radio France) (`radiofrance-franceinfo`), Le français facile avec RFI (`rfi-le-francais-facile`), Apprendre le français (`tv5monde-apprendre`), France Éducation international — DELF/DALF/TCF (`fr-fei-delf-dalf`), RFI Savoirs (`fr-rfi-savoirs`)
- **Russian**: State Pushkin Institute (`ru-pushkin-institute`)
- **Spanish**: AVE Global (`es-ave-cervantes`), Centro Virtual Cervantes (`es-cvc-cervantes`), RTVE Aprender español (`es-rtve-aprenderespanol`)
- **Turkish**: Yunus Emre Enstitüsü — Turkce (`tr-yunus-emre`)
- **Japanese**: Irodori: Japanese for Life in Japan (free PDF) (`ja-irodori`), Japan Foundation Marugoto / Minato (`ja-jf-marugoto-minato`)
- **Persian**: COERLL Persian Online (`fa-coerll-persian`)
- **Norwegian**: NTNU — Learn NoW (`no-ntnu-learnnow`)
- **Polish**: e-polish.eu (`pl-epolish`), Polonicum, University of Warsaw (`pl-polonicum`)
- **Ukrainian**: Igor Sikorsky KPI — Ukrainian MOOCs (`uk-kpi-mooc`), Ukrainian Lessons (`uk-ukrainianlessons`)
- **Italian**: RAI — Italiano per stranieri (`it-rai-italiano`)
- **Greek**: Filoglossia (`el-filoglossia`), Portal for the Greek Language (greek-language.gr) (`el-greek-language`)
- **Portuguese**: Centro Virtual Camões (`pt-instituto-camoes`)
- **Latin**: Legentibus (`la-legentibus`)
- **Dutch**: NedBox.be (`nl-nedbox`), Oefenen.nl (`nl-oefenen`), Taalunie — Nederlands leren (`nl-taalunie`)
- **German**: DeutschAkademie – Online-Deutschkurs & Grammatiktrainer (`deutschakademie-grammatiktrainer`), deutschland.de (`deutschland-de-landeskunde`), nachrichtenleicht (`dlf-nachrichtenleicht`), Nicos Weg (`dw-nicos-weg`), Deutsch für dich (`goethe-deutsch-fuer-dich`), mein-deutschbuch.de (`mein-deutschbuch-daf`), Planet Schule (`planet-schule-swr-wdr`), vhs-Lernportal – Deutsch (`vhs-lernportal-deutsch`), logo! – Die Kindernachrichten des ZDF (`zdf-logo-kindernachrichten`), Aber hallo! (vhs Passau) (`de-aberhallo-passau`), DW Learn German (`de-dw-learngerman`), Goethe-Institut — Deutsch üben (`de-goethe-deutsch-ueben`), Schubert-Verlag Online-Aufgaben (`de-schubert-verlag`)
- **Multilingual/OER**: OER Commons — Language Textbooks collection (`meta-oercommons-458`)
