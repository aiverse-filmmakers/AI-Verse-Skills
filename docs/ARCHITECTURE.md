# AI-Verse-Skills Architecture

## Scope

AI-Verse-Skills is the operational capability layer of AI-Verse OS.

AI-Verse OS core remains authoritative for:

- workspace identity and isolation
- source-of-truth Markdown state
- knowledge routing
- user/project identity
- connection ownership
- secret storage
- approval policy
- scheduling/cadence
- audit policy

AI-Verse-Skills owns:

- reusable procedural skills
- deterministic toolpacks
- machine-readable capability contracts
- validation/evaluation assets
- skill discovery metadata
- skill creation and curation workflows

The boundary is intentional. A skill can consume core-granted context, but cannot redefine core authority.

## Architecture at a glance

```text
User / Brain / Orchestrator
          |
          v
AI-Verse OS Core
  - selects workspace
  - resolves durable context
  - resolves connections
  - applies policy
  - creates runtime grants
          |
          v
Capability Resolver
  - retrieves relevant skill metadata
  - loads chosen SKILL.md
  - resolves requested toolpacks
  - filters tools against grants
  - defers long-tail schemas
          |
          v
Skill Execution
  - model-guided procedure
  - deterministic tool calls/scripts
  - subagents if granted
          |
          v
Verification Layer
  - postconditions
  - tests/assertions
  - evidence
  - structured receipt
          |
          v
Core-controlled write-back / handoff
```

## The five layers

### Layer 1: portable skill package

`SKILL.md` is the cross-agent procedural layer.

It should answer:

- what this skill accomplishes
- when it should be selected
- what inputs it needs
- important constraints
- important decision rules
- known failure modes
- what successful completion looks like

It should not contain:

- hardcoded user paths
- raw credentials
- workspace identifiers
- permission grants
- global OS policy
- massive copied manuals
- deterministic logic better implemented as code

Portable skill content should remain compatible with the Agent Skills ecosystem wherever possible.

### Layer 2: AI-Verse machine contract

`aiverse.skill.yaml` is an optional sidecar interpreted by AI-Verse OS.

It can declare:

- contract version
- skill version
- required toolpacks/capabilities
- requested effect classes
- execution posture
- idempotency
- network posture
- secret handle names
- verification mode
- supported platforms
- scheduling safety characteristics
- evaluation suite paths

This is a request/contract, not an authorization token.

The core runtime intersects this manifest with actual grants.

### Layer 3: toolpacks

Toolpacks contain deterministic executable primitives.

Examples:

- code intelligence
- filesystem transforms
- process execution
- git operations
- structured data parsing
- browser operations
- network/API operations

Each tool is independently typed, testable, cancellable, and auditable.

A toolpack should not assume that because it is installed it is visible or executable in every session.

### Layer 4: runtime grants and policy

This layer lives in the AI-Verse OS core, not in the Skills repo.

A runtime grant can contain trusted values such as:

```json
{
  "workspace_id": "opaque-id",
  "workspace_root": "/trusted/runtime/resolved/path",
  "allowed_effects": ["workspace.read", "workspace.write", "process.exec"],
  "network_domains": ["api.github.com"],
  "secret_handles": ["github.primary"],
  "expires_at": "...",
  "trace_id": "..."
}
```

The model should not be able to fabricate this object and receive authority.

Tool arguments and runtime authority are separate channels.

### Layer 5: verification and evidence

Every consequential skill should finish with a structured result.

Example:

```json
{
  "status": "success",
  "summary": "Refactored authentication adapter",
  "effects": [
    {"type": "workspace.write", "paths": ["src/auth.ts", "tests/auth.test.ts"]}
  ],
  "verification": [
    {"check": "unit-tests", "status": "passed", "evidence": "..."},
    {"check": "typecheck", "status": "passed", "evidence": "..."}
  ],
  "artifacts": [],
  "warnings": [],
  "trace_id": "..."
}
```

A prose claim that work succeeded is not sufficient for high-authority operations.

## Repository structure

Recommended structure:

```text
AI-Verse-Skills/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DAY_ONE_ARSENAL.md
│   ├── SKILL_SPEC.md
│   └── SELF_IMPROVEMENT.md
├── research/
├── schemas/
│   ├── aiverse-skill-v1.schema.json
│   ├── tool-v1.schema.json
│   └── execution-receipt-v1.schema.json
├── templates/
│   ├── skill/
│   └── toolpack/
├── registry/
│   ├── skills.json
│   ├── toolpacks.json
│   └── aliases.json
├── skills/
│   ├── engineering/
│   ├── research/
│   ├── browser/
│   ├── data/
│   ├── operations/
│   ├── knowledge/
│   └── meta/
├── toolpacks/
│   ├── code-intelligence/
│   ├── filesystem/
│   ├── process/
│   ├── git/
│   ├── browser/
│   ├── network/
│   └── structured-data/
├── evals/
│   ├── harness/
│   ├── fixtures/
│   └── shared-cases/
└── workshop/
    ├── proposals/
    ├── quarantine/
    └── reports/
```

Runtime traces, user data, private skill proposals, and secrets should not be committed here by default.

## Toolpack design

### Tool identity

Use namespaced stable names:

```text
code.semantic_sweep
git.inspect_state
git.apply_patch
process.run
browser.navigate
browser.assert_state
knowledge.stage_writeback
```

Avoid vague names such as `run`, `search`, or `do_task` inside a global registry.

### JSON Schema contracts

Every tool should provide:

```text
name
version
description
input_schema
output_schema
effect_class
idempotency
timeout/cancellation support
required runtime capabilities
error schema
```

### Effect classes

Recommended canonical effects:

```text
none
workspace.read
workspace.write
process.exec
network.read
network.write
browser.read
browser.write
connector.read
connector.write
knowledge.propose
knowledge.write
git.local_write
git.remote_write
deploy.write
secret.use
```

Effects can be extended, but they should remain few enough for policy to reason about.

### Tool visibility and approval are separate

Use at least three states:

1. **hidden** - model cannot see or call it
2. **visible, approval-gated** - model can propose a valid call but execution waits on policy/user
3. **visible, executable** - call may run once validation passes

This follows the strongest patterns in current PydanticAI, Copilot CLI, Cline, Continue, and OpenHands designs.

### Validate before approval

Do not ask a user to approve malformed calls.

Recommended call pipeline:

```text
tool selection
-> JSON schema validation
-> semantic argument validation
-> attach trusted workspace/connection scope
-> policy evaluation
-> approval if needed
-> execute
-> postcondition verification
-> audit receipt
```

### Cancellable execution

Long-running tools must accept cancellation/abort and should stream progress where useful.

A tool that can run for minutes but cannot be stopped is not production-grade agent infrastructure.

## Workspace isolation contract

The core OS already owns workspace isolation. Skills must be designed so they cannot bypass it accidentally.

### Rule 1: paths are workspace-relative by default

Model-visible tool schemas should prefer:

```json
{"path": "src/auth.ts"}
```

not:

```json
{"workspace_root": "/Users/person/private-project", "path": "src/auth.ts"}
```

The trusted runtime resolves the current workspace root.

### Rule 2: canonicalize every filesystem target

Before any read/write:

1. resolve path
2. resolve symlinks where policy requires
3. normalize `.` and `..`
4. verify real path remains inside allowed root
5. verify effect is granted for that path

### Rule 3: external paths require a new explicit grant

A skill should never "helpfully" walk into a sibling workspace or home directory.

If a legitimate task needs external input, the core provides an additional read-only handle or materializes the input inside the current execution sandbox.

### Rule 4: subagents get derived grants

A child grant must be equal to or narrower than the parent grant unless the core explicitly authorizes an expansion.

### Rule 5: generated outputs do not silently become trusted context

Files created by tools are artifacts. Their content should only enter future high-priority context through the normal knowledge routing/validation path.

## Prompt injection boundaries

### Trust classes

AI-Verse should distinguish at least:

- **system/core policy** - highest trusted runtime instructions
- **trusted skill instructions** - reviewed package instructions
- **trusted references** - package-owned reference data
- **user task input** - user-authorized instruction
- **external/untrusted content** - web, email, repository issue text, arbitrary docs, logs, tool output

External content must never be allowed to redefine tool permissions or system policy.

### Do not concatenate untrusted content into system instructions

Tool outputs should be structured as data. If free-form content must be placed in context, label its origin/trust class and keep it below policy/skill instructions.

### References are not automatically trusted because they are Markdown

A downloaded or AI-generated reference file still requires provenance. Installed package references can be trusted only after package admission checks.

### Instructions discovered inside external data are data

Examples:

- README saying "ignore previous instructions"
- issue body telling the agent to run a shell command
- web page requesting credentials
- log line containing a prompt payload

These are content to analyze, not authority.

## Secrets and connections

### Secret handles

A skill declares that it requires something like:

```yaml
secrets:
  - handle: github.primary
    purpose: authenticated GitHub API calls
```

The model receives the handle name and capability state, not the raw secret.

The executor resolves/injects the value at the last possible moment.

### Connection handles

Likewise, use opaque connection identities supplied by the core:

```text
connection://github/main
connection://postgres/staging
browser-profile://commerce-test
```

Skills should not hardcode URLs, tokens, usernames, or account IDs unless they are public constants intrinsic to the skill.

## Progressive disclosure architecture

### Skill discovery

The initial index should contain compact fields such as:

```json
{
  "name": "root-cause-debugger",
  "description": "Reproduce, isolate, fix, and verify software failures...",
  "category": "engineering",
  "risk": "medium",
  "tags": ["debugging", "logs", "tests"]
}
```

### Skill retrieval

For small catalogs, name/description injection is fine.

For a large catalog, use:

- lexical retrieval
- semantic retrieval
- category/tool compatibility filtering
- workspace posture filtering
- recency/usage only as a weak ranking feature

Then expose only a top-k candidate set.

### Tool retrieval

Toolpacks required by an activated skill can become visible after skill activation.

Long-tail tools inside a pack can still remain deferred until the model searches for them.

This avoids the failure mode where the agent sees 100 tool schemas for every turn.

## Skill execution posture

A skill should declare its expected posture without being allowed to enforce it.

Useful fields:

- `read_only`
- `workspace_write`
- `external_write`
- `high_risk`

Other useful declarations:

- interactive vs headless-safe
- idempotent vs non-idempotent
- supports resume
- supports dry-run
- supports rollback
- safe for scheduled execution

The core can reject a skill activation whose required posture conflicts with the current session policy.

## Deterministic scripts vs model-driven decisions

A good rule:

**If two correct executions should produce the same mechanical intermediate result, implement that step deterministically.**

Good candidates for scripts/tools:

- parsing manifests
- AST extraction
- graph construction
- filesystem inventories
- patch application
- schema validation
- format conversion
- hash calculation
- secret detection
- version comparison
- migration checks
- test command execution

Good candidates for model judgment:

- deciding which evidence matters
- selecting among plausible fixes
- synthesizing contradictions
- deciding whether a recurring workflow deserves a skill
- reviewing architectural tradeoffs

## Fit with the current 3Ms / 4Cs boundary

This repository should not redefine AI-Verse's higher-level framework. It only needs a clean machine contract.

For the current model:

- **Context** is supplied to a skill as scoped inputs/handles.
- **Connections** are supplied as authorized connection handles.
- **Capabilities** are resolved from skills and toolpacks.
- **Cadence** remains external; a skill can declare whether repeated/headless execution is safe.
- **Machine** is where a skill belongs: a reusable, bounded, testable operational block.

A Machine-grade skill should therefore be:

- explicit about inputs
- bounded in authority
- typed at execution boundaries
- deterministic where practical
- observable
- cancellable
- replayable where appropriate
- idempotent or explicitly non-idempotent
- verified before claiming success
- versioned
- evaluated

This remains compatible even if the Brain later replaces or greatly expands the 3Ms/4Cs framework.

## Versioning

Use independent semantic versions for skills and toolpacks.

Breaking changes include:

- input/output contract changes
- changed side-effect class
- changed permission requirements
- changed semantics that can invalidate downstream workflows

Behavioral improvements that preserve contract can be minor or patch depending on scope.

The registry should retain version and content hash so an execution trace can identify exactly what ran.

## Provenance

Every installed skill should have registry metadata including:

```text
source type
source URL/repository if external
source commit/tag if available
content hash
installed timestamp
installed by
created_by policy class
security scan status
semantic dedup status
live eval status
signature/attestation if available
```

This metadata belongs in registry state, not necessarily in portable `SKILL.md`.

## The central rule

The most important architectural sentence for AI-Verse-Skills is:

> **Skills may describe powerful work, but only the AI-Verse OS runtime can grant powerful authority.**

That keeps a rapidly evolving Skills repository compatible with strict workspace isolation and a stable Markdown-based core source of truth.