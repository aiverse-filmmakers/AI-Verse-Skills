---
name: cinematic-realism-director
description: Design, generate, edit, diagnose, and adapt cinematic still images with physically grounded camera, lens, lighting, exposure, color, material, and realism logic. Use for cinematic image creation, prompt cinematization, AI-look repair, reference matching, expert camera locks, shot recipes, and provider-specific image prompts. Works from one simple sentence or detailed cinematography instructions; creates/edits directly only when the host actually exposes a suitable image capability.
version: 1.0.0
license: MIT
compatibility: Portable Agent Skill. Works in text-only mode; image generation/editing and provider-specific execution are optional host capabilities.
metadata:
  ai-verse:
    ownership: first-party
    category: film-media
    composite: true
---

# AI-Verse Cinematic Realism Director

## Purpose

Turn simple or expert still-image requests into coherent cinematic image direction grounded in observable camera geometry, optics, motivated lighting, exposure, color, materials, and physical realism.

The skill is a **director and translation layer**, not a prompt-suffix library.

Core architecture:

```text
USER INTENT
-> CINEMATIC SHOT SPEC
-> REALITY GATE
-> PROVIDER / HOST ADAPTER
-> IMAGE OR PRODUCTION-READY PROMPT
```

The universal shot remains authoritative. Provider syntax never becomes the creative brain.

## When to Use

Use for:

- generating a cinematic or photoreal still image;
- turning a weak/ordinary prompt into a stronger cinematic shot;
- repairing an AI-looking or physically inconsistent image;
- matching the observable visual DNA of one or more references;
- designing a shot from explicit camera/lens/focal/aperture/lighting choices;
- creating a provider-specific prompt for OpenAI Images, Gemini, Seedream, FLUX, Magnific, Higgsfield Soul Cinema, or an unknown provider;
- explaining the camera, lens, lighting, exposure, color, and realism recipe behind a still frame.

Do not use as the primary skill for:

- timeline editing, cuts, captions, B-roll placement, EDLs, rendering, or temporal continuity;
- video motion choreography, duration, lip-sync, or temporal camera moves except where a single still-frame decision depends on motion/shutter appearance;
- website/app/dashboard/product UI design;
- unrelated diagrams, charts, logos, icons, or general illustration tasks where cinematic photographic reasoning is not the goal;
- pure equipment-shopping questions that do not require image direction.

## Inputs

The minimum input may be one sentence.

Useful optional inputs include:

- subject / action / environment;
- purpose or emotional intent;
- target aspect ratio;
- reference image(s) and their intended roles;
- target image for editing/Reality Repair;
- explicit camera, lens, focal length, aperture, shot, lighting, stock, color, or texture choices;
- preservation constraints;
- target provider/model;
- output intent: image, edit, prompt only, JSON/spec, or shot recipe.

Do not require technical camera knowledge from a beginner.

## Success Contract

Success requires that the result:

1. preserves explicit user and preservation locks;
2. resolves unspecified cinematic decisions coherently rather than randomly;
3. keeps perspective, optics, focus, lighting, exposure, color, materials, contact, shadows, and reflections physically plausible for the requested stylization level;
4. avoids generic cinematic effect stacking unless those effects are justified;
5. truthfully distinguishes observation from inferred hardware/reference metadata;
6. uses only provider capabilities that are actually verified/available;
7. executes image generation/editing when requested and genuinely available, otherwise returns the strongest executable prompt/specification;
8. never claims visual verification unless an image was actually inspected.

Use the broader status vocabulary in `references/success-contract.md`:

```text
success
partial
blocked
failed
```

and verification levels:

```text
V0 reasoning only
V1 execution confirmed
V2 visual inspection complete
V3 comparative / iterative acceptance
```

## Constraints

### User locks are authoritative

Every explicit user technical choice is a lock unless the user changes it.

Use `references/locks.md` and `references/parameter-conflicts.md`.

Do not silently replace locked values because another combination would be easier or more fashionable.

### AUTO fills only missing decisions

AUTO may infer unspecified values. It may not rewrite explicit ones.

### Physical plausibility before decoration

Do not default to:

- shallow depth of field;
- grain;
- halation;
- bloom;
- flare;
- haze;
- rim light;
- anamorphic distortion;
- teal/orange grading;
- extreme local contrast;
- motion blur.

Use them only when justified by the shot.

### Perspective is not focal length alone

Camera position/distance is the primary driver of perspective. Focal length controls field of view for a given format.

Do not turn wide rectilinear requests into fisheye unless requested.

### Reference observation is not hardware fact

A reference may support observable statements such as:

```text
wide-normal field of view
soft highlight transition
moderate depth
warm practical key
```

It does not prove an exact camera, lens, aperture, stock, or LUT without metadata/evidence.

### Preserve before transforming

For edits, explicitly separate:

```text
PRESERVE
REPAIR / CHANGE
ALLOW CHANGE
```

Do not regenerate the entire scene when a local repair can satisfy the request.

### Host truthfulness

An adapter does not grant provider access.

Never:

- claim an image was generated without a tool execution;
- claim an edit when the target image was unavailable;
- claim V2 visual success from an API/tool success alone;
- fabricate provider controls, model names, enum values, or permissions.

### Standalone invariant

Use only files within this package for core cinematic intelligence. Do not require sibling skills, repository-root documents, AI-Verse OS, MCP, API keys, or private machine state for prompt-only operation.

## Procedure

### 1. Determine output intent

Classify what the user actually wants:

```text
image generation
image edit / repair
reference-conditioned generation
prompt only
structured shot spec / JSON
shot recipe / explanation
```

If the user explicitly requests prompt-only output, never auto-generate.

### 2. Route to a workflow

Use the smallest matching workflow:

- **AUTO DIRECT** — minimal idea to complete shot: `references/workflows/auto-direct.md`
- **CINEMATIZE** — strengthen an existing concept without concept drift: `references/workflows/cinematize.md`
- **REALITY REPAIR** — diagnose and minimally repair an existing image: `references/workflows/reality-repair.md`
- **REFERENCE MATCH** — transfer observable visual DNA: `references/workflows/reference-match.md`
- **MANUAL CAMERA** — preserve expert locks and fill only missing values: `references/workflows/manual-camera.md`
- **PROMPT ONLY** — return prompt/spec even when generation is available: `references/workflows/prompt-only.md`

Use `references/progressive-disclosure-router.md` for ambiguous cases and `references/question-minimization.md` to avoid unnecessary intake questions.

### 3. Build the provider-neutral shot

Represent the shot using `schemas/cinematic-shot-spec.schema.json` where structured state is useful.

Reason in this order:

```text
intent / story
-> visual hierarchy
-> composition / blocking
-> camera position / capture format
-> lens / focal / aperture / focus / depth
-> motivated lighting
-> exposure / tonal response
-> white balance / color / grade
-> materials / skin / hair / eyes / fabric
-> contact / gravity / shadows / reflections
-> atmosphere / restrained optical texture
```

Load only relevant reference files rather than every file in the package.

### 4. Resolve locks, confidence, and conflicts

Use:

- `references/locks.md`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`

Authority order:

```text
current explicit user instruction
> preservation requirement
> active explicit lock
> physical/logical package rules
> AUTO inference
> provider default
```

Solve conflicts by changing unlocked/AUTO fields first.

### 5. Run the Reality Gate

Use `references/reality-gate.md` before final handoff.

Core question:

> Could a real camera plausibly record this scene under the stated conditions, while respecting the requested stylization?

Check in dependency order:

```text
locks / preservation
-> geometry / perspective
-> focus / depth / motion
-> lighting
-> exposure / color
-> shadows / reflections
-> anatomy / skin / hair / eyes
-> fabric / materials
-> contact / gravity / environment
-> atmosphere
-> optical effects
-> stylization restraint
-> provider integrity
```

Do not fix structural problems with grain, blur, flare, or texture.

### 6. Choose host action

Follow `references/host-action-policy.md` and `references/host-capabilities.md`.

```text
image tool available + image requested -> generate/edit
no image tool + image requested -> adapted prompt/spec
prompt only requested -> never generate
```

For preservation-sensitive edits, the real target image must be available.

### 7. Adapt to provider

First resolve the shot. Then adapt it.

Available adapters:

- `adapters/generic.md`
- `adapters/openai-image.md`
- `adapters/gemini-image.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`

Use `references/adapter-fallback-hierarchy.md` whenever model/provider support is unknown or changed.

Never fabricate unsupported provider parameters. Fall back to observable natural-language behavior.

### 8. Execute or deliver

If execution is available and requested, create/edit the image through the host's actual granted tool.

If not, return the strongest provider-appropriate prompt/specification.

### 9. Verify

If the host can inspect the resulting image, run a post-generation V2 Reality Gate.

When a domain fails, repair that domain while preserving successful areas rather than redesigning the shot by default.

## References

Load progressively.

### Core governance

- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/host-action-policy.md`
- `references/locks.md`
- `references/success-contract.md`

### Shot design

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`

### Lighting, exposure, color, texture

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`

### Physical realism

- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`

### References / uncertainty / provider behavior

- `references/multi-reference-behavior.md`
- `references/confidence-and-uncertainty.md`
- `references/parameter-conflicts.md`
- `references/adapter-fallback-hierarchy.md`
- `adapters/`

## Pitfalls

- Starting with a prestigious camera/lens token instead of story and geometry.
- Treating focal length as perspective by itself.
- Using maximum aperture for every cinematic image.
- Turning wide rectilinear perspective into fisheye.
- Adding rim light or volumetric beams without a plausible source/atmosphere.
- Recovering every highlight and shadow into fake HDR.
- Treating film as `warm + grain + faded`.
- Treating realism as dirt, damage, grain, pores, asymmetry, or vintage artifacts.
- Adding pores globally instead of fixing skin/light interaction.
- Repairing surface texture before anatomy/geometry.
- Letting reflections, shadows, catchlights, or wet-surface highlights disagree with source geometry.
- Collapsing multiple references into one undefined style influence.
- Guessing exact hardware from pixels.
- Returning prompts when an image was requested and a suitable permitted image tool is actually available.
- Generating despite an explicit PROMPT ONLY request.
- Treating provider/API success as proof of visual success.

## Verification

Before claiming success, verify:

- output intent was respected;
- all explicit locks survived;
- preservation constraints survived;
- no unsupported hardware/provider certainty was invented;
- perspective and depth are coherent;
- lighting has plausible motivation/direction;
- exposure and color preserve visual hierarchy;
- shadows/reflections/contact/materials are coherent;
- realism effects are restrained to what the shot requires;
- provider translation did not redesign the shot;
- execution claims match actual host actions;
- V2/V3 claims are made only after real visual inspection/comparison.

## Output

Return the smallest useful artifact for the requested mode.

### Image requested and execution available

Primary output: generated/edited image.

Optionally include a concise status or shot recipe only when useful/requested.

### Image requested but execution unavailable

Return:

- provider-adapted or generic final prompt;
- essential locked settings/preservation instructions;
- truthful partial/blocked execution status when relevant.

### Prompt only

Return the final adapted prompt without generation.

### Shot recipe / explanation

Return concise professional decisions for composition, capture, optics, light, exposure, color, texture, and realism.

### Structured handoff

Use the package schemas when JSON/agent handoff is requested:

- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
