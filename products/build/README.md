# CheckMaybe PDF build

Every CheckMaybe toolkit PDF is generated from a content JSON file with this shared design system (see `../../templates/toolkit-product-template.md` for the content rules).

| File | Purpose |
| --- | --- |
| `SCHEMA.md` | Page types and fields for a product JSON (cover, steps, cards, table, scenarios, snapshot, list, worksheet, hierarchy, sources) |
| `canva-v3.1.json`, `ai-v1.1.json` | Content of the two live products |
| `render.py` + `style.css` | JSON → HTML (CheckMaybe cream/brown/orange design, traffic-light signals) |
| `print.mjs` | HTML → A4 PDF with Playwright, plus layout QA: overflow, clipping, text overlap, safe-zone checks; small auto-fit (≥ 88%) |
| `build.sh <name>` | Full build: `<name>.json` → `<name>.pdf`, QA report, page PNGs, contact sheet |

New product: write `<name>.json` following `SCHEMA.md`, run `./build.sh <name>`, fix anything the report flags, then review the rendered pages visually before release.

## Listing images

`mk.py` + `shot.mjs` generate three 1280×720 listing images per product (exported at 2×, 2560×1440): cover, preview (4 interior pages) and featured (one page with numbered callouts). They reuse the product's own page renders (`mk/<name>-pNN.png`, 160 dpi from the built PDF). `pos.mjs` returns element positions on a page so callout markers can be placed precisely. Add a product entry to `PRODUCTS` in `mk.py`, then run `python3 mk.py && node shot.mjs`.
