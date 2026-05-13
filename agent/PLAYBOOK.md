# 📖 FEDGE 2.O — Playbook

## Scenario 1 — New Release
1. Collect: title, features, release date, ISRC
2. Register: BMI → ASCAP → SAYCE → Songtrust
3. Add to data/works.json + data/releases.json + PRO.md
4. Create SimpleTix event (if tied to show)
5. Create Monday.com release card with milestones
6. Notify T3 + T1 via WhatsApp

## Scenario 2 — Booking Request
1. Log bookings.json status: inquiry
2. Create Monday.com booking card
3. Alert T3 within 1 hour
4. If accepted → send SimpleTix draft + Booking Contract
5. On signed contract → update status: signed

## Scenario 3 — PRO Gap Detected
1. Flag in rights/CATALOG_AUDIT.md
2. Open registration portal deep-link
3. Alert Fellito (T5) via WhatsApp
4. Log in agent/MEMORY.md

## Scenario 4 — Google Drive Sync
1. PDF in PRO & Rights/ → parse → append data/royalties.json
2. PDF in Bookings/ + "signed" → update bookings.json status: signed
3. New audio in Releases/ → log asset; notify T4
4. Log all actions in MEMORY.md

## Scenario 5 — Crisis / Bad Press
1. Alert Fellito (T5) immediately
2. Do NOT post on artist socials
3. Draft 2 responses (public + private)
4. T5 approves before any action
5. Log in MEMORY.md
