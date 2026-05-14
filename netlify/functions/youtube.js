const CID = 'UCex_oMHDznqRpZM7A03RjVw';
exports.handler = async () => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  const key = process.env.YOUTUBE_API_KEY;
  if (!key) return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: 'not_configured' }) };
  try {
    const data = await fetch(`https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id=${CID}&key=${key}`).then(r => r.json());
    const item = data.items?.[0];
    return { statusCode: 200, headers: h, body: JSON.stringify({
      connected: true,
      channel_name: item?.snippet?.title,
      subscribers: parseInt(item?.statistics?.subscriberCount || 0),
      total_views: parseInt(item?.statistics?.viewCount || 0),
      video_count: parseInt(item?.statistics?.videoCount || 0)
    })};
  } catch(e) { return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: e.message }) }; }
};
