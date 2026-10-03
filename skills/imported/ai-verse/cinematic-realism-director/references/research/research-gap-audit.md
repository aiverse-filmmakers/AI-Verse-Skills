# Phase 1 Research Gap Audit

Status: PHASE 1 GATE REVIEW

Audit date: 2026-10-03

Purpose: determine whether the research corpus is strong enough to support Phase 2 structured contracts without hiding uncertainty, contaminating the core with provider-specific assumptions, or pretending unresolved evidence is settled.

## Gate Standard

Phase 1 does **not** require perfect knowledge of every lens, film stock, image model, or proprietary provider implementation.

It requires enough evidence that later runtime references can reliably distinguish:

```text
PHYSICAL / TECHNICAL KNOWLEDGE
vs
PROVIDER-SPECIFIC MODEL BEHAVIOR
vs
CORROBORATED PRACTICE
vs
INFERENCE / UNKNOWN
```

That standard is met.

# Evidence Strength Matrix

## Architecture and scope

Strength: **STRONG**

Evidence:

- Phase 0 contracts;
- repository skill specification;
- first-party provider skill structures;
- standalone portability rules.

No blocking gaps.

## Magnific Cinematic control ontology

Strength: **STRONG FOR PUBLIC SURFACE**

Evidence:

- live first-party model schema;
- live first-party `cinematicControls` schema;
- official editor/relight/upscale/reimagine surfaces.

Known unknowns:

- hidden prompt transformation;
- training data;
- model weights;
- internal mapping between a named control and exact generated latent behavior;
- private ranking/selection logic.

Disposition: not blocking. Those internals are deliberately outside scope.

## Higgsfield cinematic philosophy and public behavior

Strength: **STRONG FOR PUBLICLY DOCUMENTED CONCEPTS**

Evidence:

- official engineering write-up;
- official help/product pages;
- official public skill/CLI routing evidence.

Known unknowns:

- private prompt enhancer implementation;
- private training/fine-tuning data;
- exact internal weight given to camera/lens tokens;
- fast-changing Cinema Studio version surfaces.

Disposition: not blocking. Adapters must recheck active versions later.

## Digital cinema camera references

Strength: **STRONG FOR MAJOR V1 FAMILIES**

Strong first-party evidence exists for:

- ARRI ALEXA 35 / REVEAL;
- Sony VENICE 2;
- RED V-RAPTOR / [X];
- Canon C500 Mark II;
- Blackmagic URSA Mini Pro / BRAW color pipeline.

Gap:

- a clean, first-party technical reference that maps `IMAX 70mm` into a precise still-generation behavior without relying on mythology.

Disposition: **OPEN, NON-BLOCKING**.

V1 should treat IMAX/65-70mm as a format/scale/reference concept with conservative observable language until stronger evidence is added.

## Lens families

Strength: **STRONG FOR MOST PRIORITY FAMILIES**

Strong first-party/corroborated evidence now exists for:

- ARRI Signature;
- ARRI/ZEISS Master Prime;
- Leitz SUMMILUX-C;
- Panavision G-Series;
- Cooke Panchro Classic;
- ZEISS Supreme / Supreme Radiance;
- Hawk V-Lite;
- Angenieux Optimo technical behavior.

Moderate:

- Cooke S4 visual descriptions where current evidence is mainly practitioner testimony published by Cooke.

Weak/open:

- Canon K35 detailed optical character beyond Canon's historical package evidence;
- some still-photography lens presets exposed by Magnific, where cinema-specific generative translation is less important and less strongly sourced.

Disposition: **NON-BLOCKING**.

Unknown detailed character must remain unknown rather than filled with community mythology.

## Focal length / perspective / aperture / depth

Strength: **STRONG CONCEPTUALLY**

Core distinction is established:

- perspective depends primarily on camera position/distance;
- focal length controls field of view for a given format;
- aperture/depth should be reasoned with distance, format, focal length and focus strategy rather than used as a blur preset.

Remaining work is schema/runtime implementation, not a Phase 1 evidence gap.

## Film and photochemical response

Strength: **STRONG FOR KODAK MOTION CORE**

Strong first-party evidence exists for:

- VISION3 500T;
- VISION3 250D;
- EASTMAN DOUBLE-X;
- EKTACHROME 100D;
- stable Kodak still-stock family traits where documented.

Gaps:

- not every Magnific film preset has equivalent first-party research depth;
- discontinued Fuji, Agfa, Lomography and CineStill presets vary in source quality and historical/current availability;
- generative models may interpret stock names inconsistently.

Disposition: **NON-BLOCKING**.

V1 runtime should use deeply researched stocks confidently and use conservative descriptive translation for weaker presets. Provider-specific preset names may still be passed literally when the provider exposes them.

## Lighting and exposure fundamentals

Strength: **STRONG**

Covered:

- motivation;
- source size/softness;
- distance/falloff implications;
- negative fill;
- bounce;
- practicals;
- window/sun/sky logic;
- backlight/rim restraint;
- contrast strategy;
- specular/diffuse response;
- atmosphere;
- mixed-light/white-balance reasoning.

Remaining work is synthesis/eval.

## Color and tone

Strength: **STRONG**

Evidence includes:

- ARRI REVEAL;
- ACES 2 rendering/tone/chroma/gamut concepts;
- Blackmagic/Resolve color workflow references;
- colorist corroboration.

Strong principles established:

- highlight rolloff;
- hue preservation;
- gamut/saturation discipline;
- skin/environment separation;
- white-balance source logic;
- density/black-level distinction;
- display-independent descriptive language.

Gap:

- `movie look` preset names exposed by providers are not exact LUT definitions and should not be encoded as copyrighted or supposedly exact movie grades.

Disposition: not blocking. Named movie looks remain provider-specific presets or high-level visual references, not exact recreations.

## Current provider prompting behavior

Strength: **STRONG ENOUGH FOR ADAPTER DESIGN**

Official sources captured for:

- OpenAI GPT Image;
- Google Gemini native image generation;
- ByteDance Seedream;
- Black Forest Labs FLUX;
- Magnific;
- Higgsfield.

Known gap:

Provider names, model IDs, capabilities, limits and prompt behavior change rapidly.

Disposition: **EXPECTED VOLATILITY**.

Phase 7 must revalidate current provider behavior before freezing adapters.

## Secondary skills/workflows

Strength: **SUFFICIENT FOR ARCHITECTURE / TEST IDEAS**

Reviewed:

- fal-ai-community cinematography skill;
- Replicate image prompting skill;
- unofficial OSideMedia Higgsfield cinema skill;
- official Higgsfield/BFL public skills as provider/architecture references.

No secondary source has been promoted to physical truth without independent support.

## Physical realism beyond cinematography

Strength: **PARTIAL**

Current research already touches:

- skin texture;
- materials;
- specularity;
- shadow/contact logic;
- reflections;
- atmosphere;
- preservation-sensitive editing.

However, the dedicated runtime taxonomy for:

- skin;
- hair;
- eyes;
- cloth;
- glass;
- metal;
- plastics;
- liquids;
- roughness;
- contact/weight;
- reflections/refractions;
- common AI artifacts

has not yet been built.

Disposition: **EXPECTED, NON-BLOCKING FOR PHASE 1**.

These are explicitly scheduled for later Physical Realism / Reality Gate phases. Those phases should add targeted technical sources where a rule requires stronger evidence.

# Unknowable / Intentionally Unclaimed Areas

The project must never claim to know:

- Magnific private training data;
- Higgsfield private training data;
- private model weights;
- hidden system prompts;
- proprietary prompt-enhancer text;
- undisclosed ranking/routing systems;
- exact camera/lens/film metadata from pixels alone;
- exact proprietary movie LUTs from a movie-title preset;
- that an AI model physically simulates a real lens just because the prompt names it.

These are not research failures. They are epistemic boundaries.

# Remaining Research Debt Register

## RG-001 - IMAX / 65-70mm technical translation

Priority: MEDIUM

Need: stronger first-party/public technical evidence if the runtime wants more than conservative large-format visual language.

Until resolved: preserve user lock, reason from format/field-of-view/scale principles, avoid invented IMAX physics.

## RG-002 - Canon K35 character

Priority: MEDIUM

Need: stronger primary/corroborated technical evidence for optical character.

Until resolved: preserve literal lock and avoid over-specific universal character claims.

## RG-003 - Non-Kodak preset stock depth

Priority: LOW-MEDIUM

Need: selective research only for stocks that prove useful in actual AUTO/manual workflows.

Do not research every provider preset merely because it exists.

## RG-004 - Material/skin physical-realism taxonomy

Priority: HIGH FOR PHASE 5

Need: targeted sources/evals when implementing Reality Repair and Reality Gate.

## RG-005 - Cross-provider empirical calibration

Priority: HIGH FOR PHASE 9

Need: benchmark how strongly each model responds to camera/lens/stock language and when observable-trait translation outperforms equipment names.

This cannot be solved by desk research alone.

## RG-006 - Provider version drift

Priority: CONTINUOUS

Need: recheck image-provider docs/schema at adapter/release time.

# Phase 1 Gate Decision

## PASS

Reason:

The corpus is sufficiently strong to begin structured ontology/schema work because:

- authoritative source classes are defined;
- public Magnific/Higgsfield concepts are captured without pretending access to private internals;
- major camera/lens/film families have first-party evidence;
- lighting and color foundations are grounded;
- provider prompting behavior is clearly separated from physical cinematography;
- secondary skills are isolated as secondary evidence;
- unresolved areas are explicitly registered rather than guessed;
- no research file breaks Phase 0 scope, portability, lock or host-capability contracts.

Phase 2 may proceed.

# Mandatory Carry-Forward Rules

1. Schema fields must include confidence/provenance semantics.
2. Reference analysis must distinguish observable traits from exact metadata.
3. Provider adapters must be downstream of the universal shot spec.
4. User locks remain higher authority than AUTO/provider defaults.
5. Unknown lens/stock behavior must stay unknown or be expressed conservatively.
6. Model-specific behavior must be revalidated before release.
7. Physical Realism phase must resolve RG-004 enough for the Reality Gate.
8. Benchmark phase must resolve RG-005 empirically rather than by opinion.
