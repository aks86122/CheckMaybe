# Can I Use This? v1.2 revision (2026-10-24)

Trigger: Etsy's 22 October 2026 AI update. v1.1 page 19 (AI-written ebook) only said "disclose AI"; under the new rules AI-generated instructional e-books are not allowed on Etsy, so v1.1 was out of date.

Sources (official text pasted by founder 2026-10-24, Etsy blocks automated reads):
- Etsy Seller Handbook, "Important updates to AI use on Etsy", 22 Oct 2026 (article 1522733284810)
- Etsy Seller Handbook, "What's Etsy's Stance on AI Creations?", 22 Oct 2026 (article 1275449912004)
- Etsy Listing Image Requirements, last updated 22 Oct 2026 (policy 253962679005)

Changes (`products/build/ai-v1.2.json`, 33 pages):
- NEW p12 "Etsy's October 2026 AI rules": disclose AI in the description; not allowed = bot-generated listings, prompt bundles without the artwork, AI-generated functional instructions (patterns, recipes, plans, manuals, instructional e-books); digital downloads show a visual preview or excerpt (representative imagery only for items with no visual element); refunds/removal; reports not enforced at first; Etsy's note on California SB 1050 from 1 Jan 2027.
- p5 legend: "Etsy's current AI rules (October 2026)".
- p15 printable: step 2 = show a real preview in listing images.
- p20 AI-written ebook: watch 3 and step 3 = Etsy ban on AI instructional e-books.
- p25 prompts: Etsy prohibits prompt bundles separately from finished artwork (Stance on AI Creations).
- p28 red flags: + AI-written patterns/recipes/how-to on Etsy. p29 checklist: + real preview.
- p33 sources: 3 Etsy pages checked 24 Oct 2026; Creativity Standards kept (production partner disclosure, p14), shorter lead/closing; `.srcs` gap 3mm → 2mm (style.css, all products' sources pages).
- Cover and closing: version 1.2.

QA: build.sh, 0 failing pages (zoom p5 0.98, p12 0.9, p33 0.88), pages checked visually.
Listing: `products/can-i-use-this/listing-gumroad.md`, `gumroad-fields.md` (v1.2, 33 pages); bundle listing and images 82 → 83 pages.
Founder: upload `products/can-i-use-this/Can-I-Use-This-v1.2.pdf` on Gumroad (and Beacons), paste the listing text. The Gumroad Bundle uses the same product file.

## 2026-10-25: Photo Check link
p29 checklist: new item "I ran my listing photos through the free Photo Check (link below)" plus a FREE TOOL callout with checkmaybe-photo-check.pages.dev. The link is made clickable after the build (pymupdf `insert_link` on page 29, URL with utm_source=toolkit). Still 33 pages, QA: 0 failing. Version stays 1.2; the founder re-uploads the PDF on Gumroad.
