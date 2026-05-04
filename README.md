# Ressourcen

Kuratierte Sammlung frei verfuegbarer Online-Ressourcen fuer
Englisch, Franzoesisch und Deutsch als Fremdsprache.

Live: <https://boulingua.github.io/ressources/>

## Lizenzen

- **Code** (Quarto-Konfiguration, Python-Skripte, CSS, CI):
  MIT - siehe [LICENSE](LICENSE).
- **Inhalte** (Beschreibungen, Annotationen, Einleitungstexte,
  `_resources/sources_master.yml`): CC-BY-SA 4.0 - siehe
  [LICENSE-content](LICENSE-content).
- **Verlinkte externe Ressourcen**: jeweilige Lizenz der
  Anbieter (siehe `license_type` und `license_details` pro
  Ressource).

## Lokal bauen

```bash
pip install pyyaml jupyter
python _scripts/validate_sources.py
python _scripts/check_commercial.py
quarto render
```

## Autorin

Alle kuratorischen Inhalte: S. Le Boulanger.
