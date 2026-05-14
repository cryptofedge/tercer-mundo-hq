const AID = '0pizWb9jgAB1NTCIcJ043H';
exports.handler = async () => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  const id = process.env.SPOTIFY_CLIENT_ID, sec = process.env.SPOTIFY_CLIENT_SECRET;
  if (!id || !sec) return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: 'not_configured' }) };
  try {
    const tok = await fetch('https://accounts.spotify.com/api/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ' + Buffer.from(id+':'+sec).toString('base64') },
      body: 'grant_type=client_credentials'
    }).then(r => r.json());
    const [artist, top] = await Promise.all([
      fetch(`https://api.spotify.com/v1/artists/${AID}`, { headers: { Authorization: `Bearer ${tok.access_token}` } }).then(r => r.json()),
      fetch(`https://api.spotify.com/v1/artists/${AID}/top-tracks?market=US`, { headers: { Authorization: `Bearer ${tok.access_token}` } }).then(r => r.json())
    ]);
    return { statusCode: 200, headers: h, body: JSON.stringify({
      connected: true,
      followers: artist.followers?.total || 0,
      popularity: artist.popularity || 0,
      genres: artist.genres || [],
      top_tracks: (top.tracks || []).slice(0, 5).map(t => ({
        name: t.name, popularity: t.popularity,
        album: t.album?.name, image: t.album?.images?.[2]?.url
      }))
    })};
  } catch(e) { return { statusCode: 200, headers: h, body: JSON.stringify({ connected: false, reason: e.message }) }; }
};
