# Media Registry — Per-Language Notes

Media-landscape commentary per language: variant/dialect caveats, editorial-independence concerns, sensitivity flags, and honest statements of where good non-partisan material does not exist. Companion to `media-registry.yml` and `MEDIA_COVERAGE.md`.

**Flag key** — `state-controlled`: catalogued for language quality but NOT recommended for the pool. `news-general` / `historical-context` / `religious`: sensitivity tags for downstream course filtering. `registration-gated`: needs a free account (surfaced for manual review). `acquisition_ref` in the YAML links an entry to `resources/registry.yml`; `archived: true` means an open copy is cached under `resources/_downloads/`.

## ar — Arabic  (17 entries)

Verification confidence is lower than usual for this pass: the web-search budget was exhausted (200/200) before review, so live-currency and canonical-URL confirmation leaned on opportunistic WebFetch (blocked by Cloudflare 403 on hindawi.org and safahat.org; successful on Al Jazeera Learning and Majid) plus domain knowledge. Treat URL currency as provisional and re-verify before shipping — the Hindawi domain (hindawi.org vs the unverified safahat.org) is the single biggest open question.

MSA spine is entirely state-funded international broadcasters: after correction, BBC Arabic, DW Arabic and Monte Carlo Doualiya are all tagged state-controlled (UK/German/French state funding) rather than the draft's softer 'public-service'. They retain legally protected editorial independence, which distinguishes them in practice from the Gulf state broadcasters, but the registry now labels them consistently by funding source. A genuinely independent, non-partisan NATIVE Arabic news broadcaster essentially does not exist: Al Jazeera = Qatar, Al Arabiya = Saudi (PIF/MBC, relocated to Riyadh in 2025), Sky News Arabia = Abu Dhabi — all state-linked and none entered as a primary non-partisan news source.

Diglossia caveat: Arabic is diglossic. Every news/literature entry here is MSA; spoken/informal Arabic splits into Egyptian, Levantine, Gulf and Maghrebi. The podcast networks (Sowt = mostly Levantine/MSA mix; Kerning Cultures = pan-MENA, with an English flagship so use its Arabic productions) skew dialectal, and Tatoeba explicitly tags Egyptian/Iraqi/Moroccan alongside MSA. A course must pick an MSA-first or a dialect track and not conflate them.

Genuine category gaps (not padded): (1) news-simplified — Arabic has no public-broadcaster equivalent of NHK News Web Easy; the nearest is Al Jazeera Learning's vocalized, topic-tagged 'Language of Media' track, which is why that platform is the highest-value entry. (2) video-drama — freely-licensed, learner-oriented drama is effectively absent; Arabic TV/film drama is commercial, copyrighted and mostly dialectal. (3) music — no clean-licensed lyrics resource from a reputable non-commercial body; classic lyrics circulate on community/commercial aggregators of murky copyright. (4) print-press — no native Arabic newspaper cleanly meets the non-partisan + freely-accessible bar (Asharq Al-Awsat/Al Arabiya = Saudi-linked, Al-Ahram = Egyptian state, Lebanese titles politically aligned); the reading-news function is served instead by the broadcaster text sites.

children-youth is thin: freely-accessible public-broadcaster kids' content barely exists for Arabic. Majid Magazine (UAE government, est. 1979) is the iconic vocalized-MSA option but is Magzter-paywalled and its linked URL is only a corporate brand page — kept solely because the category would otherwise be empty. Free alternatives worth a curator's own verification (not entered, as they are private YouTube productions): Adam wa Mishmish (Jordanian MSA preschool songs, strong for A1) and Iftah Ya Simsim (Arabic Sesame Street).

Corpus/classical register: after removing OPUS OpenSubtitles (graphic content + unknown licence), the transcript-corpus category rests solely on Tatoeba (clean CC-BY, A1-B1). For advanced classical reading and NLP, Al-Maktaba al-Shamila (flagged religious) and parts of Arabic Wikisource (historical-context) are the best-attested formal corpora but religiously skewed — included for C1-C2 study, never as default material. Hindawi is the standout for accessible, modern CC-BY prose and aligned audiobooks spanning A2-C2, pending the domain re-check.

**State-controlled / not recommended:**
- BBC News Arabic — BBC World Service is funded by the UK government (Foreign Office grant-in-aid historically; partial government funding restored from 2016 onward). Reclassified to state-controlled per the registry's rule that all state-funded international broadcasters carry that value. It retains legally protected editorial independence and is not state-directed in the propaganda sense, unlike Gulf state broadcasters.
- DW Arabic — Deutsche Welle is Germany's international broadcaster, funded in full from the federal budget under the Deutsche-Welle-Gesetz. Editorially independent by law but 100% government-budget funded; a state-funded international broadcaster.
- Monte Carlo Doualiya — France Médias Monde (French state) 24/7 Arabic public radio. State-funded international broadcaster.
- Al Jazeera Learning Arabic — Owned by Qatar-government-funded Al Jazeera Media Network. Content is language pedagogy (graded texts, grammar, vocalized media excerpts) with negligible advocacy risk. Verified live (free/open, seven graded levels, content dated January 2026).
- Al Jazeera Documentary — Qatar state-funded. Acceptable for MSA listening on history/culture/science; steer away from overtly political films. Not a first-choice non-partisan source.
- Majid Magazine — Published by Abu Dhabi Media Network (UAE government-owned). Children's edutainment with low advocacy risk but expect Gulf/UAE cultural framing. Corporate brand page verified live.

**Flags:**
- `paywalled` — Majid Magazine: Full digital editions require a paid Magzter subscription; free web reading is minimal, and the linked URL (admn.ae/en/brand/...) is an English corporate brand page rather than the reading platform. Recorded access=paid, status=paywalled.
- `paywalled` — Sowt: Freemium: core episodes are free on podcast platforms, but a Sowt+ tier (~$3/mo) gates some exclusive and ad-free content.
- `sensitivity` — Sowt — Eib and similar shows: Some shows address social taboos (sexuality, abuse, mental health). Curate at show/episode level before course use.
- `sensitivity` — Al-Maktaba al-Shamila: Corpus dominated by Islamic religious texts (tafsir, hadith, fiqh) compiled by a religious community forum. Value is the classical/formal register; flagged religious and never default material.
- `sensitivity` — Arabic Wikisource: Heritage and classical texts carry period-typical attitudes and include religious material (flagged historical-context).
- `other` — Hindawi Foundation: Two unrelated 'Hindawi' entities exist: the Hindawi Foundation (free CC-BY Arabic e-books and audiobooks; canonical hindawi.org) versus the academic-journals publisher Hindawi (acquired by Wiley, brand retired 2024). The researcher's claim that the library moved to safahat.org ('301 confirmed') could NOT be verified (WebFetch 403 on both domains; web search unavailable). URL reverted to the established canonical hindawi.org pending human re-verification.
- `other` — BBC News Arabic: Arabic radio service closed 27 January 2023; online text and TV/video continue. Standalone audio transcripts are limited. Note verified accurate.

**Wikimedia:** All seven entries were verified live on 2026-07-22. Because the session's WebSearch budget was already exhausted (200/200), verification was done via WebFetch on Wikimedia pages and curl against the MediaWiki, Tatoeba and Internet-Archive APIs (Special:Statistics for the Wikimedia editions; Tatoeba sentences/audio stats; IA librivoxaudio collection for LibriVox, whose own site blocked fetching).

STRONG / large editions: Arabic Wikisource (94,020 texts) and Arabic Wikipedia (1,325,252 articles, ~493M words) are the flagship holdings — Wikipedia is the canonical monolingual MSA corpus, Wikisource the canonical public-domain heritage library. Wikimedia Commons Arabic pronunciation (~1,856 files, incl. Lingua Libre Egyptian/Algerian dialect sets) is a solid A1–A2 audio resource. Tatoeba (68,505 sentences / 483 audio) is a good A1–B1 sentence corpus.

MODEST but genuine: Spoken Wikipedia Arabic (active مشروع المقالات المسموعة, ~156 tagged pages — real project, small volume), Arabic Wikibooks (only 895 content pages but a genuine language-learning shelf exists: English/French courses for Arabic speakers), and LibriVox Arabic (only ~2 full Arabic works plus multilingual collections — included because recordings genuinely exist).

ABSENT: There is NO Arabic learner/kids encyclopedia — no Arabic Vikidia, no Klexikon equivalent, and no 'Simple Arabic Wikipedia'. So the A2–B1 'children-youth' encyclopedia slot is empty for Arabic (as the task anticipated); omitted rather than invented.

REGISTER / DIALECT CAVEATS (important for Arabic): (1) Diglossia — all seven sources are overwhelmingly Modern Standard Arabic / Classical fuṣḥā, which no one speaks natively; they build reading/formal-listening competence, not colloquial conversation. (2) Wikisource and LibriVox lean Classical/archaic (harder, B2–C2). (3) Dialect material is essentially confined to Commons pronunciation audio (Egyptian arz, Algerian arq, Moroccan) and a minority of Tatoeba sentences. (4) Note also the separate DIALECT Wikipedia editions arz.wikipedia.org (Egyptian Arabic) and ary.wikipedia.org (Moroccan Darija); these are colloquial-register encyclopedias but are controversial/uneven and machine-assisted, so they were NOT catalogued as learner resources here — flag for possible separate review if colloquial reading input is wanted.

**Category gaps:** news-simplified, video-drama, music, print-press

**Dropped in QA:** OPUS — OpenSubtitles Arabic parallel corpus (Graphic source (unfiltered profanity, violence and adult-film dialogue), licence recorded as 'unknown' with unsettled subtitle copyright, and unusable without heavy filtering per its own caveat. Fails the clean-licence + learner-usable bar; transcript-corpus coverage retained via Tatoeba (clean CC-BY).)


## zh — Chinese (Mandarin)  (19 entries)

Editorial independence is the defining axis for Chinese-language media and it splits cleanly by jurisdiction. MAINLAND CHINA has effectively no editorially independent broadcaster (CCTV/CGTN/CRI/Xinhua/People's Daily are all party-state; the more independent outlets are paywalled — Caixin 财新 — or offshore/paywalled — Initium 端傳媒; 'accessible' English-facing outlets like Sixth Tone are state-affiliated). CCTV is catalogued once, flagged state-controlled and NOT recommended, purely to provide the standard-Putonghua pronunciation and simplified-script/Mainland-variant reference no non-state source here offers. HONG KONG's independent press has been dismantled since 2020-21 (Apple Daily, Stand News, Citizen News all closed/prosecuted) and RTHK's independence has been substantially eroded, so RTHK is included flagged state-controlled and not recommended. That leaves TAIWAN as the reliable home of non-state Mandarin media, and the pool is deliberately Taiwan-weighted. IMPORTANT REVISION this pass: I tightened the state-controlled flags the researcher under-applied. RTI, TaiwanPlus and Taiwan Panorama are all state-funded outward-facing/public-diplomacy vehicles (RTI = official international broadcaster; TaiwanPlus = government international broadcaster; Taiwan Panorama = a Ministry of Foreign Affairs magazine) and are now correctly marked state-controlled rather than public-service — the same treatment DW/RFI/France24/CGTN receive. The genuinely arm's-length statutory public broadcaster PTS (drama, children) stays public-service, and CNA (independent national news agency) and NER (educational, MOE-run) stay public-service with transparency flags. KEEP-VS-REMOVE TENSION (CCTV): the ruleset both tells me to remove 'propaganda' sources AND to ensure state-controlled broadcasters carry the state-controlled flag (which only makes sense if such broadcasters are kept). I read a national broadcaster's news division as the textbook 'state-controlled' case (kept, flagged, not recommended) rather than the 'advocacy/extremist' remove-case, and CCTV is the only simplified/Mainland reference — but a stricter reviewer could defensibly delete it, and I flag that judgement call explicitly. VARIANT CAVEAT: almost all recommended entries are Taiwan Mandarin in Traditional characters (zh-TW), differing from Mainland Putonghua in some vocabulary, a few pronunciations, and script; CCTV is the only simplified/Mainland reference and RTHK the only zh-HK. TWO HONEST GAPS, reported rather than padded: (1) news-simplified — there is no free public/institutional 'easy/graded news' equivalent to NHK News Web Easy in Chinese; the closest free graded material (OCAC Huayuworld, RTI's learner strand) is coursework, and the strong graded-news products (Chairman's Bao, Du Chinese) are commercial and excluded; (2) music — no institutional, freely-licensed Mandarin music-with-lyrics source exists; commercial lyric aggregators (Mojim) are copyright-questionable and excluded, and public-domain song texts survive only as literature (詩經, classical poetry on Wikisource) without audio. Transcript/subtitle availability is a strength for video (Taiwan TV ships burned-in Chinese subtitles) but a weakness for live radio/podcasts (RTI, NER rarely publish transcripts); the corpus/graded entries (COCT, ASBC, Huayuworld) partly compensate as alignment tools. VERIFICATION METHOD: the shared WebSearch budget was already exhausted (200/200 — the environment refused every query), so this pass relied on WebFetch, which succeeded on RTI, TaiwanPlus, Taiwan Panorama, NER, COCT, ctext, CCTV and the RTHK Putonghua channel and confirmed all their canonical URLs live on 2026-07-22. Residual low-confidence items: Huayuworld (JS wall, not re-fetchable) and ASBC's login gate (old frameset) rest on prior verification; PTS apex returned a TLS quirk (not an outage), corroborated via the TaiwanPlus '© 2026 PTS' footer.

**State-controlled / not recommended:**
- 中央廣播電臺 華語 Live (Radio Taiwan International) — Taiwan's official state-funded international broadcaster (財團法人中央廣播電臺; public-diplomacy remit; DW/RFI/VOA analogue). Reclassified from public-service. Credible in practice but international/cross-strait coverage carries Taiwan's national perspective; flagged, still usable.
- TaiwanPlus — Taiwan's government-funded international broadcaster, PTS-operated (WebFetch: © 2026 PTS), MOFA-seeded public-diplomacy outlet. Reclassified from public-service. Narration often English-dominant; Mandarin value mainly via Chinese-language shows + burned-in subtitles.
- 台灣光華雜誌 Taiwan Panorama — Published directly by Taiwan's Ministry of Foreign Affairs (版權所有 外交部 光華畫報雜誌社); outward-facing multilingual public-diplomacy magazine, not arm's-length. Reclassified from public-service. Cultural/soft-power content (low propaganda risk); bilingual parallel text still valuable for B1-C1 reading.
- 央视网 CCTV News — Mainland PRC party-state broadcaster; gold-standard Putonghua and the sole simplified-script/Mainland-variant reference here. Kept flagged and explicitly NOT recommended for the learner pool; catalogued for pronunciation/variant reference only. Keep-vs-remove tension discussed in landscape notes.
- 香港電台 普通話台 RTHK Putonghua — HK public broadcaster (a government department) whose editorial independence has been substantially eroded since the 2020 National Security Law (critical programming cut, management replaced). Kept for zh-HK/Putonghua coverage; not recommended as a primary non-state source. URL refined to the Putonghua-channel page.

**Flags:**
- `other` — 中央社 CNA: Government-funded national news agency (財團法人中央通訊社) with statutory editorial independence; generally rated least-biased. Kept as public-service; flagged only for funding transparency.
- `other` — 國立教育廣播電臺 NER: Directly operated by Taiwan's Ministry of Education (a government agency, not arm's-length). Kept as public-service because content is educational/curriculum with negligible editorial-independence risk; flagged for funding transparency.
- `sensitivity` — 中文維基文庫 Chinese Wikisource: historical-context: classical, vernacular and out-of-copyright texts carry period-typical worldviews and prejudice; largely advanced literary register (B2-C2).
- `sensitivity` — 中國哲學書電子化計劃 ctext.org: historical-context: pre-modern / Classical Chinese (文言文) with archaic worldviews and period prejudice; C1-C2 specialist register.
- `registration-gated` — 全球華文網 學華語向前走 (OCAC Huayuworld): Free, but a subset of graded-reader e-books/materials requires a free account. Could not be re-fetched this pass (JS-rendered wall); status rests on prior verification, no evidence of outage.
- `registration-gated` — 中央研究院平衡語料庫 (Academia Sinica ASBC): Free, but full concordancer access historically needs a free academic account; the old frameset interface is confirmed live, though the login requirement could not be re-confirmed via fetch.
- `registration-gated` — 公視戲劇 PTS Drama (公視+): Streaming on the 公視+ platform requires a free account. Added to the registration-gated list (the researcher's list omitted it); access=free-registration retained.
- `registration-gated` — 公視兒少 / 小公視 (PTS children, 公視+): Streaming on 公視+ requires a free account; selected children's titles are free. Added to the registration-gated list (also omitted by the researcher); access=free-registration retained.

**Registration-gated (free account; verify manually):**
- 全球華文網 學華語向前走 (OCAC) — https://www.huayuworld.org/
- 中央研究院平衡語料庫 (Academia Sinica ASBC) — https://asbc.iis.sinica.edu.tw/
- 台灣光華雜誌 Taiwan Panorama — https://www.taiwan-panorama.com/

**Wikimedia:** All 8 entries verified live against Special:Statistics / Commons category pages / Tatoeba stats / Internet Archive on 2026-07-22. Counts cited are from those pages.

STRONG editions: (1) Chinese Wikisource — very large (~3.0M content pages, one of the biggest Wikisources) and classics-rich. (2) Chinese Wikipedia — 1,544,997 articles, the canonical modern-Chinese text corpus. (3) Commons 'Chinese pronunciation' — 5,159 files. (4) Tatoeba cmn — 88,344 sentences / 5,827 with audio.

PRESENT but smaller/niche: (5) Literary Chinese Wikipedia (文言文維基大典) — 14,115 articles, a distinct active edition in the classical register (added as a separate entry, not merged, per the register split). (6) Spoken Chinese Wikipedia — 284 spoken-article files (live category is 'Spoken Chinese Wikipedia'; the hyphenated 'Spoken Wikipedia - Chinese' is only a redirect). (7) Chinese Wikibooks — 3,835 books with a real Languages shelf (Subject:語言) incl. a Modern Standard Chinese course, but most books are 0-25% complete, so it is supplementary/quality-variable. (8) LibriVox Chinese — 26 completed works confirmed on the Internet Archive (Tang poetry, Lu Xun, Art of War, Analects, CUV Bible).

ABSENT: No learner-friendly Wikimedia encyclopedia edition exists for Chinese — there is no Simple Chinese Wikipedia, no Chinese Vikidia, no Klexikon/Wikikids equivalent. So the 'children-youth' A2-B1 encyclopedia slot is empty and was omitted (not invented). Wikijunior-style material exists only sparsely inside zh.wikibooks.

REGISTER / DIALECT CAVEATS (important for 'zh'): The learning target is Modern Standard Mandarin (Putonghua/Guoyu), but Wikimedia Chinese content is a shared written standard served with automatic Traditional⇄Simplified conversion and regional lexis toggles (zh-cn / zh-tw / zh-hk / zh-mo / zh-sg) — useful for contrasting Mainland/Taiwan/HK vocabulary. Two big gaps to flag in class: (a) Wikisource and LibriVox are dominated by Classical/Literary Chinese (文言文) and late-imperial vernacular, NOT modern spoken Mandarin — high difficulty, treat as advanced/CLIL only; a whole separate Literary Chinese Wikipedia also exists (specialist). (b) Commons pronunciation audio and Spoken Wikipedia mix in Cantonese (yue), Min, Wu, Sichuanese etc. — filter by file/prefix for pure Mandarin. Political caveat: zh.wikipedia is intermittently blocked in the PRC and topic coverage reflects that editing environment. Licence split throughout Wikimedia: underlying source texts/recordings public-domain (Wikisource, LibriVox) vs. community editorial layer / media CC BY-SA (Wikipedia, Wikibooks, Spoken WP, Commons audio mixed CC/CC0); Tatoeba sentences CC BY 2.0 FR with mixed-CC audio.

**Category gaps:** news-simplified, music


## en — English  (21 entries)

English is by a wide margin the richest language for free, transcript-bearing public-service media, so this list is quality-gated rather than scarcity-limited and cleanly covers all 12 categories at 15 entries; none needed removing. VERIFICATION METHOD (important honesty caveat): this session's WebSearch budget was fully exhausted (200/200) before any query could run, exactly as the draft warned, so ZERO web searches were possible. Currency rests on (a) WebFetch confirmations that succeeded — Project Gutenberg live at 77,687 ebooks; The Conversation live with July-2026 headlines and all regional editions; Storyline Online live under the SAG-AFTRA Foundation (© 2026, titles dated Dec 2025); Internet Archive, TED and PBS all live with current content — plus (b) HTTP 403/timeout responses that confirm the SERVER is up but not the content, for VOA, Smithsonian Folkways, LibriVox, British Council and english-corpora.org (all bot-protected), and BBC hosts which are hard-blocked to WebFetch entirely; and (c) knowledge to a Jan-2026 cutoff. No candidate could be shown 'dead', but two URLs carry real risk and are flagged for maintainer re-verification: VOA Learning English (USAGM dismantlement — cadence and continuity genuinely uncertain) and the BBC World Service live-stream path (BBC migrating international audio off BBC Sounds toward bbc.com/audio). ERRORS CAUGHT AND FIXED: TED licence field (CC-BY-NC -> CC-BY-NC-ND, self-contradictory in the draft); Smithsonian Folkways access (free -> mixed, paid downloads); VOA cadence (weekly -> irregular). DIALECT/VARIANT: the set is UK-heavy (BBC x3, British Council) and US-heavy (VOA, NPR, PBS, Storyline, Smithsonian, COCA), with genuinely global/mixed sources (TED, The Conversation, Project Gutenberg, LibriVox). Australian, Canadian and Irish standard varieties remain UNREPRESENTED despite being readily available from public broadcasters — the natural next additions are ABC Australia (abc.net.au / ABC listen), CBC Canada (cbc.ca/listen), RTÉ Ireland and SBS Australia; held back this pass only for category spread and transcript availability. THIN CATEGORIES: (1) video-drama is the genuine weak spot — freely accessible, globally viewable, subtitled English drama barely exists outside geo-locked broadcaster apps (BBC iPlayer, ITVX, ABC iview, SBS On Demand are region-locked; National Theatre at Home is paid), so the Internet Archive public-domain film collection is the only stable free global option and its subtitles are inconsistent. (2) music-with-published-lyrics from a public institution is scarce; Smithsonian Folkways (liner-note lyrics, now access=mixed) is the best institutional fit since the strong lyrics databases (Genius, Musixmatch) are commercial and excluded. EDITORIAL INDEPENDENCE: English has a deep bench of editorially independent public-service broadcasters (BBC, PBS, NPR), so the list does not lean on any state-controlled or advocacy outlet — VOA is the only state-controlled entry, kept strictly for its pedagogically unique public-domain Special-English simplified news and explicitly flagged not-an-anchor. Commercial ed-tech/ELT publishers were confirmed absent (cross-checked against the repo's check_commercial.py block-list); the free graded-reader gap is covered by the British Council (public body) and BBC Learning English. All 15 entries are free at point of use.

**State-controlled / not recommended:**
- VOA Learning English — US federal international broadcaster (Voice of America / USAGM). Historically protected by the statutory VOA Charter editorial firewall, but the agency has been dismantled through 2025 (RIFs, staff placed on leave, funding rescission, ongoing litigation). Content is public-domain US-government work (permanently reusable). Server responds HTTP 403 (live, bot-protected) but no 2026 content could be confirmed and update cadence is now 'irregular' at best. Catalogue as a public-domain archive; do NOT use as a pool anchor. Highest-continuity-risk URL in the set.

**Flags:**
- `sensitivity` — BBC News: news-general. Mainstream news inevitably covers war, elections and crime — rely on topic_tags to let a course pick economy/science/culture over conflict or campaign coverage.
- `sensitivity` — BBC Learning English: news-general. 'News Review' and '6 Minute English' are built on current-affairs source stories; graded but still touches politics/conflict topics.
- `sensitivity` — NPR: news-general. Natural-rate US public-radio journalism covering politics, campaigns and crime; steer via topic_tags toward science/storytelling strands.
- `sensitivity` — PBS: news-general / historical. FRONTLINE and American Experience cover war and atrocity history; prefer NOVA/Nature science strands as the default for course use.
- `sensitivity` — BBC World Service: news-general. Rolling world news, conflict and current affairs; use for immersion and filter by programme.
- `sensitivity` — The Conversation: news-general. Academic explainer journalism that still covers politics and climate; tag topics.
- `sensitivity` — Internet Archive — Feature Films: historical-context. Public-domain classic films carry period-typical, sometimes prejudiced portrayals; separately, captions/subtitles are inconsistent and often absent, limiting transcript-aligned use.
- `sensitivity` — Project Gutenberg: historical-context. Pre-1930 public-domain texts contain period-typical prejudice and dated usage; curate individual titles rather than exposing the whole corpus.
- `sensitivity` — LibriVox: historical-context. Same underlying public-domain classics as Project Gutenberg; period prejudice and dated usage; curate per title.
- `registration-gated` — english-corpora.org (COCA/BNC/NOW): Free account required with daily query limits; concordance output is unfiltered authentic language that can surface profanity or sensitive text.
- `registration-gated` — British Council LearnEnglish: Core reading/listening materials are open; some interactive/progress features need a free account. Separate paid British Council courses/exams (IELTS) are out of scope. Government-sponsored but operationally-independent charity (apolitical ELT content), tagged public-service rather than state-controlled.
- `paywalled` — PBS: Full on-demand streaming is largely US-geo-restricted and the extended 'Passport' library is a paid donor tier; PBS YouTube provides global free access to much documentary content.
- `access-mixed` — Smithsonian Folkways: Streaming previews and scholarly liner-note PDFs (which carry lyrics) are free, but high-quality audio downloads are purchase-only — access corrected to 'mixed'.
- `geo-restricted` — BBC World Service / BBC Sounds: BBC Sounds on-demand is UK-geo-locked; only the World Service English live stream and its podcasts are deliberately kept available internationally. The live-stream path needs re-verification given the BBC's migration of international audio toward bbc.com/audio.
- `licence-no-derivatives` — TED Talks / The Conversation: Both are Creative Commons with a no-derivatives clause (TED = CC BY-NC-ND, corrected from the draft's erroneous 'CC-BY-NC'; The Conversation = CC BY-ND): verbatim republication with attribution is allowed, adaptation is not.

**Registration-gated (free account; verify manually):**
- english-corpora.org (COCA/BNC/NOW) — https://www.english-corpora.org/
- British Council LearnEnglish (some interactive features) — https://learnenglish.britishcouncil.org/

**Wikimedia:** All 8 Wikimedia-family + close-adjacent editions were verified live for English on 2026-07-22 via Special:Statistics, canonical Commons category pages, and Tatoeba stats (WebSearch budget was exhausted this session, so verification used deterministic WebFetch against Wikimedia stat pages).

WHAT EXISTS AND IS STRONG:
- en.wikisource (1,119,565 content pages) — the largest Wikisource edition; deep literature + historical primary sources.
- en.wikipedia (7,212,392 articles) — the canonical English monolingual text corpus (transcript-corpus).
- Simple English Wikipedia (283,515 articles) — the standout learner asset: this IS the English learner-friendly encyclopedia variant (the counterpart to Vikidia/Klexikon/Wikikids elsewhere). A2-B1 GOLD.
- Tatoeba English (2,040,493 sentences; 849,774 with audio) — strongest A1-B1 sentence/audio bank.
- Commons Category:English pronunciation (1,420 files + 15 subcategories, incl. 8 by dialect) — A1-A2 pronunciation.
- Spoken Wikipedia English (1,924 spoken articles, Ogg Vorbis) — exists and is actively maintained (page reviewed 17 Jul 2026); added as a SEPARATE podcast entry per instructions.
- en.wikibooks Subject:Languages shelf — a genuine language-learning/textbook shelf exists (en.wikibooks = 98,553 content pages), so it is included as literature-graded.
- LibriVox English — English is LibriVox's dominant language; included as literature-public-domain audio.

CAVEATS:
- Nothing was omitted for non-existence — every project in the brief has a live, active English edition.
- Spoken Wikipedia recordings frequently lag behind edited article text; treat audio/text currency with care.
- LibriVox blocks automated fetch (403 to bots) so its exact live English count was not machine-verified this session, though the site is up and English holdings are extensive; the URL used is the canonical language-search entry (primary_key=1 = English).
- Register/dialect: Wikisource and Wikipedia lean B2-C2 (literary/encyclopedic register); Wikisource 19th-c. literature and LibriVox classics carry period prejudice (marked historical-context). Wikibooks is community-authored and uneven — vet individual books.
- The relevant English variant axis is British vs American (spelling/pronunciation); all Wikimedia editions are pan-dialectal, hence variant 'mixed'. Commons pronunciation is the one place to select a specific dialect via its by-dialect subcategories (British/American/Australian/etc.).
- Licences: Wikisource + LibriVox = public-domain source texts (Wiki editorial layer CC-BY-SA); Wikipedia/Simple/Spoken/Wikibooks = CC-BY-SA; Commons audio = mixed CC (many CC0/PD); Tatoeba = CC BY 2.0 for text, mixed CC for audio.
- These entries were NOT written to data/sources_master.yml (task was catalogue + verify only); the existing YAML already holds separate DE-annotated records for wikisource-en, tatoeba-en and librivox-en under its own schema, so watch for ID/dedup when integrating.


## fr — French  (21 entries)

French remains one of the richest languages for authentic, free, public-service media, so this is a strong list of 15 - none needed removing on suitability grounds; the draft's main defect was governance classification, not selection. VARIANT SPREAD is genuine: France (fr-FR) dominates but Belgium (RTBF Auvio, fr-BE), Quebec/Canada (Radio-Canada OHdio, fr-CA) and pan-francophone accents (TV5MONDE) are represented. EDITORIAL INDEPENDENCE - the key correction: RFI (France Medias Monde) and TV5MONDE are state-funded INTERNATIONAL broadcasters and are now flagged 'state-controlled' as a funding/governance fact; the draft's argument to keep them 'public-service' because they are non-partisan and 'unlike RT/CGTN' was rejected - the label is not a quality judgment and both stay recommended. Domestic public broadcasters (franceinfo, France Inter, France Culture, RTBF, ARTE, Radio-Canada, Okoo) and the BnF stay 'public-service'. No genuinely partisan/propaganda outlet was included. GAPS BY VARIANT: Swiss French (RTS / Play RTS, comparable to RTBF) is a plausible future addition but is not catalogued here; African/Senegalese French (fr-SN) is an honest gap - there is no dedicated public-broadcaster GRADED learner resource for West-African French, and RFI only partially serves a pan-African audience in its general programming. MISSING CATEGORIES: (1) video-drama - France.tv carries public-service fiction with French SDH subtitles but is geo-restricted to France, failing the 'freely accessible to a global learner pool' test; ARTE offers some subtitled fiction as a partial substitute. No freely-worldwide, subtitled French drama archive from a public broadcaster. (2) literature-graded - no strong NON-COMMERCIAL graded-reader source exists in French (the space is dominated by excluded ELT publishers); the function is mitigated by RFI's and TV5MONDE's CEFR-tagged content, so the gap is real but well-covered. TRANSCRIPT AVAILABILITY IS UNEVEN and is the key pedagogical variable: RFI, TV5MONDE, 1jour1actu and CLAPI publish transcripts/lyrics; France Culture, ARTE, France Inter, RTBF and OHdio largely do not and should be paired with course-supplied transcription. MUSIC with published lyrics is institutionally thin - TV5MONDE 'Paroles de clips' is effectively the only public-service option. INA's migration to the paid 'madelen' subscription is the main degradation of an otherwise excellent free landscape. TOOLING CAVEAT: this review could not perform live web verification - the WebSearch budget was exhausted (200/200) and WebFetch is network-blocked for the French hosts; currency/URL checks rest on domain knowledge (cutoff Jan 2026), the task-stated RFI migration, and repo COVERAGE.md. Re-verify all canonical URLs (especially the TV5MONDE 'Paroles de clips' sub-path, the France Culture LSD slug, and CLAPI over HTTPS) at ingestion.

**State-controlled / not recommended:**
- Le francais facile avec RFI — RFI / France Medias Monde is France's state-FUNDED international broadcaster (state budget, outward francophone mission). Reclassified from the draft's 'public-service' to 'state-controlled' per registry policy - a funding/governance fact, not a quality verdict. Operates under a public-service charter with day-to-day editorial independence and the learner content is deliberately non-partisan graded news; still RECOMMENDED, distinct in tone from RT/CGTN/PressTV but placed in the same governance bucket.
- Apprendre le francais avec TV5MONDE — TV5MONDE is a state-funded international broadcaster jointly financed by the governments of France, Belgium (FWB), Switzerland, Canada, Quebec and Monaco. Reclassified 'public-service' -> 'state-controlled' on the same funding/governance basis; remains RECOMMENDED, with pan-francophone accents a pedagogical asset.
- Paroles de clips (TV5MONDE) — Same publisher/governance as the TV5MONDE learner site; reclassified to 'state-controlled'. Shares the base URL apprendre.tv5monde.com with the main TV5MONDE entry (distinct 'music' collection, not a duplicate); supply the specific collection sub-path at ingestion.

**Flags:**
- `sensitivity` — Mainstream news / current-affairs set (news-general): sensitivity 'news-general' applies to: franceinfo, France Inter, France Culture (LSD), RTBF Auvio, Radio-Canada OHdio, ARTE, Le francais facile avec RFI, Apprendre le francais avec TV5MONDE, The Conversation France, and 1jour1actu. These inevitably cover politics, conflict, elections and crime. Use each entry's topic_tags so a course can select neutral registers (economy, science, culture) and avoid campaign/atrocity material.
- `sensitivity` — Gallica & Litteratureaudio.com: sensitivity 'historical-context': 19th/early-20th-century public-domain texts contain period-typical prejudice, colonial framing and archaic spelling. Flag when used as source material.
- `registration-gated` — CLAPI - Corpus de Langues Parlees en Interaction: Online consultation is free; some corpus data downloads may require a free academic account. Licence is research-oriented and not clearly stated (recorded 'unknown'). Additionally, the HTTPS canonical URL could not be confirmed this session (fetch refused on :443) - verify at ingestion.
- `other` — Okoo (France Televisions): Geo-restricted: most Okoo streaming is available only from France, an access barrier for a global learner pool despite being free and ad-free. (Radio-Canada OHdio and RTBF Auvio TV replay are similarly geo-limited for some content, while their audio streams free worldwide.)
- `paywalled` — INA (Institut national de l'audiovisuel): NAMED ANCHOR, NOT included as an entry: the archive has largely migrated to the paid 'madelen' subscription (approx 2.99-3.99 EUR/month). Free consultation on ina.fr remains for a large historical set but ships without transcripts or CEFR scaffolding, lowering learner usability.

**Registration-gated (free account; verify manually):**
- CLAPI - Corpus de Langues Parlees en Interaction — https://clapi.icar.cnrs.fr

**Wikimedia:** All seven requested Wikimedia-family targets exist and are active for French; 8 verified entries produced (Wikipedia yields two: the text corpus + a separate Spoken-Wikipedia audio entry). Every figure below was checked live on 2026-07-22 via Special:Statistiques, the MediaWiki/Tatoeba APIs, and archive.org (WebSearch budget was exhausted, so verification used WebFetch + curl against deterministic Wikimedia URLs).

STRONG / DEEP editions:
- Wikisource FR (699,851 texts, ~1.26B words) — among the largest Wikisource editions; full French PD canon (Hugo, Zola, Balzac, Flaubert, Voltaire, Molière, Verne, Baudelaire, Proust). B2-C2.
- Wikipedia FR (2,770,583 articles, ~1.90B words, 32,566 active editors) — the canonical monolingual French corpus; encyclopedic register; CC-BY-SA-4.0.
- Commons French pronunciation — 3,552 files directly + Lingua Libre pronunciation-fra (~430,895 files) + Shtooka; A1-A2 pronunciation. Deep but licence is MIXED CC (CC0/CC-BY/CC-BY-SA) — verify per file.
- Tatoeba French — 728,600 sentences (9,833 with audio), CC-BY-2.0, parallel-corpus; A1-B1 gold.

SOLID:
- Vikidia (fr) — 45,721 articles, CC-BY-SA-3.0; the French kids-encyclopedia (ages 8-13), francophone analogue of Simple English Wikipedia / Klexikon; A2-B1 gold learner resource.
- Wikibooks FR / Wikilivres — 21,824 books; included because it has a real 'Langues' department (Classe 8) with graded foreign-language courses. Community-authored, uneven quality.
- LibriVox French — 275+ items catalogued as French ('fre') on archive.org; volunteer PD audiobooks; audio-only (transcript n/a on-site).

MODEST / CAVEATED:
- Spoken French Wikipedia EXISTS (Commons Category:Spoken French Wikipedia, 344 recordings, audio+full text) but is small and updated sporadically — supplementary, not systematic. NAMING CAVEAT: the variant Category:Spoken_Wikipedia_-_French is an empty redirect; the live category is Category:Spoken_French_Wikipedia.

ABSENT / NOT APPLICABLE:
- There is no 'Français simple' Wikipedia edition (no French counterpart to Simple English Wikipedia at the fr.wikipedia level); Vikidia fills the learner-encyclopedia slot for French, so no gap.

REGISTER / DIALECT CAVEATS:
- French has no Bokmål/Nynorsk-style split, but the audio sources carry an accent spread: Commons/Lingua Libre and LibriVox include Belgian, Swiss and Québécois readers alongside metropolitan French — flag this for pronunciation modelling. Wikisource and LibriVox lean literary/historical register with pre-1990 orthography and period-era attitudes (marked historical-context); Wikipedia, Vikidia, Tatoeba and Wikibooks are contemporary standard French. Sensitivity is 'none' for the modern/encyclopedic sources and 'historical-context' for the public-domain literary ones (Wikisource, LibriVox). editorial_independence is 'community' across all entries (Wikimedia projects, Tatoeba, LibriVox volunteers, Association Vikidia).

No files were edited — this is a catalogue+verify pass; entries are returned here for the caller to integrate into the registry.

**Category gaps:** video-drama, literature-graded


## ru — Russian  (19 entries)

Russia's media landscape after 2022 remains severely constrained and this dominates the whole picture. Every genuinely independent Russian-language newsroom now operates in EXILE (Riga, Berlin, Amsterdam, Tbilisi) — Meduza, Novaya Gazeta Europe, plus unlisted peers (IStories/Важные истории, Mediazona, Holod, The Bell) — and is blocked inside Russia and typically branded 'foreign agent'/'undesirable'. In-country broadcast (Channel One, VGTRK/Rossiya, RT, Sputnik) is state-controlled and correctly excluded as propaganda. CONSEQUENCE: there is NO in-country, non-partisan Russian broadcaster to catalogue; the pool necessarily rests on exiled independents, foreign public-service broadcasters (BBC Russian; DW Russian at dw.com/ru is an equivalent, also blocked in RU), and the US-funded RFE/RL (Radio Svoboda) for live radio. IMPORTANT INTEGRITY POINTS from this review: (1) RFE/RL was mislabelled 'public-service' in the draft entry despite the draft's own flag calling it state-controlled — corrected to state-controlled; it also carries a genuine liveness/viability risk (2025 USAGM cuts, 2026 restructuring) and could not be re-fetched this run, so a course should not treat it as a guaranteed-stable live stream. (2) Both Arzamas entries were access=free despite a real 'Гусьгусь' paywall — corrected to mixed. (3) The Russian National Corpus is a Russian state-academic (RAS) product; retained as an apolitical reference corpus but its origin is disclosed. (4) Журнальный зал is live but was showing a technical-maintenance banner — flag for stability monitoring. (5) The LibriVox Russian browse URL could not be verified and is low-confidence. TOOLING LIMITATION (disclosed honestly): the session's web-search budget was fully exhausted (200/200) before this review began, so verification relied on opportunistic WebFetch (several sites 403-block bots) plus model knowledge to a Jan-2026 cutoff; four sites were directly fetch-confirmed live, the rest rest on prior knowledge. Variant: media Russian is highly standardised (Moscow/literary ru-RU); regional dialect spread in these sources is minimal, so ru-RU coverage is strong but there is little regional variety to offer. CATEGORY GAPS (honest, 3 of 12 unfilled): (1) news-simplified — no public-broadcaster graded-news product equivalent to NHK News Web Easy exists for Russian; CEFR-graded/simplified Russian is all commercial (RussianReading, FluencyDrop, etc.) and excluded, so Tatoeba (A1-B1 sentences) and Arzamas kids are the closest low-level authentic substitutes. (2) music — no strong institutional, non-commercial, non-state archive of Russian music WITH published lyrics; partial substitutes are a-pesni.org (amateur folk/bard/revolutionary lyric archive), song texts on Russian Wikisource, and IMSLP for public-domain art-song scores; the state culture portal culture.ru hosts folk recordings but is state-controlled. (3) literature-graded — only commercial graded readers exist; none from a public/institutional source. STRENGTHS: literature-public-domain, transcript-corpus and classic video-drama are unusually well served for Russian (Mosfilm's free official archive, RNC multimedia/spoken subcorpora, Wikisource + LibriVox), and Tatoeba + Arzamas kids partially rescue the otherwise weak A1-A2 authentic-audio end.

**State-controlled / not recommended:**
- Radio Svoboda / Настоящее Время (RFE/RL) — US-government-funded (USAGM) international broadcaster; editorially independent by charter but NOT an in-country independent voice. editorial_independence corrected public-service -> state-controlled. Viability risk: 2025 USAGM funding cuts + May 2026 restructuring/service merger; liveness not independently re-confirmed (WebFetch 403). Blocked and 'undesirable' in Russia.
- Mosfilm — Golden Collection — Russian state-owned film studio. Catalogue value is classic Soviet/Russian cinema, not news; curate apolitical classics (comedies, melodramas). Some Soviet-era films carry period ideology — treated as historical-context. Kept for cultural/authentic-dialogue value under state-controlled flag.

**Flags:**
- `registration-gated` — Russian National Corpus (ruscorpora.ru): Core concordance search is open; some downloads/saved-query features require a free account. Also note: run by a Russian state (RAS) academic institute — kept editorial_independence 'academic' (reference corpus, not a broadcaster) but state-academic origin disclosed.
- `paywalled` — Arzamas (Арзамас): Freemium: substantial free web tier, but much premium audio behind the paid 'Гусьгусь' subscription (~299-399 RUB/month). access corrected free -> mixed.
- `paywalled` — Arzamas — Детская комната / Гусьгусь: Freemium: free web selection remains, most expanded children's audio in the paid 'Гусьгусь' app. access corrected free -> mixed.
- `sensitivity` — Meduza (Медуза): news-general. Designated 'foreign agent' (2021) and 'undesirable organisation' (2023) in Russia and blocked domestically; freely reachable outside RU. In-country use needs mirror/VPN/app; content must carry the legally-required foreign-agent notice.
- `sensitivity` — BBC News Русская служба: news-general. Public-service and editorially independent, but blocked inside Russia (mirror/VPN needed for in-country learners).
- `sensitivity` — Novaya Gazeta Europe (Новая газета Европа): news-general. Independent, exiled (Riga); blocked inside Russia. War/repression-heavy focus — tag topics so a course can pick non-conflict material.
- `sensitivity` — Подкасты Медузы (Meduza Podcasts): news-general. Same exiled-independent status as Meduza; no published transcripts (limited low-level scaffolding).
- `sensitivity` — Arzamas (Арзамас): historical-context. Historical/cultural topics may carry period-typical framing.
- `sensitivity` — Mosfilm — Golden Collection: historical-context. Some Soviet-era titles carry period ideology; curate apolitical classics.
- `sensitivity` — Викитека (Russian Wikisource): historical-context. Public-domain classic/historical texts may contain period prejudice.
- `sensitivity` — LibriVox — Russian audiobooks: historical-context. Public-domain classics; same period-language caveat as the source texts.

**Registration-gated (free account; verify manually):**
- Russian National Corpus (ruscorpora.ru) — https://ruscorpora.ru/

**Wikimedia:** All 8 entries verified on 2026-07-22 against authoritative Special:Statistics / MediaWiki API / canonical category pages (WebSearch budget was exhausted, so verification was done via WebFetch on deterministic Wikimedia endpoints).

STRONG / core:
- ru.wikisource.org — very strong: 622,814 texts, ~803M words, full classical canon (Pushkin, Tolstoy, Dostoevsky, Chekhov, Gogol, Turgenev, Lermontov). The flagship literature-public-domain source for Russian.
- ru.wikipedia.org — very strong: 2,110,653 articles, ~1.2B words; the canonical modern monolingual text corpus (transcript-corpus), one of the largest Wikipedias.
- Commons Category:Russian_pronunciation — strong A1–A2 pronunciation bank; ~28,230 Lingua Libre clips plus alphabet/phrases/names subcats.
- Tatoeba rus — strong text corpus (~1.22M aligned sentences), though audio is thin (~10,652 clips).

EXISTS BUT NICHE / SMALL (included with honest caveats):
- Spoken Wikipedia 'Аудиостатьи' — real but only 174 recorded articles; slow-moving.
- Russian Vikidia (ru.vikidia.org) — the A2–B1 children's-encyclopedia slot IS filled and the wiki is live/active, but it is very small (only 277 articles) and is an independent project, not a WMF one. Coverage is thin.
- ru.wikibooks.org — modest (3,251 pages) but qualifies: it has a genuine language-learning shelf, incl. 'Русский язык как иностранный' (Russian as a Foreign Language), an English self-teacher, 'First 1000 English words', Irish, Chuvash and several conlangs. Quality uneven / many books incomplete.
- LibriVox Russian — confirmed to exist (Russian is among LibriVox's 90+ languages; all public-domain), but the collection is small and its exact size could not be machine-verified because librivox.org returns 403 to automated fetches; existence was confirmed via LibriVox's documented multilingual catalogue.

REGISTER / DIALECT CAVEATS:
- Everything is Standard (literary) Russian; no Belarusian/Ukrainian mixing.
- Wikisource's chief caveat is ORTHOGRAPHY, not dialect: many 19th-century and all pre-1918 texts use the pre-reform script (ъ, ѣ, і, ѳ), which differs visibly from modern spelling and raises reading difficulty independent of vocabulary — flag this for learners. LibriVox classical readings carry the same historical-context flag (period attitudes in 19th-c. literature).
- Wikipedia/Wikibooks/Vikidia/Tatoeba use contemporary orthography.

No fabricated entries; every project was individually confirmed live. Nothing in the Wikimedia family relevant to Russian was found to be absent — the four canonical projects (Wikisource, Wikipedia, Wikibooks, Commons audio) plus Spoken Wikipedia, Vikidia, Tatoeba and LibriVox are all present, with size the main differentiator.

**Category gaps:** news-simplified, music, literature-graded


## es — Spanish  (19 entries)

After removing the dead Practica Español, this is a lean 14-entry Spanish pool. Public broadcasting remains the backbone and its editorial standing is clean: RTVE (Spain), SBS (Australia), RTVC/Señal Colombia, INCAA/CINE.AR and Canal Once/IPN are all domestic public-service or public-institution sources with charter or parliamentary editorial independence — there is NO state-controlled international propaganda outlet in the list (correctly, no HispanTV, RT en Español or Sputnik Mundo appears), so no entry required a 'state-controlled' relabel. Regional variety is genuinely spread: es-ES (RTVE cluster, CVC, Cervantes Virtual, 20minutos), es-MX (Once Niñas y Niños), es-CO (RTVCPlay), es-AR (CINE.AR), plus pan-Hispanic es-419 (Radio Ambulante) and corpus/lyric sources (CORPES XXI, Cancioneros) and an international service (SBS). Transcript/subtitle coverage is a real strength (Radio Ambulante full transcripts, RTVE legal subtitling, CVC graded readers with activities). REMAINING GAPS: (1) news-simplified is now EMPTY — the death of Practica Español leaves no dedicated CEFR-graded authentic-news source; CVC Lecturas covers graded reading but not news. A replacement should be researched when a search budget is available (candidates to vet: RTVE 'Aprende español', VeinteMundos, or a revived Practica Español archive; commercial 'News in Slow Spanish' remains excluded under the commercial-platform ban). (2) print-press is thin — 20minutos is the only entry and its content licence is unverifiable. (3) No verified C2-only reading/listening anchor beyond literary/corpus material. Previously excluded and endorsed as correct: Pakapaka (2025 politicization — editorial-independence concern) and Notes in Spanish (individual-creator commercial course). VERIFICATION CAVEAT: the session's WebSearch budget was already fully exhausted (200/200) at the start of this review, so no snippet-based currency cross-checks were possible; verification was done instead by direct DNS/HTTP probing (which is how the Practica Español death was caught) and WebFetch. Several publisher domains block automated fetches (rae.es and cervantesvirtual.com return 403; 20minutos.es blocks WebFetch) — those were confirmed live via HTTP-200 status probing rather than full content fetch.

**State-controlled / not recommended:**
- RTVE Noticias — Spain's public broadcaster, state-owned and parliament-governed but editorially public-service (not propaganda) — 'public-service' correct, no reclassification. General news inevitably covers elections, conflict and crime; steer courses with topic_tags toward economy/culture/science.
- RNE Audio (Radio Nacional de España / RTVE) — RTVE public radio; live streams unsubtitled and native-pace, so advanced-listening only. Same public-service (not state-controlled) status as RTVE.
- RTVE Play — Documentales — Public-service catalogue; most titles subtitled by accessibility law, but some documentaries are geo-restricted to Spain.
- RTVE Clan (Infantil) — Public-service children's portal relaunched early 2026 as a walled garden inside RTVE Play; some content geo-restricted to Spain; pre-reader content often unsubtitled.
- SBS Spanish (SBS en español) — Australian public multicultural broadcaster: government-funded but editorially independent by charter, so 'public-service' (not state-controlled). General news; not every podcast is transcribed. Canonical URL is the /es-suffixed path.
- RTVCPlay / Señal Colombia — Colombia's public-media platform (RTVC). Domestic public-service, not international propaganda; subtitle coverage inconsistent (B1+ recommended).
- CINE.AR Play (INCAA, Argentina) — Free but requires a registered account to stream; some titles geo-restricted to Argentina. Public film-institute (INCAA) content, editorially public-service. Fast colloquial rioplatense speech -> B2+; select age-appropriate titles.
- Once Niñas y Niños (Canal Once / IPN, México) — Public educational broadcaster run by a public university (IPN). Public-service, not propaganda; subtitling varies by title.

**Flags:**
- `sensitivity(news-general)` — Radio Ambulante: Independent nonprofit narrative-journalism podcast (no longer NPR; iHeartMedia distribution). Individual episodes cover migration, dictatorship, violence and trauma — tag and select episodes; not all suit lower levels or sensitive learners.
- `sensitivity(news-general) + licence-uncertain` — 20minutos: Mainstream free daily (Henneo). General news including crime and politics — select topics via tags. Content licence could not be freshly verified (historically CC BY-NC-SA), hence licence='unknown'.
- `sensitivity(historical-context)` — Biblioteca Virtual Miguel de Cervantes: Public-domain literary classics: period texts carry historical prejudices typical of their era — frame for context. High-register C-level reading.
- `sensitivity(copyright + political-context)` — Cancioneros.com: Song lyrics are copyrighted (all-rights-reserved) — catalogue for reference/read-along only, do not redistribute. Cantautor / nueva canción repertoire includes politically-engaged protest songs; treat as cultural/historical context.

**Registration-gated (free account; verify manually):**
- CINE.AR Play — https://play.cine.ar/

**Wikimedia:** Catalogued + verified 8 Wikimedia-family Spanish sources on 2026-07-22 (all Wikimedia domains reliably live; verified via WebFetch on Special:Statistics pages, MediaWiki action-API calls, the Tatoeba stats table/API, and the Internet Archive advancedsearch API — the shared session web-SEARCH budget was already exhausted, so all figures come from direct fetches, not search snippets).

STRONG / flagship: es.wikipedia (2,126,764 articles — a top-tier edition, the canonical monolingual corpus), es.wikisource (89,149 content pages of rich PD Spanish literature), Wikimedia Commons Spanish pronunciation (672 direct files plus a Lingua Libre subcategory of ~19,002 clips — a deep A1-A2 pronunciation bank), and Tatoeba Spanish (443,942 sentences, 119,430 with native-speaker audio). LibriVox Spanish is solid (544 PD audiobooks on the Internet Archive under collection:librivoxaudio language spa; LibriVox language id = 5).

MODERATE but genuine: Vikidia ES (7,704 articles, 23 active editors) — the learner-friendly kids encyclopedia and the A2-B1 sweet spot; note there is NO Spanish Simple Wikipedia (Simple Wikipedia is English-only), so Vikidia is the intended Simple/kids variant for Spanish. Spanish Spoken Wikipedia exists as a separate entry: Categoría:Wikipedia:Artículos grabados = 424 recorded articles (audio + full article-text transcript), but it is small and only sporadically extended.

CAVEAT / weakest inclusion: es.wikibooks (9,719 content pages) has NO dedicated Español-como-lengua-extranjera shelf equivalent to German Wikibooks' Regal:Deutsch als Fremdsprache (confirmed absent via API). It is included under literature-graded as a general open-textbook collection written in Spanish plus a few language-course books (Español, Curso de alemán, Finés, Esperanto, Lojban); quality varies and it is a source to adapt rather than a structured ELE course.

ABSENT: no Spanish Simple Wikipedia; no Klexikon/Wikikids-type separate kids wiki beyond Vikidia.

REGISTER / DIALECT caveats: Spanish Wikimedia content is pan-Hispanic — it blends Peninsular (Castilian) and Latin American varieties. Pronunciation audio and spoken-Wikipedia recordings vary by contributor accent (distinción vs seseo, voseo, etc.), so they double as a natural accent-exposure resource but are not a single-standard model. Wikisource and LibriVox lean toward Golden Age / 19th-century literary registers (Cervantes, Quevedo, Góngora; then Bécquer, Martí, Darío) with archaic, period language and occasional colonial-era prejudice — hence historical-context sensitivity on those two; the encyclopedic and example-sentence corpora (Wikipedia, Vikidia, Tatoeba, Commons, Wikibooks) are contemporary and marked sensitivity none.

Licence notes: Wikisource works and LibriVox recordings are public-domain (Wikisource transcriptions/platform are CC BY-SA 4.0); Wikipedia/Wikibooks/Vikidia/spoken-Wikipedia are CC BY-SA (Vikidia 3.0, the rest 4.0); Commons pronunciation is mixed-CC (mostly CC BY-SA 4.0 with some CC0/CC BY — check per file); Tatoeba sentences are CC BY 2.0 with some CC0.

**Category gaps:** news-simplified

**Dropped in QA:** Practica Español (Agencia EFE / Fundación de la Lengua Española) (Dead/unreachable. practicaespanol.com fails DNS resolution from all major public resolvers (SERVFAIL on Google & Quad9, no-answer on Cloudflare). The .com delegation still points to ns1/ns2.efe.es, but those authoritative servers no longer serve the zone (root-hint referral, no SOA/A record) — a lame delegation — so no client can reach the site (curl HTTP 000). Consistent with the known shutdown of the EFE/Fundación de la Lengua Española ELE project. This was the sole news-simplified source.)


## tr — Turkish  (19 entries)

Turkish media is heavily polarised and state-dominated, which shapes this list. The domestic public broadcaster TRT and the state wire Anadolu Ajansı are pro-government rather than editorially independent, so Turkey effectively lacks a fully non-partisan DOMESTIC public broadcaster. The honest recommendation for non-partisan news therefore leans on international broadcasters (BBC News Türkçe, DW Türkçe) — but note that both have been RECLASSIFIED here from public-service to state-controlled, because each is a state-funded international broadcaster (BBC WS via UK/FCDO grant; DW via the German federal budget); they retain guaranteed editorial independence, so the label reflects funding/governance while they remain the recommended non-partisan option. DW's site is blocked inside Turkey (2022 RTÜK dispute). Independent domestic outlets exist (Bianet is catalogued; T24, Medyascope, Gazete Duvar noted) but skew advocacy/opposition and operate under pressure; Açık Radyo, Istanbul's flagship independent radio since 1995, had its RTÜK licence revoked in 2024 and was deliberately left off as a longevity risk. TRT's NON-news output is the pedagogically safe and reliable part of the state offering: TRT Çocuk is a top-tier A1-A2 resource, and TRT's streaming has rebranded from TRT İzle to 'tabii' (freemium, strong multi-language subtitles), though some TRT historical dramas/documentaries carry nationalist framing and should be vetted. TWO STRUCTURAL GAPS remain: (1) SIMPLIFIED NEWS is only nominally covered — the sole option, 'News in Simple Turkish', was discontinued in June 2024 and now survives only as a frozen (but script-rich) archive; there is NO live NHK-Easy equivalent in Turkish. (2) TRANSCRIPTS/SUBTITLES — very few Turkish broadcasters publish authored transcripts, so the transcript-corpus category (OPUS OpenSubtitles/SETIMES/TED, Tatoeba with CC-BY audio) carries the load for aligned spoken-language text. OPENLY-LICENSED material is limited to Tatoeba (CC-BY), Vikikaynak (public-domain / CC-BY-SA annotations) and OPUS (mixed per-corpus); everything else is all-rights-reserved (link-only). DIALECT: uniformly standard Istanbul Turkish (tr-TR); regional variety appears mainly in folk material (Kültür Portalı türküler) and casual drama dialogue on tabii. Music with published lyrics is thin — modern song lyrics are copyright-locked, so the viable institutional source is the Culture Ministry's public-domain türkü archive. VERIFICATION CAVEAT: WebSearch was unavailable this session (shared 200/200 cap already spent), so no fresh discovery searches were possible; currency was re-checked via WebFetch (most entries confirmed live) plus established knowledge, and bbc.com, dw.com and turkce.yee.org.tr could not be fetched (host blocks / TLS error) and were confirmed from prior verification. All URLs are the current canonical ones as of 2026-07-22.

**State-controlled / not recommended:**
- BBC News Türkçe — Reclassified from public-service: BBC World Service is a state-funded international broadcaster (UK/FCDO grant funds language services). Retains Royal-Charter-guaranteed editorial independence and remains the recommended non-partisan option; the label reflects funding/governance, not the editorial line. Live globally; in-country access in Turkey may vary (not re-verified this session). sensitivity news-general.
- DW Türkçe — Reclassified from public-service: Deutsche Welle is funded from the German federal budget (state-funded international broadcaster). Retains statutory editorial independence (DW-Gesetz); recommended non-partisan source. Website blocked inside Turkey since the 2022 RTÜK licensing dispute; live globally. sensitivity news-general.
- TRT Haber — Turkey's state broadcaster with a pro-government editorial line. Confirmed live in-country. Catalogue for language quality; restrict to economy/sport/culture via topic tags, NOT political/campaign coverage. sensitivity news-general.
- TRT Radyo (canlı) — State broadcaster; Radyo 1 news segments carry state framing, music/culture networks (Radyo 3, TRT Türkü, TRT Nağme) are low-risk. sensitivity news-general.
- TRT Dinle — State-produced audio-on-demand; culture/history/documentary catalogue largely apolitical but institutionally state-run. sensitivity none.
- tabii — TRT streaming service (former TRT İzle). Some historical epics carry nationalist/pro-government framing; vet individual series. sensitivity corrected to none (entertainment).
- TRT Belgesel — TRT documentary channel; nature/science titles safe, historical/political documentaries can carry nationalist framing. sensitivity corrected to none.
- TRT Çocuk — State broadcaster's kids' channel; content benign and pedagogically strong (A1-A2). Flagged for completeness, not as a content concern. sensitivity none.

**Flags:**
- `sensitivity` — Bianet: Genuinely independent (JTI-certified, IPS Vakfı/SIDA-supported) but rights-based/advocacy-leaning (human rights, Kurdish affairs, gender, LGBTQ+, labour). Retained as legitimate journalism; select neutral coverage, do not use as default. editorial_independence private-independent; sensitivity news-general.
- `sensitivity` — Vikikaynak (Turkish Wikisource): historical-context: includes Ottoman-era and older literary texts with period-typical language and prejudice; screen individual texts before classroom use.
- `other` — News in Simple Turkish: DISCONTINUED 28 June 2024; retained as an archived resource. ~166-episode archive with full scripts still accessible free on Spotify; former paid premium tier defunct. Only simplified-news option for Turkish, but no longer current or updated.
- `registration-gated` — tabii: Freemium: ad-supported free tier requires a free account, and some titles are premium/paid.
- `registration-gated` — Yunus Emre Enstitüsü portal: Free account required for the full portal/courses (learnturkish.com login). Turkish government-funded cultural institute; pedagogical content neutral, retained as public-service. Fresh fetch blocked by a TLS certificate-chain error; confirmed live via prior high-confidence verification.
- `other` — Kültür Portalı: Ministry of Culture (.gov.tr) heritage portal, directly state-operated; folk-culture content is neutral but the compilation is government-held. Traditional türkü lyrics are effectively public-domain, the portal presentation is not. Retained as public-service (non-broadcaster heritage database).

**Registration-gated (free account; verify manually):**
- tabii — https://www.tabii.com/
- Yunus Emre Enstitüsü — Türkçe Öğretim Portalı — https://turkce.yee.org.tr/

**Wikimedia:** VERIFIED (all live 2026-07-22, checked via Special:Statistics / canonical category pages / archive.org advancedsearch):

STRONG & INCLUDED (5 entries):
- Vikipedi (tr.wikipedia): 691,309 articles, 44,742 files, 4,296 active editors — a large edition and the canonical monolingual Turkish corpus; formal Istanbul-standard encyclopedic register (B2-C2). CC-BY-SA. Was blocked in Turkey 2017-2020, now open.
- Vikikaynak (tr.wikisource): 19,893 content texts. Deep public-domain literature — İstiklal Marşı, Mehmet Akif Ersoy (Safahat), Namık Kemal, Tevfik Fikret, Ziya Gökalp, Tanzimat/Republican-era works, folk texts, official documents. REGISTER CAVEAT: heavy Ottoman-Turkish vocabulary and pre-1928/early-Latinised orthography push real difficulty to C1-C2; sensitivity flagged historical-context.
- Commons Category:Turkish_pronunciation: 275 direct files + subcat 'Lingua Libre pronunciation-tur' (6,572 single-word clips) and 5 other subcats. Mixed CC per file (CC0/CC-BY/CC-BY-SA). A1-A2 pronunciation bank.
- Vikikitap (tr.wikibooks): 1,099 content pages, ~96 complete books, ~10 active editors. Confirmed a genuine language/textbook shelf (main-page 'Dil' shelf + Kategori:Diller with Almanca, İngilizce, Japonca, Rusça, etc.), so it qualifies as literature-graded — but thin and low-activity; books are authored in Turkish (best as B1+ reading for Turkish learners). CC-BY-SA.
- Tatoeba Turkish: 748,502 sentences (7th-largest on Tatoeba), 1,141 with audio. CC-BY-2.0. A1-B1 everyday sentences with translations.

VERIFIED ABSENT / OMITTED (do not invent):
- Learner-friendly kids/simple encyclopedia (children-youth): NONE for Turkish. tr.vikidia.org does not resolve (ENOTFOUND) — Vikidia has no Turkish edition; Simple English Wikipedia is English-only; no Turkish equivalent (Klexikon=de, Wikikids=nl) exists. No entry produced.
- Spoken Wikipedia (Sesli Vikipedi / gesprochene Wikipedia): NO active project. Tried Vikipedi:Sesli_maddeler, Kategori:Sesli_maddeler and Kategori:Seslendirilmiş_maddeler — all HTTP 404. No organised narrated-article corpus for Turkish, so no separate podcast/audio entry.
- LibriVox Turkish: NO recordings. archive.org advancedsearch (collection:librivoxaudio AND language:Turkish, and AND language:tur) both return numFound 0. Turkish is not in the LibriVox catalogue; omitted.

REGISTER/DIALECT CAVEATS: All entries are standard (Istanbul) Turkish; there is no Bokmål/Nynorsk-style split. The main pedagogical hazard is diachronic, not regional: Wikisource skews Ottoman-Turkish/archaic (hardest), Wikipedia is modern formal, Tatoeba is short everyday register (easiest), Commons audio is isolated single words. CEFR estimates are curator heuristics — no Wikimedia project carries official CEFR labelling. WebSearch budget was exhausted at session start; every verification above was done with direct WebFetch against deterministic Wikimedia/Tatoeba/archive.org endpoints.


## ja — Japanese  (16 entries)

Japan's free, quality, learner-usable authentic media is overwhelmingly dominated by NHK, the public broadcaster (8 of 13 entries). NHK is licence-fee funded and editorially independent under the Broadcasting Act, correctly classified public-service (NOT state-controlled); its government-funded international, English-narrated arm NHK World-Japan — the one service that would carry state-controlled/state-funded-international flags — is rightly excluded. No propaganda, advocacy, extremist, or commercial language-learning source was present or needed. VERIFICATION HEALTH OF THIS QA PASS: honestly, this was a constrained pass. The WebSearch budget (200 calls) was ALREADY fully spent by the researcher before review began, so I could run zero searches; I verified via WebFetch instead. WebFetch confirmed 5 sources live and matched the draft's precise figures for Aozora, Wikisource, Tadoku, CSJ and Tatoeba — those are solid. But WebFetch is hard-blocked for every NHK domain and returns only an empty SPA for TVer, so the 8 NHK/TVer entries could not be independently re-confirmed this pass and lean on the researcher's earlier verification plus stable-URL knowledge; they should be re-checked once search budget returns. CURRENCY RISK concentrates on the reported 'NHK ONE' platform migration (nhk.jp) — a real-sounding but unconfirmed consolidation that could move radio/plus/minna/school URLs; I downgraded the らじる entry from an asserted 'redirect' to 'live' and reworded the NHK ONE claims as reported rather than settled. ACCESS REALITY for audio-visual is the systemic constraint: the deep archive (NHK On Demand) is paywalled and correctly excluded, while the free AV options (NHK Plus, TVer) are geo-locked to Japan with short catch-up windows and patchy captions — so abroad, learners are effectively limited to text/audio (News Web Easy, radio, podcasts, Aozora, Wikisource, Tadoku) plus the corpora. TRANSCRIPT/SUBTITLE alignment is the other weak spot: broadcast 字幕 exist but are rarely exposed in free web streams, so the strongest text-audio pairing sits in News Web Easy, Tadoku and the academic corpora (CSJ, Tatoeba), not the AV sources. MUSIC is thin (Minna no Uta only, with non-uniform lyric access) and TATOEBA is the weakest entry (crowdsourced), kept only because it uniquely fills the open-licence beginner-audio niche. REMAINING GAP: print-press is genuinely missing — every major daily (Asahi, Yomiuri, Mainichi, Nikkei) hard-paywalls, and the free wire aggregators (Kyodo/47NEWS, 時事ドットコム Jiji) could not be verified with no search budget; reported as a documented gap rather than padded, and NHK NEWS WEB text already covers the free standard-news-reading need. DIALECT: only standard ja-JP is catalogued; regional dialects (Kansai etc.) appear only incidentally in TVer drama/variety. FOLLOW-UPS for the next budgeted pass: (1) confirm/correct all NHK URLs against the NHK ONE migration; (2) re-verify TVer live; (3) probe Japan Foundation Hirogaru/free graded resources and a dedicated lyrics-with-audio music source; (4) attempt to verify Kyodo/47NEWS/Jiji for print-press.

**Flags:**
- `editorial-independence` — NHK (all domestic services: News Web Easy, News Web, らじる, radio-news podcast, NHK Plus, Minna no Uta, NHK for School): Classified public-service, NOT state-controlled. Licence-fee funded and editorially independent under Japan's Broadcasting Act (放送法); analogous to the BBC. The government-subsidised international arm NHK World-Japan (which WOULD be state-funded-international) is deliberately excluded from this list, so no state-controlled reclassification applies.
- `sensitivity` — NHK NEWS WEB EASY: news-general — mainstream news; simplified but still covers disasters, crime and politics. Use topic_tags (culture, economy, science) to select neutral material for course seeding.
- `sensitivity` — NHK NEWS WEB: news-general — standard-register mainstream news covering politics, disaster, conflict and elections.
- `sensitivity` — NHK らじる★らじる: news-general — live radio includes news/talk (Radio 1); no transcripts, so unscripted current-affairs content is unfiltered.
- `sensitivity` — NHKラジオニュース (podcast): news-general — broadcast news bulletins.
- `sensitivity` — NHKプラス (NHK Plus): news-general — documentary/current-affairs strands (NHKスペシャル) cover crime, disaster and politics.
- `sensitivity` — 青空文庫 (Aozora Bunko): historical-context — pre-war and wartime public-domain literature can contain period-typical prejudicial language and attitudes; screen individual works before course use.
- `sensitivity` — 日本語ウィキソース (Japanese Wikisource): historical-context — includes pre-war literature and historical/legal documents that can carry period-typical language; screen per text.
- `registration-gated` — NHKプラス (NHK Plus): Requires a free NHK account to stream AND is geo-restricted to Japan with a ~1-week catch-up window — high value for learners in-country, effectively blocked abroad. Could not be re-confirmed this pass (NHK domain WebFetch-blocked).
- `registration-gated` — Corpus of Spontaneous Japanese (CSJ): Online Chunagon access requires application to NINJAL; the full offline dataset is a paid USB set. Free-online + paid-USB model confirmed live on the NINJAL page 2026-07-22. Research-use licence (recorded as 'unknown' pending explicit terms).
- `geo-restricted` — TVer: Geo-restricted to Japan; ~1-week per-episode catch-up window; inconsistent captions; distribution platform, so titles rotate off. Loaded as a JS SPA on WebFetch (no error) but content could not be re-read this pass.
- `currency` — NHK 'NHK ONE' consolidation: NHK is REPORTEDLY merging らじる★らじる, NHK Plus and programme pages under an 'NHK ONE' umbrella (nhk.jp) across 2025-2026 (draft cited a 2026-03-30 らじる rebrand). This could NOT be independently confirmed — NHK domains are WebFetch-blocked and search budget was exhausted — so several NHK URLs (radio, plus, radionews, minna, school) are best-effort canonical and MUST be re-verified before seeding courses. Article-level paths like www3.nhk.or.jp/news/easy/ have historically persisted.
- `other` — Minna no Uta lyric availability: On-screen lyric captions appear during songs, but full lyric text and the deep back-catalogue audio are not uniformly free online (some archive paywalled) — verify lyric availability per song before use.

**Registration-gated (free account; verify manually):**
- NHKプラス (NHK Plus) — https://plus.nhk.jp/
- Corpus of Spontaneous Japanese (CSJ) — https://clrd.ninjal.ac.jp/csj/en/

**Wikimedia:** Verified 2026-07-22. NB: the WebSearch budget was already exhausted at session start, so all verification was done with WebFetch against deterministic Wikimedia/Commons/Tatoeba/archive.org endpoints (Special:Statistics, category pages, Tatoeba list, Internet Archive advancedsearch API).

STRONG for Japanese: ja.wikipedia (1,511,044 articles — the flagship monolingual corpus), ja.wikisource (18,355 PD texts), Tatoeba jpn (249,096 sentences, much with audio), Commons Japanese-pronunciation audio (251 direct files + Lingua Libre 1,043 recordings). PRESENT but niche: ja.wikibooks (17,776 pages; real 語学 shelf, but oriented to Japanese speakers learning OTHER languages rather than Japanese-as-target) and LibriVox Japanese (37 PD audiobooks — small but genuine, e.g. Sōseki, Dazai, Ogawa Mimei).

ABSENT (omitted, do not invent): no Japanese Vikidia (ja.vikidia.org does not resolve — DNS ENOTFOUND); no Simple/やさしい Japanese Wikipedia edition; no Klexikon/Wikikids equivalent. The children-youth encyclopedia slot has NO Japanese member, so it is left out entirely.

SPOKEN WIKIPEDIA — excluded on the 'active' bar: a Japanese spoken-articles category exists on Commons (Category:Spoken Japanese Wikipedia, last edited 2025-03-04) but holds only 2 recordings (藤村紀雄, タチバナ). That is effectively moribund, so it is NOT given its own entry per the 'genuinely active' rule; noted here for completeness.

REGISTER / ORTHOGRAPHY caveats: Wikisource and LibriVox literary texts are largely Meiji–Shōwa era and frequently use historical kana (歴史的仮名遣い) and old kanji forms (旧字体), which pushes reading/listening difficulty to C1–C2 and carries period attitudes → sensitivity 'historical-context'. All Wikimedia Japanese text is standard Japanese (共通語 / 標準語); there is no dialectal edition and no orthographic split comparable to Norwegian Bokmål/Nynorsk — the only 'variant' axis is modern vs. classical/historical orthography within the PD-literature sources.

NON-WIKIMEDIA COMPLEMENT worth flagging: Aozora Bunko (aozora.gr.jp) is the principal public-domain Japanese literature archive and is substantially larger than ja.wikisource; it is the natural non-Wikimedia partner for the literature-public-domain category. Editorial_independence is 'community' for every entry (volunteer-run projects).

**Category gaps:** print-press


## fa — Persian  (18 entries)

VERIFICATION CONSTRAINT: the shared WebSearch budget was already at 200/200 when this QA began (the same cap the researcher reported hitting), so I could not run fresh discovery/verification searches. Verification relied on direct WebFetch, which succeeded for Euronews Persian, Radio Zamaneh, Donya-e-Eqtesad, Ketabak, Golha, Ganjoor, Persian Wikisource and Tatoeba (all confirmed live with 2026 content), and returned CDN 403s for BBC Persian, DW Persian, Radio Farda and Radio Azadi (expected — those publishers block automated fetch), which are retained live on strong prior evidence. Currency of the Common Voice hours figure could not be re-confirmed (client-rendered SPA). INDEPENDENCE GAP (confirmed): there is no genuinely independent, non-partisan Persian broadcaster operating inside Iran — IRIB (incl. PressTV and the Pooya & Nahal kids' channel) is fully state-controlled, and private dailies operate under Ministry of Culture licensing and self-censorship. The best independent journalism is diaspora-produced. Note that ALL of the broadcast spine is now flagged: BBC and DW are state-funded international broadcasters (relabelled state-controlled per the registry rule, though editorially independent), and the US-funded RFE/RL family (Farda, Azadi) is both state-controlled AND under existential funding pressure after the 2025 USAGM cuts. That leaves Radio Zamaneh (NL) as the one genuinely private-independent broadcast/news voice, and the classical/heritage/corpus sources (Ganjoor, Wikisource, Golha, Common Voice, Tatoeba, Ketabak) as the least-politicised material. Recommend leaning on BBC/DW for standard register with the state-funding caveat visible, Zamaneh for an independent editorial voice, and treating inside-Iran press (Donya-e-Eqtesad) as topic-tagged and censorship-caveated. VARIANTS: Iranian Persian (Perso-Arabic script) is the spine; Dari is represented only by the at-risk, US-funded Radio Azadi; Tajik (Cyrillic) is out of scope as effectively a separate learning target. CATEGORY GAPS (honest, all genuine): news-simplified — no public-broadcaster 'easy Persian' equivalent exists; the graded-Persian space is commercial (correctly excluded). literature-graded — no non-commercial graded readers. video-drama — Iranian TV/film drama (pedagogically ideal for colloquial register) is locked in paywalled commercial VOD (Filimo, Namava) or state IRIB, so no clean freely-accessible non-partisan source. These three categories are legitimately empty, not padding-worthy. WEAKEST KEPT ENTRIES: (1) Euronews Persian sits in video-documentary only by a generous reading — it is really a news channel; (2) Channel B is a single-creator podcast that appears dormant since ~Sept 2025 with an unresolved host attribution — both retained but flagged and worth re-checking on the next verification pass with search access restored.

**State-controlled / not recommended:**
- BBC News Persian — BBC World Service is part-funded by the UK government (FCDO grant / licence-fee settlement) — a state-funded international broadcaster. Editorially independent under the Royal Charter; tagged state-controlled per the registry rule. Usable as neutral spine but flagged.
- DW Persian — Deutsche Welle is funded entirely from the German federal budget — a state-funded international broadcaster. Editorially independent by the Deutsche-Welle-Gesetz; tagged state-controlled per the registry rule. Usable as neutral spine but flagged.
- Radio Farda — US-government-funded (RFE/RL via USAGM); editorially independent by US statute but a foreign soft-power outlet. Under acute funding threat since the March 2025 USAGM cuts — ongoing availability uncertain. Catalogued for language quality; NOT recommended as core pool material.
- Radio Azadi (Dari) — US-government-funded RFE/RL Afghan Service; editorially independent but foreign-funded. Banned inside Afghanistan by the Taliban (Dec 2024) and hit by the 2025 USAGM cuts — availability at risk. Included only to represent the Dari variant; not recommended as core material.

**Flags:**
- `sensitivity` — Ganjoor: historical-context: public-domain classical Persian poetry with period-typical imagery (wine, mysticism) and devotional content; register is C1-C2, not beginner material.
- `sensitivity` — Persian Wikisource: historical-context: period texts (prose, documents, periodicals) may carry period-typical attitudes; mixed licences under a CC-BY-SA wrapper; C1-C2 register.
- `sensitivity` — The Golha Project: historical-context: 1956–79 radio archive of classical music with sung/recited (often devotional) classical poetry; archaic/literary C1-C2 register.
- `sensitivity` — Channel B: Individual-creator podcast (not institutional); documentary/true-crime content narrates violent real events — curate at episode level. No transcripts. Host attribution unresolved (Ali Bandari vs. Mehran Bolhasani credited on site).
- `other` — Donya-e-Eqtesad: Privately owned but published inside Iran under Ministry of Culture press regulation and self-censorship; economy focus keeps political charge low, but editorial independence is constrained. Same caveat applies to all inside-Iran dailies (Etemad, Shargh, Hamshahri).
- `registration-gated` — Mozilla Common Voice — Persian: Browsing and contributing are free, but the bulk CC-0 dataset download (via Mozilla Data Collective) requires a free account and terms acceptance. Download URL: https://commonvoice.mozilla.org/fa/datasets

**Registration-gated (free account; verify manually):**
- Mozilla Common Voice — Persian (dataset download) — https://commonvoice.mozilla.org/fa/datasets

**Wikimedia:** Verified 2026-07-22 via WebFetch on deterministic Wikimedia/Tatoeba/Internet-Archive endpoints (WebSearch budget was exhausted, so all figures come from live page fetches of the projects' own statistics/category pages).

EXISTS AND STRONG:
- Persian Wikipedia (fa.wikipedia) — flagship: ~1.08M articles, ~275.7M words; the canonical monolingual Persian corpus. Very active.
- Persian Wikisource (fa.wikisource, ویکی‌نبشته) — ~29,490 content pages / ~14.8M words of public-domain classical literature (Shahnameh, Hafez, Saadi, Rumi, Nezami, Khayyam) plus historical/religious prose. Strong for advanced/classical reading.
- Commons Persian pronunciation audio — robust A1-A2 asset: ~693 files in the main category plus 'Lingua Libre pronunciation-fas' (~4,261 clips). Mixed CC licences.
- Tatoeba Persian (pes) — 31,776 sentences, partial audio; solid A1-B1 sentence corpus.

EXISTS BUT MODEST:
- Spoken Persian Wikipedia (نوشتارهای صوتی/گویا) — real but tiny: ~42 audio files tagged on fa.wikipedia, ~7 aggregated in Commons Category:Spoken Persian Wikipedia. Included as a separate podcast-style entry (audio+full-text transcript) with a caveat about size.
- Persian Wikibooks (ویکی‌کتاب) — ~3,555 content pages; a genuine textbook shelf but with uneven coverage and little dedicated L2-Persian coursework. Included as literature-graded with that caveat.

ABSENT (deliberately omitted):
- LibriVox Persian — NONE. Internet Archive advanced search over collection:librivoxaudio with language Persian/Farsi returned numFound=0. No Persian LibriVox recordings exist, so no entry.
- Learner-friendly / children's encyclopedia — NONE for Persian. Vikidia has no Persian edition (fr/en/es/it/eu/de/ru/ca/el/pt/hy/scn/oc only); Klexikon is German-only; Wikikids is Dutch-only; Simple English Wikipedia is English-only. No A2-B1 encyclopedic variant exists for Persian, so the children-youth slot is empty.

REGISTER/DIALECT CAVEATS:
- All fa.* projects and Tatoeba pes are Iranian/Western Persian (standard Farsi). Dari (Afghanistan, ISO prs) and Tajik (Cyrillic, ISO tg) are SEPARATE editions/languages — Dari has its own emerging content and Tajik uses Cyrillic; treat them independently, though some Dari contributions surface on fa.wikipedia.
- Wikisource/Wikipedia historical and classical texts use archaic, high-literary Persian and can carry period prejudice -> Wikisource flagged historical-context; ceilings lean B2-C2. Commons pronunciation is A1-A2; Tatoeba A1-B1.

NON-WIKIMEDIA ADJACENT (noted, not catalogued here): Ganjoor (ganjoor.net) is the definitive open corpus of classical Persian poetry (Ferdowsi, Hafez, Saadi, Rumi, Khayyam, Nezami) with per-poem audio recitations and is a strong complement to fa.wikisource for classical-literature study — worth a future non-Wikimedia entry.

**Category gaps:** news-simplified, video-drama, literature-graded


## no — Norwegian  (21 entries)

The draft was strong and largely accurate; this is a clean landscape with no removals needed. Norway has NO state-propaganda or state-controlled outlets in scope: NRK is a public-service broadcaster with statutory editorial independence (the Norwegian counterpart of the BBC), so no entry was downgraded to 'state-controlled', and the researcher's assessment on this point is confirmed. The list is legitimately NRK-heavy because NRK genuinely dominates quality across news, radio, podcast, documentary, drama and children's content - this reflects the market, not padding. The single concrete link fix was NRK Super's migration from nrksuper.no to tv.nrk.no/nrksuper (service consolidating into NRK TV). Two NRK browse/landing routes (podcast hub, documentary category) returned 404/400 to the automated fetcher, but individual content pages within those namespaces load normally, so the services are live - flagged as an SSR/anti-bot artifact rather than dead links. Verification note: this pass could not use WebSearch (session budget was exhausted at 200/200 before any query ran), so it relied on WebFetch, which is anti-bot-limited on NRK's SPA - the NRK landing-route statuses should ideally get a second confirmation with a browser or search when budget allows. Two-written-standard coverage is handled: Bokmaal dominates (NRK, Klar Tale, most sources) and Nynorsk (~10-15%) is represented by Framtida.no and Framtida Junior, whose Nynorsk-promotion mission is cultural/linguistic and non-partisan. Spoken Norwegian has no single standard - NRK deliberately airs many dialects, which is authentic but hard below B1; steer A1-B1 listeners to the clearer registers (Supernytt, NRK Super, Klar Tale lydavis). REMAINING GAPS: (1) literature-graded has no free institutional source - the commercial ban removes graded-reader publishers, and the nearest free substitutes are Klar Tale (paywalled) and Supernytt/NRK Super. (2) Free, non-paywalled print press is thin - mainstream dailies (Aftenposten, VG, Dagbladet, Dag og Tid) are largely paywalled, so Framtida.no (free, Nynorsk, youth) stands in for print-press. (3) Transcript-aligned listening is scarce and gated: the only good options are Klar Tale's lydavis (paywalled) and NoTa-Oslo (academic CLARIN licence) - there is no free, open, transcript-carrying podcast/radio source. (4) Access caveats for a foreign-based project: NRK TV video is often geo-blocked outside Norway and NB's in-copyright holdings need a Norwegian IP; the reliably worldwide-open pieces are NRK Radio (live + podcasts), Bokselskap.no and pre-1900 NB material. Sami-language media (NRK Sapmi etc.) is a separate language and correctly excluded from the 'no' registry.

**Flags:**
- `sensitivity` — NRK news services (Nyheter, Radio Direkte, Podkast, Dokumentar, Supernytt): news-general. Public-broadcaster news inevitably covers conflict, crime and elections; steer courses toward culture/economy/nature via topic_tags and screen individual documentary titles (crime, disaster). NRK is editorially independent by law (public-service), NOT state-controlled.
- `mature-themes` — NRK Skam: Contemporary teen drama containing sexuality, mental-health content and a sexual-assault storyline. sensitivity kept 'none' (does not fit news-general/historical-context/religious) but screen before classroom use.
- `editorial-mission` — Framtida.no: Nynorsk youth news/debate magazine (LNK; backed by Fagforbundet and Lotteritilskuddet). Self-declared editorially independent; its Nynorsk-promotion remit is cultural/linguistic, not partisan-political. sensitivity news-general. editorial_independence='community'.
- `editorial-mission` — Framtida Junior: Nynorsk children's news outlet (LNK/foundation funded). Same cultural-linguistic (non-partisan) Nynorsk-promotion mission; included for written-variant exposure. editorial_independence='community'.
- `sensitivity` — Bokselskap.no: historical-context. Classic Norwegian literature in older orthography with period-typical attitudes; advanced reading with framing, not neutral default material.
- `sensitivity` — Nasjonalbiblioteket - Nettbiblioteket / Bokhylla: historical-context. Also GEO-RESTRICTED: in-copyright material (roughly post-1900, Bokhylla/Kopinor deal) is read-online only and requires a Norwegian IP; pre-1900 public-domain works are open and downloadable worldwide.
- `sensitivity` — NB - Norske viser (Norsk visearkiv): historical-context. Older folk, revue and broadsheet songs carry period-typical content; simple folk lyrics still suit A2-B1.
- `paywalled` — Klar Tale: State-subsidised easy-read newspaper (Stiftelsen Klar Tale); full articles ('pluss') and the 'lydavis' audio sit behind a paid subscription, only some breaking news free. Highest-value transcript-aligned A2-B1 resource but budget a subscription.
- `registration-gated` — Spraakbanken - NoTa-Oslo: Spoken corpus under CLARIN academic non-commercial licence (CLARIN_ACA-NC-LOC-PRIV-ND); requires an academic/CLARIN/Feide agreement to access and cannot be redistributed. Teacher/curriculum resource, not learner-facing.

**Registration-gated (free account; verify manually):**
- Klar Tale (paid subscription for full content) — https://www.klartale.no/
- Spraakbanken - NoTa-Oslo (academic/CLARIN agreement) — https://www.nb.no/sprakbanken/en/resource-catalogue/oai-tekstlab-uio-no-nota-oslo/

**Wikimedia:** All figures verified 2026-07-22 via MediaWiki siteinfo/categoryinfo APIs, Tatoeba show_all_in headers, and Internet Archive advancedsearch (WebSearch budget was exhausted at session start, so verification was done against these deterministic Wikimedia/archive endpoints; librivox.org and the LibriVox API return HTTP 403 to automated fetches, so LibriVox was verified via archive.org instead).

STRONG / core entries:
- Wikisource (Wikikilden, no-wikisource): 14,294 texts, ~27M words, shared Bokmål+Nynorsk. Full Norwegian canon (Ibsen, Bjørnson, Hamsun, Undset, Collett, Vinje, Aasen), Asbjørnsen & Moe folktales, 1814 Constitution. Public-domain. Best literature source.
- Wikipedia Bokmål (no-wikipedia): 686,782 articles, 1,533 active editors — the canonical monolingual corpus (internal code 'nb').
- Wikipedia Nynorsk (no-wikipedia-nynorsk): 178,139 articles, 145 active editors — the main large-scale Nynorsk prose corpus; kept as a separate entry because Nynorsk is a distinct official written standard.
- Commons Norwegian pronunciation (no-commons-audio): 801 files + 7 subcats, mixed CC licences, A1-A2 pronunciation.
- Tatoeba (no-tatoeba): Bokmål 18,119 sentences (0 audio), Nynorsk 12,493 sentences; bulk CC-BY export.

MARGINAL entries (included with caveats):
- Wikibooks (no-wikibooks): tiny (968 pages, 4 active editors) but has 'Lærebok i norsk' and a few language courses; no real Norwegian-as-foreign-language shelf.
- LibriVox (no-librivox): only ONE confirmed Norwegian-language recording ('Den siste viking', Johan Bojer). Included because recordings exist, but effectively negligible.

ABSENT / OMITTED (verified non-existent, not invented):
- Spoken Wikipedia for Norwegian: OMITTED. The Commons category 'Spoken Wikipedia - Norwegian' exists but is EMPTY (0 files, 0 subcats), and no 'Talte artikler' WikiProject/category exists on no.wikipedia (the guessed category 'Kategori:Talte artikler' is missing, and prefix searches for 'Talt'/'Innlest' return no categories). No usable spoken-Wikipedia corpus for Norwegian.
- Learner/kids encyclopedia (children-youth): OMITTED. No Norwegian Vikidia edition exists (Vikidia editions: fr, it, es, eu, hy, ca, de, ru, scn, el, en — no no/nb/nn), and there is no Klexikon/Wikikids/Simple-Wikipedia equivalent in Norwegian. This is a genuine A2-B1 gap for Norwegian.

Register / dialect caveats: Norwegian has two official WRITTEN standards — Bokmål (majority, no.wikipedia) and Nynorsk (nn.wikipedia); there is no single official spoken standard. Wikisource (Wikikilden) mixes both standards and is dominated by pre-1938 / Riksmål-era orthography, so its spelling differs from modern Bokmål. Tatoeba cleanly separates nob (Bokmål) and nno (Nynorsk). Commons pronunciation audio is mostly Eastern/Oslo-area Norwegian. The single LibriVox work uses early-20th-century Riksmål-era Bokmål.

**Category gaps:** literature-graded


## pl — Polish  (18 entries)

VERIFICATION CAVEAT FIRST: this adversarial pass ran with NO WebSearch access - the session's web-search budget was already fully exhausted (200/200) before review began - so every currency check used WebFetch alone. That successfully confirmed live-in-2026 status for Polskie Radio's external and domestic services (both showing 22.07.2026 content), Radio 357, Radio Nowy Swiat, Wolne Lektury, NKJP, Biblioteka Polskiej Piosenki, and FINA (which lists Ninateka as a current service). Four sources (Polona, TVP ABC, Ninateka homepage, Spiewnik Niepodleglosci) could not be text-fetched - the first three are JS single-page apps returning only a shell, and Spiewnik returns an HTTP 403 bot-block - but all four domains resolve, so they are kept 'live' with the limitation disclosed in-entry, not marked dead.

EDITORIAL INDEPENDENCE is the defining quirk of the Polish landscape. The public broadcasters TVP, Polskie Radio and PAP were turned into ruling-party instruments under PiS (2015-2023); after the October 2023 election the Tusk coalition began depoliticising them via a legally contested company-law 'liquidation' rather than clean legislation, and as of mid-2026 reform is still incomplete, the outlets remain in liquidation, and independent monitors flag a swing to pro-coalition bias. There is therefore currently NO fully guaranteed non-partisan PUBLIC broadcaster in Poland. My correction distinguishes two cases: the state-funded EXTERNAL service (Polskie Radio dla Zagranicy) is reclassified 'state-controlled' per the registry rule for international broadcasters; the DOMESTIC public broadcasters (PR podcasts, TVP ABC, TVP Teatr Telewizji) are kept 'public-service' (they are structurally EU public-service media undergoing reform, not RT/CGTN-style propaganda) but carry mandatory editorial-independence caveat flags and are catalogued for apolitical culture/literature/children content only. The cleanest genuinely independent audio remains the two listener-funded internet stations, Radio 357 and Radio Nowy Swiat, both founded 2020-2021 by journalists who quit public Trojka.

GENUINE GAPS (honest, not padded): (1) news-simplified - Poland has NO public-broadcaster easy-news product equivalent to NHK News Web Easy or RFI Francais facile; simplified-Polish news comes only from non-institutional/semi-commercial creators (Easy Polish News app, the Easy Polish YouTube series), which fall under the individual-creator/commercial exclusion. (2) literature-graded - CEFR graded readers for Polish are almost entirely commercial (excluded); Wolne Lektury's grade-tagged 'lektury szkolne' is the closest free institutional substitute and is captured in that entry. (3) print-press - all quality current periodicals are hard-paywalled and free portals are tabloid/commercial; historical press is freely available on Polona but is not current-affairs print.

DIALECT/VARIANT: Polish media are overwhelmingly standardised pl-PL; Silesian and Kashubian are separate minority tongues, not Polish variants, and are out of scope. TRANSCRIPT/SUBTITLE reality: Polish public broadcasters publish far fewer transcripts/subtitles than NHK or RFI, so text+audio alignment is scarce - the strongest are Wolne Lektury (audiobook + matching etext), the NKJP spoken subcorpus (transcribed conversation), and Spiewnik Niepodleglosci (lyrics + translations). The registry is well-built: 12 substantive institutional/independent sources, three real fixes applied (external-service reclassification, Wolne Lektury publisher rename, Biblioteka Polskiej Piosenki merger), no removals, no duplicates.

**State-controlled / not recommended:**
- Polskie Radio dla Zagranicy (external/international service) — Reclassified to editorial_independence 'state-controlled': Poland's state-funded external broadcasting arm (ex-Radio Polonia/Radio Poland) that projects to the diaspora and abroad. Treated like other state international services. Catalogued for clear-standard-Polish B1+ listening with topic tagging, NOT as a neutral authority.

**Flags:**
- `other` — Polskie Radio (domestic podcasts / Teatr Polskiego Radia): editorial-independence caveat. Kept 'public-service' (domestic EU public broadcaster) but independence is currently not guaranteed: heavily politicised under PiS 2015-2023, then placed in a legally contested government-imposed 'liquidation' from 2024, with monitors (Demagog, IPI/MFRR) flagging a swing to pro-coalition bias as of mid-2026. Catalogued for apolitical culture/literature/radio-drama content only.
- `other` — TVP (ABC + VOD/Teatr Telewizji): editorial-independence caveat. Same 2015-2026 politicisation-and-liquidation situation as Polskie Radio. The children's (TVP ABC) and Teatr Telewizji content catalogued here is apolitical cultural programming; TVP's news/current-affairs output was deliberately excluded and is not a neutral source.
- `registration-gated` — TVP VOD (Teatr Telewizji + TVP ABC on-demand): On-demand streaming on vod.tvp.pl requires a free account; live broadcast and any YouTube clips are open. access set to 'free-registration' on the Teatr Telewizji entry.
- `registration-gated` — Radio Nowy Swiat (full podcast archive): Live stream is free and open (64/128/256 kbps); the complete on-demand podcast archive is a Patronite patron (paid/registered) benefit - confirmed 'Dostep tylko dla zalogowanych uzytkownikow' gating on some items.
- `registration-gated` — Radio 357 (premium patron features): Core live stream and most podcasts are free and ad-free (sustained by ~50,000 voluntary patrons); a minority of premium features/content may require patron support via wspieram.radio357.pl. access kept 'free'.
- `sensitivity` — Spiewnik Niepodleglosci: historical-context: WWI and independence-era patriotic/martial songs carrying strong period national sentiment; linguistically valuable and fully documented (lyrics + English translations + sheet music) but not default course material. Note: homepage returns HTTP 403 bot-block, verified reachable-but-shielded rather than dead.
- `sensitivity` — Wolne Lektury: historical-context: 19th/early-20th-century public-domain literature contains period-typical prejudice and archaic orthography; fine for B2+ literary study with framing. (Publisher corrected to Fundacja Wolne Lektury.)
- `sensitivity` — Polona: historical-context: digitised historical books/press use archaic orthography and period language; advanced/text-mining use. National Library public-service source; text-only (transcript n/a).
- `other` — Biblioteka Polskiej Piosenki: Partial-paid layer: song catalogue and lyric texts are free, but some archival lending/reproduction functions (System Wypozyczen Online) are paid - use the open lyrics/catalogue layer only. Institution merged with Centrum Kultury Podgorza as of 1 Jan 2026.
- `paywalled` — Major Polish current print press: Landscape context (no entry): Gazeta Wyborcza, Rzeczpospolita, Polityka and Tygodnik Powszechny sit behind hard paywalls; free portals (Onet, WP, Interia) are commercial/tabloid. No free, institutionally-backed current print-press source was found - print-press category left uncovered rather than padded.

**Registration-gated (free account; verify manually):**
- TVP VOD - Teatr Telewizji — https://vod.tvp.pl/teatr-telewizji,29
- TVP ABC (on-demand VOD) — https://vod.tvp.pl/dla-dzieci,24

**Wikimedia:** All seven entries are individually verified live on 2026-07-22 (WebSearch budget was exhausted, so verification used WebFetch against deterministic Wikimedia/Archive endpoints). STRONG editions: pl.wikipedia (1,702,281 articles, 9,045 active users — top-10 edition, the core monolingual corpus) and pl.wikisource/Wikiźródła (deep public-domain literary canon; note the ~1.31M 'content pages' figure is inflated by the Page: proofreading namespace, real work count is much lower). SOLID: Commons Polish pronunciation (24k+ files, Lingua Libre pronunciation-pol subcat alone 97,537 files) and Tatoeba (137,095 pol sentences). PRESENT BUT LIMITED: LibriVox Polish exists (30 PD audiobooks incl. Prus, Schulz, Potocki — the language field is 'pol', not 'Polish'); Spoken Polish Wikipedia exists but is small/dormant (37 recordings on Commons; the pl.wp project page 404'd, Commons category is the live home); pl.wikibooks has a real language-course shelf (Kategoria:Języki, ~46 books) but it targets Polish speakers learning other languages and is lightly maintained, so Polish-as-L2 graded value is modest.

ABSENT — no children-youth/learner encyclopedia entry could be created: there is NO Simple Polish Wikipedia (the 'Simple' project exists only for English), NO Polish Vikidia edition (Vikidia runs fr/es/it/eu/en/ru/ca/de/el/hy/oc/pt/scn — not pl), and no Polish Klexikon/Wikikids equivalent. The nearest learner-friendly Polish reading is therefore Wolne Lektury's school-level texts rather than any Wikimedia kids' encyclopedia.

NON-WIKIMEDIA ADJACENT worth flagging (not catalogued here): Wolne Lektury (wolnelektury.pl) is the major non-Wikimedia public-domain Polish library — school-canon literature with many free audiobook readings and clean EPUB/PDF/text, and it is the natural transcript partner for the LibriVox recordings above.

DIALECT/REGISTER caveat: Polish is essentially monocentric — no Bokmål/Nynorsk-style split — so all entries are standard literary/general Polish (variant=standard). The main learner caveat is register and orthography: Wikisource/LibriVox draw on 19th–early-20th-century texts with some pre-reform spelling and period social attitudes (hence historical-context sensitivity and B2–C2), whereas Commons pronunciation and Tatoeba supply the A1–B1 end. Licences: Wikisource texts and LibriVox are public-domain (wiki/editorial layer CC BY-SA); Wikipedia, Spoken Wikipedia, Commons audio and Wikibooks are CC BY-SA; Tatoeba is CC BY 2.0 FR (audio occasionally other CC terms — check per file)."

**Category gaps:** news-simplified, literature-graded, print-press


## uk — Ukrainian  (19 entries)

After adversarial re-verification, the draft holds up well: all 13 entries are genuinely live in July 2026, correctly categorised, and free of commercial-platform, propaganda, or duplicate violations — so the corrected list keeps all 13 with only a single CEFR consistency fix (adding A2 to the radio entry) plus documented verification notes. IMPORTANT CAVEAT ON METHOD: the WebSearch budget was fully exhausted before this review began, so verification relied entirely on direct WebFetch fetches. That worked for 11 of 13 URLs; two Suspilne URLs (suspilne.media and its /podcasts/ path) are Cloudflare-bot-blocked (HTTP 403) and Ukrinform's .ua homepage bot-blocks fetches (404), so those three are confirmed live only indirectly (English domain for Ukrinform; same-owner ukr.radio for Suspilne) rather than by a direct 200 response — a residual, low-risk uncertainty. Ukraine's media core is genuinely pluralistic: the post-2017 public broadcaster Suspilne/UA:PBC (NSTU) is the backbone across news (suspilne.media), radio (ukr.radio — eight channels incl. Radio Kultura, Radio Promin, and the A1-A2 'Kazka' fairy-tale channel) and podcasts; Hromadske and Ukrainska Pravda are established editorially-independent outlets; Ukrinform is state-owned and flagged; RFE-RL/Radio Svoboda is US-funded and war-focused, so it is noted but deliberately not catalogued. Variant is uniformly standard literary Ukrainian (uk-UA); the main learner caveat is pre-reform orthography in older Wikisource texts. Post-2022 the entire news landscape is war-saturated, so every news entry carries sensitivity news-general with topic_tags to steer toward culture/economy/society. THREE GENUINE CATEGORY GAPS remain and are NOT padded: (1) news-simplified — Ukrainian has no institutional NHK-News-Web-Easy equivalent; the popular 'Easy Ukrainian' is an individual-creator YouTube channel, excluded per the individual-creator/commercial rule; (2) literature-graded — no free, institution-backed CEFR-graded readers exist (only commercial books/paid apps); (3) video-drama — no stable, free, legal streaming of Ukrainian TV/film drama (rights-restricted; Suspilne series and the Dovzhenko Centre archive are not reliably free-to-stream). The transcript-corpus slot is filled by two research tools (GRAC written, OPUS spoken/subtitle) rather than consumer media — acceptable but worth noting as a reference-tool rather than listening/reading-media fill. Finally, the researcher's claim that Chtyvo (chtyvo.org.ua) shut down in 2026 could NOT be independently confirmed here (search budget exhausted) and should be re-checked before it is relied upon.

**State-controlled / not recommended:**
- Ukrinform (Укрінформ) — Ukraine's state-owned National News Agency (founded 1918). Clean, accessible agency Ukrainian in eight languages, but editorially state-aligned — catalogued for language quality, NOT recommended as neutral/default course material; pair with independent outlets. Confirmed live 22 July 2026.
- Radio Svoboda / RFE-RL Ukrainian service (radiosvoboda.org) — US-government-funded international broadcaster; high-quality live Ukrainian but heavy war/politics focus. NOT catalogued as an entry (deliberately excluded); recorded here for completeness so its state-funded status is on record if it is ever added.

**Flags:**
- `sensitivity` — Suspilne Novyny: news-general. Mainstream public-broadcaster news; since 2022 nearly all Ukrainian news is war-dominated — use topic_tags to steer toward culture/economy/society and avoid front-line coverage as a source focus.
- `sensitivity` — Hromadske: news-general. Independent public-interest news; war-saturated like the rest of the news pool — filter by topic.
- `sensitivity` — Ukrainska Pravda: news-general. Independent flagship newspaper; dense B2-C1 register, war-dominated feed — filter by vertical/topic.
- `sensitivity` — Ukrinform: news-general. Agency news feed, war-dominated — pair with the sensitivity + state-controlled notes above.
- `sensitivity` — Ukrainske Radio / Suspilne Radio: news-general. Mixed radio hub whose main channel is news/talk; also carries culture, music and a children's fairy-tale channel — steer learners to Radio Kultura / Kazka for lower-conflict listening.
- `sensitivity` — pisni.org.ua: historical-context. Community lyrics archive (~54,900 songs) that mixes neutral folk/children's songs with patriotic/insurgent (UPA) military songs carrying historical-political weight; pick folk/children's subsets deliberately. Per-song licensing unclear — link-only.
- `sensitivity` — Ukrainian Wikisource: historical-context. Public-domain classics often use pre-reform orthography and period-typical viewpoints; treat as advanced (B2+) and choose editions carefully.
- `paywalled` — Ukrainska Pravda — Клуб УП (UP Club): Optional paid membership tier that does NOT gate core news; access recorded as free. Flagged for completeness only.
- `other` — Ukraїner: All-rights-reserved: reuse requires written consent. Streaming/linking and its Ukrainian subtitles are fine, but no copying/redistribution — catalogue-and-link only.
- `other` — GRAC & OPUS (transcript-corpus): Research corpora, not consumer media: require a search/download interface and underlying texts are copyright-mixed. The OPUS OpenSubtitles subset may contain profanity/adult film subtitles — filter before learner use.

**Wikimedia:** Verification date 2026-07-22. WebSearch budget was fully exhausted at session start (200/200), so every claim below was verified directly via WebFetch against deterministic Wikimedia/Archive URLs and via DNS checks — not via search snippets.

WHICH EDITIONS EXIST / ARE STRONG:
- uk.wikisource.org — STRONG and mature: 390,203 content pages, ~138,263 works, 1,975 authors (Franko, Shevchenko, Lesya Ukrainka, Stefanyk, Skovoroda, Hlibov). Public-domain, redistributable. Best C-level literary reading + PD source texts.
- uk.wikipedia.org — VERY STRONG: 1,428,712 articles, 48.3M edits; the canonical monolingual Ukrainian corpus (CC-BY-SA 4.0, encyclopedic/formal register, B2-C2).
- Wikimedia Commons 'Ukrainian pronunciation' — STRONG for A1-A2 audio: ~16,215 direct files + Lingua Libre subcat (~27,373 word clips); mixed CC.
- Tatoeba (ukr) — SOLID A1-B1 example-sentence corpus: 188,673 sentences (16th overall); but audio is thin (~385 clips).
- uk.wikibooks.org — EXISTS with a real 'Мови' (Languages) textbook shelf, so it qualifies, but it is SMALL/low-activity (1,157 pages, ~10 active editors, main page last edited 2022).
- Ukrainian Spoken Wikipedia (Аудіостатті) — EXISTS as a live category but is SMALL (~16 spoken articles); added as a separate audio+text/podcast entry per instructions.
- LibriVox Ukrainian — EXISTS but MINIMAL: exactly 4 language:ukr works, each confirmed via Internet Archive item metadata. Included as public-domain audio.

WHICH ARE ABSENT (omitted, not invented):
- Learner-friendly children/youth encyclopedia (Vikidia/Klexikon/Wikikids/Txikipedia): NONE for Ukrainian. Decisive evidence: uk.vikidia.org fails DNS (getaddrinfo ENOTFOUND / getent NO-DNS) while fr/es/it/ru/en/de.vikidia.org all resolve. A WebFetch summary of the French Wikipedia Vikidia article erroneously listed 'uk' among editions, but the DNS check refutes a live Ukrainian edition. Klexikon is German-only, Wikikids Dutch-only, Txikipedia Basque-only. So there is currently NO A2-B1 kids-encyclopedia gold source for Ukrainian.

REGISTER / DIALECT CAVEATS:
- Ukrainian here is standard literary Ukrainian throughout; Wikisource/Wikipedia sit at B2-C2 (formal/encyclopedic) — not beginner-friendly on their own. The A1-B1 material is Commons pronunciation audio and Tatoeba sentences.
- Commons includes some dialectal 'vowel charts of Ukrainian dialects' — minor dialect variation, not a separate edition.
- LibriVox/Wikisource carry 19th-century literary language and folk-tale content (marked sensitivity=historical-context) — expect archaic vocabulary/period attitudes.
- Verification quirk to remember: the Internet Archive stores LibriVox language as ISO-639-3 'ukr', so language:Ukrainian returns 0 while language:ukr returns the 4 real items.

**Category gaps:** news-simplified, video-drama, literature-graded


## it — Italian  (21 entries)

Italian is a rich, well-resourced landscape dominated by the public broadcaster RAI, which supplies 7 of the 15 entries and is the single best source across news, cultural radio, video/documentary, kids' content, audiobooks and a CEFR-tagged L2 course. RAI is a bona-fide public-service (licence-fee) broadcaster - catalogue it freely as 'public-service', not 'state-controlled' - with the usual caveat about political influence on governance ('lottizzazione'), which topic-level tagging handles. Target variant is standard it-IT; broadcast and press Italian is consistently standard, while drama/soap ('Un posto al sole', 'Mare Fuori') and the OPUS subtitle corpus expose learners to regional accents and colloquial registers - a feature to level-gate, not a defect. GENUINE GAPS/CAVEATS: (1) news-simplified is the one truly missing category - Italian has no free public equivalent to NHK News Web Easy or RFI's Journal en francais facile; the only strong simplified-news product, News in Slow Italian, is a banned commercial platform, so the public stopgap is RAI's graded 'In Italia' course (catalogued under literature-graded). I did not fabricate a filler entry to close this gap. (2) Music with usable lyrics is thin: Zecchino d'Oro (children's songs, superb A1-A2) is the standout, but the official site ships sheet music + backing tracks rather than clean lyric transcripts, and general pop lyrics are copyright-locked; the RAI/MIC 'canzoneitaliana.it' archive is worth a future look. (3) Quality print-press is largely paywalled (Corriere, Repubblica, Il Sole 24 Ore, Internazionale), so free print-reading load falls on Il Post (excellent explanatory prose) and the ANSA wire. Conversely, public-domain literature is exceptionally strong (Liber Liber, Wikisource, and RAI 'Ad alta voce' for aligned text+audio), and corpora are strong and learner-oriented (PAISA, OPUS) though they are teacher/research tools, not direct learner content. VERIFICATION CAVEAT (stated plainly): the shared web-search budget was exhausted (200/200) BEFORE this review, so zero new searches were possible; verification relied on WebFetch and the repository's own same-day curated registry. WebFetch positively confirmed ilpost.it/podcasts, ansa.it, opus.nlpl.eu, zecchinodoro.org and corpusitaliano.it as live in July 2026; liberliber.it returns 403 to bots (server live). Every rai.it and raiplaysound.it host is host-blocked to WebFetch - their canonical sub-page slugs (raiplaysound.it/radio3, /programmi/adaltavoce, raiplay.it/dirette/raiyoyo, rainews.it, raicultura.it, raiscuola.rai.it/italianoperstranieri) are retained on established knowledge plus the project's same-day 'fetched/high-confidence' verification and should be spot-checked at publish time. Overall a robust pool with only news-simplified genuinely absent.

**Flags:**
- `editorial-independence` — RAI (all RAI entries): RAI - Radiotelevisione Italiana is Italy's domestic public-service broadcaster funded by the licence fee (canone), classified 'public-service' NOT 'state-controlled'. Note the standing Italian debate over political influence on RAI governance ('lottizzazione'); this affects perceived balance, not language quality, and is handled by topic-level tagging. Confirmed against the project's own registry framing.
- `registration-gated` — RaiPlay / RaiPlay Fiction e Serie: On-demand video (RaiPlay) requires a free RAI account (email registration); live streams and many pages are open without login.
- `registration-gated` — Rai Yoyo (RaiPlay): Live diretta is open; the on-demand cartoon catalogue requires a free RaiPlay account. access set to 'free-registration'.
- `paywalled` — Il Post - Morning and premium podcasts: Il Post runs a paid membership; 'Morning' and several podcasts/newsletters are primarily subscriber perks, though full episodes are widely available free on public podcast apps. Core website articles remain free. No transcripts.
- `registration-gated` — Rai Radio 3, Ad alta voce (RaiPlay Sound): Live streams and most RaiPlay Sound pages are open; some on-demand audio may prompt a free RAI login. access recorded as 'free'.
- `sensitivity` — RaiNews24, ANSA, Il Post (site & podcasts), Rai Cultura: Mainstream news / current-affairs output -> sensitivity 'news-general'. Standard, neutral broadcast and wire Italian; no propaganda/advocacy framing.
- `sensitivity` — Liber Liber, Wikisource (it), Ad alta voce: Public-domain / historical literature -> sensitivity 'historical-context'. Older works carry period-typical language and social attitudes (period prejudice); curate texts by topic for learners.
- `sensitivity` — OPUS - OpenSubtitles (Italian): Authentic but uncurated film/TV subtitle corpus - may contain profanity, violence references and adult themes; intended as a teacher/research tool, not direct learner material. Subtitle copyright status is unsettled (licence recorded 'unknown'); sensitivity kept 'none' as no clean adult-content sensitivity value exists, but the caveat is flagged here.
- `excluded-commercial` — News in Slow Italian: Deliberately excluded despite being the obvious 'simplified news' candidate: it is a commercial language-learning subscription product (interactive transcripts behind a paywall) and falls under the commercial-platform ban.

**Registration-gated (free account; verify manually):**
- RaiPlay (video on-demand, incl. Fiction/Serie and Rai Yoyo catalogue) — https://www.raiplay.it/
- RaiPlay Sound (some on-demand audio) — https://www.raiplaysound.it/

**Wikimedia:** SUMMARY (verified 2026-07-22; all figures pulled live from Wikimedia Special:Statistics, the MediaWiki API, the LibriVox API and the Internet Archive). Web-search budget for the session was exhausted, so verification was done by direct fetch/curl of deterministic Wikimedia/Tatoeba/LibriVox endpoints.

STRONG editions for Italian: (1) it.wikisource is very large - 221,975 content texts, deep classical canon from Dante through Pirandello, ~46% fully proofread; (2) it.wikipedia is huge - 1,978,634 articles / ~1.1B words / 25,530 active users - the canonical monolingual Italian corpus; (3) Commons Italian pronunciation is rich - >13,000 word audios once Lingua Libre-ita (11,978) and Shtooka (569) subcategories are counted; (4) Tatoeba has 978,455 Italian sentences (1,591 with audio).

PRESENT BUT SMALLER: (5) Vikidia IT (it.vikidia.org) genuinely exists and is live - 9,836 articles in simple Italian (A2-B1), the Italian analogue to Klexikon/Simple Wikipedia - but low editor activity (~5 active); note there is NO 'Simple Italian Wikipedia' (the Simple-Wikipedia project is English-only), so Vikidia is the correct learner-friendly variant. (6) Wikibooks IT hosts real graded courses - 'Italiano L2' (grammar-chaptered), 'Italiano per migranti A1/A2', 'Italiano' - qualifying it as literature-graded. (7) LibriVox Italian is confirmed (Divina Commedia id 529 + ~87 IA-indexed Italian works).

OMITTED - Spoken Wikipedia: the Italian 'Progetto:Wikipedia parlata' page exists (pageid 199548, last touched Feb 2026) and even names non-native speakers as a target audience, BUT it is dormant ('poco frequentato' per community discussions) and no populated category of spoken Italian articles could be found on it.wikipedia or Commons (Category:Spoken_Wikipedia_articles_in_Italian and several plausible it.wiki category names all returned 0 members). Per the 'must be active / do not invent' rule it is excluded rather than catalogued as a near-empty collection.

REGISTER / DIALECT CAVEATS: Wikisource and LibriVox carry historical, archaic and literary Italian (Dante's medieval Tuscan; 19th-c. Manzoni/Verga) - flagged historical-context; prefer short annotated passages for learners. Wikipedia is modern standard NPOV. Italy's dialect landscape matters: separate Wikimedia editions exist for Sicilian (scn), Neapolitan (nap), Venetian (vec), Lombard (lmo), Piedmontese (pms) and others, and Wikibooks even carries minority-language material (e.g. 'Lombardo per ragazzi') - none of these are standard Italian and all were deliberately excluded from the 'it' entries above, which are standard Italian only. All CEFR values are curator estimates (cefr_source=curator-estimate). editorial_independence=community throughout (Wikimedia/volunteer-run). status=live for all seven (Wikimedia/Tatoeba/LibriVox domains reliably up and all confirmed responding).

**Category gaps:** news-simplified


## el — Greek  (17 entries)

Greek public media is dominated by ERT, which supplies the strongest spread here (ERTFLIX drama/film, archive documentary, ERT εcho radio, archive children's programming) — all free, but ERT publishes subtitles/transcripts only on selected titles, and that transcript/subtitle scarcity is the single biggest pedagogical bottleneck across the whole Greek landscape. Two categories genuinely lack a suitable non-commercial source: (1) news-simplified — Greece has NO public-broadcaster equivalent of NHK News Web Easy or RFI Français Facile; the only 'easy Greek news' offerings are individual creators or commercial language-learning sites, all excluded, so this is a real gap. (2) literature-graded — CEFR-graded readers exist almost exclusively from commercial ELT publishers (excluded per the commercial ban); the closest non-commercial substitutes are the Centre for the Greek Language portal (catalogued) and its Ελληνομάθεια exam materials, which are reference/anthology resources, not graded readers. Editorial-independence caveat: press-freedom monitors have repeatedly flagged government influence over Greek public media — ERT and especially the state-supervised AMNA (now correctly marked state-controlled) — and the mainstream commercial press is strongly politically aligned; Kathimerini (centrist-conservative) is the most institutionally solid quality daily and is included with topic-level tagging, with no partisan 'balancing' title added. Dialect/variant: Standard Modern Greek (Demotic, el-GR) is highly uniform with no major regional TV/radio dialects, so nearly everything here is directly usable; the main register split is diachronic — pre-1976 Katharevousa surfaces in the ERT Archive and older Wikisource literature (both flagged historical-context). Cypriot Greek is a distinct variety and was out of scope. For the thin categories the practical answers are community/academic rather than broadcaster-published: stixoi.info for music-with-lyrics and OPUS OpenSubtitles for spoken/colloquial transcript data, both catalogued with their crowd-sourcing caveats. VERIFICATION HONESTY: the WebSearch budget was exhausted before this review began, so currency was established by direct page fetch (9/12 confirmed live in July 2026) rather than by search cross-check; ERTFLIX, Kathimerini and stixoi.info returned Cloudflare 403 bot-blocks (server up, not dead) and are retained as live but were NOT independently corroborated — a re-run with search budget should re-confirm those three and re-validate the deep ERT children's-programmes URL periodically, as deep archive paths are the most fragile links in the set.

**State-controlled / not recommended:**
- ΑΠΕ-ΜΠΕ / Athens-Macedonian News Agency (AMNA) — Wholly state-owned national news agency supervised by the Government Presidency; not editorially independent. editorial_independence corrected from 'public-service' to 'state-controlled'. Use for neutral factual/cultural wire copy (B1-B2), not for domestic-political framing. Also carries sensitivity news-general.

**Flags:**
- `sensitivity` — ERT Archive (ΕΡΤ Αρχείο): historical-context — dictatorship-era and wartime newsreels plus formal/Katharevousa register; curate selectively for B2+ and cultural context.
- `sensitivity` — Greek Wikisource (Βικιθήκη): historical-context — much modern-Greek material predates the 1976 demotic reform (Katharevousa) and older works carry period-typical attitudes.
- `sensitivity` — ERT εcho: news-general — live public-radio news/talk with routine mainstream framing; also bundles the state-funded diaspora service 'Voice of Greece'.
- `registration-gated` — Kathimerini (Η Καθημερινή): Subscriber tier paywalls some columns/long-reads; the bulk of daily reporting is open, so access kept 'free'. Also sensitivity news-general (centrist-conservative daily) — tag topics to favour economy/culture over campaign coverage.
- `sensitivity` — SBS Greek: news-general — Australian-diaspora public broadcaster; language is standard Modern Greek but the agenda is Australia-centric, and transcripts are published only on some episodes.
- `access` — ERTFLIX: Free but some films/sport are geo-restricted outside Greece, and Greek/English subtitles exist only on selected titles — the subtitled subset is the usable learner pool. (Server returned a Cloudflare 403 bot-block on fetch; treated as live.)
- `other` — stixoi.info: Community-run lyrics database; lyrics remain under copyright, no open licence, user-contributed transcriptions/translations (variable accuracy), no audio hosted. (Cloudflare 403 bot-block on fetch; treated as live.)
- `other` — OPUS – OpenSubtitles Greek: Crowd-sourced subtitle corpus: mixed/unknown per-item licensing (licence field 'unknown'), uneven quality, colloquial register that can include profanity — filter before classroom use.

**Wikimedia:** All entries verified 2026-07-22 via WebFetch of deterministic Wikimedia/Internet-Archive endpoints (Special:Statistics, Commons category pages, archive.org advancedsearch). IMPORTANT: the WebSearch budget was already exhausted (200/200) at session start, so no keyword searches were possible; verification relied entirely on the deterministic canonical URLs, which is sufficient for Wikimedia editions.

STRONG / LARGE, ACTIVE PILLARS: Greek Wikipedia (271,172 articles, ~2,390 active editors) and Greek Wikisource (12,776 texts, ~25.0M words) are the two big, live corpora. Commons 'Greek pronunciation' (244 files + Lingua Libre ~360 audio) and Tatoeba (42,302 ell sentences + audio) are the strongest learner-facing audio/sentence sources.

PRESENT BUT SMALL (included with caveats): Spoken Greek Wikipedia (~11 recordings on Commons, low activity); Greek Wikibooks (~250 content pages, ~6 active editors — has a Γλώσσες shelf, but its courses teach English/Russian THROUGH Greek, so value is indirect graded-Greek prose); LibriVox Greek (34 Modern ell + 45 Ancient grc).

ABSENT / OMITTED (no invention): No Simple Greek Wikipedia — Simple Wikipedia exists only in English. No verified active Greek children's encyclopedia: el.vikidia.org resolves (server returned Cloudflare 403, blocking content verification) but could not be confirmed as an active, populated edition, and with the search budget exhausted I could not corroborate it — so the 'children-youth' learner-encyclopedia slot is OMITTED per the do-not-invent rule. No Greek Klexikon/Wikikids equivalent.

REGISTER / DIALECT CAVEATS: (1) Wikisource spans three registers — Ancient/Koine (Homer, Plato in the original; Septuagint & NT ecclesiastical texts), 19th-c. katharevousa, and modern demotic — flag register mismatch; curate demotic works for modern learners. (2) LibriVox Greek is majority ANCIENT Greek (grc, 45 of 79 items) which is NOT Modern Greek — must filter language:ell (~34 items). (3) Wikipedia, Tatoeba and Commons pronunciation are standard Modern Greek (demotic) and are the safest learner-facing register. (4) Licence note: Commons pronunciation is mixed CC (CC-BY-SA / CC-BY / CC0 per file); Wikisource & LibriVox are public-domain; Wikipedia/Wikibooks/Spoken-Wikipedia are CC-BY-SA; Tatoeba is CC-BY-2.0.

**Category gaps:** news-simplified, literature-graded


## pt — Portuguese  (20 entries)

Portuguese splits into two large standard varieties — European (pt-PT) and Brazilian (pt-BR) — and the list deliberately pairs sources across both: RTP (Notícias, Antena 1, Play docs/cinema, Zig Zag), BND, Museu do Fado and CETEMPúblico for pt-PT; EBC (Agência Brasil, Rádio Nacional, TV Brasil), Praia dos Ossos, C-ORAL-BRASIL and COERLL for pt-BR; LibriVox spans both. PORTUGAL: public broadcaster RTP dominates free, high-quality, stable media across news, radio, documentary, cinema and children's, and enjoys strong statutory editorial independence (kept 'public-service'); the reference private press (Público, Expresso, Observador) is paywalled and excluded. BRAZIL: EBC is the public-media backbone but is state-controlled with weaker independence than RTP — all three EBC entries were re-flagged 'state-controlled' this pass, and the draft's claim that Agência Brasil is CC-BY / 'unusually reusable' was RETRACTED because the live 2026 site shows all-rights-reserved with no Creative Commons notice on the homepage, section pages or article pages; its licence is now 'unknown' and reuse should not be assumed. KEY DATA-QUALITY FIX: the Praia dos Ossos 'full PDF transcripts' claim did not survive verification and was downgraded to audio-only — a caution that the draft over-stated transcript availability elsewhere too. GENUINE GAPS remain honest: (1) news-simplified — there is NO institutional simplified-Portuguese news service comparable to NHK News Web Easy or RFI Français Facile; the only 'simple news' options are AI/commercial and were rightly excluded, so this category is empty. (2) print-press — free, institutionally-backed magazine/periodical press is thin because the quality titles are paywalled commercial; not filled. SUBTITLES/TRANSCRIPTS are a systemic Lusophone weakness: RTP Play and TV Brasil caption only a subset of titles (coverage genuinely 'partial'), and audio sources rarely publish transcripts — after the Praia dos Ossos correction, the only firmly transcript-bearing outliers are C-ORAL-BRASIL (aligned), COERLL (full transcripts + translations) and LibriVox (audio + public-domain source text), so those are disproportionately valuable for A2-B2 listening tasks and should be prioritised. STABILITY: Brazil's Portal Domínio Público has a history of downtime, so LibriVox and the Portuguese BND were chosen as public-domain anchors instead — a sound call. UNLISTED but verified live: RTP Ensina (https://ensina.rtp.pt/), a curriculum-aligned pt-PT educational portal, would be a good B1-B2 children-youth/graded complement to the younger-skewed Zig Zag. Overall the pt list is solid and now internally consistent, with the two headline overclaims (Agência Brasil CC-BY, Praia dos Ossos transcripts) corrected and every URL re-confirmed live at the correct canonical address.

**State-controlled / not recommended:**
- Agência Brasil (EBC) — Brazil's federal public-media agency (Empresa Brasil de Comunicação). Government-appointed leadership and weak statutory independence since the oversight council was abolished in 2016; government communication consolidated under 'Canal Gov' in 2024-25. Not a foreign propaganda outlet like RT/CGTN and output is factual, but editorial_independence set to state-controlled and best steered away from government-affairs framing via topic tags. NOTE: the previously-assumed CC-BY reuse licence is NOT confirmed on the live site (shows 'Todos os direitos reservados pela EBC') — treat as reserved.
- Rádio Nacional (EBC) — EBC federal public radio; same state-controlled governance caveat as Agência Brasil. Catalogued for language value with the flag applied.
- TV Brasil — DOCs Brasil (EBC) — EBC federal public television documentary strand; same state-controlled governance caveat. Content is independent/co-produced documentary, catalogued with the flag.

**Flags:**
- `sensitivity` — Praia dos Ossos (Rádio Novelo): sensitivity=historical-context. True-crime narrative journalism on the 1976 femicide of Ângela Diniz and the 'legítima defesa da honra' trial; discusses violence against women and 1970s social attitudes. Mature content — adults / B2+ only, not young learners. (Also corrected: no verifiable published transcripts.)
- `sensitivity` — Biblioteca Nacional Digital (BND): sensitivity=historical-context. 19th/early-20th-century Portuguese literary classics and periodicals contain period-typical colonial-era and slavery-era language and attitudes; treat as historical-context reading.
- `sensitivity` — LibriVox — audiolivros em português: sensitivity=historical-context. Public-domain Lusophone classics (Machado de Assis, Eça de Queirós, etc.) carry period-typical attitudes; historical register.
- `sensitivity` — Arquivo Sonoro Digital do Museu do Fado: sensitivity=historical-context. Early-20th-century fado recordings — historical audio register and period cultural context; advanced listeners.
- `sensitivity` — Mainstream news (RTP Notícias, Agência Brasil, RTP Antena 1, Rádio Nacional, CETEMPúblico): sensitivity=news-general. Standard current-affairs/newspaper coverage across politics, economy and society; ordinary news-editorial content, flagged for topic-level steering only.
- `other` — COERLL — ClicaBrasil: ClicaBrasil is CC-BY-NC-SA (non-commercial + share-alike), so reuse inside a commercial course needs care; the sibling COERLL materials (Conversa Brasileira, Tá Falado, Communication Exercises, Língua da Gente) are the more permissive CC-BY. Per-item licences re-confirmed on the live site.
- `other` — CETEMPúblico: Free online concordance access (AC/DC) needs no registration, but the full 190M-word corpus is supplied on request. A written research corpus (Público 1991-98), not current or learner-facing media.

**Wikimedia:** All verification done 2026-07-22 via WebFetch against Wikimedia siteinfo APIs, Commons category pages and the Internet Archive (the session's WebSearch budget was exhausted, so no WebSearch was used). 8 verified entries, all live.

STRONG / large holdings: pt.wikipedia (1,178,463 articles, 7,508 active editors - a top-tier edition and the canonical monolingual pt corpus); Tatoeba por (443,019 sentences, ~20,957 with audio); pt.wikisource (38,934 texts); pt.wikibooks (14,117 content pages, with a genuine 'Estante de linguas' shelf incl. a Portugues grammar/course covering pt-BR/pt-PT/pt-AO).

MODEST but real: Spoken Portuguese Wikipedia (~192 Commons recordings, both variants, some accent-tagged); Commons Portuguese pronunciation (BR + PT subcategories, ~148 files in the main audio subcat); LibriVox pt (~107 works, code 'por'); Vikidia PT (3,204 articles - the ONLY learner-friendly encyclopedia for pt, but small and low-activity at ~5 active editors).

ABSENT / caveats: There is NO Simple Portuguese Wikipedia (Simple Wikipedia is English-only) - Vikidia PT is the substitute for the 'children-youth' A2-B1 slot. Tatoeba, LibriVox and Vikidia are Wikimedia-adjacent (not Wikimedia Foundation projects); flagged in each entry. Commons pronunciation provenance is mixed contributors (Lingua Libre NOT confirmed on sampled files) and mixed CC/CC0 licences - check per file.

DIALECT / REGISTER caveats: Portuguese splits into European (pt-PT) and Brazilian (pt-BR); Commons pronunciation and Spoken Wikipedia carry explicit BR/PT subcategories and accent tags, while Wikipedia/Wikisource/Wikibooks/Tatoeba mix both (Wikibooks' Portugues course even adds Angolan pt-AO). Older Wikisource/LibriVox literary texts predate the Acordo Ortografico and often the 1911 reform, so expect archaic spelling; Fernando Pessoa (d.1935) is now public-domain. Wikisource and LibriVox flagged sensitivity=historical-context (colonial-era literature, period prejudice likely); Wikipedia/Spoken Wikipedia set to none (modern NPOV register).

**Category gaps:** news-simplified, print-press


## la — Latin  (16 entries)

After adversarial review, all 10 draft entries survive - each is verified live on 22 Jul 2026 and none is filler, duplicated, commercial-platform, or advocacy/propaganda. The most consequential correction is the Vatican News URL: the old Latin-homepage path (vaticannews.va/la.html) now redirects to a Latin podcast page that lists only the Liturgy of the Hours and no longer surfaces the weekly news bulletin, which has migrated to /en/podcast/vatican-radio-news-in-latin.html (verified current through 18 Jul 2026, full Latin text delivered via the podcast feed). Latin remains a genuinely thin, atypical media landscape and this lean list reflects that honestly. Two living variants matter: reconstructed CLASSICAL Latin (dominant in academic corpora, graded readers and the spoken-Latin video/audio scene) and ECCLESIASTICAL Latin (the only institution still producing current Latin news/audio, via the Vatican); there is no BCP-47 subtag for the distinction, so the variant field carries descriptive values. CEFR levels are ALL estimated - Latin is outside the CEFR and no publisher tags levels - so the arrays are rough guidance only. Editorial independence: the sole current-news outlet (Vatican News) is state-controlled Holy See media, so Latin has NO independent contemporary news broadcaster; the only secular 'news' is a discontinued public-service archive (Yle Nuntii Latini, ended 2019) plus community/individual efforts. The strongest free spoken-Latin and scaffolded-reading material (Latinitium, ScorpioMartianus, Steadman) is produced by individuals/small teams, so quality is high but longevity depends on the creators - and Latinitium overlaps commercially with the paid Legentibus app (its free on-site archive is what is catalogued). A newly surfaced longevity risk: The Latin Library's founder has handed maintenance to an unnamed successor. Two academic corpora are effectively frozen: Perseus 4.0 is 'no longer under active development' (successor: Scaife Viewer) and PHI is a static archive behind a personal-study licence gate. Category gaps are real, not search failures: RADIO-LIVE - no continuous live Latin radio stream (Vatican Latin audio is on-demand only); VIDEO-DRAMA - no free institutional Latin drama (Latin dubs of Harry Potter/Asterix are commercial/print); PRINT-PRESS - the only candidate, Ephemeris, is served over a self-signed 100-year hosting-default certificate with a broken HTTPS response and is run by one individual, so it is unreliable and excluded (Hebdomada Aenigmatum's distribution has also lapsed); CHILDREN-YOUTH - essentially no free public-broadcaster Latin content for children (a real A1-A2 gap; the closest substitutes are the already-listed individual-creator beginner materials from Latinitium and ScorpioMartianus). Additional solid public-domain/academic text archives NOT separately entered to avoid redundancy: Bibliotheca Augustana (hs-augsburg.de), Corpus Corporum (mlat.uzh.ch), and LacusCurtius. VERIFICATION CAVEAT: WebSearch quota was exhausted (200/200) before this run began, so currency and canonical-URL checks were done with WebFetch plus direct curl/openssl (HTTP status, redirect chains, RSS feed pubDates, article counts, TLS certificate inspection); Vatican News, CPDL and the ScorpioMartianus channel return bot-block/consent responses to WebFetch but resolve HTTP 200 and are judged live, while every excluded project failed on hard signals (no DNS, failed/expired TLS, or repurposed content).

**State-controlled / not recommended:**
- Vatican News (Latine): Hebdomada Papae — Official media of the Holy See (Dicastery for Communication), a sovereign state - not an independent broadcaster. editorial_independence=state-controlled. Catalogue for its excellent aligned Ecclesiastical-Latin audio+transcript, but NOT recommended as default course material; pair with secular sources.

**Flags:**
- `sensitivity` — Vatican News (Latine): Hebdomada Papae: Religious/devotional church content (sensitivity=religious). Linguistically the best-attested current formal Latin register, but course use should be topic-tagged, not default.
- `sensitivity` — Choral Public Domain Library (ChoralWiki): Predominantly sacred/liturgical Latin texts (sensitivity=religious). Useful for lyrics/pronunciation but should be selected topic-by-topic.
- `sensitivity` — The Latin Library: Unannotated classical canon; classical works carry period-typical content (war, slavery, invective, some sexual material). sensitivity=historical-context.
- `sensitivity` — Perseus Digital Library (Latin collection): Classical corpus with period-typical themes. sensitivity=historical-context.
- `sensitivity` — PHI Latin Texts: Full canonical Latin corpus to ~AD 200; period-typical classical content. sensitivity=historical-context.
- `sensitivity` — Geoffrey Steadman Latin Readers: Scaffolded classical authors (Caesar, Cicero, Ovid, Vergil); period-typical war/political content. sensitivity=historical-context.
- `sensitivity` — Nuntii Latini (YLE archive): Mainstream world-news bulletin. sensitivity=news-general. Now a static, discontinued (2019) listening archive.
- `licence-restricted` — PHI Latin Texts: Free to use but only via a click-through 'personal study / Fair Use' agreement; all-rights-reserved, no bulk reuse. Not registration-gated (no account), but access carries a usage restriction worth surfacing.
- `registration-gated` — registration-gated items: None. Every entry is access=free with no account/registration wall.

**Wikimedia:** All entries verified live on 2026-07-22 via deterministic APIs (MediaWiki siteinfo/categoryinfo, Tatoeba official exports, LibriVox advanced-search). WebSearch budget was exhausted at session start, so verification was done by direct API/HTTP queries rather than search. Counts are live, not estimated.

STRONG / present:
- Vicifons (la.wikisource): 20,991 texts, ~95.1M words — a deep public-domain library covering the full classical canon plus the Vulgate, medieval and Neo-Latin works. Excellent advanced reading corpus.
- Vicipaedia (la.wikipedia): 141,991 articles — the canonical monolingual Latin corpus and by far the largest single text pool; register is living Neo-Latin (encyclopedic), not classical norm.
- Commons Latin pronunciation: 720 audio files, 10 subcategories covering BOTH Classical (restored) and Ecclesiastic pronunciation, plus Lingua Libre and 'Recitations in Latin'. Mixed CC licensing.
- Tatoeba Latin: 55,771 sentences (1,064 with audio) — large, well-aligned parallel corpus, ideal A1–B1 sentence-mining input. (Non-Wikimedia close adjacent; the Tatoeba web UI and API cap displayed counts at 1,000, so the true figure was taken from the official downloads export.)
- LibriVox Latin: ~103 recordings incl. the Aeneid, Vulgate Bible, De Civitate Dei, Horace, Catullus and dedicated 'Beginning Latin' learner lessons.

WEAK BUT REAL / included:
- Vicilibri (la.wikibooks): 207 pages, low activity, but a genuine 'Grammatica Latina' textbook shelf + multilingual glossaries justify inclusion as literature-graded.

ABSENT (deliberately OMITTED):
- Spoken Wikipedia (Latin): the Commons category 'Spoken Wikipedia - Latin' exists but contains 0 files — there is no active spoken-article project for Latin, so no podcast/audio Wikipedia entry was created.
- Learner/children encyclopedia variant: there is NO Latin equivalent of Simple English Wikipedia, Vikidia, Klexikon or Wikikids. Vicipaedia is the only Latin encyclopedia, so the 'children-youth' category is empty for Latin.
- Latin Wiktionary/Wikiquote etc. were out of the requested scope and not catalogued.

REGISTER / DIALECT CAVEATS:
- Latin splits into CLASSICAL (restored) vs ECCLESIASTICAL pronunciation — Commons and LibriVox both mix the two, so learners should note which system a given clip uses (Commons is explicitly subcategorised by system).
- Vicifons/Vicipaedia text spans classical, medieval and modern Neo-Latin; Vicipaedia in particular uses non-classical neologisms and variable community style — treat as a broad reading/corpus resource, not a style authority.
- Perseus Digital Library (already in registry as la-perseus) and Legentibus (la-legentibus) remain the key non-Wikimedia complements for graded/annotated classical Latin.

**Category gaps:** radio-live, video-drama, print-press, children-youth


## nl — Dutch  (21 entries)

Dutch splits into two national standards, both served by strong, genuinely editorially-independent public broadcasters: nl-NL via NOS/NPO (plus NTR, VPRO) and nl-BE via VRT/Ketnet. There is no state-propaganda or partisan-outlet dilemma for either variant, so the registry can lean almost entirely on public-service media - correctly all flagged 'public-service', none 'state-controlled'. The list deliberately carries both variants across the major categories (two news-standard, two live radio, two children-news, plus Flanders-specific Wablieft and NedBox) so a course can pick an accent; Belgian Dutch differs from Netherlands Dutch in pronunciation and vocabulary. Dutch is unusually rich in simplified-news / NT2 infrastructure (NOS Journaal in Makkelijke Taal, Wablieft, and the KU-Leuven-built NedBox) giving exceptional A1-B1 authentic-news coverage most languages lack. Transcript/subtitle support is a genuine strength - public broadcasters subtitle almost everything (NOS Teletekst 888; VRT subtitles all channels), so catalogued video doubles as caption-supported listening; but verbatim published transcripts beyond subtitles are rare, and the Corpus Gesproken Nederlands (CGN) remains the main source of aligned spoken-Dutch transcripts for both variants. GEO-RESTRICTION is the dominant access caveat for audiovisual Dutch: VRT MAX geo-locks to Belgium, NPO Start to the Netherlands, and VPRO's YouTube is blocked inside NL - plan for VPN/geographic constraints when used abroad. Corrections this pass were light (VRT Radio 1 access free-registration->free; NedBox medium 'interactive' normalised out) - the draft was accurate and well-sourced. REMAINING GAPS (honest, not padded): (1) video-drama - quality Dutch/Flemish drama (VRT 'Thuis', NPO series) exists but sits behind the free-but-geo-locked streamers, with no clean globally-accessible free entry; (2) literature-graded - free graded readers are scarce because the market is dominated by excluded commercial publishers; NedBox (levelled news + an A1 'Alfa' track) and Wablieft partially fill the levelled-reading need; (3) print-press - strong Dutch/Flemish papers (NRC, de Volkskrant, Trouw, De Standaard, De Morgen) are hard-paywalled, so no separate quality print-press entry was added. VERIFICATION HONESTY: WebSearch was unavailable this session (budget exhausted), so currency was checked by direct WebFetch; 11 entries returned live 2026 content, while VRT MAX pages (Karrewiet, Radio 1 on-demand), NedBox (JS app shells) and CGN (HTTP 403 bot-block) could not be deep-verified though their hosts are confirmed correct - these should be re-checked once search budget is available.

**State-controlled / not recommended:**
- All Dutch/Flemish broadcasters (NOS, NPO, NTR, VPRO, VRT/Ketnet) — NONE are state-controlled. All are editorially independent domestic public-service broadcasters and are correctly catalogued editorial_independence 'public-service'. There is no state-propaganda source in the nl set, so no 'state-controlled' reclassification was made.

**Flags:**
- `sensitivity` — NOS, VRT NWS, NOS Journaal in Makkelijke Taal, NPO Radio 1, VRT Radio 1, VPRO Tegenlicht, NOS Jeugdjournaal, Karrewiet, NedBox: sensitivity 'news-general' - mainstream news inevitably covers conflict, crime and elections; topic_tags let a course steer toward neutral domains (economy, science, culture, sport).
- `sensitivity` — DBNL & Nederlandse Liederenbank: sensitivity 'historical-context' - historical literary and song corpora carry period-typical colonial, ethnic, religious or gender content; screen individual works before learner use.
- `registration-gated` — NOS Journaal in Makkelijke Taal: Live broadcast (NPO 1, 17:00) is open; on-demand replay via NPO Start requires a free NPO account and is geo-restricted to the Netherlands. access 'free-registration'.
- `registration-gated` — Karrewiet (VRT MAX): VRT MAX on-demand requires a free VRT account and geo-restricts video to Belgium; the old ketnet.be URL redirects to VRT MAX. access 'free-registration'.
- `registration-gated` — Corpus Gesproken Nederlands (CGN): Free of charge but requires signing an INT research licence agreement before download; a fixed dataset, not a click-through feed. access 'free-registration'. (Download page 403'd the automated fetcher - bot-block, host confirmed correct.)
- `registration-gated` — VRT Radio 1 (on-demand catch-up): The catalogued LIVE stream is open (access corrected to 'free'); only VRT MAX on-demand replay may prompt a free VRT account and is partly geo-limited to Belgium. Caveat noted in pedagogical_notes.
- `paywalled` — Wablieft: Free easy-Dutch articles at wablieft.be/nl/krant, but many pieces are labelled 'premium' and the print edition + full online archive need a paid subscription (trial from EUR 8). Catalogued access 'free' for the open web articles.
- `other` — Een Beetje Nederlands: Individual-creator podcast, not institutionally backed - continuity depends on one producer. Included because it is the only Dutch listening source with free, CEFR-tagged (B1/B2) full transcripts for every episode; verified still releasing in 2026 (ep #86).
- `other` — VPRO Tegenlicht: Free archive at tegenlicht.vpro.nl (verified live, Jul 2026), but NPO Start on-demand needs a free NL-only account and the VPRO/Tegenlicht YouTube channel is geo-blocked inside the Netherlands.

**Registration-gated (free account; verify manually):**
- NOS Journaal in Makkelijke Taal (NPO Start replay) — https://npo.nl/start/serie/nos-journaal-in-makkelijke-taal/afleveringen
- Karrewiet / VRT Radio 1 on-demand (VRT MAX) — https://www.vrt.be/vrtmax/a-z/karrewiet/
- Corpus Gesproken Nederlands (INT research licence) — https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/

**Wikimedia:** All 8 entries were VERIFIED live on 2026-07-22 against deterministic Wikimedia/MediaWiki APIs, Tatoeba per-language stats, and the Internet Archive advancedsearch API (WebSearch budget was exhausted at session start, so verification relied on WebFetch of API/stats endpoints — these returned concrete counts, not guesses).

EDITIONS THAT EXIST AND ARE STRONG:
- Wikipedia (nl): 2,223,566 articles — the canonical monolingual Dutch corpus.
- Commons 'Dutch pronunciation': 872,062 audio files + 11 subcats — a huge Lingua Libre pronunciation bank (A1-A2 gold).
- Tatoeba (nld): 200,517 sentences, 9,038 with audio.
- WikiKids: 53,606 articles — the Dutch learner-friendly encyclopedia (A2-B1 equivalent of Simple English Wikipedia / Vikidia / Klexikon). NOTE: independent community project run by the WikiKids community, NOT a Wikimedia Foundation wiki; licence confirmed CC-BY-SA-3.0 (no NC clause).
- Wikisource (nl): ~21,360 public-domain texts (Multatuli, Vondel, Bilderdijk, Couperus, Statenvertaling).
- Wikibooks (nl): ~10,828 modules WITH a genuine language-course shelf (Nederlands, plus Frans/Duits/Engels/Latijn/Oudgrieks/Spaans/etc. taught in Dutch) — hence included as literature-graded.
- LibriVox (nl): 210 Dutch-language public-domain audiobooks confirmed via Internet Archive.

EXISTS BUT WEAK (included per instructions, flagged as limited):
- Gesproken Wikipedia (Dutch Spoken Wikipedia): the project and category exist, but only ~29 recorded articles ('Lijst van ingesproken artikelen') and it is largely dormant. Added as a separate podcast-category entry (medium audio+text, full transcript) but with a clear small-catalogue caveat.

ABSENT / NOT FOUND: No Dutch-specific 'Simple Dutch Wikipedia' exists (WikiKids fills that A2-B1 niche instead). Several candidate spoken-article category names ('Categorie:Gesproken artikel', 'Gesproken versie', Commons 'Category:Dutch spoken Wikipedia', 'Category:Spoken articles in Dutch', and Commons 'Category:Spoken Wikipedia - Dutch') were checked and are missing or empty; only the small WikiProject category is populated.

REGISTER / DIALECT CAVEATS:
- Wikisource skews to historical orthography (much pre-1947 'De Vries–Te Winkel' / pre-1954 spelling) and period attitudes → sensitivity=historical-context; select shorter annotated excerpts.
- Wikipedia and Wikibooks mix Netherlands (Noord-Nederlands) and Belgian/Flemish (Vlaams) contributors; register is encyclopedic/formal (Wikipedia) vs. expository textbook (Wikibooks).
- Commons pronunciation audio mixes Netherlands and Belgian Dutch speakers — useful for exposing regional variation, but licences are mixed CC (CC0/CC-BY/CC-BY-SA), so verify per file before redistribution.
- LibriVox Dutch is volunteer-read: narrator accent and audio quality vary; source texts are period/colonial works.
- No IDs collide with existing registry entries (existing nl entries are only nl-nedbox, nl-oefenen, nl-taalunie; no Wikimedia-family Dutch entries existed before). Suggested ids follow the requested nl-<project> pattern.

**Category gaps:** video-drama, literature-graded, print-press


## de — German  (19 entries)

German remains a resource-rich language with a well-funded, editorially-independent public-broadcaster ecosystem, so quality authentic free material is abundant. Variant spread is genuinely covered: Germany (ARD/tagesschau, ZDF/logo!, WDR/Maus, Deutschlandfunk, Deutschlandfunk Nova, and DW), Austria (ORF, de-AT simplified news), Switzerland (SRF, incl. Mundart, de-CH). The A1-B1 simplified-news layer is a real strength (DW Langsam gesprochene Nachrichten with full read-along transcripts, Deutschlandfunk nachrichtenleicht, ORF, plus tagesschau in Einfacher Sprache). BIGGEST EDITORIAL FINDING: the draft treated Deutsche Welle as public-service; DW is federally-budget-funded international broadcasting and, per the rubric, is now 'state-controlled' (2 entries) — the domestic license-fee broadcasters (ARD/ZDF/WDR/Deutschlandradio/ORF/SRF/ARTE) correctly stay public-service. FACTUAL ERRORS CAUGHT: (a) Projekt Gutenberg-DE's operator is tredition, not the invented 'Cultural Assets GmbH'; (b) nachrichtenleicht is a WEEKLY Wochenrückblick, not the claimed 'daily Mon-Fri podcast since April 2026'. GAPS remain honest: literature-graded is thin from non-commercial sources (the German graded-reader market is dominated by the excluded ELT publishers Klett/Hueber/Cornelsen/Langenscheidt; DW's Nico's Weg is the only partial fill, and it is now state-controlled), and print-press is thin for FREE access (quality dailies SZ/FAZ/Zeit/Spiegel are hard-paywalled; free 'press' means public-broadcaster online journalism or low-activity German Wikinews). Transcripts of AUTHENTIC audio are the main pedagogical bottleneck: native podcasts/radio (Hörsaal, SRF) rarely publish transcripts, so reliably-transcribed material is the learner-oriented DW/Dlf output. Public-broadcaster video (ARD/ZDF/ARTE/Maus) is subject to Depublizierung, so archive_depth is realistically 'months'. VERIFICATION CAVEAT (important): the WebSearch budget was already fully exhausted (200/200) at the start of this QA session, so NO verification/discovery searches were possible; verification relied on WebFetch, which confirmed 6 domains live (nachrichtenleicht.de, liederprojekt.org, logo.de, projekt-gutenberg.org, srf.ch/radio-srf-1, opus.nlpl.eu) but was host-blocked on tagesschau.de, learngerman.dw.com (both DW entries), arte.tv and deutschlandfunknova.de — those four/five rest on prior knowledge and are flagged per entry, and the ORF teletext URL/page numbers remain unconfirmed. Registration-gated: none in this set (the IDS Mannheim DGD/FOLK and DWDS corpora are stronger academic spoken/parallel resources but need free registration / have restrictive reuse terms — correctly noted rather than listed).

**Flags:**
- `editorial_independence` — Deutsche Welle – Langsam gesprochene Nachrichten: RECLASSIFIED to state-controlled. DW is Germany's federally-budget-funded international broadcaster (Auslandsrundfunk); per the rubric, state-funded international broadcasters carry 'state-controlled' despite the editorial-independence guarantee in the Deutsche-Welle-Gesetz.
- `editorial_independence` — Deutsche Welle – Nico's Weg: RECLASSIFIED to state-controlled for the same reason (DW = state-funded international broadcaster). Also: host-blocked for fetch and course id c-36519789 not individually verified this session.
- `sensitivity` — tagesschau in 100 Sekunden: news-general: mainstream ARD news, inevitably covers conflict/elections/crime; use topic_tags to prefer economy/culture. Host-blocked for direct fetch; canonical video path unverified this session.
- `sensitivity` — Langsam gesprochene Nachrichten (DW): news-general: daily world news; state-controlled (see above).
- `sensitivity` — nachrichtenleicht (Deutschlandfunk): news-general: simplified authentic news (A2-B1); weekly Wochenrückblick, not daily.
- `sensitivity` — ORF Nachrichten leicht verständlich: news-general (de-AT). Verification soft: JS-rendered teletext deep-link could not be confirmed this session.
- `sensitivity` — logo! – Die Kindernachrichten des ZDF: news-general: children's news covering politics/climate/health at A2-B1; confirmed live 21 Jul 2026.
- `sensitivity` — Radio SRF 1 (Livestream): news-general (de-CH): Swiss news plus Mundart dialect; no transcripts. Confirmed live via fetch.
- `sensitivity` — Projekt Gutenberg-DE: historical-context: period-typical prejudice in older public-domain texts. Also: operator corrected to tredition (since Jan 2026); monitor stability post-handover.
- `sensitivity` — Das Liederprojekt (SWR2 & Carus): religious subset: predominantly secular folk/children's songs but includes Christian carols and devotional church hymns (e.g. 'Gelobet seist du, Jesu Christ'). Overall sensitivity kept 'none'; religious register flagged for course selection. Licence mixed (recordings © Carus-Verlag).
- `sensitivity` — OPUS OpenSubtitles (German): Unfiltered movie/TV dialogue may contain profanity, violence references and adult themes; NO formal open licence (licence 'unknown', research use with attribution). Clean and filter before any learner exposure. Not learner-facing media.
- `sensitivity` — ARTE Mediathek – Dokumentationen: Platform mixes light and heavy subject matter (war, atrocity, disaster); select culture/science/nature titles. Limited availability windows (Depublizierung). Editorial_independence public-service (Franco-German license-fee, editorially independent) — NOT state-controlled, unlike DW.

**Wikimedia:** All 8 Wikimedia-family sources verified LIVE and ACTIVE for German on 2026-07-22 via WebFetch against the canonical Wikimedia/Commons/Tatoeba domains (WebSearch budget was exhausted this session, so verification used direct fetches of Spezial:Statistik and category/project pages).

VERIFIED SIZES: de.wikisource 649,550 content pages / ~57k completed works; de.wikipedia 3,137,636 articles (8.59M total pages); Gesprochene Wikipedia ~1,361 spoken articles (active); Klexikon ~3,500 articles; Commons Category:German_pronunciation 14 subcats + 306 direct files, with Lingua Libre pronunciation-deu ~25,825 and Shtooka German 677 in subcategories; Wikibooks DaF Regal ~25+ L1-specific courses; Tatoeba 775,692 sentences / 32,938 audio; LibriVox 3,074 German audiobooks (2nd-largest language).

WHAT EXISTS / IS STRONG: German is exceptionally well served across the whole Wikimedia family. Strongest: de.wikisource (huge PD literary corpus), de.wikipedia (canonical monolingual corpus), and - crucially for this pool - Klexikon as the genuine German A2-B1 learner encyclopedia (direct analog of Simple English Wikipedia / Vikidia; sister MiniKlexikon is A1-A2). A real Gesprochene Wikipedia audio corpus exists and is active, so it was added as a separate podcast-category entry. LibriVox German and Tatoeba German are both large.

WHAT IS ABSENT: nothing material in the requested set is missing for German - all 7 project types requested are present, plus the Spoken Wikipedia bonus, giving 8 entries.

REGISTER / DIALECT CAVEATS: (1) Written sources are Standard High German (Hochdeutsch). (2) Wikisource and much of LibriVox preserve HISTORICAL orthography (pre-1901 spelling, Fraktur) and archaic register, so effective decoding difficulty runs above the nominal CEFR level - flagged sensitivity: historical-context on both. (3) de.wikipedia's encyclopedic/nominal register pushes it to B2-C2 despite accessible topics. (4) Commons pronunciation audio spans multiple regional variants (Austrian, Swiss, and dialect subcategories) - good for accent exposure but not uniformly Standard. (5) Scope note: Low German (Plattdeutsch) has its own separate editions (nds.wikipedia, nds.wikisource) and is intentionally excluded from language code 'de'.

KLEXIKON RECONCILIATION: de.wikipedia's Klexikon article gives ~3,500 articles at klexikon.zum.de; the MediaWiki content-page counter on Spezial:Statistik reports a much lower number (article-count method quirk). Reported the secondary-source figure. klexikon.de resolves to the same project (klexikon.zum.de is the canonical ZUM-hosted wiki).

OVERLAP WITH EXISTING DB (data/sources_master.yml): German entries already exist for wikisource-de, wikibooks-deutsch-als-fremdsprache, klexikon-kinderlexikon, commons-de-aussprache and gutenberg-de - these structured entries are the verified 2026-07-22 refresh of those. NEW for German (no prior German-specific entry): de.wikipedia, Gesprochene Wikipedia, Tatoeba-de and LibriVox-de (the DB previously held only tatoeba-en and librivox-en). Recommend de-tatoeba and de-librivox reuse the existing CC-BY-2.0 FR and public-domain licence framing already curated for their English counterparts.

**Category gaps:** literature-graded, print-press


## Appendix — open items not yet in the acquisition layer

These carry an open licence (public-domain / CC) and a clean Wikimedia/Gutenberg-family domain but are **not yet** in `resources/registry.yml`. They are candidates for the acquisition/caching build (`scripts/refresh-resources.sh`):

- `ar` ar-commons-audio — https://commons.wikimedia.org/wiki/Category:Arabic_pronunciation
- `ar` ar-librivox — https://librivox.org/search
- `ar` ar-tatoeba — https://tatoeba.org/en/sentences/show_all_in/ara/none
- `ar` ar-wikibooks — https://ar.wikibooks.org/
- `ar` ar-wikipedia — https://ar.wikipedia.org/
- `ar` ar-wikipedia-spoken — https://ar.wikipedia.org/wiki/%D8%AA%D8%B5%D9%86%D9%8A%D9%81:%D9%85%D9%82%D8%A7%D9%84%D8%A7%D8%AA_%D9%85%D8%B3%D9%85%D9%88%D8%B9%D8%A9
- `ar` ar-wikisource — https://ar.wikisource.org/
- `de` de-tatoeba — https://tatoeba.org/en/sentences/show_all_in/deu/none
- `de` de-wikipedia-gesprochene — https://de.wikipedia.org/wiki/Wikipedia:Gesprochene_Wikipedia
- `el` el-commons-audio — https://commons.wikimedia.org/wiki/Category:Greek_pronunciation
- `el` el-tatoeba — https://tatoeba.org/en/sentences/show_all_in/ell/none
- `el` el-wikibooks — https://el.wikibooks.org/
- `el` el-wikipedia — https://el.wikipedia.org/
- `el` el-wikisource — https://el.wikisource.org/
- `en` en-librivox — https://librivox.org/search?primary_key=1&search_category=language&search_page=1&search_form=get_results
- `en` en-simple-wikipedia — https://simple.wikipedia.org/wiki/Main_Page
- `en` en-spoken-wikipedia — https://en.wikipedia.org/wiki/Wikipedia:Spoken_articles
- `en` en-wikibooks-languages — https://en.wikibooks.org/wiki/Subject:Languages
- `es` es-commons-audio — https://commons.wikimedia.org/wiki/Category:Spanish_pronunciation
- `es` es-librivox — https://librivox.org/search?primary_key=5&search_category=language&search_page=1&search_form=get_results
- `es` es-tatoeba — https://tatoeba.org/en/sentences/show_all_in/spa/none
- `es` es-vikidia — https://es.vikidia.org/wiki/Vikidia:Portada
- `es` es-wikibooks — https://es.wikibooks.org/wiki/Portada
- `es` es-wikipedia-hablada — https://es.wikipedia.org/wiki/Categoría:Wikipedia:Artículos_grabados
- `es` es-wikisource — https://es.wikisource.org/wiki/Wikisource:Portada
- `fa` fa-commons-audio — https://commons.wikimedia.org/wiki/Category:Persian_pronunciation
- `fa` fa-tatoeba — https://tatoeba.org/en/sentences/show_all_in/pes/none
- `fa` fa-wikibooks — https://fa.wikibooks.org/
- `fa` fa-wikipedia — https://fa.wikipedia.org/
- `fa` fa-wikipedia-spoken — https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D9%86%D9%88%D8%B4%D8%AA%D8%A7%D8%B1%D9%87%D8%A7%DB%8C_%D8%B5%D9%88%D8%AA%DB%8C
- `fa` fa-wikisource — https://fa.wikisource.org/
- `fr` fr-librivox — https://librivox.org/search?primary_key=3&search_category=language&search_page=1&search_form=get_results
- `fr` fr-tatoeba — https://tatoeba.org/en/sentences/show_all_in/fra/none
- `fr` fr-wikibooks — https://fr.wikibooks.org/wiki/Accueil
- `fr` fr-wikipedia — https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal
- `it` it-commons-audio — https://commons.wikimedia.org/wiki/Category:Italian_pronunciation
- `it` it-tatoeba — https://tatoeba.org/en/sentences/show_all_in/ita/none
- `it` it-vikidia — https://it.vikidia.org/wiki/Pagina_principale
- `it` it-wikibooks — https://it.wikibooks.org/wiki/Italiano_L2
- `it` it-wikipedia — https://it.wikipedia.org/wiki/Pagina_principale
- `it` it-wikisource — https://it.wikisource.org/wiki/Pagina_principale
- `ja` ja-commons-audio — https://commons.wikimedia.org/wiki/Category:Japanese_pronunciation
- `ja` ja-tatoeba — https://tatoeba.org/en/sentences/show_all_in/jpn/none
- `ja` ja-wikibooks — https://ja.wikibooks.org/wiki/Category:語学
- `ja` ja-wikipedia — https://ja.wikipedia.org/wiki/メインページ
- `ja` ja-wikisource — https://ja.wikisource.org/wiki/Main_Page
- `la` la-commons-audio — https://commons.wikimedia.org/wiki/Category:Latin_pronunciation
- `la` la-librivox — https://librivox.org/search?primary_key=39&search_category=language&search_page=1&search_form=advanced
- `la` la-tatoeba — https://tatoeba.org/en/sentences/show_all_in/lat/none
- `la` la-vicipaedia — https://la.wikipedia.org/wiki/Pagina_prima
- `la` la-wikibooks — https://la.wikibooks.org/
- `la` la-wikipedia — https://la.wikipedia.org/
- `la` la-wikisource — https://la.wikisource.org/
- `nl` nl-commons-audio — https://commons.wikimedia.org/wiki/Category:Dutch_pronunciation
- `nl` nl-tatoeba — https://tatoeba.org/en/sentences/show_all_in/nld/none
- `nl` nl-wikibooks — https://nl.wikibooks.org/wiki/Hoofdpagina
- `nl` nl-wikipedia — https://nl.wikipedia.org/wiki/Hoofdpagina
- `nl` nl-wikisource — https://nl.wikisource.org/wiki/Hoofdpagina
- `no` no-commons-audio — https://commons.wikimedia.org/wiki/Category:Norwegian_pronunciation
- `no` no-tatoeba — https://tatoeba.org/en/sentences/show_all_in/nob/none
- `no` no-wikibooks — https://no.wikibooks.org/
- `no` no-wikipedia — https://no.wikipedia.org/
- `no` no-wikipedia-nynorsk — https://nn.wikipedia.org/
- `no` no-wikisource — https://no.wikisource.org/
- `pl` pl-tatoeba — https://tatoeba.org/en/sentences/show_all_in/pol/none
- `pl` pl-wikibooks — https://pl.wikibooks.org/wiki/Kategoria:Języki
- `pl` pl-wikipedia — https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna
- `pl` pl-wikipedia-spoken — https://commons.wikimedia.org/wiki/Category:Spoken_Polish_Wikipedia
- `pl` pl-wikisource — https://pl.wikisource.org/wiki/Wikiźródła:Strona_główna
- `pt` pt-commons-audio — https://commons.wikimedia.org/wiki/Category:Portuguese_pronunciation
- `pt` pt-librivox-portugues — https://librivox.org/
- `pt` pt-tatoeba — https://tatoeba.org/en/sentences/show_all_in/por/none
- `pt` pt-vikidia — https://pt.vikidia.org/
- `pt` pt-wikibooks — https://pt.wikibooks.org/
- `pt` pt-wikipedia — https://pt.wikipedia.org/
- `pt` pt-wikisource — https://pt.wikisource.org/
- `ru` ru-commons-audio — https://commons.wikimedia.org/wiki/Category:Russian_pronunciation
- `ru` ru-librivox — https://librivox.org/search?primary_key=27&search_category=language&search_page=1&search_form=get_results
- `ru` ru-librivox-russian — https://librivox.org/keywords/21382
- `ru` ru-tatoeba — https://tatoeba.org/en/sentences/show_all_in/rus/none
- `ru` ru-vikidia — https://ru.vikidia.org/
- `ru` ru-wikibooks — https://ru.wikibooks.org/
- `ru` ru-wikipedia — https://ru.wikipedia.org/
- `ru` ru-wikipedia-spoken — https://ru.wikipedia.org/wiki/Википедия:Список_аудиостатей
- `ru` ru-wikisource — https://ru.wikisource.org/
- `tr` tr-commons-audio — https://commons.wikimedia.org/wiki/Category:Turkish_pronunciation
- `tr` tr-tatoeba — https://tatoeba.org/en/sentences/show_all_in/tur/none
- `tr` tr-vikikaynak-wikisource — https://tr.wikisource.org/
- `tr` tr-wikibooks — https://tr.wikibooks.org/wiki/Kategori:Diller
- `tr` tr-wikipedia — https://tr.wikipedia.org/wiki/Anasayfa
- `tr` tr-wikisource — https://tr.wikisource.org/wiki/Ana_Sayfa
- `uk` uk-commons-audio — https://commons.wikimedia.org/wiki/Category:Ukrainian_pronunciation
- `uk` uk-spoken-wikipedia — https://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%90%D1%83%D0%B4%D1%96%D0%BE%D1%81%D1%82%D0%B0%D1%82%D1%82%D1%96
- `uk` uk-tatoeba — https://tatoeba.org/en/sentences/show_all_in/ukr/none
- `uk` uk-wikibooks — https://uk.wikibooks.org/
- `uk` uk-wikipedia — https://uk.wikipedia.org/
- `uk` uk-wikisource — https://uk.wikisource.org/
- `zh` zh-commons-audio — https://commons.wikimedia.org/wiki/Category:Chinese_pronunciation
- `zh` zh-tatoeba — https://tatoeba.org/en/sentences/show_all_in/cmn/none
- `zh` zh-wikibooks — https://zh.wikibooks.org/
- `zh` zh-wikipedia — https://zh.wikipedia.org/
- `zh` zh-wikipedia-classical — https://zh-classical.wikipedia.org/
- `zh` zh-wikisource — https://zh.wikisource.org/

## Appendix — link-check anomalies (2026-07-22)

URLs the automated checker could not confirm as live from the CI sandbox. `dead` = fix or drop; `000`/geo = likely reachable in-region (verify in a browser).

- `en` `en-britishcouncil-learnenglish` (HTTP 000) — https://learnenglish.britishcouncil.org/
- `fr` `fr-cnrs-clapi` (HTTP 000) — https://clapi.icar.cnrs.fr
- `no` `no-nrk-tv-dokumentar` (HTTP 404) — https://tv.nrk.no/kategori/dokumentar
- `no` `no-nrk-tv-drama-skam` (HTTP 404) — https://tv.nrk.no/serie/skam
- `tr` `tr-yee-ogretim-portali` (HTTP 000) — https://turkce.yee.org.tr/
- `zh` `zh-pts-drama` (HTTP 000) — https://www.pts.org.tw/
