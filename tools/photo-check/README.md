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

## Etsy listing images (founder download, 2026-10-24)
3 images saved from Etsy listings (`il_1140xN.<id>_<hash>.jpg`): 1140 × 1140, only an ICC color profile left; no EXIF, XMP or C2PA. So a buyer can't learn anything from a downloaded listing image. The tool now recognises Etsy file names and switches to buyer advice (read the AI disclosure, review photos, ask the seller for an unedited photo, report misleading AI images).

## v0.3 (2026-10-24): reverse image search + feedback
- Reverse image search box: paste a listing image address, open TinEye / Google Lens / Bing with it (link-out, nothing sent by us).
- "Was this result right?" under every result. Stored in the artifact's `db` collection `feedback` (rule: read/write `interact`; the prototype is private, so only the owner can open it). Each row: correct yes/no, what it really was (camera / edited / made with AI / edited with AI / screenshot / someone else's image / design / not sure), optional tool name and comment, and the check's findings (verdict, signals, format, size, camera yes/no, C2PA issuer, source types, tool names, file-name pattern). Never the photo, file name, location or account IDs.
- Read it with ArtifactData `list` on `feedback`. For the public site this needs our own store (e.g. a small form endpoint) and a privacy note; part of the security review.

## v0.3.1 (2026-10-25): search from each result
Every result now has "Is this image used somewhere else?": Copy image (PNG to clipboard, up to 2000 px) + Open Google Lens / TinEye / Bing, with paste/drag instructions; Etsy-named files point to the address box instead. In-site results are not possible for free: Google Lens has no official API, Bing Search APIs were retired on 2025-08-11, TinEye's API is paid per search and needs a backend for the key (Pro idea, see ROADMAP).

## v0.3.2 (2026-10-25): designed graphics
First feedback round (2 rows): Etsy image correct; a 1000 × 1500 PNG pin (Canva AI mascot, layout drawn by code) was rated wrong ("almost no data left", actually AI art). New rule: no camera data + a social-media size (Pinterest 1000×1500/2000×3000, Instagram 1080×1350/1080×1080, story 1080×1920, link preview 1200×630, landscape 1080×566, thumbnail 1280×720) on a PNG, or any non-square of those → "Looks like a designed graphic, not a photo" with a self-disclosure reminder. Still can't tell if the art inside is AI: that case goes to the AI-detector evaluation set. Suite now 25 files, all as expected.

## v0.4 (2026-10-25): optional pixel check
"Run pixel check" under each photo result (not for screenshots, designed graphics, or files with an AI marker). Runs an AI-image model in the browser; the photo is not uploaded. Shows "Strong AI-like patterns" only at score ≥0.97, otherwise "No strong AI-like patterns" with a "doesn't prove it's real" line. Feedback rows now carry the score (`tool_version` 0.4). Model hosting: 8 parts under 25 MiB for Cloudflare Pages, see `pixel-check/README.md`; the model is not in git.
Tested locally (headless Chromium): with and without cross-origin isolation, cache hit after reload (0 part downloads), browser scores match Python within 0.02 except one low-score AI image (0.37 → 0.27), 25-file suite unchanged, 390px layout OK.
The claude.ai artifact stays on v0.3: it can't host the model files. Not yet tested on a real Android phone or iPhone Safari.
