/**
 * APEX — Early access endpoint (Cloudflare Pages Function)
 * POST /api/early-access
 *
 * Pipeline (plan §5): quick form → D1 storage → Resend email notification.
 * The lead survives if EITHER storage or email succeeds.
 *
 * Bindings / vars:
 *   DB              D1 database (wrangler.toml)
 *   RESEND_API_KEY  secret — `wrangler pages secret put RESEND_API_KEY`
 *   TO_EMAIL        optional var, defaults to privatelofter@gmail.com
 *   FROM_EMAIL      optional var, defaults to onboarding@resend.dev
 *                   (switch to hello@apex-rider.com after domain verification on Resend)
 */

const DEFAULT_TO = 'privatelofter@gmail.com';
const DEFAULT_FROM = 'APEX <onboarding@resend.dev>';

export async function onRequestPost(context) {
  const { request, env } = context;

  let form;
  try {
    form = await request.formData();
  } catch (e) {
    return new Response('Bad request', { status: 400 });
  }
  const f = (k, max) => String(form.get(k) || '').trim().slice(0, max);

  // Honeypot: bots fill the hidden "website" field → pretend success, store nothing.
  const lang = f('lang', 2) === 'it' ? 'it' : 'en';
  if (f('website', 10)) return redirectOk(lang);

  const name = f('name', 120);
  const email = f('email', 200);
  const pack = f('pack', 40);
  const bike = f('bike', 120);
  const usage = f('usage', 60);
  const consent = form.get('consent') ? 1 : 0;

  if (!name || !pack || !consent || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return new Response(
      lang === 'it'
        ? 'Compila nome, email, pack e consenso privacy, poi riprova.'
        : 'Please fill in name, email, pack and the privacy consent, then retry.',
      { status: 400, headers: { 'content-type': 'text/plain; charset=utf-8' } }
    );
  }

  let stored = false;
  let mailed = false;

  // 1 · Store in D1
  try {
    await env.DB.prepare(
      `INSERT INTO early_access_requests (name, email, pack, bike, usage, lang, consent, created_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))`
    ).bind(name, email, pack, bike, usage, lang, consent).run();
    stored = true;
  } catch (e) {
    console.error('D1 insert failed:', e && e.message);
  }

  // 2 · Email notification via Resend
  try {
    const to = env.TO_EMAIL || DEFAULT_TO;
    const from = env.FROM_EMAIL || DEFAULT_FROM;
    const text = [
      `Nome:     ${name}`,
      `Email:    ${email}`,
      `Pack:     ${pack}`,
      `Moto:     ${bike || '—'}`,
      `Uso:      ${usage || '—'}`,
      `Lingua:   ${lang}   ·   Salvato in D1: ${stored ? 'sì' : 'NO — recuperare da questa email'}`,
    ].join('\n');

    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from,
        to: [to],
        reply_to: email,
        subject: `[APEX EA] Nuova richiesta — ${pack} — ${name}`,
        text,
      }),
    });
    mailed = res.ok;
    if (!res.ok) console.error('Resend failed:', res.status, await res.text());
  } catch (e) {
    console.error('Resend error:', e && e.message);
  }

  if (!stored && !mailed) {
    return new Response(
      lang === 'it'
        ? 'Qualcosa è andato storto e la richiesta non è stata registrata. Scrivici a hello@apex-rider.com.'
        : 'Something went wrong and your request was not recorded. Email us at hello@apex-rider.com.',
      { status: 500, headers: { 'content-type': 'text/plain; charset=utf-8' } }
    );
  }

  return redirectOk(lang);
}

function redirectOk(lang) {
  return new Response(null, {
    status: 303,
    headers: { Location: lang === 'it' ? '/it/beta.html?sent=1' : '/beta.html?sent=1' },
  });
}
