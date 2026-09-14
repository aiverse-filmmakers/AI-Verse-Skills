# Governed Self-Improvement for AI-Verse Skills

**Current status:** implemented for public beta.

The canonical cross-component and lifecycle contract is [PUBLIC_BETA.md](PUBLIC_BETA.md). This document explains the Skills-owned implementation.

## Core law

A candidate may be proposed more freely than it may be promoted.

Skills owns reusable procedure state. It does not own Brain strategy, general Memory, Gateway execution authority or Automations scheduling.

The public-beta default is:

```text
propose
```

## Implemented lifecycle

```text
candidate
-> proposal
-> evaluating
-> pending_approval | auto_eligible
-> applied
   OR rejected
   OR quarantined
```

The state is persisted under:

```text
<skills-root>/.aiverse/learning/
├── config.json
├── proposals/
├── archive/
├── usage.json
├── skill-state.json
├── budget.json
└── audit.ndjson
```

The audit ledger is hash-chained. Candidate package bytes remain outside active immutable generations until promotion.

## Modes

### off

Automatic review and curator-driven candidate creation are disabled.

Explicit user learning remains available:

```bash
aiverse-skills learn ...
aiverse-skills refine ...
```

### propose

Foreground correction, successful-procedure review and curator work may create proposals. Promotion requires approval.

### auto

Auto does not mean unrestricted self-modification.

Public-beta auto promotion is restricted to eligible low-risk learned/local changes where all mandatory gates remain true.

For a new `create` candidate:

- source ownership is `agent_learned`, or `workspace_local` with explicit owner configuration;
- risk is low and confidence is at least 0.90;
- evidence/provenance is present;
- candidate scope is valid; `workspace_local` requires a concrete workspace id;
- no requested capability/dependency expansion exists;
- no new Connection or credential is required;
- deterministic security admission passes with no review/deny finding;
- no duplicate gate blocks it;
- the exact immutable base generation has not changed since proposal/evaluation;
- current mode and policy still allow auto;
- the previous immutable generation remains a rollback target.

Repair/update/archive auto rules keep their existing learned-owner, target-integrity, security and permission gates.

If any gate fails, the proposal remains pending approval or is quarantined. Auto mode never grants execution authorization.

## Protected Skills

The following ownership classes cannot be autonomously overwritten:

```text
first_party
curated_upstream
user_authored
external
```

Corrections may still become evidence. The safe public-beta outcome is an upstream change or a separately owned learned Skill, not silent mutation of the protected package.

## Explicit learning

```bash
aiverse-skills learn --envelope candidate.json --candidate-dir ./candidate-skill
aiverse-skills refine --envelope repair.json --candidate-dir ./candidate-skill
```

A package candidate must contain `SKILL.md`.

Candidate packages are copied into the proposal store with a size bound. Symlinks are not allowed in learned candidate packages.

## Foreground correction

Gateway may trigger a repair candidate after a failed Skill use.

For repair/update candidates, Skills records:

- target Skill id;
- target ownership/protection;
- exact active generation id;
- target package digest;
- bounded evidence references;
- requested capabilities/dependencies;
- risk/confidence.

Apply uses compare-and-set semantics. If the active generation or target package digest changed after evaluation, promotion fails closed.

## Background review and cost limits

Automations or Gateway may wake review work, but Skills remains the state owner.

Current deterministic controls include:

- maximum pending proposals;
- maximum candidate bytes;
- maximum background reviews per day;
- explicit mode;
- no raw transcript/credential fields in candidate envelopes;
- no scheduler inside Skills.

## Evaluation

```bash
aiverse-skills proposals evaluate <proposal-id>
```

Evaluation checks:

- candidate structure;
- package safety scan;
- secret-like content;
- symlink containment;
- permission/dependency expansion request;
- target ownership;
- exact target generation/digest;
- duplicate/overlap signal;
- provenance presence.

Possible results include `pending_approval`, `auto_eligible` and `quarantined`.

## Promotion

```bash
aiverse-skills proposals apply <proposal-id> --approved-by <principal>
```

Promotion:

1. pins the current active generation;
2. records that generation as rollback backup;
3. copies it to a staging area;
4. adds/replaces the learned package;
5. regenerates provider-v1 metadata;
6. regenerates admission metadata;
7. verifies the complete candidate generation;
8. commits a new immutable generation;
9. atomically activates it;
10. records proposal state and audit events.

Active Skill bytes are never edited in place.

## Rollback

```bash
aiverse-skills proposals rollback <proposal-id>
```

Learning rollback only succeeds while that proposal's applied generation is still current. It refuses to overwrite a newer generation.

General immutable-generation rollback remains:

```bash
aiverse-skills rollback
```

## Usage

```bash
aiverse-skills usage record <skill-id> --success
aiverse-skills usage record <skill-id> --failure
```

Skills records bounded lifecycle counters and timestamps, not general user history.

## Curator

```bash
aiverse-skills curator run
```

Current curator behavior:

- marks learned Skills stale after configured inactivity;
- creates reversible archive-review proposals;
- detects high-overlap learned Skills;
- creates consolidation candidates;
- preserves provenance and audit history.

Archive and restore:

```bash
aiverse-skills curator archive <skill-id> --approved-by <principal>
aiverse-skills curator restore <skill-id>
```

Archive removes the learned Skill from the newly active immutable generation while preserving the source generation for reversible restore.

There is no autonomous hard deletion.

## Package admission

Self-learning uses the same separation as normal packages:

```text
integrity != admitted != trusted != ready != authorized
```

Promotion cannot grant execution authorization.

## Privacy

The proposal envelope prefers opaque/bounded `evidence_refs` instead of copied conversations.

Envelope fields representing raw transcripts, credentials, secrets, private keys or raw tool outputs are refused.

Candidate package content also passes deterministic safety scanning before promotion.

## Acceptance coverage

The public-beta test suite exercises:

- off/propose/auto behavior;
- explicit learn while automatic learning is off;
- immutable create/promotion;
- bounded safe auto-create of a new agent-learned Skill;
- explicit opt-in boundary for workspace-local auto-create;
- negative gates for risk, confidence, permissions, dependencies, Connections/credentials, duplicates, secrets and generation drift;
- bounded auto repair of an agent-learned Skill;
- protected first-party mutation refusal;
- secret candidate quarantine;
- generation/digest compare-and-set protection;
- usage tracking;
- stale/archive proposal creation;
- physical archive removal;
- restore;
- rollback protection;
- later-task learned Skill rediscovery and generation-bound successful execution receipt validation;
- Linux, macOS and Windows lifecycle/parser behavior.

## Future-only improvements

These are not required for public-beta completion:

- richer embedding-based deduplication;
- hosted multi-user policy/reputation services;
- automatic upstream pull-request creation;
- enterprise security/compliance scanner integrations;
- marketplace signing/reputation;
- broad live invocation acceptance for every external runtime adapter;
- autonomous hard deletion.
