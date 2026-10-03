# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical task definitions: `IMPLEMENTATION_PLAN.md`

This file is the authoritative completion state and restart point for future chats/agents.

## Current State

- Phase 0: COMPLETE, gate PASSED
- Phase 0 post-research re-audit: PASSED
- Phase 1: COMPLETE, gate PASSED
- Phase 2: COMPLETE, gate PASSED
- Phase 3: COMPLETE, gate PASSED
- Phase 4: COMPLETE, gate PASSED
- Phase 5: COMPLETE, gate PASSED
- Phase 6: COMPLETE, gate PASSED
- Phase 7: COMPLETE, gate PASSED
- Phase 8: COMPLETE, gate PASSED
- Phase 9: COMPLETE, gate PASSED
- Phase 10: NEXT
- V1 task progress: **78 / 93 tasks complete**

Agreed execution rule:

> Complete a minimum of five numbered tasks per batch. If the current phase ends before five tasks are available, finish the phase, run its gate, and continue into the next phase until at least five numbered tasks have been completed.

---

# Completed Phase Evidence

## Phase 0 - Architecture, Scope, Governance
Status: COMPLETE
Gate: PASSED
Post-research audit: PASSED
Evidence:
- `references/routing.md`
- `references/portability.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/success-contract.md`
- `PHASE_0_AUDIT.md`

## Phase 1 - Research Corpus and Provenance
Status: COMPLETE
Gate: PASSED
Evidence:
- `references/source-ledger.md`
- `references/source-ledger-addendum.md`
- `references/research/`
Completed: Tasks 1.1-1.11.

## Phase 2 - Cinematic Shot Ontology and Contracts
Status: COMPLETE
Gate: PASSED
Evidence:
- `schemas/cinematic-shot-spec.schema.json`
- `schemas/realism-diagnosis.schema.json`
- `schemas/reference-dna.schema.json`
- `references/confidence-and-uncertainty.md`
- `references/confidence-serialization.md`
- `references/parameter-conflicts.md`
- `PHASE_2_AUDIT.md`
Completed: Tasks 2.1-2.5.

## Phase 3 - Core Cinematography Knowledge Base
Status: COMPLETE
Gate: PASSED
Evidence:
- `references/visual-intent.md`
- `references/composition-and-blocking.md`
- `references/cameras-and-capture-formats.md`
- `references/lens-character.md`
- `references/focal-length-and-perspective.md`
- `references/aperture-focus-and-depth.md`
- `references/motion-and-shutter.md`
- `PHASE_3_AUDIT.md`
Completed: Tasks 3.1-3.7.

## Phase 4 - Lighting, Exposure, Film Response, Color
Status: COMPLETE
Gate: PASSED
Evidence:
- `references/motivated-lighting.md`
- `references/lighting-roles.md`
- `references/environment-lighting-recipes.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/color-science-and-grading.md`
- `references/texture-effects-restraint.md`
- `PHASE_4_AUDIT.md`
Completed: Tasks 4.1-4.7.

## Phase 5 - Physical Realism and Anti-AI Intelligence
Status: COMPLETE
Gate: PASSED
Evidence:
- `references/anti-ai-artifact-taxonomy.md`
- `references/skin-realism.md`
- `references/hair-and-eye-realism.md`
- `references/fabric-and-material-realism.md`
- `references/contact-gravity-environment.md`
- `references/reflection-shadow-coherence.md`
- `references/optical-imperfection.md`
- `references/reality-gate.md`
- `PHASE_5_AUDIT.md`
Completed: Tasks 5.1-5.8.

## Phase 6 - Decision Engine and Workflows
Status: COMPLETE
Gate: PASSED
Evidence:
- `references/workflows/auto-direct.md`
- `references/workflows/cinematize.md`
- `references/workflows/reality-repair.md`
- `references/workflows/reference-match.md`
- `references/workflows/manual-camera.md`
- `references/workflows/prompt-only.md`
- `references/progressive-disclosure-router.md`
- `references/question-minimization.md`
- `references/multi-reference-behavior.md`
- `PHASE_6_AUDIT.md`
Completed: Tasks 6.1-6.9.

## Phase 7 - Provider and Host Adapters
Status: COMPLETE
Gate: PASSED
Evidence:
- `adapters/generic.md`
- `adapters/openai.md`
- `adapters/gemini.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`
- `references/adapter-fallback-hierarchy.md`
- `references/host-action-policy.md`
- `PHASE_7_AUDIT.md`
Completed: Tasks 7.1-7.9.

## Phase 8 - Portable Skill, Manifest, and UX
Status: COMPLETE
Gate: PASSED
Evidence:
- `SKILL.md`
- `aiverse.skill.yaml`
- `README.md`
- `references/INDEX.md`
- `references/verified-pitfalls.md`
- `examples/`
- `PHASE_8_AUDIT.md`
Completed: Tasks 8.1-8.6.

## Phase 9 - Evaluation, Benchmarking, and Regression
Status: COMPLETE
Gate: PASSED
Evidence:
- `evals/routing.json`
- `evals/shot-design.json`
- `evals/expert-locks.json`
- `evals/realism-repair.json`
- `evals/reference-match.json`
- `evals/adapter-behavior.json`
- `evals/anti-cliche.json`
- `evals/physical-plausibility.json`
- `evals/adversarial.json`
- `evals/benchmark-matrix.md`
- `evals/regression.json`
- `PHASE_9_AUDIT.md`

Completed: Tasks 9.1-9.11.

Phase 9 gate result:

> The skill now has explicit repeatable behavior contracts rather than only subjective examples.

Key evaluation coverage:

```text
routing
beginner AUTO
expert locks
Reality Repair
Reference Match
cross-provider consistency
anti-cliche restraint
physical plausibility
adversarial authority boundaries
matched Magnific/Higgsfield benchmark protocol
permanent regression corpus
```

The regression corpus maps all **22 verified implementation failure patterns** into permanent tests.

Benchmark limitation remains explicit:

> No claim is made that AI-Verse already outperforms Magnific or Higgsfield. `evals/benchmark-matrix.md` defines the controlled repeated benchmark required before any such claim can be supported.

---

# Core Invariants

```text
story before prestige tokens
explicit user value = lock
AUTO fills only missing choices
perspective != focal length alone
cinematic != shallow DOF / grain / flare / teal-orange
reference observation != exact hardware fact
preserve before transforming
Reality Gate before visual-success claims
provider adapter != cinematic brain
adapter file != provider access
PROMPT ONLY override is absolute
successful tool call != visual quality verified
standalone package operation remains mandatory
```

---

# Next Batch - Phase 10

Complete the next five numbered tasks:

```text
10.1 Determine canonical registry placement
10.2 Update required registry metadata
10.3 Add contract tests
10.4 Add standalone package test
10.5 Test runtime adapter exposure
```

Then continue with 10.6-10.8 and the Phase 10 gate in the following batch, extending into Phase 11 as needed to satisfy the five-task minimum.

Next task: **10.1 - Determine canonical registry placement**

---

# Change Discipline

Phase 0 remains the governing architecture contract.

Later phases may not silently:
- expand into temporal video authority;
- introduce required external runtime dependencies;
- turn a provider into the core cinematic brain;
- override explicit user or preservation locks;
- treat inferred reference hardware as known fact;
- convert marketing language into physical truth;
- use cinematic artifacts as mandatory realism tokens;
- beautify/redesign preserved identity during repair;
- claim image generation/editing/visual verification when the host did not actually perform it;
- allow provider syntax or controls to redesign the universal shot.
