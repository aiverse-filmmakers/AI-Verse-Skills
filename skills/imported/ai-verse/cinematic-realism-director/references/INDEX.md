# Cinematic Realism Director - Reference Index

Status: RUNTIME LOADING MAP

Purpose: help a capable host load only the local knowledge required for the current task while never skipping the Professional Quality Floor or execution-priority rules.

All paths are package-root relative.

Do **not** load every reference by default.

## 1. Core Runtime Policies

For normal image generation/editing, treat these as the core:

- `references/professional-quality-floor.md` — best-professional interpretation of every photographic request.
- `references/execution-priority.md` — explicit provider lock, otherwise native/local first, external fallback only when materially required.
- `references/locks.md` — hard locks, preservation locks, AUTO, conflict precedence.
- `references/host-capabilities.md` — H1-H6 host behavior.
- `references/host-action-policy.md` — execute vs prompt/spec and edit requirements.
- `references/success-contract.md` — success/partial/blocked/failed and V0-V3 verification.
- `references/reality-gate.md` — physical plausibility and anti-AI verification.

Load `references/routing.md` for activation boundaries and `references/portability.md` for package/host integration.

## 2. Workflow Routing

- `references/workflows/auto-direct.md` — minimal idea -> professional complete shot.
- `references/workflows/cinematize.md` — strengthen an existing concept without concept drift.
- `references/workflows/reality-repair.md` — preserve -> diagnose -> targeted repair -> verify.
- `references/workflows/reference-match.md` — transfer observable visual DNA.
- `references/workflows/manual-camera.md` — explicit technical locks + AUTO completion.
- `references/workflows/prompt-only.md` — adapted prompt/spec only, no generation.

Support:

- `references/progressive-disclosure-router.md`
- `references/question-minimization.md`
- `references/multi-reference-behavior.md`

## 3. Shot Design

### Intent / professional specialty
- `references/visual-intent.md`
- `references/professional-quality-floor.md`

### Composition / viewpoint
- `references/composition-and-blocking.md`

### Capture / camera character
- `references/cameras-and-capture-formats.md`

### Lens rendering
- `references/lens-character.md`

### Focal / distance / perspective
- `references/focal-length-and-perspective.md`

### Aperture / focus / depth
- `references/aperture-focus-and-depth.md`

### Still-frame motion
- `references/motion-and-shutter.md`

## 4. Lighting, Exposure, Color, Texture

- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`
- `references/optical-imperfection.md`

The quality floor sets the default professional finish. These domain files refine how that finish is achieved without cliché stacking.

## 5. Physical Realism / Repair

Start with:

- `references/anti-ai-artifact-taxonomy.md`
- `references/reality-gate.md`

Then load affected domains only:

- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`

Structured repair: `schemas/realism-diagnosis.schema.json`.

## 6. Reference Match / Uncertainty

- `references/multi-reference-behavior.md`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `schemas/reference-dna.schema.json`

Hard rule:

```text
observable trait != exact hardware fact
```

## 7. Expert Locks

Load:

- `references/locks.md`
- `references/parameter-conflicts.md`
- relevant technical domain files;
- `schemas/cinematic-shot-spec.schema.json` when structured state helps.

Authority:

```text
current explicit user instruction
> preservation requirement
> active explicit lock
> package physical/logical rules
> Professional Quality Floor for unspecified fields
> AUTO inference
> provider default
```

## 8. Execution and Provider Adaptation

Choose execution **before** loading a provider adapter.

Execution priority:

```text
explicit user provider lock
> native/local host image path
> permitted external path only when native/local lacks a material requirement
> prompt/spec fallback
```

Then load the adapter for the selected path:

- `adapters/generic.md`
- `adapters/openai.md`
- `adapters/gemini.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md` — explicit user request or controlled benchmark only.
- `adapters/higgsfield-soul-cinema.md` — explicit user request or controlled benchmark only.

Use `references/adapter-fallback-hierarchy.md` for translation/version fallback.

Adapter presence must never cause provider selection.

## 9. Structured Contracts

- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`

Do not expose structured state merely because a schema exists.

## 10. Research Evidence

`references/research/` contains provenance used to build runtime knowledge. Normally do not load it during ordinary execution.

Use it for factual audits, provider refreshes, source provenance, or knowledge-base maintenance.

Magnific/Higgsfield research is competitor/provider evidence, not a default execution recommendation.

## 11. Fast Loading Recipes

### Beginner one-line image

```text
professional-quality-floor
execution-priority
auto-direct
visual-intent
composition + relevant technical/light/color/texture references
reality-gate
adapter for chosen native/local path
```

### iPhone / selfie

```text
professional-quality-floor
auto-direct
composition + perspective
lighting/exposure/color
skin/material realism
reality-gate
native/local path
```

### Expert locked shot

```text
professional-quality-floor
manual-camera
locks + parameter-conflicts
relevant technical references
reality-gate
chosen execution adapter
```

### AI-looking portrait repair

```text
professional-quality-floor
execution-priority
reality-repair
anti-ai + skin + hair/eyes (+ reflection/shadow if needed)
reality-gate
native/local edit first
```

### Prompt only

```text
professional-quality-floor
prompt-only
only required domain references
requested provider adapter or generic
```

## 12. Loading Invariant

Progressive loading is correct when:

- the host understands the active task from `SKILL.md`;
- Professional Quality Floor and execution priority are not skipped;
- only relevant domain knowledge is opened;
- provider files are loaded after execution-path selection;
- research evidence is not routinely loaded;
- no parent/sibling file is required for core operation.
