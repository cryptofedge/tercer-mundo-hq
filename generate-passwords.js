const crypto = require('crypto');
const SECRET = process.argv[4] || 'fedge2o-dev-secret';
const hash = p => crypto.createHash('sha256').update(p + SECRET).digest('hex');
console.log('\nPW_FELLITO=' + hash(process.argv[2]));
console.log('PW_MANDO='   + hash(process.argv[3]));
console.log('\nAdd these + JWT_SECRET to Netlify env vars.\n');
