# Adapter Fallback Hierarchy

Status: RUNTIME POLICY
Task: 7.8

Purpose: choose the strongest valid provider translation without fabricating capabilities when a provider, model, host, or version differs from what the package has verified.

## Core Rule

```text
never sacrifice shot truth to preserve adapter specificity
```

A lower-specificity truthful adapter is better than a high-specificity stale or invented one.

## Fallback Order

Use this hierarchy:

```text
1. exact current provider + current model adapter
2. provider-family adapter with verified compatible semantics
3. generic provider adapter
4. provider-neutral shot spec / prompt-only handoff
```

Execution availability is a separate host question handled by `host-action-policy.md`.

## Level 1 - Exact Current Adapter

Use when:

- provider is known;
- model/surface is known;
- required capability has been verified recently enough for the task;
- the live host exposes the expected operation.

Use native controls only when they actually exist.

## Level 2 - Provider-Family Adapter

Use when the provider is known but the exact model/version differs and the remaining semantics are still verified at provider-family level.

Allowed:

- natural-language prompt strategy known to the family;
- current reference behavior known to be shared;
- provider-wide positive-prompt or edit conventions when documented.

Not allowed:

- stale enum values;
- old model names treated as current;
- assumed reference limits;
- assumed negative-prompt support;
- assumed regional-edit controls;
- assumed cinematic selector names.

## Level 3 - Generic Adapter

Use `adapters/generic.md` when:

- provider/model is unknown;
- model is newer than the adapter;
- controls changed;
- the host hides the underlying provider;
- documentation is contradictory or incomplete;
- execution tool accepts only generic natural-language instructions.

The generic adapter preserves:

- shot intent;
- camera geometry;
- optics/depth;
- lighting/exposure;
- color/tone;
- physical realism;
- preservation boundaries;
- reference roles;
- output constraints.

## Level 4 - Shot Spec / Prompt-Only Handoff

Use when no suitable image execution path exists.

Return:

- final adapted or generic prompt;
- essential locked parameters;
- preservation constraints for edits;
- relevant shot recipe when useful;
- truthful blocked/partial status if execution was requested but unavailable.

Never imply generation occurred.

## Capability-Specific Fallback

Fallback may happen per capability rather than per whole provider.

Example:

```text
provider supports generation + references
but not verified regional editing
```

Then:

- use provider adapter for generation/reference syntax;
- translate regional-edit intent into natural-language preservation instructions;
- do not fabricate a mask/coordinate parameter.

## Locked Parameter Rule

A provider limitation does not erase a lock.

If a locked value has no literal provider control:

1. keep the lock in the Cinematic Shot Spec;
2. translate its observable result into prompt language;
3. mark it as semantic translation if structured output is visible;
4. report a hard execution conflict only when the provider genuinely cannot honor the requested outcome.

## Reference Fallback

If a provider cannot accept all references or role types:

1. preserve the reference-role map internally;
2. prioritize references required for identity/product/preservation locks;
3. translate lower-priority style/lighting references into observed visual DNA where possible;
4. disclose meaningful loss of conditioning rather than pretending all references were used.

## Edit Fallback

If a provider cannot perform preservation-sensitive editing:

```text
true edit available -> targeted edit
reference-conditioned regeneration only -> disclose preservation risk
no image conditioning -> return repair handoff prompt/spec
```

Do not call regeneration an exact edit.

## Negative-Prompt Fallback

If negative-prompt support is unverified:

- use positive desired-state language;
- do not invent a `negative_prompt` field.

## Version Drift Rule

Provider facts are time-sensitive.

Before release and whenever a live host contradicts an adapter:

- live verified schema/documentation wins;
- update adapter later through normal package maintenance;
- current task falls back immediately rather than blocking on maintenance.

## Failure Conditions

Incorrect behavior includes:

- using stale exact parameters because an adapter file exists;
- silently swapping a locked lens/camera/stock for a provider preset;
- fabricating a provider feature;
- dropping preservation constraints during fallback;
- treating generic fallback as lower cinematography quality;
- claiming identity/reference conditioning that was not actually supplied.

## Acceptance

Any provider/model change can degrade gracefully from exact adapter to generic prompt/spec while preserving the creative shot, locks, reference roles, and truthfulness of execution claims.