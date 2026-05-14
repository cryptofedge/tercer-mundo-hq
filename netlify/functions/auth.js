const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET || 'fedge2o-dev-secret';
const hash = p => crypto.createHash('sha256').update(p + SECRET).digest('hex');
const USERS = {
  fellito: { tier: 5, name: 'Fellito Rodriguez', role: 'Executive Director' },
  mando:   { tier: 1, name: 'Mando El Pelado',   role: 'Artist' }
};
exports.handler = async (event) => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  if (event.httpMethod === 'OPTIONS') return { statusCode: 200, headers: h, body: '' };
  if (event.httpMethod !== 'POST') return { statusCode: 405, headers: h, body: '{}' };
  const { username, password } = JSON.parse(event.body || '{}');
  const u = USERS[username?.toLowerCase()];
  const expected = process.env[`PW_${username?.toUpperCase()}`];
  if (!u || !expected || hash(password) !== expected)
    return { statusCode: 401, headers: h, body: JSON.stringify({ error: 'Invalid credentials' }) };
  const token = jwt.sign({ username: username.toLowerCase(), ...u }, SECRET, { expiresIn: '7d' });
  return { statusCode: 200, headers: h, body: JSON.stringify({ token, user: { name: u.name, tier: u.tier, role: u.role } }) };
};
