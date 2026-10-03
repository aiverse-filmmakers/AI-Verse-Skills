# Phase 7 Audit - Provider and Host Adapters

Status: PASSED
Phase: 7

## Gate Requirement

> Core shot intent survives translation across providers without becoming seven separate cinematic brains.

## Evidence Audited

Adapters:

- `adapters/generic.md`
- `adapters/openai-image.md`
- `adapters/gemini-image.md`
- `adapters/seedream.md`
- `adapters/flux.md`
- `adapters/magnific.md`
- `adapters/higgsfield-soul-cinema.md`

Policies:

- `references/adapter-fallback-hierarchy.md`
- `references/host-action-policy.md`
- `references/host-capabilities.md`
- `references/locks.md`
- `references/reality-gate.md`

## Audit Cases

### Case 1 - Beginner cinematic portrait

Input concept:

```text
woman waiting for a taxi in London at night
```

Expected invariant across providers:

- same story moment;
- same visual hierarchy;
- same camera geometry;
- same motivated urban-night lighting strategy;
- same realism targets;
- no provider adds mandatory grain, flare, teal/orange, rim light, or shallow depth.

Result: PASS.

Provider adapters alter serialization and verified controls only.

### Case 2 - Expert locked camera setup

Locked values:

```text
ARRI ALEXA 35
35mm
f/4
low angle
rectilinear perspective
natural window light
no grain
```

Expected:

- literal locks retained where provider can accept them;
- unsupported literal controls translated into visible behavior;
- no provider silently substitutes a different camera/lens/aperture;
- exact provider control absence does not erase the lock.

Result: PASS.

### Case 3 - Reality Repair

Preserve:

```text
identity
pose
composition
wardrobe
background architecture
```

Repair:

```text
plastic skin
floating fabric edge
inconsistent catchlights
```

Expected:

- preserve/change boundary survives every adapter;
- targeted editing is preferred where provider/host exposes it;
- regeneration is not mislabeled as exact editing;
- missing edit capability degrades to repair handoff/spec.

Result: PASS.

### Case 4 - Multi-reference identity/product/style

Roles:

```text
Reference A = identity
Reference B = product geometry/material
Reference C = lighting/color language
```

Expected:

- role map remains separate;
- provider reference limitations trigger prioritization/fallback rather than role collapse;
- style reference cannot override identity/product preservation locks.

Result: PASS.

### Case 5 - Magnific Cinematic

Expected:

- verified current cinematic controls are used only when Magnific is actually active;
- compound provider fields do not overwrite decomposed universal shot decisions;
- unsupported nuance remains in prompt language;
- control menu is not copied into the universal brain.

Result: PASS.

### Case 6 - Higgsfield Soul Cinema + Soul identity

Expected:

- Soul identity remains identity continuity only;
- shot spec controls composition/camera/light/color/realism;
- provider enhancer does not become the upstream director;
- still-frame hero-frame output remains within V1 scope.

Result: PASS.

### Case 7 - FLUX positive prompting

Expected:

- avoidance language translates into positive desired-state language when negative prompts are unsupported;
- cinematic intent remains unchanged;
- no universal negative-prompt block is injected.

Result: PASS.

### Case 8 - Unknown/new provider model

Condition:

```text
provider is named but exact model/version is newer than verified adapter
```

Expected:

- exact stale parameters are not guessed;
- fallback hierarchy uses provider-family semantics only when verified;
- otherwise use `adapters/generic.md`;
- no reduction in core cinematography quality.

Result: PASS.

### Case 9 - Host action behavior

Scenarios:

```text
image requested + image tool available
image requested + no image tool
PROMPT ONLY + image tool available
edit requested + target image missing
execution succeeds but result cannot be inspected
```

Expected:

```text
generate/edit
prompt/spec
never generate
no fake edit
V1 only, not V2
```

Result: PASS.

## Cross-Adapter Invariants

Verified:

- provider-neutral Cinematic Shot Spec remains upstream authority;
- explicit user locks remain authoritative;
- preservation locks survive provider translation;
- camera position is never replaced by focal length shorthand;
- named camera/lens references are not claimed as literal physical simulation;
- provider controls are used only when verified/current;
- reference roles survive translation;
- unknown capabilities fall back rather than being fabricated;
- PROMPT ONLY always overrides execution;
- adapter existence does not imply provider access/authorization;
- V1 execution is distinguished from V2 visual verification;
- still-image scope is preserved.

## Violation Counts

```text
provider-core contamination: 0
explicit-lock violations: 0
preservation violations: 0
reference-role violations: 0
fabricated-control violations: 0
stale-model hard-dependency violations: 0
false hardware-certainty violations: 0
false provider-access claims: 0
prompt-only override violations: 0
false visual-verification claims: 0
still-vs-video scope violations: 0
```

## Phase 7 Gate Verdict

**PASSED**

Phase 7 now provides one cinematic brain with multiple truthful translation layers rather than provider-specific creative brains.

Carry forward into Phase 8:

1. `SKILL.md` must route into the universal workflows first and adapters second.
2. The portable skill must work without any provider connection.
3. The manifest must describe optional image/network effects without granting them.
4. `generic.md` remains mandatory fallback.
5. The final skill may generate/edit only when the current host actually exposes the required capability and user output intent permits execution.