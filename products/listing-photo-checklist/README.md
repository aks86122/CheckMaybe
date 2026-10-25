# Listing Photo Checklist (free lead magnet, v1.0, 2026-10-25)

Funnel: free PDF on Gumroad ($0+, collects buyer emails) → free Photo Check tool → Can I Use This? (page 4 links to it).

| File | Use |
| --- | --- |
| `Listing-Photo-Checklist.pdf` | Upload to Gumroad. Built from `../build/photo-v1.0.json` with `../build/build.sh photo-v1.0`, then links added with pymupdf (tool URL with utm_source=gumroad&utm_medium=pdf, Can I Use This?, the five source URLs) |
| `listing-gumroad.md` | Gumroad copy and fields |
| `images/` | Gumroad cover and thumbnail, from `build_images.py` |

Checked 2026-10-25: 4 pages, QA 0 failing, 8 links in the PDF. Facts: Etsy pages checked 24 Oct 2026; tool behaviour from our own tests (`tools/photo-check/README.md`). `render.py` gained an optional `nokey` on the cover to hide the signal key (no signals in this product).
