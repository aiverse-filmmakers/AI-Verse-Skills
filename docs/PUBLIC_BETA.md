# AI-Verse Skills Public-Beta Contract

**Status:** Skills-owned public-beta implementation contract  
**Version:** 1.1.0-beta.1

## Ownership

Skills owns:

- immutable Skill package generations;
- provider metadata;
- package admission and Skill-specific trust/provenance;
- reusable learned procedure proposals;
- candidate package bytes;
- evaluation and promotion state;
- learned Skill usage and curator state;
- archive/restore and Skill-generation rollback evidence.

Skills does not own:

- goal strategy or completion;
- general Memory;
- schedules/triggers;
- host workspace permissions;
- connection credentials;
- final external-action authorization.

## Public lifecycle

```text
install
-> setup
-> status / doctor
-> enable / disable
-> update / rollback
-> uninstall
-> explicit purge only
```

All public lifecycle surfaces provide structured output where orchestration needs it. `status --json`, `doctor --json`, `setup --json`, `install --json`, `update --json`, `rollback --json`, `uninstall --json`, `readiness --json` and `descriptor --json` are stable public-beta surfaces.

Setup verifies the current immutable generation and provider/admission metadata. Default-root OS discovery is dynamic. Custom roots are reported as requiring explicit host/provider configuration.

## Admission law

The following are separate facts:

```text
integrity
admission
trust
readiness
authorization
```

Integrity never implies trust. Trust never implies readiness. Readiness never implies authorization.

Skills never writes `authorized=true` as a consequence of install, admission, setup or learning.

## Self-learning lifecycle

The canonical public-beta lifecycle is:

```text
evidence/candidate envelope
-> candidate
-> proposal
-> evaluating
-> pending_approval | auto_eligible
-> applied
   OR rejected
   OR quarantined
```

Applied package changes create a new immutable generation. The previous generation remains a rollback target subject to explicit retention policy.

### Modes

`propose` is the default.

- `off`: automatic reviews are disabled. Explicit user `/learn` or equivalent remains allowed.
- `propose`: eligible evidence may create proposals, but production promotion requires approval.
- `auto`: only low-risk maintenance of eligible learned/local Skills may auto-promote after every mandatory gate.

Mode is not permission.

### Protected ownership

These are protected from autonomous rewriting:

```text
first_party
curated_upstream
user_authored
external
```

These may be eligible for governed maintenance when policy allows:

```text
agent_learned
workspace_local
```

A correction to a protected/upstream Skill may produce evidence and a proposal, but public beta does not overwrite that Skill. The safe route is an upstream update or a separately owned derived learned Skill.

### Foreground correction

For an actually used Skill that fails:

1. Gateway preserves bounded failure evidence.
2. Brain classifies the finding as a reusable Skills candidate when appropriate.
3. Skills binds the repair proposal to the exact active `generation_id` and package digest.
4. Skills scans and evaluates the candidate.
5. If the target generation/digest changed, apply fails closed and requires re-evaluation.
6. Promotion follows approval/auto policy.
7. Retry belongs to Gateway/host policy, not Skills.

### Background review

Gateway or Automations may trigger a detached review. Skills enforces:

- learning mode;
- max pending proposals;
- max proposal bytes;
- max background reviews per day;
- no raw transcript/credential fields in the candidate envelope;
- immutable proposal/audit state.

A timer or wake can trigger review. It never authorizes mutation by itself.

### Explicit learning

Equivalent surface:

```bash
aiverse-skills learn --envelope candidate.json --candidate-dir ./candidate
```

The envelope may include:

```json
{
  "candidate_id": "learn_...",
  "scope": {},
  "suggested_owner": "skills",
  "kind": "create",
  "skill_id": "example-procedure",
  "target_skill_id": null,
  "summary": "Reusable procedure",
  "evidence_refs": ["memory:..."],
  "success_signal": [],
  "failure_signal": [],
  "risk": "low",
  "confidence": 0.9,
  "requested_capabilities": [],
  "requested_dependencies": []
}
```

Evidence references are preferred over copied transcripts.

### Evaluation

Before promotion, Skills checks as applicable:

- candidate package structure;
- static secret/safety scan;
- symlink containment;
- requested capability/dependency expansion;
- source ownership/protection;
- exact target generation/digest binding;
- semantic duplicate/overlap signal;
- provenance completeness;
- approval or bounded auto eligibility.

Executable/dependency/permission-expanding changes are not auto-promoted.

### Promotion and backup

Before mutation, the current immutable generation is recorded as the backup generation. Promotion builds a complete new stage, regenerates provider and admission metadata, verifies it, commits it as a new immutable generation, then atomically activates it.

The audit ledger records promotion intent and result.

### Rollback

Proposal rollback is compare-and-set. It only rolls back automatically while that proposal's applied generation remains current. If newer work is active, Skills refuses to overwrite it.

General generation rollback remains available through `aiverse-skills rollback`.

### Usage and curator

Skills tracks Skill-specific lifecycle signals such as selection, success and failure timestamps/counts.

Curator can:

- mark learned Skills stale;
- propose reversible archive review;
- detect high-overlap learned Skills and create consolidation proposals;
- restore archived learned Skills.

Curator cannot permanently auto-delete a Skill.

### Retention and purge

Archive is reversible. Old immutable generations referenced by proposal rollback or archive provenance are protected from purge.

`purge` is an explicit destructive maintenance command and requires `--yes`. There is no autonomous hard purge in public beta.

### Privacy and cost controls

Public-beta controls include:

- evidence references instead of raw transcript persistence;
- rejection of raw credential/secret envelope fields;
- deterministic secret-like content scan;
- bounded proposal size;
- bounded pending proposals;
- bounded background reviews/day;
- no scheduler inside Skills.

Model/provider cost accounting can be attributed by Token when available, but Token is not required for Skills state correctness.

## Exact cross-component calls

### Brain -> Skills

Brain sends a learning candidate envelope to the Skills submission surface:

```text
learning submit
  candidate_id
  scope
  suggested_owner=skills
  kind=create|repair|update|consolidate|archive-review
  skill_id / target_skill_id
  summary
  evidence_refs[]
  success_signal[]
  failure_signal[]
  risk
  confidence
  requested_capabilities[]
  requested_dependencies[]
```

Brain does not send Skill bytes directly into the active generation and does not write Skills state.

### Memory -> Brain / Skills

Memory supplies bounded evidence references and recalled correction/success/failure evidence. Skills accepts references in `evidence_refs`. Memory never invokes promotion and never owns candidate package bytes.

### Gateway -> Skills

Gateway calls:

```text
learning submit        # foreground failure/correction or detached post-run candidate
learn                   # explicit user learning request
refine                  # explicit user refinement request
proposals evaluate      # when candidate bytes are available
proposals apply         # after explicit approval when required
usage record            # selected/success/failure lifecycle signal
```

Gateway must present approval when Skills returns `pending_approval`. Gateway may retry a task only under its own current execution budget and authorization.

### Automations -> Skills

Automations calls:

```text
curator run
learning submit --trigger automation
```

Automations provides only a wake/trigger. It does not mutate active Skill bytes, approve proposals, or own curator state.

### Skills -> Brain / Gateway

Skills returns inspectable projections:

```text
proposal_id
proposal state
evaluation result
approval requirement
active/applied generation_id
backup/rollback generation
usage/health projection
archive/restore result
```

No hidden chain-of-thought is required or stored by this contract.

## Runtime support

Only AI-Verse OS is currently a public-beta end-to-end execution claim. Other runtime adapters are explicit package exposure compatibility surfaces until maintained real invocation acceptance exists for each runtime.

## Future-only

Not required to call this Skills public-beta implementation complete:

- marketplace signing/reputation infrastructure;
- hosted multi-user policy service;
- automatic upstream pull-request authoring;
- richer semantic embeddings for deduplication;
- broad live invocation acceptance for every third-party runtime adapter;
- enterprise compliance scanners;
- automatic hard deletion;
- a scheduler inside Skills;
- general Memory or Brain behavior inside Skills.
