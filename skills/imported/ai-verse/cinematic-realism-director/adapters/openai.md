# OpenAI Image Adapter

Status: RUNTIME ADAPTER
Task: 7.2
Verified against current first-party documentation: 2026-10-03

Purpose: translate the provider-neutral Cinematic Shot Spec into OpenAI image-generation or image-editing instructions without changing the underlying creative decisions.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
OpenAI adapter = provider translation
```

If current OpenAI capabilities differ from this file, fall back to `adapters/generic.md` and preserve the shot spec.

## Current Verified Surface

Current first-party OpenAI image documentation exposes:

- text-to-image generation;
- image editing;
- multi-turn image workflows through the Responses API;
- image inputs during generation/editing;
- configurable size, quality, format, compression, and background where supported;
- current GPT Image 2.5 variants including a precision-oriented `sunburst` variant and a faster general-generation `flare` variant.

Model names and parameter sets are time-sensitive. Never make them part of the universal cinematic brain.

## Provider Selection Rule

When the host exposes an OpenAI image tool:

1. resolve the universal shot first;
2. detect whether the operation is generate or edit;
3. preserve PROMPT ONLY if active;
4. use the host's actually exposed OpenAI image capability;
5. use a current high-precision editing path for preservation-sensitive edits when available;
6. otherwise use the host's normal current generation path;
7. never fabricate an API field merely because current public docs mention it.

If the host abstracts away the model/API details, pass strong natural-language instructions rather than surfacing unsupported API syntax.

## Prompt Style

OpenAI image prompting should favor concrete visible properties:

- subject and action;
- environment and spatial relationships;
- composition and camera position;
- lens/focal/depth appearance;
- motivated lighting;
- materials;
- colors and tone;
- physical realism;
- output/framing requirements.

Structured headings may be used internally or in prompt-only output for complex shots, but no magic syntax is required.

Avoid empty prestige stacks such as:

```text
8K, masterpiece, ultra cinematic, award winning
```

when they do not specify visible image behavior.

## New Generation Serialization

Default order:

```text
SUBJECT / MOMENT
ENVIRONMENT / STORY CONTEXT
COMPOSITION / CAMERA POSITION / PERSPECTIVE
OPTICS / DEPTH / FOCUS
LIGHTING / EXPOSURE
COLOR / GRADE
MATERIAL / SKIN / PHYSICAL REALISM
JUSTIFIED TEXTURE / ATMOSPHERE
OUTPUT / ASPECT CONSTRAINTS
```

The final prompt may be fluent prose rather than visible headings.

## Camera and Lens References

A locked camera or lens name may be included literally, but its observable intent should remain explicit where important.

Example:

```text
ARRI ALEXA 35 character, with controlled highlight transition, natural skin separation, dense but open shadows, and restrained digital sharpness
```

Do not imply OpenAI physically simulates the named camera/lens.

## Editing / Reality Repair

For edits, preserve the semantic separation:

```text
PRESERVE
CHANGE
DESIRED PHYSICAL RESULT
```

OpenAI's current image guidance supports targeted editing, so Reality Repair should use the smallest change set that solves the diagnosed failure.

Example structure:

```text
Preserve the subject identity, pose, wardrobe, framing, background geometry, and lighting direction.
Change only the skin rendering on the face and hands.
Restore natural region-specific skin texture, subtle tonal variation, and source-consistent specular response while keeping makeup and age unchanged.
```

Do not rewrite the entire scene when only one region is defective.

## Multi-Turn Editing

When the host retains image state across turns:

- prefer small targeted iterations over repeated whole-image rewrites;
- restate critical preservation constraints when drift begins;
- run the Reality Gate after each meaningful repair pass when visual inspection is available;
- stop once the target is achieved rather than adding unnecessary refinement passes.

If image state is not actually available in the host, do not pretend the prior image can be edited.

## Multiple References

When multiple image inputs are supported:

- retain explicit role assignments from `references/multi-reference-behavior.md`;
- state those roles in natural language when the host provides no dedicated role field;
- never let a style reference override identity/product geometry locks;
- do not assume provider ordering alone communicates reference priority.

Example:

```text
Reference 1 supplies identity only.
Reference 2 supplies product geometry and materials only.
Reference 3 supplies lighting and color language only.
```

## Negative / Avoidance Guidance

Do not assume a separate negative-prompt channel.

Prefer positive desired-state translation:

```text
natural unretouched skin with visible fine texture
```

instead of relying on:

```text
no plastic skin
```

Explicit avoidances may still appear in ordinary language when necessary, but the requested visible result should be stated positively.

## Output Controls

Use current host-exposed controls only when available, including:

- aspect/dimensions;
- quality;
- output format;
- compression;
- transparency/background.

Do not invent exact fields in prompt-only output unless the user explicitly requests API-ready parameters and those parameters are verified current.

## Host Modes

### OpenAI image-capable host
If the user requests an image/edit, execute through the available image tool after resolving the shot.

### Text/vision-only OpenAI host
Return the adapted prompt/spec.

### PROMPT ONLY
Never execute generation.

## Reality Gate Integration

Before generation: V0 reasoning gate.

After generation/editing, if the host can inspect the result: V2 visual gate.

A successful tool call is not proof that the image passed the gate.

## Current-Model Drift Rule

If the current host exposes a newer/different GPT Image model or different parameters:

1. preserve the Cinematic Shot Spec;
2. use verified current host capabilities if available;
3. otherwise fall back to `adapters/generic.md`;
4. never downgrade or alter user locks merely to match a remembered model interface.

## Sources

Current first-party OpenAI documentation rechecked on 2026-10-03:

- OpenAI Image generation guide;
- OpenAI image generation tool guide;
- OpenAI Images API reference.

These sources are provenance, not runtime dependencies.

## Acceptance

Task 7.2 passes when OpenAI generation/editing can consume the universal shot without provider-core contamination, preserve edit boundaries, use actual host capabilities truthfully, and fall back safely when current model details drift.