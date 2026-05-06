/* ============================================================
   #ressources Übersicht: Filter-Chips + vis-network Label-Graph
   + click-to-expand mit "Weiterführende Ressourcen".
   ============================================================ */
(function () {
  const root = document.getElementById('overview-root');
  if (!root) return;

  const dataUrl = root.dataset.json;
  if (!dataUrl) return;

  fetch(dataUrl).then(r => r.json()).then(init).catch(err => {
    root.innerHTML = '<p>Fehler beim Laden der Daten: ' + err + '</p>';
  });

  // ---------------------------------------------------------
  function init(data) {
    const ui = data.ui;
    const resourcesById = {};
    data.resources.forEach(r => { resourcesById[r.id] = r; });

    // ---- Layout-Skeleton --------------------------------
    root.innerHTML = `
      <section class="ov-section ov-graph-section">
        <h2>${escapeHtml(ui.graph_heading)}</h2>
        <p class="ov-hint">${escapeHtml(ui.graph_hint)}</p>
        <div id="ov-graph"></div>
      </section>

      <section class="ov-section ov-filter-section">
        <div class="ov-filter-header">
          <h2>${escapeHtml(ui.filter_heading)}</h2>
          <button class="ov-clear" type="button">${escapeHtml(ui.filter_clear)}</button>
        </div>
        <div id="ov-chips"></div>
      </section>

      <section class="ov-section ov-results-section">
        <h2>${escapeHtml(ui.results_heading)} <span class="ov-count" id="ov-count"></span></h2>
        <div id="ov-list"></div>
      </section>
    `;

    const chipsEl = document.getElementById('ov-chips');
    const listEl = document.getElementById('ov-list');
    const countEl = document.getElementById('ov-count');
    const clearBtn = root.querySelector('.ov-clear');

    const active = new Set();

    // ---- Chips nach Kategorie ---------------------------
    const order = ['lang', 'lic', 'cefr', 'skill', 'unit'];
    const catLabel = {
      lang: ui.category_lang,
      lic: ui.category_lic,
      cefr: ui.category_cefr,
      skill: ui.category_skill,
      unit: ui.category_unit,
    };
    order.forEach(cat => {
      const inCat = data.labels.filter(l => l.category === cat);
      if (!inCat.length) return;
      const group = document.createElement('div');
      group.className = 'ov-chip-group';
      group.innerHTML = `<h3>${escapeHtml(catLabel[cat] || cat)}</h3>`;
      const wrap = document.createElement('div');
      wrap.className = 'ov-chips';
      inCat.forEach(l => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'ov-chip cat-' + l.category;
        chip.dataset.id = l.id;
        chip.innerHTML =
          `<span class="ov-chip-label">${escapeHtml(l.label)}</span>` +
          `<span class="ov-chip-count">${l.count}</span>`;
        chip.addEventListener('click', () => toggleChip(l.id));
        wrap.appendChild(chip);
      });
      group.appendChild(wrap);
      chipsEl.appendChild(group);
    });

    clearBtn.addEventListener('click', () => {
      active.clear();
      syncChips();
      render();
    });

    function toggleChip(id) {
      if (active.has(id)) active.delete(id); else active.add(id);
      syncChips();
      render();
    }

    function syncChips() {
      chipsEl.querySelectorAll('.ov-chip').forEach(el => {
        el.classList.toggle('active', active.has(el.dataset.id));
      });
    }

    // ---- vis-network Graph ------------------------------
    const catColor = {
      lang:  { bg: '#6c757d', fg: '#ffffff' },
      lic:   { bg: '#5c7c9a', fg: '#ffffff' },
      cefr:  { bg: '#1565c0', fg: '#ffffff' },
      skill: { bg: '#1a73e8', fg: '#ffffff' },
      unit:  { bg: '#6a1b9a', fg: '#ffffff' },
    };
    const nodes = new vis.DataSet(data.labels.map(l => ({
      id: l.id,
      label: l.label,
      value: l.count,
      group: l.category,
      title: `${catLabel[l.category] || l.category}: ${l.label} (${l.count})`,
      color: {
        background: catColor[l.category]?.bg || '#888',
        border: catColor[l.category]?.bg || '#888',
        highlight: { background: '#ffd54f', border: '#e6a817' },
      },
      font: { color: catColor[l.category]?.fg || '#ffffff', size: 14 },
    })));
    const edges = new vis.DataSet(data.edges.map(e => ({
      from: e.from, to: e.to, value: e.weight,
      color: { color: 'rgba(120,120,120,0.35)', highlight: '#e6a817' },
    })));
    const network = new vis.Network(
      document.getElementById('ov-graph'),
      { nodes, edges },
      {
        nodes: { shape: 'dot', scaling: { min: 8, max: 32 }, borderWidth: 1 },
        edges: { smooth: { type: 'continuous' }, scaling: { min: 0.5, max: 4 } },
        physics: {
          stabilization: { iterations: 200 },
          barnesHut: { gravitationalConstant: -2500, springLength: 120 },
        },
        interaction: { hover: true, tooltipDelay: 150 },
      }
    );
    network.on('click', params => {
      if (params.nodes.length) toggleChip(params.nodes[0]);
    });

    // ---- Render-Liste -----------------------------------
    function render() {
      const filtered = data.resources.filter(r => {
        if (!active.size) return true;
        for (const tag of active) if (!r.tags.includes(tag)) return false;
        return true;
      });
      countEl.textContent = ui.results_count.replace('{n}', filtered.length);
      if (!filtered.length) {
        listEl.innerHTML = `<p class="no-resources">${escapeHtml(ui.no_results)}</p>`;
        return;
      }
      listEl.innerHTML = filtered.map(renderCard).join('');
      listEl.querySelectorAll('.ov-card-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
          const card = btn.closest('.ov-card');
          card.classList.toggle('expanded');
          btn.textContent = card.classList.contains('expanded')
            ? ui.details_close
            : ui.details_open;
        });
      });
      listEl.querySelectorAll('.ov-related-link').forEach(a => {
        a.addEventListener('click', e => {
          e.preventDefault();
          const targetId = a.dataset.target;
          const target = document.getElementById('card-' + targetId);
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            target.classList.add('expanded');
            const tBtn = target.querySelector('.ov-card-toggle');
            if (tBtn) tBtn.textContent = ui.details_close;
          }
        });
      });
      listEl.querySelectorAll('.ov-back-graph').forEach(a => {
        a.addEventListener('click', e => {
          e.preventDefault();
          document.getElementById('ov-graph')
            .scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
    }

    function renderCard(r) {
      const badges = [
        `<span class="type-badge type-${r.license_type.toLowerCase()}">${escapeHtml(r.license_type)}</span>`,
        `<span class="lang-badge">${escapeHtml(r.language)}</span>`,
        ...r.cefr_levels.map(l => `<span class="cefr-badge cefr-${l.toLowerCase()}">${escapeHtml(l)}</span>`),
        ...r.skills_labels.map(l => `<span class="skill-badge">${escapeHtml(l)}</span>`),
      ].join('');
      const relIds = (data.related[r.id] || []).slice(0, 3);
      const related = relIds.length
        ? `<div class="ov-related">
             <h4>${escapeHtml(ui.related_heading)}</h4>
             <ul>${relIds.map(id => {
               const o = resourcesById[id];
               return o ? `<li><a class="ov-related-link" href="#card-${o.id}" data-target="${o.id}">${escapeHtml(o.title)}</a> <span class="ov-rel-pub">— ${escapeHtml(o.publisher)}</span></li>` : '';
             }).join('')}</ul>
             <p class="ov-back"><a href="#ov-graph" class="ov-back-graph">↑ ${escapeHtml(ui.related_back)}</a></p>
           </div>`
        : '';
      const notes = r.curator_notes
        ? `<p class="resource-notes"><em>${escapeHtml(r.curator_notes)}</em></p>` : '';
      return `
<article class="ov-card resource-card" id="card-${r.id}">
  <h3>${escapeHtml(r.title)}</h3>
  <p class="resource-publisher">${escapeHtml(ui.publisher_label)}: ${escapeHtml(r.publisher)} · <a href="${escapeHtml(r.url)}">${escapeHtml(ui.open_resource)}</a></p>
  <div class="resource-badges">${badges}</div>
  <button type="button" class="ov-card-toggle">${escapeHtml(ui.details_open)}</button>
  <div class="ov-card-body">
    <p class="resource-description">${escapeHtml(r.description)}</p>
    ${notes}
    <p class="resource-checked">${escapeHtml(ui.last_check)}: ${escapeHtml(r.last_checked)}</p>
    ${related}
  </div>
</article>`;
    }

    render();
  }

  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, c => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    ));
  }
})();
