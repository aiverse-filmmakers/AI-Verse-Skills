# Generic Provider Adapter

Status: RUNTIME ADAPTER
Task: 7.1

Purpose: translate the provider-neutral Cinematic Shot Spec into a strong natural-language image-generation or image-editing instruction when the target provider is unknown, changed, unsupported, or exposes no verified special controls.

This adapter is the mandatory fallback for all provider uncertainty.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
Generic Adapter = translation layer
```

The adapter may serialize and rephrase the shot. It may not silently redesign it.

## When to Use

Use `generic.md` when:

- no provider/model is named;
- the host exposes a generic image tool with no known provider semantics;
- a named provider/model is newer or different from the verified adapter;
- provider capabilities cannot be checked confidently;
- provider-specific syntax/control support is uncertain;
- a text-only user wants a portable prompt.

## Input

Primary input:

- resolved `Cinematic Shot Spec`;
- active workflow;
- user/preservation locks;
- optional reference-role map;
- host capability class;
- V0 Reality Gate result.

Do not consume raw user text alone when a resolved shot spec already exists.

## Natural-Language Serialization Order

Use this order as a strong default, omitting irrelevant sections:

```text
1. subject and action / moment
2. environment and story context
3. composition, shot size, camera position and perspective
4. capture/lens/focal/depth behavior
5. motivated lighting and exposure
6. color, white balance, tone and grade
7. skin, hair, fabric, materials and physical realism
8. motion, atmosphere and justified capture texture
9. preservation/change instructions for edits
10. output format / aspect / orientation
```

This is an ordering heuristic, not mandatory visible headings.

## Prompt Style

Prefer:

- clear natural language;
- concrete visible relationships;
- physical descriptions;
- positive desired-state language;
- concise technical cues when they materially affect the image;
- direct spatial instructions.

Avoid:

- prestige-word keyword piles;
- `masterpiece`, `award-winning`, `8K`, `ultra cinematic` as substitutes for visual design;
- duplicated synonyms solely to inflate the prompt;
- fake provider parameters;
- unsupported negative-prompt syntax;
- exact hardware claims inferred only from references.

## Camera / Lens Translation

If a camera/lens name is locked:

- preserve the literal name when useful;
- immediately express the desired observable behavior where it improves portability.

Example:

```text
ARRI ALEXA 35 character: controlled highlight transition, natural skin separation, dense but open shadows, restrained digital sharpness
```

Do not claim the provider physically simulates that sensor.

If provider support for the literal name is unknown, observable behavior remains authoritative.

## Perspective Translation

Always express camera geometry concretely when it matters.

Prefer:

```text
camera close to the foreground subject at low height, wide rectilinear field of view, strong near/far scale difference, straight background architecture without fisheye curvature
```

rather than only:

```text
14mm cinematic lens
```

Focal length supplements camera position; it does not replace it.

## Depth Translation

Describe:

- focus target;
- relative subject/background distances;
- shallow/moderate/deep focus behavior;
- continuous focus falloff.

Avoid generic `beautiful bokeh` unless bokeh is a real creative requirement.

## Lighting Translation

Serialize lighting through:

```text
motivation
source direction
apparent size / softness
falloff
fill / negative fill
ambient contribution
practicals
edge/back light only if motivated
exposure consequence
```

Do not write `cinematic lighting` alone.

## Color / Grade Translation

Describe visible relationships:

- white-balance intent;
- warm/cool source relationship;
- saturation level;
- color separation;
- skin/product color preservation;
- black density;
- highlight rolloff;
- neutral vs stylized grade.

Never impose teal/orange by default.

## Physical Realism Translation

Use positive desired states.

Examples:

Instead of:
```text
no plastic skin
```

Use:
```text
natural region-specific skin texture, subtle color variation, source-consistent specular response, age-appropriate detail
```

Instead of:
```text
no fake fabric
```

Use:
```text
fabric with weight-appropriate folds, compression at contact points, scale-appropriate weave and material-specific roughness
```

## Texture / Effects Translation

Grain, sensor noise, halation, bloom, flare, haze, diffusion, scratches or VHS artifacts are included only when justified by the shot spec.

Unknown provider does not justify adding more effects.

## New Generation Template

Conceptual template:

```text
[subject/action] in [environment/context].
Camera: [position/height/angle/shot/framing/perspective].
Optics: [format/lens/focal/depth/focus behavior].
Lighting/exposure: [motivated sources, direction, softness, contrast, exposure hierarchy].
Color/tone: [WB, palette, separation, saturation, density, highlights/shadows].
Physical realism: [only relevant skin/material/contact/reflection requirements].
Texture/atmosphere: [only justified effects].
Output: [aspect/orientation/composition constraints].
```

The final prompt may be prose rather than labeled sections.

## Edit / Reality Repair Template

Always structure semantically as:

```text
PRESERVE
- ...

CHANGE
- ...

DESIRED PHYSICAL RESULT
- ...
```

Even if the provider receives one prose prompt, this internal separation must remain.

Do not turn a local repair into a whole-image redesign.

## Reference-Conditioned Template

For each reference, preserve the role map:

```text
Reference 1: identity only
Reference 2: product geometry/material only
Reference 3: lighting/color visual language
Target image: composition/environment/edit continuity
```

If provider-specific role syntax is unavailable, state the roles in natural language.

## Negative Prompt Policy

Default: do not assume negative-prompt support.

Translate avoidances positively.

If a later provider-specific adapter confirms negative prompts, that adapter may add a dedicated negative field.

## Unsupported Controls

If the shot spec contains a control with no generic equivalent:

1. identify the observable intent;
2. express it naturally;
3. preserve the original lock internally;
4. mark it as semantic translation if structured output is exposed;
5. do not fabricate a control name.

## Host Capability Degradation

### Image-capable host
If the user asked for an image and host policy permits execution, the generic prompt may be sent to the available image tool.

### Vision-only or text-only host
Return the generic prompt/spec. Never imply generation occurred.

### PROMPT ONLY
Return prompt/spec regardless of tool availability.

## Verification

Before handoff:

- all explicit locks preserved;
- no provider-specific syntax invented;
- shot intent survived serialization;
- edit preserve/change boundary survived;
- reference roles survived;
- no mandatory cinematic cliches added;
- Reality Gate issues translated into corrections rather than hidden.

## Fallback Guarantee

Every Phase 7 provider adapter must be able to fall back to this file when:

- the current model changed;
- a capability is missing;
- documentation is stale;
- the host exposes only generic text prompting.

Acceptance: an unknown provider still receives a coherent, portable, physically grounded cinematic prompt without provider-core contamination or fabricated controls.