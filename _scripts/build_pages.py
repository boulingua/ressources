"""Generator fuer alle Content-qmd-Dateien in DE / EN / FR.

Liest Texte aus i18n.UI und erzeugt parallel:
  de/<...>.qmd, en/<...>.qmd, fr/<...>.qmd
Wird einmal beim Bootstrap und nach jeder Anpassung an i18n.UI
ausgefuehrt; in CI als Render-Vorstufe (siehe deploy.yml).
"""
from __future__ import annotations

from pathlib import Path

from i18n import LANGS, t

ROOT = Path(__file__).resolve().parent.parent

CHUNK = '''```{{python}}
#| echo: false
import sys
from pathlib import Path
_p = Path.cwd().resolve()
while _p != _p.parent and not (_p / "_quarto.yml").exists():
    _p = _p.parent
sys.path.insert(0, str(_p / "_scripts"))
from render_resources import render_filtered
render_filtered({args}, lang="{lang}")
```
'''


def write(rel: str, body: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def chunk(args: str, lang: str) -> str:
    return CHUNK.format(args=args, lang=lang)


# ---------- Landing page (per language) -----------------------
def landing(lang: str) -> str:
    return f"""---
title: "{t('landing_title', lang)}"
subtitle: "{t('landing_subtitle', lang)}"
pagetitle: "{t('site_title', lang)} – {t('landing_title', lang)}"
toc: false
---

::: {{.hero}}
::: {{.kicker}}
{t('kicker', lang)}
:::

{t('hero_lead', lang)}
:::

## {t('entries_heading', lang)}

::: {{.card-grid}}

::: {{.entry-card}}
### [{t('nav_language', lang)}](nach_sprache/englisch.qmd)
{t('entry_lang_lead', lang)}
:::

::: {{.entry-card}}
### [{t('nav_skill', lang)}](nach_fertigkeit/hoeren.qmd)
{t('entry_skill_lead', lang)}
:::

::: {{.entry-card}}
### [{t('nav_level', lang)}](nach_niveau/a1.qmd)
{t('entry_level_lead', lang)}
:::

::: {{.entry-card}}
### [{t('nav_unit', lang)}](nach_unit/efl/index.qmd)
{t('entry_unit_lead', lang)}
:::

:::

## {t('criteria_heading', lang)}

{t('criteria_text', lang)}
"""


# ---------- About / Imprint / Privacy -------------------------
ABOUT = {
    "de": """---
title: "Über den Hub"
---

#ressources ist eine kuratierte Sammlung frei zugänglicher
Online-Materialien für den Unterricht in Englisch, Französisch
und Deutsch als Fremdsprache. Der Hub ist weder Aggregator
noch Crawler, sondern eine handverlesene Auswahl — jede
Ressource wird einzeln geprüft, eingeordnet und mit einer
kuratorischen Anmerkung versehen.

## Was hier zu finden ist

Der Hub verlinkt auf Plattformen öffentlicher Einrichtungen
(British Council, BBC, Deutsche Welle, Goethe-Institut,
TV5Monde), auf Materialien unter Creative-Commons-Lizenz und
auf gemeinfreie Inhalte. Die Ressourcen sind nach Sprache,
Fertigkeit, GER-Niveau und nach Bezug zu konkreten Einheiten
der drei Schwestern-Sites geordnet:

- [Englisch in der Sekundarstufe](https://boulingua.github.io/efl/)
- [Französisch in der Sekundarstufe](https://boulingua.github.io/fle/)
- [Deutsch als Fremdsprache nach GER](https://boulingua.github.io/daf/)

## Was ausgeschlossen ist

Kommerzielle Anbieter, Verlage und Marktplätze — auch solche
mit teilweise freien Angeboten — sind grundsätzlich nicht
aufgeführt. Der Hub soll Lehrende auf Materialien hinweisen,
die ohne finanzielle oder vertragliche Hürden genutzt und
verlinkt werden können.

## Lizenztypen

- **OE** — Öffentliche Einrichtung. Vollurheberrecht beim
  Anbieter, frei zugänglich, verlinkbar, nicht kopierbar.
- **CC** — Creative Commons. Wiederverwendbar unter den
  jeweiligen Lizenzbedingungen.
- **PD** — Public Domain. Gemeinfrei, ohne Einschränkungen.

## Autorin

Alle kuratorischen Inhalte stammen von S. Le Boulanger.
""",
    "en": """---
title: "About the hub"
---

#ressources is a curated collection of freely accessible
online materials for teaching English, French and German as
foreign languages. The hub is neither an aggregator nor a
crawler but a hand-picked selection — every resource is
reviewed individually, classified, and given an editorial note.

## What you'll find here

The hub links to platforms run by public institutions (British
Council, BBC, Deutsche Welle, Goethe-Institut, TV5Monde), to
Creative Commons material, and to public-domain content.
Resources are organised by language, skill, CEFR level and
mapping to concrete units on the three sister sites:

- [English in secondary education](https://boulingua.github.io/efl/)
- [French in secondary education](https://boulingua.github.io/fle/)
- [German as a foreign language by CEFR](https://boulingua.github.io/daf/)

## What's excluded

Commercial providers, publishers and marketplaces — including
those with partially free offerings — are not listed on
principle. The hub points teachers to materials they can use
and link to without financial or contractual hurdles.

## Licence types

- **OE** — Public institution. Full copyright with the
  provider; freely accessible, linkable, not copyable.
- **CC** — Creative Commons. Reusable under the respective
  licence terms.
- **PD** — Public domain. No restrictions.

## Editor

All curatorial content is by S. Le Boulanger.
""",
    "fr": """---
title: "À propos"
---

#ressources est une sélection de ressources en ligne
librement accessibles pour l'enseignement de l'anglais, du
français et de l'allemand langue étrangère. Le hub n'est ni
un agrégateur ni un crawler mais une sélection manuelle —
chaque ressource est vérifiée individuellement, classée et
accompagnée d'une note éditoriale.

## Ce que vous y trouverez

Le hub renvoie vers des plateformes d'institutions publiques
(British Council, BBC, Deutsche Welle, Goethe-Institut,
TV5Monde), vers des contenus sous licence Creative Commons et
vers des contenus du domaine public. Les ressources sont
organisées par langue, compétence, niveau du CECR et par
correspondance avec des unités concrètes des trois sites
jumeaux :

- [Anglais dans l'enseignement secondaire](https://boulingua.github.io/efl/)
- [Français dans l'enseignement secondaire](https://boulingua.github.io/fle/)
- [Allemand langue étrangère selon le CECR](https://boulingua.github.io/daf/)

## Ce qui est exclu

Les fournisseurs commerciaux, éditeurs et places de marché —
y compris ceux qui proposent une partie en accès libre — ne
sont pas répertoriés par principe. Le hub oriente les
enseignants vers des supports utilisables et partageables
sans barrière financière ni contractuelle.

## Types de licence

- **OE** — Institution publique. Plein droit d'auteur chez le
  fournisseur ; librement accessible, partageable, non copiable.
- **CC** — Creative Commons. Réutilisable selon les conditions
  de la licence.
- **PD** — Domaine public. Sans restriction.

## Éditrice

Tous les contenus éditoriaux sont de S. Le Boulanger.
""",
}

IMPRINT = {
    "de": """---
title: "Impressum"
---

## Angaben gemäß § 5 TMG

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Deutschland

## Kontakt

E-Mail: 277736839+s-leboulanger@users.noreply.github.com

## Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Deutschland

## Haftung für Inhalte

Die Inhalte dieses Hubs wurden mit größter Sorgfalt erstellt.
Für die Richtigkeit, Vollständigkeit und Aktualität wird keine
Gewähr übernommen.

## Haftung für Links

Dieser Hub verlinkt auf externe Ressourcen Dritter. Für deren
Inhalte ist stets der jeweilige Anbieter verantwortlich. Die
Ressourcen wurden zum Zeitpunkt der Aufnahme geprüft. Bei
Bekanntwerden von Rechtsverletzungen werden betroffene Links
unverzüglich entfernt.

## Urheberrecht

Code: MIT-Lizenz. Kuratorische Inhalte: CC-BY-SA 4.0. Die
verlinkten Ressourcen unterliegen den Lizenzen ihrer Anbieter.
""",
    "en": """---
title: "Imprint"
---

This site is operated from Germany; the German imprint
("Impressum") is the legally binding version. The English
text below is provided for convenience.

## Provider

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Germany

Contact: 277736839+s-leboulanger@users.noreply.github.com

## Responsible for content (§ 55 (2) RStV)

S. Le Boulanger, address above.

## Liability for content

Content has been compiled with utmost care, but no warranty is
given for completeness, accuracy or timeliness.

## Liability for links

This hub links to third-party resources. The respective
providers remain solely responsible for their content. Links
were checked at the time of inclusion. Any link found to
infringe rights will be removed without delay.

## Copyright

Code: MIT licence. Curatorial content: CC-BY-SA 4.0. Linked
resources are subject to their providers' licences.
""",
    "fr": """---
title: "Mentions légales"
---

Ce site est exploité depuis l'Allemagne ; la version
juridiquement contraignante est l'« Impressum » en allemand.
Le texte français ci-dessous est fourni à titre de commodité.

## Responsable

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Allemagne

Contact : 277736839+s-leboulanger@users.noreply.github.com

## Responsable du contenu (§ 55 al. 2 RStV)

S. Le Boulanger, adresse ci-dessus.

## Responsabilité du contenu

Les contenus ont été élaborés avec le plus grand soin, sans
garantie d'exhaustivité, d'exactitude ou d'actualité.

## Responsabilité concernant les liens

Ce hub renvoie vers des ressources tierces. Leur contenu
relève exclusivement de la responsabilité du fournisseur
concerné. Les liens ont été vérifiés au moment de leur
inclusion. Tout lien constaté comme portant atteinte à des
droits sera supprimé sans délai.

## Droits d'auteur

Code : licence MIT. Contenus éditoriaux : CC-BY-SA 4.0. Les
ressources liées sont soumises aux licences de leurs
fournisseurs.
""",
}

PRIVACY = {
    "de": """---
title: "Datenschutzerklärung"
---

## Verantwortliche Stelle

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Deutschland
E-Mail: 277736839+s-leboulanger@users.noreply.github.com

## Hosting

Diese Site wird über GitHub Pages gehostet. Anbieter ist
GitHub, Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA
94107, USA. Beim Aufruf der Seiten werden technische Daten
(IP-Adresse, Datum, Uhrzeit, abgerufene Ressource) durch
GitHub verarbeitet. Details:
<https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement>.

## Cookies, Tracking, Analytics

Diese Site setzt keine eigenen Cookies, verwendet kein
Tracking und keine Analyse-Werkzeuge.

## Externe Links

Bei Klick auf einen externen Link erfolgt keine
Datenübertragung durch diese Site an die Zielseite. Sobald
Sie den Link aufgerufen haben, gelten die
Datenschutzbestimmungen des jeweiligen Anbieters.

## SSL

Die Site wird ausschließlich über HTTPS bereitgestellt.

## Ihre Rechte

Sie haben das Recht auf Auskunft, Berichtigung, Löschung und
Einschränkung der Verarbeitung Ihrer personenbezogenen Daten
sowie auf Widerspruch und Datenübertragbarkeit gemäß
Art. 15–21 DSGVO.
""",
    "en": """---
title: "Privacy"
---

## Controller

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Germany
Email: 277736839+s-leboulanger@users.noreply.github.com

## Hosting

This site is hosted on GitHub Pages (GitHub, Inc., 88 Colin
P. Kelly Jr. St., San Francisco, CA 94107, USA). On every
page request GitHub processes technical data (IP address,
timestamp, requested resource). See:
<https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement>.

## Cookies, tracking, analytics

This site sets no cookies of its own and uses neither
tracking nor analytics.

## External links

Clicking an external link does not transmit any data from
this site to the destination. Once you follow the link, the
target site's privacy policy applies.

## SSL

The site is served exclusively over HTTPS.

## Your rights

You have the right to access, rectification, erasure and
restriction of processing of your personal data, plus rights
of objection and data portability under Articles 15–21 GDPR.
""",
    "fr": """---
title: "Confidentialité"
---

## Responsable du traitement

S. Le Boulanger
Albert-Einstein-Straße 47
02977 Hoyerswerda
Allemagne
Courriel : 277736839+s-leboulanger@users.noreply.github.com

## Hébergement

Ce site est hébergé sur GitHub Pages (GitHub, Inc., 88 Colin
P. Kelly Jr. St., San Francisco, CA 94107, États-Unis). À
chaque requête, GitHub traite des données techniques (adresse
IP, horodatage, ressource demandée). Voir :
<https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement>.

## Cookies, traçage, analyse

Ce site ne dépose aucun cookie propre et n'utilise ni
traçage ni outils d'analyse.

## Liens externes

Cliquer sur un lien externe ne transmet aucune donnée de ce
site vers la cible. Une fois sur le site cible, sa politique
de confidentialité s'applique.

## SSL

Le site est servi exclusivement en HTTPS.

## Vos droits

Vous disposez d'un droit d'accès, de rectification,
d'effacement et de limitation du traitement de vos données
personnelles, ainsi que du droit d'opposition et à la
portabilité des données (art. 15–21 RGPD).
""",
}


def overview_page(lang: str) -> str:
    return f"""---
title: "{t('overview_title', lang)}"
pagetitle: "{t('overview_title', lang)}"
toc: false
---

{t('overview_lead', lang)}

```{{=html}}
<link rel="stylesheet"
      href="https://unpkg.com/vis-network/styles/vis-network.min.css">
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<div id="overview-root"
     data-json="../assets/data/resources.{lang}.json"></div>

<script src="../assets/js/overview.js"></script>
```
"""


def view_page(title: str, lead: str, args: str, lang: str) -> str:
    return f"""---
title: "{title}"
---

{lead}

{chunk(args, lang)}"""


def card_grid_unit_links(items: list[tuple[str, str]]) -> str:
    """items: list of (label, href)."""
    return (
        "::: {.card-grid}\n"
        + "\n".join(
            f"::: {{.entry-card}}\n### [{lab}]({href})\n:::\n"
            for lab, href in items
        )
        + ":::\n"
    )


# ---------- Build all pages -----------------------------------
def build():
    languages_for_pages = {"englisch.qmd": "EN", "franzoesisch.qmd": "FR", "deutsch.qmd": "DE"}
    lang_full_keys = {"englisch.qmd": "lang_en_full",
                      "franzoesisch.qmd": "lang_fr_full",
                      "deutsch.qmd": "lang_de_full"}
    lang_lead_keys = {"englisch.qmd": "lead_lang_en",
                      "franzoesisch.qmd": "lead_lang_fr",
                      "deutsch.qmd": "lead_lang_de"}

    skills = ["hoeren", "lesen", "schreiben", "sprechen",
              "grammatik", "wortschatz", "landeskunde"]
    levels = ["a1", "a2", "b1", "b2", "c1"]

    for lang in LANGS:
        # ----- Landing -----
        write(f"{lang}/index.qmd", landing(lang))

        # ----- Overview (Filter + Graph + Related) -----
        # Pfad zur JSON-Datei: liegt unter assets/data/, also relativ
        # vom Sub-Ordner: ../assets/data/...
        write(f"{lang}/overview.qmd", overview_page(lang))

        # ----- About / Imprint / Privacy -----
        write(f"{lang}/about.qmd", ABOUT[lang])
        write(f"{lang}/imprint.qmd", IMPRINT[lang])
        write(f"{lang}/privacy.qmd", PRIVACY[lang])

        # ----- By language -----
        for fn, code in languages_for_pages.items():
            title = f"{t(lang_full_keys[fn], lang)}"
            lead = t(lang_lead_keys[fn], lang)
            write(f"{lang}/nach_sprache/{fn}",
                  view_page(title, lead, f'language="{code}"', lang))

        # ----- By skill -----
        for sk in skills:
            title = t(f"skill_{sk}", lang)
            lead = t(f"lead_skill_{sk}", lang)
            write(f"{lang}/nach_fertigkeit/{sk}.qmd",
                  view_page(title, lead, f'skill="{sk}"', lang))

        # ----- By level -----
        for lv in levels:
            title = lv.upper()
            lead = t(f"lead_lvl_{lv}", lang)
            write(f"{lang}/nach_niveau/{lv}.qmd",
                  view_page(title, lead, f'cefr_level="{lv.upper()}"', lang))

        # ----- By unit (EFL) -----
        klasse = t("klasse", lang)
        items = [(f"{klasse} {k}", f"kl{k:02d}.qmd") for k in range(5, 14)]
        write(f"{lang}/nach_unit/efl/index.qmd",
              f"""---
title: "{t('unit_efl_overview', lang)}"
---

{t('unit_efl_lead', lang)}

{card_grid_unit_links(items)}""")
        for k in range(5, 14):
            title = f"EFL — {klasse} {k}"
            lead = t("unit_efl_grade_lead", lang).format(k=k)
            write(f"{lang}/nach_unit/efl/kl{k:02d}.qmd",
                  view_page(title, lead, f'unit_prefix="efl_kl{k}"', lang))

        # ----- By unit (FLE) -----
        items = [(f"{klasse} {k}", f"kl{k:02d}.qmd") for k in range(6, 14)]
        write(f"{lang}/nach_unit/fle/index.qmd",
              f"""---
title: "{t('unit_fle_overview', lang)}"
---

{t('unit_fle_lead', lang)}

{card_grid_unit_links(items)}""")
        for k in range(6, 14):
            title = f"FLE — {klasse} {k}"
            lead = t("unit_fle_grade_lead", lang).format(k=k)
            write(f"{lang}/nach_unit/fle/kl{k:02d}.qmd",
                  view_page(title, lead, f'unit_prefix="fle_kl{k}"', lang))

        # ----- By unit (DaF) -----
        items = [(lvl.upper(), f"{lvl}.qmd") for lvl in levels]
        write(f"{lang}/nach_unit/daf/index.qmd",
              f"""---
title: "{t('unit_daf_overview', lang)}"
---

{t('unit_daf_lead', lang)}

{card_grid_unit_links(items)}""")
        for lvl in levels:
            title = f"DaF — {lvl.upper()}"
            lead = t("unit_daf_lvl_lead", lang).format(lvl=lvl.upper())
            write(f"{lang}/nach_unit/daf/{lvl}.qmd",
                  view_page(title, lead, f'unit_prefix="daf_{lvl}"', lang))

    print("Pages generated for languages:", LANGS)


if __name__ == "__main__":
    build()
