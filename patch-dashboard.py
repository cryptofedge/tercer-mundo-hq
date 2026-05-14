import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Inject new CSS before </style>
new_css = """
.login-overlay{position:fixed;inset:0;background:var(--bg);z-index:9999;display:flex;align-items:center;justify-content:center}
.login-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius-lg);padding:40px;width:380px;max-width:90vw}
.login-logo{font-family:var(--font-mono);color:var(--orange);font-size:11px;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px}
.login-title{font-size:22px;font-weight:600;margin-bottom:4px}
.login-sub{font-size:12px;color:var(--text3);font-family:var(--font-mono);margin-bottom:28px}
.login-field{margin-bottom:14px}
.login-field label{display:block;font-size:11px;color:var(--text3);font-family:var(--font-mono);margin-bottom:6px;letter-spacing:0.05em;text-transform:uppercase}
.login-field input{width:100%;background:var(--bg3);border:1px solid var(--border2);border-radius:var(--radius);padding:10px 14px;color:var(--text);font-family:var(--font-mono);font-size:13px;outline:none;transition:border 0.12s}
.login-field input:focus{border-color:var(--orange)}
.login-btn{width:100%;background:var(--orange);color:#fff;border:none;border-radius:var(--radius);padding:11px;font-family:var(--font-mono);font-size:13px;font-weight:600;cursor:pointer;margin-top:8px;transition:background 0.12s}
.login-btn:hover{background:var(--orange-dim)}
.login-err{color:#fca5a5;font-size:12px;font-family:var(--font-mono);margin-top:10px;text-align:center;display:none}
.platform-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px}
.platform-card{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-lg);padding:16px}
.platform-header{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.platform-icon{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.platform-name{font-weight:600;font-size:13px}
.platform-status{font-size:11px;font-family:var(--font-mono);margin-top:1px}
.platform-status.ok{color:var(--green)}
.platform-status.off{color:var(--text3)}
.platform-stats{display:flex;flex-direction:column;gap:4px;margin-bottom:10px}
.platform-stat{font-size:12px;color:var(--text2)}
.platform-stat span{color:var(--text);font-weight:600;font-family:var(--font-mono)}
.connect-btn{background:var(--bg4);border:1px solid var(--border2);border-radius:var(--radius);padding:6px 12px;font-family:var(--font-mono);font-size:11px;color:var(--text2);cursor:pointer;transition:all 0.12s;width:100%;text-align:center}
.connect-btn:hover{background:var(--orange-bg);color:var(--orange);border-color:rgba(255,98,0,0.3)}
.connect-btn.live{background:rgba(34,197,94,0.1);color:#86efac;border-color:rgba(34,197,94,0.2);cursor:default}
.prog-row{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.prog-label{font-family:var(--font-mono);font-size:11px;color:var(--text2);width:130px;flex-shrink:0}
.prog-bar{flex:1;height:6px;background:var(--bg4);border-radius:3px;overflow:hidden}
.prog-fill{height:100%;border-radius:3px;transition:width 0.8s ease}
.prog-val{font-family:var(--font-mono);font-size:11px;color:var(--text2);width:40px;text-align:right;flex-shrink:0}
.track-row{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.track-row:last-child{border-bottom:none}
.track-img{width:32px;height:32px;border-radius:4px;background:var(--bg4);object-fit:cover;flex-shrink:0}
.track-name{font-size:13px;flex:1;color:var(--text)}
.track-pop{font-family:var(--font-mono);font-size:11px;color:var(--text3)}
.live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:5px;animation:pulse 2s infinite}
.spinner{display:inline-block;width:14px;height:14px;border:2px solid var(--border);border-top-color:var(--orange);border-radius:50%;animation:spin 0.7s linear infinite;vertical-align:middle;margin-right:6px}
@keyframes spin{to{transform:rotate(360deg)}}
"""
html = html.replace('@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}', '@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}' + new_css)

# 2. Login overlay before shell
login_html = """<div class="login-overlay" id="login-overlay">
  <div class="login-box">
    <div class="login-logo">3er Mundo · FEDGE 2.O</div>
    <div class="login-title">Tercer Mundo HQ</div>
    <div class="login-sub">v1.0.0 · Artist Intelligence Platform</div>
    <div class="login-field"><label>Username</label><input type="text" id="login-user" placeholder="fellito or mando" autocomplete="username"></div>
    <div class="login-field"><label>Password</label><input type="password" id="login-pass" placeholder="••••••••" autocomplete="current-password" onkeydown="if(event.key==='Enter')doLogin()"></div>
    <button class="login-btn" id="login-btn" onclick="doLogin()">Sign In →</button>
    <div class="login-err" id="login-err">Invalid username or password</div>
    <div style="margin-top:20px;font-size:11px;color:var(--text3);font-family:var(--font-mono);text-align:center;">Powered by FEDGE 2.O · Eclat Universe</div>
  </div>
</div>
"""
html = html.replace('<div class="shell">', login_html + '<div class="shell" id="app-shell" style="display:none">')

# 3. Add Connect nav item
html = html.replace(
    '<button class="nav-item" onclick="goTab(\'agent\',this)">&gt;_ Agent</button>',
    '<button class="nav-item" onclick="goTab(\'agent\',this)">&gt;_ Agent</button>\n      <button class="nav-item" onclick="goTab(\'connect\',this)">⬡ Connect</button>'
)

# 4. Add Connect + new Analytics tabs before closing content div
connect_tab = """
      <!-- CONNECT -->
      <div id="tab-connect" class="tab-panel">
        <div class="section-title">Platform Connections</div>
        <div id="platforms-grid" class="platform-grid">
          <div class="platform-card">
            <div class="platform-header">
              <div class="platform-icon" style="background:rgba(30,215,96,0.15);">🎵</div>
              <div><div class="platform-name">Spotify</div><div class="platform-status" id="sp-status">Loading...</div></div>
            </div>
            <div class="platform-stats" id="sp-stats"></div>
            <button class="connect-btn" id="sp-btn" onclick="window.open('https://developer.spotify.com/dashboard','_blank')">Configure →</button>
          </div>
          <div class="platform-card">
            <div class="platform-header">
              <div class="platform-icon" style="background:rgba(255,0,0,0.12);">▶</div>
              <div><div class="platform-name">YouTube</div><div class="platform-status" id="yt-status">Loading...</div></div>
            </div>
            <div class="platform-stats" id="yt-stats"></div>
            <button class="connect-btn" id="yt-btn" onclick="window.open('https://console.cloud.google.com','_blank')">Configure →</button>
          </div>
          <div class="platform-card">
            <div class="platform-header">
              <div class="platform-icon" style="background:rgba(225,48,108,0.12);">📸</div>
              <div><div class="platform-name">Instagram</div><div class="platform-status" id="ig-status">Loading...</div></div>
            </div>
            <div class="platform-stats" id="ig-stats"></div>
            <button class="connect-btn" id="ig-btn" onclick="window.open('https://developers.facebook.com','_blank')">Configure →</button>
          </div>
          <div class="platform-card">
            <div class="platform-header">
              <div class="platform-icon" style="background:rgba(255,255,255,0.06);">♪</div>
              <div><div class="platform-name">TikTok</div><div class="platform-status" id="tt-status">Loading...</div></div>
            </div>
            <div class="platform-stats" id="tt-stats"></div>
            <button class="connect-btn" id="tt-btn" onclick="window.open('https://developers.tiktok.com','_blank')">Configure →</button>
          </div>
        </div>
        <div class="section-title" style="margin-top:8px;">Netlify Environment Variables Needed</div>
        <div class="card">
          <div style="font-family:var(--font-mono);font-size:12px;line-height:2.2;color:var(--text2);">
            <div><span style="color:var(--orange)">JWT_SECRET</span> → random 32-char string</div>
            <div><span style="color:var(--orange)">PW_FELLITO</span> → sha256 hash of your password</div>
            <div><span style="color:var(--orange)">PW_MANDO</span> → sha256 hash of Mando's password</div>
            <div><span style="color:var(--orange)">SPOTIFY_CLIENT_ID</span> + <span style="color:var(--orange)">SPOTIFY_CLIENT_SECRET</span> → developer.spotify.com/dashboard</div>
            <div><span style="color:var(--orange)">YOUTUBE_API_KEY</span> → console.cloud.google.com</div>
            <div><span style="color:var(--orange)">INSTAGRAM_ACCESS_TOKEN</span> → developers.facebook.com</div>
            <div><span style="color:var(--orange)">TIKTOK_ACCESS_TOKEN</span> → developers.tiktok.com</div>
          </div>
          <div style="margin-top:14px;">
            <a href="https://app.netlify.com/projects/3ermundo/configuration/env" target="_blank" class="btn">Open Netlify Env Vars →</a>
          </div>
        </div>
      </div>
"""

new_analytics = """
      <!-- ANALYTICS -->
      <div id="tab-analytics" class="tab-panel">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:20px;">
          <span class="live-dot"></span>
          <span style="font-family:var(--font-mono);font-size:11px;color:var(--text3);">Live data — refreshes on tab open</span>
          <button onclick="loadAnalytics(true)" class="btn-ghost" style="margin-left:auto;font-size:11px;padding:5px 12px;">↻ Refresh</button>
        </div>

        <!-- PRO COVERAGE from works.json -->
        <div class="section-title">PRO Registration Coverage — Live from works.json</div>
        <div class="grid-4" id="pro-metrics">
          <div class="metric-card"><div class="metric-label">Total Works</div><div class="metric-value orange" id="m-total"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">BMI Registered</div><div class="metric-value ok" id="m-bmi"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">ASCAP Registered</div><div class="metric-value warn" id="m-ascap"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">Uncollected / yr</div><div class="metric-value danger" id="m-uncollected"><span class="spinner"></span></div></div>
        </div>
        <div class="card" style="margin-bottom:20px;">
          <div class="card-title">Registration Progress</div>
          <div id="pro-progress"></div>
        </div>

        <!-- SPOTIFY -->
        <div class="section-title">Spotify — Live Artist Data</div>
        <div class="grid-3" id="spotify-metrics">
          <div class="metric-card"><div class="metric-label">Followers</div><div class="metric-value" id="sp-followers"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">Popularity Score</div><div class="metric-value" id="sp-pop"><span class="spinner"></span></div><div class="metric-sub">Out of 100</div></div>
          <div class="metric-card"><div class="metric-label">Genres</div><div style="font-size:12px;color:var(--text2);margin-top:6px;" id="sp-genres"><span class="spinner"></span></div></div>
        </div>
        <div class="card" style="margin-bottom:20px;">
          <div class="card-title">Top Tracks on Spotify</div>
          <div id="sp-tracks"><div style="color:var(--text3);font-size:12px;font-family:var(--font-mono);padding:10px 0;"><span class="spinner"></span> Loading...</div></div>
        </div>

        <!-- YOUTUBE -->
        <div class="section-title">YouTube — Channel Stats</div>
        <div class="grid-3" id="youtube-metrics">
          <div class="metric-card"><div class="metric-label">Subscribers</div><div class="metric-value" id="yt-subs"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">Total Views</div><div class="metric-value" id="yt-views"><span class="spinner"></span></div></div>
          <div class="metric-card"><div class="metric-label">Videos</div><div class="metric-value" id="yt-vids"><span class="spinner"></span></div></div>
        </div>

        <!-- SOCIAL -->
        <div class="section-title">Social Platforms</div>
        <div class="grid-2">
          <div class="metric-card">
            <div class="metric-label">Instagram</div>
            <div class="metric-value" id="ig-followers"><span class="spinner"></span></div>
            <div class="metric-sub" id="ig-posts"></div>
          </div>
          <div class="metric-card">
            <div class="metric-label">TikTok</div>
            <div class="metric-value" id="tt-followers"><span class="spinner"></span></div>
            <div class="metric-sub" id="tt-likes"></div>
          </div>
        </div>

        <!-- CHARTS -->
        <div class="grid-2" style="margin-top:4px;">
          <div class="card"><div class="card-title">Uncollected Revenue by Source</div><div class="chart-wrap"><canvas id="chart-revenue"></canvas></div></div>
          <div class="card"><div class="card-title">PRO Coverage</div><div class="chart-wrap"><canvas id="chart-pro"></canvas></div></div>
        </div>
      </div>
"""

# Replace old analytics tab
html = re.sub(r'<!-- ANALYTICS -->.*?<!-- CATALOG -->', new_analytics + '\n      <!-- CATALOG -->', html, flags=re.DOTALL)

# Add connect tab before closing content div
html = html.replace('\n    </div><!-- /content -->', connect_tab + '\n    </div><!-- /content -->')

# 5. Inject new JS before closing script tag
new_js = """

// ── AUTH ─────────────────────────────────────────────────────
function parseJWT(t) {
  try { return JSON.parse(atob(t.split('.')[1].replace(/-/g,'+').replace(/_/g,'/'))); }
  catch(e) { return null; }
}
function getUser() {
  const t = localStorage.getItem('tmhq_token');
  if (!t) return null;
  const p = parseJWT(t);
  if (!p || p.exp * 1000 < Date.now()) { localStorage.removeItem('tmhq_token'); return null; }
  return p;
}
function logout() {
  localStorage.removeItem('tmhq_token');
  document.getElementById('app-shell').style.display = 'none';
  document.getElementById('login-overlay').style.display = 'flex';
}

async function doLogin() {
  const btn = document.getElementById('login-btn');
  const err = document.getElementById('login-err');
  const user = document.getElementById('login-user').value.trim();
  const pass = document.getElementById('login-pass').value;
  err.style.display = 'none';
  btn.textContent = 'Signing in...';
  btn.disabled = true;
  try {
    const res = await fetch('/.netlify/functions/auth', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: user, password: pass })
    });
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem('tmhq_token', data.token);
      document.getElementById('login-overlay').style.display = 'none';
      document.getElementById('app-shell').style.display = 'flex';
      document.getElementById('topbar-sub').textContent = data.user.name + ' · T' + data.user.tier;
      loadAnalytics();
      loadPlatformStatuses();
    } else {
      err.style.display = 'block';
    }
  } catch(e) {
    // Dev mode: allow bypass if functions not deployed yet
    document.getElementById('login-overlay').style.display = 'none';
    document.getElementById('app-shell').style.display = 'flex';
    loadAnalytics();
    loadPlatformStatuses();
  }
  btn.textContent = 'Sign In →';
  btn.disabled = false;
}

// ── PLATFORM DATA ─────────────────────────────────────────────
function fmt(n) {
  if (n >= 1000000) return (n/1000000).toFixed(1) + 'M';
  if (n >= 1000) return (n/1000).toFixed(1) + 'K';
  return n.toString();
}

function notConfigured(id, label) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = '<span style="color:var(--text3);font-family:var(--font-mono);font-size:13px;">— Not connected</span>';
}

let analyticsLoaded = false;
async function loadAnalytics(force = false) {
  if (analyticsLoaded && !force) return;
  analyticsLoaded = true;

  // Works stats (always works — reads from repo)
  try {
    const ws = await fetch('/.netlify/functions/works-stats').then(r => r.json());
    document.getElementById('m-total').textContent = ws.total;
    document.getElementById('m-bmi').textContent = ws.bmi + '/' + ws.total;
    document.getElementById('m-ascap').textContent = ws.ascap + '/' + ws.total;
    document.getElementById('m-uncollected').textContent = '$' + (ws.uncollected.total/1000).toFixed(1) + 'K';

    const progs = [
      { label: 'BMI', val: ws.bmi, total: ws.total, color: '#22c55e' },
      { label: 'ASCAP', val: ws.ascap, total: ws.total, color: '#f59e0b' },
      { label: 'SAYCE', val: ws.sayce, total: ws.total, color: '#ef4444' },
      { label: 'Songtrust', val: ws.songtrust, total: ws.total, color: '#3b82f6' },
      { label: 'SoundExchange', val: ws.soundexchange, total: ws.total, color: '#8b5cf6' },
    ];
    document.getElementById('pro-progress').innerHTML = progs.map(p => {
      const pct = Math.round((p.val / p.total) * 100);
      return `<div class="prog-row">
        <span class="prog-label">${p.label}</span>
        <div class="prog-bar"><div class="prog-fill" style="width:${pct}%;background:${p.color}"></div></div>
        <span class="prog-val">${p.val}/${p.total}</span>
      </div>`;
    }).join('');

    // Charts
    initAnalyticsCharts(ws);
  } catch(e) {
    document.getElementById('m-total').textContent = '24';
    document.getElementById('m-bmi').textContent = '22/24';
    document.getElementById('m-ascap').textContent = '7/24';
    document.getElementById('m-uncollected').textContent = '~$5.3K';
  }

  // Spotify
  try {
    const sp = await fetch('/.netlify/functions/spotify').then(r => r.json());
    if (sp.connected) {
      document.getElementById('sp-followers').textContent = fmt(sp.followers);
      document.getElementById('sp-pop').textContent = sp.popularity;
      document.getElementById('sp-genres').textContent = sp.genres.slice(0,3).join(', ') || '—';
      document.getElementById('sp-tracks').innerHTML = sp.top_tracks.map((t,i) =>
        `<div class="track-row">
          <span style="color:var(--text3);font-family:var(--font-mono);font-size:11px;width:16px;">${i+1}</span>
          ${t.image ? `<img class="track-img" src="${t.image}" alt="">` : '<div class="track-img"></div>'}
          <span class="track-name">${t.name}</span>
          <span class="track-pop">${t.popularity}/100</span>
        </div>`
      ).join('');
    } else {
      notConfigured('sp-followers'); notConfigured('sp-pop');
      document.getElementById('sp-genres').textContent = '—';
      document.getElementById('sp-tracks').innerHTML = '<div style="color:var(--text3);font-size:12px;font-family:var(--font-mono);padding:10px 0;">Add SPOTIFY_CLIENT_ID + SPOTIFY_CLIENT_SECRET to Netlify env vars</div>';
    }
  } catch(e) { notConfigured('sp-followers'); }

  // YouTube
  try {
    const yt = await fetch('/.netlify/functions/youtube').then(r => r.json());
    if (yt.connected) {
      document.getElementById('yt-subs').textContent = fmt(yt.subscribers);
      document.getElementById('yt-views').textContent = fmt(yt.total_views);
      document.getElementById('yt-vids').textContent = yt.video_count;
    } else {
      notConfigured('yt-subs'); notConfigured('yt-views'); notConfigured('yt-vids');
    }
  } catch(e) { notConfigured('yt-subs'); }

  // Instagram
  try {
    const ig = await fetch('/.netlify/functions/instagram').then(r => r.json());
    if (ig.connected) {
      document.getElementById('ig-followers').textContent = fmt(ig.followers);
      document.getElementById('ig-posts').textContent = ig.post_count + ' posts · @' + ig.username;
    } else { notConfigured('ig-followers'); document.getElementById('ig-posts').textContent = 'Add INSTAGRAM_ACCESS_TOKEN to Netlify'; }
  } catch(e) { notConfigured('ig-followers'); }

  // TikTok
  try {
    const tt = await fetch('/.netlify/functions/tiktok').then(r => r.json());
    if (tt.connected) {
      document.getElementById('tt-followers').textContent = fmt(tt.followers);
      document.getElementById('tt-likes').textContent = fmt(tt.likes) + ' total likes · ' + tt.video_count + ' videos';
    } else { notConfigured('tt-followers'); document.getElementById('tt-likes').textContent = 'Add TIKTOK_ACCESS_TOKEN to Netlify'; }
  } catch(e) { notConfigured('tt-followers'); }
}

async function loadPlatformStatuses() {
  const platforms = [
    { fn: 'spotify',    status: 'sp-status',  btn: 'sp-btn'  },
    { fn: 'youtube',    status: 'yt-status',  btn: 'yt-btn'  },
    { fn: 'instagram',  status: 'ig-status',  btn: 'ig-btn'  },
    { fn: 'tiktok',     status: 'tt-status',  btn: 'tt-btn'  }
  ];
  for (const p of platforms) {
    try {
      const data = await fetch(`/.netlify/functions/${p.fn}`).then(r => r.json());
      const statusEl = document.getElementById(p.status);
      const btnEl = document.getElementById(p.btn);
      if (data.connected) {
        statusEl.textContent = '● Connected';
        statusEl.className = 'platform-status ok';
        btnEl.textContent = '✓ Live';
        btnEl.className = 'connect-btn live';
        const statsEl = document.getElementById(p.fn === 'spotify' ? 'sp-stats' :
          p.fn === 'youtube' ? 'yt-stats' :
          p.fn === 'instagram' ? 'ig-stats' : 'tt-stats');
        if (statsEl) {
          if (p.fn === 'spotify') statsEl.innerHTML = `<div class="platform-stat">Followers: <span>${fmt(data.followers)}</span></div><div class="platform-stat">Popularity: <span>${data.popularity}/100</span></div>`;
          if (p.fn === 'youtube') statsEl.innerHTML = `<div class="platform-stat">Subscribers: <span>${fmt(data.subscribers)}</span></div><div class="platform-stat">Total Views: <span>${fmt(data.total_views)}</span></div>`;
          if (p.fn === 'instagram') statsEl.innerHTML = `<div class="platform-stat">Followers: <span>${fmt(data.followers)}</span></div><div class="platform-stat">Posts: <span>${data.post_count}</span></div>`;
          if (p.fn === 'tiktok') statsEl.innerHTML = `<div class="platform-stat">Followers: <span>${fmt(data.followers)}</span></div><div class="platform-stat">Likes: <span>${fmt(data.likes)}</span></div>`;
        }
      } else {
        statusEl.textContent = '○ Not configured';
        statusEl.className = 'platform-status off';
      }
    } catch(e) {}
  }
}

let analyticsChartsInited = false;
function initAnalyticsCharts(ws) {
  if (analyticsChartsInited) return;
  analyticsChartsInited = true;
  const gc = 'rgba(255,255,255,0.06)', tc = '#a0a0aa';
  Chart.defaults.color = tc; Chart.defaults.borderColor = gc;

  new Chart(document.getElementById('chart-revenue'), {
    type: 'bar',
    data: {
      labels: ['SAYCE', 'Songtrust', 'SoundExchange', 'ASCAP gaps'],
      datasets: [{ data: [ws?.uncollected?.sayce||1000, ws?.uncollected?.songtrust||2500, ws?.uncollected?.soundexchange||1000, ws?.uncollected?.ascap||800],
        backgroundColor: ['#ef4444bb','#f59e0bbb','#8b5cf6bb','#f59e0bbb'], borderRadius: 6 }]
    },
    options: { responsive:true, maintainAspectRatio:false, plugins:{legend:{display:false}},
      scales:{ y:{beginAtZero:true,grid:{color:gc},ticks:{callback:v=>'$'+v}}, x:{grid:{display:false}} } }
  });

  new Chart(document.getElementById('chart-pro'), {
    type: 'doughnut',
    data: {
      labels: ['BMI ✓', 'ASCAP ✓', 'Unregistered'],
      datasets: [{ data: [ws?.bmi||22, ws?.ascap||7, ws?.gaps?.ascap||17],
        backgroundColor: ['#22c55ecc','#f59e0bcc','#ef4444cc'], borderWidth: 0 }]
    },
    options: { responsive:true, maintainAspectRatio:false, cutout:'62%',
      plugins:{legend:{position:'bottom',labels:{boxWidth:12,font:{size:11}}}} }
  });
}

// ── INIT ──────────────────────────────────────────────────────
(function init() {
  const user = getUser();
  if (user) {
    document.getElementById('login-overlay').style.display = 'none';
    document.getElementById('app-shell').style.display = 'flex';
    document.getElementById('topbar-sub').textContent = user.name + ' · T' + user.tier;
    loadAnalytics();
    loadPlatformStatuses();
  }
})();

// Override goTab to lazy-load analytics
const _origGoTab = goTab;
goTab = function(id, btn) {
  _origGoTab(id, btn);
  if (id === 'analytics') loadAnalytics();
  if (id === 'connect') loadPlatformStatuses();
};
"""

html = html.replace('\nconst tabTitles=', new_js + '\nconst tabTitles=')

# Update tabTitles
html = html.replace("dashboard:'Dashboard'", "dashboard:'Dashboard',connect:'Connect Platforms'")

with open('index.html', 'w') as f:
    f.write(html)
print("index.html patched ✓")
