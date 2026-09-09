# Day-One Arsenal

**Target:** September 2026 state-of-the-art operational capability set for AI-Verse OS.

This list intentionally excludes generic chatbot utilities. These are reusable blocks of serious agentic work that should materially change what AI-Verse can accomplish inside a scoped workspace.

The recommended launch set is **20 skills: 18 operational skills plus 2 meta-skills for capability growth**.

## Priority model

- **P0:** foundational. A general local-first agent OS feels incomplete without it.
- **P1:** high-value operational depth. Ship on day one if the goal is a serious autonomous OS rather than a coding assistant.
- **META:** capability lifecycle. Required if the repository is expected to improve itself safely.

## P0: foundational operational skills

### 1. `semantic-codebase-sweep`

**Purpose:** Build a compact, query-aware structural map of a repository before substantial code work.

This should be much richer than grep or embedding search.

Core behavior:

- enumerate repository structure without reading generated/vendor noise unnecessarily
- parse symbols through tree-sitter/LSP where possible
- build imports/dependency graph
- build definitions/references/call relationships where available
- rank structurally important files and symbols using graph centrality plus query relevance
- map tests to production code
- identify config/build/deployment entry points
- identify recent high-churn areas from git when relevant
- return an architecture map with exact file/symbol references

**Inputs:** current workspace grant, task/query, optional scope filters.

**Outputs:** structured repo map, relevant symbol shortlist, dependency edges, uncertainty/gaps.

**Permission posture:** read-only.

**Verification:** every reported symbol/path resolves inside the granted workspace.

**Research lineage:** Aider repo map, Cline/OpenHands search surfaces, semantic code search patterns.

---

### 2. `root-cause-debugger`

**Purpose:** Move from symptom to reproducible cause and verified fix.

Core behavior:

- capture exact failure
- reproduce with the smallest reliable command/test
- gather logs/traces/config/runtime state
- generate competing hypotheses
- falsify hypotheses with targeted probes
- optionally use git history/bisect
- implement the narrowest justified fix
- re-run reproduction plus relevant regression checks
- produce a root-cause report with evidence

**Inputs:** symptom, logs/error, workspace grant.

**Outputs:** reproduction, root cause, patch if authorized, verification evidence, remaining risk.

**Permission posture:** read by default; workspace write and command execution as explicit capabilities.

**Verification:** the original reproduction must pass after the fix, not merely disappear from logs.

---

### 3. `transactional-refactor`

**Purpose:** Perform safe multi-file changes as a transaction rather than a sequence of unconstrained edits.

Core behavior:

- determine affected symbols/files before editing
- capture clean baseline
- produce change plan and invariants
- apply structured patches
- preserve style and public contracts unless change is intentional
- format/lint/typecheck/test
- report exact diff and affected interfaces
- rollback if verification fails and policy requires atomic behavior

**Outputs:** patchset, diff summary, verification report, rollback state.

**Permission posture:** workspace write; destructive operations separately gated.

**Verification:** configured quality gates plus task-specific invariants.

---

### 4. `verification-harness`

**Purpose:** Give every other skill a standard way to prove that work succeeded.

This is arguably the most important reusable skill after codebase understanding.

Core behavior:

- detect project-native test/build/lint/typecheck commands
- select targeted checks based on changed surface
- run fast checks before expensive broad checks
- collect exit codes and machine-readable outputs
- distinguish environment failure from product failure
- retry only when a retry is justified
- emit a verification receipt

Should support more than code over time: files, data transforms, browser outcomes, generated artifacts, deployments.

**Outputs:** pass/fail/blocked status, checks executed, evidence, uncovered risk.

**Permission posture:** command execution in current workspace, network denied unless required by the project and granted.

---

### 5. `deep-research-synthesis`

**Purpose:** Turn external research into a defensible evidence package rather than a pile of search results.

This is not generic web search. Search/extract tools are only primitives underneath it.

Core behavior:

- decompose a research question into evidence requirements
- prioritize primary and authoritative sources
- broaden sources when the topic is contested or uncertain
- distinguish publication date from event date
- maintain a claim-to-source ledger
- identify contradictions and unresolved uncertainty
- avoid duplicate-source amplification
- synthesize findings with source-level provenance
- optionally package durable findings for knowledge write-back

**Outputs:** findings, claim ledger, contradiction table, confidence notes, sources.

**Permission posture:** external read/network only unless write-back is separately granted.

**Verification:** every material factual claim is traceable to evidence.

---

### 6. `browser-workflow-operator`

**Purpose:** Execute multi-step browser work reliably with scope, secrets, and completion proof.

Core behavior:

- operate inside an isolated/pinned browser profile
- restrict navigation to approved domains when possible
- use DOM/accessibility state before vision-only guessing
- use credential placeholders/secret handles, never raw secrets in model context
- survive redirects/popups/dialogs/iframes
- checkpoint irreversible steps
- collect proof of final state
- detect whether an action was actually completed rather than merely clicked

**Outputs:** completed/blocked status, receipts/IDs, final URL/state, optional screenshots.

**Permission posture:** domain-scoped network + browser; consequential submissions can require approval.

**Verification:** postcondition assertion after every consequential action.

**Research lineage:** Browser Use, OpenClaw browser isolation patterns, Copilot URL permissions.

---

### 7. `api-integration-engineer`

**Purpose:** Safely understand and integrate an API from documentation, OpenAPI, code, SDKs, or captured traffic.

Core behavior:

- discover canonical API contract
- map authentication without exposing credentials
- derive typed request/response models
- handle pagination, retries, rate limits, idempotency, and error semantics
- generate minimal integration code or adapter
- create contract tests/fixtures
- reverse-engineer HAR/network behavior when documentation is incomplete and authorization permits
- document unsupported assumptions

**Outputs:** integration plan/code, schemas, test evidence, operational notes.

**Permission posture:** docs/network read first; external write calls require explicit connection grants and policy.

---

### 8. `git-change-lifecycle`

**Purpose:** Own the safe lifecycle of a repository change without conflating local edits with remote publication.

Core behavior:

- inspect repository status and branch topology
- isolate a task branch/worktree when appropriate
- stage coherent changes
- produce conventional, evidence-based commits
- rebase/cherry-pick safely when requested
- resolve conflicts with verification
- prepare PR description and change summary
- optionally create/update PR through a granted connector
- generate release notes when appropriate

**Critical separation:** commit, push, PR creation, merge, and destructive history rewrite are different effect classes.

**Verification:** clean expected working tree, intended diff only, tests linked to change.

---

### 9. `dependency-supply-chain-audit`

**Purpose:** Understand and safely change software dependencies rather than blindly upgrading packages.

Core behavior:

- inspect manifests and lockfiles
- identify direct/transitive dependencies
- find vulnerable/outdated/unmaintained packages
- inspect licenses and provenance where relevant
- generate SBOM when useful
- rank upgrades by risk/value
- test upgrades incrementally
- detect suspicious package substitutions or install scripts
- preserve lockfile determinism

**Outputs:** dependency graph, risk report, recommended patchset, verification.

**Permission posture:** read-only audit by default; package installs/network and writes separately granted.

---

### 10. `environment-doctor`

**Purpose:** Diagnose and repair a workspace's execution environment without polluting the host.

Core behavior:

- detect project language/runtime/package manager versions
- inspect lockfiles and local environment declarations
- detect missing binaries, version mismatches, broken virtualenvs, path problems, ports, services
- prefer project-local installs and reproducible setup
- never silently make global machine changes
- emit exact environment delta

**Outputs:** diagnosis, minimal repair plan, repaired local environment if authorized, verification command.

**Permission posture:** workspace/process read first; installs/writes gated; host-global writes denied by default.

## P1: high-value operational depth

### 11. `database-migration-guardian`

**Purpose:** Design and validate data/schema changes with rollback and production safety in mind.

Core behavior:

- inspect current schema and migration chain
- model forward and backward compatibility
- detect table-lock/long-running/backfill risk
- generate migration and rollback plan
- handle expand/migrate/contract patterns where necessary
- test against disposable database/fixture
- verify data invariants before and after

**Permission posture:** local/test database by default; production write requires a separate high-risk grant.

---

### 12. `incident-forensics`

**Purpose:** Reconstruct what happened from logs, traces, process state, metrics, git changes, and artifacts.

Core behavior:

- preserve evidence before mutation
- normalize timestamps/timezones
- construct event timeline
- correlate service/process/release changes
- distinguish symptom from initiating event
- identify gaps in observability
- produce root-cause candidates with evidence strength

**Outputs:** timeline, evidence bundle, root-cause assessment, remediation candidates.

**Permission posture:** read-only unless remediation is explicitly requested.

---

### 13. `structured-ingestion-normalization`

**Purpose:** Convert heterogeneous source material into structured local-first data suitable for retrieval and durable Markdown knowledge.

Core behavior:

- ingest documents, PDFs, HTML exports, repositories, logs, structured files, archives
- preserve source boundaries and provenance
- normalize headings/entities/tables/metadata
- chunk by semantic structure rather than arbitrary token windows where possible
- create index/manifest
- flag extraction uncertainty instead of silently inventing missing text

**Outputs:** normalized Markdown/JSON plus manifest and provenance map.

**Permission posture:** read source, write only to granted workspace destination.

---

### 14. `knowledge-writeback`

**Purpose:** Safely convert completed work into a proposed update to AI-Verse OS's Markdown source of truth.

The Skills repo must not become a second memory database.

Core behavior:

- identify durable vs transient information
- locate the correct core-owned destination through the OS knowledge router
- compare against existing truth
- deduplicate and detect contradiction
- preserve provenance and timestamps where the core contract requires them
- create a staged patch/proposal
- validate structure and links
- commit only through the core's approved write interface

**Outputs:** structured write-back proposal, conflict notes, final write receipt if accepted.

**Permission posture:** cannot choose arbitrary cross-workspace destinations. Destination is provided as a core-issued handle.

---

### 15. `delegation-orchestrator`

**Purpose:** Use multiple agents as isolated workers without turning delegation into uncontrolled recursion.

Core behavior:

- split work only when parallelism or specialization adds value
- assign narrow task contracts
- give each child minimum required skills/tools
- isolated context by default
- explicit time/iteration/cost budgets
- prohibit recursive delegation by default
- require structured result/evidence
- reconcile conflicting child results
- parent remains responsible for final verification

**Outputs:** task graph, worker results, merged result, dissent/conflict record.

**Permission posture:** child capabilities are a subset of explicit grants, never an automatic clone of parent authority.

---

### 16. `release-deploy-guard`

**Purpose:** Turn deployment into a verified state transition rather than a command invocation.

Core behavior:

- identify target environment and release artifact
- run preflight checks
- verify configuration/secrets exist through handles without reading raw values
- build/package reproducibly
- produce deployment plan and rollback trigger
- require approval at irreversible boundary when policy says so
- monitor health after deployment
- rollback or stop on failed postconditions
- produce release receipt

**Permission posture:** deployment connection scoped to named environment; production is high risk.

---

### 17. `change-review`

**Purpose:** Review a proposed change as an adversarial second pass before promotion, commit, merge, or release.

Core behavior:

- understand intended behavior first
- inspect semantic diff, not just changed lines
- assess correctness, security, data loss, race/concurrency, compatibility, performance, operability, test coverage
- inspect related unchanged code when needed
- rank findings by severity and confidence
- distinguish actual defect from preference
- verify critical findings with a reproduction/probe when feasible

**Outputs:** structured findings, evidence, false-positive notes, merge/release recommendation.

**Permission posture:** read-only by default.

---

### 18. `configuration-contract-doctor`

**Purpose:** Make complex runtime/configuration dependencies explicit and reproducible without leaking secrets.

Core behavior:

- enumerate required environment/config keys from code and manifests
- distinguish secret vs non-secret values
- validate existence/type/format through secret/config APIs
- detect stale/dead config
- compare environment schemas without exposing secret values
- generate `.env.example` or typed config schema safely
- identify configuration drift

**Outputs:** config contract, missing/invalid fields, drift report, safe template.

**Permission posture:** secret metadata/handle checks only unless a dedicated secret-management capability is granted.

## META: safe capability growth

### 19. `skill-forge`

**Purpose:** Own the complete lifecycle of creating or changing an AI-Verse skill.

It should be the only normal mutating path for skill authoring.

Core behavior:

- scaffold portable `SKILL.md`
- create/update `aiverse.skill.yaml`
- attach deterministic scripts/references only when justified
- validate names/frontmatter/links/schema
- scan for secrets/PII/prompt injection/risky code
- create trigger and non-trigger evals
- run behavioral evals in isolated workspace
- compare with overlapping existing skills
- version and produce promotion report

**Outputs:** candidate package in Workshop/quarantine, scan report, eval report, proposed version.

**Permission posture:** writes to Workshop by default, not directly to trusted `skills/`.

---

### 20. `skill-miner`

**Purpose:** Discover skill-worthy repeated work from successful and frustrating execution history.

This should be read-only and proposal-only.

Core behavior:

- analyze execution traces/session summaries without ingesting raw secrets
- find repeated successful tool/workflow sequences
- find recurring failures with proven recoveries
- detect repeated output contracts and verification patterns
- weight recurrence, value, and frustration/severity
- deduplicate against the actual content/capability coverage of existing skills
- propose a ranked shortlist with trace hashes/evidence
- never create or edit a trusted skill itself

**Outputs:** skill proposals with recurrence, evidence, suggested scope, expected value.

**Permission posture:** read execution metadata; no trusted skill writes.

## Skills that should NOT be separate day-one skills

Several capabilities are important but should remain runtime primitives or subfeatures rather than becoming top-level skills.

### Basic file read/write/search

These are tools/toolpack primitives underneath higher-level skills.

### Generic shell execution

A primitive, not a reusable workflow.

### Generic web search

A primitive underneath deep research.

### Generic calculator/unit conversion/weather

Useful utilities, but irrelevant to the heavy operational layer this repository is for.

### Raw memory save/load

AI-Verse OS owns durable truth. Skills should use `knowledge-writeback` rather than inventing a parallel memory store.

### Scheduler/cron

Cadence is a core runtime concern. A skill may declare that it is safe/idempotent for scheduled execution, but should not own global scheduling semantics.

### Workspace switching or creation

Workspace authority belongs to AI-Verse OS. A skill receives a workspace grant; it does not choose a different workspace by path.

## Recommended build order

### Wave 1: make coding and research trustworthy

1. semantic-codebase-sweep
2. verification-harness
3. root-cause-debugger
4. transactional-refactor
5. deep-research-synthesis
6. git-change-lifecycle

### Wave 2: expand operational reach

7. browser-workflow-operator
8. api-integration-engineer
9. environment-doctor
10. dependency-supply-chain-audit
11. structured-ingestion-normalization
12. knowledge-writeback

### Wave 3: high-authority operations

13. database-migration-guardian
14. incident-forensics
15. delegation-orchestrator
16. change-review
17. configuration-contract-doctor
18. release-deploy-guard

### Wave 4: self-expansion

19. skill-forge
20. skill-miner

The meta-skills should ship only after the validation/evaluation pipeline they depend on is real. A system that can generate new skills before it can quarantine and evaluate them has the order backwards.