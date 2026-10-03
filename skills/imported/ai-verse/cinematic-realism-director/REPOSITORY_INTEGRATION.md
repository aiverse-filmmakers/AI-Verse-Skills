# Repository Integration Contract

Status: Phase 10 integration decision
Package: `cinematic-realism-director`
Branch: `feat/cinematic-realism-director`

## Canonical Placement

The V1 package remains canonically located at:

```text
skills/imported/ai-verse/cinematic-realism-director/
```

This is the repository namespace reserved for AI-Verse-authored first-party skills.

The package is therefore **first-party-native** to AI-Verse-Skills while remaining independently copyable as a portable Agent Skill.

## Ranked Registry Decision

V1 does **not** silently insert this package into the existing ranked employee catalog in:

```text
registry/skills.json
registry/packages.json
```

Reason:

- the current registry intentionally declares exactly 20 foundation + 100 employee capabilities;
- employee ranks 1-100 are already occupied;
- the `full` profile explicitly describes the existing 120 canonical capabilities;
- adding a new rank, replacing an existing ranked skill, or renumbering the roster is a product/catalog decision, not a package implementation detail.

Therefore Phase 10 preserves the existing canonical accounting instead of casually turning the ranked catalog into 101 employees or displacing another capability.

This is a deliberate compatibility choice, not an omission. Ranked-catalog promotion remains a separate explicit product decision.

## Metadata Already Applicable

No new source-trust record is required for V1 because `registry/trust-policy.json` already classifies:

```text
aiverse-filmmakers/AI-Verse-Skills
```

as first-party, MIT, redistributable, vendoring-allowed, and non-autonomously mutable.

No new runtime-adapter record is required because `registry/runtime-adapters.json` describes package-agnostic exposure surfaces. The Cinematic Realism Director uses the same portable directory package contract as other Agent Skills-compatible packages.

No alias is required because the canonical skill name is already stable:

```text
cinematic-realism-director
```

No operator dependency is required for core operation. Image/provider execution remains optional host capability and is never granted by the skill manifest.

## Current Integration Level

V1 guarantees:

```text
first-party package namespace        YES
portable SKILL.md                    YES
AI-Verse sidecar manifest            YES
standalone folder operation          YES
repository contract tests            YES
adapter materialization compatibility YES
ranked employee roster promotion     NO (deliberately deferred)
full-profile automatic installation  NO until explicit catalog promotion
```

The package can still be:

- copied as a standalone Agent Skill;
- loaded directly by a capable client from this repository path;
- materialized through the repository's directory adapter mechanics when included in a generation;
- integrated into a future catalog release without changing its internal package contract.

## Future Ranked-Catalog Promotion

If AI-Verse later decides this skill should become a ranked employee capability, that change must be explicit and atomic.

At minimum, promotion must update and verify:

1. `registry/skills.json`
   - assign an intentional employee rank;
   - update employee/total counts if the roster expands;
   - or explicitly replace/reorder another entry if the product keeps exactly 100 employees.
2. `registry/packages.json`
   - add the first-party package entry under the `ai-verse` source;
   - keep package counts consistent;
   - use an appropriate first-party source pin/provenance decision.
3. `registry/profiles.json`
   - add to `full`;
   - normally add to `creator` and `filmmaker`;
   - update profile descriptions/count language where required.
4. `registry/roles.json`
   - consider `ai-filmmaker` and `creative-director` only if role semantics benefit.
5. registry validation and contract tests.

Promotion must never be achieved by silently changing an existing rank or dropping another capability.

## Runtime Adapter Compatibility

The repository adapter mechanism is package-directory based after a generation has been pinned.

Phase 10 tests create an isolated synthetic generation containing the complete Cinematic Realism Director package, then materialize it through the same adapter machinery used for Codex/Claude/Hermes/Gemini/OpenClaw exposure.

The test must verify:

- the complete directory survives materialization;
- the target `SKILL.md` is intact;
- references, adapters, schemas, examples and evals survive;
- package digest remains identical;
- `adapter-verify` semantics accept the materialized target;
- no provider access or execution authority is implied.

## Standalone Invariant

Repository integration must never weaken the package's original invariant:

> Copying only `cinematic-realism-director/` must retain the core cinematic reasoning, workflows, schemas, adapters, examples, and prompt-only behavior.

Registry state is distribution metadata, not a hidden runtime knowledge dependency.

## Task Mapping

```text
10.1 canonical registry placement     -> this document
10.2 required registry metadata       -> no ranked-registry mutation required for V1; existing first-party trust/runtime policy applies
10.3 contract tests                   -> tests/test_cinematic_realism_director_contract.py
10.4 standalone package test          -> same test module, isolated-copy suite
10.5 runtime adapter exposure test    -> same test module, synthetic-generation materialization suite
```
