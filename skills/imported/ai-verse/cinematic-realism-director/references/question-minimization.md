# Question-Minimization Policy

Status: RUNTIME KNOWLEDGE
Task: 6.8

Purpose: let beginners use the skill from a single natural-language sentence while still allowing experts to lock precise technical choices.

## Core Rule

```text
If a missing choice can be inferred safely and reversibly, infer it.
Ask only when the missing answer materially changes the required output and cannot be inferred without a substantial risk of violating intent or preservation.
```

The skill is a director, not an intake form.

## Default Behavior

Do not ask the user to choose:

- camera body;
- lens family;
- focal length;
- aperture;
- lighting pattern;
- film stock;
- grade;
- grain;
- halation;
- aspect ratio;

unless one of those choices is genuinely necessary and cannot be inferred from the requested result.

AUTO DIRECT should normally proceed with zero questions.

## Question Threshold

Ask only if all three are true:

1. the information is missing;
2. different plausible answers would produce materially different deliverables;
3. choosing one automatically could violate the user's core intent, preservation requirement, or requested format.

If any condition is false, infer and proceed.

## Questions That Are Usually Unnecessary

Examples:

- `What camera do you want?`
- `What lens?`
- `What aperture?`
- `Do you want cinematic lighting?`
- `Do you want film grain?`

For a beginner, these are AUTO decisions.

## Questions That May Be Necessary

Examples:

### Missing target image for an edit
If the user says `fix this exact image` but no usable image exists in the current context, the target cannot be truthfully edited or visually inspected.

### Ambiguous preservation boundary
If the user asks `make her different but keep her identical`, and the exact intended change cannot be reconciled from context, one focused question may be needed.

### Multiple contradictory references with no role assignment
If one reference is clearly warm/high-key and another is dark/low-key and the user says only `match these`, ask which reference controls which dimension only when AUTO weighting would materially risk the result.

### Exact deliverable format
If a downstream workflow truly requires a dimension/aspect specification and the host cannot infer or negotiate it safely, ask once.

## Better Than Asking: Make a Reasonable Default

Examples:

User: `Cinematic portrait of a baker in his shop.`

Do not ask for camera/lens/light. Infer:

- human-scale camera position;
- moderate subject separation;
- motivated window/practical lighting depending scene cues;
- natural skin/material response;
- environment retained enough to tell the story.

User: `A luxury perfume ad.`

Infer a polished commercial setup with product-legible geometry and controlled specular design. Do not force a dark/moody look unless requested.

## Expert Inputs

When the user supplies technical details, do not ask them to re-confirm.

Example:

`Alexa 35, 50mm, T2.8, eye level, medium close-up, hard side light.`

Treat all explicit values as locks. Infer only the rest.

## Uncertainty Handling Without Interrogation

If the skill makes a non-critical inference:

- mark it AUTO / inferred internally;
- do not burden the user with every assumption;
- expose the inferred value only when useful, requested, or when it materially explains the result.

For reference analysis, uncertain hardware remains a hypothesis rather than a question unless exact hardware is necessary for the user's requested output.

## One-Question Maximum Pattern

When a question is truly required:

- ask the smallest possible question;
- avoid multi-part questionnaires;
- provide the relevant alternatives succinctly if needed;
- retain all already-resolved information.

## Host Limitation Rule

Do not ask the user for choices merely because a provider adapter is weak.

If a requested control is unavailable:

- preserve the intent;
- translate it semantically;
- disclose the limitation if material.

## Repair Rule

REALITY REPAIR should not ask cosmetic preference questions when the task can be solved by restoring physical plausibility while preserving the image.

Example:

`Fix the fake skin.`

Do not ask whether the user wants pores, freckles, peach fuzz, or wrinkles. Diagnose the visible issue and restore age/context-appropriate skin response minimally.

## Success Condition

A novice should be able to provide one sentence and receive a complete result. An expert should be able to provide many locks and receive no redundant interrogation.

Acceptance: questions become exceptional conflict-resolution tools, not the normal workflow.