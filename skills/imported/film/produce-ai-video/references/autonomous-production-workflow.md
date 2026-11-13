# Auditable Decision Chain for Autonomous Video Production

## Contents

1. Objective and facts
2. Script interpretation
3. Directing decisions
4. Shot group design
5. Prompt mapping
6. Generation and editing
7. Repair and review loop

## 1. Objective and facts

First reduce the task to an observable result: the audience should see a playable finished video that tells the story clearly, has fluid shots, credible continuity, and complete sound.

Establish four columns:

- **Verified facts**: current script, characters, locations, props, timing, approved assets, and user-locked structure.
- **Unknowns**: unresolved matters that affect story, cost, permissions, or delivery.
- **Assumptions**: provisional decisions made to move forward that later footage can disprove.
- **Conventions**: previous projects and industry practices are candidates, not replacements for judgment about the current story.

The contracts in this package supply experience, failure examples, and methods. The script supplies the facts for this production. Directing judgment determines the shot design.

## 2. Script interpretation

For each generatable segment answer:

1. What is the single dramatic event in this segment?
2. What does each character want at this moment?
3. Who controls the space, and when does control change?
4. What action actually changes the situation?
5. What information must the audience see clearly?
6. At what moment does the emotion turn?
7. At what moment does sound enter, interrupt, or continue?
8. What are the segment's entry and exit states?

If these answers are unclear, do not proceed to prompting.

## 3. Directing decisions

Decide the audience's viewing path before choosing the camera:

- Does the audience first learn about the space, character, action, object, or reaction?
- What information should be hidden, and when should it be revealed?
- Which character owns the center of the frame, and when do they lose it?
- Which action should be shown in full, and which can be conveyed through detail, reaction, or occlusion?
- Which cut reduces the number of visible states the generation model must maintain simultaneously?

Continuity is not pixel continuity. It means that world coordinates, character identity, action causality, prop state, light direction, and sound space remain credible. Shots may change frequently, but after each camera change recalculate screen left and right, depth, occlusion, entrances and exits, and illumination.

## 4. Shot group design

### Hierarchy

`Script event → short segment → at least 7–8 effective shots → generated material → edited segment → longer finished video`

An effective shot must satisfy all of these:

- It is a distinct, uninterrupted viewpoint.
- It has a distinct shot size, angle, camera behavior, or visual subject.
- It gives the audience new information, a stage of action, an emotional reaction, or a spatial relationship.
- It has a reason to enter and a reason to leave.

Repeated crops, moves that change no information, or new wording for the same camera position do not count as new shots.

### Common coverage functions

Choose according to the script, without applying them mechanically. In autonomous mode the total must nevertheless be at least 7–8 shots:

1. Establish space or relationships.
2. Show subject intention or the start of an action.
3. Show a key action relationship.
4. Show a bodily, prop, or environmental detail.
5. Show another character's reaction.
6. Show a reverse angle, eyeline destination, or power shift.
7. Show the result of an action or an emotional turn.
8. Hand off visually or through sound to the next segment.

Shot durations are determined by audience comprehension, performance, action, dialogue, emotional pauses, and editing rhythm, and must not be evenly divided mechanically. Model duration constrains submission method, not the director's timing decisions.

### DIRECTOR_SHOT_PACKAGE

Record at least the following for each segment:

- Dramatic objective.
- Total duration.
- Entry and exit states.
- Locked world space and lighting.
- Shot numbers and nonuniform timing.
- Shot size, camera position, focal length, and camera movement.
- Visible action and performance.
- Dialogue, sound, and pauses.
- Motivation for the edit.
- Continuity handoffs to and from adjacent segments.

## 5. Prompt mapping

The prompt encodes decisions already made by the director; it does not invent shots at the last moment.

Use the six outer modules and ten-item information core bundled in this skill:

1. Generation task: specify that this is a short segment containing at least 7–8 internal shots, not a default long take.
2. Main subjects: include only visible identity, state, and performance constraints.
3. Scene state: describe world space, orientation, props, and light sources.
4. Emotional objective: describe observable emotional progression and power changes.
5. Visual style: describe cinematography, materials, color, movement, and negative boundaries.
6. Segmented script: map timing, shot size and camera position, camera, action, sound, cuts, and handoffs shot by shot.

Each time block in the segmented script must correspond to a real shot. Do not disguise action phases such as increasing light or falling stone dust from one camera position as multiple shots.

## 6. Generation and editing

Preserve the directing plan first, then adapt to the tools:

- If the model can reliably execute multiple shots, generate with one segment-level prompt and check that every internal shot actually appears.
- If it cannot, generate individual shots or small shot groups while preserving identity, space, and light locks, then edit them into the designed segment.
- If platform limits require splitting, split execution batches, not dramatic structure.

Prefer action, eyeline, objects, occlusion, sound, and changes in information as edit points. Adjacent shots need only carry forward the necessary current state reliably; do not force the model to preserve every pixel.

## 7. Repair and review loop

After watching the complete video, prioritize the earliest point where the audience loses trust:

1. The story cannot be understood.
2. Characters or space break continuity.
3. Action causality fails.
4. Performance or pacing fails.
5. Obvious generation artifacts appear.
6. Sound feels pasted on or discontinuous.
7. Minor visual flaws.

In each round, first fix the earliest, most consequential viewer-rejecting issue, then watch the entire video again. A local pass does not mean the whole video passes.
