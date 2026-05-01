// POST /api/subscribe — captures email, notifies via Resend
export default async function handler(req, res) {
  // CORS / methods
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    return res.status(200).end();
  }
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, source = 'landing' } = req.body || {};

  // Basic validation
  if (!email || typeof email !== 'string' || !email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
    return res.status(400).json({ error: 'Valid email required' });
  }
  if (email.length > 256) {
    return res.status(400).json({ error: 'Email too long' });
  }

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error('RESEND_API_KEY missing');
    return res.status(500).json({ error: 'Server misconfigured' });
  }

  const ip = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  const ua = req.headers['user-agent'] || 'unknown';
  const ts = new Date().toISOString();

  // Notify owner via Resend
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'Vault Pro <onboarding@resend.dev>',
        to: ['jadedfocus@gmail.com'],
        reply_to: email,
        subject: `🎉 New Vault Pro subscriber: ${email}`,
        text: [
          `New subscriber from ${source}`,
          ``,
          `Email:   ${email}`,
          `Source:  ${source}`,
          `Time:    ${ts}`,
          `IP:      ${ip}`,
          `UA:      ${ua}`,
          ``,
          `Landing: https://vault-pro-landing.vercel.app`,
        ].join('\n'),
      }),
    });

    if (!r.ok) {
      const txt = await r.text();
      console.error('Resend error:', r.status, txt);
      return res.status(500).json({ error: 'Notification failed' });
    }
  } catch (err) {
    console.error('Resend exception:', err);
    return res.status(500).json({ error: 'Notification failed' });
  }

  res.setHeader('Access-Control-Allow-Origin', '*');
  return res.status(200).json({ ok: true, message: 'Thanks — you\'re on the v1.1 list' });
}
