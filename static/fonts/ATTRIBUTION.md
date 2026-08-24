# Fonts shipped by this repository

Seven self-hosted faces, Google Fonts cuts rather than
`kit/design/build_fonts.py` output, because this hub uses weights the kit's
tiers do not carry.

Self-hosting rather than linking `fonts.googleapis.com` is deliberate: a
webfont request to a third party is a data transfer the Datenschutzerklärung
would have to declare, and this site publishes one in three languages.

Not covered by `kit/design/fonts/ATTRIBUTION.md`, which documents the kit's own
subsets. Gate A4 reads both.

| File | Family | Licence | Upstream |
|---|---|---|---|
| `jetbrains-mono-v24-latin_latin-ext-500.woff2` | JetBrains Mono | OFL 1.1 | <https://github.com/JetBrains/JetBrainsMono> |
| `jetbrains-mono-v24-latin_latin-ext-regular.woff2` | JetBrains Mono | OFL 1.1 | <https://github.com/JetBrains/JetBrainsMono> |
| `source-sans-3-v19-latin_latin-ext-300.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-500.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-600.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-700.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-regular.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |

Licence texts: [`kit/design/fonts/LICENSES/`](https://github.com/boulingua/kit/tree/main/design/fonts/LICENSES).
Both families are the same OFL projects the kit documents; only the cut differs.

`latin-ext` is required: this hub publishes in German, English and French, so
ä ö ü ß, é è ê à ç and the œ ligature all appear in body text.
