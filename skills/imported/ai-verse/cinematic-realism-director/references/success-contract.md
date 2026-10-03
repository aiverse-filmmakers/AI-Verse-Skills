# Cinematic Realism Director - Success Contract and Failure Vocabulary

Status: FROZEN FOR V1

This contract defines what the skill may truthfully call success across generation, editing, analysis, reference matching, prompt-only, and explanation workflows.

The skill must never confuse a plausible plan, a successful tool invocation, and a visually verified result.

## Status Vocabulary

Use only these top-level execution states when an explicit status is needed:

```text
success
partial
blocked
failed
```

The status should normally remain concise and user-facing only when useful. Internal orchestration may track more detailed evidence.

## SUCCESS

`success` means every material postcondition for the requested operation is satisfied to the level the current host can actually verify.

Success requires all of the following that apply:

- the correct workflow was selected;
- explicit user locks were preserved;
- preservation constraints were respected;
- the shot/prompt/edit was constructed using the cinematic/realism rules;
- required Reality Gate checks completed at the highest level the host can perform;
- the requested artifact was actually produced when the host had the required execution capability;
- provider/tool execution returned without an unresolved blocking error;
- no material limitation was hidden from the user.

`success` does not mean the image is objectively perfect. It means the requested task reached its defined verified postconditions without a known material defect.

## PARTIAL

`partial` means meaningful progress or a useful deliverable was produced, but at least one material requested postcondition could not be completed or verified.

Examples:

- the host created an image but cannot inspect the returned output, so execution is confirmed but visual quality is unverified;
- Reality Repair diagnosis is complete but the host lacks an editing tool, so only the repair prompt/spec can be delivered;
- a requested provider is unavailable but a generic cinematic prompt was produced;
- most locks were preserved but one provider limitation prevents exact execution;
- a reference can be analyzed visually, but exact metadata requested by the user is unknowable;
- the tool generated an image but one observable lock is wrong and no further edit/regeneration can be executed.

A partial result must identify the unresolved limitation when it matters to the user's next action.

## BLOCKED

`blocked` means the requested task cannot proceed to a meaningful deliverable because a required input, capability, authorization, or compatible execution path is absent.

Examples:

- user requests preservation-sensitive editing but no source image is available and the missing visual information cannot be reconstructed from text;
- user asks to generate an image but explicitly forbids prompt-only output and no image tool exists;
- the required image tool exists but the user/runtime has not granted access and no acceptable fallback is allowed;
- mutually contradictory hard locks cannot be reconciled without user choice and the task cannot reasonably continue under either interpretation;
- the target provider rejects the task and the user explicitly requires that provider with no fallback.

`blocked` is not failure when the skill correctly identifies an external prerequisite that prevents execution.

## FAILED

`failed` means the skill attempted an operation that should have been possible but did not satisfy the required postconditions because of an execution or logic failure.

Examples:

- the image tool errors after a valid request and retries/fallback rules are exhausted;
- the skill violates a hard user lock;
- an edit unexpectedly changes a preservation-locked product or identity and cannot be corrected;
- the final prompt contradicts the structured shot specification;
- the wrong workflow is used and produces an unusable result;
- the Reality Gate identifies a material defect that remains unresolved while the skill nevertheless would otherwise claim completion.

A failed result should state the material failure, not bury it in optimistic language.

## Verification Levels

Track the strongest level actually achieved.

### V0 - Reasoning only

Verified:

- task intent;
- workflow selection;
- locks;
- structured shot logic;
- prompt/spec consistency.

Not verified:

- actual generated pixels.

Typical for text-only hosts.

### V1 - Execution confirmed

Verified:

- provider/tool accepted and completed the requested operation;
- an output artifact/reference was returned.

Not necessarily verified:

- whether the image visually satisfies the cinematic target.

### V2 - Visual inspection completed

Verified:

- returned image was inspected by a vision-capable host;
- observable locks/preservation constraints were checked where practical;
- Reality Gate was applied to the actual output.

### V3 - Comparative/iterative acceptance

Verified:

- V2 completed;
- material defects were corrected through one or more iterations where tools allow;
- final inspected output satisfies the task-specific acceptance criteria.

V3 is ideal for capable iterative hosts but is not mandatory for every environment.

## Operation-Specific Success Contracts

### AUTO DIRECT / New Image Generation

Full success requires:

- minimal input expanded into a coherent cinematic shot without unnecessary questioning;
- story/subject/environment determine the capture choices;
- user locks preserved;
- no unjustified cinematic clichés automatically added;
- provider-neutral shot intent created before provider adaptation;
- final prompt/tool request internally consistent;
- if generation capability exists and image output was requested, image generation executed;
- if image can be inspected, actual output passes the Reality Gate or is iterated/reported partial.

Text-only success is valid when the user or host can only receive a prompt/specification. In that case success applies to the prompt task, not to nonexistent image generation.

### CINEMATIZE

Full success requires:

- core subject, action, purpose, and requested style preserved;
- vague quality adjectives replaced or supported with concrete cinematic decisions;
- photographic/physical coherence improved;
- no unnecessary redesign of subject or scene;
- final output suited to the requested/available provider.

### REALITY REPAIR

Full success requires:

- source image actually available to the analyzing/editing host when visual diagnosis is claimed;
- preserve / repair / allow-change boundaries established;
- synthetic-looking causes diagnosed at the appropriate confidence level;
- repair targets only the necessary systems unless user requests broader redesign;
- preservation locks remain intact;
- if editing is available and requested, edit is executed;
- if resulting image is inspectable, compare against source and verify both realism improvement and preservation.

If editing is unavailable, a complete diagnosis + edit specification can be `success` for a prompt-only request, but only `partial` when the user requested an executed edit.

### REFERENCE MATCH

Full success requires:

- distinguish observable visual traits from uncertain metadata;
- derive reusable composition, perspective, light, depth, color, texture, atmosphere, material, and tonal characteristics where visible;
- never invent exact camera/lens/stock metadata as fact;
- transfer the visual DNA without needlessly copying irrelevant content;
- preserve any explicit subject/product/identity constraints in the target.

### MANUAL CAMERA

Full success requires:

- all valid explicit user values represented as locks;
- unspecified fields remain AUTO;
- AUTO choices support rather than override the locked package;
- direct contradictions are handled under `locks.md`;
- final provider adaptation preserves the intended observable result.

### PROMPT ONLY

Full success requires:

- no image generation/editing is invoked;
- prompt reflects the full cinematic shot intent;
- user locks are present;
- provider-specific syntax is used only when known and appropriate;
- unsupported parameters are expressed semantically rather than fabricated;
- output is ready to paste/use with minimal additional work.

### SHOT RECIPE / EXPLAIN

Full success requires:

- explain actual decisions rather than inventing hidden metadata;
- separate user-locked choices from AUTO choices when useful;
- distinguish physical principle, provider-specific behavior, and inference;
- keep the explanation concise unless detailed analysis is requested.

## Reality Gate and Success

The Reality Gate is a release condition for any workflow that claims a cinematic/photorealistic result.

Before full success, check all relevant dimensions available to the host:

- perspective and camera geometry;
- depth/focus plausibility;
- lighting motivation and direction;
- shadow consistency;
- exposure and highlight behavior;
- skin/hair/eye realism where present;
- material response and roughness;
- reflections/refractions where present;
- contact, weight, gravity and environment interaction;
- texture/grain/halation/bloom restraint;
- color coherence;
- preservation constraints;
- user locks;
- obvious AI artifacts.

For prompt-only hosts, apply the gate to the planned shot and instructions. For vision-capable hosts, apply it to the actual output when available.

## Tool Success Is Not Visual Success

Never equate:

```text
API returned 200
```

with:

```text
cinematic target achieved
```

If the host cannot inspect output, report execution as confirmed but visual verification as unavailable when that distinction matters.

## Confidence and Unknowns

The skill must not convert uncertainty into fake certainty merely to make a result look complete.

Examples:

- exact lens from a reference: may be unknown;
- exact film stock: may be unknown;
- exact key-to-fill ratio from a compressed image: may be approximate;
- provider's private prompt transformation: unknown unless publicly documented.

Unknown technical metadata does not block success when observable visual behavior can be reproduced without it.

## Retry and Iteration Principle

Where the host supports repeated generation/editing and inspection:

1. inspect the first output;
2. identify only material failures;
3. preserve what already works;
4. make the smallest useful correction;
5. re-run the Reality Gate.

Do not regenerate endlessly for trivial differences. The detailed retry policy may be refined during eval phases.

## User-Facing Result Discipline

Do not flood beginners with internal status machinery.

Normally:

- deliver the image or prompt directly;
- mention limitations only when material;
- expose technical verification/status on request or when partial/blocked/failed.

For agents, tests, structured workflows, or explicit diagnostic requests, the following shape is preferred:

```text
status: success | partial | blocked | failed
summary: ...
verification_level: V0 | V1 | V2 | V3
locks_preserved: true | false | unverified
reality_gate: pass | partial | fail | not_applicable
artifact: ...
remaining_uncertainty: ...
```

This is a conceptual result contract. The exact machine-readable schema may be defined later if needed.

## Failure Conditions for This Contract

The skill violates Task 0.5 if it:

- claims success despite a known broken hard lock;
- claims an image was generated when only a prompt exists;
- calls an API response visual verification;
- calls a repair successful without checking preservation when inspection is available;
- labels missing external authorization as an internal skill failure;
- treats unknowable reference metadata as a reason the visual match itself must fail;
- hides material unresolved limitations behind generic positive language;
- forces verbose status output on every beginner request.

## Task 0.5 Acceptance

Task 0.5 is satisfied when:

- `success`, `partial`, `blocked`, and `failed` have non-overlapping operational meanings;
- generation, edit, analysis/reference, manual-lock, prompt-only, and explanation tasks each have clear success postconditions;
- execution confirmation is separated from visual verification;
- Reality Gate participation is defined;
- missing capabilities degrade truthfully rather than being reported as completed work;
- status reporting remains lightweight for normal users and explicit for agent/test contexts.
