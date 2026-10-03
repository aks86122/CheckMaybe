# Before You Click "Pay Later" (free mini guide)

Plan: `planning/2026-10-before-you-click-pay-later/01-plan.md`. Funnel: page 11 links to Hidden Cost Tracker.

| File | Use |
| --- | --- |
| `Before-You-Click-Pay-Later.pdf` | The product (12 pages, fillable list on page 10). Upload this to Gumroad / Beacons |
| `listing-gumroad.md` | Gumroad + Beacons copy (listing-copy skill) |
| `images/` | `gumroad/` cover + thumb, `beacons/` square, `instagram/` 5-slide carousel |
| `build_guide.mjs` → `add_fields.py` | Rebuild the PDF: `SHOTS=<dir> node build_guide.mjs && python3 add_fields.py` |
| `build_images.py` | Rebuild images from the page shots: `SHOTS=<dir> python3 build_images.py` |

Checked 2026-10-03: 12 pages, no overflow, 62 form fields on page 10 (tested by filling one), example rates match Hidden Cost Tracker (RATE), deferred-interest wording follows the CFPB pages cited on page 12.
