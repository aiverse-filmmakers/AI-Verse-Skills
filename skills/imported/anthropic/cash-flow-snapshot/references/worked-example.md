# Worked example — cash-flow-snapshot

Every number below is the real output of `scripts/cash_forecast.py` run on
`assets/example-input.json`. Run it yourself to check:

```bash
python3 scripts/cash_forecast.py assets/example-input.json
```

**Scenario:** small services business, today is 2026-04-22, $19,200 in the bank,
three open invoices, payroll on the 25th, rent and software on the 1st.

## Input

| Receivable | Amount | Due | Mean lag | Std dev | Payments on record |
|---|---|---|---|---|---|
| Acme Corp INV-112 | $8,400 | 2026-04-10 | 18 days | 4 days | 11 |
| BlueSky LLC INV-108 | $14,200 | 2026-04-22 | 7 days | 2 days | 8 |
| Crestwood Inc INV-115 | $6,000 | 2026-05-05 | 12 days | 5 days | 6 |

Payables: payroll $22,000 (Apr 25, May 25), rent $3,200 and software $480 (May 1, Jun 1).

## Timeline the script builds (expected receipt = due date + mean lag)

| Date | Item | In or out | Amount | Band |
|---|---|---|---|---|
| 2026-04-25 | Payroll | out | $22,000 |  |
| 2026-04-28 | Acme Corp INV-112 | in | $8,400 | 22.2% |
| 2026-04-29 | BlueSky LLC INV-108 | in | $14,200 | 28.6% |
| 2026-05-01 | Rent | out | $3,200 |  |
| 2026-05-01 | Software subscriptions | out | $480 |  |
| 2026-05-17 | Crestwood Inc INV-115 | in | $6,000 | 41.7% |
| 2026-05-25 | Payroll | out | $22,000 |  |
| 2026-06-01 | Rent | out | $3,200 |  |
| 2026-06-01 | Software subscriptions | out | $480 |  |

Band per receivable = std dev ÷ mean lag (Acme 4 ÷ 18 = 22.2%).

## Forecast

| Window | Inflows | Outflows | Net | Band | Low | High |
|---|---|---|---|---|---|---|
| 0-30 days | $28,600 | $25,680 | +$2,920 | 29.5% | -$5,504 | +$11,344 |
| 31-60 days | $0 | $25,680 | -$25,680 | 0.0% | -$25,680 | -$25,680 |
| 61-90 days | $0 | $0 | +$0 | 0.0% | +$0 | +$0 |

The window band is the amount weighted average of its receivables' bands.
Low = inflows × (1 − band) − outflows. Money going out is not banded.

## Risks the script flags

- Shortfall risk: low band cash first goes negative (-2800.00) on 2026-04-25 after Payroll.

That is the answer to "will I make payroll": expected receipts arrive three days
after the April 25 payroll, so the account dips to -$2,800 first.
The lowest point in the 90 days is -$11,984 (low band) on 2026-06-01, because no new
invoices are on the books for the second month. Say that plainly; do not hide it.

## Chat summary

```
Cash Flow Snapshot — 2026-04-22 to 2026-07-21
Source(s): QuickBooks, PayPal

            Expected    Low        High
30-day net: +$2,920    -$5,504    +$11,344
60-day net: -$25,680   -$25,680   -$25,680
90-day net: +$0        +$0        +$0

⚠ Risks flagged: 2
  • Payroll crunch: $22,000 payroll on Apr 25 lands before the Acme and BlueSky
    receipts (Apr 28 and 29). Low band cash that day: -$2,800.
  • No invoices on the books after May 17: days 31 to 60 are all money out.

This forecast is based on QuickBooks AR/AP and PayPal settlement history. It is
not a substitute for accounting advice — verify with your bookkeeper before
making financing decisions.
```
