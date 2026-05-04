"""UI-Strings fuer den dreisprachigen Hub.

Eine Quelle der Wahrheit fuer alle Beschriftungen, Skill-Namen,
Hinweise und Tabellenkoepfe in DE / EN / FR. Wird sowohl von den
qmd-Generatoren als auch von der Render-Schicht importiert.
"""
from __future__ import annotations

LANGS = ("de", "en", "fr")

UI = {
    "site_title":       {"de": "#ressources", "en": "#ressources", "fr": "#ressources"},
    "landing_title":    {
        "de": "Ressourcen für den Sprachunterricht",
        "en": "Resources for the language classroom",
        "fr": "Ressources pour l'enseignement des langues",
    },
    "landing_subtitle": {
        "de": "Kuratierte, frei verfügbare Materialien für Englisch, Französisch und Deutsch als Fremdsprache.",
        "en": "Curated, freely accessible materials for English, French and German as a foreign language.",
        "fr": "Ressources sélectionnées et librement accessibles pour l'anglais, le français et l'allemand langue étrangère.",
    },
    "nav_language":     {"de": "Nach Sprache",     "en": "By language",  "fr": "Par langue"},
    "nav_skill":        {"de": "Nach Fertigkeit",  "en": "By skill",     "fr": "Par compétence"},
    "nav_level":        {"de": "Nach Niveau",      "en": "By level",     "fr": "Par niveau"},
    "nav_unit":         {"de": "Nach Unit",        "en": "By unit",      "fr": "Par unité"},
    "nav_about":        {"de": "Über",             "en": "About",        "fr": "À propos"},
    "nav_imprint":      {"de": "Impressum",        "en": "Imprint",      "fr": "Mentions légales"},
    "nav_privacy":      {"de": "Datenschutz",      "en": "Privacy",      "fr": "Confidentialité"},

    "footer":           {
        "de": "© S. Le Boulanger · Code: MIT · Inhalte: CC-BY-SA 4.0",
        "en": "© S. Le Boulanger · Code: MIT · Content: CC-BY-SA 4.0",
        "fr": "© S. Le Boulanger · Code : MIT · Contenus : CC-BY-SA 4.0",
    },

    "kicker":           {
        "de": "KURATIERT UND FREI VERFÜGBAR",
        "en": "CURATED AND FREELY AVAILABLE",
        "fr": "SÉLECTIONNÉ ET LIBREMENT ACCESSIBLE",
    },
    "hero_title":       {
        "de": "Ressourcen für den Sprachunterricht",
        "en": "Resources for the language classroom",
        "fr": "Ressources pour l'enseignement des langues",
    },
    "hero_lead":        {
        "de": "Eine kuratierte Sammlung frei zugänglicher Online-Ressourcen für Englisch, Französisch und Deutsch als Fremdsprache. Jede Ressource ist manuell geprüft, nach Niveau und Fertigkeit eingeordnet und mit kuratorischen Anmerkungen versehen.",
        "en": "A curated collection of freely accessible online resources for English, French and German as a foreign language. Every resource is reviewed by hand, classified by level and skill, and accompanied by editorial notes.",
        "fr": "Une sélection de ressources en ligne librement accessibles pour l'anglais, le français et l'allemand langue étrangère. Chaque ressource est vérifiée à la main, classée par niveau et par compétence, et accompagnée de notes éditoriales.",
    },

    "entries_heading":  {"de": "Einstiegspunkte", "en": "Entry points", "fr": "Points d'entrée"},
    "entry_lang_lead":  {
        "de": "Englisch, Französisch und Deutsch — jede Sprache mit einer eigenen kuratierten Auswahl.",
        "en": "English, French and German — each language with its own curated selection.",
        "fr": "Anglais, français et allemand — chaque langue avec sa propre sélection.",
    },
    "entry_skill_lead": {
        "de": "Hören, Lesen, Schreiben, Sprechen, Grammatik, Wortschatz und Landeskunde — direkter Zugriff.",
        "en": "Listening, reading, writing, speaking, grammar, vocabulary and culture — direct access.",
        "fr": "Compréhension orale, écrite, expression écrite, expression orale, grammaire, lexique et culture — accès direct.",
    },
    "entry_level_lead": {
        "de": "Von A1 bis C1 — alle Ressourcen, die für das gewählte CEFR-Niveau geeignet sind.",
        "en": "From A1 to C1 — every resource suitable for the chosen CEFR level.",
        "fr": "De A1 à C1 — toutes les ressources adaptées au niveau CECR choisi.",
    },
    "entry_unit_lead":  {
        "de": "Direkt passend zu den Unterrichtseinheiten der Schwestern-Sites EFL, FLE und DaF.",
        "en": "Directly mapped to the units of the sister sites EFL, FLE and DaF.",
        "fr": "Directement aligné sur les unités des sites jumeaux EFL, FLE et DaF.",
    },

    "criteria_heading": {
        "de": "Auswahlkriterien",
        "en": "Selection criteria",
        "fr": "Critères de sélection",
    },
    "criteria_text":    {
        "de": "Aufgenommen werden ausschließlich Ressourcen, die kostenfrei zugänglich sind und entweder von öffentlichen Einrichtungen bereitgestellt werden, unter Creative-Commons-Lizenz stehen oder gemeinfrei sind. Kommerzielle Anbieter und Marktplätze sind grundsätzlich ausgeschlossen.",
        "en": "Only resources that are freely accessible and either provided by public institutions, released under a Creative Commons licence, or in the public domain are included. Commercial providers and marketplaces are excluded as a matter of principle.",
        "fr": "Ne sont retenues que les ressources accessibles gratuitement et soit fournies par des institutions publiques, soit publiées sous licence Creative Commons, soit relevant du domaine public. Les fournisseurs commerciaux et places de marché sont exclus par principe.",
    },

    "passt_zu":         {"de": "Passt zu:",          "en": "Matches:",       "fr": "Convient à :"},
    "letzter_check":    {"de": "Letzter Link-Check:", "en": "Last link check:", "fr": "Dernière vérification :"},
    "ressource_open":   {"de": "Ressource öffnen",   "en": "Open resource",  "fr": "Ouvrir la ressource"},
    "no_resources":     {
        "de": "Für diese Auswahl sind noch keine Ressourcen kuratiert.",
        "en": "No resources have been curated for this selection yet.",
        "fr": "Aucune ressource n'a encore été sélectionnée pour ce choix.",
    },

    # ---- Sprach-Seitennamen (Vollform) ----
    "lang_en_full": {"de": "Englisch",  "en": "English", "fr": "Anglais"},
    "lang_fr_full": {"de": "Französisch","en": "French", "fr": "Français"},
    "lang_de_full": {"de": "Deutsch",   "en": "German",  "fr": "Allemand"},

    # ---- Skill-Namen ----
    "skill_hoeren":     {"de": "Hören",       "en": "Listening",   "fr": "Compréhension orale"},
    "skill_lesen":      {"de": "Lesen",       "en": "Reading",     "fr": "Compréhension écrite"},
    "skill_schreiben":  {"de": "Schreiben",   "en": "Writing",     "fr": "Expression écrite"},
    "skill_sprechen":   {"de": "Sprechen",    "en": "Speaking",    "fr": "Expression orale"},
    "skill_grammatik":  {"de": "Grammatik",   "en": "Grammar",     "fr": "Grammaire"},
    "skill_wortschatz": {"de": "Wortschatz",  "en": "Vocabulary",  "fr": "Lexique"},
    "skill_landeskunde":{"de": "Landeskunde", "en": "Culture",     "fr": "Culture"},

    # ---- Lead-Texte je Sprachseite ----
    "lead_lang_en": {
        "de": "Frei verfügbare Online-Ressourcen für den Englischunterricht. Schwerpunkt: British Council, BBC und weitere öffentlich-rechtliche Anbieter.",
        "en": "Freely available online resources for teaching English. Focus on the British Council, the BBC and other public broadcasters.",
        "fr": "Ressources en ligne librement accessibles pour l'enseignement de l'anglais. Accent sur le British Council, la BBC et d'autres organismes publics.",
    },
    "lead_lang_fr": {
        "de": "Frei verfügbare Online-Ressourcen für den Französischunterricht. Schwerpunkt: TV5Monde, RFI Savoirs und weitere frankophone Bildungseinrichtungen.",
        "en": "Freely available online resources for teaching French. Focus on TV5Monde, RFI Savoirs and other Francophone institutions.",
        "fr": "Ressources en ligne librement accessibles pour l'enseignement du français. Accent sur TV5Monde, RFI Savoirs et d'autres institutions francophones.",
    },
    "lead_lang_de": {
        "de": "Frei verfügbare Online-Ressourcen für Deutsch als Fremdsprache. Schwerpunkt: Deutsche Welle, Goethe-Institut und weitere öffentliche Mittlerorganisationen.",
        "en": "Freely available online resources for German as a foreign language. Focus on Deutsche Welle, Goethe-Institut and other public intermediaries.",
        "fr": "Ressources en ligne librement accessibles pour l'allemand langue étrangère. Accent sur la Deutsche Welle, le Goethe-Institut et d'autres institutions publiques.",
    },

    # ---- Lead-Texte je Skill ----
    "lead_skill_hoeren": {
        "de": "Materialien für das Hör- und Hör-Seh-Verstehen: Podcasts, Videos, Nachrichten und didaktisierte Audioformate.",
        "en": "Materials for listening and audiovisual comprehension: podcasts, videos, news and pedagogically prepared audio.",
        "fr": "Matériaux pour la compréhension orale et audiovisuelle : podcasts, vidéos, actualités et audio didactisé.",
    },
    "lead_skill_lesen": {
        "de": "Lesetexte und Leseübungen unterschiedlicher Niveaus — von didaktisierten Kurztexten bis zu authentischen Pressebeiträgen.",
        "en": "Reading texts and exercises at different levels — from pedagogically prepared short texts to authentic press articles.",
        "fr": "Textes et exercices de lecture à différents niveaux — du texte court didactisé à l'article de presse authentique.",
    },
    "lead_skill_schreiben": {
        "de": "Anregungen, Modelle und Übungsformate für das Schreiben in der Fremdsprache — vom Schreibimpuls bis zum Korrekturwerkzeug.",
        "en": "Prompts, models and practice formats for writing in the foreign language — from writing impulses to correction tools.",
        "fr": "Amorces, modèles et exercices d'écriture en langue étrangère — de l'incitation au travail de correction.",
    },
    "lead_skill_sprechen": {
        "de": "Sprechanlässe, Aussprachetraining und Modelle mündlicher Kommunikation — oft mit Audio- oder Videounterstützung.",
        "en": "Speaking prompts, pronunciation training and models of oral communication — often with audio or video support.",
        "fr": "Amorces de parole, entraînement à la prononciation et modèles de communication orale — souvent avec support audio ou vidéo.",
    },
    "lead_skill_grammatik": {
        "de": "Erklärungen und Übungen zu grammatischen Phänomenen, didaktisch aufbereitet und niveaudifferenziert.",
        "en": "Explanations and exercises on grammatical phenomena, prepared pedagogically and differentiated by level.",
        "fr": "Explications et exercices sur les phénomènes grammaticaux, didactisés et différenciés par niveau.",
    },
    "lead_skill_wortschatz": {
        "de": "Vokabeltrainer, thematische Wortschatzlisten und Übungen zum Aufbau und zur Festigung des Wortschatzes.",
        "en": "Vocabulary trainers, thematic word lists and exercises to build and consolidate vocabulary.",
        "fr": "Trainers de vocabulaire, listes thématiques et exercices pour acquérir et consolider le lexique.",
    },
    "lead_skill_landeskunde": {
        "de": "Materialien zu Kultur, Geschichte, Alltag und Gesellschaft der jeweiligen Sprachräume.",
        "en": "Materials on culture, history, everyday life and society of the respective language areas.",
        "fr": "Matériaux sur la culture, l'histoire, la vie quotidienne et la société des aires linguistiques concernées.",
    },

    # ---- Lead-Texte je CEFR-Niveau ----
    "lead_lvl_a1": {
        "de": "Einstiegsniveau — Ressourcen für absolute Anfängerinnen und Anfänger.",
        "en": "Beginner level — resources for absolute beginners.",
        "fr": "Niveau débutant — ressources pour grands débutants.",
    },
    "lead_lvl_a2": {
        "de": "Grundlegende Kommunikation in vertrauten Routinesituationen.",
        "en": "Basic communication in familiar everyday situations.",
        "fr": "Communication de base dans des situations familières.",
    },
    "lead_lvl_b1": {
        "de": "Selbständige Sprachverwendung in den meisten Alltagssituationen.",
        "en": "Independent language use in most everyday situations.",
        "fr": "Usage autonome de la langue dans la plupart des situations courantes.",
    },
    "lead_lvl_b2": {
        "de": "Sicheres Sprachhandeln auch zu komplexeren und abstrakten Themen.",
        "en": "Confident language use even on more complex and abstract topics.",
        "fr": "Maîtrise sûre de la langue, y compris sur des sujets complexes et abstraits.",
    },
    "lead_lvl_c1": {
        "de": "Differenzierter Sprachgebrauch für anspruchsvolle Texte und Diskurse.",
        "en": "Nuanced language use for demanding texts and discourse.",
        "fr": "Usage nuancé de la langue pour des textes et discours exigeants.",
    },

    # ---- Unit-Header ----
    "unit_efl_overview": {
        "de": "EFL — Übersicht",
        "en": "EFL — Overview",
        "fr": "EFL — Vue d'ensemble",
    },
    "unit_fle_overview": {
        "de": "FLE — Übersicht",
        "en": "FLE — Overview",
        "fr": "FLE — Vue d'ensemble",
    },
    "unit_daf_overview": {
        "de": "DaF — Übersicht",
        "en": "German as foreign language — Overview",
        "fr": "Allemand langue étrangère — Vue d'ensemble",
    },
    "unit_efl_lead": {
        "de": "Ressourcen, die zu den Englisch-Einheiten der Schwestern-Site passen. Wählen Sie die Klassenstufe.",
        "en": "Resources matching the English units of the sister site. Choose a grade level.",
        "fr": "Ressources correspondant aux unités d'anglais du site jumeau. Choisissez un niveau scolaire.",
    },
    "unit_fle_lead": {
        "de": "Ressourcen, die zu den Französisch-Einheiten der Schwestern-Site passen. Wählen Sie die Klassenstufe.",
        "en": "Resources matching the French units of the sister site. Choose a grade level.",
        "fr": "Ressources correspondant aux unités de français du site jumeau. Choisissez un niveau scolaire.",
    },
    "unit_daf_lead": {
        "de": "Ressourcen, die zu den DaF-Einheiten der Schwestern-Site passen. Wählen Sie das Niveau.",
        "en": "Resources matching the German units of the sister site. Choose a level.",
        "fr": "Ressources correspondant aux unités d'allemand du site jumeau. Choisissez un niveau.",
    },
    "klasse": {"de": "Klasse", "en": "Grade", "fr": "Niveau"},

    # ---- Uebersicht ----
    "nav_overview": {"de": "Übersicht", "en": "Overview", "fr": "Aperçu"},
    "overview_title": {
        "de": "Übersicht aller Ressourcen",
        "en": "Overview of all resources",
        "fr": "Aperçu de toutes les ressources",
    },
    "overview_lead": {
        "de": "Alle kuratierten Ressourcen mit Filter-Chips, Label-Netzwerk und drei automatisch ermittelten ähnlichen Vorschlägen pro Eintrag. Kein Tracking, kein externer Datenfluss.",
        "en": "All curated resources with filter chips, a label network and three automatically suggested similar entries per item. No tracking, no external data flow.",
        "fr": "Toutes les ressources sélectionnées avec des étiquettes de filtre, un réseau d'étiquettes et trois suggestions similaires calculées automatiquement par entrée. Aucun pistage, aucun envoi de données externe.",
    },

    "unit_efl_grade_lead": {
        "de": "Ressourcen, die zur EFL-Einheit der Klasse {k} passen.",
        "en": "Resources matching the EFL unit for grade {k}.",
        "fr": "Ressources correspondant à l'unité EFL du niveau {k}.",
    },
    "unit_fle_grade_lead": {
        "de": "Ressourcen, die zur FLE-Einheit der Klasse {k} passen.",
        "en": "Resources matching the FLE unit for grade {k}.",
        "fr": "Ressources correspondant à l'unité FLE du niveau {k}.",
    },
    "unit_daf_lvl_lead": {
        "de": "Ressourcen, die zur DaF-Einheit auf Niveau {lvl} passen.",
        "en": "Resources matching the German unit at level {lvl}.",
        "fr": "Ressources correspondant à l'unité d'allemand au niveau {lvl}.",
    },
}


def t(key: str, lang: str) -> str:
    """UI-String fuer Schluessel + Sprache. Faellt auf 'de' zurueck."""
    entry = UI.get(key, {})
    return entry.get(lang) or entry.get("de") or key


SKILL_LABEL_KEY = {
    "hoeren": "skill_hoeren",
    "lesen": "skill_lesen",
    "schreiben": "skill_schreiben",
    "sprechen": "skill_sprechen",
    "grammatik": "skill_grammatik",
    "wortschatz": "skill_wortschatz",
    "landeskunde": "skill_landeskunde",
}


def skill_label(skill: str, lang: str) -> str:
    return t(SKILL_LABEL_KEY.get(skill, skill), lang)
