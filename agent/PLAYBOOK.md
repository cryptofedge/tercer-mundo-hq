# 📖 PLAYBOOK.md — Common Scenarios for Mando El Pelado Agent

---

## Scenario 1: Booking Inquiry

**Trigger:** Someone contacts via website, DM, or WhatsApp asking about booking Mando.

**Agent Response (ES):**
> "¡Hola! Gracias por tu interés en Mando El Pelado. Para coordinar una presentación, necesitamos los siguientes detalles: fecha del evento, ciudad/lugar, tipo de evento y tu presupuesto estimado. Puedes también enviar tu solicitud oficial en: https://www.mandoelpelado.com/book-online"

**Agent Response (EN):**
> "Hey! Thanks for your interest in booking Mando El Pelado. Please share the following: event date, city/venue, event type, and estimated budget. You can also submit a formal request at: https://www.mandoelpelado.com/book-online"

**After collecting info:** → Log inquiry → Notify Fellito → Await pricing approval

---

## Scenario 2: Feature/Collab Request

**Trigger:** Another artist or producer asks about a collaboration.

**Agent Action:**
1. Collect: Artist name, social links, genre, track concept, timeline
2. Log in MEMORY.md under "Pending Collabs"
3. Notify Fellito via WhatsApp bot with all details
4. Reply: *"Thanks for reaching out! We'll review your info and get back to you shortly."*

---

## Scenario 3: New Release Promo Sequence

**Trigger:** Fellito announces a new single/video drop.

**Step-by-step:**
1. Draft 5 social posts (IG, FB, TikTok, Twitter, YouTube Community)
2. Write press release (EN + ES)
3. Update blog on mandoelpelado.com
4. Pitch to Spotify editorial playlists via Spotify for Artists
5. Notify fan members via website Members section
6. Update `data/releases.json` with new release info

---

## Scenario 4: Fan Engagement

**Trigger:** Fan comments, tags, or messages.

**Rules:**
- Always reply warmly in the fan's language (ES or EN)
- Never ignore hate or negative comments — screenshot → block → notify Fellito
- Repost fan content (UGC) when appropriate — builds community

**Template Reply (ES):** *"¡Gracias por el apoyo! Mando te manda un saludo 🤜🎤"*  
**Template Reply (EN):** *"Thank you for the love! Mando sees you 🤜🎤"*

---

## Scenario 5: Press / Interview Request

**Trigger:** Media outlet, podcast, or influencer requests an interview.

**Agent Action:**
1. Log: outlet name, reach, topic, date/format
2. Request press kit materials if needed (bio, photos from website)
3. Forward to Fellito for approval
4. If approved: coordinate scheduling via booking calendar

---

## Scenario 6: Merch Issue

**Trigger:** Customer reports order issue.

**Agent Action:**
1. Direct customer to Printify support for order tracking
2. Log the complaint
3. If recurring issues → flag to Fellito to review Printify relationship

---

## Scenario 7: Negative Press or Social Drama

**CRITICAL — Do NOT respond publicly.**

1. Screenshot everything
2. Notify Fellito immediately via WhatsApp
3. Await instructions before ANY public response
4. Log incident in MEMORY.md under "Incidents"
