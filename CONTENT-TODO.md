# Content still needed before launch

Everything below is a hole Carv fills with real data and APEX cannot yet. Each is wired: add the
entry in `tools/content/en.py` **and** `it.py`, rebuild, done.

| Item | Where | What happens today |
|---|---|---|
| Press / expert quotes | `PRESS = [("“<15 words”", "Outlet")]` | Strip hidden on Home and Reviews |
| Survey numbers ("X% improved their cornering") | `RESULTS = dict(eyebrow, h, intro, items=[(v, label)])` | "Your results" block hidden |
| Community line ("N riders") | `COMMUNITY = dict(h, p)` | Hidden on Reviews |
| Rider testimonials (name, role, quote) | `TESTIMONIALS = [dict(q, name, role)]` | "First riders are on the road" band on Home, Product, Reviews |
| Rider videos | `REVIEWS["videos"] = [("title", "youtube_id")]` | Section hidden |
| Milestones | `STORY["milestones"] = [("2025", "title", "text")]` | Section hidden |
| Founder roles | `STORY["founders"]` | All three listed as "Co-founder" — add real titles |
| Product photography (5 slots) + step photos + story photos | `media()` calls in `tools/build.py` | Labelled placeholder blocks |
| Hero video (Carv autoplays one) | `page_home()` hero right column | Review card is used instead — keep it if no video |
| Physical specs (size, weight, battery, IP rating, app store links) | `PRODUCT["specs"]` | Note says "published with the first run" |
| Delivery window for first run | `PRODUCT["buy_meta"]` | "confirmed when we contact you" |
| Legal texts | `LEGAL` in both files | Draft structure with a visible "Draft" notice — counsel must review; remove `LEGAL_NOTICE` rendering in `page_legal()` when approved |
| Social links | footer | Only email shown; add Instagram/YouTube in `layout()` when accounts exist |
| Newsletter double opt-in | `functions/api/early-access.js` | Signups are stored/emailed like early-access requests; no confirmation mail |
| OG images | `assets/apex-og*.png` | Reused from v2 (dark). Regenerate on the light system when photography exists |

Also worth deciding: whether Pro pre-order should have its own landing page (`/lp/pro`), as Carv
does for campaigns.
