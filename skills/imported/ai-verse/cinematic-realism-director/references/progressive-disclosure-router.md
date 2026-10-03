# Progressive Disclosure Router

Status: RUNTIME KNOWLEDGE
Task: 6.7

Purpose: keep the skill fast, readable, and portable by loading only the references needed for the active request instead of treating every knowledge file as mandatory context.

## Core Rule

```text
route first -> load only relevant references -> reason -> adapt -> verify
```

Do not load the entire package for every request.

## Stage 1 - Identify Operation

Route the request to one primary workflow:

```text
AUTO_DIRECT
CINEMATIZE
REALITY_REPAIR
REFERENCE_MATCH
MANUAL_CAMERA
PROMPT_ONLY
SHOT_RECIPE / EXPLAIN
```

When several apply, choose one primary workflow and treat others as modifiers.

Examples:

- `Make this image more cinematic but keep the person identical` -> CINEMATIZE with preservation constraints.
- `Fix the plastic skin in this image` -> REALITY_REPAIR.
- `Match this reference but use a 35mm lens` -> REFERENCE_MATCH + MANUAL_CAMERA lock.
- `Give me a Seedream prompt only` -> PROMPT_ONLY + provider adapter.

## Stage 2 - Always-Available Core Contracts

The host should know or load the minimum contract set needed to remain safe and coherent:

- `references/routing.md`
- `references/locks.md`
- `references/success-contract.md`
- `references/host-capabilities.md`
- `schemas/cinematic-shot-spec.schema.json` when structured output is needed.

Do not repeatedly restate these to the user.

## Stage 3 - Workflow Reference

Load exactly the active workflow file:

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

### Camera / framing
Use as needed:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`

### Lighting / color / finish
Use as needed:

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`

### Realism / repair
Use as needed:

- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`

### Reference analysis
Use:

- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`

### Conflicts
Load `references/parameter-conflicts.md` only when a real contradiction or strong technical tension exists.

## Stage 5 - Provider Adapter

Only after the universal shot or repair plan is resolved:

```text
generic / unknown -> adapters/generic.md
OpenAI -> provider adapter
Gemini -> provider adapter
Seedream -> provider adapter
FLUX -> provider adapter
Magnific -> provider adapter
Higgsfield -> provider adapter
```

A provider adapter may translate the shot. It may not redesign it silently.

## Stage 6 - Reality Gate Depth

Use the lightest verification appropriate to the task:

### V0 prompt/spec
Run reasoning checks on planned geometry, light, exposure, materials, locks, and provider translation.

### V2 inspected/generated image
Run full visual Reality Gate only if an actual image is available for inspection.

Do not simulate visual inspection from a prompt alone.

## Loading Examples

### Beginner: `A woman waiting alone at a rainy bus stop at night`
Load:
- AUTO DIRECT;
- visual intent;
- composition;
- camera/perspective/depth;
- motivated lighting + night environment recipe;
- exposure/color;
- Reality Gate;
- active provider adapter.

Do not load detailed skin, fabric, film-stock, or repair taxonomies unless the shot requires them.

### Repair: `Fix the fake skin and hair but change nothing else`
Load:
- REALITY REPAIR;
- realism-diagnosis schema;
- anti-AI taxonomy;
- skin;
- hair/eyes;
- Reality Gate;
- edit-capable provider adapter.

Do not load full lens research unless the visible problem involves optics.

### Expert: `Alexa 35, Signature Prime 35mm, T2.8, deep focus, hard noon desert`
Load:
- MANUAL CAMERA;
- camera/capture;
- lens character;
- perspective;
- depth;
- hard-noon/desert lighting;
- exposure/color;
- parameter conflicts if needed;
- Reality Gate;
- adapter.

## Anti-Bloat Rule

Do not load research evidence files during normal runtime unless:

- a claim needs provenance verification;
- an adapter is being updated;
- a runtime reference contains an unresolved evidence note.

Runtime references should contain the synthesized behavior.

## Standalone Rule

Every routed path must resolve only to files inside this package folder. Missing optional references must degrade to the universal shot spec and generic adapter rather than requiring a sibling skill or external service.

Acceptance: each major workflow can execute from a small, explicit subset of local files while retaining locks, physical plausibility, and provider-neutral reasoning.