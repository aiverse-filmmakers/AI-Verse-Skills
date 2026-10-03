# Phase 8 Audit - Portable Skill, Manifest, and User Experience

Status: PASSED

Gate requirement:

> A capable agent receiving only this folder can understand how and when to use it.

## Scope Audited

Phase 8 tasks:

```text
8.1 final SKILL.md
8.2 aiverse.skill.yaml
8.3 standalone README
8.4 reference index
8.5 examples
8.6 verified pitfalls
```

## Package Entry Points

Verified present:

- `SKILL.md` — portable behavioral contract and routing entry point.
- `README.md` — human-readable standalone installation/use guide.
- `aiverse.skill.yaml` — AI-Verse sidecar runtime declaration.
- `references/INDEX.md` — progressive-loading map.
- `schemas/` — provider-neutral structured contracts.
- `adapters/` — provider translation layer.
- `examples/` — behavior illustrations.
- `references/verified-pitfalls.md` — verified failure/regression ledger.

## Gate Case 1 - Beginner With Only This Folder

Input:

```text
woman waiting for a taxi in London at night
```

Expected discovery path:

```text
SKILL.md
-> AUTO DIRECT
-> local workflow/reference files
-> Reality Gate
-> available local adapter or generic adapter
```

Result: PASS.

No camera knowledge, sibling skill, repository-root document, AI-Verse OS component, MCP, or provider credential is required to produce a complete prompt/specification.

## Gate Case 2 - Expert With Technical Locks

Input:

```text
ARRI ALEXA 35 character, 35mm, f/4, low angle, no haze, no flare
```

Expected discovery path:

```text
SKILL.md
-> MANUAL CAMERA
-> local locks/conflict references
-> local cinematography references
-> Reality Gate
-> adapter
```

Result: PASS.

Explicit values remain authoritative; AUTO is available locally for missing fields.

## Gate Case 3 - Reality Repair

Input:

```text
Make this AI portrait look real but keep identity, pose, clothes and framing unchanged.
```

Expected discovery path:

```text
SKILL.md
-> REALITY REPAIR
-> anti-AI taxonomy + affected realism domains
-> local diagnosis schema when useful
-> Reality Gate
-> edit-capable adapter if actually available
```

Result: PASS.

The package explains preserve/repair/allow-change boundaries and does not require a sibling editing skill.

## Gate Case 4 - Reference Match

Input:

```text
Match this reference's visual language, not its subject.
```

Result: PASS.

The package locally defines observable DNA, reference roles, uncertainty, metadata boundaries, and target-lock precedence.

Exact hardware inference is not required or implied.

## Gate Case 5 - Text-Only Host

Host state:

```text
vision = unavailable
generation = unavailable
editing = unavailable
```

Result: PASS.

The package still provides AUTO/CINEMATIZE/MANUAL/PROMPT ONLY reasoning and a generic final prompt. Reduced execution capability does not reduce the cinematography decision layer.

## Gate Case 6 - Tool-Capable Host

Host state:

```text
image generation/editing capability = actually granted
user requests image
```

Result: PASS.

`SKILL.md`, `host-capabilities.md`, and `host-action-policy.md` instruct execution when appropriate, while the manifest itself does not claim to grant tool/provider authority.

## Gate Case 7 - PROMPT ONLY Override

Input:

```text
Give me the final Seedream prompt only. Do not generate.
```

Result: PASS.

Explicit output intent prevents execution even on a tool-capable host.

## Gate Case 8 - Progressive Disclosure

Verified loading structure:

- routing/governance loaded when needed;
- workflow file chosen by request type;
- shot-domain references loaded only for relevant decisions;
- physical-realism domains loaded selectively;
- provider adapter loaded only after shot design;
- research evidence normally excluded from ordinary runtime;
- schemas loaded only when structured state/handoff is useful.

Result: PASS.

`references/INDEX.md` makes this path explicit.

## Gate Case 9 - Examples Are Illustrative, Not Hidden Authority

Verified examples:

- `examples/beginner-auto.md`
- `examples/expert-locks.md`
- `examples/reality-repair.md`
- `examples/reference-match.md`
- `examples/prompt-only.md`

Each states that it demonstrates behavior rather than defining hidden mandatory rules.

Result: PASS.

## Gate Case 10 - Verified Pitfalls Only

`references/verified-pitfalls.md` records failures exposed during implementation/gates, including:

- confidence serialization drift;
- focal-length/perspective conflation;
- cinematic effect stacking;
- film stereotype stacking;
- realism-as-dirt/pores/noise;
- repair drift;
- unavailable target-image pretending;
- beginner question bloat;
- reference-role collapse;
- exact-hardware hallucination;
- frozen-moment camera/pose drift;
- provider-core contamination;
- stale provider controls;
- adapter-existence/access confusion;
- V1 execution vs V2 visual-verification confusion;
- prompt-only override risk;
- standalone dependency risk.

Result: PASS.

No hypothetical filler is required for task completion.

## Standalone Dependency Audit

Core runtime contract requires no:

```text
parent-directory file
sibling AI-Verse skill
repository-root document
absolute user path
AI-Verse OS service
MCP server
API key
provider account
private machine state
```

Provider execution is optional and host-granted.

Result: PASS.

## Manifest Audit

`aiverse.skill.yaml`:

- declares low risk;
- requires read-only workspace effect only;
- keeps mutation/network/browser effects optional;
- declares no raw secret handles;
- uses explicit-postcondition verification;
- does not authorize providers or tools merely because adapters exist.

Result: PASS.

## Scope Audit

Still-image authority remains primary.

The package does not take ownership of:

- video timelines/cuts/captions/rendering;
- temporal motion choreography/lip-sync;
- product/app/web UI design;
- unrelated diagrams/logos/icons/general graphics.

Result: PASS.

## Audit Result

```text
portable entry-point violations: 0
standalone dependency violations: 0
sibling dependency violations: 0
hidden provider-access assumptions: 0
prompt-only override violations: 0
progressive-loading violations: 0
example-as-hidden-rule violations: 0
manifest authority violations: 0
still-image scope violations: 0
verified-pitfall filler violations: 0
```

# Phase 8 Gate Verdict

**PASSED**

A capable agent receiving only `cinematic-realism-director/` can determine:

- when the skill should and should not activate;
- which workflow to use;
- how explicit locks and AUTO interact;
- how to build and verify a cinematic shot;
- how to diagnose/repair realism failures;
- how to handle references without false hardware certainty;
- how to adapt to known or unknown providers;
- when to execute versus return a prompt/specification;
- how to degrade truthfully on weaker hosts;
- how to load the knowledge progressively.
