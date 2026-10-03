# Gemini Image Adapter

Status: RUNTIME ADAPTER
Task: 7.3
Verified against current first-party documentation: 2026-10-03

Purpose: translate the provider-neutral Cinematic Shot Spec into Gemini-native image generation/editing instructions while preserving the universal shot and all user locks.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
Gemini adapter = conversational/provider translation
```

If the active Gemini image model or host differs materially from the verified surface, use `adapters/generic.md` rather than guessing.

## Current Verified Surface

Current Google AI documentation exposes native Gemini image generation and text-plus-image editing, including:

- text-to-image;
- image + text editing;
- adding/removing/modifying elements;
- style/color-grade changes;
- reference-conditioned composition;
- conversational/multi-turn refinement;
- explicit aspect-ratio output controls on current supported image interactions.

Current docs show Gemini image model names changing over time. Model identity therefore belongs to host/provider adaptation, not the core skill.

## Prompt Style

Gemini should receive direct natural-language descriptions with explicit spatial relationships.

Prioritize:

```text
subject / action
environment
composition / layout
camera position / viewpoint
materials
lighting
color / grade
reference roles
preservation constraints
output framing
```

Do not reduce the shot to aesthetic tags.

## New Generation

Serialize the resolved shot in clear prose.

Example internal order:

```text
Create [subject/action] in [environment].
Frame it as [shot/framing] from [camera position/height/angle], with [perspective behavior].
Use [lens/focal/depth behavior].
Lighting comes from [motivated source], with [fill/contrast/exposure].
Color is [white balance/palette/density/saturation treatment].
Render [relevant skin/material/contact/reflection realism].
Output [aspect/orientation].
```

Do not duplicate camera terminology when the same visible instruction is already explicit.

## Image Editing

Gemini's current image docs support natural-language edits against supplied images.

For preservation-sensitive editing, structure internally as:

```text
KEEP
CHANGE
RESULT
```

Example:

```text
Keep the exact composition, camera angle, subject pose, wardrobe, facial identity, room geometry, and lighting direction.
Replace only the chair with a pale oak chair in the same position and scale.
Match the existing perspective, contact shadows, reflections, and color temperature.
```

Prefer narrow edits over whole-image restatements.

## Conversational Refinement

When the host genuinely retains the edited image in the active interaction:

- use short targeted follow-ups;
- preserve previously accepted regions;
- correct one failure domain at a time when practical;
- rerun visual Reality Gate checks when inspection is available.

Do not assume cross-turn image persistence when the host does not expose it.

## Multiple References

Gemini can accept image inputs in supported image workflows. Preserve explicit reference roles:

```text
identity reference
product reference
location reference
composition reference
lighting/color reference
style reference
edit target
```

When the host has no formal role field, state the role in text next to the reference relationship.

Target locks always outrank transferred reference traits.

## Reference Match

Transfer observable DNA only:

- framing;
- light direction/quality;
- contrast;
- palette;
- depth behavior;
- lens-like rendering;
- texture;
- material response.

Do not claim the exact source camera, lens, stock, LUT, or aperture from visual inference.

## Reality Repair

Use the Phase 5 diagnosis and preservation boundaries before composing the edit request.

Repair order:

```text
structural geometry
-> focus/depth/motion
-> lighting/exposure
-> reflections/shadows
-> anatomy/skin/hair/eyes
-> fabric/material/contact
-> optical effects
```

Do not ask Gemini to beautify or broadly restyle a repair target unless the user requested that.

## Negative / Avoidance Guidance

Prefer concrete positive desired states.

Instead of:

```text
no fake reflections
```

prefer:

```text
reflections consistent with the camera viewpoint, surface curvature, roughness, and visible environment
```

Use explicit `do not change` wording for preservation where needed; this is distinct from assuming a provider-level negative-prompt parameter.

## Aspect / Output

Pass aspect/output controls only when the current Gemini host exposes them.

If the host offers no verified control, express framing/orientation in the prompt and record the limitation rather than inventing a parameter.

## Host Modes

### Gemini image host with generation/editing
Execute when the user asked for an image and policy/tool access permits.

### Vision-only Gemini host
Analyze references and return adapted instructions.

### Text-only host
Return prompt/spec.

### PROMPT ONLY
Never execute image generation/editing.

## Model Drift Rule

If the active model name, reference limits, or editing behavior differs from current docs:

1. keep the universal shot unchanged;
2. check actual host capability if exposed;
3. use supported behavior only;
4. fall back to `adapters/generic.md` for uncertain features.

## Sources

Current first-party Google AI image-generation documentation rechecked on 2026-10-03.

These sources are provenance only, not required runtime dependencies.

## Acceptance

Task 7.3 passes when Gemini receives strong conversational image instructions, edits remain preservation-aware, multi-reference roles remain explicit, and version/model drift cannot silently redesign the shot.