---
name: roadmap-update
description: "Update, create, or reprioritize a product roadmap that is saved as a file in the project, with a dated change log. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch."
license: Apache-2.0
compatibility: "No tools required. Uses a connected project tracker when present; otherwise keeps the roadmap in a ROADMAP.md file."
metadata:
  source: "Adapted by AI-Verse from anthropics/knowledge-work-plugins (Apache-2.0). Modified; see SOURCE.json."
---

# Roadmap Update

Update, create, or reprioritize a product roadmap.

## Hard rules

1. **Read the saved roadmap first.** Never rebuild it from memory or from an earlier chat.
2. **Adding means asking what moves.** A roadmap is fixed against capacity; something comes off, slips or shrinks.
3. **Show before and after, and get a yes, before saving.**
4. **Every change is logged** with its date and its reason.
5. **Nothing disappears silently.** An item that is cut moves to the "Cut" list with the reason.
6. **Never invent a date, an owner or an estimate.** An unknown says "not set".

## Where the roadmap lives

One file per project: `ROADMAP.md` in the project folder, or the place named in the project's adjustments. It is the source of truth unless a project tracker is connected. `assets/roadmap-template.md` is the starting shape.

- **File exists:** read it, apply the change, show before and after, save on a yes, add a line to its change log.
- **No file yet:** build it from what the user gives, show it, and save it on a yes.
- **A tracker is connected:** the tracker is the source of truth. Offer to keep `ROADMAP.md` as a readable summary.

## Workflow

### 1. Understand Current State

If a **project tracker** is connected:
- Pull current roadmap items with their statuses, assignees, and dates
- Identify items that are overdue, at risk, or recently completed
- Surface any items without clear owners or dates

If no project tracker is connected:
- Read the saved `ROADMAP.md` (see **Where the roadmap lives**)
- If there is none, ask the user to describe, paste or upload the current roadmap. Accept any format: list, table, spreadsheet, screenshot, or prose

### 2. Determine the Operation

Ask what the user wants to do:

**Add item**: New feature, initiative, or work item to the roadmap
- Gather: name, description, priority, estimated effort, target timeframe, owner, dependencies
- Suggest where it fits based on current priorities and capacity

**Update status**: Change status of existing items
- Options: not started, in progress, at risk, blocked, completed, cut
- For "at risk" or "blocked": ask for the blocker and mitigation plan

**Reprioritize**: Change the order or priority of items
- Ask what changed (new information, strategy shift, resource change, customer feedback)
- Apply a prioritization framework if helpful — see `references/frameworks.md` for RICE, MoSCoW, ICE, and value-vs-effort
- Show before/after comparison

**Move timeline**: Shift dates for items
- Ask why (scope change, dependency slip, resource constraint)
- Identify downstream impacts on dependent items
- Flag items that move past hard deadlines

**Create new roadmap**: Build a roadmap from scratch
- Ask about timeframe (quarter, half, year)
- Ask about format preference (Now/Next/Later, quarterly columns, OKR-aligned) — see `references/frameworks.md`
- Gather the list of initiatives to include

### 3. Generate Roadmap Summary

Produce a roadmap view with:

#### Status Overview
Quick summary: X items in progress, Y completed this period, Z at risk.

#### Roadmap Items
For each item, show:
- Name and one-line description
- Status indicator (on track / at risk / blocked / completed / not started)
- Target timeframe or date
- Owner
- Key dependencies

Group items by:
- Timeframe (Now / Next / Later) or quarter, depending on format
- Or by theme/goal if the user prefers

#### Risks and Dependencies
- Items that are blocked or at risk, with details
- Cross-team dependencies and their status
- Items approaching hard deadlines

#### Changes This Update
If this is an update to an existing roadmap, summarize what changed:
- Items added, removed, or reprioritized
- Timeline shifts
- Status changes

### 4. Save

On a yes, write the updated `ROADMAP.md` and add one line to its change log: the date, what changed, and why. Then confirm the file path.

### 5. Follow Up

After generating the roadmap:
- Offer to format for a specific audience (executive summary, engineering detail, customer-facing)
- Offer to draft communication about roadmap changes
- If project management tool is connected, offer to update ticket statuses

## Output Format

Use a clear, scannable format. Tables work well for roadmap items. Use text status labels: **Done**, **On Track**, **At Risk**, **Blocked**, **Not Started**.

## Tips

- A roadmap is a communication tool, not a project plan. Keep it at the right altitude — themes and outcomes, not tasks.
- When reprioritizing, always ask what changed. Priority shifts should be driven by new information, not whim.
- Flag capacity issues early. If the roadmap has more work than the team can handle, say so.
- Dependencies are the biggest risk to roadmaps. Surface them explicitly.
- If the user asks to add something, always ask what comes off or moves. Roadmaps are zero-sum against capacity.

## Reference files

| File | Load when |
|---|---|
| `assets/roadmap-template.md` | Creating the roadmap file for the first time |
| `references/frameworks.md` | Choosing a roadmap format, scoring priorities, mapping dependencies, planning capacity, or announcing a change |

## Project adjustments

If the current project has adjustments for this skill (where the roadmap file lives, the format in use, team size and capacity, hard deadlines, who must be told about changes), apply them. Where they disagree with these instructions, the project's adjustments win.
