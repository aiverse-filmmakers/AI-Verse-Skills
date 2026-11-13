---
name: business-pulse
description: "Use when the user asks how the business is doing, wants a snapshot, a weekly summary or a Monday brief, or says \"what am I missing\" or \"catch me up on the business\". Produces a one-page business snapshot for a small business owner: cash position, sales trend, pipeline movement, this week's commitments, urgent watch-list items, and the single most important thing needing attention today. Pulls from whatever is connected (accounting, payments, CRM, calendar, email, chat) and from uploaded exports when nothing is."
license: Apache-2.0
compatibility: "Best with connected accounting, payments, CRM, calendar, email and chat tools. Works in a reduced form from uploaded or pasted exports."
metadata:
  source: "Adapted by AI-Verse from anthropics/knowledge-work-plugins (Apache-2.0). Modified; see SOURCE.json."
---

# Business Pulse

One prompt, one page. Pull live data from every connected tool, synthesize it into a single scannable brief, and surface the single most important thing to act on today. Do the work — don't ask the user to help find the data.

## Step 1 — Pull data in parallel

**Dispatch all connector calls in a single parallel batch.** `references/data_sources.md` maps each metric to the kind of tool that provides it. The tool names there are examples from one setup; use whichever connected tool does the same job. Do not pull serially; latency turns a 30-second skill into a painful wait.

Connectors to attempt simultaneously:

- **QuickBooks** — cash balance, MTD revenue, outstanding receivables, overdue invoices
- **PayPal / Square** — 7-day settlements, sales trend, failed/pending transactions
- **HubSpot** — pipeline by stage, deals moved/closed, deals gone cold, new leads
- **Google Calendar** — key meetings, deadlines, events this week and next 7 days
- **Gmail** — threads flagged urgent, customer complaints, time-sensitive requests
- **Slack / Teams** — urgent internal signals, threads needing owner attention
- **Intercom / Zendesk** — open tickets, escalations (if connected)
- **Shopify / Square** — fulfillment issues (if connected)

If a connector errors or returns no data, record it internally and move on. Never block the pulse on a single bad integration.

**Nothing connected?** Say so in one line and ask once for what the owner can share: a bank or accounting export, a payments export, a deal list, this week's calendar, or pasted figures. Build the pulse from those and mark every section without data "n/a". Never return an empty page without saying why.

**QuickBooks fallback**: if QBO returns an unexpected state (account not connected, sync pending, empty response), mark the Cash section "n/a — QuickBooks unavailable" and proceed. Do not retry or ask the user to reconnect.

**Email fallback**: if the email call errors, skip the Watch List section and note "Email unavailable" in the appendix — do not surface an error mid-pulse.

## Step 2 — Compute metrics

Read `references/thresholds.md` for red/yellow/green cutoffs. Compute:

- **AR aging** — open QuickBooks invoices grouped by days since due date (0–30, 31–60, 61+)
- **Pipeline coverage** — HubSpot weighted pipeline ÷ monthly revenue target
- **Revenue trend** — this month's QBO revenue vs. prior month (or 7-day PayPal/Square vs. prior 7 days)

Assign a 🟢/🟡/🔴 status to each section. If a source returned nothing, mark the metric "n/a" and note it in the appendix.

## Step 3 — Flag risks proactively

Scan for actionable items. Every risk entry must name a specific record and a next step — "some overdue invoices" is useless; "$3,400 from Acme Corp, 47 days overdue, no response since Mar 12" is actionable.

- QuickBooks invoices past due > 30 days — name customer, amount, days overdue
- HubSpot deals with no activity in 7+ days, or close date in past but still open
- Gmail threads marked urgent or containing "escalation," "complaint," "cancel," "refund"
- Failed or pending PayPal/Square transactions > $500

## Step 4 — Compose the output

Use the exact template in `references/output_template.md`. Include only sections where real data exists — omit headers for connectors that weren't available. Adapt depth to context: a casual "how are we doing" gets a fuller report; "quick snapshot before a call" gets a tighter one.

Cross-connector synthesis is where this skill earns its keep. If a Slack message connects to a stalled HubSpot deal, surface that link in the #1 Priority section. Synthesis is what makes the pulse more useful than checking each tool separately.

Writing rules:
- Numbers lead, words follow. Never write "revenue is healthy" — write "$43k this month, ▲ 8% MoM" and let the owner judge.
- Every number carries a delta vs. the prior period where available. Absolute snapshots (cash balance) still show WoW delta.
- Names and dollars, not adjectives. "$4,200 from Acme, 23 days overdue" beats "some concerning receivables."
- No filler. If a section has nothing worth reporting, write "No material changes" and move on.

## Step 5 — Export and share (once)

After presenting the pulse, offer once:
- "Want me to save this as a file?" (use Files connector if available)
- "Should I post this to your Slack?" (only if Slack is connected and the user confirms — Slack write requires explicit approval)

If they say yes, do it. If they say no or don't respond, move on — don't ask again.

## Scope variants

The owner may ask for a narrower cut:

- **"Just cash" / "financial check"** → only Cash & Finance + AR-related risks
- **"Pipeline only" / "deals check"** → only Pipeline section + stalled-deal risks
- **"Watch list" / "anything urgent"** → only Watch List + all risks, no metric sections
- **"Quick snapshot before a call"** → TL;DR + #1 Priority only, no full sections

## What not to do

- **Do not ask permission before pulling data.** If the skill was invoked, run it. Asking "should I check QuickBooks?" defeats the whole point. Reading connected sources needs no extra yes; posting, sending or saving anywhere always does.
- **Do not invent or estimate numbers.** If a source returned nothing, say "n/a" explicitly. Never fill a gap with guesswork.
- **Do not skip the delta.** A number without a comparison is a missed insight. If there's no prior-period baseline, say "(no prior baseline)" rather than omitting the field.
- **Do not surface connector errors mid-pulse.** Log them to the appendix. The pulse leads with what was delivered.

## Reference files

- `references/data_sources.md` — exact connector tool → metric mapping with fallbacks
- `references/thresholds.md` — 🟢/🟡/🔴 cutoffs, tunable per owner
- `references/output_template.md` — exact markdown structure; do not deviate
- `references/gotchas.md` — known failure modes (QB states, Gmail auth, Slack write)

## Project adjustments

If the current project has adjustments for this skill (revenue target, traffic light thresholds, which channels and customers matter, currency), apply them. Where they disagree with these instructions, the project's adjustments win.
