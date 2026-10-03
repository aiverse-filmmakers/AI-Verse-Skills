# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state.

## Current State

- Phase 0: COMPLETE
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE
- Phase 1 gate: PASSED
- Next task: **2.1 - Define `cinematic-shot-spec.schema.json`**

# Phase 0 - Architecture, Scope, and Governance

Status: COMPLETE

## 0.1 Package identity and routing

Status: COMPLETE

Evidence: `references/routing.md`

Frozen identity:

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
```

## 0.2 Standalone portability

Status: COMPLETE

Evidence: `references/portability.md`

Core guarantees:

- no required parent-repo knowledge;
- no sibling-skill dependency;
- no AI-Verse OS requirement for reasoning/prompt-only operation;
- no MCP requirement;
- no API key required for prompt-only use;
- package-local references/adapters/schemas;
- isolated-folder V1 release test required.

## 0.3 Host capability degradation

Status: COMPLETE

Evidence: `references/host-capabilities.md`

H1-H6 host classes cover native generation/editing through text-only operation. Every class has a useful truthful result path.

## 0.4 Explicit locks

Status: COMPLETE

Evidence: `references/locks.md`

User-supplied values and preservation requirements are locks. Unspecified values remain AUTO. Provider defaults cannot silently override locks.

## 0.5 Success/failure contract

Status: COMPLETE

Evidence: `references/success-contract.md`

Top-level states:

```text
success
partial
blocked
failed
```

Verification levels:

```text
V0 reasoning only
V1 execution confirmed
V2 visual inspection completed
V3 comparative/iterative acceptance
```

## Phase 0 Post-Research Re-Audit

Status: PASSED

Evidence: `PHASE_0_AUDIT.md`

After Phase 1 research began landing:

```text
Architecture violations: 0
Standalone violations: 0
Scope violations: 0
Lock violations: 0
Host-capability violations: 0
Success-contract violations: 0
Research-isolation violations: 0
```

# Phase 1 - Research Corpus and Provenance

Status: COMPLETE

## 1.1 Source ledger framework

Status: COMPLETE

Evidence:

- `references/source-ledger.md`
- `references/source-ledger-addendum.md`

Implemented evidence classes:

- CONFIRMED
- CORROBORATED
- MODEL-BEHAVIOR
- PROVIDER-SPECIFIC
- INFERRED

Also implemented source authority, time-sensitivity, copyright, public/private evidence, and provenance rules.

## 1.2 Magnific public evidence

Status: COMPLETE

Evidence: `references/research/magnific.md`

Captured:

- live Cinematic model surface;
- camera/lens/focal/aperture/shot ontology;
- film stocks/movie looks;
- lighting, motion blur, grain, halation and tonal controls;
- structure-preservation and realism-enhancement concepts;
- strict boundary around unknowable private internals.

## 1.3 Higgsfield public evidence

Status: COMPLETE

Evidence: `references/research/higgsfield.md`

Captured:

- Soul Cinema role;
- Cinema Studio engineering philosophy;
- camera/lens vocabulary as model visual priors;
- DP/operator testing;
- lens-character amplification;
- prompt enhancement/AUTO principles;
- Soul ID/color continuity concepts;
- hero-frame workflow;
- version-drift caution.

## 1.4 Camera manufacturer knowledge

Status: COMPLETE

Evidence: `references/research/cameras.md`

First-party evidence captured for ARRI, Sony, RED, Canon and Blackmagic. IMAX/65-70mm deeper technical translation remains registered as research debt rather than guessed.

## 1.5 Lens manufacturer knowledge

Status: COMPLETE

Evidence:

- `references/research/lenses.md`
- `references/research/lenses-supplement.md`

Strong/usable evidence now covers:

- ARRI Signature;
- ARRI/ZEISS Master Prime;
- Leitz SUMMILUX-C;
- Panavision G-Series;
- Cooke Panchro Classic;
- ZEISS Supreme / Radiance;
- Hawk V-Lite;
- Angenieux Optimo.

Canon K35 detailed character remains conservative due to weaker first-party evidence.

## 1.6 Film stock / photochemical knowledge

Status: COMPLETE

Evidence: `references/research/film-stocks.md`

Strong Kodak motion-stock evidence plus negative/reversal, white-balance, grain, halation and tonal-response distinctions captured. Weaker provider stock presets remain explicitly lower-confidence.

## 1.7 Lighting / cinematography fundamentals

Status: COMPLETE

Evidence: `references/research/lighting.md`

Captured motivated lighting, source-size/softness, falloff, negative fill, bounce, practicals, sun/sky/window logic, exposure hierarchy, specular/diffuse response, atmosphere and mixed-source logic.

## 1.8 Color and display-independent visual principles

Status: COMPLETE

Evidence: `references/research/color-and-tone.md`

Captured:

- scene-referred versus display-referred distinction;
- highlight rolloff;
- hue preservation;
- gamut/saturation discipline;
- skin/environment separation;
- white-balance and mixed-light logic;
- density and black-level strategy;
- display-independent visual language;
- color Reality Gate questions.

Primary support includes ARRI REVEAL and official ACES 2 documentation.

## 1.9 Current model-provider prompting guidance

Status: COMPLETE

Evidence: `references/research/provider-prompting.md`

Current official guidance captured for:

- OpenAI GPT Image;
- Google Gemini native image generation;
- ByteDance Seedream;
- Black Forest Labs FLUX;
- Magnific;
- Higgsfield.

The file preserves a model-independent core and assigns syntax/capability differences to adapters.

## 1.10 Secondary public skills/workflows

Status: COMPLETE

Evidence: `references/research/secondary-public-workflows.md`

Reviewed secondary public material for architecture/test hypotheses only. No weaker skill was promoted above first-party cinematography/provider evidence.

Explicitly rejected contamination patterns include:

- prestige-word prompt stacks;
- universal camera suffixes;
- anamorphic caricature;
- automatic maximum shallow DOF;
- mandatory teal/orange;
- negative-prompt dumping across unsupported providers;
- exact hardware hallucination from reference frames.

## 1.11 Research gap audit

Status: COMPLETE

Evidence: `references/research/research-gap-audit.md`

Open research debt is explicitly registered, including:

- RG-001 IMAX / 65-70mm translation;
- RG-002 Canon K35 detailed character;
- RG-003 selected non-Kodak stock depth;
- RG-004 physical-realism/material taxonomy for Phase 5;
- RG-005 cross-provider empirical calibration for Phase 9;
- RG-006 continuous provider-version drift.

None of these requires fabricated answers before Phase 2.

# Phase 1 Gate

Status: PASSED

The corpus is strong enough to begin structured ontology/schema work because later references can now distinguish:

```text
physical / technical knowledge
provider-specific behavior
corroborated practice
model behavior
inference / unknown
```

No Phase 1 evidence breaks the Phase 0 contracts.

# Next

**Task 2.1 - Define `schemas/cinematic-shot-spec.schema.json`**

Phase 2 will turn the research into provider-neutral structured contracts. It must not yet flatten all research into prose prompts or provider-specific controls.

# Change Discipline

Phase 0 remains the governing architecture contract.

Research and later runtime rules may not silently:

- expand the skill into temporal video authority;
- introduce required external runtime dependencies;
- turn one image provider into the core brain;
- override explicit user locks;
- convert marketing language into physical truth;
- turn secondary public skills into authoritative cinematography sources.

Any later change that threatens those invariants triggers another architecture audit.