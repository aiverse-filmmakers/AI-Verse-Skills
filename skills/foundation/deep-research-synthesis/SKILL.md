---
name: deep-research-synthesis
description: "Research a hard question across several sources, reconcile where they disagree, and give a dated, sourced answer with a confidence level. Use when the user asks to research, compare, fact check or find out something where being wrong matters: which tool or model is best right now, what a rule or a price really is, whether a claim is true, or what the evidence says."
license: MIT
compatibility: "Needs web search or documents supplied by the user. With neither, say so and stop."
metadata:
  tier: foundation
  owner: ai-verse
---

# Deep Research Synthesis

Turn a question into an answer someone can act on, check and date.

Three failure modes, worst first:

1. **Answering from memory.** Prices, models, laws and versions change. A confident stale answer is worse than no answer.
2. **Counting one source five times.** Five articles repeating one press release are one source.
3. **Averaging a disagreement into mush.** "Opinions differ" helps nobody. Say who disagrees, why, and which you believe.

## Gate

If one lookup answers it, answer it and skip this skill. If the user needs a decision, name the decision before searching: it tells you what to ignore.

## Hard rules

1. **No claim the answer depends on without a source opened in this session.** Memory is a lead, never a source.
2. **Every source has a date.** For anything that changes, write "as of" and the date.
3. **Trace to the origin.** When several pages cite the same origin, cite the origin and count it once.
4. **Show disagreements.** Never average them.
5. **Label what is yours.** "Sourced:" for what a source says, "My inference:" for what you conclude from it.
6. **Never invent** a quote, a number, a name or a link. Quotes are short and exact.
7. **Say what you did not check.**

## Step 1 — The brief

State it back in three lines before searching. Ask at most one question, and only if the decision is unclear.

```
Question:  what exactly is being asked
Decision:  what the answer will be used for
Fresh to:  how old is too old (this month, this year, any time)
Out of scope: what you will not cover
```

## Step 2 — Plan the search

Split the question into 3 to 6 smaller questions. For each, decide where the first hand source would be before you search, then go there.

| Tier | What it is | Use it for |
| --- | --- | --- |
| 1. First hand | Official documentation, the text of the law, filings, pricing pages, papers, datasets, the maker's release notes | Facts |
| 2. Independent testing | Hands on tests that show their method, reputable press with named sources | Performance, comparisons |
| 3. Second hand | Aggregators, "top 10" lists, vendor blogs, forums | Leads only |

A maker's own page is Tier 1 for its price and specification, and Tier 3 for how good it is. Forum posts are fine as "what users report", labelled as anecdote.

## Step 3 — Source log

Keep it as you go. It is the evidence behind the answer.

| # | Claim | Source and link | Published | Tier | Limits (method, bias, age) |
| --- | --- | --- | --- | --- | --- |

**Minimum:** two independent sources for every claim the answer depends on, one of them Tier 1 where a Tier 1 source exists. If you cannot reach that, mark the claim "single source".

## Step 4 — Reconcile

When sources disagree, check in this order. Most disagreements end at the first or second.

1. **Different dates.** For things that change, newer usually wins.
2. **Different definitions.** "Users", "free", "best" rarely mean the same thing twice.
3. **Different version, region or plan.**
4. **Different method.** What was tested, and how?
5. **Incentive.** Who gains if this is believed?

Then either settle it and say why, or present both sides and say what would settle it.

## Step 5 — Write

```
Answer (as of <date>): two to four sentences. The decision, not a tour.
Confidence: High, Medium or Low, and why.
Key findings:
  - finding [1][3]
Where sources disagree:
What would change this answer:
Not checked:
Sources:
  [1] Title, publisher, date, link
```

| Confidence | Means |
| --- | --- |
| High | Two or more independent sources including first hand, fresh enough, no open conflict |
| Medium | Good sources with a gap: one side untested, slightly old, or one conflict explained but not settled |
| Low | Single source, stale, or an unresolved conflict |

## When to stop

- New searches repeat what the log already holds.
- Most questions settle within 6 to 12 sources. Past 20, the question is too wide: narrow it with the user.
- **"The evidence is not there" is a valid answer.** Say it plainly and say what would be needed.

## Never

| Never | Instead |
| --- | --- |
| State a price, version or rule from memory | Open the page, date it |
| Cite a page you did not open | Open it or drop it |
| Count repeats of one origin as agreement | Cite the origin once |
| Present a vendor's benchmark as a result | Label it the vendor's claim |
| Give legal, medical or financial advice | Report what the sources say, with date and country |
| Hide a weak answer behind long text | Lead with the confidence level |

## Project adjustments

If the current project has adjustments for this skill (trusted sources, country, currency and units, how deep to go), apply them. Where they disagree with these instructions, the project's adjustments win.
