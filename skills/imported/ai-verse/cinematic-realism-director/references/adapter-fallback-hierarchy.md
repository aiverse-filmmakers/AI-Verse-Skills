# Adapter Fallback Hierarchy

Status: RUNTIME POLICY

Purpose: translate an already-resolved shot into the strongest truthful provider syntax without allowing adapter availability to choose the execution provider.

Use with `references/execution-priority.md`.

## Core Separation

```text
execution-priority.md chooses WHERE to execute
this file chooses HOW to translate for that already-chosen path
```

An adapter is never a routing recommendation.

## Core Rule

```text
never sacrifice shot truth to preserve adapter specificity
```

A lower-specificity truthful adapter is better than a high-specificity stale or invented one.

## Translation Fallback Order

For the provider/path already selected:

```text
1. exact current provider + current model adapter
2. provider-family adapter with verified compatible semantics
3. generic provider adapter
4. provider-neutral shot spec / prompt-only handoff
```

Do **not** interpret this hierarchy as permission to choose an external provider over the native/local image model.

## Level 1 - Exact Current Adapter

Use only when:

- the execution provider/path has already been selected under `execution-priority.md`;
- provider/model is known;
- required semantics are verified sufficiently for the task;
- the active host exposes the expected operation.

Use native controls only when they actually exist.

## Level 2 - Provider-Family Adapter

Use when the selected provider is known but exact model/version differs and family-level semantics remain verified.

Do not assume stale enum values, old model names, reference limits, negative-prompt support, regional-edit controls, or cinematic selector names.

## Level 3 - Generic Adapter

Use `adapters/generic.md` when:

- provider/model is hidden or unknown;
- model is newer than cached adapter knowledge;
- controls changed;
- documentation is incomplete;
- execution accepts generic natural-language instructions.

The generic adapter must preserve professional quality, shot intent, geometry, optics/depth, lighting/exposure, color/tone, physical realism, preservation boundaries, reference roles, and output constraints.

## Level 4 - Shot Spec / Prompt Handoff

Use when no suitable execution path exists or the user requested prompt-only output.

Return a production-ready prompt/spec without implying generation occurred.

## Competitor Adapter Boundary

`adapters/magnific.md` and `adapters/higgsfield-soul-cinema.md` are explicit-target/benchmark translation adapters.

They must not be selected automatically for ordinary requests.

Only use them when:

- the user explicitly requests that provider/export; or
- a controlled benchmark explicitly names that provider.

## Capability-Specific Fallback

Fallback may occur per capability rather than for the whole provider.

If the chosen provider supports generation and references but lacks verified regional editing, keep the provider for supported features and translate the edit intent semantically; do not fabricate unsupported controls.

## Locked Parameter Rule

If a locked value has no literal provider control:

1. keep the lock in the universal shot;
2. translate its observable result into prompt language;
3. mark semantic translation when structured output is visible;
4. report a hard conflict only when the chosen provider genuinely cannot honor the requested outcome.

## Reference Fallback

If the chosen provider cannot accept all reference roles:

1. preserve the role map internally;
2. prioritize identity/product/preservation references;
3. translate lower-priority style/light references into observed visual DNA;
4. disclose meaningful conditioning loss rather than pretending every reference was used.

## Edit Fallback

```text
true targeted edit available -> targeted edit
reference-conditioned regeneration only -> disclose preservation risk
no image conditioning -> repair handoff prompt/spec
```

Do not call regeneration an exact edit.

## Version Drift

Live verified host/provider behavior wins over cached adapter details.

```text
live verified surface
> cached provider adapter
> generic adapter
```

At every level:

```text
user locks + Professional Quality Floor + universal shot
> provider defaults
```

## Failure Conditions

Incorrect behavior includes:

- scanning adapter files and selecting a provider because its adapter appears richer;
- choosing Magnific/Higgsfield automatically for cinematic quality;
- stale exact parameters used as current truth;
- locked lens/camera/stock silently changed for a provider preset;
- fabricated provider features;
- preservation constraints dropped during fallback;
- generic fallback treated as lower creative/cinematography quality.
