// APEX — interactions (vanilla, no framework)
(function () {
  var doc = document;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* language: remember choice + auto-detect Italian on first home visit */
  try {
    var path = location.pathname;
    var onIT = /^\/it(\/|$)/.test(path);
    var isHome = path === '/' || path === '/index.html' || path === '/it/' || path === '/it/index.html';
    var saved = localStorage.getItem('apex_lang');
    if (saved) {
      if (isHome) {
        if (saved === 'it' && !onIT) location.replace('/it/');
        if (saved === 'en' && onIT) location.replace('/');
      }
    } else if (isHome && !onIT) {
      if ((navigator.language || '').toLowerCase().indexOf('it') === 0) location.replace('/it/');
    }
    doc.querySelectorAll('[data-lang]').forEach(function (a) {
      a.addEventListener('click', function () { localStorage.setItem('apex_lang', a.getAttribute('data-lang')); });
    });
  } catch (e) {}

  /* mobile nav */
  var header = doc.querySelector('.site-header');
  var toggle = doc.querySelector('.nav-toggle');
  if (toggle && header) toggle.addEventListener('click', function () {
    var open = header.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* reveal on scroll */
  var els = doc.querySelectorAll('[data-reveal]');
  if (reduce || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* tabs (product page) */
  doc.querySelectorAll('[data-tabs]').forEach(function (root) {
    var btns = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    function show(id) {
      btns.forEach(function (b) { b.setAttribute('aria-selected', b.getAttribute('aria-controls') === id ? 'true' : 'false'); });
      panels.forEach(function (p) { p.hidden = p.id !== id; });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.getAttribute('aria-controls')); history.replaceState(null, '', '#' + b.getAttribute('aria-controls')); }); });
    var h = location.hash.replace('#', '');
    if (h && root.querySelector('#' + CSS.escape(h) + '[role="tabpanel"]')) show(h);
  });

  /* pack selection → CTA link carries the chosen pack */
  var packs = doc.querySelectorAll('input[name="pack-choice"]');
  var buyBtn = doc.querySelector('[data-buy]');
  if (packs.length && buyBtn) {
    var base = buyBtn.getAttribute('href').split('?')[0];
    packs.forEach(function (r) { r.addEventListener('change', function () {
      buyBtn.setAttribute('href', base + '?pack=' + encodeURIComponent(r.value));
      var priceEl = doc.querySelector('[data-price]');
      if (priceEl && r.dataset.price) priceEl.textContent = r.dataset.price;
    }); });
  }

  /* guides filters */
  var filterRoot = doc.querySelector('[data-filters]');
  if (filterRoot) {
    var state = { level: 'all', topic: 'all' };
    var cards = doc.querySelectorAll('[data-guide]');
    function apply() {
      cards.forEach(function (c) {
        var okL = state.level === 'all' || (c.dataset.levels || '').split(' ').indexOf(state.level) > -1;
        var okT = state.topic === 'all' || c.dataset.topic === state.topic;
        c.hidden = !(okL && okT);
      });
    }
    filterRoot.querySelectorAll('button[data-f]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.dataset.f, v = b.dataset.v;
        state[k] = v;
        filterRoot.querySelectorAll('button[data-f="' + k + '"]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        apply();
      });
    });
  }

  /* early access form: prefill pack from ?pack=, AJAX submit with graceful fallback */
  var form = doc.getElementById('early-access-form');
  if (form) {
    if (/[?&]sent=1/.test(location.search)) { form.hidden = true; var okEl = doc.getElementById('early-access-ok'); if (okEl) okEl.classList.add('is-on'); }
    try {
      var q = new URLSearchParams(location.search).get('pack');
      var sel = form.querySelector('select[name="pack"]');
      if (q && sel) { Array.prototype.forEach.call(sel.options, function (o) { if (o.value.toLowerCase().indexOf(q.toLowerCase()) === 0) sel.value = o.value; }); }
    } catch (e) {}
    form.addEventListener('submit', function (ev) {
      if (!window.fetch) return;
      ev.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), redirect: 'follow' })
        .then(function (r) { if (!r.ok) return r.text().then(function (t) { throw new Error(t || r.status); }); })
        .then(function () {
          form.hidden = true;
          var ok = doc.getElementById('early-access-ok');
          if (ok) { ok.classList.add('is-on'); ok.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' }); }
        })
        .catch(function (err) {
          btn.disabled = false;
          var e = doc.getElementById('early-access-err');
          if (e) { e.textContent = String(err.message || err); e.hidden = false; }
        });
    });
  }

  /* footer newsletter: reuse the early-access endpoint with pack=newsletter */
  var nl = doc.getElementById('newsletter-form');
  if (nl) nl.addEventListener('submit', function (ev) {
    if (!window.fetch) return;
    ev.preventDefault();
    var fd = new FormData(nl);
    fd.set('name', 'Newsletter'); fd.set('pack', 'newsletter'); fd.set('consent', 'on');
    fetch('/api/early-access', { method: 'POST', body: fd }).then(function () {
      nl.innerHTML = '<p>' + nl.dataset.ok + '</p>';
    });
  });
})();
