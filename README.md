# apex-rider.com — v3 (Carv-structured redesign)

Static, bilingual (EN/IT) marketing site for APEX, built to run on **Cloudflare Pages**
with one Pages Function (`/api/early-access`) backed by D1 + Resend.

```
/                      built HTML (served as-is by Cloudflare Pages — DO NOT edit by hand)
/it/                   Italian pages
/guides/  /it/guide/   articles
/legal/   /it/legal/   terms · privacy · warranty · returns (drafts)
/assets/               favicons, OG images
/functions/api/        early-access.js (Pages Function)
/src/                  apex.css · apex.js  (source of the two static files at root)
/tools/build.py        generator — renders everything from tools/content/*
/tools/content/en.py   all English copy
/tools/content/it.py   all Italian copy
/tools/content/articles.json   the 5 guides (EN + IT), ported from v2
_redirects _headers wrangler.toml schema.sql robots.txt llms.txt sitemap.xml
```

## Edit → build → deploy

1. Change copy in `tools/content/en.py` / `it.py` (or an article in `articles.json`).
2. `python3 tools/build.py --check` (Python 3.8+, no dependencies). Rebuilds all 38 pages,
   copies `src/apex.css|js` to root, regenerates `sitemap.xml`, and link-checks.
3. Commit and push. Cloudflare Pages deploys the repo root.

Never edit the HTML files directly: the next build overwrites them.

## Cloudflare Pages settings (unchanged from v2)

- Build command: *(none)* · Build output directory: `/` (`pages_build_output_dir = "."` in wrangler.toml)
- D1 binding `DB` → `apex-early-access` (see `schema.sql`; run `wrangler d1 execute apex-early-access --file=schema.sql` once)
- Secret `RESEND_API_KEY` → `wrangler pages secret put RESEND_API_KEY`
- Optional vars `TO_EMAIL`, `FROM_EMAIL`

The function now redirects to `/early-access?sent=1` (EN) or `/it/accesso-anticipato?sent=1` (IT)
for non-JS submissions; with JS the form posts via fetch and shows the success state inline.
The footer newsletter posts to the same endpoint with `pack=newsletter` so signups land in D1 too.

## URL structure (v3)

| EN | IT | Carv equivalent |
|---|---|---|
| `/` | `/it/` | Home |
| `/how-it-works` | `/it/come-funziona` | How It Works |
| `/reviews` | `/it/recensioni` | Reviews |
| `/product` | `/it/prodotto` | Product page (packs, tabs, specs) |
| `/guides/` + 5 articles | `/it/guide/` + 5 | Blog (filters by level + topic) |
| `/faq` | `/it/faq` | Help Center |
| `/contact` | `/it/contatti` | Contact |
| `/our-story` | `/it/storia` | Our Story |
| `/pro` | `/it/pro` | Pro Deal |
| `/early-access` | `/it/accesso-anticipato` | Onboarding / Buy flow |
| `/legal/terms` `privacy` `warranty` `returns` | `/it/legal/termini` `privacy` `garanzia` `resi` | Legal |

All v2 URLs (`/beta`, `/pricing`, `/answers/*`, `/it/risposte/*`, …) 301 to their v3 equivalent
in `_redirects`, one hop, no chains.

See `DESIGN-AND-STRUCTURE.md` for the design rationale and `CONTENT-TODO.md` for what still
needs real data before launch.
