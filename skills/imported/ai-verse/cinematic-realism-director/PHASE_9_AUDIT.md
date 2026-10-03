# Phase 9 Audit - Evaluation, Benchmarking, and Regression

Status: COMPLETE
Gate: PASSED

Phase 9 goal:

> Verify repeatable behavior rather than relying on a few attractive or subjective examples.

This audit checks that the skill now has explicit, reusable evaluation contracts for routing, shot design, lock preservation, repair, reference matching, provider translation, anti-cliche behavior, physical plausibility, adversarial boundaries, controlled provider comparison, and permanent regressions.

## Task Evidence

| Task | Evidence | Result |
| --- | --- | --- |
| 9.1 Routing evals | `evals/routing.json` | PASS |
| 9.2 Beginner AUTO evals | `evals/shot-design.json` | PASS |
| 9.3 Expert-lock evals | `evals/expert-locks.json` | PASS |
| 9.4 Reality Repair evals | `evals/realism-repair.json` | PASS |
| 9.5 Reference Match evals | `evals/reference-match.json` | PASS |
| 9.6 Adapter consistency evals | `evals/adapter-behavior.json` | PASS |
| 9.7 Anti-cliche evals | `evals/anti-cliche.json` | PASS |
| 9.8 Physical plausibility evals | `evals/physical-plausibility.json` | PASS |
| 9.9 Adversarial / instruction-boundary evals | `evals/adversarial.json` | PASS |
| 9.10 Magnific / Higgsfield comparison protocol | `evals/benchmark-matrix.md` | PASS |
| 9.11 Regression corpus | `evals/regression.json` | PASS |

## Repeatability Evidence

The evaluation layer is no longer a set of prose examples alone.

It now contains machine-readable or procedural contracts for:

- activation and workflow selection;
- beginner AUTO completion without camera-intake bloat;
- exact expert lock preservation;
- preservation-aware Reality Repair;
- observation vs hardware-inference separation;
- cross-provider shot invariance;
- anti-cliche restraint;
- optics/light/material/contact plausibility;
- prompt-injection and external-content authority boundaries;
- matched provider benchmarking;
- permanent regression coverage.

## Key Gate Checks

### 1. Beginner behavior is testable

`shot-design.json` checks multiple photographic domains rather than one canonical hero prompt.

AUTO is evaluated by properties such as:

```text
coherent story hierarchy
camera geometry before prestige gear
motivated light
appropriate depth
physical realism
no unnecessary questions
no mandatory cinematic effect stack
```

The tests do not require one exact lens/camera choice when several coherent solutions are possible.

Result: PASS.

### 2. Expert locks are testable

`expert-locks.json` verifies that explicit camera/lens/focal/aperture/angle/framing/texture constraints survive AUTO completion and provider translation.

Unusual but coherent combinations are not rejected merely for being unconventional.

Result: PASS.

### 3. Repair is preservation-aware

`realism-repair.json` tests common synthetic failure domains while keeping preservation and dependency order explicit.

A beautiful redesign that changes the wrong identity/product/pose/composition remains a failure.

Result: PASS.

### 4. Reference inference remains honest

`reference-match.json` distinguishes:

```text
observable trait
known metadata
hardware hypothesis
unknown
```

Exact hardware cannot become fact from pixels alone.

Result: PASS.

### 5. Provider adapters remain translations

`adapter-behavior.json` verifies that one resolved Cinematic Shot Spec retains intent and locks across Generic, OpenAI, Gemini, Seedream, FLUX, Magnific, and Higgsfield paths.

Stale/unknown provider details must fall back rather than redesigning the shot.

Result: PASS.

### 6. Cinematic cliches are explicitly regression-tested

`anti-cliche.json` includes clean commercial, documentary, harsh-noon, architecture, food, night, film-stock, luxury, action, rain and beauty cases.

It specifically guards against unjustified defaults including:

```text
shallow DOF
teal-orange
haze
anamorphic flare
extreme grain
dramatic rim light
film stereotype stacking
```

Result: PASS.

### 7. Physical plausibility is explicit

`physical-plausibility.json` tests:

- rectilinear wide perspective;
- camera-position vs focal-length logic;
- aperture/depth conflicts;
- wet automotive reflections;
- contact shadows;
- candle and mixed-source lighting;
- glass response;
- fabric gravity;
- skin/focus behavior;
- subject motion;
- true 90-degree top-down geometry;
- OTS geometry;
- structural-before-surface repair.

Result: PASS.

### 8. External content cannot seize authority

`adversarial.json` tests prompt-injection attempts in:

- reference-image text;
- metadata;
- documents;
- websites;
- cached provider instructions;
- adapter presence;
- tool status messages;
- multi-reference content.

The tests preserve:

```text
current explicit user instruction
> preservation lock
> package/runtime authority
> AUTO/provider suggestion
```

Result: PASS.

### 9. Comparative benchmarking is controlled

`benchmark-matrix.md` requires:

- matched concepts;
- version/provenance receipts;
- comparable reference and output intent;
- at least five outputs per concept/system when access/cost permits;
- blind review where possible;
- per-dimension scores;
- hard-failure tags;
- expert-control preservation;
- zero-config quality;
- limitations and sample size disclosure.

It expressly forbids superiority claims based on one cherry-picked image or unmatched settings.

Result: PASS for protocol completeness.

Important limitation:

> Phase 9 does **not** claim that a live Magnific/Higgsfield benchmark has already proven AI-Verse superior. The protocol exists so such a claim can be tested honestly later. No provider superiority result is asserted by this gate.

### 10. Verified failures are permanent regressions

`regression.json` maps all 22 failures recorded in `references/verified-pitfalls.md` into permanent requirements, including:

- confidence authority drift;
- false perspective logic;
- cinematic effect stacking;
- film stereotypes;
- realism-through-dirt/pores/flyaways;
- structural-vs-surface repair order;
- reflection/shadow conflicts;
- repair drift;
- missing target images;
- beginner question bloat;
- reference-role collapse;
- hardware hallucination;
- frozen-moment drift;
- adapter-core contamination;
- provider-version drift;
- adapter-access confusion;
- V1 vs V2 verification confusion;
- PROMPT ONLY violations;
- standalone dependency regressions.

Result: PASS.

## Gate Result

Phase 9 Gate requirement:

> The skill has evidence of repeatable behavior, not only subjective examples.

Result: **PASSED**.

The skill now has a repeatable evaluation surface with explicit pass/fail properties and a permanent regression ledger. Provider visual-performance claims remain intentionally separate from this gate until real matched benchmark runs are executed.

## Violations Found in Gate Review

```text
routing coverage missing: 0
beginner-domain coverage missing: 0
explicit-lock contract missing: 0
repair-preservation contract missing: 0
reference-certainty boundary missing: 0
adapter-invariance contract missing: 0
anti-cliche coverage missing: 0
physical-plausibility coverage missing: 0
adversarial authority boundary missing: 0
benchmark fairness protocol missing: 0
verified-pitfall regression mapping missing: 0
unsupported superiority claims: 0
```

Phase 9 is closed.