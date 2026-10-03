# Multi-Image and Reference Behavior

Status: RUNTIME KNOWLEDGE
Task: 6.9

Purpose: define how the skill handles several images or references without blending identities, copying incidental content, inventing reference roles, or allowing one reference to silently override explicit target locks.

Use with:

- `schemas/reference-dna.schema.json`
- `references/workflows/reference-match.md`
- `references/locks.md`
- `references/confidence-and-uncertainty.md`
- `references/reality-gate.md`

## Core Rule

```text
Every reference must have a role.
Target locks outrank reference tendencies.
Observable DNA may transfer; hidden metadata may not be invented.
```

## Supported Reference Roles

A reference may control one or more dimensions:

```text
identity
product identity / geometry
composition
camera position / perspective
pose / action
wardrobe
location / environment
production design
lighting
exposure / tone
color / grade
lens character
depth / bokeh
texture / finish
material response
atmosphere
overall visual language
edit target
```

Do not treat all uploaded images as equal `style references`.

## Role Resolution Priority

Assign roles in this order:

1. explicit user instruction;
2. clear task semantics;
3. safe AUTO inference;
4. ask one focused question only if conflicting plausible roles would materially change the result.

Example:

`Use image 1 for the woman, image 2 for the dress, image 3 for the lighting.`

This creates three distinct bindings. Do not average them together.

## Identity Reference

When a reference controls identity:

Preserve:

- facial structure;
- age impression;
- body proportions when visible/relevant;
- hair identity where requested;
- distinctive non-sensitive appearance traits;
- expression only if requested or part of the target moment.

Do not automatically copy:

- background;
- lighting;
- clothing;
- camera angle;
- color grade;

unless those dimensions are also assigned.

## Product Reference

Product identity has strict geometry and branding priority.

Preserve where visible/requested:

- silhouette;
- proportions;
- packaging geometry;
- label/logo placement;
- material/color identity;
- functional details.

Do not redesign the product to make it more cinematic.

Lighting, environment, lens and camera position may change only within the requested brief.

## Location / Environment Reference

Transfer:

- spatial layout when relevant;
- architecture;
- material palette;
- environmental structure;
- atmosphere only if assigned.

Do not automatically copy people, vehicles, signs, or incidental foreground objects.

## Style / Visual-Language Reference

Extract observable DNA:

```text
composition
perspective behavior
lighting geometry
contrast/exposure
color relationships
depth
optical behavior
texture/finish
material response
atmosphere
```

Do not assume the exact camera, lens, LUT, film stock, or proprietary process unless supplied by metadata/user/source.

## Multiple References for the Same Role

When several references control the same dimension:

### Compatible references
Synthesize common traits.

Example:
- both use low camera height, broad natural daylight, restrained saturation.

### Complementary references
Use explicit weighting or scoped transfer.

Example:
- ref A controls composition;
- ref B controls color and light.

### Conflicting references
Do not average incompatible features blindly.

Resolve using:

1. user priority;
2. target constraints;
3. dominant reference if one is clearly designated;
4. safe AUTO weighting if conflict is minor;
5. one focused question if conflict is major and materially changes the result.

## Reference Priority

A host/runtime may represent priority numerically, but the reasoning meaning is ordinal:

```text
primary
secondary
supporting
```

Do not expose fake precision such as `72% style from image 1` unless the provider actually supports a meaningful blend control and the adapter owns that syntax.

## Frozen-Moment Multi-Camera Case

If the user provides a scene reference and requests new camera angles of the exact same instant:

Lock:

- subject positions;
- body/limb pose;
- gaze;
- expression;
- object positions;
- environment;
- lighting state;
- time/moment.

Change only:

- camera position;
- camera height/angle;
- framing;
- visible occlusion due to the new viewpoint;
- perspective that necessarily follows the new camera position.

Hard rule:

```text
same frozen moment = scene stays fixed; camera moves
```

Do not turn it into a character turnaround or action sequence.

## Edit Target + Supporting References

When one image is the edit target and others are references:

- the edit target owns scene continuity by default;
- supporting images may supply identity, material, product, or visual DNA;
- supporting references do not authorize broad scene replacement.

REALITY REPAIR must preserve the edit target unless change is required by the repair list.

## Missing / Unusable References

Never pretend a reference is available when it is not accessible in the active host context.

If the user refers to `the last image` but the host cannot actually access it:

- do not fabricate its content;
- use any explicit description available;
- if exact visual continuity is required, request the missing image/identifier only when necessary.

## Provider Adaptation

Adapters may differ in:

- maximum reference count;
- identity/reference weighting;
- image-role syntax;
- regional editing;
- style/image-strength controls.

The universal system must preserve the role map even if the adapter must reduce or serialize the references differently.

If a provider supports fewer references than supplied:

1. preserve hard identity/product/edit-target references first;
2. preserve the highest-priority visual references;
3. convert lower-priority references into textual observable DNA where possible;
4. disclose any material dropped capability.

## Multi-Reference Reality Gate

Check:

- each reference had a role;
- identities/products were not blended accidentally;
- target locks outranked style references;
- reference-specific incidental content was not copied without instruction;
- conflicting references were resolved explicitly;
- exact hardware was not hallucinated;
- provider limits did not silently change priorities;
- frozen-moment tasks did not drift pose/action/time.

Acceptance: the skill can use one or many references with explicit role separation, priority, conflict handling, preservation, and truthful provider degradation.