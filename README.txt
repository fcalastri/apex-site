APEX — website (static + early access pipeline, EN + IT)
=========================================================

STRUCTURE
  index.html / it/index.html ......... Home (new, v2)
  how-it-works.html / it/come-funziona.html
  for-riders.html / it/per-i-piloti.html   (legacy — replaced in T3/T4)
  beta.html / it/beta.html ........... Early access quick form (wired to /api/early-access)
  apex.css, apex.js .................. design system v2 + interactions
  functions/api/early-access.js ...... Pages Function: D1 storage + Resend email
  schema.sql ......................... D1 table
  wrangler.toml ...................... Pages + D1 binding config

EARLY ACCESS PIPELINE
  Form POST -> /api/early-access
    1. saves the request into D1 table `early_access_requests`
    2. emails privatelofter@gmail.com via Resend
       subject: [APEX EA] Nuova richiesta — {Pack} — {Nome}
  The lead survives if either step succeeds. Honeypot field blocks basic bots.

ONE-TIME SETUP (~15 min)
  1. npm i -g wrangler && wrangler login
  2. wrangler d1 create apex-early-access
       -> copy the database_id it prints into wrangler.toml
  3. wrangler d1 execute apex-early-access --remote --file=schema.sql
  4. Resend: create the account WITH privatelofter@gmail.com at resend.com,
     create an API key. (Without a verified domain, Resend only delivers to
     the account owner's address and sends from onboarding@resend.dev —
     which is exactly our setup. Later: verify apex-rider.com and set
     FROM_EMAIL=hello@apex-rider.com in Pages > Settings > Variables.)
  5. wrangler pages project create apex   (skip if it already exists)
  6. wrangler pages secret put RESEND_API_KEY --project-name=apex
       -> paste the Resend key

DEPLOY (every time)
  wrangler pages deploy . --project-name=apex

  IMPORTANT: dashboard drag-and-drop is NO LONGER enough — the /api function
  only ships via wrangler. Custom domain: project -> Custom domains -> apex-rider.com.

READ THE SAVED REQUESTS
  wrangler d1 execute apex-early-access --remote \
    --command "SELECT * FROM early_access_requests ORDER BY created_at DESC"
  (or Cloudflare dashboard -> D1 -> apex-early-access -> console; export via SQL)

TEST AFTER FIRST DEPLOY
  Submit the form on /beta.html -> expect redirect to ?sent=1 with the green
  confirmation, a new D1 row, and the email in privatelofter@gmail.com inbox.
