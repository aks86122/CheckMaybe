# Pixel check model files

The model (199MB) is not in git. To build the files the site needs:

1. `python export_onnx.py` (needs torch, transformers, onnx, onnxruntime): downloads haywoodsloan/ai-image-detector-deploy (Apache-2.0) and writes `det_int8.onnx`.
2. `python split_model.py det_int8.onnx ../model/`: 8 parts of 24 MiB (Cloudflare Pages allows 25 MiB per file) plus `manifest.json` with a SHA-256 per part.
3. Deploy `photo-check.html` (as `index.html`), `_headers` and `model/` together.

How the page uses them (`photo-check.html`, "Pixel check"):
- Only after the user presses "Run pixel check"; never for screenshots, designed graphics or files that already carry an AI marker.
- onnxruntime-web 1.20.1 from jsDelivr; the parts download one by one, each is checked against its SHA-256, and kept in the browser's Cache Storage (`pixel-check-v1`), so later visits download nothing.
- `_headers` turns on cross-origin isolation (COEP `credentialless`, so jsDelivr scripts still load), which lets the model use 4 threads. Without it, it runs on 1 thread (slower, still works).
- Resizing uses `resize.js` (PIL-compatible bicubic) on the full-size image; the browser's own canvas resize moved scores across the 0.97 line in testing.
- Shown only as "Strong AI-like patterns" (score ≥0.97) or "No strong AI-like patterns", never as a verdict. The score goes into feedback rows (`check.pixel`).

Third-party notice to keep on the site: model by haywoodsloan, Apache-2.0; onnxruntime-web, MIT.
