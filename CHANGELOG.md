# v3.0.0 — 2026-08-27 — Carv-structured redesign

- New information architecture mirroring getcarv.com: Home, How it works, Reviews, Product
  (packs + tabs), Guides (filterable), FAQ, Contact, Our story, Pro, Early access, Legal ×4.
  38 pages, EN + IT.
- New light design system (`src/apex.css`), review card as signature element, labelled image slots.
- All copy rewritten in both languages; v2 guides ported intact into the new article template.
- Generator (`tools/build.py`) + content files replace hand-edited HTML.
- `_redirects` covers every v1/v2 URL → v3, one hop. Sitemap regenerated with hreflang.
- `/api/early-access` now redirects to the new pages; footer newsletter reuses it.
