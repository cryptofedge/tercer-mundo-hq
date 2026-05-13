# ⚙️ FEDGE 2.O — Task Schedule

> Runtime: OpenClaw / pm2 | Timezone: America/New_York

## On Every Session Open
- [ ] Connect to https://github.com/cryptofedge
- [ ] Load org/MEMBERS.md — identify member + tier
- [ ] Check MEMORY.md for last sync timestamps
- [ ] If PRO sync stale >7 days → trigger refresh
- [ ] Scan Google Drive for new files
- [ ] Check bookings.json for past-due approvals

## Weekly (Monday 9am ET)
- [ ] PRO sync: BMI + ASCAP → update data/royalties.json
- [ ] Notify artist (T1) if new statement available
- [ ] DSP snapshot: Spotify/Apple/YouTube → update ANALYTICS.md
- [ ] Catalog gap check → update rights/CATALOG_AUDIT.md
- [ ] OAuth token health: alert T5 if expiring within 7 days

## Monthly (1st, 10am ET)
- [ ] Revenue report per artist → export PDF to Google Drive
- [ ] Royalty aggregate: flag works with 0 earnings + >10k streams
- [ ] Agent audit export → Drive: Exec/Agent Logs/[YYYY-MM].md

## On New Release
- [ ] Register BMI → https://www.bmi.com/creators
- [ ] Register ASCAP → https://www.ascap.com/member-access
- [ ] Register SAYCE (Ecuador)
- [ ] Submit to Songtrust
- [ ] Add to data/works.json + artists/[name]/PRO.md
- [ ] Create Google Drive release folder
- [ ] Create Monday.com release card
- [ ] Notify T3 manager

## WhatsApp Bot Commands
| Command | Tier | Action |
|---------|------|--------|
| !sync pro | T5 | Force PRO sync |
| !royalties | T1+ | Show PRO balances (scoped) |
| !catalog | T3+ | Run gap audit |
| !onboard [name] [tier] | T5 | Begin onboarding |
| !tierset [id] [tier] | T5 | Change member tier |
| !booking [artist] [date] [venue] | T3+ | Create booking |
| !lang [code] | T1+ | Switch language |
| !status | T3+ | Org health summary |
