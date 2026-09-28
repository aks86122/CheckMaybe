# Hidden Cost Tracker (prototype)

`build_tracker.py` → `hidden-cost-tracker-prototype.xlsx` (English, dark theme; for Google Sheets / Excel).

Tabs: Dashboard · How to Use · Settings · Debts & Installments · Subscriptions.

Key formulas
- Real APR = stated APR if entered, else `RATE(total payments, -monthly payment, original amount) * 12` (estimate; excludes separately charged fees).
- Payments left = total − made, or `NPER` from APR, payment and balance ("Never" if the payment doesn't cover interest).
- Trial cancel-by = start date + trial days − 1; days left counted from `TODAY()`.
- Committed share = (loan + installment payments + subscriptions, per month) ÷ monthly income.

Verified 2026-09-28 with the `formulas` Python engine (LibreOffice Calc is not installed here): 0 errors; sample phone installment (1,200 over 24 × 67) → 29.8% APR; committed 1,377.32 of 4,200 = 32.8%; yearly savings from "Keep? = No" = 599.88.
