# APEX v3 — design & structure notes

Goal: take the structure, page logic and communication discipline of getcarv.com and rebuild
apex-rider.com on it, for APEX's audience (road and track motorcyclists), mission (every ride
becomes a review) and product (kit + fitting + 12 months of reviews, one price).

## 1. What was taken from Carv

| Carv pattern | APEX v3 implementation |
|---|---|
| Header: Logo · How It Works · Reviews · Blog · **Buy Now** | Logo · How it works · Reviews · Guides · **Buy** · EN/IT · *Request early access* |
| Home = one promise → press strip → "Meet Carv 2 in 3 steps" → results → community → testimonials → trust row | Home = one promise → *(press strip, conditional)* → **"In every sport the review is normal"** → "Meet APEX in 3 steps" → *(results, conditional)* → "Three things after every ride" → who it's for → testimonials → trust row → CTA band |
| How It Works = 4-step journey (track → review → coach → improve) + skills + tech explainer | 4-step journey (**Fit → Ride → Review → Improve**) + "the four things that make a corner" (braking/line/throttle/smoothness) + "Under the fairing" (sensing / Ride AI / road detection) + "What APEX is not" + FAQ |
| Reviews = press, numbers, review wall, videos, ability-based FAQs | Same skeleton; press/numbers/wall/videos are data-driven and render an honest empty state until real data exists; FAQs by rider type are live |
| Product = gallery, price, pass selector, delivery/returns reassurance, tabs (How it works / Passes / Tech specs), outcomes by ability, tracking, 3 coaching modes | Gallery (5 slots), price that updates with the pack radio, Start/Rider/Pro selector, 4 reassurance lines, tabs (How it works / Packs / Tech specs), outcomes by rider level, "APEX tracks every ride", 3 coaching modes, pack comparison + "how buying works" |
| Blog with two classification axes (ability × content type) | Guides with **rider level × topic** filters, featured card, read time, byline, prev/next, breadcrumbs, in-article "APEX tip" |
| Help Center, Contact, Our Story, Pro Deal, Onboarding, Legal ×4 | FAQ (4 groups), Contact, Our story, Pro (instructors & schools), Early access, Legal ×4 (drafts) |
| Footer: product / company / legal columns + newsletter + socials | Same, newsletter wired to the existing D1 endpoint |

## 2. Where APEX deliberately differs from Carv

- **No invented social proof.** Carv leans on 56k skiers, 5,393-rider surveys and 20+ named quotes.
  APEX has none of that yet. Those blocks exist in the code (`PRESS`, `RESULTS`, `COMMUNITY`,
  `TESTIMONIALS`, `videos`, `milestones` in `tools/content/*.py`) and switch on the moment data is
  added. Until then the home/reviews/product pages show a plain "the first riders are on the road
  now" band instead of fake quotes. This matches APEX's stated preference: precision over inflation.
- **The sports-review comparison** (chess / tennis / football / rider) replaces Carv's press strip as
  the second thing you see. It is APEX's strongest single argument and it was buried on v2.
- **Buy flow = early access, not cart.** Carv's Buy → Cart → Checkout becomes Buy → pack selector →
  early-access form (pack pre-filled from `?pack=`) → founders confirm bike → payment. Every "Buy"
  CTA and the product page say explicitly that there is no payment on the site.
- **One accent, light base.** Carv is white with photography. APEX v2 was a fully dark dashboard.
  v3 goes light and photography-first like Carv, keeps APEX Lime as the only accent, and keeps the
  dark surface for exactly one thing: the review card, which is the product.

## 3. Visual system

- **Type**: Archivo 800/900 for display (kept from the brand kit), Inter for body, IBM Plex Mono
  for data labels, eyebrows and the review card — the mono is what makes the site feel like a
  measurement tool rather than a lifestyle brand.
- **Colour**: paper `#FFFFFF` / `#F4F6F8`, ink `#0B0F14`, lime `#B8FF2C` (never as body text on
  white; `#5C8A00` is the on-white lime for eyebrows), asphalt surfaces for the review and tech
  sections.
- **Signature element**: the **review card** — corner map with your line (lime) drawn against the
  ideal line (grey dashed), brake/apex/throttle markers, three scores, three flags, one "work on".
  It appears in the hero, on How it works (step 3, anchored `#review`) and in the product tab.
  The line draws itself on load (respects `prefers-reduced-motion`).
- **Image slots**: every photo/video position is a labelled `.media` block (dark or light) with a
  road ribbon so the layout reads correctly before real photography exists. Labels say what the
  photo should be. Replace with `<img>`/`<video>` in `tools/build.py → media()` when assets arrive.

## 4. Copy principles applied

- Verbs first, second person, no marketing adjectives: "Fit the kit once. Forget it."
- Every claim on the site is something APEX already said on v2 or can defend today
  (prices, what's included, no subscription, no payment on site, works on any bike, road + track).
- Anything not yet true is either omitted or, for legal/spec pages, marked as draft on the page.
- Rider segments are named by how they ride (new / weekend / track), not by skill adjectives.
- EN and IT are written separately, not machine-translated; IT uses "review" untranslated,
  matching the v2 tagline "Ogni giro diventa una review".

## 5. Technical notes

- Zero build dependencies: `python3 tools/build.py`. Output is committed, so Cloudflare Pages needs
  no build step (same as v2).
- Schema.org graph per page (Organization, WebSite, WebPage + FAQPage / Product / Article /
  BreadcrumbList / CollectionPage), `hreflang` en/it/x-default on every page and in the sitemap.
- `_redirects` maps every v1 and v2 URL to v3 in one hop; `--check` verifies internal links.
- Accessibility: skip link, visible focus, semantic tabs (`role=tab/tabpanel`), labelled form
  fields, `<details>` FAQs, reduced-motion respected for marquee, reveal and line-draw.
- Mobile: hamburger nav, single-column grids, sticky product gallery disabled below 900px.
