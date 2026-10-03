# Cinematic Realism Director - Confidence and Uncertainty Semantics

Status: FROZEN FOR V1

This contract defines how the skill distinguishes user-supplied truth, direct observation, strong inference, weak inference, AUTO choice, provider translation, and genuinely unknown information.

It exists to prevent two opposite failures:

1. presenting guesses as facts;
2. becoming so cautious that the skill stops making useful cinematic decisions.

The governing principle is:

> Be decisive about creative choices the skill is authorized to make, but explicit about uncertainty in claims that purport to describe existing reality, source metadata, or provider capability.

## 1. Confidence Does Not Mean Lock Strength

Confidence and lock state are separate dimensions.

A user may explicitly request an unusual value that the skill considers creatively unconventional. That value remains a hard lock regardless of confidence about whether it is the most conventional choice.

Example:

```text
User: use a 14mm lens for this close portrait.
```

Represent conceptually as:

```text
path: capture.focal_length
state: user_supplied
locked: true
confidence: certain
value: 14mm
```

The skill does not lower confidence because it dislikes the choice.

Conversely, the skill may be highly confident that a reference frame has wide-angle perspective without being entitled to lock an exact focal length.

```text
observed: strong wide-angle perspective cues
confidence: high
exact focal length: unknown
locked: false
```

## 2. Parameter State Vocabulary

Use the following conceptual states for field-level provenance.

### `user_supplied`

The user explicitly supplied the value in the active task.

Properties:

- highest authority for creative intent;
- normally `locked: true`;
- confidence in provenance is `certain`;
- does not imply the requested combination is physically coherent;
- contradictions are handled by Task 2.5, not by silently reducing authority.

Examples:

```text
25mm
f/1.2
low angle
keep the exact product geometry
```

### `user_preserved`

The user explicitly requires an existing property to remain unchanged or materially consistent.

Examples:

- identity;
- pose;
- camera angle;
- framing;
- product design;
- wardrobe;
- location layout.

This is normally a preservation lock.

### `directly_observed`

The property is visible in a supplied image or otherwise directly available to the host.

Examples:

- subject is backlit;
- frame is portrait orientation;
- strong warm practical is visible camera-left;
- foreground hand is much larger than the head due to near-camera placement.

Observation confidence may still vary because visibility can be obscured, compressed, ambiguous, or cropped.

Direct observation of an effect does not prove its hidden cause.

Example:

```text
Observed: oval out-of-focus highlights.
Not automatically proven: exact anamorphic lens model.
```

### `metadata_confirmed`

The value comes from trusted metadata or another authoritative supplied record.

Examples:

- EXIF focal length when present and trustworthy;
- explicitly supplied camera report;
- known provider response containing actual used settings.

This may support exact hardware values that visual analysis alone cannot justify.

### `strong_inference`

Multiple coherent cues support the conclusion and plausible alternatives are limited.

Examples:

- low camera position inferred from horizon and subject geometry;
- shallow depth behavior inferred from clear focus-plane separation;
- large soft key inferred from broad highlight transition and soft directional shadows.

Strong inference is useful operationally but must remain distinguishable from confirmed fact.

### `weak_inference`

The value is plausible but several alternatives could explain the same visual evidence.

Examples:

- probable focal-length range from a single cropped reference;
- probable stock family from a heavily graded JPEG;
- probable lens family from flare alone.

Weak inference must not be converted into exact technical metadata.

### `auto_selected`

The user did not specify the parameter and the skill deliberately chose it to support intent, story, composition, physical plausibility, or other locks.

AUTO is not uncertainty.

Example:

```text
User gives: woman waiting for a taxi in London at night.
Skill chooses: medium-wide framing, eye-level camera, motivated sodium/LED street practicals.
```

Those are creative decisions, not guesses about an existing image.

AUTO-selected values should be internally coherent and may be changed freely by the skill until execution, unless subsequently locked by the user.

### `auto_open`

The parameter is intentionally left unresolved because deciding it is unnecessary at the current stage or best delegated to a later adapter/provider.

Use sparingly.

Example:

```text
exact camera body: AUTO
observable camera character: natural highlight rolloff, high dynamic range, restrained digital sharpness
```

### `provider_translated`

A provider-neutral intent has been translated into syntax or controls supported by the active image model/provider.

Example:

```text
Core intent: restrained organic shadow grain
Provider translation: specific supported grain control or descriptive prompt wording
```

This state must never imply that the provider literally simulates the named real hardware unless the provider documents that behavior.

### `unknown`

The value cannot currently be known and does not need to be invented.

Examples:

- exact lens model from an untagged reference frame;
- exact T-stop from a flattened JPEG;
- hidden prompt enhancer used by a proprietary provider;
- exact light output in lux from a photograph alone.

Unknown is a legitimate state.

### `not_applicable`

The parameter does not meaningfully apply to the current task.

Example:

- skin rendering for an empty architectural exterior;
- eye realism for a product-only still.

## 3. Confidence Vocabulary

When an explicit confidence label is needed, use:

```text
certain
high
medium
low
unknown
not_applicable
```

### `certain`

Use only when provenance is direct enough that meaningful doubt is absent for the task.

Typical sources:

- explicit user instruction;
- trusted metadata;
- provider-returned actual setting;
- simple direct observation such as image orientation or visible subject count.

Do not use `certain` for visually inferred hidden hardware.

### `high`

Evidence is strong and alternatives are limited.

The conclusion can normally drive AUTO reasoning without a clarification question.

### `medium`

The conclusion is useful but alternatives remain plausible.

The skill may use it to guide a result when exactness is not critical, while avoiding presentation as fact.

### `low`

Evidence is weak or underdetermined.

Low-confidence values should normally:

- remain descriptive rather than exact;
- not become hard locks;
- not be exposed as fact;
- not override stronger evidence.

### `unknown`

Insufficient evidence exists to assign the value.

### `not_applicable`

Confidence is irrelevant because the field itself does not apply.

## 4. Confidence Is About Claims, Not Creativity

The skill should not attach fake statistical confidence to subjective creative choices.

Bad:

```text
85% confidence that 50mm is the best lens for this story.
```

Better:

```text
50mm selected automatically because the shot needs natural facial proportions at the chosen camera distance and moderate environmental context.
```

Creative AUTO choices require rationale and coherence, not pseudo-probabilities.

Confidence is most useful for:

- reference analysis;
- metadata claims;
- diagnosis;
- provider capability claims;
- inferred physical conditions;
- verification results.

## 5. Numeric Scores Are Optional, Not Required

The core runtime should prefer semantic confidence labels rather than arbitrary percentages.

If a later evaluator uses numeric confidence, it must map to the semantic vocabulary consistently and must not imply calibrated probability unless actual calibration exists.

No V1 output should claim a statistically meaningful percentage merely because an LLM can generate one.

## 6. Observation vs Cause

Always separate what is seen from why it may be happening.

Example:

```text
OBSERVATION
background highlights are vertically elongated / oval
confidence: high

POSSIBLE CAUSE
anamorphic optical behavior
confidence: medium

EXACT HARDWARE
unknown
```

Another example:

```text
OBSERVATION
bright source produces broad warm bloom
confidence: high

POSSIBLE CAUSES
halation-like processing, diffusion filter, lens veiling flare, sensor/post bloom
confidence: medium

EXACT FILTER / STOCK
unknown
```

This distinction is mandatory for Reference Match.

## 7. Reference Hardware Rule

Visual analysis alone may produce:

```text
wide-angle
normal
telephoto
spherical-like
anamorphic-like
modern-clean
vintage-lower-contrast
soft focus falloff
controlled flare
```

It must not claim exact hardware such as:

```text
ARRI Alexa 35
Cooke S4 32mm
Kodak 5219
T2.0
```

unless supported by user-supplied information, metadata, production records, or another authoritative source.

Named hardware may be offered as an optional reproduction reference when useful, clearly labeled as a creative match rather than recovered fact.

## 8. AUTO vs Unknown

These states must never be conflated.

### AUTO

Means:

> The skill is allowed to choose this value.

### UNKNOWN

Means:

> The skill lacks evidence to truthfully claim this value about an existing source or system.

Example:

For a new image:

```text
camera_reference = AUTO
```

The skill may choose an ARRI-like high-latitude character.

For a reference image:

```text
exact_camera_used = UNKNOWN
```

The skill must not invent one.

## 9. Confidence Propagation

Derived claims cannot normally be more certain than the evidence they depend on.

Example:

```text
weak inference: likely vintage spherical lens
```

cannot become:

```text
certain: Cooke Panchro 40mm
```

without new evidence.

However, an AUTO creative decision may intentionally choose Cooke Panchro as a reproduction strategy even when the source lens is unknown. That is not confidence escalation because it is a new creative choice, not a claim about the source.

## 10. Multiple Evidence Sources

When several evidence sources agree, confidence may increase.

Priority remains:

1. current explicit user instruction for intent;
2. authoritative metadata/source records for factual claims;
3. direct visual observation;
4. strong inference;
5. weak inference;
6. provider/default assumptions.

Contradictory evidence must not be averaged blindly.

Example:

```text
User says reference was shot on 85mm.
Visual crop feels wider.
```

If the user's statement describes known production metadata, preserve 85mm as supplied truth and consider crop, format, stitching, reframing, or perspective before declaring the user wrong.

## 11. Provider Capability Confidence

Provider capabilities are time-sensitive.

Use:

- `certain/high` when supported by current official schema/docs or an actually available host tool;
- `medium/low` for remembered or secondary descriptions;
- `unknown` when capability cannot be verified.

Never fabricate a parameter because another provider supports something similar.

## 12. Diagnosis Confidence

Reality Repair findings should distinguish:

```text
observed defect
suspected cause
recommended repair
```

Example:

```text
Observed: fingers merge into each other. confidence: high
Cause: generative anatomy failure. confidence: high
Repair: reconstruct hand anatomy while preserving wrist position and gesture.
```

Versus:

```text
Observed: skin has broad waxy highlights. confidence: high
Possible cause: excessive smoothing / synthetic specular response. confidence: medium
Repair: restore pore-scale roughness variation and natural tonal breakup without changing identity.
```

## 13. User-Facing Disclosure

Do not show confidence bookkeeping to beginners unless it materially matters.

Expose uncertainty when:

- the user asks what camera/lens/stock a reference used;
- a low-confidence inference affects the requested match;
- a provider limitation is uncertain;
- a contradiction depends on uncertain evidence;
- structured JSON/shot-recipe output is requested.

Normal AUTO generation should remain fluid and decisive.

## 14. Structured Carrier Requirement

`schemas/cinematic-shot-spec.schema.json` already provides `parameter_states` as the field-level carrier.

A parameter-state record should conceptually support:

```text
path
state
locked
value / normalized_value where represented by the containing spec
confidence
basis / evidence
source_reference when applicable
notes
```

Task 2.4 defines these semantics even if a host chooses a compact serialization.

Reference-specific uncertainty belongs additionally in `reference-dna.schema.json`.

Diagnosis-specific uncertainty belongs additionally in `realism-diagnosis.schema.json`.

## 15. Failure Conditions

Confidence handling fails if the skill:

- invents exact hardware from visual appearance alone;
- uses fake percentages as though calibrated;
- calls AUTO creative decisions uncertain merely because the user did not specify them;
- treats `unknown` as permission to guess;
- lets low-confidence inference override a user lock;
- converts provider-specific marketing into confirmed physical truth;
- hides uncertainty when it materially changes the user's interpretation;
- asks unnecessary questions for ordinary AUTO fields the skill is authorized to choose.

## Task 2.4 Acceptance

Task 2.4 is complete when the structured system can distinguish at minimum:

- directly supplied user values;
- user preservation requirements;
- direct observation;
- metadata-confirmed facts;
- strong inference;
- weak inference;
- AUTO-selected values;
- intentionally open AUTO values;
- provider translations;
- unknown values;
- not-applicable fields;
- confidence independent from lock authority.
