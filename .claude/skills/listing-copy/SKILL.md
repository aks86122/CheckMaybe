---
name: listing-copy
description: Write or rewrite CheckMaybe product listing copy (Gumroad, Etsy, Beacons descriptions, summaries, receipt fields) using the house sales-page structure: hook, pain points, what it helps you do, what you get, how it works, FAQ, good to know. Use whenever a CheckMaybe product needs a sales page, product description or store listing, new or revised.
---

# CheckMaybe listing copy

Founder decision (2026-10-03): every product description follows this structure. First used for Hidden Cost Tracker (`products/hidden-cost-tracker/listing-gumroad.md`, "Description v2").

## Before writing
1. Read the product's own files in `products/<slug>/` (README, build script or PDF source, buyer guide) and any existing `listing-*.md`. Every feature, number and limit in the copy must come from there.
2. Check each number you plan to quote against the product itself (sheet value, PDF page). Example figures must be the product's made-up example rows and must say they are made up.
3. For legal/licensing toolkits, quotes from official sources must match the saved source word for word (see `templates/toolkit-product-template.md`).

## Structure (in this order)
1. **Hook** — one line that names the hidden cost or the question the buyer has. Then one or two sentences with a concrete example from the product.
2. **If you're tired of… / …this is for you** — 3 to 5 pain points, in the buyer's words, as • bullets.
3. **What [Product] helps you do** — 5 to 8 outcomes, each starting with ✔ and a verb, each tied to a real feature.
4. **What you get** — the actual files and tabs/pages, capacity, example rows. ✔ bullets.
5. **How it works** — 3 numbered steps from purchase to first result.
6. **Frequently asked questions** — 4 to 6 numbered Q&As: software needed, privacy, what it does not do, limits/expanding, format/currency, delivery (nothing shipped).
7. **Good to know** — disclaimers: estimates only / not financial, legal or tax advice (or "educational, not legal advice" for toolkits); what the numbers exclude; example data is made up; personal use, don't share or resell.

## Never
- Income or results claims ("make $5K", "$1K days"), testimonials we don't have, "students".
- "Total value $X" stacks, fake bonuses, countdowns, "only X left", limited-time discounts without a real end date.
- Superlatives we can't prove ("the best", "proven", "guaranteed").
- Telling the buyer what financial or legal choice to make.
- Markdown bold (`**`) inside paste-ready blocks: storefront editors don't render it. Bold the section headings by hand after pasting.

## Style
- Plain English, short sentences, second person ("you").
- Numbers as digits with units ($1,200, 24 payments, 29.8% APR).
- Same facts on every platform; if one listing changes, update the others.

## Platform fields
| Platform | Fields and limits |
| --- | --- |
| Gumroad | Name; Summary (one line, the "You'll get" line); Description (the structure above); Additional details (3–5 label/value rows: Format, Works in / Includes, Capacity or Best for, Language); Button text ≤26 characters; Receipt custom message ≤500 characters (what to open first, where to start, one disclaimer line) |
| Etsy | Title ≤140 characters, keyword-first; 13 tags ≤20 characters each, mark evidence vs assumption; Description = same structure, first sentence ≤160 characters with the main keywords; image plan |
| Beacons | Title, price, one short description (5–7 lines: hook, 3–4 ✔ outcomes, format line, disclaimer) |

## Output
- Save to `products/<slug>/listing-<platform>.md`. Keep earlier versions in the file, labelled v1, v2…, with the date and which one is live.
- In chat, give every paste-ready field in its own code block so the founder can copy it with one tap, then a short table of what changed from the previous version.
- Count characters for limited fields and write the count next to the heading.

## Check before handing over
- [ ] Every claim maps to a feature in the product files
- [ ] Every number re-checked against the product
- [ ] Example data labelled as made up
- [ ] No income claims, value stacks, fake urgency
- [ ] Disclaimer present in Description and Receipt message
- [ ] Field limits respected
