---
name: structured-ingestion-normalization
description: "Turn messy documents, pasted lists, exports, logs or web pages into one clean table, with every row traceable to its source and nothing invented. Use when the user says 'put these into a spreadsheet', 'clean up this export', 'extract the names, dates and amounts from these files', 'merge these lists', or 'fix the dates and duplicates in this CSV'."
license: MIT
compatibility: "Needs Python 3.9 or newer for the bundled checker, and a reader for the file types involved (PDF, Word, spreadsheets)."
metadata:
  tier: foundation
  owner: ai-verse
---

# Structured Ingestion and Normalization

Messy in, one clean table out, and proof that nothing was lost or made up on the way.

Three failure modes, worst first:

1. **Inventing a value to fill a blank.** It looks tidy and it is false.
2. **Dropping rows that do not fit.** Nobody notices until the totals are wrong.
3. **"Fixing" a value into a different one.** `03/04/2026` is March in one country and April in another.

## Hard rules

1. **Columns first.** Agree the table before extracting anything.
2. **Every row names its source:** file, plus page, line or row number.
3. **Empty means the source had nothing.** Never write "N/A", 0 or a guess. Doubt goes in a `needs_review` column, with the reason.
4. **The counts must add up:** rows found = clean + duplicates merged + rejected. Report all four.
5. **Never overwrite the original.** Write new files.
6. **Parse, do not read by eye,** whenever the input has structure (CSV, JSON, spreadsheets). Read by eye only what cannot be parsed.
7. **Keep the raw value** beside the cleaned one wherever cleaning could be wrong: ambiguous dates, amounts in mixed formats, merged names.

## Step 1 — Agree the columns

Look at 5 to 10 records, then propose the table. If the user already named the columns, skip the question.

| Column | Type | Required | Format | Example |
| --- | --- | --- | --- | --- |

Always add `source` and `needs_review`. Ask which column makes a row unique (an email, an invoice number): that is the duplicate key.

## Step 2 — Extract

One file, or at most 50 records, at a time. Fill `source` as you go, not afterwards.

## Step 3 — Clean

| Type | Rule |
| --- | --- |
| Date | `YYYY-MM-DD`. If day and month could be swapped, look for a value above 12 elsewhere in the same source to settle the order. Still unsure: keep the raw value and flag it |
| Money | Plain number, dot for decimals, no symbol. Currency in its own column. Decide `1.234,56` against `1,234.56` once per source, not per cell |
| Name | Trim and collapse spaces. Do not change capitals or split first and last name unless asked |
| Email | Lowercase, trimmed. Flag if there is no `@` |
| Phone | Digits and a leading `+` only. Never add a country code |
| Text | Trim. Keep the original language and spelling |
| Units | Convert only if asked. Keep the unit in its own column |
| Missing | Leave empty |

## Step 4 — Duplicates

- Same key: merge, and count it.
- Nearly the same (same name, different email): **flag, never merge.** The user decides.
- When two copies disagree on a field, keep the fuller one and flag the row.

## Step 5 — Check

```bash
python3 scripts/check_table.py clean.csv --required name,email --key email --dates invoice_date --numbers amount
```

It reports empty required cells, duplicate keys, dates that are not `YYYY-MM-DD`, amounts that are not numbers, rows with the wrong number of columns and stray spaces. Fix or flag everything it lists, then run it again until it passes or every remaining item is in `needs_review`.

For more than 100 rows, also re-read 10 random rows against their sources and report how many matched.

## Step 6 — Deliver

- The clean table
- A rejects file: rows that could not be used, each with a reason
- This summary:

```
Sources:        40 files
Rows found:     212  (clean 198, duplicates merged 9, rejected 5)
Needs review:   14 cells, listed in the needs_review column
Changed:        dates to YYYY-MM-DD, amounts to plain numbers
Spot check:     10 of 10 rows matched their source
```

## Never

| Never | Instead |
| --- | --- |
| Fill a blank with a likely value | Leave it empty and flag it |
| Skip a row that does not fit | Put it in the rejects file with a reason |
| Guess the day and month order | Settle it from the source, or keep the raw value |
| Merge "probably the same" people | Flag them |
| Report "done" without counts | Give the four counts |

## Project adjustments

If the current project has adjustments for this skill (column names, date and currency conventions, the duplicate key, where files are saved), apply them. Where they disagree with these instructions, the project's adjustments win.
