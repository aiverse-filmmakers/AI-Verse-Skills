# Finished Video Production: This Package's Storyboard and Prompt Compiler

## When to use

Run only after script facts, directing decisions, character, scene and prop locks, total duration, and segment entry and exit states are clear. The prompt encodes decisions already made; it does not invent story or shots at the last moment.

## Inputs

- Script facts, verbatim dialogue, and user locks.
- `DIRECTOR_SHOT_PACKAGE`.
- Character, scene, prop, and light states.
- Total duration, aspect ratio, frame rate, and known platform limits.
- Previous segment exit state and next segment entry state.

## Five-column human-readable storyboard

Each row is one real, continuous shot. Default to five columns; a valid format locked by the user takes priority.

| Time | Shot size / camera position | Camera | Image and action | Dialogue / sound |
|---|---|---|---|---|

- Time: provide complete start and end seconds, with no gaps or overlaps, adding up to the segment duration.
- Shot size / camera position: shot size, direction, height, tilt, and focal length.
- Camera: fixed, or the specific movement's start, trigger, path, speed, end, direction, and focus handoff.
- Image and action: character positions and orientations, phases of action, prop state, environmental feedback, and exit state.
- Dialogue: preserve verbatim and check that it fits the time window at a natural speaking rate with pauses.
- Sound: ambience, action, dialogue, music entrances and exits, and handoffs across cuts.

## Ten-item information core

Every formal prompt must contain all ten categories inside its six outer modules:

1. Duration, aspect ratio, frame rate, and cut plan.
2. Subject identities, appearance locks, and scene space.
3. Action events, phases, physical objectives, and results.
4. Shot size, camera position, focal length, focus, and camera behavior.
5. Light sources, color temperature, lighting ratio, color areas, and exposure.
6. Materials, contact, weight, inertia, and physical prohibitions.
7. Observable emotional progression and changes in relationship or power.
8. Final-frame character position, pose, props, light, background anchors, and entry to the next shot.
9. Ambience, action sound, dialogue, music, and pauses.
10. General, scene, action, continuity, text, watermark, and generation-failure constraints.

## Six outer modules

1. **Generation task**: segment objective, duration, aspect ratio, actual internal shot count, and generation method.
2. **Main subjects**: identity, current state, performance, and locked features of characters, creatures, or equipment.
3. **Scene state**: world coordinates, left and right, depth, fixed anchors, props, environment, and light sources.
4. **Emotional objective**: audience information, emotional progression, relationship or power change, and endpoint.
5. **Visual style**: cinematography, composition, optics, light, color, materials, motion quality, and negative boundaries.
6. **Segmented script**: shot-by-shot timing, camera, visible action, dialogue, sound, cuts, and continuity handoffs.

All six modules must appear; the ten items are their internal information core and must not be expanded into additional sections seven through ten.

When the user specifies one total duration, first deliver one complete master prompt with the six modules appearing once. Generation calls may be split by shot or group to accommodate verified model limits, but internal production splitting must not change the requested total duration, shot order, or direct-delivery format. If separate production units are needed, append them rather than replacing the master prompt. Use natural names for characters, places, and props in user-visible text; keep internal asset numbers, contract IDs, paths, and review fields in production records.

Each segment heading must directly show shot size and focal length, camera direction, height and tilt, camera path and orientation, speed, focus or occlusion handoff, and action endpoint. Preserve the selected cinematography shot by shot; do not compress compound movement into a generic “follow,” or add movement to a fixed shot. Reconstruct the camera, character actions, and ending state from the final text alone, then compare against the director package for omitted detail, lost wording, or structural drift.

## World and continuity

First establish fixed world coordinates. Then recalculate screen left and right, depth, occlusion, entrances and exits, eyelines, and illumination for every camera position. Do not move the room merely to preserve screen left and right. Each shot must inherit the previous shot's character, prop, environment, light, and sound states and specify its own exit state.

## Twelve completion gates

1. Script facts, dialogue, and user-locked order are unchanged.
2. Each shot has a distinct function, reason to enter, and reason to leave.
3. Blocking and camera together express the dramatic change.
4. Shot sizes, positions, focal lengths, focus, and movement are not mere rotation of terminology.
5. The timeline closes completely and shots are not mechanically equal in duration.
6. Dialogue fits its time window with room for action and breath.
7. World coordinates, axis, eyelines, entrances and exits, and occlusion are consistent.
8. Character identity, position, pose, and performance state are continuous.
9. Prop holder, orientation, visible side, and changes of state are traceable.
10. Light sources have an on-screen or world basis, with consistent direction and shadows.
11. Sound has a source, entrance, exit, and handoff across cuts.
12. The five-column table, six modules, and ten items are complete; negative constraints address real risks.

If any gate fails, return to the corresponding design layer and repair it. Complete fields, successful platform submission, or one attractive frame do not constitute a pass.

## Output

The following are internal materials needed for compilation; they cannot substitute for the result requested by the main task. A finished-video task still delivers a playable video. If the user explicitly requests only the prompt, deliver only the complete copyable prompt and keep the five-column table, states, and check receipts internal rather than automatically sending them. User-locked table formats and limited revision scopes likewise take precedence.

- Complete five-column human-readable storyboard.
- One complete six-module master prompt covering the requested total duration, with production units appended only when execution requires splitting.
- World state and handoffs between adjacent segments.
- Receipts for timeline closure, six modules 6/6, ten items 10/10, and the twelve completion gates.
