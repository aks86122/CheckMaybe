# Listing Photo Check (prototype v0.2, 2026-10-24)

Free tool idea (founder 2026-10-24): a photo check that leads to the toolkits. Private preview: https://claude.ai/artifact/3za29W5K4qVn7Lrjyxsjdg (owner only). Not deployed; public hosting needs founder approval and a security review first (uploads + production, CLAUDE.md hard limits).

Everything runs in the browser: no upload, no backend, no paid API.

## What it reads
- EXIF/XMP/IPTC with `exifr` 7.1.3 (MIT): camera, capture and save times, settings, software, GPS presence (coordinates never shown), maker notes.
- Content Credentials with the official `@contentauth/c2pa-web` 0.15.3 (MIT, inline WASM via jsDelivr `+esm`, ~12 MB, loaded only when a file has a C2PA record): signer (certificate issuer), each action's IPTC digital source type and software agent, invisible watermark action, ingredients, validation codes. Trust list not checked (signer name shown as written). If the library can't load, it falls back to a text scan and says the signature wasn't verified.
- IPTC Digital Source Type vocabulary mapped to plain words (camera capture … trainedAlgorithmicMedia = made with generative AI, compositeWithTrainedAlgorithmicMedia = edited with generative AI, screenCapture = screenshot).
- Consistency checks: image size vs size the camera recorded (cropped/resized), save time vs capture time (saved again later), missing maker notes, screenshot markers/names, screen-sized images without data, chat-app and app-export file names, design-app account IDs (hidden, flagged).

## Test suite (2026-10-24, 23 files, all as expected, no console errors, 390 px no horizontal scroll)
| File | Verdict |
| --- | --- |
| 2 ASUS phone originals | straight from camera |
| resized copy / re-saved copy | camera photo changed later (size changed / saved again later) |
| Photoshop-tagged copy | edited in Photoshop (+ size changed) |
| GPS copy | location warning |
| C2PA fixtures CA / XCA / E-sig (c2pa-rs) | credentials intact / changed after signing / signature broken |
| c2pa-rs sample1.png | edited in Lightroom, saved again later |
| ChatGPT PNG (founder) | AI: made with generative AI, gpt-image, signed by OpenAI OpCo, LLC, invisible watermark; certificate issue (likely expiry) shown amber, not as tampering |
| Canva AI PNG (founder) | AI: edited with generative AI, Canva AI, signed by Canva, credentials intact, account IDs flagged |
| Canva plain edits (UUID names) | no data, app-export name |
| LINE saves (13-digit / _NNN names) | no data, chat-app name |
| Android phone screenshot (+ Screenshot_ name copy) | screenshot (UserComment marker) |
| PC/chat screenshots 1920×1080 WebP | no data, screen-sized image |
| AI brand image saved as JPG | no data (known limit: markers lost) |
| Our own pin render PNG | no data |
Founder's photos and other people's screenshots are not in this repo.
