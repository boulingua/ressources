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

Voraussetzungen: Python 3.12, Node 22, Go 1.26.1 und Hugo extended 0.159.2.

```sh
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
npm ci
python _scripts/validate_sources.py
python _scripts/check_commercial.py
python _scripts/build_overview.py --check
python _scripts/validate_network_data.py
hugo --minify --gc --panicOnWarning
hugo server --bind 127.0.0.1
```

Die lokale Adresse wird von Hugo ausgegeben. Die Übersicht unter
`/ressources/de/overview/` bietet Filter, Detailansichten und ein optionales
Netzwerk. Alle Skripte werden lokal ausgeliefert. Der große Netzwerk-Code wird
erst nach einem Klick geladen. Ohne JavaScript bleiben die redaktionellen
Ressourcenlisten auf der Startseite verfügbar.

Nach Änderungen an `data/sources_master.yml` zuerst
`python _scripts/build_overview.py` ausführen und die drei JSON-Dateien gemeinsam
mit der Quelle prüfen und committen. `--check` verändert keine Datei.
`kit check` führt dieselben Katalogprüfungen als A22 aus.

## Autorin

Alle kuratorischen Inhalte: S. Le Boulanger.

## Einsatz von LLM-Werkzeugen

Teile dieses Projekts wurden mit Unterstützung von Large-Language-Model-Werkzeugen für eng umrissene, nicht-autorschaftliche Aufgaben erstellt: Lektorat, sprachliche Glättung, Markdown-/LaTeX-Formatierung, Gerüstbau von Boilerplate-Dateien (CI-Konfigurationen, Build-Skripte), Code-Refactoring. Verwendet wurden Chat AI, der LLM-Dienst von KISSKI (GWDG), sowie ein selbst gehostetes Mistral Small (24B, Apache-2.0), lokal betrieben über Ollama und das R-Paket ollamar — ausschließlich lokale Inferenz, ohne Übermittlung von Daten an Dritte beim selbst gehosteten Modell.
