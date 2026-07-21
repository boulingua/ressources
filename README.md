# Ressourcen

Kuratierte Sammlung frei verfuegbarer Online-Ressourcen fuer
Englisch, Franzoesisch und Deutsch als Fremdsprache.

Live: <https://boulingua.github.io/ressources/>

## Lizenzen

- **Code** (Hugo-Konfiguration, Python-Skripte, CSS, CI):
  MIT - siehe [LICENSE](LICENSE).
- **Inhalte** (Beschreibungen, Annotationen, Einleitungstexte,
  `data/sources_master.yml`): CC-BY-SA 4.0 - siehe
  [LICENSE-content](LICENSE-content).
- **Verlinkte externe Ressourcen**: jeweilige Lizenz der
  Anbieter (siehe `license_type` und `license_details` pro
  Ressource).

## Lokal bauen

```bash
pip install pyyaml jsonschema
python _scripts/validate_sources.py
python _scripts/check_commercial.py
python _scripts/build_overview.py
hugo --minify
cp static/index.html public/index.html
```

Hugo (extended) >= 0.147 wird benoetigt; Theme `hugo-coder` wird ueber
Hugo Modules eingebunden (`go.mod`).

## Autorin

Alle kuratorischen Inhalte: S. Le Boulanger.

## Einsatz von LLM-Werkzeugen

Teile dieses Projekts wurden mit Unterstützung von Large-Language-Model-Werkzeugen für eng umrissene, nicht-autorschaftliche Aufgaben erstellt: Lektorat, sprachliche Glättung, Markdown-/LaTeX-Formatierung, Gerüstbau von Boilerplate-Dateien (CI-Konfigurationen, Build-Skripte), Code-Refactoring. Verwendet wurden Chat AI, der LLM-Dienst von KISSKI (GWDG), sowie ein selbst gehostetes Mistral Small (24B, Apache-2.0), lokal betrieben über Ollama und das R-Paket ollamar — ausschließlich lokale Inferenz, ohne Übermittlung von Daten an Dritte beim selbst gehosteten Modell.
