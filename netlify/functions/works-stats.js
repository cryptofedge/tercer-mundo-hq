const fs = require('fs'), path = require('path');
exports.handler = async () => {
  const h = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' };
  try {
    const works = JSON.parse(fs.readFileSync(path.join(__dirname, '../../data/works.json'), 'utf8')).works;
    const c = fn => works.filter(fn).length;
    return { statusCode: 200, headers: h, body: JSON.stringify({
      total: works.length,
      bmi:    c(w => w.bmi_id && !['NOT REGISTERED','NOT FOUND'].includes(w.bmi_id)),
      ascap:  c(w => w.ascap && !['not_registered','unknown'].includes(w.ascap)),
      sayce:  c(w => w.sayce === 'registered'),
      songtrust: c(w => w.songtrust === true),
      soundexchange: c(w => w.soundexchange === true),
      tv_placements: c(w => !!w.tv),
      gaps: {
        bmi:   c(w => !w.bmi_id || ['NOT REGISTERED','NOT FOUND'].includes(w.bmi_id)),
        ascap: c(w => !w.ascap || ['not_registered','unknown'].includes(w.ascap)),
        sayce: c(w => w.sayce !== 'registered'),
        songtrust: c(w => w.songtrust !== true),
        soundexchange: c(w => w.soundexchange !== true)
      },
      uncollected: { sayce: 1000, songtrust: 2500, soundexchange: 1000, ascap: 800, total: 5300 }
    })};
  } catch(e) { return { statusCode: 500, headers: h, body: JSON.stringify({ error: e.message }) }; }
};
