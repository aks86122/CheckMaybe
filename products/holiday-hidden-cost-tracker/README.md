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
- **Deal Check** (v1.1, 2026-10-24): item, sale price, usual price, tax, shipping, pay with, plan. Works out % below usual, total at checkout, plan total, extra on the plan and a verdict (Real deal / Small deal / Deal, but the plan costs more / Not a deal / Skip it / Find the usual price). Good-deal threshold in M4 (default 10%).
- **Settings**, **How to Use**, **Chart Data** (helper).

## Checked (2026-10-03, LibreOffice recalculation, 0 formula errors)
- Example plans: Dec 2026 $498.00, Jan 2027 $428.25, Feb–Apr $148.50 each.
- Real APR: pay-in-4 at checkout 0%; TV 12 × $59 on $649 = 16.4%; console 6 × $89.50 on $499 = 25.7% (matches numpy-financial).
- With Today set to Jan 8, 2027: watch 1 payment left (Jan 8 not yet paid), flights 2, TV 11, console 5; trials show Trial ended / Cancelled / OK correctly.

## v1.1 check (2026-10-24, LibreOffice recalculation, 0 formula errors)
- Headphones $199 vs $249: 20.1% below, $214.92 at checkout, Real deal. Air fryer $89 vs $89: Not a deal. TV $499 vs $549 on 12 × $49: $538.92 vs $588, extra $49.08. Smart watch 6.7% below: Small deal. Robot vacuum $186.72 at checkout: Real deal. Scooter, Need it = No: Skip it. Other tabs unchanged.
- Founder OK 2026-10-24 (option A). Done: buyer guide source (Seven tabs, Deal Check row), listing text v1.1 in all three listing files.
- 2026-10-24: Deal Check tab written to the Google master (index 6, before Chart Data) and How to Use rows 13–14 added. Read back: 6 items checked · 2 real deals · 1 not a deal · plans add $61; every row matches the LibreOffice check. Guide PDF rebuilt (Seven tabs). The /copy link is unchanged, so the old PDF already copies the new tab.
- Existing buyers' copies don't update by themselves: tell them to make a fresh copy from the same link.
- 2026-10-24: founder pasted the v1.1 text and new PDF on Gumroad (checked on the live page: Deal Check lines present). Still old: Product tab "Includes" field. Beacons text v1.1 not pasted yet. Not on Etsy.

## Still to do (see plan timeline)
- ✅ Google master (2026-10-05): https://docs.google.com/spreadsheets/d/1wxzEeO6fx0MqJOv0SrB6MLGLvvn0hh80Hj-1qJ8dajQ/copy (anyone-with-link viewer). Polished with holiday_polish.gs (checkboxes, slicers, native charts, en_US locale) on 2026-10-05.
- ✅ Buyer guide: `node build_guide.mjs "<copy link>"` → `Holiday-Hidden-Cost-Tracker-Access-Guide.pdf`. Listing copy: `listing-gumroad.md`, `listing-etsy.md`, `listing-beacons.md` (house structure).
- Listing images (Etsy 10 / Gumroad / Beacons).
