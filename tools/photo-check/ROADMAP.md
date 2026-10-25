# Listing Photo Check: where it can grow (draft 2026-10-24)

Rule for every step: build the next stage only when the current one shows demand (numbers below). Every rule shown in the tool comes from an official page with a check date.

## Stage 1: free photo check (now)
Single photos, in the browser. Job: bring sellers to the toolkits.
Small additions that make the free check better:
- HEIC preview (iPhone photos) and an iPhone test of what Safari's file picker keeps (location, camera data).
- Platform picker: Etsy / Instagram & Facebook / Pinterest / Gumroad. The "still for you to check" column changes per platform (Etsy unedited photo, Meta AI label, Pinterest "AI-modified" toggle).
- Each to-do links to the exact toolkit page, with UTM per to-do so we see which advice sells.
- Privacy fix button: remove location and design-app account IDs from a copy, keep AI markers (removing AI markers to dodge labels stays out).
Gate to stage 2: about 50 checks a week for 4 weeks, or people asking for batch / reports.

## Stage 2: Pro, sold like the PDFs (one-time, about US$9–15, to test)
Delivered as an offline HTML file (no hosting, no accounts), or bundled free with a toolkit.
- Batch: a whole listing folder at once, one summary table (which photo can be the unedited one, which need AI disclosure, which leak location).
- Listing photo record: PDF/CSV with each file's capture data, SHA-256 and check date, to keep in case a listing is questioned. Wording: a record, not legal proof.
- Printable / PDF preflight (fits digital sellers): page size Letter vs A4, image resolution inside the PDF, embedded fonts, file size limits per platform, preview pages present.
- Built-in reverse image search (TinEye API, about US$0.01–0.04 per search, key on a small backend; listing URLs only unless the user agrees to send a file).
- Original vs edited pair: show that an edited listing photo and its camera original are the same shot.
Gate to stage 3: steady Pro sales (for example 20+ a month) and requests that need an account.

## Stage 3: hosted app (only with proven demand)
Needs a backend, so: security review, founder approval, paid hosting (Replit or similar).
- Accounts and saved history per shop, team access.
- Video Content Credentials (C2PA also covers MP4).
- Trust-list check of signers.
- Alerts when a platform's AI or photo rules change.

## Not doing
- Guessing "AI or not" from pixels (unreliable; wrongly accuses real makers).
- Stripping metadata to avoid AI labels or disclosure.
- Scraping Etsy or other marketplaces (Etsy Terms 6.C).
- Accounts, payments or cloud storage before stage 3.
