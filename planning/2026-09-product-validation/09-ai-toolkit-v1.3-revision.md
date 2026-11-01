# Can I Use This? v1.3 revision (2026-11-01)

Trigger: Etsy's updated Terms of Use (effective 16 Dec 2026) give Etsy and its partners a license to use Your Content to train AI. Founder asked to update the product (2026-11-01) so posts about it can link straight to Gumroad.

Sources (texts pasted by founder 2026-11-01; quotes and notes in `content/2026-11-01-etsy-ai-training-note.md`):
- Etsy Terms of Use, effective 16 Dec 2026, last updated 26 Oct 2026: §5 (Your Content list), §5.C (irrevocable, perpetual; AI training sentence), §6.E, §7, §11.G
- Etsy Privacy Policy (US English PDF), published 26 Oct 2026, effective 16 Dec 2026: §2 legitimate-interests row on AI training, objection right for "EEA, UK, and other countries", §7 Right to Object, §12 contacts
- Etsy US Regional Privacy Policy, last updated 26 Oct 2026 (page id 1146293244010; NOT the archived 1286798590693)

Changes (`products/build/ai-v1.3.json`, 34 pages):
- NEW p13 "Etsy's new Terms: your content and AI training": what you agree to; EEA/UK right to object (not a switch); US opt-outs don't list AI training; arbitration opt-out (11.G) and closing your account are separate; callout §6.E.
- p29 red flags: + not reading Etsy's section 5 license before uploading. p30 checklist: + know what the marketplace's terms let it do with uploads.
- p34 sources: + Etsy Terms of Use and Privacy Policies (checked 1 Nov 2026). To fit one page: OpenAI entry shortened (US version; note EEA/CH/UK differ), the two Etsy Seller Handbook articles merged into one entry (both URLs kept), shorter lead.
- Cover, meta, closing: version 1.3.
- Photo Check link on p30 made clickable after build (utm_campaign=cius-v13).

QA: build.sh, 0 failing pages (zoom p5 0.98, p12 0.9, p13 0.9, p34 0.9); p13, p30, p34 checked visually.
Listing: `products/can-i-use-this/listing-gumroad.md`, `listing-beacons.md`, `gumroad-fields.md` (v1.3, 34 pages). Bundle: 83 → 84 pages (`bundle.py`, `products/bundle/listing-gumroad.md`, images in `products/bundle/images/`).
Founder: upload `products/can-i-use-this/Can-I-Use-This-v1.3.pdf` on Gumroad (Can I Use This? and the bundle) and Beacons; paste the updated listing text; replace bundle images.
