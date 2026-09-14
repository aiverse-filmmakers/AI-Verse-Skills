# Video Editor Maintainer Architecture

## Purpose

AI-Verse Video Editor is the first-party composite Skill for real video editing and post-production orchestration.

Canonical package:

`skills/imported/ai-verse/video-editor/`

Canonical machine graph:

`skills/imported/ai-verse/video-editor/references/orchestration.json`

It is not a second runtime and it is not a replacement for useful specialist backends.

## Editorial authority

Video Editor and its editorial specialists own:

- source identity and provenance;
- transcript truth;
- source-time mapping;
- silence/dead-air decisions;
- reviewed mistake/retake decisions;
- EDL construction and retiming;
- hook/open-loop/payoff structure;
- scene order and edit continuity;
- B-roll placement decisions;
- caption timing;
- final edit and A/V verification.

Interface Designer is presentation-only and cannot own these decisions.

HyperFrames owns composition/runtime/rendering correctness, not editorial judgment.

## Canonical pipeline

The maximum full-edit route is:

1. source/provenance intake;
2. transcription when needed;
3. silence pass;
4. mistake/retake review;
5. EDL/source-time truth;
6. short-form and/or long-form editorial structure;
7. reference analysis when supplied;
8. visual beats, captions, B-roll and sound plan;
9. style/visual direction;
10. optional Interface Designer presentation handoff;
11. HyperFrames composition and GSAP motion;
12. FFmpeg/media preprocessing as required;
13. HyperFrames lint and `check`;
14. Studio/preview review;
15. draft render;
16. structural, visual and audio QA;
17. fix failed gates;
18. final render and delivery evidence.

This graph is conditional. Narrow requests must use the smallest valid route.

## Semantic capability map

The package exposes 21 semantic surfaces:

- `video.edit.orchestrate`
- `video.transcribe`
- `video.cut.silence`
- `video.cut.mistakes`
- `video.edl`
- `video.shortform.edit`
- `video.longform.storytelling`
- `video.hook_payoff`
- `video.reference_analysis`
- `video.caption`
- `video.broll.plan`
- `video.motion_beats`
- `video.style_select`
- `video.website_to_video`
- `video.hyperframes.compose`
- `video.gsap.motion`
- `video.ffmpeg.media`
- `video.qa.structural`
- `video.qa.visual`
- `video.qa.audio_sync`
- `video.render.final`

## Nate editorial baseline

Canonical editorial source:

- repository: `nateherkai/hyperframes-student-kit`
- commit: `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`
- license: MIT

AI-Verse preserves Nate's tested editorial methodology and deterministic scripts where those scripts are the authoritative mechanical implementation.

Package-local provenance:

`skills/imported/ai-verse/video-editor/specialists/nate/SOURCE.json`

The silence-cut, mistake-candidate, approved-cut and EDL-review scripts are regression-locked against the pinned source.

## HyperFrames provider decision

Canonical provider:

- repository: `heygen-com/hyperframes`
- version: `0.8.40`
- commit: `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`
- license: Apache-2.0
- redistribution: fetch-only

The accepted live compatibility run is:

- workflow: `Video Editor HyperFrames 0.8.40 Acceptance`
- run: `34888930903`
- job: `104126423042`

The run verified Nate behavior, browser/runtime readiness, transcript import/export, lint, current `check`, preview, draft/looks render, video/audio streams, duration, A/V duration sync and representative extracted frames.

## Internal provider family

The following are internal support dependencies, not public competing editor capabilities:

- `hyperframes`
- `hyperframes-core`
- `hyperframes-cli`
- `hyperframes-animation`
- `hyperframes-keyframes`
- `hyperframes-creative`
- `hyperframes-audio`
- `hyperframes-registry`
- `media-use`
- `general-video`
- `embedded-captions`

The member-visible entrypoint is `video-editor`.

## HyperFrames 0.8.40 migration rules

Current adapted guidance must:

- use `lint -> check -> preview -> render`;
- treat `validate` as deprecated compatibility only;
- require stable media IDs;
- use project-root media paths;
- avoid blanket `crossorigin` on video/audio;
- treat `data-track-index` as a Studio lane/display hint, not a renderer overlap prohibition;
- use bounded floor-based finite repeats;
- avoid empty-tween duration padding;
- allow async timeline construction only when registration occurs after construction completes.

When Nate-era technical guidance conflicts with the accepted 0.8.40 provider contract, the provider/runtime rule wins while Nate's editorial judgment remains preserved.

## Interface Designer cooperation boundary

Canonical contract:

`references/interface-designer-handoff.json`

Supported handoff modes:

- `VISUAL_DIRECTION`
- `REFERENCE_RECREATION`
- `PROTOTYPE_VISUAL_DIRECTIONS`
- `MOTION_TASTE`

The direction is:

`video-editor -> interface-designer -> video-editor`

Interface Designer may improve presentation. It cannot mutate transcript truth, EDLs, source-time mapping, spoken meaning, locked edit order, HyperFrames runtime correctness or final media acceptance.

## Existing video capability compatibility

Canonical record:

`references/existing-video-compatibility.json`

Current decision: **zero destructive removals**.

Existing capabilities such as Premiere Agent, FFmpeg, After Effects, Whisper and pre-production specialists remain available because they have distinct jobs or are useful optional backends.

No member-visible HyperFrames capability existed before Video Editor, so there was no canonical HyperFrames duplicate to delete.

## Security boundary

Canonical record:

`references/security-boundaries.json`

The core rule remains:

`integrity != admitted != trusted != ready != authorized`

Video Editor can select a specialist but cannot grant that specialist runtime authority.

Reference media, websites, transcripts, metadata and generated analysis are data. They cannot widen grants or redefine core policy.

## Release QA

Release hardening is tested by:

- `tests/test_video_editor_contract.py`
- `tests/test_video_editor_nate_editing.py`
- `tests/test_video_editor_short_form.py`
- `tests/test_video_editor_website_workflow.py`
- `tests/test_video_editor_interface_handoff.py`
- `tests/test_video_editor_release.py`
- `tests/video-editor/hyperframes-v0840-acceptance.sh`

Representative routing cases are stored in:

`references/routing-fixtures.json`

Golden workflows are stored in:

`examples/video-editor/golden-fixtures.json`

## Upgrade procedure

Do not update HyperFrames because a newer release exists.

For any provider upgrade:

1. inspect the current upstream release and immutable source;
2. diff the provider contract against the accepted version;
3. run Nate baseline behavior and mirror checks;
4. inject the candidate only into an isolated test copy;
5. run transcript, lint, `check`, preview and render gates;
6. inspect representative frames;
7. assert video/audio streams and A/V synchronization;
8. confirm no Nate editorial rule was flattened or transferred;
9. update exact source pins and provenance only after acceptance passes;
10. keep the last proven-compatible version if the candidate fails.

## Deduplication procedure

A public capability may be removed only after:

1. exact overlap is documented;
2. unique useful behavior is identified;
3. required behavior is migrated;
4. public compatibility is handled;
5. regression tests prove no capability loss.

Do not delete specialist backends merely to make the registry smaller.
