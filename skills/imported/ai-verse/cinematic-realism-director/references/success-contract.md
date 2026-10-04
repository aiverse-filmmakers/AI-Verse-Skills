# Cinematic Realism Director - Success Contract

Status: RUNTIME CONTRACT

Purpose: define what the skill may truthfully call success across generation, editing, analysis, reference matching, prompt-only, and explanation workflows.

The skill must never confuse a plausible plan, a successful tool invocation, and a visually verified result.

## Status Vocabulary

```text
success
partial
blocked
failed
```

### success

Every material postcondition for the requested operation is satisfied to the strongest level the current host can actually verify.

For photographic/cinematic work, success also requires the Professional Quality Floor to be satisfied unless the user explicitly requested a degraded/amateur/raw/technical-clean aesthetic.

### partial

A useful result exists but at least one material requested postcondition could not be executed or verified.

Examples:

- image generated but host cannot inspect it;
- repair diagnosis complete but editing unavailable;
- explicit provider unavailable and fallback prompt supplied;
- one hard provider limitation prevents exact execution.

### blocked

A required input/capability/authorization/compatible path is absent and no acceptable deliverable can proceed under the user's constraints.

Examples:

- preservation-sensitive edit requested with no source image;
- user forbids prompt fallback and no image tool exists;
- explicit provider is unavailable and fallback is forbidden;
- mutually contradictory hard locks require user choice.

### failed

An operation that should have been possible did not satisfy required postconditions because of an execution or logic failure.

Examples:

- hard user lock violated;
- professional quality floor omitted from a normal AUTO request;
- requested mobile/candid medium erased;
- ordinary request auto-routed to Magnific/Higgsfield;
- native/local image model bypassed by external MCP without justification;
- preservation-locked identity/product changed and not corrected;
- Reality Gate identifies an unresolved material defect but completion is claimed.

## Verification Levels

### V0 - Reasoning / specification

Verified:

- task intent and medium;
- professional specialty and quality floor;
- workflow;
- locks;
- structured shot logic;
- provider/execution routing logic;
- prompt/spec consistency.

Actual generated pixels are not verified.

### V1 - Execution confirmed

Verified:

- tool/provider accepted and completed the operation;
- output artifact/reference returned.

Not verified:

- whether the image visually satisfies the target.

### V2 - Visual inspection completed

Verified:

- returned image inspected;
- observable locks/preservation checked where practical;
- Professional Quality Floor and Reality Gate applied to the actual output.

### V3 - Comparative / iterative acceptance

Verified:

- V2 completed;
- material defects corrected through one or more iterations where possible;
- final inspected output satisfies task-specific acceptance.

## Global Success Requirements

Where applicable, full success requires:

1. literal user content preserved;
2. explicit user/preservation/provider locks preserved;
3. requested/implicit photographic medium identified correctly;
4. Professional Quality Floor applied to unspecified decisions;
5. composition/camera relationship/optics/light/exposure/color/texture/physical realism coherent;
6. professional finish without unjustified cinematic cliché stacking;
7. execution path obeys `execution-priority.md`;
8. Magnific/Higgsfield not auto-selected for ordinary requests;
9. prompt-only override honored;
10. execution claims and visual-verification claims remain distinct.

## AUTO DIRECT

Full success requires:

- a sufficient one-line prompt completes without unnecessary technical questions;
- the correct professional specialty is inferred from the requested medium;
- the user does not need to add `professional`, `cinematic`, `Hollywood`, `ARRI`, `high quality`, or equivalent words;
- professional composition, light, exposure, tonal response, color, material realism and finishing are automatically supplied;
- most normal photographic/cinematic work receives subtle organic filmic texture unless the medium/user calls for pristine/no-grain output;
- cliché effects remain absent unless justified;
- provider-neutral image design is complete before provider adaptation;
- native/local generation is used first when available and adequate.

A merely competent literal rendering is not AUTO DIRECT success.

## Mobile / Selfie / Candid Medium Fidelity

Professional quality must not erase the requested medium.

For example:

- iPhone/selfie success = elite mobile photography/editing while retaining believable phone perspective/processing;
- candid success = decisive, believable, non-performative professional photography rather than staged cinema posing.

## CINEMATIZE

Success requires stronger professional visual causality and finishing while preserving the concept and locks. Do not use effect stacking as the definition of `more cinematic`.

## REALITY REPAIR

Success requires:

- real target image available when visual diagnosis/edit is claimed;
- preserve/repair/allow-change boundaries established;
- causes diagnosed before surface decoration;
- smallest useful repair scope;
- preservation locks intact;
- resulting image inspected when possible.

## REFERENCE MATCH

Success requires:

- observable traits separated from uncertain metadata;
- composition/perspective/light/depth/color/texture/material/atmosphere transferred where relevant;
- exact hardware not invented;
- target subject/product/identity locks preserved.

## MANUAL CAMERA

Success requires:

- all valid explicit values remain locks;
- unspecified fields remain AUTO;
- Professional Quality Floor completes missing fields without overriding locks;
- final provider translation preserves the intended observable result.

## PROMPT ONLY

Success requires:

- no image execution;
- prompt already contains professional quality floor and complete image direction;
- provider-specific syntax used only when requested/known;
- unsupported parameters expressed semantically rather than fabricated.

## Execution Priority and Success

Unless a provider is explicitly locked:

```text
native/local image capability
> external provider only for missing material capability
> prompt/spec
```

Using an external MCP/provider before an adequate native/local path is a contract violation.

Magnific/Higgsfield may be used only for explicit target/export or controlled benchmark requests.

## Reality Gate and Success

Before full success, check all relevant available dimensions:

- professional medium/specialty fit;
- composition and camera geometry;
- depth/focus/motion;
- motivated lighting;
- exposure/highlight behavior/shadow density;
- color separation and grade;
- skin/hair/eye realism;
- materials/reflections/refractions;
- contact/weight/gravity/environment;
- subtle texture vs unjustified visible effects;
- preservation constraints;
- explicit locks;
- obvious AI artifacts.

## Tool Success Is Not Visual Success

Never equate a successful API/tool response with the cinematic/professional target being visually achieved.

If output cannot be inspected, report execution as confirmed but visual verification as unavailable when the distinction matters.

## Confidence and Unknowns

Unknown technical metadata does not need to be invented.

Examples:

- exact lens from a reference may be unknown;
- exact stock may be unknown;
- exact key-to-fill ratio may be approximate;
- private provider prompt transformation is unknown unless documented.

Observable visual behavior may still be reproduced without fake certainty.

## Retry / Iteration

When generation/editing and inspection are available:

1. inspect output;
2. identify material failures;
3. preserve what works;
4. attempt focused correction through the current native/local path first when practical;
5. use an external fallback only under execution-priority rules;
6. re-run Reality Gate.

Do not endlessly regenerate for trivial differences.

## User-Facing Discipline

Normally deliver the image/prompt directly and mention only material limitations.

Do not flood beginners with internal status machinery unless requested.
