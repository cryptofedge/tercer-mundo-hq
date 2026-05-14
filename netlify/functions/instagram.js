exports.handler = async () => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  const token = process.env.INSTAGRAM_ACCESS_TOKEN;
  if (!token) return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: 'not_configured' }) };
  try {
    const p = await fetch(`https://graph.instagram.com/me?fields=username,followers_count,media_count&access_token=${token}`).then(r => r.json());
    return { statusCode: 200, headers: h, body: JSON.stringify({
      connected: true, username: p.username,
      followers: p.followers_count || 0, post_count: p.media_count || 0
    })};
  } catch(e) { return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: e.message }) }; }
};
