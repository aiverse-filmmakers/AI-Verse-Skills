---
name: video-editor
description: Orchestrate real video editing from footage, transcript, script, URL, or reference through transcript truth, silence and mistake passes, EDLs, short-form or long-form editorial structure, visual beats, captions/B-roll, HyperFrames assembly, media QA, and final render. Use for full edits and multi-stage video-post workflows. Route narrow requests such as silence removal directly to the relevant internal specialist. Do not use Interface Designer as the editorial authority.
version: 0.1.0
license: MIT
metadata:
  ai-verse:
    ownership: first-party
    category: film-media
    composite: true
    registration: registered-release-candidate
---

# AI-Verse Video Editor

## Purpose

Take a video-editing request from source material to a verified deliverable while preserving source-time truth, editorial intent, deterministic edit decisions, runtime correctness, and final media evidence.

This Skill is the member-facing editor/orchestrator. It coordinates specialist Skills and providers. It does not duplicate their bodies or invent substitute renderer behavior.

## Current Registration State

This package is a **registered release candidate** on the Video Editor implementation branch.

Its Nate-derived editorial specialists are package-local and provenance-locked. The
accepted HyperFrames 0.8.40 provider family is pinned as internal support dependencies.

Registration is not release acceptance. PR #14 remains draft until the remaining
cross-skill, media-QA, regression, documentation, and final release gates pass.

Do not equate registry presence with a completed public-beta release.

## Read First

Before substantial work:

1. inspect project/repository instructions;
2. identify the exact source footage/transcript/script/reference inputs;
3. preserve source identity and provenance;
4. detect whether this is a full edit or a bounded operation;
5. read [references/capabilities.json](references/capabilities.json);
6. route with [references/orchestration.json](references/orchestration.json);
7. preserve the authority boundaries in [references/ownership.md](references/ownership.md);
8. use [references/routing.md](references/routing.md) for task-class behavior.

## Scope Classes

Choose the smallest matching scope:

- `SILENCE_ONLY`
- `MISTAKE_RETAKE_ONLY`
- `CAPTIONS_ONLY`
- `MOTION_GRAPHICS_ONLY`
- `SHORT_FORM_EDIT`
- `LONG_FORM_TALKING_HEAD`
- `WEBSITE_PROMO`
- `REFERENCE_LED_EDIT`
- `FULL_EDIT`

Do not run the full pipeline for a narrow deterministic operation.

## Editorial Authority Rule

Editorial truth comes before graphics.

The Video Editor and its editorial specialists own:

- source-video identity;
- transcript truth;
- source-time to edited-time mapping;
- silence/dead-air decisions;
- false-start, retake, stutter and mistake decisions;
- EDL construction;
- scene order and editorial continuity;
- hook/open-loop/payoff structure;
- B-roll placement decisions;
- caption timing;
- final A/V sync and cut verification.

Graphics, design and motion specialists may improve presentation but cannot silently rewrite those decisions.

## Canonical Full-Edit Flow

For a complete edit, the maximum route is:

1. source/provenance intake;
2. transcription when needed;
3. silence/dead-air pass;
4. mistake/retake review;
5. EDL and transcript retiming;
6. short-form or long-form editorial structure;
7. reference analysis when supplied;
8. visual beats, captions, B-roll and sound plan;
9. style/visual direction;
10. HyperFrames composition and GSAP motion;
11. FFmpeg/media preprocessing as required;
12. lint and current HyperFrames `check`;
13. Studio/preview review;
14. draft render;
15. structural, visual and audio QA;
16. fix failed gates;
17. final render and delivery evidence.

Stages are conditional. Never execute this as blind ceremony.

## Narrow Operations

Examples:

- “Remove the silences” routes to the silence-cut specialist only, with source/timing validation and output verification.
- “Clean the mistakes and retakes” routes to the reviewed mistake/retake specialist.
- “Add captions” routes to caption/transcript timing specialists and the canonical renderer as needed.
- “Add motion graphics” preserves the existing edit and invokes motion/visual specialists plus render QA.
- “Turn this into a Reel” invokes short-form editorial structure, not merely a 9:16 crop.

## HyperFrames Provider Rule

AI-Verse Video Editor uses one canonical HyperFrames provider family.

Accepted provider baseline:

- upstream: `heygen-com/hyperframes`
- version: `0.8.40`
- immutable release commit: `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`

New guidance uses:

```bash
npx hyperframes lint
npx hyperframes check
npx hyperframes preview
npx hyperframes render --output final.mp4
```

Do not introduce a second Nate-bundled HyperFrames provider.

## Nate Editorial Preservation Rule

The Nate Herk student-kit is the editorial baseline, pinned during integration to:

`nateherkai/hyperframes-student-kit@b1afdb1dcbcad39dd27638ea699f132fe44ce6df`

Preserve its uniquely useful editorial logic as separate specialists where appropriate.

Do not preserve obsolete renderer instructions merely because they existed in the older kit. Provider-specific rules must follow the accepted HyperFrames version.

## Interface Designer Boundary

When presentation expertise would materially improve the video, read
[references/interface-designer-handoff.md](references/interface-designer-handoff.md)
and its machine-readable contract
[references/interface-designer-handoff.json](references/interface-designer-handoff.json).

There are exactly four allowed handoff modes:

- `VISUAL_DIRECTION` for substantial graphic language, typography, palette, composition, or visual-system work;
- `REFERENCE_RECREATION` for visual reconstruction from supplied references without stealing editorial pacing analysis;
- `PROTOTYPE_VISUAL_DIRECTIONS` for bounded divergent presentation options before a costly full build;
- `MOTION_TASTE` for specialist pacing, easing, continuity, emphasis, and gesture advice inside locked editorial/runtime constraints.

Video Editor sends locked editorial meaning and only the visual context needed for
the selected handoff. Interface Designer returns presentation decisions to Video
Editor, which remains responsible for implementation and verification.

Interface Designer may contribute:

- visual direction;
- typography;
- composition;
- palette hierarchy;
- reference reconstruction;
- prototype visual directions;
- design-system cleanup;
- general motion taste.

Interface Designer must not own:

- edit decisions;
- transcript truth;
- EDLs;
- retake/mistake judgment;
- source-time mapping;
- hook/payoff editorial logic;
- caption timing truth;
- audio/video synchronization;
- HyperFrames runtime correctness;
- final media acceptance.

If generic interface-motion advice conflicts with HyperFrames runtime rules,
HyperFrames wins for implementation. If visual preference conflicts with locked
editorial truth, editorial truth wins.

## Verification Contract

Never claim completion because the composition compiled.

For substantial edits verify, as applicable:

- source/transcript identity;
- EDL validity;
- source-time mapping;
- deterministic composition;
- HyperFrames lint/check;
- real preview/Studio state;
- draft output;
- hook and major beat frames;
- transitions;
- CTA/outro;
- blank/black frames;
- cropping and text legibility;
- cut joins and abrupt sentence boundaries;
- audio presence;
- A/V sync;
- requested aspect ratios independently;
- final encoded output.

Automated waveform or frame checks supplement human media review; they do not justify claiming listening or visual inspection that did not occur.

## Conflict Order

Resolve conflict in this order:

1. explicit current user instruction;
2. source/provenance truth;
3. established project authority and locked edit decisions;
4. editorial specialist authority;
5. canonical HyperFrames/runtime correctness;
6. media QA evidence;
7. visual-design specialist advice;
8. optional polish.

## Success Contract

Completion requires:

- the requested edit scope was correctly classified;
- source-time truth and EDL integrity were preserved;
- no specialist silently stole another owner's responsibility;
- only the canonical HyperFrames provider was used;
- selected verification gates actually ran;
- unresolved visual/audio/runtime risk is stated instead of hidden;
- final delivery evidence refers to the actual encoded media, not only source code or preview.
