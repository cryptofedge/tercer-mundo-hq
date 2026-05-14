const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET || 'fedge2o-secret';
const USERS = {
  fellito: { pw: process.env.PW_FELLITO, tier: 5, name: 'Fellito Rodriguez', role: 'Executive Director' },
  mando:   { pw: process.env.PW_MANDO,   tier: 1, name: 'Mando El Pelado',   role: 'Artist' }
};
exports.handler = async (event) => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type' };
  if (event.httpMethod === 'OPTIONS') return { statusCode: 200, headers: h, body: '' };
  if (event.httpMethod !== 'POST') return { statusCode: 405, headers: h, body: '{}' };
  try {
    const { username, password } = JSON.parse(event.body || '{}');
    const u = USERS[username?.toLowerCase()];
    if (!u || u.pw !== password)
      return { statusCode: 401, headers: h, body: JSON.stringify({ error: 'Invalid credentials' }) };
    const token = jwt.sign({ username: username.toLowerCase(), name: u.name, tier: u.tier, role: u.role }, SECRET, { expiresIn: '7d' });
    return { statusCode: 200, headers: h, body: JSON.stringify({ token, user: { name: u.name, tier: u.tier, role: u.role } }) };
  } catch(e) {
    return { statusCode: 500, headers: h, body: JSON.stringify({ error: e.message }) };
  }
};
