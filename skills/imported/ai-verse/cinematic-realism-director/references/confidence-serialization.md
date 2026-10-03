# Confidence Serialization Mapping

Status: PHASE 2 COMPATIBILITY CONTRACT

This file maps the richer Task 2.4 semantics in `confidence-and-uncertainty.md` onto the compact `parameter_states` carrier already defined inside `schemas/cinematic-shot-spec.schema.json`.

The numeric `confidence` field is an **ordinal serialization value**, not a calibrated probability.

Do not display values such as `0.8` to users as "80% probability" unless a future evaluator has actually calibrated them.

## Canonical Mapping

| Semantic meaning | `state` in shot schema | `confidence` carrier | `locked` |
| --- | --- | ---: | --- |
| explicit user value | `user_supplied` | `1.0` | `true` by default |
| explicit preservation requirement | `preservation_supplied` | `1.0` | `true` |
| direct clear visual observation | `reference_observed` | `1.0` or `0.8` depending ambiguity | `false` unless user locks it |
| trusted supplied metadata | `known_metadata` | `1.0` | depends on task |
| strong inference | `inferred` | `0.8` | `false` |
| medium inference | `inferred` | `0.6` | `false` |
| weak inference | `inferred` | `0.3` | `false` |
| deliberate AUTO selection | `auto` | `1.0` as decision confidence, not factual probability | `false` |
| intentionally open AUTO field | `auto` | `null` | `false` |
| provider translation | `provider_translated` | `1.0` when translation is known/supported, lower when approximate | preserves source lock separately |
| unknown factual metadata | omit exact value or keep it null in the containing field; record unknown in provenance/uncertainty notes | `null` | `false` |
| not applicable | omit parameter-state entry or record in domain-specific schema where supported | `null` | `false` |

## Why AUTO May Use `1.0`

For AUTO creative decisions, confidence is not a claim that the decision is objectively correct.

It means:

> this is the intentional chosen value for the current shot plan.

Example:

```text
state: auto
confidence: 1.0
```

means the director intentionally selected the value, not that there is a 100% factual probability that the choice is uniquely best.

## Why Inference Uses Ordinal Values

The values:

```text
0.8 strong
0.6 medium
0.3 weak
```

are canonical serialization codes for ordering evidence strength inside V1. They are not statistically calibrated probabilities.

A future evaluation system may replace or calibrate them, but it must preserve the semantic distinction.

## Observation Mapping

Use:

```text
reference_observed + 1.0
```

for direct, unambiguous visual facts such as:

- portrait orientation;
- visible subject count;
- clearly backlit subject;
- strong top-down viewpoint.

Use:

```text
reference_observed + 0.8
```

when the feature is visible but interpretation has some ambiguity.

Do not use `reference_observed` for hidden causes such as exact focal length, exact stock, or exact lens model.

## Unknown Is Not Weak Inference

If there is no defensible value, do not encode a guessed value as:

```text
inferred + 0.3
```

merely to fill the field.

Use an unknown/null representation instead.

Weak inference means there is some positive evidence, not merely absence of knowledge.

## Lock Independence

`confidence` never determines `locked`.

Examples:

```text
user_supplied + 1.0 + locked=true
```

and:

```text
reference_observed + 1.0 + locked=false
```

are both valid.

A directly observed property can be certain without being an instruction the target must preserve.

## Provider Translation

When an explicit lock is translated for a provider that lacks the literal control, retain two conceptual records:

```text
source parameter: user_supplied, locked=true
provider expression: provider_translated, locked=false
```

The translation cannot overwrite or erase the source lock.

## Domain-Specific Richer Uncertainty

The compact shot-schema carrier does not replace richer uncertainty structures in:

- `schemas/reference-dna.schema.json`
- `schemas/realism-diagnosis.schema.json`

Those schemas should preserve their more specific evidence, hypotheses, findings and uncertainty fields.

## V1 Invariant

The system must be able to recover these semantic distinctions from serialized state:

```text
supplied
preserved
observed
metadata-confirmed
strongly inferred
weakly inferred
AUTO-selected
AUTO-open
provider-translated
unknown
```

without interpreting ordinal confidence numbers as statistical probabilities.
