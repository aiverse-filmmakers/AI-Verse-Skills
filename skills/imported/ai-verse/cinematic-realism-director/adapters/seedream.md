# Seedream Image Adapter

Status: RUNTIME ADAPTER
Task: 7.4
Verified against current first-party BytePlus / Seedream documentation: 2026-10-03

Purpose: translate the provider-neutral Cinematic Shot Spec into Seedream generation/editing instructions while preserving shot intent, target locks, and edit boundaries.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
Seedream adapter = provider translation + optional spatial editing
```

If the current Seedream host does not expose a documented feature, fall back to natural language or `adapters/generic.md`; never invent API syntax.

## Current Verified Surface

Current Seedream 5.0 Pro / Flash documentation supports, depending on the active model/host:

- text-to-image;
- single-reference generation/editing;
- multiple-reference generation;
- interactive editing using normalized point and bounding-box targeting;
- explicit unchanged/preserved regions;
- precise local modifications;
- current 5.0 Pro/Flash image-generation APIs;
- layer decomposition on supported 5.0 Pro workflows.

Current BytePlus documentation states that 5.0 Pro/Flash can use multiple reference images for a single output and that interactive editing can target regions using coordinates/annotations. These are provider capabilities, not core assumptions.

## Provider Selection Rule

When Seedream is active:

1. resolve the universal shot first;
2. determine whether the operation is generation, reference-conditioned generation, or edit;
3. use exact spatial controls only when the host exposes them;
4. otherwise serialize the same intent in natural language;
5. preserve all hard locks and preserve/change boundaries;
6. use `generic.md` for unverified model-specific behavior.

## Generation Prompt Structure

Prefer direct visible instructions:

```text
subject / action
scene / environment
composition / camera geometry
lens / focal / depth behavior
motivated lighting / exposure
color / tone
skin / materials / physical realism
reference roles
output framing
```

Seedream should not receive empty cinematic prestige keywords in place of physical instructions.

## Reference-Conditioned Generation

When multiple references are actually supported, preserve explicit roles:

```text
Reference A -> identity only
Reference B -> product geometry/material only
Reference C -> location/environment only
Reference D -> lighting/color/style only
```

Do not rely on reference order alone to communicate authority.

If the host supports fewer references than requested:

- prioritize preservation-critical references first;
- merge compatible style/lighting references conceptually where safe;
- disclose dropped/translated reference roles;
- never silently discard identity/product locks.

## Interactive Editing

Seedream's current interactive-edit guidance supports target points and bounding boxes when the host exposes those controls.

Use them especially for REALITY REPAIR when the defect is local.

Internal procedure:

```text
1. identify exact defect region
2. identify preserve regions
3. select point/box only if host supports it
4. describe the desired physical result
5. explicitly state what remains unchanged
6. perform the smallest edit
7. run Reality Gate if the result can be inspected
```

Coordinates are provider mechanics, not cinematic reasoning.

## Spatial Edit Translation

Example conceptual edit:

```text
Target: face and visible hands only.
Preserve: identity, expression, hairstyle, clothing, camera angle, background, lighting direction.
Change: remove waxy smoothing and restore natural skin texture, subtle color variation, and source-consistent specular response.
```

If point/box controls exist, attach them to the same edit intent. If they do not, retain the natural-language instruction.

## Preservation Rule

Seedream editing should exploit explicit unchanged regions when exposed.

Never use a local edit capability to alter:

- identity;
- product geometry;
- pose;
- composition;
- wardrobe;
- text/logo;
- background structure;

unless those regions are part of the requested change.

## Layer Decomposition

If a current 5.0 Pro host exposes layer decomposition:

- treat it as an optional downstream editing convenience;
- never require it for core skill operation;
- do not infer semantic layer correctness without inspection;
- preserve the same shot spec across layer-based edits.

## Camera / Lens / Film Translation

Pass literal names when useful, but reinforce visible behavior for critical traits.

Do not assume Seedream physically simulates named hardware or film stock.

Example:

```text
35mm rectilinear perspective from a close camera position, natural edge geometry, moderate depth separation, controlled highlight rolloff, organic fine grain only if justified
```

## Negative / Avoidance Guidance

Prefer positive desired states and explicit preservation.

Do not assume a universal Seedream negative-prompt channel across every host.

## Host Degradation

### Full Seedream generation/edit host
Execute when requested and authorized.

### Seedream host without regional controls
Use natural-language editing.

### Text/vision-only environment
Return prompt/spec and optional spatial-edit instructions conceptually.

### PROMPT ONLY
Never execute.

## Version Drift Rule

Model names, limits, reference counts, and interactive-edit syntax are time-sensitive.

If the active host differs from this verified surface:

1. preserve the shot spec;
2. query actual host capability if possible;
3. use only verified exposed fields;
4. fall back to generic natural-language translation.

## Sources

Current first-party BytePlus Seedream documentation rechecked on 2026-10-03:

- Seedream user guide;
- Seedream 5.0 Pro / Flash interactive editing guide;
- Seedream image generation API documentation.

These are provenance references, not runtime dependencies.

## Acceptance

Task 7.4 passes when Seedream can use its current reference and spatial-edit strengths without moving those provider mechanics into the universal brain, and local Reality Repair remains preservation-aware and truthful about host capability.