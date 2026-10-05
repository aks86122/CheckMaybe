# Holiday Hidden Cost Tracker

Seasonal edition of Hidden Cost Tracker (dark green / gold / berry). Plan: `planning/2026-10-holiday-hidden-cost-tracker/01-plan.md`.

| File | Use |
| --- | --- |
| `Holiday-Hidden-Cost-Tracker.xlsx` | The tracker. Upload to Google Drive and save as Google Sheets to make the master |
| `holiday_polish.gs` | One-time polish for the master: locale, checkboxes, filter bars, dark charts, soft protection |
| `build_holiday.py` | Rebuilds the xlsx |

## Tabs
- **Dashboard**: budget, spent, left, gifts sorted; what holiday plans charge next month and the month after; highest real APR; trials ending soon; month-by-month table and chart; plans ranked by real APR; still to buy; how gifts were paid (chart).
- **Gift List**: recipient, relationship, gift, budget, actual cost, paid with, status. Marks gifts on a payment plan.
- **Holiday Payments**: price, payment, number of payments, every 2 weeks or monthly, first payment date, first payment at checkout. Works out total, extra cost, real APR (RATE, annuity-due when paid at checkout), last payment, payments left, and what each plan charges in each of 5 calendar months from Settings.
- **Free Trials**: start, trial days, price after, billing, cancelled. Cancel-by date, countdown, yearly cost if kept.
- **Settings**, **How to Use**, **Chart Data** (helper).

## Checked (2026-10-03, LibreOffice recalculation, 0 formula errors)
- Example plans: Dec 2026 $498.00, Jan 2027 $428.25, Feb–Apr $148.50 each.
- Real APR: pay-in-4 at checkout 0%; TV 12 × $59 on $649 = 16.4%; console 6 × $89.50 on $499 = 25.7% (matches numpy-financial).
- With Today set to Jan 8, 2027: watch 1 payment left (Jan 8 not yet paid), flights 2, TV 11, console 5; trials show Trial ended / Cancelled / OK correctly.

## Still to do (see plan timeline)
- ✅ Google master (2026-10-05): https://docs.google.com/spreadsheets/d/1KWwokhobH8ib60UvtkmG-2BDGjGJabm8K_BFTVcotKI/copy (anyone-with-link viewer). Set File › Settings › Locale to United States.
- ✅ Buyer guide: `node build_guide.mjs "<copy link>"` → `Holiday-Hidden-Cost-Tracker-Access-Guide.pdf`. Listing copy: `listing.md`.
- Listing images (Etsy 10 / Gumroad / Beacons).
