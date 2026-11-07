# AI detector models: first evaluation (2026-10-25)

Question: can a pixel-based AI detector add a useful signal to Listing Photo Check, without wrongly flagging real makers' photos?

## Test set (small, kept out of the repo)
| Group | Files | What they are |
| --- | --- | --- |
| Real photos | 15 | Founder's phone photos (originals, chat-app copies, resized, edited in Photoshop), 1 C2PA sample photo |
| AI images | 28 | 5 ChatGPT images, 1 Canva AI image, 1 brand image (AI), 21 CheckMaybe mascot images (Canva AI, one cartoon style) |
| Screenshots | 4 | Phone and computer screenshots |
| Designed pins | 2 | AI art plus text, rendered pins |

Every file was also tested as an "Etsy copy": longest side 1140px, JPEG quality 85.
Score = the model's probability for its AI label; flagged when ≥0.5.

## Results
| Model (license) | Real photos flagged (lower is better) | AI found | AI found, Etsy copy | Screenshots flagged |
| --- | --- | --- | --- | --- |
| haywoodsloan/ai-image-detector-deploy (Apache-2.0, SwinV2, 195M params) | **0/15** | **27/28** | **26/28** | 3/4 |
| Ateeqq/ai-vs-human-image-detector (Apache-2.0, SigLIP, 93M) | 4/15 (scores of 1.00) | 25/28 | 25/28 | 3/4 |
| umm-maybe/AI-image-detector (CC-BY-4.0, 2024) | 3/15 | 3/28 | 2/28 | 4/4 |
| dima806/ai_vs_human_generated_image_detection (Apache-2.0) | 0/15 | 2/28 | 2/28 | 0/4 |
| NYUAD-ComNets/NYUAD_AI-generated_images_detector (Apache-2.0) | 1/15 | 2/28 | 2/28 | 0/4 |

haywoodsloan, without the 21 mascots (one style, inflates the score): 6/7 AI found, 5/7 on Etsy copies. Misses: the brand AI JPG (0.13), and one ChatGPT image that dropped from 0.99 to 0.02 after Etsy-style compression.

## What this means
- Only haywoodsloan is worth keeping. The others either miss most AI images or call real photos AI with full confidence (Ateeqq), which is the failure we must avoid.
- Even haywoodsloan flags screenshots and designed graphics as AI. The tool already identifies these first (screenshot and designed-graphic rules), so the model must never run as the verdict for them.
- 15 real photos from mostly one phone is far too few to promise a false-alarm rate. Real product photos from other phones, studio lighting and white backgrounds are untested.
- Compression can erase the signal (one ChatGPT image), so "low" never means "not AI".

## Recommendation
1. Use haywoodsloan only as a supporting signal, worded "Pixel check: looks AI-made (low / medium / high)", never as the main verdict, and only when there is no stronger evidence (C2PA, AI metadata, screenshot, designed graphic).
2. Show it after the metadata verdict, with the line "Pixel checks can be wrong, especially on compressed or edited photos."
3. Size problem: 195M params ≈ 200MB as int8 ONNX. Too heavy to load on every visit. Options: (a) optional "Run pixel check" button that downloads the model once (browser, no server), (b) hosted inference (needs a backend: stage 3 security review and founder approval). Start with (a) after an ONNX export and browser speed test.
4. Before showing it to anyone: test at least 100 real product photos (different phones, white backgrounds, studio light) and 50 more AI images from tools other than ChatGPT/Canva (Midjourney, Gemini, Flux). Gate: real photos flagged ≤2%.
5. Feedback rows (tool v0.3) should store the pixel score so wrong calls can be counted.

Not changed: ROADMAP "Not doing" still bans a pixel guess as the verdict.

## Round 2: 88 more real photos (2026-10-25)
Founder added 88 phone photos (one phone, Jul–Oct 2026): food, objects, streets, receipts, indoor and night shots. Each tested 3 ways: original, Etsy copy (1140px, q85), and a typical seller edit (square crop, +15% brightness, +10% contrast, q90). Top 3 models only.

| Model | Original flagged | Etsy copy flagged | Seller edit flagged |
| --- | --- | --- | --- |
| haywoodsloan | 1/88 | 2/88 | 1/88 |
| Ateeqq | 2/88 | 2/88 | 5/88 |
| umm-maybe | 3/88 | 2/88 | 4/88 |

haywoodsloan flagged 3 different photos (3/88 = 3.4% in at least one version), with high scores (0.92–0.96), so a "medium" band would not hide them:
- a backlit harbour scene (flagged as the original and the Etsy copy)
- a hand holding a printed receipt (text-heavy, like the screenshots in round 1; Etsy copy only)
- a food tray (only after the brighten/crop edit)
The same photo can flip between 0.01 and 0.96 depending on compression or a small edit.

Thresholds, haywoodsloan, all checks so far (294 real checks, 56 AI checks incl. Etsy copies):

| Flag when score ≥ | Real checks flagged | AI found | AI found, mascots left out |
| --- | --- | --- | --- |
| 0.5 | 4/294 | 53/56 | 11/14 |
| 0.95 | 1/294 | 51/56 | 9/14 |
| 0.97 | 0/294 | 48/56 | 9/14 |
| 0.99 | 0/294 | 44/56 | 6/14 |

## Updated recommendation
- Show the pixel check only as one line, only when the score is ≥0.97: "Pixel check: strong AI-like patterns. Pixel checks can be wrong." Below 0.97 show nothing (not "looks real").
- 0.97 was picked on this same set, so it is tuned to these photos. The real false-alarm rate on other people's photos is unknown; the false alarms sat at 0.92–0.96, just under the line.
- Never run it on screenshots, receipts or documents, or designed graphics (text-heavy images trigger it). The tool already detects screenshots and graphics; photos of printed text are not detected yet.
- Before launch: photos from at least 3 other phones (iPhone included) and 50 AI images from other generators. Keep the 0.97 line only if real photos stay at 0 flagged.
- Store the pixel score in feedback rows to keep measuring after launch.

## Round 3: in the browser (2026-10-25)
Model: haywoodsloan exported to ONNX and quantized to int8 (`pixel-check/export_onnx.py`): **199MB** (fp32 was 783MB). Run with onnxruntime-web 1.20.1 (WASM, multi-threaded) in headless Chromium on a 4-core cloud machine. Phone speed was simulated with Chrome's CPU slowdown (x4 ≈ mid-range phone, x6 ≈ older phone); no real phone or Safari tested yet.

Accuracy after int8: on 274 checks the score moved 0.009 on average. At the 0.97 line: real photos flagged 0/206 (same as full model), AI found 49/56 (full model 48/56).

| Setup | Model start (once per visit) | One photo |
| --- | --- | --- |
| Desktop, 4 threads | 7.5s | about 1.1s (first run 1.9s) |
| Desktop, 1 thread | 4.2s | about 2.9s |
| Mid-range phone (CPU x4) | 25s | about 3.4s |
| Older phone (CPU x6) | 36s | about 4.7s |
| WebGPU | not measurable here (cloud machine has no real GPU) | |

Download of 199MB, first visit only (then kept in the browser cache): about 16s at 100Mbps, 55s at 30Mbps, 2.5 min at 10Mbps.
Memory: about 200MB for the model on top of the page; risky on older iPhones (Safari closes heavy tabs).
A pre-optimized model starts faster (1.3s desktop, 5.6s at CPU x4) but is 326MB to download. Not worth it.

Preprocessing matters: the browser's own canvas resize moved scores enough to cross the 0.97 line (0.994 → 0.973). A PIL-compatible bicubic resize in JavaScript (`pixel-check/resize.js`) brings browser scores back in line with Python (0.983/0.983, 0.994/0.994, 0.999/0.999).

### What this means
- Desktop: fine as an opt-in button ("Run pixel check, 199MB one-time download"), about 10s the first time after the download, about 1s per photo afterwards.
- Phones: possible but slow (about 30–40s before the first result, plus the download). Offer it on desktop by default; on phones show the button with the size and time warning.
- Hosting: one 199MB file does not fit Cloudflare Pages (25MB per file) or GitHub Pages (100MB per file). Options: split into 9 parts under 25MB and join them in the browser, or host the file on Hugging Face (needs an account and founder approval to publish).
- Still to test: a real Android phone and an iPhone (Safari memory), and the cache surviving a second visit.
