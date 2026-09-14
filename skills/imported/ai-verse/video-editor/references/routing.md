# Video Editor Routing

## Classify before editing

Choose the smallest scope matching the request.

### SILENCE_ONLY

Use when the user explicitly wants silence/dead-air removal and no broader editorial redesign.

Required truth:
- exact source identity;
- transcript or equivalent timing evidence when the specialist needs it;
- retained-order/source-time validity.

Do not add graphics merely because the Video Editor can.

### MISTAKE_RETAKE_ONLY

Use for false starts, repeated takes, stutters or spoken-error cleanup.

The mistake/retake specialist must distinguish objective repeated/abandoned speech from stylistic wording. Ambiguous semantic edits require review rather than silent deletion.

### CAPTIONS_ONLY

Preserve the existing cut. Generate/import transcript timing, author captions, then verify representative frames and encoded output.

### MOTION_GRAPHICS_ONLY

Preserve existing edit timing unless the user asks to change it. Visual specialists may help establish art direction. HyperFrames/runtime rules remain authoritative for the rendered implementation.

### SHORT_FORM_EDIT

Use for Reels, Shorts, TikTok-style edits, short paid-social video and other retention-sensitive short-form.

Own:
- opening hook;
- open loops;
- payoff;
- footage ledger/source truth;
- caption timing;
- B-roll/visual beat placement;
- sound-design plan where requested.

A vertical aspect ratio alone does not make an edit good short-form.

### LONG_FORM_TALKING_HEAD

Use for longer interviews, explainers, educational or creator talking-head material.

Preserve:
- transcript anchors;
- coherent thought boundaries;
- persistent-world/spatial storytelling when applicable;
- camera-as-edit/visual hierarchy decisions;
- listenability at cut joins.

### WEBSITE_PROMO

Use the website-to-video specialist for site capture/design extraction, script/storyboard/timing and video assembly.

Interface Designer may improve visual direction, but does not replace the video workflow.

### REFERENCE_LED_EDIT

Analyze separately:
- editorial pacing/structure;
- visual language;
- audio cues only when audio was actually inspected.

Never claim an audio-reference match from silent frames/screenshots.

### FULL_EDIT

Run the complete applicable editorial pipeline. Short-form and long-form stages are mutually selective unless the source intentionally contains both deliverable types.

## Required fail-closed behavior

If a requested specialist/provider is not registered or cannot run:

- do not fabricate its output;
- do not silently substitute Interface Designer for editorial work;
- preserve completed upstream edit truth;
- report the unavailable stage and stop before claiming final delivery.
