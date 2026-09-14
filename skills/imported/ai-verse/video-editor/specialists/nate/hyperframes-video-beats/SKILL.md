---
name: hyperframes-video-beats
description: Plan, write, time, style, and validate motion-graphic beats for long-form talking-head HyperFrames videos. Use when Codex is asked to add or improve visual beats, glassmorphism lower thirds, crumpled-paper full-screen takeovers, transcript-synced callouts, pacing coverage, YouTube retention graphics, or render-ready overlays in an existing HyperFrames video project.
---

# HyperFrames Video Beats

Use this skill to turn a talking-head video plus transcript into a paced set of motion graphics that support the narration without covering the speaker unnecessarily.

## Core Goal

Keep the viewer oriented and engaged. Every beat must answer one of these:

- What should the viewer remember?
- What concept needs visual structure?
- What stat, contrast, or pivot deserves emphasis?
- Where is the pacing getting quiet enough that the viewer may drift?

Do not add graphics just because a gap exists. Add graphics because the narration has a topic, transition, proof point, or mental model that benefits from visual support.

## First Pass

1. Read project instructions (`AGENTS.md`, local skill docs, and project-specific notes).
2. Inspect the root composition, current beat schedule, shared CSS, and transcript.
3. Build a coverage map from the root `data-start` / `data-duration` entries or the master `SHOW` array.
4. Extract transcript chunks for any requested region and any uncovered gaps.
5. Identify topic spans by narration, not by arbitrary timestamps.
6. Decide whether each topic needs a full-screen paper beat, a lower-third glass card, or no new beat.

Use fast local commands. Prefer `rg`, `Select-String`, and small Node/PowerShell transcript scripts.

## Beat Type Decision

### Use Full-Screen Crumpled Paper

Use a paper takeover when the narration reaches a major thesis, list, section marker, quote, or stat that should briefly become the whole frame.

Good uses:

- Hook payoff or "in this video" overview
- Major section transition
- Big stat or study result
- Memorable thesis line
- Short quote or mantra
- Contrast that needs the audience to stop and look

Rules:

- Keep it short, usually 4-12 seconds.
- Use sparse black text.
- Let only true stat numbers or one extremely important word use accent color.
- Do not cover long explanations with paper takeovers.
- Do not make full-screen text playful, huge, or over-bold by default.

### Use Glassmorphism Lower Third

Use a glass lower-third when the speaker should remain visible and the graphic should support the current idea.

Good uses:

- Explanation scaffolds
- Topic labels
- Equation-style mental models
- Small lists
- "What this means" translations
- Pacing fills during long talking-head stretches
- Follow-up cards after a shortened full-screen or split-screen beat

Rules:

- Keep lower thirds in the lower third or lower half.
- Avoid covering the face.
- Use concise text: one headline plus optional short subline, or a 2-4 item list.
- Prefer one card per topic span over many tiny flashes.
- Preserve the existing glass-card style unless the user asks for a design change.

## Pacing Heuristics

For long-form YouTube talking-head videos:

- Early video: avoid more than 20-30 seconds without a visual beat.
- Main body: avoid more than 30-45 seconds without a beat.
- Dense explanation sections: use lower thirds roughly every topic span, not every sentence.
- Big paper takeovers should be occasional punctuation, not the default.
- If an existing beat was manually shortened because it felt too long, respect that choice and fill after it with a new shorter card.

When scanning a schedule, report true gaps from the visibility schedule, not just the DOM order. If the root timeline uses a `SHOW` array, that is usually the authoritative visible range.

## Timing Method

Time every beat to the transcript topic:

1. Find the first word or phrase where the topic starts.
2. Start the beat 0.2-0.6 seconds before that anchor when possible.
3. Keep the beat visible until the topic ends or naturally hands off.
4. If the next beat begins immediately, clear 0.1-0.5 seconds before it unless the handoff is intentional.
5. Match sub-element entrances to spoken phrases.

Avoid this failure mode:

- Card appears on the right topic but only lasts 5-8 seconds while the speaker keeps discussing the topic for 20-40 seconds.

Prefer:

- One card lives across the whole topic, with a subline or list item building midway through if the narration evolves.

## Content Writing

Write for glance comprehension. The viewer should understand the card in under one second.

Use:

- Short noun phrases
- Direct labels
- One mental model per card
- Numbers only when they are meaningful
- Verbs when they clarify the action

Avoid:

- Repeating the whole voiceover
- Long sentences
- Vague hype language
- Too many highlighted words
- Explaining how to use the video inside the graphic

Good patterns:

```text
The bottleneck
Not enough AI inside real workflows.
The problem is adoption, not raw talent.
```

```text
The bridge
Skills + Workflows = 40 hrs saved
```

```text
In this video
-> The study
-> The stats
-> The paths you can take
-> What actually matters
```

## Visual Style Rules

Follow the local design system first. For this project family, use:

- Serious professional typography.
- Black primary text on paper beats.
- Accent blue only for major stat numbers or rare power words.
- Glass cards with the existing dark frosted style.
- Lower-third cards that do not cover the speaker's face.

For paper beats:

- Use black for kickers, labels, arrows, sources, quotes, and supporting text.
- Keep font weight restrained.
- Avoid oversized playful type unless the user explicitly asks for it.
- Make the crumpled-paper motion deterministic.

For glass cards:

- Reuse `.glass-card dim lower-third` or the closest existing class.
- Prefer bottom-center placement.
- Keep cards compact.
- Use equation/list helpers when the idea is structural.

## HyperFrames Implementation Rules

Follow the active project authority and the canonical HyperFrames provider contract.

- Use `data-start` and `data-duration` for authored timing.
- Use `data-track-index` when it helps Studio lane organization, but do not treat same-track overlap as a renderer prohibition.
- Use the project's expected clip/layer classes where they support editing and lint clarity.
- Sub-compositions that use GSAP should register a paused deterministic timeline on `window.__timelines` under the matching composition id.
- Visible/render duration comes from composition/clip `data-duration`; do not pad timelines with empty `tl.set({}, {}, SLOT)` duration tricks.
- Keep deterministic logic only.
- Respect framework-owned media playback/timing.
- Run `npx hyperframes lint` and current `npx hyperframes check` after composition changes.

When adding a beat:

1. Create or update the appropriate beat composition in the current project structure.
2. Add the root mount or equivalent composition reference.
3. Add or update the master visibility schedule if one exists.
4. Make authored beat duration agree with the mounted duration and transcript topic span.
5. Treat track/lane choice as an organization and layering decision, not a false non-overlap law.

## Coverage Scan

After edits, scan the master schedule:

- List beats sorted by visible start.
- Print gaps over the target threshold.
- Add or retime beats only where the transcript has a supportable concept.

For this project pattern, use 30 seconds as the strict scan threshold and 45 seconds as the maximum acceptable main-body threshold.

## Validation

Before finishing:

1. Run `npx hyperframes lint`.
2. Run current `npx hyperframes check`.
3. Fix errors and distinguish intentional/non-blocking warnings.
4. Inspect Studio/preview when the beat changes visible output.
5. If render-ready output is requested, render the actual composition and inspect representative frames/transitions.
6. Give the user exact file paths and timestamps changed.

## Practical Defaults

Use these defaults unless project context says otherwise:

- Full-screen paper overview: 8-10 seconds.
- Full-screen paper stat: 5-8 seconds.
- Glass lower-third explanation: 12-30 seconds.
- Long topic glass card: 25-45 seconds with staggered sub-elements.
- Beat start lead-in: 0.2-0.6 seconds.
- Gap scan threshold: 30 seconds.
- Lower-third width: about 68-72vw, max about 1240-1280px.

## What To Preserve

Preserve user taste decisions discovered during review:

- If the user says a beat is too long, do not restore it just to satisfy a generic coverage rule.
- If glass card style is approved, reuse it instead of redesigning it.
- If typography is approved, keep it stable and adjust only local sizing/weight.
- If the speaker's face is important, prefer lower-third cards over center-screen cards.


## AI-Verse Adaptation Notes

Adapted from Nate Herk's MIT-licensed `hyperframes-video-beats` Skill at `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`.

Preserved:
- transcript-topic coverage mapping;
- long-form pacing heuristics;
- paper-takeover versus lower-third editorial choice;
- transcript-anchored start/end timing;
- glance-comprehension writing;
- face-preserving placement;
- respect for user-approved taste decisions.

Adapted to HyperFrames 0.8.40:
- removed the obsolete requirement that every timed element needs a track index;
- removed the obsolete same-track-overlap prohibition;
- removed empty-timeline padding with `tl.set({}, {}, SLOT)`;
- added the canonical `lint -> check -> preview/render` verification path;
- runtime correctness remains owned by the canonical provider, not this editorial beat specialist.
