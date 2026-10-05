# Debt Payoff Planner

`build_planner.py` → `Debt-Payoff-Planner.xlsx` (English, dark theme like Hidden Cost Tracker; Google Sheets / Excel; any currency).

Part of the Debt Toolkit (`planning/2026-10-debt-toolkit/01-plan.md`). Logic adapted from the founder's own debt planner (prepayment rules, cash-flow order, high-risk first), made generic for any country.

## What it does that a plain snowball/avalanche sheet doesn't
| Feature | Why it matters |
| --- | --- |
| Early payoff rule per debt: Allowed / Allowed with a fee / Locked until a date / Not sure - ask lender | Prepayment fees and lock-ins exist in many countries (some loans and mortgages, fixed-rate break costs). "Not sure" and locks get minimums only until they unlock. |
| Fee check: fee vs interest you'd save at minimums | If the fee costs more, extra waits until the fee ends; if it's worth it, the fee is counted in the totals. |
| 0% / promo rate end date + APR after promo + Deferred interest? | Rate switches in the simulation. Smart clears deferred-interest debts before the deadline; any order that misses a deadline gets a warning (back-interest is not added to the totals). |
| Behind on payments? | Smart puts these first. |
| Cash-flow order | Frees monthly money fastest (minimum ÷ balance). Smart uses it when minimums take 35%+ of income. |
| Compare four orders side by side | Smart, Avalanche, Snowball, Cash-flow: debt-free month, interest, fees, first debt cleared. |
| One-time extra (bonus / tax refund) in a chosen month | |
| Blank-safe | Only Name, Balance, APR, Minimum are needed. Optional blanks = no fee, no lock, no promo, not behind. Blank rows anywhere are fine. |

## Tabs
Start Here · Plan (settings, compare, checks, payoff order, charts) · My Debts (12 rows) · Schedule (360 months, chosen order) · hidden Calc Smart / Calc Avalanche / Calc Snowball / Calc Cashflow.

## Engine (each Calc sheet, month by month)
1. Every debt with a balance pays its minimum (capped at what's due).
2. Extra = monthly budget − minimums of debts still open (+ one-time extra in its month).
3. Extra goes to the highest-ranked debt that is open and allowed to take extra this month (lowest rank among open, unlocked debts via `1/SUMPRODUCT(MAX(cond/rank))`; no MINIFS, so it also works in Excel 2016). Whatever it can't absorb rolls to the next one.
4. Interest = balance × APR ÷ 12, using the promo APR before the promo end and the after-promo APR from then on.
5. Fee charged if a fee debt is cleared before its fee end date.

Limits (stated in the sheet): no back-interest calculation, interest monthly at APR÷12, at most two debts take extra in the same month, 30-year horizon.

## Checked
- LibreOffice recalc: 0 formula errors (≈70k formulas).
- An independent Python simulation gives identical months, interest and fees for all four orders, on the sample data and on an edge-case copy (fee charged, lock date, blank row mid-table, APR blank, one-time extra in month 3, Avalanche selected).

## Still to do (needs a computer once)
- Upload to Drive → Save as Google Sheets → check charts and drop-downs → make the `/copy` link.
- Buyer guide: `node build_guide.mjs "<copy link>"` → `Debt-Payoff-Planner-Access-Guide.pdf` (master: https://docs.google.com/spreadsheets/d/1aAwr-2Z8s7axpqPHufyJ8z0-JK3JMnx0_E8O2Xu3GRE/copy, anyone-with-link viewer). Listing copy: `listing-gumroad.md`, `listing-etsy.md`, `listing-beacons.md` (house structure).
- Master copy: set File › Settings › Locale to United States so buyers see English month names.
