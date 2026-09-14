---
name: edit-video
description: Edit a raw talking-head video through transcription, silence trimming, mistake review, visual storytelling, motion graphics, and verified HyperFrames rendering. Use for a complete edit; route a single requested operation directly to its specialist skill.
---

# Edit a video

Keep each project in `video-projects/<slug>/`, preserving the source recording.
Read the workspace guide and the project's brief or DESIGN.md. Preserve any locked editorial or visual direction. If a visual direction is missing, route through the Video Editor style/visual-direction stages rather than assuming Nate's example-project style registry exists.

1. Inspect duration, streams, and source resolution with ffprobe. Copy the source
   into the project's assets or reference an explicitly provided local path.
2. Reuse a matching word-level transcript when one exists. Otherwise route through the AI-Verse transcription capability/provider available in the current runtime. Normalize provider output before downstream editing. Check credentials or local dependencies first, and explain uploads/costs before any service call whose authorization is still missing.
3. Read `../cut-silences/SKILL.md`. Produce an EDL and a retimed transcript, and
   render the silence pass when editing is authorized.
4. Read `../cut-mistakes/SKILL.md`. Inspect candidates in context and preserve
   intentional emphasis. Record the reviewed cuts. If no mistakes need cutting,
   carry forward the silence output. Match every transcript to its actual video.
5. Read `../video-storytelling/SKILL.md` for the visual arc and
   `../hyperframes-video-beats/SKILL.md` for overlays. Write a beat sheet with
   transcript anchors, one visual idea per beat, and deliberate callbacks.
6. Read the Video Editor ownership/runtime contract, the accepted canonical HyperFrames provider, and relevant GSAP guidance before authoring. Use the package-local style specialist when available. Localize every asset used by the composition. Provider/runtime rules outrank obsolete Nate-era HyperFrames instructions.
7. Run preflight, `npx hyperframes lint`, and current `npx hyperframes check` from the project, plus the transcript-sync validator for anchored sub-compositions when applicable. Review Studio/preview before the draft.
8. Render a draft, inspect encoded frames and transitions, and listen across cut
   boundaries. Check face framing, text legibility, black frames, and A/V sync.
   Resolve failures before the final render. Follow any review approvals already
   provided; do not repeat approval requests for the same authorized action.

Deliver the final MP4 path, edit decisions, retimed transcript, composition,
and `VERIFY.md` describing what was checked and any remaining limitations.
An automated detector proposes edits; editorial judgment remains necessary.


## AI-Verse Adaptation Notes

This specialist is adapted from Nate Herk's MIT-licensed `edit-video` Skill at commit `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`.

Preserved:
- stage ordering;
- transcript-first edit truth;
- silence then mistake review;
- storytelling and motion-beat planning;
- draft render plus encoded-frame/audio verification;
- editorial judgment over automated detections.

Adapted:
- removed Nate-workspace-specific API-key/setup file dependency;
- removed dependency on Nate's old bundled HyperFrames technical Skill;
- current HyperFrames provider uses `lint -> check -> preview -> render`;
- visual/style routing now goes through AI-Verse Video Editor boundaries.
