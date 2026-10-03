# Cinematic Realism Director - Reference Index

Status: RUNTIME LOADING MAP

Purpose: help a capable host load only the local knowledge required for the current task.

All paths below are package-root relative unless explicitly stated otherwise.

Do **not** load every reference file by default.

## 1. Always-Useful Core

Load these when routing, resolving authority, or verifying execution claims:

- `references/routing.md` — activation boundaries and authority order.
- `references/locks.md` — hard locks, preservation locks, AUTO, and conflict precedence.
- `references/host-capabilities.md` — H1-H6 execution/degradation behavior.
- `references/host-action-policy.md` — whether to generate/edit, return a prompt, or abstain from execution.
- `references/success-contract.md` — success/partial/blocked/failed and V0-V3 verification levels.
- `references/reality-gate.md` — final physical-plausibility and anti-AI verification.

Load `references/portability.md` when package/host integration or standalone behavior is relevant.

## 2. Workflow Routing

Choose the smallest workflow matching the user's intent:

- `references/workflows/auto-direct.md` — minimal idea -> complete shot.
- `references/workflows/cinematize.md` — strengthen an existing concept without concept drift.
- `references/workflows/reality-repair.md` — preserve -> diagnose -> targeted repair -> verify.
- `references/workflows/reference-match.md` — transfer observable visual DNA.
- `references/workflows/manual-camera.md` — explicit technical locks + AUTO completion.
- `references/workflows/prompt-only.md` — adapted prompt/spec only, no generation.

Support policies:

- `references/progressive-disclosure-router.md` — ambiguous or overlapping cases.
- `references/question-minimization.md` — ask only when an answer materially changes execution or preservation.
- `references/multi-reference-behavior.md` — roles, priorities, and multiple-reference handling.

## 3. Shot Design

Load according to the missing decision layer.

### Intent / story
- `references/visual-intent.md`

### Composition / blocking / viewpoint
- `references/composition-and-blocking.md`

### Capture format / camera character
- `references/cameras-and-capture-formats.md`

### Lens rendering
- `references/lens-character.md`

### Focal length / distance / perspective
- `references/focal-length-and-perspective.md`

### Aperture / focus / depth
- `references/aperture-focus-and-depth.md`

### Still-frame motion / shutter language
- `references/motion-and-shutter.md`

## 4. Lighting, Exposure, Film Response, Color, Texture

### Motivated source logic
- `references/motivated-lighting.md`
- `references/lighting-roles.md`

### Environment-specific lighting
- `references/environment-lighting-recipes.md`

### Exposure / dynamic range
- `references/exposure-and-dynamic-range.md`

### Film/sensor character
- `references/film-and-sensor-response.md`

### Color / grading
- `references/color-science-and-grading.md`

### Grain / halation / bloom / flare / diffusion restraint
- `references/texture-effects-restraint.md`
- `references/optical-imperfection.md`

## 5. Physical Realism / Reality Repair

Start with:

- `references/anti-ai-artifact-taxonomy.md`
- `references/reality-gate.md`

Then load only the affected domains:

- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`

For structured repair output, also use:

- `schemas/realism-diagnosis.schema.json`

## 6. Reference Match / Uncertainty

Load:

- `references/multi-reference-behavior.md`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `schemas/reference-dna.schema.json`

Hard rule:

```text
observable trait != exact hardware fact
```

Use exact camera/lens/stock metadata only when supplied by the user, embedded metadata, or documented evidence supports it.

## 7. Expert Locks / Manual Camera

Load:

- `references/locks.md`
- `references/parameter-conflicts.md`
- whichever shot-domain references contain the locked/missing fields;
- `schemas/cinematic-shot-spec.schema.json` when structured state is useful.

Authority remains:

```text
current explicit user instruction
> preservation requirement
> active explicit lock
> package physical/logical rules
> AUTO inference
> provider default
```

## 8. Provider Adaptation

Resolve the provider-neutral shot first.

Then load one matching adapter:

- `adapters/generic.md`
- `adapters/openai.md`
- `adapters/gemini.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`

Also load:

- `references/adapter-fallback-hierarchy.md`

when the provider/model is unknown, changed, unavailable, or missing a required capability.

Provider adapters may translate the shot. They may not redesign it.

## 9. Structured Contracts

Use only when JSON/state handoff or machine validation helps:

- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`

Do not expose structured state merely because a schema exists if the user asked only for an image or concise prompt.

## 10. Research Evidence

`references/research/` contains source/provenance evidence used to build the runtime knowledge.

Normally **do not load research files during ordinary execution**.

Use them when:

- auditing a factual camera/lens/stock claim;
- refreshing provider-specific behavior;
- checking source provenance;
- updating the knowledge base.

Important research files include:

- `references/research/magnific.md`
- `references/research/higgsfield.md`
- `references/research/cameras.md`
- `references/research/lenses.md`
- `references/research/lenses-supplement.md`
- `references/research/film-stocks.md`
- `references/research/lighting.md`
- `references/research/color-and-tone.md`
- `references/research/provider-prompting.md`
- `references/research/secondary-public-workflows.md`
- `references/research/research-gap-audit.md`

Source ledgers:

- `references/source-ledger.md`
- `references/source-ledger-addendum.md`

Research evidence is not a second runtime brain.

## 11. Fast Loading Recipes

### Beginner one-line image request

```text
references/workflows/auto-direct.md
references/visual-intent.md
references/composition-and-blocking.md
relevant capture/light references only
references/reality-gate.md
matching provider adapter or adapters/generic.md
```

### Expert locked shot

```text
references/workflows/manual-camera.md
references/locks.md
references/parameter-conflicts.md
relevant technical references
references/reality-gate.md
matching adapter
```

### AI-looking portrait repair

```text
references/workflows/reality-repair.md
references/anti-ai-artifact-taxonomy.md
references/skin-realism.md
references/hair-and-eye-realism.md
references/reflection-shadow-coherence.md when needed
references/reality-gate.md
matching edit-capable adapter
```

### Reference look match

```text
references/workflows/reference-match.md
references/multi-reference-behavior.md
references/confidence-and-uncertainty.md
relevant visual-domain references
schemas/reference-dna.schema.json when structured output helps
references/reality-gate.md
matching adapter
```

### Prompt-only request

```text
references/workflows/prompt-only.md
only the domain references needed to resolve the shot
matching adapter or adapters/generic.md
```

## 12. Loading Invariant

Progressive loading is correct when:

- the host can understand the active task from `SKILL.md`;
- only relevant domain knowledge is opened;
- provider files are loaded after shot design;
- research evidence is not routinely loaded;
- no parent/sibling file is required for core operation.
