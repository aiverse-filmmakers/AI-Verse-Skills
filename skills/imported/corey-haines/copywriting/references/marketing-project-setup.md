# Marketing setup for one project

Use this when a project has no marketing notes yet, or when the notes need updating. The answers are saved as the project's `marketing` adjustments, so every marketing skill (copywriting, ad creative, content strategy, customer research, email sequences, SEO audits, community marketing, social content) starts from them and no one asks the same questions twice.

Adapted from the product-marketing skill in coreyhaines31/marketingskills (MIT, see the LICENSE in this skill's folder).

## Where the notes live

Inside the current project only, as the `marketing` topic of that project's skill adjustments. Never read or write another project's notes, and never store passwords, keys or tokens in them. If you are not working inside a project, ask the questions, use the answers for this task, and offer to save them once a project is chosen.

When the skills are loaded through the skill finder with a project scope, the notes arrive with the skill. Otherwise read `skill-adjustments/marketing.md` in the project's `context` folder. To save, use the `adjustments-save` operation with the name `marketing`, then tell the user: "Saved for this project only."

## How to run it

1. If notes exist, read them back in a few lines and ask which sections to update. Only ask about those.
2. If none exist, offer two routes: draft a first version from what the project already contains (readme, site copy, about pages, existing docs) and ask what is wrong or missing, or walk through the sections one at a time.
3. Ask one section at a time, never all questions at once. Push for the customers' own words, because exact phrases beat polished descriptions.
4. Show the finished notes, ask what needs adjusting, then save.

## Sections

1. **Product**: one line, what it does, category (the shelf customers search on), type, business model and price.
2. **Audience**: who buys (type, size, stage), who decides, the main problem, the two or three jobs they hire it for.
3. **People** (only when several people take part in buying): user, champion, decision maker, who pays. What each cares about.
4. **Problems**: the core problem before they found you, why current options fall short, what it costs them, the emotional side.
5. **Competition**: direct (same solution), secondary (different solution, same problem), indirect (a different approach). How each falls short.
6. **Difference**: what you offer that alternatives lack, why that is better, why people choose you.
7. **Objections**: the top three heard, and who is not a good fit.
8. **Switching**: what pushes them away from the old way, what pulls them to you, what keeps them stuck, what worries them about switching.
9. **Customer language**: how they describe the problem and your solution, words to use, words to avoid, product terms.
10. **Voice**: tone, style, three to five personality words.
11. **Proof**: numbers, customers, quotes, the main themes and the evidence for each.
12. **Goals**: the business goal, the one action you want people to take, current numbers if known.

## Format to save

```
# Marketing notes
Version: v1   Updated: YYYY-MM-DD

## Product
One line:  What it does:  Category:  Type:  Business model:

## Audience
Who buys:  Who decides:  Main problem:  Jobs to be done:

## Problems
Core problem:  Why alternatives fall short:  What it costs them:  Emotional side:

## Competition and difference
Direct:  Secondary:  Indirect:  What is different:  Why people choose us:

## Objections
Top three and the answer to each:  Not a good fit:

## Switching
Push:  Pull:  Habit:  Anxiety:

## Customer language
Their words for the problem:  Their words for us:  Use:  Avoid:  Terms:

## Voice
Tone:  Style:  Personality:

## Proof
Numbers:  Customers:  Quotes:  Themes and evidence:

## Goals
Business goal:  Action we want:  Numbers:

## Changelog (newest first, one line per change and why)
- v1 (YYYY-MM-DD): first version.
```

On an update, raise the version, set the date, and add one changelog line on top saying what changed and why. A typo fix needs no new version.
