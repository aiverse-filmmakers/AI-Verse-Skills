---
name: one-three-one-rule
description: "1-3-1 decision briefs: problem, three options, one pick. Use when the user asks for a 1-3-1, asks for options or choices on a decision, or needs a short proposal to forward to someone."
author: Willard Moore
license: MIT
metadata:
  source: "Adapted by AI-Verse from NousResearch/hermes-agent (MIT). Modified; see SOURCE.json."
---

# 1-3-1 Communication Rule

Structured decision-making format for when a task has multiple viable approaches and the user needs a clear recommendation. Produces a concise problem framing, three options with trade-offs, and an actionable plan for the recommended path.

## When to Use

- The user explicitly asks for a "1-3-1" response.
- The user says "give me options" or "what are my choices" for a decision.
- A task has multiple viable approaches with meaningful trade-offs (a plan, a purchase, a delivery, a tool, a way of working).
- The user needs a proposal they can forward to a team or stakeholder.

Do NOT use for simple questions with one obvious answer, debugging sessions, or tasks where the user has already decided on an approach.

## Procedure

1. **Problem** (one sentence)
   - State the core decision or desired outcome in a single concise sentence.
   - Focus on the *what*, not the *how* — no implementation details, tool names, or specific technologies.
   - Keep it tight. If you need "and", you're describing two problems.

2. **Options** (exactly three)
   - Present three distinct, viable approaches labeled A, B, C.
   - Each option gets a brief description, pros, and cons.
   - Options should represent genuinely different strategies, not minor variations of the same approach.

3. **Recommendation** (one option)
   - State which option you recommend and why, based on the user's context and priorities.
   - Be direct — this is your professional judgment, not a hedge.

4. **Definition of Done**
   - List the specific success criteria for the recommended option.
   - These are concrete, verifiable outcomes — not vague aspirations.
   - If the user picks a different option, revise this section to match.

5. **Implementation Plan**
   - Concrete steps to execute the recommended option.
   - Include specific commands, tools, or actions where applicable.
   - If the user picks a different option, revise this section to match.

## Verification

- Response has exactly one Problem sentence.
- Response has exactly three Options (A, B, C) with pros and cons for each.
- Response has a single Recommendation that picks one option with reasoning.
- Definition of Done and Implementation Plan align with the recommended option.
- If the user selects a different option, Recommendation, DoD, and Implementation Plan update accordingly.

## Example

User: "Give me a 1-3-1 for getting a client video delivered by Friday when the edit is two days behind."

Agent:

**Problem:** The client video is due Friday and the edit is about two days behind schedule.

**Options:**

- **Option A: Cut the scope.**
  Deliver a shorter version on Friday (60 seconds instead of 90) and send the longer cut the following week.
  Pros: Hits the deadline; less rushed work.
  Cons: The client gets less than agreed first; needs their buy-in.

- **Option B: Work extra hours and keep the full scope.**
  Pros: The client gets exactly what was agreed.
  Cons: Tired editing leads to mistakes; no time left for client feedback rounds.

- **Option C: Ask for a short extension.**
  Pros: Keeps quality and scope; costs nothing extra.
  Cons: Depends on the client agreeing; may affect their own launch plans.

**Recommendation:** Option A. It protects the deadline and the quality, and clients usually accept a shorter first delivery when it is offered early.

**Definition of Done:**
- The client has agreed to the shorter first delivery in writing.
- A 60 second cut is exported and sent by Friday noon.
- The remaining 30 seconds is scheduled for the following Wednesday.

**Implementation Plan:**
1. Message the client today with the offer and the new dates.
2. Pick the strongest 60 seconds and lock the edit by Thursday evening.
3. Export, check on a phone and on a laptop, and send by Friday noon.
4. Finish the extended cut and send it on Wednesday.
