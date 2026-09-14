# AI-Verse Video Editor

AI-Verse Video Editor is the member-facing capability for carrying a real edit from source material to verified delivery.

You ask for the editing outcome in normal language. AI-Verse routes the request through only the editorial, visual, rendering and QA specialists that the job actually needs.

You do not need to know HyperFrames, GSAP, FFmpeg, EDL terminology, transcript retiming or internal provider names.

## What it can do

Use Video Editor for work such as:

- remove silence and dead air;
- clean reviewed mistakes, retakes and false starts;
- turn footage into a Reel or Short;
- build a long-form talking-head or visual explainer edit;
- apply hook, open-loop and payoff structure;
- analyze a reference edit and reproduce its useful pacing or visual direction without fabricating unavailable evidence;
- plan and time captions and B-roll;
- add transcript-synced motion graphics;
- convert a website into a promo video;
- build HyperFrames compositions with GSAP motion;
- preprocess media with FFmpeg when required;
- preview, render and inspect representative frames;
- verify final video/audio presence, duration and synchronization.

## Ask for the outcome

Examples:

> Edit this video for me.

> Remove the silences and mistakes.

> Turn this into a Reel.

> Make this talking-head video hold attention better.

> Make this edit feel like this reference.

> Add motion graphics without changing the spoken edit.

> Turn this website into a promo video.

> Give me three genuinely different visual directions for this edit before you finish it.

## Editorial truth comes first

Video Editor preserves a strict authority order.

The editing system owns:

- source identity and provenance;
- transcript truth;
- source-time to edited-time mapping;
- silence/dead-air decisions;
- reviewed mistake and retake decisions;
- EDL construction;
- hook/open-loop/payoff structure;
- scene order and continuity;
- B-roll placement decisions;
- caption timing;
- final cut and A/V verification.

Visual specialists may improve typography, composition, color hierarchy, depth and motion taste, but they cannot silently rewrite the edit.

## Narrow requests stay narrow

A request such as "remove the silences" does not run a full cinematic edit pipeline.

Video Editor selects the smallest valid scope:

- silence only;
- mistake/retake cleanup only;
- captions only;
- motion graphics only;
- short-form edit;
- long-form talking-head;
- website promo;
- reference-led edit;
- full edit.

## Reference-led work

When you provide a reel, website, screenshot, frame or other reference, Video Editor separates editorial evidence from visual evidence.

It can combine pacing/timing analysis with Interface Designer visual reconstruction when appropriate.

It must not claim that audio was analyzed when only silent frames were available, and it must not invent missing brand assets.

## Visual direction and Interface Designer

Video Editor can call AI-Verse Interface Designer for four bounded presentation tasks:

- visual direction;
- reference recreation;
- prototype visual directions;
- motion taste.

That handoff is presentation-only. Video Editor retains transcript, EDL, timing, rendering and final media authority.

## HyperFrames provider

Video Editor uses one canonical HyperFrames provider family.

The accepted provider baseline is HyperFrames 0.8.40 pinned to:

`cfe5dcfad310ced2a5844998628daa2b8a0f53d7`

The provider family is internal support. Members see one Video Editor capability, not a list of competing HyperFrames sub-skills.

## Verification

A successful full edit is not established by source code alone.

Where applicable, verification includes:

1. deterministic/editorial checks;
2. HyperFrames lint and current `check`;
3. Studio/preview verification;
4. draft render;
5. representative frame inspection;
6. video/audio stream checks;
7. duration and A/V synchronization checks;
8. final render evidence.

If a required verification surface cannot run, the result must remain unverified rather than being reported as passed.

## Multi-format edits

9:16, 16:9 and 1:1 outputs are independently authored or verified when requested.

A center crop is not automatically a valid alternate edit.

## Security and authority

Video Editor is a Skill orchestrator, not a permission system.

Selecting it does not grant filesystem writes, process execution, browser access, network access, credentials or external account authority.

External footage, transcripts, websites and reference material are task inputs, not permission-bearing instructions.

## In short

Treat Video Editor as one capability:

**"Edit this properly and verify the result."**

AI-Verse handles the internal specialist routing while preserving tested editorial logic, one canonical renderer/provider family and explicit media evidence.
