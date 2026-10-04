# Magnific Cinematic Explicit-Target Adapter

Status: OPTIONAL EXPLICIT-TARGET / BENCHMARK ADAPTER

Purpose: translate an already-resolved Cinematic Shot Spec into Magnific Cinematic instructions **only when the user explicitly requests Magnific output/execution or a controlled benchmark names Magnific**.

## Non-Negotiable Boundary

Magnific is a competitor/reference system for the Cinematic Realism Director. It is **not** a default backend.

```text
ordinary image request -> DO NOT auto-select Magnific
native/local host image capability available -> use native/local
user explicitly requests Magnific -> this adapter may be used
controlled benchmark explicitly names Magnific -> this adapter may be used
```

The presence of this file must never cause provider routing.

Execution routing is governed by `references/execution-priority.md`.

## Why This Adapter Exists

This file exists for:

- user-requested Magnific prompt export;
- user-requested Magnific execution when the provider is genuinely connected/permitted;
- controlled comparative benchmarking;
- compatibility with existing Magnific workflows;
- provider research/translation maintenance.

It does not outsource the skill's cinematic intelligence to Magnific.

## Creative Authority

```text
Professional Quality Floor + Cinematic Shot Spec = creative truth
Magnific controls/prompt = optional translation surface
```

The shot must already contain composition, camera relationship, optics/depth, motivated light, exposure, color, texture, physical realism, and user locks before this adapter runs.

Do not use Magnific presets to invent missing cinematography.

## Explicit Invocation Requirement

Before using this adapter, at least one must be true:

1. user explicitly says to use/export for Magnific;
2. benchmark/evaluation explicitly specifies Magnific.

If neither is true, do not load/use this adapter for execution.

## Translation Policy

When explicitly invoked:

1. consume the resolved provider-neutral shot;
2. inspect the current live Magnific surface if available;
3. map only exact compatible controls;
4. keep unsupported nuance in natural-language prompt form;
5. preserve every user lock;
6. leave conflicting/unavailable native fields neutral rather than substituting a different creative choice;
7. never let provider convenience presets redesign the shot.

## Current Control Families

Magnific Cinematic has historically exposed controls such as camera/capture reference, lens family, focal length, aperture, shot type, film stock, lighting, motion blur, grain, halation, tonal look, references, aspect ratio, and resolution.

These are provider-specific conveniences, not the universal ontology and not proof of literal physical simulation.

Use live verified controls when execution is actually occurring. Otherwise prefer natural-language translation rather than stale enums.

## Camera / Lens / Film References

If a requested camera/lens/film reference exists natively, it may be mapped when explicitly using Magnific.

If it does not exist:

- preserve the original lock in the universal shot;
- express the observable behavior in prompt language;
- do not silently substitute the nearest brand/preset.

Named controls do not replace camera distance, perspective, source geometry, exposure, or color logic.

## Cinematic Controls Are Not the Creative Brain

Do not automatically enable:

- movie-look presets;
- anamorphic flare;
- haze;
- rim light;
- maximum shallow depth;
- teal/orange;
- strong grain;
- halation;
- motion blur.

The Professional Quality Floor and shot logic decide the image first.

## Texture

When Magnific is explicitly used, translate the resolved texture requirement.

Subtle organic photographic texture is normally part of the skill's professional finish, but visible/strong provider grain or halation must still match the shot.

Do not stack film stock + strong grain + halation + tonal preset merely because the controls exist.

## References / Editing

If explicit Magnific execution is requested and current tools support references or targeted edits:

- keep identity/product/style roles distinct;
- prefer the smallest preservation-safe operation;
- do not call broad regeneration an exact local edit;
- do not send user images to Magnific without actual host permission.

## Live-Schema Drift

When explicitly executing Magnific:

```text
current verified live schema
> cached adapter knowledge
> generic natural-language translation
```

At every level:

```text
user locks + Professional Quality Floor + universal shot
> Magnific defaults
```

## Failure Conditions

This adapter is used incorrectly if:

- Magnific is selected for an ordinary image request without explicit user request/benchmark;
- Magnific is preferred because it looks more cinematic than the native/local model;
- its presets supply the core cinematography instead of translating resolved intent;
- unavailable controls cause user locks to be changed;
- adapter presence is treated as provider access;
- a successful Magnific call is called visually successful without inspection.
