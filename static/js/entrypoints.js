/* ============================================================
   Sprachabhaengige Sub-Navbar mit den vier Einstiegspunkten
   (Sprache / Fertigkeit / Niveau / Unit) als Top-Header mit
   Items darunter. Wird nur auf Seiten unterhalb /de|en|fr/
   angezeigt; auf der Sprach-Picker-Wurzelseite ausgeblendet.
   ============================================================ */
(function () {
  const m = location.pathname.match(/\/(de|en|fr)(?:\/|$)/);
  if (!m) return;
  const lang = m[1];
  const idx = location.pathname.indexOf('/' + lang + '/');
  const langRoot = location.pathname.slice(0, idx) + '/' + lang + '/';

  const LABELS = {
    de: {
      lang: 'Sprache', skill: 'Fertigkeit', level: 'Niveau', unit: 'Unit',
      langItems: [
        ['Englisch',     'nach_sprache/englisch.html'],
        ['Französisch',  'nach_sprache/franzoesisch.html'],
        ['Deutsch',      'nach_sprache/deutsch.html'],
      ],
      skillItems: [
        ['Hören',        'nach_fertigkeit/hoeren.html'],
        ['Lesen',        'nach_fertigkeit/lesen.html'],
        ['Schreiben',    'nach_fertigkeit/schreiben.html'],
        ['Sprechen',     'nach_fertigkeit/sprechen.html'],
        ['Grammatik',    'nach_fertigkeit/grammatik.html'],
        ['Wortschatz',   'nach_fertigkeit/wortschatz.html'],
        ['Landeskunde',  'nach_fertigkeit/landeskunde.html'],
      ],
    },
    en: {
      lang: 'Language', skill: 'Skill', level: 'Level', unit: 'Unit',
      langItems: [
        ['English',      'nach_sprache/englisch.html'],
        ['French',       'nach_sprache/franzoesisch.html'],
        ['German',       'nach_sprache/deutsch.html'],
      ],
      skillItems: [
        ['Listening',    'nach_fertigkeit/hoeren.html'],
        ['Reading',      'nach_fertigkeit/lesen.html'],
        ['Writing',      'nach_fertigkeit/schreiben.html'],
        ['Speaking',     'nach_fertigkeit/sprechen.html'],
        ['Grammar',      'nach_fertigkeit/grammatik.html'],
        ['Vocabulary',   'nach_fertigkeit/wortschatz.html'],
        ['Culture',      'nach_fertigkeit/landeskunde.html'],
      ],
    },
    fr: {
      lang: 'Langue', skill: 'Compétence', level: 'Niveau', unit: 'Unité',
      langItems: [
        ['Anglais',                 'nach_sprache/englisch.html'],
        ['Français',                'nach_sprache/franzoesisch.html'],
        ['Allemand',                'nach_sprache/deutsch.html'],
      ],
      skillItems: [
        ['Compréhension orale',     'nach_fertigkeit/hoeren.html'],
        ['Compréhension écrite',    'nach_fertigkeit/lesen.html'],
        ['Expression écrite',       'nach_fertigkeit/schreiben.html'],
        ['Expression orale',        'nach_fertigkeit/sprechen.html'],
        ['Grammaire',               'nach_fertigkeit/grammatik.html'],
        ['Lexique',                 'nach_fertigkeit/wortschatz.html'],
        ['Culture',                 'nach_fertigkeit/landeskunde.html'],
      ],
    },
  };
  const LEVELS = ['a1', 'a2', 'b1', 'b2', 'c1'];
  const UNITS = [
    ['EFL', 'nach_unit/efl/index.html'],
    ['FLE', 'nach_unit/fle/index.html'],
    ['DaF', 'nach_unit/daf/index.html'],
  ];

  const L = LABELS[lang];
  const levelItems = LEVELS.map(l => [l.toUpperCase(), 'nach_niveau/' + l + '.html']);

  function escape(s) {
    return String(s).replace(/[&<>"']/g, c => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    ));
  }

  function activeClass(href) {
    const target = langRoot + href;
    return location.pathname.endsWith(href.split('/').pop())
      && location.pathname.includes(href.replace(/index\.html$/, ''))
      ? ' active' : '';
  }

  function group(label, items) {
    const links = items
      .map(([txt, href]) => `<a href="${langRoot}${href}" class="ep-item${activeClass(href)}">${escape(txt)}</a>`)
      .join('');
    return `
      <div class="ep-group">
        <div class="ep-group-label">${escape(label)}</div>
        <div class="ep-group-items">${links}</div>
      </div>`;
  }

  function build() {
    const navbar = document.querySelector('header#quarto-header')
                || document.querySelector('nav.navbar')?.parentElement
                || document.body;
    const subnav = document.createElement('div');
    subnav.className = 'entry-subnav';
    subnav.innerHTML = `
      <div class="entry-subnav-inner">
        ${group(L.lang,  L.langItems)}
        ${group(L.skill, L.skillItems)}
        ${group(L.level, levelItems)}
        ${group(L.unit,  UNITS)}
      </div>
    `;
    const nav = document.querySelector('nav.navbar');
    if (nav && nav.parentNode) {
      nav.parentNode.insertBefore(subnav, nav.nextSibling);
    } else {
      document.body.insertBefore(subnav, document.body.firstChild);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
