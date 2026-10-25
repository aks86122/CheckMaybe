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
