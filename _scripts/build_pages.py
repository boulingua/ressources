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
lang: de
aliases:
  - /de/legal/impressum/
---

## Angaben gemäß § 5 DDG

S. Le Boulanger\\
Albert-Einstein-Straße 47\\
02977 Hoyerswerda\\
Deutschland

## Kontakt

E-Mail: [277736839+s-leboulanger@users.noreply.github.com](mailto:277736839+s-leboulanger@users.noreply.github.com)

Der Kontaktweg ist eine GitHub-Noreply-Adresse; Antworten können
entsprechend verzögert erfolgen. Für schnelle Fehlermeldungen ist
ein Issue im
[Repository](https://github.com/boulingua/ressources/issues) der
effizientere Weg.

## Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV

S. Le Boulanger\\
Albert-Einstein-Straße 47\\
02977 Hoyerswerda\\
Deutschland

## EU-Streitschlichtung

Die Europäische Kommission stellt eine Plattform zur
Online-Streitbeilegung (OS) bereit:
<https://ec.europa.eu/consumers/odr/>.

Ich bin nicht verpflichtet und nicht bereit, an einem
Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle
teilzunehmen.

## Haftung für Inhalte

Hinweise zur Haftung für eigene Inhalte, fremde Inhalte und Links
sowie zum Urheberrecht finden Sie auf der Seite
[Haftungsausschluss](disclaimer.qmd).
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
lang: de
aliases:
  - /de/legal/privacy/
---

## 1. Verantwortlicher

Verantwortliche Stelle im Sinne der Datenschutz-Grundverordnung
(DSGVO) ist:

S. Le Boulanger\\
Albert-Einstein-Straße 47\\
02977 Hoyerswerda\\
Deutschland

E-Mail: [277736839+s-leboulanger@users.noreply.github.com](mailto:277736839+s-leboulanger@users.noreply.github.com)

Eine gesetzliche Pflicht zur Bestellung einer/eines
Datenschutzbeauftragten besteht nicht; entsprechend ist keine
solche Person bestellt.

## 2. Allgemeine Hinweise und Pflichtinformationen

### Datenschutz auf einen Blick

Diese Website ist ein nicht-kommerzielles, kuratorisches Angebot
mit Verweisen auf frei verfügbare didaktische Ressourcen. Es
werden so wenige personenbezogene Daten verarbeitet wie technisch
möglich.

### Rechtsgrundlagen der Datenverarbeitung

- **Art. 6 Abs. 1 lit. a DSGVO** — Einwilligung,
- **Art. 6 Abs. 1 lit. b DSGVO** — vorvertragliche Maßnahmen,
- **Art. 6 Abs. 1 lit. f DSGVO** — berechtigte Interessen
  (insbesondere stabiler Betrieb, Sicherheit, statistische
  Reichweitenmessung).

### Empfänger und Übermittlung in Drittländer

Hosting der Website-Auslieferung erfolgt durch GitHub, Inc.;
Schriftarten werden über Google Fonts (Google Ireland Limited)
ausgeliefert. Beide können Verbindungsdaten in die USA
übermitteln; Grundlage sind das EU-US Data Privacy Framework
bzw. Standardvertragsklauseln. Eine darüber hinausgehende
Übermittlung in Drittländer findet **nicht** statt. Die
Reichweitenmessung mittels Plausible Analytics erfolgt auf einer
**selbst gehosteten Instanz auf einem Server in Deutschland**.

### Beschwerderecht

**Sächsischer Datenschutz- und Transparenzbeauftragter**\\
Devrientstraße 1\\
01067 Dresden\\
<https://www.saechsdsb.de/>

### Ihre Rechte

Auskunft (Art. 15), Berichtigung (16), Löschung (17),
Einschränkung (18), Datenübertragbarkeit (20), Widerspruch (21),
Widerruf (Art. 7 Abs. 3), Beschwerde (Art. 77).

### SSL- bzw. TLS-Verschlüsselung

Diese Seite nutzt aus Sicherheitsgründen eine TLS-
Verschlüsselung.

## 3. Datenerfassung auf dieser Website

### Server-Log-Dateien

GitHub Pages (GitHub, Inc., 88 Colin P Kelly Jr St, San
Francisco, CA 94107, USA) erhebt automatisch Server-Log-Dateien
(Browsertyp, Betriebssystem, Referrer-URL, Hostname, Uhrzeit,
IP-Adresse). Eine Zusammenführung mit anderen Datenquellen durch
die Verantwortliche findet **nicht** statt. Rechtsgrundlage:
Art. 6 Abs. 1 lit. f DSGVO.
[GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).

### Cookies

Diese Website setzt **keine eigenen Tracking-Cookies**.
Technisch notwendige Cookies (z. B. Sprachpräferenz) sind durch
§ 25 Abs. 2 Nr. 2 TDDDG gedeckt.

## 4. Analyse-Tools und Tools von Drittanbietern

### Plausible Analytics (selbst gehostet)

Diese Website verwendet **Plausible Analytics** zur statistischen
Reichweitenmessung. Plausible wird als **selbst gehostete
Instanz** unter `analytics.hellebo.de` betrieben; der Server
steht in **Deutschland**. Eine Übermittlung an Plausible
Insights OÜ oder andere Drittanbieter findet **nicht** statt.
Plausible ist cookielos und erhebt keine personenbezogenen
Daten im engeren Sinn. IP-Adressen werden nicht gespeichert; zur
Sitzungserkennung wird täglich rotierend ein gesalzener Hash
gebildet. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. Eine
Einwilligung nach § 25 TDDDG ist nicht erforderlich.
<https://plausible.io/data-policy>

### VG Wort Zählpixel (Standard)

Auf einzelnen, kennzeichenpflichtig angemeldeten Inhaltsseiten
kann ein **Zählpixel** der Verwertungsgesellschaft WORT
eingebunden sein:

**Verwertungsgesellschaft WORT (VG WORT)**\\
Untere Weidenstraße 5\\
81543 München\\
Deutschland\\
<https://www.vgwort.de/>

Zweck: Erfassung statistischer Kennzahlen zur Berechnung von
Vergütungsansprüchen gemäß § 53 UrhG / METIS-Programm. Es werden
**keine Cookies** gesetzt; die IP-Adresse wird durch VG Wort
SHA-256-gehasht und gekürzt. Verarbeitung auf Servern in
Deutschland. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.
<https://www.vgwort.de/datenschutz.html>

### GitHub Pages

Anbieterin: GitHub, Inc., 88 Colin P Kelly Jr St, San Francisco,
CA 94107, USA.
[GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).

## 5. Eingebettete Inhalte und Schriftarten

### Google Fonts (CDN)

Diese Website bindet Schriften (Source Sans 3, JetBrains Mono)
über die Google-Fonts-CDN ein. Beim Aufruf überträgt Ihr Browser
Verbindungsdaten an Google (Google Ireland Limited).
Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO.
<https://policies.google.com/privacy>.

### Externe Verlinkungen

Diese Website ist primär ein Verzeichnis externer Ressourcen.
Beim Klick auf solche Links verlassen Sie diese Seite; die
jeweilige Datenschutzpolitik des verlinkten Angebots gilt.

## 6. Ihre Rechte als betroffene Person

Auskunft (Art. 15), Berichtigung (16), Löschung (17),
Einschränkung (18), Datenübertragbarkeit (20), Widerspruch (21),
Widerruf (Art. 7 Abs. 3), Beschwerde (Art. 77).

Wahrnehmung über die unter Abschnitt 1 genannte Verantwortliche.
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


DISCLAIMER = {
    "de": """---
title: "Haftungsausschluss"
lang: de
aliases:
  - /de/legal/disclaimer/
---

## Haftung für Inhalte

Als Diensteanbieterin bin ich gemäß § 7 Abs. 1 DDG für eigene
Inhalte auf diesen Seiten nach den allgemeinen Gesetzen
verantwortlich. Nach §§ 8 bis 10 DDG bin ich als
Diensteanbieterin jedoch nicht verpflichtet, übermittelte oder
gespeicherte fremde Informationen zu überwachen oder nach
Umständen zu forschen, die auf eine rechtswidrige Tätigkeit
hinweisen. Verpflichtungen zur Entfernung oder Sperrung der
Nutzung von Informationen nach den allgemeinen Gesetzen bleiben
hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst
ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung
möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen
werde ich diese Inhalte umgehend entfernen.

## Haftung für Links

Dieses Angebot ist primär eine kuratierte Sammlung von
Verweisen auf externe Ressourcen Dritter. Auf deren Inhalte habe
ich keinen Einfluss. Deshalb kann ich für diese fremden Inhalte
auch keine Gewähr übernehmen. Für die Inhalte der verlinkten
Seiten ist stets der jeweilige Anbieter oder Betreiber der
Seiten verantwortlich. Die verlinkten Seiten wurden zum
Zeitpunkt der Aufnahme auf mögliche Rechtsverstöße überprüft;
rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht
erkennbar.

Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist
ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht
zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden solche
Links umgehend entfernt.

## Urheberrecht

Die durch die Seitenbetreiberin erstellten kuratorischen Inhalte
unterliegen dem deutschen Urheberrecht. Code dieser Website
steht unter der **MIT-Lizenz**, kuratorische Inhalte unter
**CC-BY-SA 4.0**. Die verlinkten Ressourcen unterliegen den
Lizenzen ihrer jeweiligen Anbieter; vor Weiterverwendung ist
deren Lizenz zu beachten.

Sollten Sie auf eine Urheberrechtsverletzung aufmerksam werden,
bitte ich um einen entsprechenden Hinweis.
""",
    "en": """---
title: "Disclaimer"
lang: en
---

The German "Haftungsausschluss" is the legally binding version.
The English text below is provided for convenience.

## Liability for content

As a service provider I am liable for own content on these
pages under the general laws (§ 7 (1) DDG). Under §§ 8–10 DDG I
am not obliged, however, to monitor transmitted or stored
third-party information or to investigate circumstances that
indicate illegal activity. Any liability is contingent upon
knowledge of a specific infringement; on becoming aware of one
I will remove the content without delay.

## Liability for links

This site is essentially a directory of third-party resources.
The respective providers remain solely responsible for the
content of the linked pages. Links were checked at the time of
inclusion; no infringing content was discernible. Any link
later found to infringe rights will be removed without delay.

## Copyright

Curatorial content created by the operator is subject to German
copyright law. Site code is licensed under the **MIT licence**;
curatorial content under **CC-BY-SA 4.0**. Linked resources are
subject to their providers' licences.
""",
    "fr": """---
title: "Avis de non-responsabilité"
lang: fr
---

La version juridiquement contraignante est l'« Haftungsausschluss »
en allemand. Le texte français ci-dessous est fourni à titre
de commodité.

## Responsabilité du contenu

En tant que fournisseur de services, je suis responsable des
contenus propres conformément aux lois générales (§ 7 (1) DDG).
Conformément aux §§ 8 à 10 DDG, je ne suis cependant pas tenue
de surveiller les informations tierces transmises ou stockées
ni de rechercher des circonstances indiquant une activité
illicite. Une responsabilité ne peut être engagée qu'à compter
de la connaissance d'une violation concrète ; toute violation
identifiée sera supprimée sans délai.

## Responsabilité concernant les liens

Ce site est avant tout un répertoire de ressources tierces. Le
contenu des pages liées relève exclusivement de la
responsabilité de leurs fournisseurs respectifs. Les liens ont
été vérifiés au moment de leur inclusion ; aucun contenu
illicite n'était discernible. Tout lien ultérieurement constaté
comme portant atteinte à des droits sera supprimé sans délai.

## Droits d'auteur

Les contenus éditoriaux créés par l'opératrice sont protégés
par le droit d'auteur allemand. Le code du site est sous
licence **MIT**, les contenus éditoriaux sous **CC-BY-SA 4.0**.
Les ressources liées sont soumises aux licences de leurs
fournisseurs.
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

        # ----- About / Imprint / Privacy / Disclaimer -----
        write(f"{lang}/about.qmd", ABOUT[lang])
        write(f"{lang}/imprint.qmd", IMPRINT[lang])
        write(f"{lang}/privacy.qmd", PRIVACY[lang])
        write(f"{lang}/disclaimer.qmd", DISCLAIMER[lang])

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
