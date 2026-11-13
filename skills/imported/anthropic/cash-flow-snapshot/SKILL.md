---
name: cash-flow-snapshot
description: "Produces a 30/60/90-day cash flow forecast with confidence bands and named risk flags, from QuickBooks, PayPal, Stripe or Square data or a CSV upload. Delivers a chat summary and a spreadsheet. Use when the user asks \"forecast my cash flow\", \"will I make payroll\", mentions \"runway\", or says \"cash crunch\"."
license: Apache-2.0
compatibility: "Needs Python 3.9 or newer for the bundled calculator. Data comes from a QuickBooks, PayPal, Stripe or Square connection, or a CSV upload. Spreadsheet output uses the xlsx skill, with a CSV fallback."
metadata:
  source: "Adapted by AI-Verse from anthropics/knowledge-work-plugins (Apache-2.0). Modified; see SOURCE.json."
---

# Cash Flow Snapshot

Produces a 30/60/90-day cash flow forecast with percentage-variance confidence
bands and named risk flags. Delivers a two-part output: a concise chat summary
and a downloadable XLSX workbook.

**Quick start**

> "Will I make payroll next month?"

Claude pulls AR/AP and fixed costs from connected sources, calculates expected
inflows and outflows across 30, 60, and 90-day windows, applies confidence
bands based on each customer's historical payment variance, and flags specific
risks by name.

---

## Workflow

### Step 1 — Identify available data sources

Check which connectors are live. Try in this order:

1. QuickBooks — primary source for AR aging, AP, and fixed costs
2. PayPal — transaction history and settlement timing
3. Stripe — charge and payout history
4. Square — sales and payout history
5. CSV upload — fallback if no connector is connected

If no connector is live and no file is attached, ask the user to either connect
a source or upload a CSV (income/expense tabular data, any reasonable format).
Note which sources were used in the output — this affects confidence band width.

### Step 2 — Pull the data

**From QuickBooks:**
- AR aging report: customer name, invoice amount, invoice date, due date, days outstanding
- AP: vendor name, amount due, due date
- Recurring fixed costs: rent, payroll, subscriptions (look for recurring transactions)

**From PayPal / Stripe / Square:**
- Settlement history: transaction date, amount, settlement date
- Use settlement lag (transaction date → payout date) to compute each source's
  average and variance payment delay

**From CSV upload:**
- Parse as income/expense tabular data
- Required columns (flexible naming): date, amount, type (income or expense), description
- If columns are ambiguous, show the header row and ask the user to confirm mapping

### Step 3 — Compute historical payment timing

For each AR customer (or income source from CSV), calculate:
- **Mean payment lag** — average days from invoice/transaction date to receipt
- **Payment variance** — standard deviation of payment lag across last 6–12 payments
- Use variance to set confidence band width (see Step 4)

If fewer than 3 payments exist for a customer, use the population mean as the
point estimate and apply a ±30% variance band as the default. When running on
CSV data with sufficient history (≥3 payments per source), compute the band
from the actual payment variance — do not assume ±30%.

### Step 4 — Build the 30/60/90-day forecast

Produce three time windows: 0–30 days, 31–60 days, 61–90 days.

For each window, compute:

| Line | Method |
|---|---|
| Expected inflows | AR due in window, adjusted for mean payment lag |
| Expected outflows | AP due in window + fixed costs falling in window |
| Net cash position | Inflows − Outflows |
| Confidence band | ± weighted average payment variance as a % of expected inflows |

**Do not do this arithmetic by hand.** Write the pulled data to a JSON file in the
shape of `assets/example-input.json` and run:

```bash
python3 scripts/cash_forecast.py input.json
```

The script applies these rules, the same way every time:

```
expected receipt  = due date + mean payment lag
band per customer = stddev_days / mean_lag_days
                    (5% if mean lag ≤ 1 day; 30% if fewer than 3 payments; capped at 50%)
window band       = amount weighted average of its customers' bands
low  = inflows × (1 − band) − outflows
high = inflows × (1 + band) − outflows
```

Only money coming in is banded; bills and payroll are treated as fixed. Expand
recurring costs into one payables row per date. Pass `opening_cash` when the user
gives a bank balance: the script then reports the first date the low band goes
negative, which is the direct answer to "will I make payroll".

If Python is not available, say so, apply the same rules by hand, and mark the
forecast "calculated by hand, not machine checked".

### Step 5 — Flag named risks

Scan for conditions that push the low-band estimate negative or create a
liquidity crunch. For each risk found, produce a one-line flag:

- **Late-payer risk:** "Customer X historically pays 18 days late; that shifts
  their $8,400 invoice out of the 30-day window into day 48."
- **Payroll crunch:** "Payroll ($22,000) hits April 15. Low-band cash on hand
  April 14: $19,200. Shortfall risk: $2,800."
- **Thin data warning:** "Only 2 payments on record for Customer Y — confidence
  band set to default ±30%."
- **No-connector warning:** "Running on CSV data only — no real-time AP or
  recurring cost data. Confidence bands are wider than normal."

Limit to the top 5 risks by severity (largest dollar impact first).

### Step 6 — Deliver outputs

**Chat summary** (always):
```
Cash Flow Snapshot — [date range]
Source(s): [connectors used]

            Expected    Low       High
30-day net: $X,XXX     $X,XXX    $X,XXX
60-day net: $X,XXX     $X,XXX    $X,XXX
90-day net: $X,XXX     $X,XXX    $X,XXX

⚠ Risks flagged: [count]
  • [risk 1]
  • [risk 2]
  ...
```

**XLSX workbook** (always):
Use the xlsx skill if it is available. If not, deliver the three sheets as three
CSV files and say so. Produce a workbook with three sheets:

1. **Summary** — the 30/60/90 forecast table with confidence bands. Beneath
   each window row, expand inline sub-rows showing the individual transactions
   that make up its inflows (green) and outflows (red). This makes the estimates
   auditable without leaving the Summary sheet.

2. **Detail** — all transactions grouped by window, sorted by date within each
   group. Include a running net column (cumulative inflows minus outflows within
   the window) and a subtotal row at the bottom of each window showing total
   inflows, total outflows, and net. Grey out past transactions in a separate
   section at the bottom for reference. Ensure all three windows have rows even
   if one is empty — show a "No transactions in this window" placeholder row.

3. **Risks** — the flagged risks with dollar impact and affected window.

Save as `cash-flow-snapshot-[YYYY-MM-DD].xlsx`.

---

## Approval gates

No destructive actions — this skill is read-only. No approval gate required
before generating the forecast.

Remind the user after delivery:
> "This forecast is based on [sources listed]. It is not a substitute for
> accounting advice — verify with your bookkeeper before making financing decisions."

---

## Reference files

| File | Load when |
|---|---|
| `references/gotchas.md` | When a connector returns unexpected data or variance is extreme |
| `references/worked-example.md` | When modeling the output format for a new data shape |
| `scripts/cash_forecast.py` | Step 4, always |
| `assets/example-input.json` | The input shape the script expects |

---

## Project adjustments

If the current project has adjustments for this skill (currency, payroll dates, known fixed costs, customers who always pay late), apply them. Where they disagree with these instructions, the project's adjustments win.
