# Hidden Cost Tracker (prototype)

`build_tracker.py` → `Hidden-Cost-Tracker.xlsx` (English, dark theme; for Google Sheets / Excel).
`sheets_polish.gs` → one-time Apps Script for the Google Sheets master copy (buyers never run it).

Tabs: Dashboard · How to Use · Settings · Debts & Installments · Subscriptions · Chart Data.

Look & feel (v2, matches the polish level of top-selling Etsy trackers)
- Colour-coded "chips" on drop-downs (category, billing, debt type, flags, alerts) via conditional formatting.
- Dashboard: 8 KPI cards with captions, today's date card, Coming up (next 6 charges), Free trials with cancel-by,
  Debts ranked by real APR, Monthly money map, flag legend, 3 charts (income donut, spend vs potential savings
  with a By category / By subscription VIEW switch, real APR by debt).
- Tables: dark headers colour-coded by who fills them (blue = you, orange = calculated), banded rows,
  header filter buttons, one-line live summary above each table, row highlight for trials about to bill.
- 19 sample subscriptions and 8 sample debts so the charts look full.

Google Sheets master copy (needs a computer browser once)
1. Upload the xlsx to Drive → open → File › Save as Google Sheets.
2. Extensions › Apps Script → paste `sheets_polish.gs` → run `polishTemplate`.
   Adds real checkboxes (Auto-renew / Cancel it? / Free trial), filter bars (slicers), native dark charts,
   and warning-only protection on calculated cells.
3. Share as a `/copy` link in the buyer PDF.

Key formulas
- Real APR = stated APR if entered, else `RATE(total payments, -monthly payment, original amount) * 12` (estimate; excludes separately charged fees).
- Payments left = total − made, or `NPER` from APR, payment and balance ("Never" if the payment doesn't cover interest).
- Trial cancel-by = start date + trial days − 1; days left counted from `TODAY()`.
- Committed share = (loan + installment payments + subscriptions, per month) ÷ monthly income.
- Dashboard lists use hidden sort-key columns (value + ROW()/n) so ties don't repeat the same name.

Buyer guide PDF
- `node build_guide.mjs "https://docs.google.com/spreadsheets/d/<ID>/copy"` → `Hidden-Cost-Tracker-Access-Guide.pdf` (Letter, 4 pages, dark).
- Without a link it builds `...-DRAFT.pdf` with a red placeholder and a "DO NOT UPLOAD" mark.
- Seller setup steps (Chinese): `SETUP-zh.md`.
