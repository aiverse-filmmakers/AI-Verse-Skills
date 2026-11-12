#!/usr/bin/env python3
"""Deterministic 30/60/90 day cash forecast. Standard library only, Python 3.9+.

Usage: python3 cash_forecast.py input.json
Input (JSON):
  as_of          "YYYY-MM-DD"
  opening_cash   number, optional (needed for the lowest point check)
  receivables    [{name, amount, due, mean_lag_days, stddev_days, payments_on_record}]
  payables       [{name, amount, due}]   (expand recurring costs into one row per date)
Rules (same as SKILL.md):
  expected receipt = due + mean lag
  band per receivable = stddev / mean lag; 5% when mean lag <= 1 day;
  30% when fewer than 3 payments on record; capped at 50%
  window band = amount weighted average of its receivables' bands
  low = inflows x (1 - band) - outflows; high = inflows x (1 + band) - outflows
"""
import json
import sys
from datetime import date, timedelta

WINDOWS = [("0-30", 0, 30), ("31-60", 31, 60), ("61-90", 61, 90)]


def band_for(r, flags):
    if r.get("payments_on_record", 0) < 3:
        flags.append("Thin data: %s has fewer than 3 payments on record; band set to 30%%." % r["name"])
        return 0.30
    lag = float(r["mean_lag_days"])
    if lag <= 1:
        return 0.05
    band = float(r["stddev_days"]) / lag
    if band > 0.50:
        flags.append("High variance: %s band capped at 50%%; treat its timing as unknown." % r["name"])
        return 0.50
    return band


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    as_of = date.fromisoformat(data["as_of"])
    flags, events = [], []
    for r in data.get("receivables", []):
        expected = date.fromisoformat(r["due"]) + timedelta(days=round(float(r.get("mean_lag_days", 0))))
        if expected < as_of:
            flags.append("Overdue: %s was expected %s; counted on day 0." % (r["name"], expected.isoformat()))
            expected = as_of
        events.append({"name": r["name"], "kind": "in", "amount": float(r["amount"]),
                       "date": expected, "band": band_for(r, flags)})
    for p in data.get("payables", []):
        due = max(date.fromisoformat(p["due"]), as_of)
        events.append({"name": p["name"], "kind": "out", "amount": float(p["amount"]), "date": due, "band": 0.0})
    events.sort(key=lambda e: (e["date"], e["kind"] == "in"))  # same day: money out first

    windows = []
    for label, lo, hi in WINDOWS:
        inside = [e for e in events if lo <= (e["date"] - as_of).days <= hi]
        inflow = sum(e["amount"] for e in inside if e["kind"] == "in")
        outflow = sum(e["amount"] for e in inside if e["kind"] == "out")
        band = (sum(e["amount"] * e["band"] for e in inside if e["kind"] == "in") / inflow) if inflow else 0.0
        windows.append({"window": label, "inflows": round(inflow, 2), "outflows": round(outflow, 2),
                        "net": round(inflow - outflow, 2), "band_pct": round(band * 100, 1),
                        "low": round(inflow * (1 - band) - outflow, 2),
                        "high": round(inflow * (1 + band) - outflow, 2)})

    result = {"as_of": as_of.isoformat(), "windows": windows, "flags": flags,
              "events": [{"date": e["date"].isoformat(), "name": e["name"], "kind": e["kind"],
                          "amount": e["amount"], "band_pct": round(e["band"] * 100, 1)}
                         for e in events if (e["date"] - as_of).days <= 90]}
    if "opening_cash" in data:
        expected = low = float(data["opening_cash"])
        worst = {"date": as_of.isoformat(), "expected": expected, "low": low, "after": "opening balance"}
        first_negative = None
        for e in events:
            if (e["date"] - as_of).days > 90:
                break
            if e["kind"] == "in":
                expected += e["amount"]
                low += e["amount"] * (1 - e["band"])
            else:
                expected -= e["amount"]
                low -= e["amount"]
            if low < 0 and first_negative is None:
                first_negative = {"date": e["date"].isoformat(), "low": round(low, 2), "after": e["name"]}
            if low < worst["low"]:
                worst = {"date": e["date"].isoformat(), "expected": round(expected, 2),
                         "low": round(low, 2), "after": e["name"]}
        result["lowest_point"] = worst
        result["first_negative"] = first_negative
        if first_negative:
            flags.append("Shortfall risk: low band cash first goes negative (%.2f) on %s after %s."
                         % (first_negative["low"], first_negative["date"], first_negative["after"]))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 cash_forecast.py input.json")
    main(sys.argv[1])
