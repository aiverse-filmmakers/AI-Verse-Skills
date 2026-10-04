# Progressive Disclosure Router

Status: RUNTIME KNOWLEDGE

Purpose: keep the skill fast and portable by loading only the local references needed for the active request while guaranteeing the Professional Quality Floor and native-first execution policy are never skipped.

## Core Rule

```text
route
-> load quality floor + locks + execution priority
-> load active workflow
-> load only relevant visual domains
-> resolve universal shot
-> choose execution path
-> adapt for that chosen path
-> verify
```

Do not load the entire package for every request.

## Stage 1 - Identify Operation

Choose one primary workflow:

```text
AUTO_DIRECT
CINEMATIZE
REALITY_REPAIR
REFERENCE_MATCH
MANUAL_CAMERA
PROMPT_ONLY
SHOT_RECIPE / EXPLAIN
```

Modifiers may coexist with one primary workflow.

## Stage 2 - Always-Available Core

For ordinary generation/editing requests, the minimum core should include:

- `references/professional-quality-floor.md`
- `references/execution-priority.md`
- `references/locks.md`
- `references/host-capabilities.md`
- `references/host-action-policy.md`
- `references/success-contract.md`

Use `references/routing.md` when activation boundaries are relevant and `schemas/cinematic-shot-spec.schema.json` when structured state helps.

The quality floor is not optional just because a prompt is simple.

## Stage 3 - Workflow Reference

Load exactly the active workflow:

```text
AUTO DIRECT      -> references/workflows/auto-direct.md
CINEMATIZE       -> references/workflows/cinematize.md
REALITY REPAIR   -> references/workflows/reality-repair.md
REFERENCE MATCH  -> references/workflows/reference-match.md
MANUAL CAMERA    -> references/workflows/manual-camera.md
PROMPT ONLY      -> references/workflows/prompt-only.md
```

## Stage 4 - Domain References

Load only the systems materially involved.

### Intent / camera / framing

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`

### Lighting / color / finish

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`

### Realism / repair

- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`

### Reference analysis

- `references/multi-reference-behavior.md`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `schemas/reference-dna.schema.json`

Load `references/parameter-conflicts.md` only for a real contradiction/technical tension.

## Stage 5 - Resolve Professional Shot Before Provider

The universal shot must already contain:

- the requested/implicit image medium;
- professional specialty standard;
- visual hierarchy;
- composition/camera relationship;
- optics/depth;
- motivated light;
- exposure/tonal response;
- color/grade;
- default subtle organic texture when appropriate;
- physical realism;
- user locks.

A provider adapter is not allowed to supply the missing professional vision.

## Stage 6 - Choose Execution Path

Follow `references/execution-priority.md`:

```text
explicit provider lock
> native/local host image capability
> permitted external provider only for missing material capability
> prompt/spec fallback
```

Magnific/Higgsfield are explicit-target/benchmark only, never automatic choices.

## Stage 7 - Provider Adapter

Only now load the adapter for the path already selected.

```text
unknown/native hidden provider -> adapters/generic.md
OpenAI -> adapters/openai.md
Gemini -> adapters/gemini.md
Seedream -> adapters/seedream.md
FLUX -> adapters/flux.md
Magnific -> adapters/magnific.md ONLY when explicitly requested/benchmarking
Higgsfield -> adapters/higgsfield-soul-cinema.md ONLY when explicitly requested/benchmarking
```

Provider adapters translate. They do not choose providers or redesign the shot.

## Stage 8 - Reality Gate

### V0 prompt/spec
Check planned geometry, light, exposure, materials, professional finish, locks, and translation.

### V2 inspected/generated image
Inspect the actual pixels where possible. If material failures exist, repair them while preserving successful domains.

## Loading Examples

### Beginner: `A woman waiting alone at a rainy bus stop at night`

Load:

- Professional Quality Floor;
- Execution Priority;
- AUTO DIRECT;
- visual intent;
- composition/camera/depth;
- night lighting + exposure/color;
- texture restraint;
- Reality Gate;
- adapter for the already-chosen execution path.

### Mobile: `iPhone mirror selfie in a hotel room`

Load:

- Professional Quality Floor;
- AUTO DIRECT;
- composition/perspective;
- lighting/exposure/color;
- skin/material realism;
- Reality Gate;
- native/local adapter path.

Do not load a cinema-camera provider merely because the skill is named Cinematic Realism Director.

### Repair: `Fix the fake skin and hair but change nothing else`

Load:

- Professional Quality Floor;
- Execution Priority;
- REALITY REPAIR;
- diagnosis + skin/hair references;
- Reality Gate;
- native edit path first.

### Expert: `Alexa 35, Signature Prime 35mm, T2.8, deep focus, hard noon desert`

Load MANUAL CAMERA, locks, relevant technical/light references, quality floor, Reality Gate, then the chosen execution adapter.

## Anti-Bloat Rule

Do not load research evidence during ordinary runtime unless provenance/adapters require verification.

## Standalone Rule

Every routed path must resolve only to files inside this package. Missing optional references or external tools degrade to the universal shot and generic adapter rather than requiring a sibling skill or external service.
