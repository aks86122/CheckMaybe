# Photo Check website (Cloudflare Pages)

Files: `index.html`, `app.js`, `style.css`, `_headers`, plus `model/v1/` (8 model parts + `manifest.json`, built with `../pixel-check/split_model.py`, not in this repo).
`app.js` is the v0.7 page script (feedback through the Google Form, pixel check on, model at `model/v1/`).

`_headers`: COOP/COEP (credentialless) for 4-thread WASM, a Content-Security-Policy (scripts only from this site and cdn.jsdelivr.net, blob: for onnxruntime's worker, styles from Google Fonts, no framing, no form posts), nosniff, referrer policy, no camera/mic/location, and a 1-year cache on the versioned model folder.

Tested locally 2026-10-25 with `serve-local.cjs` (applies `_headers`), headless Chromium at 390px: cross-origin isolated, C2PA check of a ChatGPT image works, pixel check runs (strong AI patterns on a mascot image), the Google Form link is pre-filled, Inter font loads, no CSP errors.

Deploy repo: github.com/aks86122/checkmaybe-photo-check (private), branch main, pushed 2026-10-25 (commit 0a1cb20): index.html, app.js, style.css, _headers, model/v1/ (8 parts + manifest), THIRD-PARTY.md. Cloudflare Pages: connect this repo, no build command, output directory /.

Live 2026-10-25: https://checkmaybe-photo-check.pages.dev (Cloudflare Pages, auto-deploys main). Checked live: all security headers present, model parts served with 1-year immutable cache, headless Chromium 390px: cross-origin isolated, C2PA check works, pixel check 25.5s first run including the 199MB download, form link pre-filled, no console errors. Not yet tested on a real phone.

2026-10-25: founder tested on a computer and a phone. The claude.ai artifact now only says the tool moved, with a link to https://checkmaybe-photo-check.pages.dev (its earlier versions stay in the artifact's history).
