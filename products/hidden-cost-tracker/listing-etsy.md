# Hidden Cost Tracker — Etsy listing (v1 draft, 2026-10-01)

Language: English, US buyers. Status: ready to paste once the final Access Guide PDF (with the real /copy link) exists. Not published.
Sources: `README.md`, `SETUP-zh.md`, `build_tracker.py`, `build_guide.mjs` (this folder); `planning/2026-09-debt-payoff-tracker/01-etsy-research.md` (R1) and `02-subscription-bnpl-research.md` (R2). House style: `products/can-i-sell-this/listing-gumroad.md`.

Buyer-facing text below is plain text on purpose (no bold). In section 3, copy everything between the two `---` lines exactly.

## 1. Title

Main title (127 / 140 characters):

```
Debt Payoff Tracker Google Sheets, Real APR Calculator, Subscription Tracker, Free Trial Cancel Dates, BNPL Installment Tracker
```

Why: "debt payoff tracker" is the highest-demand phrase we have evidence for (R1: Etsy autocomplete, 1,000+ items, 32 Bestseller badges on page 1). "Google Sheets" sits in 27 of 47 page-1 titles (R1). "Real APR" (0 page-1 titles mention interest or APR, R1), "free trial" (1 listing on page 1, R2) and "BNPL" (0 listings built for it, R2) are our differentiators.

Alternate title for a later A/B test (129 / 140 characters):

```
Debt Payoff Tracker Spreadsheet, Snowball Avalanche, Real APR, BNPL Installment, Subscription & Free Trial Tracker, Google Sheets
```

Why: tests whether the table-stakes "snowball / avalanche" wording (27 of 47 page-1 titles, R1) pulls more clicks than "Calculator" and "Cancel Dates". Uses "&" once only (Etsy limits some special characters to one use per title; confirm in the editor).

Run the main title first. Change only the title when switching, and give each version at least 30 days or a few hundred views before comparing.

## 2. Tags (13)

| # | Tag | Chars | Evidence |
| --- | --- | --- | --- |
| 1 | debt payoff tracker | 19 | Evidence: R1, Etsy autocomplete, 1,000+ items, 32 Bestsellers on page 1 |
| 2 | subscription tracker | 20 | Evidence: R2, real market, 42 listings on page 1, median ≈US$5.7 |
| 3 | bnpl tracker | 12 | Evidence: R2, offered by Etsy autocomplete; 0 page-1 listings built for BNPL (demand level unknown) |
| 4 | debt snowball | 13 | Evidence: R1, snowball/avalanche in 27 of 47 page-1 titles |
| 5 | debt avalanche | 14 | Evidence: R1, same as above |
| 6 | google sheets budget | 20 | Evidence: R1, Google Sheets/Excel in 27 titles, budget planner combined in 22 |
| 7 | bill tracker | 12 | Evidence: R2, 22 subscription listings say "bill"; BNPL search returns bill trackers |
| 8 | budget spreadsheet | 18 | Evidence: R2, BNPL search returns budget spreadsheets; R1, 22 combine budget planner |
| 9 | free trial tracker | 18 | Assumption: R2 shows the gap (1 listing mentions a free-trial countdown), not search volume |
| 10 | apr calculator | 14 | Assumption: R1 shows the gap (0 titles mention APR/interest), not search volume |
| 11 | interest calculator | 19 | Assumption: plain-English version of "APR" for buyers who don't use the term |
| 12 | installment tracker | 19 | Assumption: covers store financing / phone plans; not tested on Etsy |
| 13 | buy now pay later | 17 | Assumption: long form of "BNPL" for buyers who don't know the acronym |

All 13 are 20 characters or fewer, no two are the same phrase. Tags 1–8 have research behind them; 9–13 are bets on our differentiators. After 30 days, swap any of 9–13 that Etsy Stats shows with zero impressions.

## 3. Description

Paste from here:

---

Debt payoff tracker for Google Sheets that works out the real APR on your installment plans and BNPL, and counts down free trials before they charge you.

That $1,200 phone paid as 24 × $67 sounds cheap each month. It works out to about 29.8% APR. Store financing, pay-in-4 plans and "low monthly payment" deals rarely show the yearly rate, and free trials turn into charges when you're not looking.

Hidden Cost Tracker puts your debts, installments and subscriptions in one Google Sheet, so you can see how much of your income is already committed each month and which costs to deal with first.

What it does
• Real APR: enter the amount, the monthly payment and the number of payments, and it estimates the yearly interest rate. Know the stated APR? Enter that instead.
• HIGH / CHECK / OK flag on every debt (20% and 10% by default, change them in Settings).
• Payments left, debt-free date and interest still to pay.
• Payoff order both ways: avalanche (highest rate first) and snowball (smallest balance first).
• Subscriptions: monthly and yearly cost, next charge date and days until it hits.
• Free trials: cancel-by date and a countdown, with the row highlighted when a trial is about to bill.
• Tick "Cancel it?" on anything you plan to drop and see the yearly saving.

The Dashboard
• 8 cards: income, committed each month, share of income committed, left over, highest real APR, interest still to pay, free trials ending soon, yearly savings
• Next charges, free trials list and debts ranked by real APR
• Monthly money map
• 3 charts: income donut, spending vs potential savings (switch between By category and By subscription), real APR by debt
• Filters on the tables

What's included
• PDF access guide with your "Make a copy" link and setup steps
• Google Sheets tracker, dark theme, 5 tabs: Dashboard, How to Use, Settings, Debts & Installments, Subscriptions (plus a small Chart Data helper tab)
• Room for 20 debts and 30 subscriptions
• Made-up example rows so you can see how it works. Overwrite or delete them.

How it works
1. Download the PDF, click the link and choose "Make a copy". The tracker saves to your own Google Drive. A free Google account is all you need.
2. Add your monthly take-home pay in Settings, then your debts and subscriptions. Blue headers are yours to fill in. Orange headers calculate themselves.
3. Open the Dashboard to see your highest real APR, what's charging next and which free trials to cancel.

FAQ

Do I need Excel or paid software?
No. It's made for Google Sheets, which is free with a Google account, on a computer or in the Google Sheets app. Prefer Excel? Download your copy as .xlsx (File › Download › Microsoft Excel). The formulas still work, and tick boxes become Yes/No drop-downs.

Will anything be shipped?
No. This is a digital download. You get a PDF with the link to your copy of the tracker.

Is my information private?
Your copy lives in your own Google Drive. We can't see what you enter.

Can I track more than 20 debts or 30 subscriptions?
Yes. Insert a row inside the table, then copy the row above into it so the formulas come along. The PDF guide shows how.

My currency isn't US dollars.
Select the money columns and change the currency under Format › Number. The maths stays the same.

Good to know
• All figures are estimates to help you plan. This is not financial, legal or tax advice.
• Real APR is estimated from your payment schedule and does not include fees charged separately. Your loan or credit agreement is the final word.
• The tracker only uses the numbers you type in. It doesn't connect to your bank or cards and doesn't cancel anything for you.
• Example numbers in the photos are made up.
• For personal use. Please don't share or resell the template link.

How this was made
CheckMaybe planned the features, layout and test cases. AI tools helped write the spreadsheet formulas and the scripts that build the file, and every formula was checked against the example data before release.

---

End of description.

Snippet check: the first sentence is 156 characters, so it fits the ~160-character search/preview snippet and contains "debt payoff tracker", "Google Sheets", "real APR", "installment", "BNPL" and "free trials".

Consistency with the buyer PDF (`build_guide.mjs`): flags, Excel note, privacy line, row capacity, currency tip and personal-use line all match its wording. If the PDF changes, update this description too.

## 4. Listing settings

| Field | Suggested value | Status |
| --- | --- | --- |
| Category | Paper & Party Supplies › Paper › Calendars & Planners | Assumption. Before choosing, open 2–3 of the Bestseller listings from the saved "debt payoff tracker" page and copy the category breadcrumb they use |
| Type | Digital files | Fact |
| Who made it? | I did | Fact |
| What is it? | A finished product | Fact |
| When was it made? | Most recent option (2020–2026 or similar) | Check exact wording in editor |
| Attributes (if offered) | Planner type: budget / finance; Format or software: Google Sheets, Excel; Theme/colour: dark (black) | Assumption, depends on what the category shows |
| Personalization | Off | Fact |
| Quantity | 999 (digital, never runs out) | Fact; no "only X left" messaging |
| Digital file to upload | `Hidden-Cost-Tracker-Access-Guide.pdf` only (the final one, never the `-DRAFT` file) | Fact, per SETUP-zh.md step 3 |
| Optional second file | `Hidden-Cost-Tracker.xlsx` for Excel users | Founder decision. Not needed if the Google "Download as .xlsx" route is tested and works |
| Renewal | Manual for the first 4 months | Recommendation: avoids repeat US$0.20 fees if the test fails |
| Returns | Shop policy: no returns on digital items, but invite a message if something doesn't work | Set in shop policies, not in the listing |

Price recommendation: list at US$8 (range US$7–9).
Rationale: page-1 medians are about US$5.6 (debt payoff), US$5.7 (subscription) and US$4 (BNPL) (R1, R2); this one file covers all three plus the real-APR feature nobody else lists, which supports pricing above the median, while a new shop with zero reviews should stay at or below US$9. Final price: pricing analyst. Any launch discount should be a real Etsy sale with an honest end date, no fake countdowns.

## 5. Image plan (10 images)

Format: 4:3 landscape so Etsy's thumbnail crop doesn't cut text (about 3000 × 2250 px; confirm Etsy's current size guidance in the upload screen). Dark backgrounds to match the sheet. Big headline text, readable on a phone. Screenshots come from the real Google Sheets master copy with the made-up example rows. Add a small "Example data" label on every image that shows numbers.

| # | Headline text on the image | Screenshot needed | Notes |
| --- | --- | --- | --- |
| 1 | See what your debts and subscriptions really cost | Full Dashboard (KPI cards + charts) on a laptop mockup, with 3 small chips: "Real APR" · "Free trial countdown" · "Debt-free date" | Thumbnail. Must read at small size |
| 2 | That $1,200 phone plan? About 29.8% APR | Debts & Installments tab cropped to the "Phone installment plan" row: $1,200, $67, 24 payments, Real APR 29.8%, red HIGH chip | Confirm the sheet shows 29.8% before using the number |
| 3 | 8 numbers that show where your money goes each month | Dashboard KPI card row (all 8 cards) | |
| 4 | Know which debt to pay off first | Dashboard "Debts ranked by real APR" list + Avalanche/Snowball order columns from the Debts tab | |
| 5 | Never miss a free trial cancel-by date | Dashboard free trials list + Subscriptions tab with cancel-by date, countdown and the highlighted "about to bill" row | |
| 6 | Tick "Cancel it?" and see your yearly savings | Subscriptions tab with several "Cancel it?" boxes ticked + the yearly savings card | |
| 7 | Charts that update as you type | The 3 charts; show the By category / By subscription switch (two small side-by-side crops if needed) | |
| 8 | Your monthly money map | Monthly money map + "Coming up" next charges list | |
| 9 | Ready in 3 steps | Google "Make a copy" dialog, Settings tab (income cell), Dashboard, numbered 1–2–3 | Same 3 steps as the description |
| 10 | What's included | PDF guide cover + list: 5 tabs, room for 20 debts and 30 subscriptions, Google Sheets + Excel (.xlsx), dark theme, digital download. Footer line: "Estimates only. Not financial advice." | Final image doubles as the disclaimer |

Optional later: a 5–15 second screen recording ticking "Cancel it?" and watching the savings card change (Etsy listing video).

## 6. Evidence vs assumption, and next action

Evidence (from our saved Etsy page-1 research, 2026-09-28, Taiwan site, one page each):
- "debt payoff tracker" has real paid demand: 1,000+ items, 32 Bestsellers, median ≈US$5.6 (R1).
- Google Sheets and snowball/avalanche are expected by buyers (27 of 47 titles each, R1).
- No page-1 debt listing mentions APR or interest (R1); 1 subscription listing mentions a free-trial countdown (R2); 0 listings are built for BNPL (R2).
- Product facts and the 29.8% example come from the build script and buyer guide.

Assumptions (not yet tested):
- That buyers actually search "free trial tracker", "apr calculator", "interest calculator", "installment tracker", "buy now pay later" (we only know the gap exists, not the demand).
- The BNPL gap might mean low demand, not opportunity (R2 says only an Etsy test can tell).
- Category and attributes (not checked in the live Etsy editor).
- US$8 converts better than US$7 or US$9.
- Research is one search page each on the Taiwan Etsy site; US results and ranking may differ.

Risks to check before publishing:
- Excel route: the guide and this listing say a Google copy downloaded as .xlsx keeps working with Yes/No drop-downs. That was true for the openpyxl-built .xlsx; after `sheets_polish.gs` adds native Google checkboxes, the downloaded file may show TRUE/FALSE instead. Test one download in Excel (or attach the .xlsx as a second file) before going live.
- AI disclosure: the wording meets the "disclose in the description" rule as briefed; re-read Etsy's current Creativity Standards page once when listing, since the rules change.
- Upload only the final PDF; the DRAFT PDF has a placeholder link.

Smallest next action: make the Google Sheets master copy and /copy link (SETUP-zh.md steps 1–2), then take the screenshot for image 2 (the phone row showing 29.8% APR) and test the .xlsx download once.
