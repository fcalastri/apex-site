// APEX — interactions (vanilla, no framework)
(function () {
  var doc = document;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- language: remember choice + auto-detect Italian on first home visit ---------- */
  try {
    var path = location.pathname;
    var onIT = /(^|\/)it\//.test(path);
    var isHome = /(^|\/)(index\.html)?$/.test(path) || /\/it\/(index\.html)?$/.test(path);
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

  /* ---------- helpers ---------- */
  function setText(key, val) {
    doc.querySelectorAll('[data-v="' + key + '"]').forEach(function (el) { el.textContent = val; });
  }
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var jit = function (v, a) { return v + (Math.random() - 0.5) * a; };

  /* ---------- live HUD ---------- */
  var live = { speed: 104, lean: 42, brake: 61, g: 1.2 };
  function paintLive() {
    setText('speed', String(live.speed));
    setText('lean', live.lean + '\u00B0');
    setText('brakePct', live.brake + '%');
    setText('g', live.g.toFixed(2));
    var bar = doc.querySelector('[data-bar="brake"]');
    if (bar) bar.style.width = live.brake + '%';
  }
  if (doc.querySelector('[data-v="speed"]')) {
    paintLive();
    if (!reduce) setInterval(function () {
      live.speed = Math.round(clamp(jit(live.speed, 12), 42, 162));
      live.lean = Math.round(clamp(jit(live.lean, 8), 5, 55));
      live.brake = Math.round(clamp(jit(live.brake, 24), 0, 100));
      live.g = +clamp(jit(live.g, 0.32), 0.1, 1.7).toFixed(2);
      paintLive();
    }, 260);
  }

  /* ---------- ride score + rings ---------- */
  function paintScore(score) {
    setText('score', String(score));
    var f = score / 100;
    doc.querySelectorAll('circle[style*="stroke-dasharray:201px"]').forEach(function (c) {
      c.style.strokeDashoffset = (201 * (1 - f)).toFixed(1) + 'px';
    });
    doc.querySelectorAll('circle[style*="stroke-dasharray:402px"]').forEach(function (c) {
      c.style.strokeDashoffset = (402 * (1 - f)).toFixed(1) + 'px';
    });
  }
  function countTo(targets, dur, onUpdate, after) {
    var start = performance.now(), from = {};
    Object.keys(targets).forEach(function (k) { from[k] = 0; });
    var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
    (function step(now) {
      var t = Math.min(1, (now - start) / dur), e = ease(t), upd = {};
      Object.keys(targets).forEach(function (k) { upd[k] = Math.round(from[k] + (targets[k] - from[k]) * e); });
      onUpdate(upd);
      if (t < 1) requestAnimationFrame(step); else if (after) after();
    })(start);
  }
  if (doc.querySelector('[data-v="score"]')) {
    if (reduce) { paintScore(87); }
    else {
      countTo({ score: 87 }, 1500, function (u) { paintScore(u.score); }, function () {
        setInterval(function () { paintScore(Math.max(83, Math.min(91, 87 + Math.round((Math.random() - 0.5) * 4)))); }, 1600);
      });
    }
  }

  /* ---------- trust stats count-up on scroll ---------- */
  var trust = doc.querySelector('[data-countup]');
  if (trust && doc.querySelector('[data-v="riders"]')) {
    var run = function () {
      if (reduce) { setText('riders', '4,200+'); setText('corners', '1.48M'); setText('recommend', '96%'); return; }
      countTo({ riders: 4200, corners: 1480000, recommend: 96 }, 1700, function (u) {
        setText('riders', u.riders.toLocaleString('en-US') + '+');
        setText('corners', (u.corners / 1e6).toFixed(2) + 'M');
        setText('recommend', u.recommend + '%');
      });
    };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { run(); io.disconnect(); } });
      }, { threshold: 0.3 });
      io.observe(trust);
    } else run();
  }

  /* ---------- reveal on scroll (progressive: visible by default) ---------- */
  if (!reduce && 'IntersectionObserver' in window) {
    var rio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.style.opacity = '1'; e.target.style.transform = 'none'; rio.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    var pending = [];
    doc.querySelectorAll('[data-reveal]').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.92 && r.bottom > 0) return; // already visible, leave it
      el.style.opacity = '0';
      el.style.transform = 'translateY(22px)';
      el.style.transition = 'opacity .55s cubic-bezier(.23,1,.32,1), transform .55s cubic-bezier(.23,1,.32,1)';
      var d = el.getAttribute('data-delay');
      if (d) el.style.transitionDelay = d + 'ms';
      rio.observe(el);
      pending.push(el);
    });
    // Safety net: content must never stay invisible if the observer misses a
    // fast anchor-jump, an automated full-page screenshot, or a slow device.
    if (pending.length) {
      setTimeout(function () {
        pending.forEach(function (el) {
          if (el.style.opacity === '0') { el.style.opacity = '1'; el.style.transform = 'none'; }
        });
      }, 1800);
    }
  }

  /* ---------- magnetic buttons ---------- */
  if (!reduce) doc.querySelectorAll('[data-magnetic]').forEach(function (el) {
    el.addEventListener('pointermove', function (ev) {
      var r = el.getBoundingClientRect();
      el.style.transform = 'translate(' + ((ev.clientX - r.left - r.width / 2) * 0.3) + 'px,' + ((ev.clientY - r.top - r.height / 2) * 0.5) + 'px)';
    });
    el.addEventListener('pointerleave', function () { el.style.transform = 'translate(0,0)'; });
  });

  /* ---------- scroll progress ---------- */
  var bar = doc.querySelector('[data-progress]');
  if (bar) {
    var onScroll = function () {
      var h = doc.documentElement, m = h.scrollHeight - h.clientHeight;
      bar.style.width = (m > 0 ? (h.scrollTop / m * 100) : 0) + '%';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- billing toggle ---------- */
  var prices = {
    monthly: { rider: ['\u20AC12.99', 'per month'], pro: ['\u20AC24.99', 'per month'], safe: ['\u20AC6.49', 'per month'] },
    annual:  { rider: ['\u20AC7.50', 'per month \u00B7 billed \u20AC89.99/yr'], pro: ['\u20AC15.00', 'per month \u00B7 billed \u20AC179.99/yr'], safe: ['\u20AC4.17', 'per month \u00B7 billed \u20AC49.99/yr'] }
  };
  // localized notes if page is Italian
  var isIt = doc.documentElement.lang === 'it';
  if (isIt) {
    prices.monthly.rider[1] = prices.monthly.pro[1] = prices.monthly.safe[1] = 'al mese';
    prices.annual.rider[1] = 'al mese \u00B7 fatturato \u20AC89.99/anno';
    prices.annual.pro[1] = 'al mese \u00B7 fatturato \u20AC179.99/anno';
    prices.annual.safe[1] = 'al mese \u00B7 fatturato \u20AC49.99/anno';
  }
  var billBtns = doc.querySelectorAll('[data-bill]');
  if (billBtns.length) {
    var applyBill = function (mode) {
      billBtns.forEach(function (btn) {
        var on = btn.getAttribute('data-bill') === mode;
        btn.style.background = on ? '#B8FF2C' : 'transparent';
        btn.style.color = on ? 'var(--asphalt)' : 'var(--muted)';
      });
      ['rider', 'pro', 'safe'].forEach(function (k) {
        var p = prices[mode][k];
        doc.querySelectorAll('[data-v="' + k + 'Price"]').forEach(function (el) { el.textContent = p[0]; });
        doc.querySelectorAll('[data-v="' + k + 'Note"]').forEach(function (el) { el.textContent = p[1]; });
      });
    };
    billBtns.forEach(function (btn) {
      btn.addEventListener('click', function () { applyBill(btn.getAttribute('data-bill')); });
    });
    applyBill('monthly');
  }

  /* ---------- beta form: success state after real POST (?sent=1) ---------- */
  var form = doc.getElementById('beta-form');
  if (form && /[?&]sent=1/.test(location.search)) {
    form.style.display = 'none';
    var ok = doc.getElementById('form-ok');
    if (ok) { ok.style.display = 'block'; ok.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
  }
})();
