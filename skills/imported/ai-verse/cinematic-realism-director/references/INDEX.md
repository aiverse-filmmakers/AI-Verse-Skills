# Cinematic Realism Director - Reference Index

Status: RUNTIME LOADING MAP

Purpose: help a capable host load only the local knowledge required for the current task.

Do **not** load every reference file by default.

## 1. Always-Useful Core

Load these when routing, resolving authority, or verifying execution claims:

- `routing.md` — activation boundaries and authority order.
- `locks.md` — hard locks, preservation locks, AUTO, and conflict precedence.
- `host-capabilities.md` — H1-H6 execution/degradation behavior.
- `host-action-policy.md` — whether to generate/edit, return a prompt, or abstain from execution.
- `success-contract.md` — success/partial/blocked/failed and V0-V3 verification levels.
- `reality-gate.md` — final physical-plausibility and anti-AI verification.

Load `portability.md` when package/host integration or standalone behavior is relevant.

## 2. Workflow Routing

Choose the smallest workflow matching the user's intent:

- `workflows/auto-direct.md` — minimal idea -> complete shot.
- `workflows/cinematize.md` — strengthen an existing concept without concept drift.
- `workflows/reality-repair.md` — preserve -> diagnose -> targeted repair -> verify.
- `workflows/reference-match.md` — transfer observable visual DNA.
- `workflows/manual-camera.md` — explicit technical locks + AUTO completion.
- `workflows/prompt-only.md` — adapted prompt/spec only, no generation.

Support policies:

- `progressive-disclosure-router.md` — ambiguous or overlapping cases.
- `question-minimization.md` — ask only when an answer materially changes execution or preservation.
- `multi-reference-behavior.md` — roles, priorities, and multiple-reference handling.

## 3. Shot Design

Load according to the missing decision layer.

### Intent / story
- `visual-intent.md`

### Composition / blocking / viewpoint
- `composition-and-blocking.md`

### Capture format / camera character
- `cameras-and-capture-formats.md`

### Lens rendering
- `lens-character.md`

### Focal length / distance / perspective
- `focal-length-and-perspective.md`

### Aperture / focus / depth
- `aperture-focus-and-depth.md`

### Still-frame motion / shutter language
- `motion-and-shutter.md`

## 4. Lighting, Exposure, Film Response, Color, Texture

### Motivated source logic
- `motivated-lighting.md`
- `lighting-roles.md`

### Environment-specific lighting
- `environment-lighting-recipes.md`

### Exposure / dynamic range
- `exposure-and-dynamic-range.md`

### Film/sensor character
- `film-and-sensor-response.md`

### Color / grading
- `color-science-and-grading.md`

### Grain / halation / bloom / flare / diffusion restraint
- `texture-effects-restraint.md`
- `optical-imperfection.md`

## 5. Physical Realism / Reality Repair

Start with:

- `anti-ai-artifact-taxonomy.md`
- `reality-gate.md`

Then load only the affected domains:

- `skin-realism.md`
- `hair-and-eye-realism.md`
- `fabric-and-material-realism.md`
- `contact-gravity-environment.md`
- `reflection-shadow-coherence.md`
- `optical-imperfection.md`

For structured repair output, also use:

- `../schemas/realism-diagnosis.schema.json`

## 6. Reference Match / Uncertainty

Load:

- `multi-reference-behavior.md`
- `confidence-and-uncertainty.md`
- `confidence-serialization.md`
- `parameter-conflicts.md`
- `../schemas/reference-dna.schema.json`

Hard rule:

```text
observable trait != exact hardware fact
```

Use exact camera/lens/stock metadata only when supplied by the user, embedded metadata, or documented evidence supports it.

## 7. Expert Locks / Manual Camera

Load:

- `locks.md`
- `parameter-conflicts.md`
- whichever shot-domain references contain the locked/missing fields;
- `../schemas/cinematic-shot-spec.schema.json` when structured state is useful.

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

- `../adapters/generic.md`
- `../adapters/openai-image.md`
- `../adapters/gemini-image.md`
- `../adapters/seedream.md`
- `../adapters/flux.md`
- `../adapters/magnific.md`
- `../adapters/higgsfield-soul-cinema.md`

Also load:

- `adapter-fallback-hierarchy.md`

when the provider/model is unknown, changed, unavailable, or missing a required capability.

Provider adapters may translate the shot. They may not redesign it.

## 9. Structured Contracts

Use only when JSON/state handoff or machine validation helps:

- `../schemas/cinematic-shot-spec.schema.json`
- `../schemas/realism-diagnosis.schema.json`
- `../schemas/reference-dna.schema.json`

Do not expose structured state merely because a schema exists if the user asked only for an image or concise prompt.

## 10. Research Evidence

`research/` contains source/provenance evidence used to build the runtime knowledge.

Normally **do not load research files during ordinary execution**.

Use them when:

- auditing a factual camera/lens/stock claim;
- refreshing provider-specific behavior;
- checking source provenance;
- updating the knowledge base.

Important research files include:

- `research/magnific.md`
- `research/higgsfield.md`
- `research/cameras.md`
- `research/lenses.md`
- `research/lenses-supplement.md`
- `research/film-stocks.md`
- `research/lighting.md`
- `research/color-and-tone.md`
- `research/provider-prompting.md`
- `research/secondary-public-workflows.md`
- `research/research-gap-audit.md`

Source ledgers:

- `source-ledger.md`
- `source-ledger-addendum.md`

Research evidence is not a second runtime brain.

## 11. Fast Loading Recipes

### Beginner one-line image request

```text
workflows/auto-direct.md
visual-intent.md
composition-and-blocking.md
relevant capture/light references only
reality-gate.md
matching provider adapter or generic.md
```

### Expert locked shot

```text
workflows/manual-camera.md
locks.md
parameter-conflicts.md
relevant technical references
reality-gate.md
matching adapter
```

### AI-looking portrait repair

```text
workflows/reality-repair.md
anti-ai-artifact-taxonomy.md
skin-realism.md
hair-and-eye-realism.md
reflection-shadow-coherence.md when needed
reality-gate.md
matching edit-capable adapter
```

### Reference look match

```text
workflows/reference-match.md
multi-reference-behavior.md
confidence-and-uncertainty.md
relevant visual-domain references
reference-dna.schema.json when structured output helps
reality-gate.md
matching adapter
```

### Prompt-only request

```text
workflows/prompt-only.md
only the domain references needed to resolve the shot
matching adapter or generic.md
```

## 12. Loading Invariant

Progressive loading is correct when:

- the host can understand the active task from `SKILL.md`;
- only relevant domain knowledge is opened;
- provider files are loaded after shot design;
- research evidence is not routinely loaded;
- no parent/sibling file is required for core operation.
