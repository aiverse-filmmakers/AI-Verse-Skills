# Qualified Video Acceptance Gates

## Contents

1. Status definitions
2. Hard gates
3. Full playback review
4. Failure and fallback

## 1. Status definitions

- **Qualified final video**: every hard gate has passed, the entire video has been watched, and necessary repairs have been completed.
- **Candidate final video**: the file is playable and has passed internal checks, but aesthetic judgments still await user confirmation.
- **Incomplete / awaiting verification**: generation, editing, sound, full rendering, full playback review, or evidence for any hard gate is missing.

The user's final confirmation outranks internal judgment. Do not represent an internal pass as user acceptance.

## 2. Hard gates

### A. Story clarity

- The audience can understand what happens without reading the prompt.
- Character objectives, key actions, changes in information, and emotional turns are visible on screen.
- The shots do more than display visual assets.

### B. Shot design

- In autonomous mode, each short segment contains at least 7–8 effective shots, unless the user explicitly requests a long take.
- Shot durations are not mechanically equal.
- Each cut is motivated by action, eyeline, sound, an object, reaction, space, or a change in information.
- Repeated compositions, digital zooms, or crops that add no information do not count as shots.

### C. Continuity

- Character identity, clothing, anatomy, and major performance states are credible.
- Blocking, direction of movement, the main axis, and entrances and exits do not jump without cause.
- Prop appearance, possession, and states before and after actions do not reset.
- Light has a source; its direction, color temperature, and response on materials do not change without cause across cuts.
- Adjacent shots connect through action, eyeline, sound, or information.

### D. Generation quality

- No immediately obvious serious face changes, extra limbs, melting, object penetration, teleportation, flicker, or sudden changes in background structure.
- Actions have preparation, contact, force, result, and environmental feedback rather than drifting.
- Key subjects are clear; composition and shot size serve the story.

### E. Editing and rhythm

- The result does not feel like unrelated AI demonstrations joined together.
- The sequence of action, reaction, and information makes sense.
- Pauses are held when needed, and momentum does not drag when the story should move forward.
- Transitions do not conceal missing story.

### F. Sound

- Dialogue is clear and, where lip sync is required, synchronization is credible.
- Ambience and effects reflect space, distance, and action.
- Sound bridges, silence, and transitions support continuity.
- No unauthorized music, subtitles, or narration appears.

### G. Real delivery

- The final file opens and plays and has the correct duration and aspect ratio.
- The final render itself has been watched, not just the source clips, timeline, or extracted frames.
- The final delivery is video, not a prompt, still image, animatic, test clip, or report.

## 3. Full playback review

Perform at least two passes:

1. **Audience pass**: watch at normal speed without pausing; judge story, emotion, rhythm, and the first point where the viewer loses confidence.
2. **Quality pass**: check every cut, character, action, prop, space, light, sound, and generation artifact.

Add frame by frame or slow motion inspection when needed, but do not substitute extracted frames for full playback.

Record the first viewer-rejecting issue, its impact, the repair, and the result of reviewing again after repair. Without a rewatch, the repair loop is not complete.

## 4. Failure and fallback

Do not deliver as a qualified final video if any of these occur:

- A segment was made as a single long take by default.
- Multiple single-shot clips were joined directly at fixed durations.
- Only technical parameters, file existence, or automated checks passed.
- The final render was not watched in full.
- User-locked structure was changed without authorization.
- Generation permissions, spending authorization, or publishing permission were not obtained.
- Significant continuity errors or generation artifacts remain visible.

Return to the earliest failing layer: redo directing judgments if the script was misunderstood; redesign the shot group if shot design failed; repair the prompt if the mapping omitted decisions; regenerate only failed shots when material fails locally; re-edit while retaining acceptable material when the edit fails. Do not patch over an upstream problem downstream.
