# Legal pages — Pflege- und Build-Hinweise

Dieses Repository veröffentlicht das mehrsprachige `#ressources`-
Verzeichnis (DE/EN/FR). Rechtsgrundlage ist die deutsche Fassung
unter `de/`:

- `de/imprint.qmd` — Impressum (§ 5 DDG, § 18 Abs. 2 MStV)
- `de/privacy.qmd` — Datenschutzerklärung
- `de/disclaimer.qmd` — Haftungsausschluss

EN/FR-Fassungen unter `en/imprint.qmd`, `en/privacy.qmd`,
`fr/imprint.qmd`, `fr/privacy.qmd` sind Übersetzungs-Stubs zum
Komfort und verweisen ggf. auf die deutsche Fassung als
verbindliche Rechtsfassung.

Im Header oben rechts unter **Rechtliches · Legal · Mentions**;
im Footer mit eigenen Links plus Kontakt-`mailto:`.

## Plausible Analytics

Eingebunden über `_includes/in-header.html` (selbst gehostet
auf `analytics.hellebo.de`, Server Deutschland, cookielos).

## VG Wort

Im Hub-Repo selbst werden in der Regel **keine** zählpflichtigen
Werke veröffentlicht (die Inhalte sind kuratorische Annotationen,
unter 1500 Zeichen). Sollten substantielle Eigenartikel
hinzukommen, kann der Lua-Filter `_scripts/vgwort.lua` aktiviert
und pro Seite via `vgwort_pixel:` in der Frontmatter ein Token
eingetragen werden.

## CI-Guard

`scripts/check-legal-placeholders.sh` prüft das gerenderte
`_site/`-Verzeichnis auf unausgefüllte Platzhalter. Lokal:

```bash
BUILD_DIR=_site bash scripts/check-legal-placeholders.sh
```
