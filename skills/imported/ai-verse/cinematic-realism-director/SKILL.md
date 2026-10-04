---
name: cinematic-realism-director
description: Direct, generate, edit, diagnose, and adapt professional cinematic or photographic still images from minimal or expert input. Automatically applies the best professional execution appropriate to the requested medium, preserves explicit camera/style locks, uses the host-native/local image model before optional external providers, and keeps Magnific/Higgsfield as explicit-target or benchmark adapters rather than default backends.
version: 1.1.0
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

Turn any still-image request—from a one-line beginner idea to a fully specified cinematography brief—into the strongest professional image appropriate to that exact medium, subject, and context.

The user should not need to type `professional`, `cinematic`, `Hollywood`, `ARRI`, `good lighting`, `good composition`, `realistic`, or `high quality` to unlock expert direction.

Core architecture:

```text
USER INTENT
-> REQUESTED / IMPLIED IMAGE MEDIUM
-> PROFESSIONAL QUALITY FLOOR
-> CINEMATIC SHOT SPEC
-> REALITY GATE
-> EXECUTION PRIORITY
-> PROVIDER ADAPTER FOR THE ALREADY-CHOSEN PATH
-> IMAGE OR PRODUCTION-READY PROMPT
```

The skill is a visual director and cinematography/photography intelligence layer, not a prompt-suffix library and not a router to premium third-party generators.

## When to Use

Use for:

- generating a cinematic or professional photographic still;
- turning a simple/ordinary prompt into a top-tier professional image;
- mobile/iPhone/selfie photography that should look expertly shot and edited while remaining recognizably mobile;
- candid, documentary, street, editorial, narrative, portrait, product, fashion, automotive, food, architecture, travel, hospitality, and commercial imagery;
- repairing an AI-looking or physically inconsistent image;
- matching observable visual DNA from references;
- respecting explicit camera/lens/focal/aperture/lighting/stock/color/texture locks;
- creating a provider-specific prompt when the user explicitly requests one;
- explaining a professional shot recipe.

Do not use as the primary skill for:

- timeline editing, cuts, captions, B-roll placement, EDLs, rendering, or temporal continuity;
- video motion choreography, duration, or lip-sync except where a still-frame choice depends on motion/shutter appearance;
- website/app/dashboard/product UI design;
- unrelated charts/diagrams/logos/icons;
- pure equipment-shopping questions with no image-direction task.

## Inputs

The minimum input may be one sentence.

Useful optional inputs:

- subject / action / environment;
- requested medium (`iPhone selfie`, `candid photo`, `movie still`, `product ad`, etc.);
- purpose/emotional intent;
- aspect ratio;
- references and their roles;
- target image for editing;
- explicit camera, lens, focal, aperture, shot, light, stock, color, or texture choices;
- preservation constraints;
- explicit provider/model request;
- output intent: image, edit, prompt-only, JSON/spec, or shot recipe.

Do not require technical camera knowledge from a beginner.

## Success Contract

Success requires that the result:

1. preserves literal subject/action/environment and explicit user/preservation locks;
2. applies the **Professional Quality Floor** to every unspecified decision;
3. chooses the professional specialty appropriate to the requested medium rather than applying one generic cinema preset;
4. resolves composition, camera relationship, optics/depth, motivated lighting, exposure, color, texture, materials, contact, shadows, and reflections coherently;
5. reaches a world-class professional standard without needing the user to add quality/cinema keywords;
6. uses subtle organic filmic texture by default for most photographic/cinematic work unless the medium/user calls for pristine cleanliness;
7. avoids cinematic cliché stacking such as automatic blue anamorphic streaks, teal/orange, haze, rim light, maximum blur, Dutch angle, or heavy halation;
8. uses the host-native/local image capability before optional external MCP/plugin/provider execution unless the user explicitly locks a provider or native lacks a material required capability;
9. never automatically selects Magnific Cinematic or Higgsfield Soul Cinema for ordinary requests;
10. truthfully distinguishes observation from inferred hardware/reference metadata;
11. executes image generation/editing when requested and genuinely available, otherwise returns the strongest production-ready prompt/spec;
12. never claims visual verification unless an actual image was inspected.

Use `references/success-contract.md` for `success`, `partial`, `blocked`, `failed` and V0-V3 verification semantics.

## Constraints

### Professional Quality Floor is mandatory

Load and apply `references/professional-quality-floor.md` for ordinary generation/editing work.

A basic prompt must not receive merely competent, generic, or under-directed photography when a stronger professional interpretation is safely inferable.

Professionalization is medium-aware:

```text
iPhone/selfie -> elite mobile photographer/editor
candid/documentary -> elite candid/editorial/documentary photographer
narrative/movie-like -> feature-film cinematographer
portrait/beauty -> top portrait/beauty photographer
fashion -> top editorial/fashion photographer
product -> world-class commercial product photographer
automotive -> specialist automotive campaign photographer
food -> specialist food photographer
architecture -> elite architectural photographer
travel/hospitality -> top travel/hospitality photographer/cinematographer
```

Do not convert an explicit phone/selfie request into generic cinema-camera imagery. Execute the requested medium expertly.

### User locks are authoritative

Every explicit user technical/aesthetic/provider choice is a lock unless the user changes it.

Use:

- `references/locks.md`
- `references/parameter-conflicts.md`

AUTO fills only unspecified fields.

### Native/local execution is the default

Follow `references/execution-priority.md`.

```text
1. explicit user-locked provider, if actually available/permitted
2. host-native/local image generation/editing
3. permitted external MCP/plugin/connector only when native/local lacks a material requirement
4. prompt/spec fallback
```

Never prefer an external provider merely because it looks more cinematic, premium, specialized, or exposes more controls.

MCP is transport, not creative authority.

### Magnific/Higgsfield are not automatic backends

`adapters/magnific.md` and `adapters/higgsfield-soul-cinema.md` are explicit-target/benchmark adapters only.

Use them only when:

- the user explicitly requests that provider/export; or
- a controlled benchmark explicitly names it.

Do not route ordinary image requests to either provider.

### Default professional cinema DNA

For narrative/cinematic work—or a general photographic scene without a stronger medium signal—AUTO should normally target observable qualities such as:

```text
feature-film visual hierarchy
premium digital-cinema tonal response
ARRI-like highlight rolloff / gentle highlight-to-mid transition
rich but readable shadows
motivated source falloff
professional color separation
natural skin/material rendering
realistic optical/focus falloff
subtle organic filmic texture
high-end restrained grade
```

`ARRI-like` is an observable tonal target, not a claim of literal ARRI capture/simulation.

### Texture default

For most photographic/cinematic outputs, subtle organic filmic texture is a normal finishing layer.

Strong/coarse grain, halation, bloom, flare, dirt, scratches, or obvious vintage artifacts still require a specific reason.

Reduce/remove base texture when:

- user says no grain/pristine/clinical/noise-free;
- the medium clearly requires sterile technical cleanliness;
- a product/beauty macro requires texture-free clarity.

See `references/texture-effects-restraint.md`.

### Professional quality is not cliché stacking

Do not automatically add:

- anamorphic blue streaks;
- teal/orange grading;
- haze/fog;
- dramatic rim light;
- f/1.2 / maximum bokeh;
- Dutch angle;
- heavy bloom;
- obvious halation;
- strong vignette;
- arbitrary motion blur;
- crushed blacks;
- prestige camera/lens tokens with no observable purpose.

Restraint must not be used as an excuse for ordinary/sterile output.

### Perspective is not focal length alone

Camera position/distance primarily drives perspective. Focal length controls field of view for a given format.

Do not turn wide rectilinear requests into fisheye unless requested.

### Reference observation is not hardware fact

Visible traits may support statements such as:

```text
wide-normal field of view
soft highlight transition
moderate depth
warm practical key
```

They do not prove an exact camera/lens/aperture/stock/LUT without evidence.

### Preserve before transforming

For edits, separate:

```text
PRESERVE
REPAIR / CHANGE
ALLOW CHANGE
```

Do not regenerate the entire scene when a local repair can satisfy the request.

### Host truthfulness

Never:

- claim an image was generated without tool execution;
- claim an edit when the target image was unavailable;
- claim V2 visual success from API/tool success alone;
- fabricate provider controls/model names/permissions;
- treat adapter presence as provider access.

### Standalone invariant

Core cinematic intelligence must use only files within this package. Do not require sibling skills, repository-root docs, AI-Verse OS, MCP, API keys, or private machine state for prompt/spec operation.

## Procedure

### 1. Determine output intent

Classify:

```text
image generation
image edit / repair
reference-conditioned generation
prompt only
structured shot spec / JSON
shot recipe / explanation
```

PROMPT ONLY is absolute.

### 2. Identify medium and professional specialty

From the user's wording, infer whether this is mobile/selfie, candid/documentary, narrative/cinematic, portrait, fashion, product, automotive, food, architecture, travel/hospitality, or another specialty.

Do not ask if a reasonable professional choice is inferable.

### 3. Apply the Professional Quality Floor

Load `references/professional-quality-floor.md`.

Resolve the best professional execution appropriate to that medium before provider selection.

### 4. Route to a workflow

- **AUTO DIRECT** — minimal idea to complete professional shot.
- **CINEMATIZE** — strengthen an existing concept without concept drift.
- **REALITY REPAIR** — diagnose and minimally repair an existing image.
- **REFERENCE MATCH** — transfer observable visual DNA.
- **MANUAL CAMERA** — preserve expert locks and fill only missing values.
- **PROMPT ONLY** — return prompt/spec and never generate.

Use `references/progressive-disclosure-router.md` and `references/question-minimization.md`.

### 5. Build the provider-neutral shot

Reason in this order:

```text
intent / requested medium
-> professional specialty / quality floor
-> visual hierarchy
-> composition / blocking
-> camera position / capture character
-> lens / focal / aperture / focus / depth
-> motivated lighting
-> exposure / highlight rolloff / shadow density
-> white balance / color separation / grade
-> skin / hair / fabric / materials
-> contact / gravity / shadows / reflections
-> subtle base texture + any justified optical effects
```

Use `schemas/cinematic-shot-spec.schema.json` when structured state helps.

### 6. Resolve locks/conflicts

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

Change unlocked/AUTO fields first.

### 7. Run Reality Gate V0

Use `references/reality-gate.md`.

Core question:

> Could an elite professional plausibly create this requested image under the stated medium/conditions, with physically coherent capture and finishing?

Check geometry, perspective, depth, lighting, exposure, color, shadows/reflections, anatomy/skin/hair, materials, contact/gravity, texture/effects, medium fidelity, locks, and professional finish.

### 8. Choose execution path before provider adapter

Follow `references/execution-priority.md` and `references/host-action-policy.md`.

```text
explicit provider lock
> native/local host image tool
> external fallback only for missing material capability
> prompt/spec
```

Do not scan adapters to decide which provider looks best.

### 9. Adapt only to the chosen path

Default/generic/native-hidden provider:

- `adapters/generic.md`

Known normal providers when actually selected by the host:

- `adapters/openai.md`
- `adapters/gemini.md`
- `adapters/seedream.md`
- `adapters/flux.md`

Explicit-target/benchmark only:

- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`

Use `references/adapter-fallback-hierarchy.md` for translation/version fallback.

### 10. Execute or deliver

If image execution is requested and available, execute through the chosen path.

Otherwise return the strongest provider-neutral/adapted prompt/spec.

### 11. Verify actual output

If the host can inspect the generated/edited image, run V2 Reality Gate.

Repair material failures while preserving successful regions/locks. If native/local execution produced an imperfect first result, try focused native/local correction before escaping to an external provider.

## References

Load progressively from `references/INDEX.md`.

Core:

- `references/professional-quality-floor.md`
- `references/execution-priority.md`
- `references/locks.md`
- `references/host-capabilities.md`
- `references/host-action-policy.md`
- `references/success-contract.md`
- `references/reality-gate.md`

Workflows:

- `references/workflows/auto-direct.md`
- `references/workflows/cinematize.md`
- `references/workflows/reality-repair.md`
- `references/workflows/reference-match.md`
- `references/workflows/manual-camera.md`
- `references/workflows/prompt-only.md`

Technical domains:

- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motivated-lighting.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`
- physical-realism references listed in `references/INDEX.md`.

## Pitfalls

- Returning ordinary literal photography because the user did not say `professional` or `cinematic`.
- Forcing cinema-camera aesthetics onto an explicit phone/selfie/mobile request.
- Treating anti-cliché restraint as `no professional finish`.
- Using strong grain/effects instead of physical realism.
- Treating focal length as perspective by itself.
- Treating wide as fisheye.
- Treating shallow depth as automatically cinematic.
- Automatically routing to an MCP/external provider before native/local generation.
- Automatically selecting Magnific/Higgsfield because they are cinema-oriented.
- Treating adapters as provider recommendations/access.
- Letting provider controls redesign the universal shot.
- Claiming exact hardware from a visual reference without evidence.
- Broad regeneration when a local preservation-safe edit is enough.
- Claiming visual success after tool execution without inspection.

## Verification

### V0 - reasoning/spec

Verify:

- requested medium recognized;
- professional specialty chosen correctly;
- quality floor applied;
- user locks preserved;
- shot physically coherent;
- subtle texture/finish appropriate;
- clichés absent unless justified;
- execution path obeys native-first policy;
- Magnific/Higgsfield not selected automatically;
- provider translation does not alter creative truth.

### V1 - execution confirmed

Tool/provider completed and returned an output. Do not infer visual success.

### V2 - visual inspection

Inspect actual output for:

- professional-quality floor;
- medium fidelity;
- composition/camera relationship;
- light/exposure/color;
- skin/material/contact/reflection realism;
- focus/depth;
- texture quality;
- AI artifacts;
- locks/preservation.

### V3 - iterative acceptance

Correct material failures and re-run V2 until the result satisfies task-specific acceptance or a real limitation remains.

## Output

### Image-capable host

Return the generated/edited image directly. Keep internal technical machinery hidden unless useful/requested.

### Image unavailable

Return a production-ready professional prompt/spec that already contains the quality floor; do not ask the user to add cinema/quality keywords later.

### Prompt-only

Return only the requested prompt/spec/JSON/settings. Execute no provider.

### Shot recipe / explain

Explain locked vs AUTO decisions, medium/professional specialty, composition, capture, lighting, exposure, color, texture, realism, and provider translation when relevant.
