# Listing Photo Check (prototype v0.1, 2026-10-24)

Free tool idea (founder 2026-10-24): a photo check that leads to the toolkits. Private preview: https://claude.ai/artifact/3za29W5K4qVn7Lrjyxsjdg (owner only). Not deployed; public hosting needs founder approval and a security review first (uploads + production, CLAUDE.md hard limits).

What it does, all in the browser (no upload, no backend, no API):
- Reads EXIF/XMP/IPTC with `exifr` 7.1.3 (MIT, jsDelivr): camera, capture time, settings, software, GPS presence (never shows coordinates).
- Scans the file text for C2PA/JUMBF records, IPTC DigitalSourceType (`trainedAlgorithmicMedia`, `compositeWithTrainedAlgorithmicMedia`), generator names, editing apps. C2PA signatures are NOT verified (c2pa-web left for later).
- Verdict + three columns: in the file / what platforms can read / still for you to check, with links to Can I Use This? and Can I Sell This? (utm_source=photocheck).
- Limits shown on the page: missing data ≠ not AI, camera data ≠ never edited, can't predict labels.

Tested 2026-10-24 (Playwright, local): original phone photo → straight from camera; chat-app copy → almost no data left; Photoshop-tagged copy → edited; synthetic XMP + C2PA file → AI marker; GPS copy → location warning; text file and empty file → errors; 390px width, no horizontal scroll, no console errors. Founder's Drive files (2026-10-24): ChatGPT PNG → AI marker + C2PA written by "OpenAI Media Service API" (c2pa.created, c2pa.converted); an AI brand image saved as JPG → no data left (shows why missing markers ≠ not AI); LINE-saved life photo → no data left. Canva AI export not tested yet. Founder's own photos stay out of this repo.
