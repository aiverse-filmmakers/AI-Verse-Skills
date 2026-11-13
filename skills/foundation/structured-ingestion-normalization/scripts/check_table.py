#!/usr/bin/env python3
"""Check a cleaned CSV table. Standard library only, Python 3.9+.

Usage:
  python3 check_table.py table.csv [--required a,b] [--key col] [--dates c,d] [--numbers e,f]

Reports problems with row numbers (the header is row 1) and exits 1 if any are found.
"""
import argparse
import csv
import re
import sys
from collections import defaultdict

ISO_DATE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")


def cols(value):
    return [c.strip() for c in value.split(",") if c.strip()] if value else []


def main():
    ap = argparse.ArgumentParser(description="Check a cleaned CSV table.")
    ap.add_argument("path")
    ap.add_argument("--required", default="", help="columns that must not be empty")
    ap.add_argument("--key", default="", help="column that must be unique")
    ap.add_argument("--dates", default="", help="columns that must be YYYY-MM-DD")
    ap.add_argument("--numbers", default="", help="columns that must be plain numbers")
    args = ap.parse_args()

    with open(args.path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        sys.exit("The file is empty.")
    header = [h.strip() for h in rows[0]]
    problems = []
    wanted = cols(args.required) + cols(args.key) + cols(args.dates) + cols(args.numbers)
    for name in dict.fromkeys(wanted):
        if name not in header:
            problems.append("Column not found: %s" % name)
    if len(set(header)) != len(header):
        problems.append("Duplicate column names in the header.")
    index = {name: i for i, name in enumerate(header)}
    seen = defaultdict(list)
    data_rows = 0

    for number, row in enumerate(rows[1:], start=2):
        if not any(cell.strip() for cell in row):
            problems.append("Row %d: empty row" % number)
            continue
        data_rows += 1
        if len(row) != len(header):
            problems.append("Row %d: %d columns, expected %d" % (number, len(row), len(header)))
            continue
        for i, cell in enumerate(row):
            if cell != cell.strip():
                problems.append("Row %d: stray spaces in %s" % (number, header[i]))
        for name in cols(args.required):
            if name in index and not row[index[name]].strip():
                problems.append("Row %d: %s is empty" % (number, name))
        for name in cols(args.dates):
            if name in index:
                value = row[index[name]].strip()
                if value and not ISO_DATE.match(value):
                    problems.append("Row %d: %s is not YYYY-MM-DD (%s)" % (number, name, value))
        for name in cols(args.numbers):
            if name in index:
                value = row[index[name]].strip()
                if value:
                    try:
                        float(value)
                    except ValueError:
                        problems.append("Row %d: %s is not a plain number (%s)" % (number, name, value))
        key = args.key.strip()
        if key in index and row[index[key]].strip():
            seen[row[index[key]].strip().lower()].append(number)

    for value, numbers in seen.items():
        if len(numbers) > 1:
            problems.append("Duplicate %s '%s' in rows %s" % (args.key, value, ", ".join(map(str, numbers))))

    print("Rows checked: %d" % data_rows)
    if problems:
        print("Problems: %d" % len(problems))
        for line in problems:
            print("  - " + line)
        sys.exit(1)
    print("No problems found.")


if __name__ == "__main__":
    main()
