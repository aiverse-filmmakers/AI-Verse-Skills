# Higgsfield Soul Cinema Adapter

Status: RUNTIME ADAPTER
Task: 7.7
Verified against public first-party Higgsfield tooling and repository evidence on 2026-10-03.

Purpose: translate the provider-neutral Cinematic Shot Spec into Higgsfield Soul Cinema / Soul-aware still-image instructions without turning Higgsfield product semantics into the universal cinematic brain.

## Core Boundary

```text
Cinematic Shot Spec = creative truth
Higgsfield adapter = provider translation / routing
Soul identity = identity continuity, not cinematography authority
```

Do not infer private prompt enhancers, hidden control weights, training data, or proprietary lens-profile logic.

## Current Public Surface

Current first-party Higgsfield agent tooling publicly exposes:

- `soul_cinematic` as a Soul-aware cinematic generation route;
- reusable Soul identity references through Soul ID / Soul Character systems;
- quality tiers including 1.5K and 2K for Soul image generation in current public tooling;
- ordinary prompt-driven generation through the Higgsfield generation CLI/skill.

Current model names and controls are provider-specific and may drift. Recheck the live Higgsfield surface before depending on exact names or parameters.

## When to Use

Use this adapter when:

- the active provider is Higgsfield and the requested still-image path is Soul Cinema / `soul_cinematic`;
- a user explicitly asks for Soul Cinema behavior;
- a reusable Soul identity reference is available and should remain identity-locked;
- the host exposes current Higgsfield generation tooling with Soul support.

Do not use merely because the user says `cinematic` when another provider is active.

## Input

Consume:

- resolved Cinematic Shot Spec;
- active workflow;
- user and preservation locks;
- optional Soul identity reference;
- optional reference-role map;
- host capability class;
- V0 Reality Gate result.

The adapter must not redesign unresolved cinematic decisions on its own.

## Soul Identity Separation

If a Soul identity reference exists:

```text
identity reference -> face / identity continuity
shot spec -> camera / composition / light / color / realism
```

Do not let an identity asset silently override:

- age or appearance instructions explicitly locked by the user;
- pose;
- wardrobe;
- shot size;
- lens behavior;
- lighting;
- color design;
- scene geometry.

If the identity system conflicts with a hard preservation constraint, preserve the user constraint and report the conflict rather than silently substituting.

## Prompt Translation

Use strong natural language that preserves the universal shot structure:

1. subject / action / story moment;
2. environment and production context;
3. composition, camera position, angle and perspective;
4. focal/lens/depth behavior;
5. motivated lighting and exposure;
6. color, density and tonal treatment;
7. skin, material, contact and reflection realism;
8. atmosphere and justified optical/capture texture;
9. explicit preservation instructions when editing/reference conditioning;
10. output/aspect requirements.

Do not replace physical instructions with `cinematic`, `movie still`, or prestige camera names alone.

## Camera and Lens Language

Higgsfield public engineering material supports camera/lens vocabulary as useful learned visual priors, but the adapter must still express observable behavior.

If the user locks a camera or lens reference:

- keep the literal reference where useful;
- preserve its observable intended behavior;
- do not claim literal physical simulation.

If the model response to a named lens is weak, reinforce only the relevant observable traits rather than exaggerating every possible artifact.

## Beginner Enhancement

For short prompts, the universal AUTO DIRECT workflow completes the shot before this adapter runs.

Do not outsource core cinematography reasoning to an opaque provider enhancer.

Provider enhancement, when available, is an execution convenience after the shot spec is resolved.

## Reference Handling

Keep reference roles explicit.

Example:

```text
Soul ID: identity only
Reference image 1: wardrobe / product geometry
Reference image 2: lighting and color language
Shot Spec: target composition and cinematography
```

Do not treat every reference as equal global style authority.

## Color Continuity

If Higgsfield exposes current color/palette continuity controls, map only the relevant shot-spec color intent into them.

The universal color design remains:

- white balance;
- palette;
- separation;
- saturation;
- density;
- highlight/shadow chroma;
- skin treatment.

A provider palette feature does not replace this reasoning.

## Reality Repair

When repairing an existing image through a Higgsfield-capable host:

- preserve the actual target image and identity references;
- use the smallest provider operation capable of the requested change;
- keep `PRESERVE`, `CHANGE`, and `DESIRED PHYSICAL RESULT` separate;
- avoid full regeneration when a targeted operation is available and preservation matters;
- perform a post-generation Reality Gate if the host can inspect the result.

If current Higgsfield tooling cannot guarantee the required edit preservation, fall back to an explicit repair prompt/spec rather than claiming exact preservation.

## Hero-Frame Principle

For broader cinematic workflows, treat the still image as a hero frame:

```text
resolve still-frame visual truth first
-> verify it
-> hand off to temporal/video systems later if requested
```

Do not expand this V1 skill into video direction merely because Higgsfield supports video.

## Unsupported or Changed Controls

If a remembered Higgsfield control is missing or changed:

1. preserve the universal shot decision;
2. translate it into natural-language visible behavior;
3. use only current verified provider parameters;
4. fall back to `adapters/generic.md` when exact support is uncertain;
5. never invent a provider flag.

## Host Degradation

- Higgsfield generation tool connected and user asks for an image: execute through the current permitted image route.
- Higgsfield unavailable: return the adapted prompt/spec or use another granted provider through its adapter.
- PROMPT ONLY: never execute generation.
- No target image available for an edit: do not pretend the edit occurred.

## Verification

Before handoff or execution, verify:

- user locks survived;
- Soul identity is used only for identity continuity;
- reference roles survived;
- no hidden hardware certainty was invented;
- provider version-specific assumptions are current or omitted;
- cinematography remains provider-neutral upstream;
- Reality Gate corrections survived translation.

Acceptance: Soul Cinema receives a coherent cinematic shot while identity continuity and provider semantics remain separate from universal creative authority.