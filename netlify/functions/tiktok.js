exports.handler = async () => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  const token = process.env.TIKTOK_ACCESS_TOKEN;
  if (!token) return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: 'not_configured' }) };
  try {
    const res = await fetch('https://open.tiktokapis.com/v2/user/info/?fields=display_name,follower_count,likes_count,video_count', {
      headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }
    }).then(r => r.json());
    const u = res.data?.user;
    return { statusCode: 200, headers: h, body: JSON.stringify({
      connected: true, display_name: u?.display_name,
      followers: u?.follower_count || 0, likes: u?.likes_count || 0, video_count: u?.video_count || 0
    })};
  } catch(e) { return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: e.message }) }; }
};
