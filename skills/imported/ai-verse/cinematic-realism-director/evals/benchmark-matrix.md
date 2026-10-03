# Magnific / Higgsfield Comparison Protocol

Status: EVAL PROTOCOL
Task: 9.10

Purpose: define a fair, repeatable benchmark for comparing AI-Verse Cinematic Realism Director outputs against Magnific Cinematic and Higgsfield Soul Cinema / Cinema Studio where equivalent public capabilities are available.

This protocol does **not** claim that AI-Verse outperforms either provider. A superiority claim is forbidden until repeated controlled runs support it.

## Core Principle

Compare matched creative problems, not marketing labels.

```text
same concept
+ same preservation constraints
+ comparable reference inputs
+ comparable aspect/output intent
+ provider-appropriate controls
= fairer comparison
```

The systems are not identical, so exact parameter equality is often impossible. The benchmark therefore compares **observable output quality and control preservation**, while recording provider-specific execution differences.

## Systems Under Test

At minimum, record separate rows for:

1. AI-Verse Cinematic Realism Director + generic/provider adapter + active renderer;
2. Magnific Cinematic;
3. Higgsfield Soul Cinema / Cinema Studio still-image path.

Optional additional rows may include raw renderer baselines without the AI-Verse skill to measure the value of the decision layer itself.

Never combine results from materially different provider/model versions under one label.

## Version / Provenance Receipt

Every benchmark run must record:

```text
date/time
system/provider
model or product surface if exposed
adapter version / skill commit SHA
resolution / aspect ratio
reference count and roles
provider-native controls used
prompt/spec used
number of attempts
whether output was generated, edited, or reference-conditioned
whether visual inspection was possible
```

If a provider hides model details, record `provider-managed / undisclosed` rather than inventing them.

## Benchmark Classes

### A. Beginner Zero-Config

Use one-sentence inputs with no camera jargon.

Required concepts:

1. lonely woman waiting for a taxi in London at night;
2. bright premium skincare commercial on white;
3. documentary baker in a daylight kitchen;
4. family travel moment on a beach;
5. luxury watch product still;
6. sports/action still with a decisive frozen instant;
7. architecture interior requiring spatial readability;
8. food by natural window light;
9. automotive image on a wet night street;
10. harsh-noon exterior.

Goal: test whether the system produces coherent cinematography without the user specifying technical settings.

### B. Expert Control Preservation

Use explicit locked inputs.

Required concepts include:

- exact focal length + rectilinear projection + camera proximity;
- explicit aperture with a non-default depth requirement;
- exact camera/lens reference where supported;
- explicit top-down / OTS / low-angle geometry;
- clean image with explicit `no grain`, `no haze`, `no flare`;
- unusual but coherent combinations such as large-format capture intent plus downstream VHS treatment.

Goal: test whether the system follows the user rather than replacing the request with its preferred preset.

### C. Reality Repair

Use the same source images where provider terms permit.

Defect classes:

- waxy skin;
- malformed hand plus skin artifact;
- fake wet-road reflections;
- floating product/contact failure;
- fabric without weight/contact;
- inconsistent catchlights/shadows;
- overprocessed HDR/highlight halos.

Goal: compare realism improvement **and preservation drift** separately.

### D. Reference Match

Use references with explicit roles:

- composition only;
- lighting/color only;
- identity only;
- product geometry only;
- multi-reference role separation.

Goal: test visual-DNA transfer without incidental content copying or false hardware claims.

## Attempt Count

For visual comparisons, use at least:

```text
5 outputs per concept per system
```

when cost/access permits.

For stochastic systems, a single attractive output is not sufficient evidence.

If provider pricing or limits prevent five outputs, record the reduced sample size and do not present the result as equally strong evidence.

## Prompt / Control Fairness

### AI-Verse

Resolve one universal Cinematic Shot Spec, then use the appropriate adapter.

### Magnific

Use native Cinematic controls only when they express the same intended shot. Do not deliberately cripple Magnific by withholding relevant native controls.

### Higgsfield

Use public/current Soul Cinema / Cinema Studio semantics when available. Do not deliberately avoid provider features that are part of its normal cinematic still workflow.

### No prompt-copy cheating

Do not paste proprietary/hidden prompts from one platform into another. Use observable creative intent and public controls only.

## Scoring Dimensions

Score each generated image independently from 1 to 5 for each dimension.

### 1. Photographic Plausibility

Does the frame plausibly look recordable by a real camera under the stated conditions?

### 2. Cinematic Coherence

Do composition, camera relationship, optics, light, exposure, color and texture feel like one deliberate shot rather than disconnected effects?

### 3. Material Realism

Do fabric, metal, glass, skin, wet surfaces, wood, plastic, product finishes and other relevant materials respond believably?

### 4. Skin / Human Realism

Where humans are present: anatomy, skin variation, hair, eyes, catchlights and focus-scale detail.

### 5. Lighting Motivation

Can visible light plausibly be explained by sources in or around the scene?

### 6. Optical Coherence

Perspective, projection, depth, focus falloff, bokeh/flare only where justified, and absence of contradictory lens behavior.

### 7. Color Restraint / Tone

White balance, source-color relationships, saturation, density, highlights/shadows, skin/product color preservation.

### 8. Composition / Visual Hierarchy

Does the frame clearly communicate the intended subject/action/context and viewer relationship?

### 9. Control Preservation

For expert/edit/reference cases, did the system preserve explicit locks and preservation boundaries?

### 10. Cross-Prompt Consistency

Across unrelated concepts, does the system repeatedly produce coherent results without collapsing into one house cliché?

## Hard-Failure Tags

In addition to 1-5 scores, record binary failure tags:

```text
LOCK_DRIFT
IDENTITY_DRIFT
PRODUCT_GEOMETRY_DRIFT
POSE_OR_T0_DRIFT
FALSE_HARDWARE_CLAIM
FISHEYE_WHEN_RECTILINEAR
UNMOTIVATED_LIGHT
SHADOW_REFLECTION_CONFLICT
FLOATING_CONTACT
PLASTIC_SKIN
MATERIAL_FAILURE
OVERPROCESSED_HDR
UNJUSTIFIED_GRAIN
UNJUSTIFIED_HAZE
UNJUSTIFIED_FLARE
UNJUSTIFIED_TEAL_ORANGE
PROMPT_ONLY_VIOLATION
PROVIDER_CONTROL_HALLUCINATION
```

A beautiful image with a critical hard failure must not be treated as full success.

## Blind Review

Where possible:

1. strip provider names from images;
2. randomize ordering;
3. use at least two independent raters for serious comparison rounds;
4. score before revealing provider identity;
5. resolve major scoring disagreement through a second inspection, not averaging blindly.

Automated vision scoring may supplement review but should not be the sole basis for a public superiority claim.

## Pairwise Review

For matched concepts, also ask:

```text
Which frame better satisfies the stated shot intent?
Which frame is more physically plausible?
Which frame better preserves explicit controls?
```

Pairwise preference is secondary evidence; dimension scores and hard-failure tags remain required.

## Aggregate Reporting

Report per system:

- number of concepts;
- number of outputs;
- median and mean per dimension;
- hard-failure rate;
- expert-lock failure rate;
- repair preservation-drift rate;
- reference-role failure rate;
- zero-config success rate.

Do not collapse everything into a single vanity score unless the component metrics remain visible.

## Superiority Claim Rule

Statements such as:

```text
AI-Verse is better than Magnific
AI-Verse beats Soul Cinema
```

are not permitted from:

- one prompt;
- one cherry-picked image;
- unmatched settings;
- different source/reference images;
- different creative intent;
- unblinded subjective preference alone.

A comparative claim requires repeated matched tests and must state:

- benchmark date;
- product/model versions where known;
- sample size;
- scoring method;
- dimensions where performance differed;
- limitations.

If results are mixed, report them as mixed.

## Benchmark Record Template

For each concept:

```text
BENCHMARK ID:
CONCEPT:
CLASS: beginner | expert | repair | reference
LOCKS / PRESERVE:
ASPECT / OUTPUT:
REFERENCES:

AI-VERSE:
provider/renderer:
adapter:
settings:
outputs:
scores:
hard failures:

MAGNIFIC:
model/surface:
settings:
outputs:
scores:
hard failures:

HIGGSFIELD:
model/surface:
settings:
outputs:
scores:
hard failures:

BLIND REVIEW NOTES:
PAIRWISE NOTES:
LIMITATIONS:
```

## Acceptance

Task 9.10 is complete when a future evaluator can run matched, version-recorded, multi-attempt comparisons without changing the creative target between systems or making unsupported superiority claims.