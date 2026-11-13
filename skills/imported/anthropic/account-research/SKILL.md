---
name: account-research
description: "Research a company or person and return a sourced briefing, or a call prep brief with attendees, agenda and questions. Use when the user says \"research [company]\", \"look up [person]\", \"who is [name] at [company]\", \"intel on [prospect]\", \"tell me about [company] before my call\", or \"prep me for my call with [company]\"."
license: Apache-2.0
compatibility: "Needs web search. Uses a connected enrichment tool, CRM, calendar, email, chat or call transcripts when present."
metadata:
  source: "Adapted by AI-Verse from anthropics/knowledge-work-plugins (Apache-2.0). Modified; see SOURCE.json."
---

# Account Research

Research a company or person and return a sourced briefing. When the user is getting ready for a meeting, turn it into a call brief.

## Hard rules

1. **Every fact carries a link and a date.** No link, no fact.
2. **"Not found" beats a guess.** Never estimate revenue, headcount, funding, tech stack or an email address. A field you could not source says "Not found".
3. **People: public professional information only.** Role, employer, career history, published work, public posts. No home address, family, health, private accounts or personal contact details.
4. **Recent means the last 90 days** unless the user says otherwise. Date every news item.
5. **Lead with the Quick Take.** The user reads the first three lines; the rest is backup.
6. **One page.** Cut before you pad.

## Step 1 — Work out the request

| The user says | Produce |
|---|---|
| "Research Stripe", "intel on acme.com" | Company briefing |
| "Look up John Smith at Acme" | Person, plus a short company profile |
| "Who is the CTO at Notion?" | Find the person holding the role, then the person briefing |
| "Tell me about Acme before my call", "prep me for my call with Acme" | Call brief (see **Call brief** below) |

If the name could be more than one company or person, ask one question naming the candidates. Do not guess.

## Step 2 — Search (always)

Run these, adapting to the request:

1. `"[Company]"` → homepage, about page
2. `"[Company] news"` → announcements in the last 90 days
3. `"[Company] funding"` → investment history
4. `"[Company] careers"` → hiring signals
5. `"[Person] [Company] LinkedIn"` → role and background
6. `"[Company] product"` and `"[Company] customers"` → what they sell and to whom

Prefer the company's own site, filings and reputable press over aggregator sites. When two sources disagree, show both and say which is newer.

## Step 3 — Connected tools (if any)

| If connected | Pull |
|---|---|
| Enrichment tool | Firmographics, verified contacts, tech stack, org chart |
| CRM | Prior relationship, past opportunities, known contacts, notes |
| Calendar, email, chat, call transcripts (call brief only) | The meeting, recent threads, open commitments, earlier calls |

Where a connected tool and the web disagree, prefer the tool for the fields it owns and say which source each fact came from. If nothing is connected, do not ask the user to connect anything; carry on with the web.

## Step 4 — Write the briefing

Use `references/research-template.md`. Two things make it useful, so never drop them:

- **Every news item says why it matters** for the user's outreach or meeting.
- **Every gap becomes a question.** What you could not find goes under "Unknown (Ask in Discovery)".

The "why they might need you" angle needs to know what the user sells. Take it from the project's adjustments or the conversation. If neither says, ask once, or leave the angle out and say so.

## Call brief

When the user is preparing for a meeting:

1. You need the company, the meeting type (discovery, demo, negotiation, check in) and who is attending. Take what the message and any connected calendar already give you, then ask for only what is missing, in one question.
2. Do Steps 2 and 3 for the company and for each attendee.
3. Write it with `references/call-brief.md`, which also says what to emphasise for each meeting type.

Anticipated objections and discovery questions come from what you found and what you could not find, not from a generic list.

## Before you send it

- [ ] Every fact has a link and a date
- [ ] No estimated numbers; gaps say "Not found"
- [ ] Nothing private about a person
- [ ] Quick Take first; fits one page
- [ ] Sources listed at the end

## Project adjustments

If the current project has adjustments for this skill (what you sell, who you sell to, proof points, tone, competitors to watch), apply them. Where they disagree with these instructions, the project's adjustments win.
