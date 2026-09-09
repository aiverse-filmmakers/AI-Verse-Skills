# Safe Self-Improvement for AI-Verse-Skills

## Goal

Allow AI-Verse to learn reusable operational capabilities from successful work without turning self-improvement into uncontrolled self-modification.

The recommended model is inspired by the strongest parts of current Hermes Agent, OpenClaw Skill Workshop, LifeOS SuggestSkills/CreateSkill separation, Letta's separation of skills from runtime enforcement, and NVIDIA's skill security/evaluation pipeline.

## Core rule

**The agent may propose capabilities more freely than it may promote capabilities.**

Creation and trust are different permissions.

A successful workflow should not immediately become a trusted `SKILL.md` merely because the agent believes it was successful.

## Lifecycle

```text
Execution traces
      |
      v
Skill Miner
  read-only analysis
      |
      v
Proposal
  redacted + evidence-linked
      |
      v
Workshop / Quarantine
      |
      +--> deterministic validation
      +--> security scan
      +--> semantic deduplication
      +--> trigger/non-trigger evals
      +--> sandboxed live task evals
      |
      v
Promotion decision
      |
      +--> reject
      +--> revise
      +--> keep in workshop
      +--> promote to generated/trusted
      |
      v
Usage monitoring
      |
      v
Curator
  improve / merge / archive AI-owned skills
```

## 1. Observe execution without storing raw everything

Self-improvement should operate on structured execution metadata rather than blindly saving complete private conversations forever.

Recommended trace fields:

```text
trace_id
workspace_class or opaque workspace id
skill versions invoked
tool calls and effect classes
result status
verification outcomes
user correction/frustration signals
retries/failure recoveries
artifacts produced
duration/cost if available
model/runtime versions
redacted task summary
```

Private content should be minimized and, where possible, represented by hashes or redacted summaries.

The skill miner should not need secret values or raw credential-bearing tool payloads.

## 2. What is skill-worthy?

A workflow is a good skill candidate when one or more of these repeat:

### Repeated successful sequence

The agent repeatedly performs substantially the same operational pattern and the sequence is non-trivial.

Example:

- inspect repository
- map dependency graph
- locate migration boundary
- patch three related files
- run targeted tests
- run schema validation
- produce migration notes

### Repeated failure shield

The same failure recurs and a proven recovery/verification pattern repeatedly fixes it.

This is often more valuable than a happy-path workflow.

### Repeated contract

The user or system repeatedly needs the same structured output or verification standard.

### Repeated expensive discovery

The agent repeatedly has to rediscover non-obvious operational facts that are stable enough to encode procedurally.

### Repeated frustration

LifeOS's current SuggestSkills design highlights a useful signal: a topic may appear to be "covered" while the user repeatedly hits the same failure class inside it. Frustration and repeated corrections should be weighted above raw topic frequency.

## 3. What is NOT skill-worthy?

Do not create skills for:

- one-off facts
- transient project state
- user personality preferences
- a single URL or credential
- generic advice a strong model already knows
- behavior steering that belongs in core/user preferences
- a workflow whose only content is "call tool X"
- tasks already genuinely covered by an existing skill
- project-specific private facts that should live in the workspace truth layer

A skill should represent reusable procedural leverage.

## 4. `skill-miner` must be read-only

This separation is important enough to enforce at the runtime level.

`skill-miner` may:

- inspect eligible trace metadata
- cluster repeated patterns
- inspect existing skill bodies for real coverage
- calculate recurrence/value/frustration signals
- propose candidate skills

It may not:

- create trusted skill files
- edit existing trusted skills
- modify policy
- grant tool permissions

Output example:

```yaml
proposal_id: sp_2026_09_001
candidate_name: migration-verifier
evidence:
  qualifying_traces: 7
  verified_successes: 6
  repeated_failures: 3
  user_corrections: 2
coverage_check:
  nearest_existing_skills:
    - database-migration-guardian
  gap: "Current skill validates schema migration but does not own cross-service compatibility verification."
confidence: medium
recommended_action: extend-existing-skill
```

This follows the strong permission-boundary idea in LifeOS SuggestSkills: discovery proposes, creation mutates.

## 5. Workshop proposal package

When a proposal is accepted for development, `skill-forge` creates a candidate inside Workshop/quarantine.

Suggested local structure:

```text
workshop/proposals/<proposal-id>/
├── proposal.yaml
├── candidate/
│   ├── SKILL.md
│   ├── aiverse.skill.yaml
│   ├── references/
│   ├── scripts/
│   └── evals/
├── evidence/
│   ├── trace-hashes.json
│   └── redacted-patterns.md
└── reports/
    ├── static-validation.json
    ├── security.json
    ├── dedup.json
    └── live-eval.json
```

Workshop state does not need to be committed to the public repository.

## 6. Candidate authoring

`skill-forge` should create the smallest reusable package that captures the leverage.

It should ask:

1. Is this a new skill or an extension to an existing one?
2. What is the invariant success contract?
3. What part is model judgment?
4. What part should become deterministic code?
5. What toolpacks are actually required?
6. What are the side effects?
7. What should be impossible outside the active workspace?
8. What real failure cases need regression tests?

The forge should avoid copying entire previous conversations into a skill.

## 7. Admission gate: Tier 1 deterministic validation

Before any semantic or live testing:

### Schema

- valid `SKILL.md` frontmatter
- valid AI-Verse manifest
- valid names/version
- no broken required references
- scripts have valid declared dependencies

### Privacy

- no credentials
- no private keys
- no tokens
- no personal absolute paths
- no client/customer data unless candidate is explicitly private and policy allows it
- no accidental environment dumps

### Security

- prompt injection patterns
- unicode/invisible instruction smuggling
- suspicious shell/download/exec chains
- environment variable harvesting
- data exfiltration paths
- dependency confusion/typosquatting signals
- unsafe archives/symlinks
- excessive tool requirements
- MCP/tool poisoning indicators if applicable

### Code quality

- scripts parse/compile
- lint or equivalent
- deterministic tests pass
- no host-global writes in tests

### Licensing/provenance

- source recorded
- license compatibility checked for copied/reused material

NVIDIA SkillSpector and SkillEvaluator are direct implementation references for this stage.

## 8. Admission gate: Tier 2 semantic analysis

The candidate then undergoes semantic checks.

### Cross-skill duplication

Does an existing skill already solve this problem?

Do not compare only names/descriptions. Read candidate and nearest skill bodies.

Possible decisions:

- new capability
- extend existing skill
- merge with existing generated skill
- reject as redundant

### Intra-skill redundancy

Does `SKILL.md` repeat itself, contain unnecessary model choreography, or duplicate references?

### Permission minimization

Could the same skill work with fewer toolpacks/effects?

### Portability

Has environment-specific logic leaked into portable instructions?

### Trigger quality

Does the description over-trigger or under-trigger?

## 9. Admission gate: Tier 3 live evaluation

Run the candidate in an isolated disposable workspace.

Never live-test a new generated skill directly against the user's production workspace merely to see what happens.

### Required eval classes

- positive activation cases
- negative activation cases
- representative normal tasks
- blocked/missing-permission tasks
- adversarial prompt-injection tasks
- path traversal attempts
- corrupted/malformed input
- real regression traces when safely reproducible

### Compare against baseline

For improvements to an existing skill, test:

- old version
- candidate version

A candidate should show actual improvement rather than merely different prose.

### Evaluate outcomes, not wording

Do not grade whether the model says the phrase "I verified the fix." Grade whether the verification actually happened and passed.

## 10. Promotion

A proposal becomes trusted only after policy says it can.

Recommended initial policy:

- human approval for all new skills
- human approval for material permission/effect expansion
- optional automated patch/minor promotion for AI-owned skills only after the evaluator is mature
- never auto-promote a candidate that failed or skipped required security stages

Promotion should be one auditable operation that records:

```text
proposal id
skill name/version
content hash
parent version if any
source trace hashes
security result
dedup result
live eval result
approver/policy
promotion timestamp
```

Git provides an additional rollback layer but should not be the only provenance record.

## 11. Ownership classes

Every skill should have a policy ownership class in registry metadata.

Suggested values:

### `core`

Foundational AI-Verse-maintained capability. Autonomous curator cannot edit.

### `human`

Human-authored/customized. Autonomous curator cannot edit unless explicitly adopted.

### `vendor`

Installed from an external trusted source. Curator can flag stale/conflicting behavior but cannot rewrite.

### `installed`

Third-party package. Curator can recommend upgrade/removal but not rewrite source silently.

### `generated`

AI-Verse generated and explicitly eligible for autonomous maintenance under policy.

This mirrors Hermes's useful distinction: the field controlling autonomous mutation is a policy boundary, not merely a historical authorship claim.

## 12. Curator

The curator is a maintenance agent for AI-owned/generated skills.

It should run at a lower cadence than ordinary execution and use cheap deterministic signals before model judgment.

Responsibilities:

- identify stale unused generated skills
- detect overlapping generated skills
- detect repeated corrections after skill execution
- suggest or apply narrow improvements when policy allows
- merge duplicates
- archive obsolete generated skills
- keep eval/corrections corpus current

It should not:

- auto-delete permanently
- rewrite core/human/vendor skills
- expand permissions because a skill keeps failing
- silently weaken verification
- remove regression tests to make scores improve

## 13. Archive, do not erase

Hermes currently favors recoverable archive over autonomous deletion. AI-Verse should do the same.

Suggested:

```text
workshop/archive/<skill-name>/<version>/
```

or a git-backed archive registry.

Archive should retain:

- content hash
- reason
- previous usage metrics
- replacement skill if any
- promotion lineage

## 14. Corrections log

Each actively maintained generated skill should accumulate a lightweight corrections record.

Example:

```yaml
- date: 2026-09-09
  failure: "Over-triggered on requests to only explain a stack trace."
  trace_hash: "..."
  correction: "Added negative routing case and activation eval."
  regression_eval: "evals/routing-007.yaml"
```

Real corrections are high-value training/evaluation material.

## 15. Skill telemetry

Track enough to improve routing and quality without turning the system into surveillance.

Useful aggregate metrics:

- activation count
- explicit vs automatic activation
- task success rate
- verification pass rate
- approval-denial rate
- user correction rate
- abort rate
- average retries
- dominant failure categories
- last used
- version-specific regressions

Do not optimize solely for activation count. A skill that activates less often but precisely can be healthier.

## 16. When the agent should offer to save a workflow

Hermes currently supports the useful interaction where, after solving a complex problem, the agent can offer to save the approach as a skill.

AI-Verse can support that, but the action should create a proposal, not direct production capability.

Good offer threshold:

- task was non-trivial
- workflow appears reusable
- outcome was verified
- no existing skill already covers it
- the reusable portion can be separated from private project state

## 17. Learning from source material

Hermes `/learn` shows a strong model for turning docs, code, URLs, or a prior workflow into an on-demand skill.

AI-Verse should support two distinct outputs:

### Procedural skill

Use when source material describes how to reliably perform an operation.

### Knowledge/reference package

Use when the material is primarily domain knowledge. Keep the main `SKILL.md` lean and place distilled topic references under `references/`.

Do not compress a large source into one lossy giant prompt.

## 18. External skill installation

External skills should enter the same trust pipeline as generated skills, with source provenance added.

Recommended install process:

```text
fetch/stage
-> pin source commit/hash
-> enumerate exact bundle files
-> reject unsafe symlink escapes
-> static/security scan
-> semantic capability/permission review
-> optional live eval
-> install disabled or approval-required
-> enable after policy approval
```

A public registry listing is discovery, not trust.

## 19. Self-improvement and workspace isolation

Self-improvement must never use a project workspace as an excuse to mutate the global Skills repository directly.

A project execution can emit a reusable-work proposal with redacted evidence.

The global skill forge operates in its own trusted Workshop scope.

This avoids:

- project prompt injection writing global skills
- client/private data leaking into public skills
- one compromised repository persisting malicious instructions globally

## 20. Recommended initial automation policy

For the first production version:

### Automatically allowed

- collect redacted skill-worthiness signals
- generate read-only skill proposals
- run deterministic validation
- run static security scanning
- run semantic dedup analysis
- run isolated live evals
- archive already-generated skills when policy threshold is met, provided archive is reversible

### Human approval required

- promote a brand-new skill
- modify a core/human/vendor skill
- expand required effect classes
- add shell/network/deployment authority
- add new external dependencies with executable install steps
- publish a skill publicly

### Never automatically allowed

- copy raw secrets into skills
- copy raw private workspace content into a public skill
- rewrite core OS policy
- weaken workspace isolation
- remove safety evals merely to pass promotion

## Final model

Self-improvement should make AI-Verse more competent while leaving a clear chain of evidence for why a capability exists, what proved it works, what it can access, who allowed it, and how to undo it.

That is the difference between a self-improving capability system and an agent that simply edits its own prompt files.