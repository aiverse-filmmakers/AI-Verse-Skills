---
name: ai-video-director
description: Direct AI video from an existing story, script, brief or approved creative plan. Use for shot design, storyboards, AI video prompts, continuity, or producing a finished AI video when suitable tools are available. For screenplay creation or diagnosis use a screenplay specialist if available; for editing supplied footage use a video editor when appropriate. Replaces the retired produce-ai-video and ai-storyboard-director skills, so use it when either old name is asked for.
license: Apache-2.0
---

# AI Video Director

Turn the user's story or approved creative direction into the requested shot design, video prompts, or playable video. A storyboard request, prompt request, limited revision, and finished film are different jobs. Deliver the requested outcome; planning artifacts do not substitute for a finished video.

## Where this skill sits in the filmmaking chain

When a story is not settled, `director-agent` plans it first, including each character's objective, action verb and reaction. This skill then decides the deliverable and designs the shots. For any shot with a character, hand the performance to `higgsfield-acting` when it is available. For a Seedance prompt, `ai-realism` assembles the final prompt in its fixed block order and formats each prompt in a code block. `video-editor` owns editing of real footage. Do not skip a step that applies; if a named skill is not installed, say so and do that step plainly yourself. The user's creative brief and locked references outrank all of them.

## First choose the task

- **Shot design or storyboard**: create an understandable, actionable shot plan. Provide prompts only when requested or clearly needed for the intended generation workflow.
- **Prompt only**: deliver the requested copyable prompt or prompts. Do not generate media or add an unsolicited storyboard.
- **Review or revise**: identify the specific issue and change only the requested scope, preserving approved shots and other locks.
- **Actual video**: plan, generate, select, edit, sound, review, repair and deliver actual playable media when the necessary tools, permissions and resources exist. Read [production workflow](references/video-production.md).

A brief or existing script can be enough to start. If no screenplay exists, work from the supplied idea at the requested scope; for substantial screenplay writing or diagnosis, use an available screenplay specialist or explain the limitation. Do not require the user to fill out an internal form. Ask only when a missing fact, creative choice, cost, access or permission would materially change the result.

## Preserve creative authority

Treat the current user request, approved script, dialogue, reference roles, shots, sequence, timing, staging, visual locks and explicitly requested output as authoritative. Distinguish source facts, decisions, assumptions and unknowns. Do not add new story, people, dialogue, locations, props or outcomes merely to make a shot more interesting. An image or video reference controls only what the user assigned it to control; do not import unrelated faces, objects, brands, sound or style from a motion reference.

In autonomous work make ordinary directing choices yourself within the brief. When the user has locked creative choices, inherit them and change only what was requested. Explain any material conflict before changing a locked decision. Never treat a tool, package, example or past project as permission to spend, upload private assets, publish, or change an account.

## Direct the sequence

1. Read the relevant story and identify what changes, what characters want and do, what the audience needs to see, and any fixed assets and constraints. Preserve exact dialogue unless revision is authorized.
2. Design the sequence from story and physical action. Choose the number and duration of shots for the scene, performance, readability and brief. A long take, a few shots, or a more detailed sequence may be right. No minimum shot count or equal shot duration is required.
3. Establish the needed world state: location, subject positions and orientation, meaningful landmarks, props and holders, action axis, light sources and relevant environment. For each camera change derive framing, left and right, eyelines, occlusion, entrances, exits and illumination from that same world rather than moving objects to preserve screen labels. Check whether the cut itself preserves intelligible direction.
4. Design blocking and camera together. Use shot size, position, optics, focus, movement and edits only when they serve a visible action, relationship or reveal. For a complex move specify the start, trigger, route, handoffs, speed and endpoint. Make fine action, contact and reactions readable with enough time.
5. Produce only the requested deliverable. A time, shot size or position, camera, visible action, dialogue and sound table is useful when a storyboard is requested; adapt the format to the user's brief. If a prompt is requested, include the subject, action, setting, camera, lighting, timing, sound and relevant continuity constraints that the chosen task needs. Preserve selected shots during compilation. Use natural names in member-facing prompts, keeping internal IDs and review records out unless requested.
6. If a user explicitly asks for one prompt covering the whole duration, provide one complete prompt. If separate shot prompts are requested, provide self-contained prompts per shot with the required identity, wardrobe, location, visual continuity, camera, action and start/end state. Split generation into workable units when verified platform limits require it, while preserving the requested structure and explaining a consequential change.
7. Check source facts, dialogue, user locks, shot order, action causality, timing, spatial projection, character and prop continuity, lighting and any requested format. Use [production contract](references/production-contract.md) for the shared storyboard and prompt checks. For demanding shot design read [shot design](references/shot-design-engine.md), [cinematography](references/cinematography-design-engine.md) and [framing and axis](references/framing-and-axis.md) as needed. Examples and reference rules inform judgment; they are not mandatory output templates or authority to override the user.

## Project continuity

For a clearly identified project with a real need to resume across sessions, preserve the source, approved choices, shot and scene states and unresolved items in its authorized project location. Use an existing project system when suitable. The optional bundled `scripts/design_memory.py` and [memory protocol](references/design-memory-protocol.md) offer a local structured record; use them only if their format and write permissions fit the project. Read the protocol first. An unavailable or failed helper must be reported, not treated as a successful save. Its structural checks cannot prove shot quality or video success. A one-off consultation does not require a project folder.

## Execution and handoff

Choose tools actually available in the current host. Do not assume Codex, a specific video model, an external account, paid generation, editing software or a successful connection. Confirm material spending or external access within the user's authorized scope. Use the existing Video Editor skill when available for editorial work; it owns source and transcript timing, edit decisions, caption timing, synchronization and edit verification. Pass the locked creative plan and constraints; do not let a handoff silently change them. If that skill is unavailable, use a suitable available editing route or state the limitation.

For a finished video, inspect real generated material, assemble and render it, then watch the complete final file and check sound when the host permits. Report whether the result is a reviewed final, a playable candidate needing judgment, or incomplete/unverified. A file, prompt, still, preview or automated check alone cannot prove the film is finished or accepted. If generation, playback, sound inspection, permission or a hard requirement is unavailable, provide the useful completed work and clearly name what remains.
