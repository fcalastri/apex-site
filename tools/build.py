#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX site builder — renders the whole bilingual site from tools/content/*.py
into the repository root (which Cloudflare Pages serves as-is).

    python3 tools/build.py            # build
    python3 tools/build.py --check    # build + link check

No dependencies beyond the Python 3 standard library.
"""
import os, re, sys, json, html, shutil, importlib.util
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
SRC = os.path.join(ROOT, "src")
DOMAIN = "https://apex-rider.com"
TODAY = date.today().isoformat()

def load(name):
    p = os.path.join(TOOLS, "content", name + ".py")
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

EN, IT = load("en"), load("it")
ARTICLES = json.load(open(os.path.join(TOOLS, "content", "articles.json"), encoding="utf-8"))
ARTICLE_ORDER = ["how-to-know-if-you-ride-well", "how-to-improve-cornering", "riding-coach-cost", "motorcycle-telemetry-road", "first-track-day-guide"]

e = html.escape

# ---------------------------------------------------------------- helpers ---
def guide_url(C, aid):
    return C.ROUTES["guides"] + C.GUIDE_SLUGS[aid]

def alt_url(C, page_id, aid=None):
    O = IT if C is EN else EN
    return guide_url(O, aid) if aid else O.ROUTES[page_id]

def out_path(url):
    if url.endswith("/"): return os.path.join(ROOT, url.strip("/"), "index.html") if url != "/" else os.path.join(ROOT, "index.html")
    return os.path.join(ROOT, url.strip("/") + ".html")

def read_time(blocks):
    words = sum(len(re.sub(r"<[^>]+>", "", b[1]).split()) for b in blocks)
    return max(3, round(words / 200))

def icon(name):
    I = {
        "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
        "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8 12 3 3 8v8l9 5 9-5V8z"/><path d="m3 8 9 5 9-5M12 13v8"/></svg>',
        "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="3"/><path d="M3 10h18M8 2v4M16 2v4"/></svg>',
        "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/></svg>',
        "sensor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="2.5"/><path d="M7.5 7.5a6.4 6.4 0 0 0 0 9M16.5 7.5a6.4 6.4 0 0 1 0 9M4.5 4.5a10.6 10.6 0 0 0 0 15M19.5 4.5a10.6 10.6 0 0 1 0 15"/></svg>',
        "ai": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18 9 8l3 6 3-4 5 8"/><path d="M3 21h18"/></svg>',
        "road": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c4-6 4-10 8-10s4 4 8 10"/><path d="M12 4v3M12 11v3"/></svg>',
        "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 7 9 6 9-6"/></svg>',
    }
    return I[name]

def road_svg(seed=0, light=False):
    """Decorative road ribbon used inside media placeholders."""
    c = "#B8FF2C"
    paths = ["M-20 300 C 120 260, 160 120, 300 130 S 480 40, 620 90", "M-20 90 C 140 120, 180 260, 320 230 S 520 300, 620 200", "M-20 200 C 100 60, 260 60, 340 180 S 540 120, 620 260"][seed % 3]
    stroke = "rgba(11,15,20,.18)" if light else "rgba(245,247,250,.16)"
    return f'<svg class="media-road" viewBox="0 0 600 320" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><path d="{paths}" fill="none" stroke="{stroke}" stroke-width="42" stroke-linecap="round"/><path d="{paths}" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="14 18" opacity=".8"/></svg>'

def media(label, cls="", seed=0):
    light = "media-light" in cls
    return f'<div class="media {cls}" role="img" aria-label="{e(label)}">{road_svg(seed, light)}<span class="media-label">{e(label)}</span></div>'

def review_card(C):
    R = C.REVIEW_CARD
    metrics = "".join(f'<div class="metric"><div class="k">{e(k)}</div><div class="v">{v}<small>/100</small></div><div class="bar"><i style="--w:{v}%"></i></div></div>' for k, v in R["metrics"])
    flags = "".join(f'<div class="flag {kind}"><b>{e(k)}</b><span>{e(t)}</span></div>' for kind, k, t in R["flags"])
    svg = '''<svg viewBox="0 0 520 260" aria-hidden="true">
  <defs><pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M26 0H0v26" fill="none" stroke="#1A222D" stroke-width="1"/></pattern></defs>
  <rect width="520" height="260" fill="url(#grid)"/>
  <path d="M30 230 C 120 230, 180 120, 250 80 S 400 40, 490 30" fill="none" stroke="#2C3748" stroke-width="34" stroke-linecap="round"/>
  <path d="M30 230 C 120 230, 180 120, 250 80 S 400 40, 490 30" fill="none" stroke="#8A95A5" stroke-width="2" stroke-dasharray="6 8" class="draw"/>
  <path d="M30 238 C 110 236, 170 150, 236 96 S 396 52, 490 40" fill="none" stroke="#B8FF2C" stroke-width="3" stroke-linecap="round" class="draw d2"/>
  <circle cx="118" cy="232" r="7" fill="#0B0F14" stroke="#FFB21A" stroke-width="3"/><text x="130" y="222" fill="#FFB21A" font-family="IBM Plex Mono,monospace" font-size="11">BRAKE</text>
  <circle cx="236" cy="96" r="7" fill="#0B0F14" stroke="#FFB21A" stroke-width="3"/><text x="248" y="88" fill="#FFB21A" font-family="IBM Plex Mono,monospace" font-size="11">APEX</text>
  <circle cx="330" cy="62" r="7" fill="#0B0F14" stroke="#31E981" stroke-width="3"/><text x="342" y="56" fill="#31E981" font-family="IBM Plex Mono,monospace" font-size="11">THROTTLE</text>
</svg>'''
    return f'''<div class="review" aria-label="Example ride review">
  <div class="review-head"><span>{e(R["head"])}</span><span class="pill">{e(R["pill"])}</span></div>
  <div class="review-map">{svg}</div>
  <div class="review-legend"><span><i style="background:#B8FF2C"></i>{e(R["legend_you"])}</span><span><i style="background:#8A95A5"></i>{e(R["legend_ideal"])}</span></div>
  <div class="review-metrics">{metrics}</div>
  <div class="review-flags">{flags}</div>
  <div class="review-next"><div class="k">{e(R["next_k"])}</div><p>{e(R["next"])}</p></div>
</div>'''

def faq_list(items):
    return '<div class="faq">' + "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items) + "</div>"

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def cta_band(C):
    B = C.CTA_BAND
    return f'''<section class="section-tight"><div class="wrap"><div class="cta-band" data-reveal>
  <div><span class="eyebrow">{e(B["eyebrow"])}</span><h2>{e(B["h"])}</h2><p>{e(B["p"])}</p></div>
  <div class="btn-row"><a class="btn btn-lime btn-lg" href="{C.ROUTES["early"]}">{e(B["btn"])} <span class="arr">→</span></a><a class="btn btn-ghost" href="{C.ROUTES["product"]}">{e(B["btn2"])}</a></div>
</div></div></section>'''

def trust_row(C):
    ic = ["box", "cal", "shield"]
    return '<div class="trust">' + "".join(f'<div>{icon(ic[i])}<div><b>{e(t)}</b><span>{e(s)}</span></div></div>' for i, (t, s) in enumerate(C.TRUST)) + "</div>"

def testimonials(C, with_head=True):
    if C.TESTIMONIALS:
        figs = "".join(f'<figure><blockquote>{e(t["q"])}</blockquote><figcaption><span class="av">{e(t["name"][:1])}</span><div class="who"><b>{e(t["name"])}</b><span>{e(t["role"])}</span></div></figcaption></figure>' for t in C.TESTIMONIALS)
        body = f'<div class="wall">{figs}</div>'
    else:
        E = C.EMPTY_TESTIMONIALS
        body = f'<div class="empty-band"><b>{e(E["b"])}</b><p>{e(E["p"])}</p><p style="margin-top:18px"><a class="btn btn-ghost btn-sm" href="{C.ROUTES["how"]}#review">{e(E["btn"])}</a></p></div>'
    head = f'<div class="center" data-reveal><span class="eyebrow">{e(C.HOME["testimonials_eyebrow"])}</span><h2>{e(C.HOME["testimonials_h"])}</h2></div><div class="stack-2"></div>' if with_head else ""
    return head + body

def press_strip(C):
    if not C.PRESS: return ""
    items = "".join(f'<figure>{e(q)}<figcaption>{e(s)}</figcaption></figure>' for q, s in C.PRESS)
    return f'<div class="quote-strip"><div class="wrap" style="max-width:none;padding:0"><div class="quote-track">{items}{items}</div></div></div>'

def results_block(C):
    R = C.RESULTS
    if not R: return ""
    nums = "".join(f'<div class="number"><div class="v">{e(v)}</div><div class="l">{e(l)}</div></div>' for v, l in R["items"])
    return f'<section class="section section-dark"><div class="wrap"><div data-reveal><span class="eyebrow">{e(R.get("eyebrow","Results"))}</span><h2>{e(R["h"])}</h2><p class="lead muted sub">{e(R["intro"])}</p></div><div class="numbers stack-2">{nums}</div></div></section>'

# ------------------------------------------------------------------ layout ---
def layout(C, *, page_id, title, description, body, alt, canonical, ld=None, aid=None, og_type="website"):
    O = IT if C is EN else EN
    en_url = canonical if C is EN else alt
    it_url = alt if C is EN else canonical
    nav = "".join(f'<a href="{C.ROUTES[pid]}"{" aria-current=\"page\"" if pid == page_id else ""}>{e(lbl)}</a>' for pid, lbl in C.NAV)
    foot_cols = "".join(f'<div><h4>{e(h)}</h4><ul>' + "".join(f'<li><a href="{C.ROUTES[pid]}">{e(l)}</a></li>' for pid, l in links) + "</ul></div>" for h, links in C.FOOTER.values())
    ld_graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": DOMAIN + "/#org", "name": "APEX", "url": DOMAIN + "/", "logo": DOMAIN + "/assets/apex-og.png", "email": C.SITE["email"], "address": {"@type": "PostalAddress", "addressLocality": "Milano", "addressCountry": "IT"}},
        {"@type": "WebSite", "@id": DOMAIN + "/#site", "url": DOMAIN + "/", "name": "APEX", "inLanguage": C.LANG, "publisher": {"@id": DOMAIN + "/#org"}},
        {"@type": "WebPage", "@id": DOMAIN + canonical, "url": DOMAIN + canonical, "name": title, "description": description, "inLanguage": C.LANG, "isPartOf": {"@id": DOMAIN + "/#site"}},
    ] + (ld or [])}
    og_img = "/assets/apex-og-it.png" if C is IT else "/assets/apex-og.png"
    NL = C.NEWSLETTER
    return f'''<!doctype html>
<html lang="{C.LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{en_url}">
<link rel="alternate" hreflang="it" href="{DOMAIN}{it_url}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{en_url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="APEX"><meta property="og:locale" content="{"it_IT" if C is IT else "en_GB"}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{DOMAIN}{canonical}"><meta property="og:image" content="{DOMAIN}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0F14">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/apex.css">
<script type="application/ld+json">{json.dumps(ld_graph, ensure_ascii=False)}</script>
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{C.ROUTES["home"]}" aria-label="APEX home"><span class="brand-mark"><svg viewBox="0 0 16 16" fill="none" stroke="#B8FF2C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13 8 3l6 10M5 10h6"/></svg></span>APEX</a>
  <nav class="site-nav" aria-label="Main">{nav}</nav>
  <div class="header-actions">
    <div class="lang-switch"><a href="{en_url}" data-lang="en"{' class="is-active"' if C is EN else ""} hreflang="en">EN</a><a href="{it_url}" data-lang="it"{' class="is-active"' if C is IT else ""} hreflang="it">IT</a></div>
    <a class="btn btn-primary btn-sm" href="{C.ROUTES[C.NAV_CTA[0]]}">{e(C.NAV_CTA[1])}</a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div class="foot-brand"><a class="brand" href="{C.ROUTES["home"]}"><span class="brand-mark"><svg viewBox="0 0 16 16" fill="none" stroke="#B8FF2C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13 8 3l6 10M5 10h6"/></svg></span>APEX</a>
      <p>{e(C.FOOT_BLURB)}</p>
      <form class="newsletter" id="newsletter-form" data-ok="{e(NL["ok"])}" aria-label="{e(NL["label"])}"><input type="hidden" name="lang" value="{C.LANG}"><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off"><input type="email" name="email" required placeholder="{e(NL["placeholder"])}" aria-label="{e(NL["placeholder"])}"><button type="submit">{e(NL["button"])}</button></form>
    </div>
    {foot_cols}
  </div>
  <div class="foot-bottom"><span>{e(C.COPYRIGHT)} · {e(C.SITE["company"])}</span><span class="social"><a href="mailto:{C.SITE["email"]}">{C.SITE["email"]}</a><a href="#main">{e(C.BACK_TO_TOP)} ↑</a></span></div>
</div></footer>
<script src="/apex.js" defer></script>
</body>
</html>'''

# ------------------------------------------------------------------- pages ---
def page_home(C):
    H = C.HOME; h = H["hero"]; S = H["sports"]; M = H["meet"]; CH = H["changes"]; R = H["riders"]
    rows = "".join(f'<div class="sports-row{"" if ok else " is-bad"}"><b class="who">{e(w)}</b><span class="what">{e(t)}</span><span class="{"tick" if ok else "cross"}">{"✓" if ok else "✕"}</span></div>' for w, t, ok in S["rows"])
    rows += f'<div class="sports-row is-apex"><b class="who">{e(S["apex"][0])}</b><span class="what">{e(S["apex"][1])}</span><span class="tick">✓</span></div>'
    steps = "".join(f'<div class="step" data-reveal><div class="step-media">{media(t, "square", i)}</div><div class="step-body"><div class="step-k">STEP {i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for i, (t, d) in enumerate(M["steps"]))
    changes = "".join(f'<div class="skill" data-reveal><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in CH["items"])
    riders = "".join(f'<div class="rider" data-reveal><span class="mono">{e(a)}</span><h3>{e(t)}</h3><p>{e(d)}</p><a class="link" href="{C.ROUTES["product"]}">{e(C.NAV[3][1])} →</a></div>' for t, a, d in R["items"])
    body = f'''
<section class="hero"><div class="wrap"><div class="hero-grid">
  <div><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p>
    <div class="btn-row"><a class="btn btn-primary btn-lg" href="{C.ROUTES["early"]}">{e(h["btn"])} <span class="arr">→</span></a><a class="btn btn-ghost btn-lg" href="{C.ROUTES["how"]}">{e(h["btn2"])}</a></div>
    <p class="hero-note">{e(h["note"])}</p></div>
  <div>{review_card(C)}</div>
</div></div></section>
{press_strip(C)}
<section class="section section-dark"><div class="wrap"><div class="split">
  <div data-reveal><span class="eyebrow">{e(S["eyebrow"])}</span><h2>{e(S["h"])}</h2></div>
  <div class="sports" data-reveal>{rows}</div>
</div></div></section>
<section class="section"><div class="wrap">
  <div class="center" data-reveal><span class="eyebrow">{e(M["eyebrow"])}</span><h2>{e(M["h"])}</h2></div>
  <div class="steps stack-2">{steps}</div>
  <div class="center stack-2"><a class="btn btn-ghost" href="{C.ROUTES["how"]}">{e(M["btn"])} <span class="arr">→</span></a></div>
</div></section>
{results_block(C)}
<section class="section section-alt"><div class="wrap">
  <div data-reveal><span class="eyebrow">{e(CH["eyebrow"])}</span><h2>{e(CH["h"])}</h2></div>
  <div class="skills stack-2" style="grid-template-columns:repeat(3,1fr)">{changes}</div>
</div></section>
<section class="section"><div class="wrap">
  <div data-reveal><span class="eyebrow">{e(R["eyebrow"])}</span><h2>{e(R["h"])}</h2></div>
  <div class="riders stack-2">{riders}</div>
</div></section>
<section class="section section-alt"><div class="wrap">{testimonials(C)}</div></section>
<section class="section-tight"><div class="wrap">{trust_row(C)}</div></section>
{cta_band(C)}'''
    return dict(page_id="home", title=H["title"], description=H["description"], body=body)

def page_how(C):
    H = C.HOW; h = H["hero"]
    steps = []
    for i, s in enumerate(H["journey"]):
        vis = review_card(C) if s["media"] == "review" else media(s["media"], "", i)
        li = "".join(f'<li><b>{e(a)}</b> — {e(b)}</li>' for a, b in s["li"])
        text = f'<div class="text" data-reveal><span class="journey-k" aria-hidden="true">{s["k"]}</span><span class="eyebrow">{e(s["eyebrow"])}</span><h2>{e(s["h"])}</h2><p class="lead">{e(s["p"])}</p><ul>{li}</ul></div>'
        steps.append(f'<div class="split{" rev" if i % 2 else ""}" id="{"review" if s["media"]=="review" else "step-"+s["k"]}"><div data-reveal>{vis}</div>{text}</div>')
    SK = H["skills"]
    skills = "".join(f'<div class="skill" data-reveal><div class="g"><i style="--w:{w}%"></i></div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d, w in SK["items"])
    T = H["tech"]; ic = ["sensor", "ai", "road"]
    tech = "".join(f'<div data-reveal><span class="ic">{icon(ic[i])}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(T["items"]))
    N = H["not_"]
    nots = "".join(f'<div class="skill" data-reveal><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in N["items"])
    body = f'''
<section class="hero"><div class="wrap"><div class="center" style="max-width:820px;margin:0 auto"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
<section class="section-tight"><div class="wrap"><div class="journey">{"".join(steps)}</div></div></section>
<section class="section section-alt"><div class="wrap">
  <div data-reveal><span class="eyebrow">{e(SK["eyebrow"])}</span><h2>{e(SK["h"])}</h2><p class="lead sub">{e(SK["p"])}</p></div>
  <div class="skills stack-2">{skills}</div>
</div></section>
<section class="section section-dark"><div class="wrap">
  <div data-reveal><span class="eyebrow">{e(T["eyebrow"])}</span><h2>{e(T["h"])}</h2></div>
  <div class="tech stack-2">{tech}</div>
</div></section>
<section class="section"><div class="wrap">
  <div data-reveal><span class="eyebrow">{e(N["eyebrow"])}</span><h2>{e(N["h"])}</h2></div>
  <div class="skills stack-2" style="grid-template-columns:repeat(3,1fr)">{nots}</div>
</div></section>
<section class="section section-alt"><div class="wrap-narrow"><h2 data-reveal>{e(H["faq_h"])}</h2><div class="stack-2">{faq_list(H["faq"])}</div></div></section>
{cta_band(C)}'''
    return dict(page_id="how", title=H["title"], description=H["description"], body=body, ld=[faq_ld(H["faq"])])

def page_reviews(C):
    R = C.REVIEWS; h = R["hero"]
    com = ""
    if C.COMMUNITY:
        com = f'<section class="section section-dark"><div class="wrap center" data-reveal><h2>{e(C.COMMUNITY["h"])}</h2><p class="lead muted sub">{e(C.COMMUNITY["p"])}</p></div></section>'
    vids = ""
    if R["videos"]:
        vids = f'<section class="section"><div class="wrap"><h2 data-reveal>{e(R["videos_h"])}</h2><div class="cards stack-2">' + "".join(f'<div class="card"><div class="media wide"><iframe title="{e(t)}" src="https://www.youtube-nocookie.com/embed/{y}" loading="lazy" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe></div></div>' for t, y in R["videos"]) + "</div></div></section>"
    body = f'''
<section class="hero"><div class="wrap"><div class="center" style="max-width:820px;margin:0 auto"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
{press_strip(C)}
{results_block(C)}
{com}
<section class="section"><div class="wrap">{testimonials(C, with_head=False)}</div></section>
{vids}
<section class="section section-alt"><div class="wrap-narrow"><h2 data-reveal>{e(R["faq_h"])}</h2><div class="stack-2">{faq_list(R["faq"])}</div></div></section>
<section class="section-tight"><div class="wrap">{trust_row(C)}</div></section>
{cta_band(C)}'''
    return dict(page_id="reviews", title=R["title"], description=R["description"], body=body, ld=[faq_ld(R["faq"])])

def page_product(C):
    P = C.PRODUCT
    packs = "".join(f'<label class="pack{" is-soon" if p["soon"] else ""}"><input type="radio" name="pack-choice" value="{p["id"]}" data-price="{e(p["price"])}"{" checked" if i == 1 else ""}><span><span class="n">{e(p["name"])}<span class="tag">{e(p["tag"])}</span></span><span class="d">{e(p["d"])}</span></span><span class="p">{e(p["price"])}</span></label>' for i, p in enumerate(P["packs"]))
    meta = "".join(f'<div>{icon("check")}<span>{e(m)}</span></div>' for m in P["buy_meta"])
    thumbs = "".join(media(g, "square", i + 1) for i, g in enumerate(P["gallery"][1:]))
    tabs = "".join(f'<button role="tab" id="{tid}-tab" aria-controls="{tid}" aria-selected="{"true" if i == 0 else "false"}">{e(l)}</button>' for i, (tid, l) in enumerate(P["tabs"]))
    O = P["outcomes"]; levels = "".join(f'<div class="level"><h3>{e(t)}</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul></div>" for t, xs in O["items"])
    TR = P["tracking"]; track = "".join(f'<li><b>{e(a)}</b> — {e(b)}</li>' for a, b in TR["items"])
    MO = P["modes"]; modes = "".join(f'<div class="mode"><span class="mono">{e(s)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, s, d in MO["items"])
    CM = P["compare"]
    def cell(v): return '<td class="y">✓</td>' if v == 1 else ('<td class="n">—</td>' if v == 0 else f'<td>{e(v)}</td>')
    cmp_rows = "".join(f'<tr><td>{e(r)}</td>' + "".join(cell(v) for v in vs) + "</tr>" for r, vs in CM["rows"])
    buying = "".join(f'<div class="skill"><span class="mono" style="color:var(--lime-ink)">{i+1} · {e(k)}</span><h3 style="margin-top:10px">{e(t)}</h3><p>{e(d)}</p></div>' for i, (k, t, d) in enumerate(CM["buying"]))
    specs = "".join(f'<tr><th>{e(k)}</th><td>{e(v)}</td></tr>' for k, v in P["specs"])
    product_ld = [{"@type": "Product", "name": "APEX kit", "description": P["p"], "brand": {"@type": "Brand", "name": "APEX"}, "offers": [{"@type": "Offer", "name": p["name"], "price": p["price"].replace("€", "").replace(",", ".").strip(), "priceCurrency": "EUR", "availability": "https://schema.org/PreOrder", "url": DOMAIN + C.ROUTES["product"]} for p in P["packs"]]}]
    body = f'''
<section class="section-tight" style="padding-top:clamp(28px,4vw,56px)"><div class="wrap"><div class="product">
  <div class="gallery">{media(P["gallery"][0], "", 0)}<div class="thumbs">{thumbs}</div></div>
  <div class="buy">
    <span class="eyebrow">{e(P["eyebrow"])}</span><h1>{e(P["h"])}</h1><p class="lead sub">{e(P["p"])}</p>
    <div class="price"><span>{e(P["from_"])}</span><b data-price>{e(P["packs"][1]["price"])}</b><span>{e(P["price_note"])}</span></div>
    <h3 style="margin-top:26px">{e(P["packs_h"])}</h3>
    <div class="packs" role="radiogroup">{packs}</div>
    <a class="btn btn-primary btn-lg" href="{C.ROUTES["early"]}?pack=Rider" data-buy>{e(P["buy_btn"])} <span class="arr">→</span></a>
    <div class="buy-meta">{meta}</div>
  </div>
</div></div></section>
<section class="section-tight"><div class="wrap" data-tabs>
  <div class="tabs" role="tablist">{tabs}</div>
  <div class="tabpanel" role="tabpanel" id="tab-how" aria-labelledby="tab-how-tab">
    <h2 style="font-size:clamp(24px,3vw,36px)">{e(O["h"])}</h2><div class="levels stack-2">{levels}</div>
    <div class="split stack-3"><div><h2 style="font-size:clamp(24px,3vw,36px)">{e(TR["h"])}</h2><ul>{track}</ul></div><div>{review_card(C)}</div></div>
    <h2 class="stack-3" style="font-size:clamp(24px,3vw,36px)">{e(MO["h"])}</h2><div class="modes stack-2">{modes}</div>
  </div>
  <div class="tabpanel" role="tabpanel" id="tab-packs" aria-labelledby="tab-packs-tab" hidden>
    <h2 style="font-size:clamp(24px,3vw,36px)">{e(CM["h"])}</h2>
    <div class="stack-2" style="overflow-x:auto"><table class="cmp"><thead><tr><th></th>{"".join(f"<th>{e(c)}</th>" for c in CM["cols"])}</tr></thead><tbody>{cmp_rows}</tbody></table></div>
    <h2 class="stack-3" style="font-size:clamp(24px,3vw,36px)">{e(CM["buying_h"])}</h2><div class="skills stack-2">{buying}</div>
  </div>
  <div class="tabpanel" role="tabpanel" id="tab-specs" aria-labelledby="tab-specs-tab" hidden>
    <h2 style="font-size:clamp(24px,3vw,36px)">{e(P["tabs"][2][1])}</h2>
    <div class="stack-2"><table class="spec"><tbody>{specs}</tbody></table><p class="muted" style="font-size:14px;margin-top:16px">{e(P["specs_note"])}</p></div>
  </div>
</div></section>
<section class="section section-alt"><div class="wrap">{testimonials(C)}</div></section>
<section class="section-tight"><div class="wrap">{trust_row(C)}</div></section>
{cta_band(C)}'''
    return dict(page_id="product", title=P["title"], description=P["description"], body=body, ld=product_ld, og_type="product")

def page_guides(C):
    G = C.GUIDES; h = G["hero"]
    topic_lbl = dict(G["topics"])
    cards = []
    for i, aid in enumerate(ARTICLE_ORDER):
        A = ARTICLES[aid][C.LANG]; levels, _ = C.GUIDE_META[aid]; topic = ARTICLES[aid]["topic"]
        rt = read_time(A["blocks"])
        cards.append(f'<a class="card{" featured" if i == 0 else ""}" href="{guide_url(C, aid)}" data-guide data-levels="{" ".join(levels)}" data-topic="{topic}">{media(A["title"], "", i)}<div class="card-body"><span class="mono">{e(topic_lbl[topic])}{" · " + e(G["featured"]) if i == 0 else ""}</span><h3>{e(A["title"])}</h3><p>{e(A["description"])}</p><span class="rt">{rt} {e(G["read"])} · {e(G["by"])}</span></div></a>')
    fl = f'<span class="lbl">{e(G["level_lbl"])}</span><button data-f="level" data-v="all" aria-pressed="true">{e(G["all_"])}</button>' + "".join(f'<button data-f="level" data-v="{k}" aria-pressed="false">{e(l)}</button>' for k, l in G["levels"])
    ft = f'<span class="lbl">{e(G["topic_lbl"])}</span><button data-f="topic" data-v="all" aria-pressed="true">{e(G["all_"])}</button>' + "".join(f'<button data-f="topic" data-v="{k}" aria-pressed="false">{e(l)}</button>' for k, l in G["topics"])
    body = f'''
<section class="hero" style="padding-bottom:24px"><div class="wrap"><div style="max-width:820px"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
<section class="section-tight"><div class="wrap" data-filters><div class="filters">{fl}</div><div class="filters" style="margin-top:10px">{ft}</div><div class="cards stack-2">{"".join(cards)}</div></div></section>
<section class="section section-alt"><div class="wrap center" data-reveal><h2>{e(G["end"]["h"])}</h2><p class="lead sub">{e(G["end"]["p"])}</p><div class="btn-row stack-2"><a class="btn btn-primary" href="{C.ROUTES["early"]}">{e(C.NAV_CTA[1])} <span class="arr">→</span></a><a class="btn btn-ghost" href="{C.ROUTES["how"]}">{e(C.NAV[0][1])}</a></div></div></section>'''
    ld = [{"@type": "CollectionPage", "name": G["title"], "hasPart": [{"@type": "Article", "headline": ARTICLES[a][C.LANG]["title"], "url": DOMAIN + guide_url(C, a)} for a in ARTICLE_ORDER]}]
    return dict(page_id="guides", title=G["title"], description=G["description"], body=body, ld=ld)

def page_article(C, aid):
    G = C.GUIDES; A = ARTICLES[aid][C.LANG]; levels, tip = C.GUIDE_META[aid]; topic = ARTICLES[aid]["topic"]
    topic_lbl = dict(G["topics"])[topic]; rt = read_time(A["blocks"])
    i = ARTICLE_ORDER.index(aid); prev_id = ARTICLE_ORDER[i - 1] if i > 0 else None; next_id = ARTICLE_ORDER[i + 1] if i < len(ARTICLE_ORDER) - 1 else None
    prose = ""; mid = len([b for b in A["blocks"] if b[0] == "h2"]) // 2; seen = 0
    for kind, inner in A["blocks"]:
        if kind == "h2":
            seen += 1
            if seen == mid + 1:
                prose += f'<div class="tip"><span class="mono">{e(G["tip_k"])}</span><p>{e(tip)} <a href="{C.ROUTES["how"]}">{e(C.NAV[0][1])} →</a></p></div>'
            prose += f"<h2>{inner}</h2>"
        else:
            inner = inner.replace('href="/product"', f'href="{C.ROUTES["product"]}"').replace('href="/it/prodotto"', f'href="{C.ROUTES["product"]}"').replace('href="/beta"', f'href="{C.ROUTES["early"]}"').replace('href="/it/beta"', f'href="{C.ROUTES["early"]}"')
            prose += f"<p>{inner}</p>"
    pager = ""
    if prev_id: pager += f'<a href="{guide_url(C, prev_id)}"><span class="mono">← {e(G["prev"])}</span><b>{e(ARTICLES[prev_id][C.LANG]["title"])}</b></a>'
    else: pager += "<span></span>"
    if next_id: pager += f'<a href="{guide_url(C, next_id)}"><span class="mono">{e(G["next"])} →</span><b>{e(ARTICLES[next_id][C.LANG]["title"])}</b></a>'
    url = guide_url(C, aid)
    share = f'<a href="mailto:?subject={e(A["title"])}&body={DOMAIN}{url}" class="link">{e(G["share"])}</a>'
    body = f'''
<section class="article-head"><div class="wrap-narrow">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{C.ROUTES["home"]}">APEX</a><span>/</span><a href="{C.ROUTES["guides"]}">{e(C.NAV[2][1])}</a><span>/</span><span>{e(topic_lbl)}</span></nav>
  <span class="eyebrow">{e(topic_lbl)}</span><h1>{e(A["title"])}</h1>
  <div class="byline"><span class="av">A</span><span>{e(G["by"])}</span><span>·</span><span>{rt} {e(G["read"])}</span><span>·</span>{share}</div>
  <div class="key">{A["lead"]}</div>
</div></section>
<section class="section-tight"><div class="wrap-narrow"><div class="prose">{prose}</div>
  <h2 style="font-size:clamp(24px,2.6vw,32px);margin-top:56px">FAQ</h2><div class="stack-2">{faq_list(A["faq"])}</div>
  <div class="article-foot"><a class="link" href="{C.ROUTES["guides"]}">← {e(G["back"])}</a><span class="muted">{e(G["by"])}</span></div>
  <div class="pager">{pager}</div>
</div></section>
<section class="section section-alt"><div class="wrap-narrow center" data-reveal><h2 style="font-size:clamp(24px,3vw,36px)">{A["cta_h"]}</h2><p class="lead sub">{A["cta_p"]}</p><div class="btn-row stack-2"><a class="btn btn-primary" href="{C.ROUTES["early"]}">{e(C.NAV_CTA[1])} <span class="arr">→</span></a></div></div></section>'''
    ld = [{"@type": "Article", "headline": A["title"], "description": A["description"], "inLanguage": C.LANG, "author": {"@type": "Organization", "name": "APEX"}, "publisher": {"@id": DOMAIN + "/#org"}, "mainEntityOfPage": DOMAIN + url, "dateModified": TODAY},
          {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "APEX", "item": DOMAIN + C.ROUTES["home"]}, {"@type": "ListItem", "position": 2, "name": C.NAV[2][1], "item": DOMAIN + C.ROUTES["guides"]}, {"@type": "ListItem", "position": 3, "name": A["title"], "item": DOMAIN + url}]},
          faq_ld(A["faq"])]
    return dict(page_id="guides", title=A["title"] + " — APEX", description=A["description"], body=body, ld=ld, aid=aid, og_type="article")

def page_faq(C):
    F = C.FAQ; h = F["hero"]
    groups = "".join(f'<div><h2>{e(g)}</h2>{faq_list(items)}</div>' for g, items in F["groups"])
    allq = [q for _, items in F["groups"] for q in items]
    body = f'''
<section class="hero"><div class="wrap"><div class="center" style="max-width:760px;margin:0 auto"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
<section class="section-tight"><div class="wrap-narrow"><div class="faq-groups">{groups}</div></div></section>
{cta_band(C)}'''
    return dict(page_id="faq", title=F["title"], description=F["description"], body=body, ld=[faq_ld(allq)])

def page_contact(C):
    K = C.CONTACT; h = K["hero"]
    items = "".join(f'<div><span class="ic" style="color:var(--lime-ink);display:block;width:26px">{icon("mail")}</span><h3>{e(t)}</h3><p>{e(d)}</p><p style="margin-top:12px"><a href="mailto:{m}">{m}</a></p></div>' for t, d, m in K["items"])
    body = f'''
<section class="hero"><div class="wrap"><div class="center" style="max-width:760px;margin:0 auto"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
<section class="section-tight"><div class="wrap"><div class="contact-grid">{items}</div><p class="muted center stack-2">{e(K["hours"])} · <a class="link" href="{C.ROUTES["faq"]}">{e(K["faq_link"])}</a></p></div></section>
{cta_band(C)}'''
    return dict(page_id="contact", title=K["title"], description=K["description"], body=body)

def page_story(C):
    S = C.STORY; h = S["hero"]
    body_blocks = "".join(f'<div class="split{" rev" if i % 2 else ""}"><div data-reveal>{media("Photo: " + t, "", i)}</div><div data-reveal><h2>{e(t)}</h2><p class="lead">{e(d)}</p></div></div>' for i, (t, d) in enumerate(S["body"]))
    founders = "".join(f'<div class="founder"><span class="av">{e(n[:1])}</span><b>{e(n)}</b><span>{e(r)}</span></div>' for n, r in S["founders"])
    ms = ""
    if S["milestones"]:
        ms = f'<section class="section"><div class="wrap-narrow"><h2 data-reveal>{e(S["milestones_h"])}</h2><div class="timeline stack-2">' + "".join(f'<div><span class="mono">{e(y)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for y, t, d in S["milestones"]) + "</div></div></section>"
    body = f'''
<section class="hero"><div class="wrap"><div style="max-width:860px"><span class="eyebrow">{e(h["eyebrow"])}</span><h1>{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p></div></div></section>
<section class="section-tight"><div class="wrap"><div class="journey">{body_blocks}</div></div></section>
<section class="section section-alt"><div class="wrap"><h2 data-reveal>{e(S["founders_h"])}</h2><div class="founders stack-2">{founders}</div><p class="muted stack-2">{e(S["where"])}</p></div></section>
{ms}
{cta_band(C)}'''
    return dict(page_id="story", title=S["title"], description=S["description"], body=body)

def page_pro(C):
    P = C.PRO; h = P["hero"]
    who = "".join(f'<div class="skill"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in P["who"])
    ben = "".join(f'<div class="skill" data-reveal><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in P["benefits"])
    body = f'''
<section class="hero"><div class="wrap"><div class="hero-grid"><div><span class="eyebrow">{e(h["eyebrow"])}</span><h1 style="font-size:clamp(36px,5vw,64px)">{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p><div class="btn-row"><a class="btn btn-primary btn-lg" href="mailto:{C.SITE["email"]}?subject=APEX%20Pro%20deal">{e(P["btn"])} <span class="arr">→</span></a></div><p class="hero-note">{e(P["note"])}</p></div><div>{media("Photo: instructor and student in the paddock", "", 2)}</div></div></div></section>
<section class="section section-alt"><div class="wrap"><h2 data-reveal>{e(P["who_h"])}</h2><div class="skills stack-2">{who}</div></div></section>
<section class="section"><div class="wrap"><h2 data-reveal>{e(P["benefits_h"])}</h2><div class="skills stack-2">{ben}</div></div></section>
{cta_band(C)}'''
    return dict(page_id="pro", title=P["title"], description=P["description"], body=body)

def page_early(C):
    E_ = C.EARLY; h = E_["hero"]; f = E_["f"]
    packs = "".join(f'<option value="{e(v)}">{e(l)}</option>' for v, l in f["packs"])
    usages = "".join(f'<option value="{v}">{e(l)}</option>' for v, l in f["usages"])
    steps = "".join(f'<div class="skill"><span class="mono" style="color:var(--lime-ink)">{i+1}</span><h3 style="margin-top:8px">{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(E_["steps"]))
    body = f'''
<section class="hero" style="padding-bottom:0"><div class="wrap"><div class="hero-grid" style="align-items:start">
  <div><span class="eyebrow">{e(h["eyebrow"])}</span><h1 style="font-size:clamp(36px,5vw,64px)">{e(h["h"])}</h1><p class="lead">{e(h["p"])}</p>
    <div class="skills stack-2" style="grid-template-columns:1fr">{steps}</div>
    <div class="stack-2"><h3>{e(E_["direct_h"])}</h3><p class="muted sub">{e(E_["direct_p"])}</p><p style="margin-top:10px"><a class="link" href="mailto:{C.SITE["email"]}">{C.SITE["email"]}</a></p></div>
  </div>
  <div>
    <form class="form" id="early-access-form" method="POST" action="/api/early-access">
      <input type="hidden" name="lang" value="{C.LANG}"><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="row"><div class="field"><label for="f-name">{e(f["name"])}</label><input id="f-name" name="name" required autocomplete="name"></div><div class="field"><label for="f-email">{e(f["email"])}</label><input id="f-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="field"><label for="f-pack">{e(f["pack"])}</label><select id="f-pack" name="pack" required><option value="">{e(f["pack_ph"])}</option>{packs}</select></div>
      <div class="row"><div class="field"><label for="f-bike">{e(f["bike"])}</label><input id="f-bike" name="bike" placeholder="{e(f["bike_ph"])}"></div><div class="field"><label for="f-usage">{e(f["usage"])}</label><select id="f-usage" name="usage"><option value="">{e(f["usage_ph"])}</option>{usages}</select></div></div>
      <label class="check"><input type="checkbox" name="consent" required><span>{e(f["consent"])} (<a href="{C.ROUTES["privacy"]}">{e(f["consent_link"])}</a>).</span></label>
      <button class="btn btn-primary btn-lg" type="submit">{e(f["btn"])} <span class="arr">→</span></button>
      <p class="form-note">{e(f["note"])}</p>
      <p id="early-access-err" class="notice" hidden style="margin-top:14px"></p>
    </form>
    <div class="form-ok" id="early-access-ok" role="status"><h3>✓ {e(E_["ok"]["h"])}</h3><p class="sub">{e(E_["ok"]["p"])}</p></div>
  </div>
</div></div></section>
<section class="section-tight"><div class="wrap">{trust_row(C)}</div></section>'''
    return dict(page_id="early", title=E_["title"], description=E_["description"], body=body)

def page_legal(C, key):
    L = C.LEGAL[key]
    secs = "".join(f'<h2>{e(t)}</h2><p>{e(d)}</p>' for t, d in L["sections"])
    body = f'''
<section class="article-head"><div class="wrap-narrow"><span class="eyebrow">{e(C.FOOTER["legal"][0])}</span><h1>{e(L["h"])}</h1><p class="muted sub">{e(L["updated"])}</p><p class="notice stack-2">{e(C.LEGAL_NOTICE)}</p></div></section>
<section class="section-tight"><div class="wrap-narrow legal">{secs}</div></section>'''
    return dict(page_id=key, title=L["title"], description=L["sections"][0][1], body=body)

# ------------------------------------------------------------------- build ---
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh: fh.write(content)

def build():
    urls = []
    for C in (EN, IT):
        pages = [page_home(C), page_how(C), page_reviews(C), page_product(C), page_guides(C), page_faq(C), page_contact(C), page_story(C), page_pro(C), page_early(C)] + [page_legal(C, k) for k in ("terms", "privacy", "warranty", "returns")]
        for p in pages:
            canonical = C.ROUTES[p["page_id"]]; alt = alt_url(C, p["page_id"])
            write(out_path(canonical), layout(C, canonical=canonical, alt=alt, **p)); urls.append((canonical, alt))
        for aid in ARTICLE_ORDER:
            p = page_article(C, aid); canonical = guide_url(C, aid); alt = alt_url(C, "guides", aid)
            write(out_path(canonical), layout(C, canonical=canonical, alt=alt, **p)); urls.append((canonical, alt))
    # static assets
    for f in ("apex.css", "apex.js"): shutil.copy(os.path.join(SRC, f), os.path.join(ROOT, f))
    # sitemap (EN entries carry hreflang pairs)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u, a in urls:
        en, it = (u, a) if not u.startswith("/it") else (a, u)
        sm.append(f'  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod><xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{en}"/><xhtml:link rel="alternate" hreflang="it" href="{DOMAIN}{it}"/><xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{en}"/></url>')
    sm.append("</urlset>")
    write(os.path.join(ROOT, "sitemap.xml"), "\n".join(sm) + "\n")
    print(f"built {len(urls)} pages")
    return urls

def check(urls):
    known = {u for u, _ in urls} | {"/api/early-access"}
    bad = 0
    for u, _ in urls:
        t = open(out_path(u), encoding="utf-8").read()
        for href in re.findall(r'href="(/[^"#?]*)', t):
            if href.startswith("/assets/") or href in ("/apex.css", "/apex.js"): continue
            if href not in known: print("BROKEN", u, "->", href); bad += 1
    print("link check:", "ok" if not bad else f"{bad} broken")

if __name__ == "__main__":
    u = build()
    if "--check" in sys.argv: check(u)
