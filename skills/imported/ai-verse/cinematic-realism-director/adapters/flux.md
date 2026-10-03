# FLUX Image Adapter

Status: RUNTIME ADAPTER
Task: 7.5
Verified against current first-party Black Forest Labs public skill material: 2026-10-03

Purpose: translate the provider-neutral Cinematic Shot Spec into FLUX-family prompts and editing instructions while preserving the universal creative decisions.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
FLUX adapter = positive natural-language serialization
```

If the active FLUX model/host differs from verified behavior, fall back to `adapters/generic.md`.

## Current Verified Surface

Black Forest Labs' current public `flux-image-best-practices` skill covers FLUX.2 and FLUX.1 families and currently recommends a natural-language prompt structure equivalent to:

```text
Subject + Action/Pose + Style/Medium + Context/Setting + Lighting + Camera/Technical
```

The current first-party skill also states:

- do not rely on negative prompts;
- describe the desired result positively;
- be specific;
- natural language works well;
- lighting should be explicit;
- current model-family behavior differs across FLUX.2 / FLUX.1 editing and generation variants.

Model choice remains a provider concern, not a core cinematic rule.

## Serialization Order

Translate the resolved shot spec into this FLUX-friendly order:

```text
1. subject
2. action / pose / moment
3. visual medium / rendering intent
4. environment / context
5. composition / camera position
6. lighting / exposure
7. camera / lens / focal / depth
8. color / materials / physical realism
9. output constraints
```

The universal shot's geometry and light logic outrank this ordering heuristic.

## Positive Prompt Rule

When the universal diagnosis contains an avoidance, convert it into a positive physical target.

Examples:

```text
avoid plastic skin
-> natural unretouched skin with visible fine texture, subtle tonal variation, and source-consistent specular response
```

```text
no fake fabric
-> fabric with weight-appropriate folds, contact compression, scale-appropriate weave, and material-specific roughness
```

```text
no fisheye
-> rectilinear wide-angle geometry with straight background architecture and perspective exaggeration created by camera proximity
```

Do not append generic negative-prompt blocks when the active FLUX path does not support them.

## Camera / Technical Placement

Keep camera/technical language concise and physically meaningful.

Prefer:

```text
camera low and close to the foreground subject, 24mm-equivalent rectilinear field of view, moderate depth, continuous focus falloff
```

rather than prestige-token stacks.

Named lens/camera references may be preserved when user-locked, but observable behavior remains authoritative.

## Lighting

Lighting should be explicit because it strongly controls FLUX output quality.

Serialize:

```text
source motivation
source direction
softness / apparent size
fill / negative fill
ambient contribution
exposure hierarchy
```

Do not write only `cinematic lighting`.

## Text / Brand Color

When text is part of the requested image, preserve exact quoted wording where the current FLUX host supports text rendering.

When exact brand colors matter and the host/model supports precise color prompting, use the user-provided color specification while still describing the color visually.

Do not invent brand colors from memory or references when exact preservation is required.

## Image Editing

Where the active FLUX model supports image editing/reference input:

- preserve the REALITY REPAIR preserve/change boundary;
- state what must remain unchanged;
- prefer narrow edits;
- use multi-reference roles explicitly;
- do not assume all FLUX family variants expose identical editing behavior.

If the active host lacks verified editing support, return the strongest adapted prompt or use the generic adapter rather than pretending an edit occurred.

## Multiple References

Retain reference roles from the universal workflow.

Example:

```text
image 1: subject identity only
image 2: product geometry/material only
image 3: lighting/color reference only
```

If the host cannot express roles structurally, encode them in text.

## Structured Prompting

Current BFL materials allow structured prompting for complex scenes, but structured JSON is optional.

Use structured form only when:

- the host/model supports it;
- scene complexity benefits from explicit relationships;
- it does not make the prompt less portable or introduce unsupported keys.

Natural language remains the safe default.

## Model-Family Rule

Do not hardcode one FLUX model as universal.

When the user/host exposes a current model:

- use its verified generation/edit capability;
- preserve the shot spec;
- translate unsupported controls semantically;
- disclose material capability gaps when they affect preservation.

## Reality Gate

Before handoff:

- verify user locks survived positive translation;
- ensure avoidances were not lost when negative prompts were removed;
- verify lighting remained motivated;
- verify provider wording did not introduce default shallow DOF, flare, grain, or teal/orange;
- if output can be inspected, run V2 Reality Gate.

## Sources

Current first-party source rechecked on 2026-10-03:

- `black-forest-labs/skills`, `flux-image-best-practices` (public official repository; current master material updated 2026-08-10).

This source is provenance, not a runtime dependency.

## Acceptance

Task 7.5 passes when FLUX receives concise positive natural-language instructions, avoidances survive as positive physical targets, editing behavior remains capability-checked, and provider syntax never becomes the universal cinematic brain.