# Agent Capability Landscape, September 2026

**Research date:** 2026-09-09

**Purpose:** Determine what a standalone, local-first AI operating system skills repository should ship with on day one, and how those skills should be structured, isolated, validated, and allowed to improve over time.

This research deliberately focuses on heavy operational capabilities. Generic chatbot utilities such as weather, calculator, and basic web search are not considered a meaningful day-one differentiator.

## Executive findings

Across the strongest systems, six design patterns have converged.

### 1. Skills and tools are different layers

A tool is a typed executable primitive. A skill is reusable procedural intelligence that tells an agent when and how to combine primitives into a reliable outcome.

The most mature systems increasingly separate:

- tool schema and execution
- procedural skill instructions
- runtime permissions
- user/project context
- validation and evaluation

This separation is important for AI-Verse because workspace isolation already belongs to the core OS. A skill must consume a granted scope, never define or expand that scope itself.

### 2. Progressive disclosure is now table stakes

The dominant pattern is:

1. expose compact skill metadata
2. load the selected `SKILL.md`
3. load references/scripts/assets only as needed
4. expose large or rare tool schemas only after discovery

Hermes, OpenClaw, Gemini CLI, OpenCode, DeepAgents, Codex, Agent Skills, and PydanticAI all converge on variants of this idea.

A large static tool or skill prompt is now an anti-pattern. Tool selection quality drops as the visible toolset grows, and systems with hundreds of skills need retrieval rather than prompt stuffing.

### 3. A skill must not be able to grant itself authority

The strongest permission architectures treat a skill's requested tools as advisory. Runtime policy remains authoritative.

Useful distinctions seen in current systems:

- tool visible vs hidden
- tool callable vs disabled
- execution auto-approved vs approval required
- filesystem path in scope vs outside scope
- URL/domain allowed vs prohibited
- secret available as an execution handle vs visible to the model
- network enabled vs denied

This should be a first-class AI-Verse law: **skill is not permission**.

### 4. Reusable cognitive guidance belongs in Markdown; deterministic work belongs in code

LifeOS's current authoring doctrine is useful here: avoid brittle prose choreography when a capable model can choose the method, but keep safety gates, verified gotchas, exact tool contracts, and output contracts. Codex similarly recommends scripts when a task needs deterministic or repeatedly reliable execution.

For AI-Verse, a skill should describe intent, constraints, decision rules, failure modes, and verification. Repeated parsing, graph construction, transformations, linting, migrations, checks, and structured extraction should live in tested tool implementations or scripts.

### 5. Skill security now needs its own software supply-chain process

This is no longer theoretical. NVIDIA SkillSpector and SkillEvaluator now provide dedicated skill security and quality pipelines. OpenClaw and Hermes also stage or quarantine external skills and record provenance.

The strongest admission model is:

- schema/frontmatter validation
- static security scan
- secret/PII detection
- unicode and concealed-instruction checks
- dependency and license checks
- semantic duplication analysis
- sandboxed behavioral evaluation
- explicit promotion decision

Treat every externally sourced or AI-generated skill as untrusted until it passes that process.

### 6. Self-improvement works best as proposal, evaluation, promotion, curation

Hermes can author skills from successful work and has a curator that operates only on eligible agent-created skills. OpenClaw's Skill Workshop places reusable work into a proposal queue instead of writing directly into trusted skill files. LifeOS separates read-only skill-gap discovery from mutating skill creation. Letta separates memory, procedural skills, and deterministic harness changes.

The safe pattern is therefore not "agent rewrites its own capabilities whenever it wants." It is:

**observe -> propose -> redact -> deduplicate -> scan -> evaluate -> approve/promote -> monitor -> curate/archive**

## Benchmark matrix

| System / repository | Important current pattern | What AI-Verse should take | What not to copy blindly |
|---|---|---|---|
| NousResearch/hermes-agent | Named toolsets, coding posture, progressive skill disclosure, `/learn`, agent skill CRUD, Skills Hub, usage-aware curator | Toolset composition, conditional skill activation, skill learning, provenance, curator protections | Letting ordinary skills mutate unrestricted global state |
| danielmiessler/LifeOS | Canonical skill lifecycle, public/private boundary, customization overlays, deterministic tools inside skills, SuggestSkills vs CreateSkill split | Separate read-only skill mining from creation, validation-first authoring, keep personal context outside public skills | LifeOS-specific naming and broader operating philosophy |
| openclaw/openclaw | Agent Skills, layered roots, Workshop proposal queue, install policy, symlink containment, sandbox materialization | Proposal queue, external skill quarantine, realpath checks, per-agent isolation | Coupling AI-Verse to OpenClaw-specific metadata |
| agentskills.io specification | Small portable `SKILL.md` contract with optional scripts/references/assets | Use as interoperability baseline | Extending core spec with AI-Verse-only required fields |
| anthropics/skills | Portable skill directories, examples across technical workflows | Cross-client portability and folder conventions | Assuming one vendor's runtime permissions |
| OpenAI Codex skill creator | Lean instructions, scaffold + validate, deterministic scripts, independent behavioral testing | Skill forge workflow, usage-driven improvement, validation scripts | Putting runtime-specific UI metadata in portable core |
| openai/skills | Reusable operational skill packages | Compatibility target and examples | Copying domain selection without AI-Verse priorities |
| langchain-ai/deepagents | Skills middleware over backend abstraction, source layering, isolated/fork subagents, explicit filesystem permissions | Keep skill loading independent of storage backend, isolated delegation by default | Inheriting parent permissions too broadly |
| pydantic/pydantic-ai | Composable toolsets, filtered visibility, approval wrappers, deferred loading, ToolSearch, capabilities | Dynamic tool exposure and validated approval boundary | Exposing dozens of schemas eagerly |
| google-gemini/gemini-cli | Agent Skills tiers, activation consent, skill folder access added only after approval | Consent before expanding readable paths, interoperable `.agents/skills` | Injecting all discovery metadata forever at very large scale |
| GitHub Copilot CLI | Separate available tools from approval policy, path and URL permission layers, `allowed-tools` in skills | Visibility vs authorization split, scoped allow/deny semantics | Trusting skill-provided shell preapproval without external review |
| cline/cline | Per-tool enabled/autoApprove policy, typed tools, abort signals, streaming output, testable tool functions | Explicit tool policy model, cancellation, streaming, unit-testability | Auto-approve defaults for a local OS with broad authority |
| OpenHands/software-agent-sdk | File-based agents with explicit tools, skills, model, budget, max iterations, permission mode, hooks | Subagent budgets and strict registry resolution | Unlimited delegation or ambiguous inherited permissions |
| anomalyco/opencode | On-demand skill tool, multiple compatible skill roots | Portable discovery and explicit load | Dependence on a single client's directory convention |
| block/goose | Skills plus parameterized recipes, load/delegate primitives, self-test recipe, nested delegation prevention | Distinguish reusable skill knowledge from instantiated recipes; self-test capability | Recursive delegation without a deliberate policy |
| block/agent-skills | Cross-agent skill marketplace with focused reusable workflows | Marketplace compatibility and contribution quality rules | Trusting marketplace popularity as security proof |
| browser-use/browser-use | Persistent browser sessions, domain allowlists, sensitive-data placeholders, local/remote browser split | Credential handles, domain scope, browser evidence | Giving browser skills raw credentials |
| letta-ai/letta-code | Git-backed memory filesystem, skills as procedural memory, mods as trusted runtime behavior, background reflection | Strong boundary between procedural skill and deterministic harness policy | Letting skill text become an enforcement mechanism |
| Aider-AI/aider | Repository map using tree-sitter and graph relevance, disciplined edit formats, reflection around lint/test failures | Semantic codebase sweep and context-ranking architecture | Sending a whole repo map every turn regardless of need |
| crewAIInc/crewAI | Agents, tools, flows, memory/knowledge, guardrails | Workflow composition and role-specialized execution | Treating orchestration configuration as portable skill format |
| continuedev/continue | Tool allow/ask/exclude states, path patterns, hooks around many lifecycle events | Three-state permissions and deterministic hooks | Letting prompt rules replace hard policy |
| microsoft/agent-framework | Agent/chat/function middleware, mutable live tool list, workflow primitives | Progressive tool exposure through middleware | Tight coupling to one SDK's object model |
| agent0ai/agent-zero | Project/profile scoped memory and skills, configurable tool/MCP/skill policies | Scope-specific policies and skill selection | Mixing memory and executable capability boundaries |
| NVIDIA/SkillSpector | Purpose-built static/semantic security scanner for skills, dependency checks, prompt-injection and exfiltration detection | Mandatory admission scan for external/generated skills | Treating a clean scan as a sandbox substitute |
| NVIDIA/SkillEvaluator | Tier 1 deterministic validation, Tier 2 semantic dedup, Tier 3 sandboxed live evaluation | Adopt the three-stage quality model | Depending on live evaluation for basic deterministic checks |
| JPeetz/agent-skills | Cross-platform catalog, minimum eval cases, corrections logs, skill miner/foundry | Corrections log and failure-driven skill iteration | Trusting collection claims without independent validation |
| Roo Code | Large skill/config surfaces exposed context-management issues at scale | Negative lesson: search/retrieve long-tail skills | Loading hundreds of skill descriptions into every prompt |
| SWE-agent | Tool bundles and constrained coding environment | Purpose-built tool bundles for task posture | Treating a coding-only bundle as universal OS capability |

## Detailed anchor analysis

### Hermes Agent

Hermes currently exposes a broad typed runtime surface but groups it into named toolsets rather than presenting a single undifferentiated registry. Current groups include file, terminal, browser, skills, memory, session search, code execution, delegation, cron, and composite postures such as coding and debugging.

Important architecture lessons:

- Toolsets can include other toolsets.
- A coding posture can remove irrelevant high-risk or high-noise tools.
- Webhook-triggered sessions receive a deliberately safer subset.
- Skills have progressive disclosure from list metadata to full skill to individual reference files.
- Skills can declare platform compatibility and conditional activation based on available tools/toolsets.
- `/learn` can transform a successful conversation, local docs, URLs, or large knowledge sources into a reusable skill.
- Large knowledge skills keep a lean `SKILL.md` and put topic/chapter material under references.
- Skill install state records origin and hashes.
- The curator tracks usage, consolidates overlaps, archives stale agent-created skills, and avoids silently mutating protected external/vendor material.

AI-Verse takeaway: combine Hermes's dynamic discovery and curator ideas with stricter core-enforced workspace grants.

Sources:

- https://github.com/NousResearch/hermes-agent/blob/main/toolsets.py
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/curator.md

### LifeOS

LifeOS currently treats skills as its action surface and has a formal skill lifecycle. Of particular value to AI-Verse:

- `CreateSkill` owns creation, modification, canonicalization, validation, testing, and improvement.
- `SuggestSkills` is explicitly read-only and proposal-only.
- Skill-gap discovery uses recurrence and frustration signals rather than just topic frequency.
- Gap proposals are deduplicated against the actual body of existing skills, not only names.
- Public skill logic is separated from user-specific customizations.
- Deterministic collection is preferred before model judgment so repeated evaluations see comparable evidence.
- Authoring guidance favors outcome/constraint contracts rather than over-specified model reasoning steps, while retaining safety gates, tool contracts, known gotchas, and output contracts.

AI-Verse takeaway: keep a hard permission boundary between discovering a skill gap and mutating the trusted capability repository.

Sources:

- https://github.com/danielmiessler/LifeOS/blob/main/LifeOS/install/LIFEOS/DOCUMENTATION/Skills/SkillSystem.md
- https://github.com/danielmiessler/LifeOS/blob/main/LifeOS/install/skills/CreateSkill/SKILL.md
- https://github.com/danielmiessler/LifeOS/blob/main/LifeOS/install/skills/SuggestSkills/SKILL.md

### OpenClaw

OpenClaw has one of the clearest current models for skill lifecycle security.

Important patterns:

- Multiple skill roots with precedence.
- Workspace/project skills can be materialized into an execution sandbox rather than exposing host originals.
- Skill eligibility and tool authorization are separate.
- Skill Workshop provides a proposal queue for reusable agent-discovered work.
- Third-party skill installation is treated as untrusted-code installation.
- Realpath checks and symlink containment protect skill roots.
- An install policy hook can fail closed before installation.

AI-Verse takeaway: make the Workshop concept native, but keep AI-Verse OS as the authority that grants execution scope.

Source:

- https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md

## Portability baseline: Agent Skills

The open Agent Skills format is the correct portability floor for AI-Verse.

Current core structure:

```text
skill-name/
├── SKILL.md
├── scripts/        # optional
├── references/     # optional
└── assets/         # optional
```

Core frontmatter centers on:

- `name`
- `description`
- optional license/compatibility/metadata
- experimental or client-specific tool declarations

The key architectural advantage is progressive disclosure. Metadata is cheap enough to index broadly, the main instructions load on activation, and larger resources load only when needed.

AI-Verse should remain compatible with this format and place richer runtime contracts in an optional sidecar rather than making non-standard fields mandatory inside `SKILL.md`.

Source:

- https://agentskills.io/specification

## Tool registries: what the best systems are converging on

A modern tool registry needs more than a function name and description.

### Minimum tool contract

Every tool should have:

- stable name and version
- concise description optimized for retrieval
- JSON Schema input
- JSON Schema output
- side-effect class
- required runtime capabilities
- network policy
- secret requirements expressed as handles
- timeout and cancellation support
- idempotency classification
- structured error types
- audit/trace metadata

### Visibility is dynamic

PydanticAI's deferred tool loading and current provider-native tool search illustrate an important constraint: a model should not see every tool schema all the time.

A good target for AI-Verse is:

- small hotset eagerly visible
- skill-required toolpack visible after skill activation
- long-tail tools discoverable by tool search
- individual dangerous tools possibly visible but approval-gated
- tools irrelevant to the current workspace posture completely hidden

### Approval happens after argument validation

PydanticAI's current approval pattern is especially strong: validate arguments first, then defer or request approval. This prevents a user from being asked to approve malformed or ambiguous calls.

AI-Verse should mirror that sequence:

**select -> validate -> resolve scope -> policy check -> approve if required -> execute -> verify -> record**

## Coding intelligence: why semantic sweeping is day-one critical

Aider's repository map remains an important architecture reference because it does more than text search. It extracts structural symbols with tree-sitter and ranks relevant code relationships so the model can understand a large repository without reading every file.

A modern AI-Verse codebase-sweep skill should extend this idea with:

- AST/symbol extraction
- imports and dependency graph
- call/reference graph where available
- git change history relevance
- test-to-code mapping
- config/build graph
- PageRank or similar centrality
- query-specific lexical/semantic ranking
- generated concise architecture map plus links to exact files/symbols

The map is a derived artifact, not source of truth. It can be rebuilt.

Source:

- https://github.com/Aider-AI/aider/blob/main/aider/repomap.py

## Browser operations: execution needs proof and secret isolation

Browser Use demonstrates two patterns that should be mandatory for high-authority browser skills:

- domain allowlists/prohibited domains
- sensitive values represented to the model by placeholders, with real values injected only at execution time

AI-Verse browser skills should also require completion evidence for consequential actions, such as the resulting page state, receipt identifier, final URL, or screenshot/DOM assertion.

Sources:

- https://github.com/browser-use/browser-use/blob/main/skills/open-source/references/browser.md
- https://github.com/browser-use/browser-use/blob/main/skills/open-source/references/examples.md

## Subagents: isolate by default

DeepAgents, OpenHands, Goose, and current multi-agent coding systems all show why delegation must be scoped.

Recommended AI-Verse defaults:

- child gets only delegated task, not entire parent transcript, unless explicitly forked
- child receives a narrower toolset than parent by default
- child receives an explicit workspace permission set
- child has iteration/time/cost budget
- recursive delegation disabled by default
- child returns structured result plus artifacts/evidence
- parent merges results, not child state

OpenHands additionally exposes per-subagent model, max iteration, max budget, hooks, MCP config, permission mode, and condenser settings. Goose's self-test explicitly checks that nested delegation cannot silently expand.

Sources:

- https://github.com/langchain-ai/deepagents/blob/main/libs/deepagents/deepagents/middleware/subagents.py
- https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/subagent/AGENTS.md
- https://github.com/block/goose/blob/main/goose-self-test.yaml

## Memory and knowledge write-back

Letta Code provides a useful separation:

- memory affects future judgment/context
- skills represent procedural knowledge loaded on demand
- mods/harness configuration enforce deterministic runtime behavior

This maps cleanly to AI-Verse's existing core/source-of-truth design. The Skills repo should not become a second memory system. Instead, a `knowledge-writeback` skill should produce a structured, provenance-preserving patch proposal for the core Markdown source of truth.

Source:

- https://github.com/letta-ai/letta-code/blob/main/src/agent/prompts/letta_local_memfs.md

## Security and quality gates

### NVIDIA SkillSpector

SkillSpector is a direct signal that skills have become a software supply-chain surface. Its current checks cover prompt injection, exfiltration, privilege escalation, supply-chain behavior, excessive agency, memory poisoning, tool misuse, concealed instructions, dangerous code, taint tracking, MCP least privilege, and tool poisoning.

AI-Verse should either integrate SkillSpector directly or implement equivalent checks before enabling third-party or generated skills.

Source:

- https://github.com/NVIDIA/SkillSpector

### NVIDIA SkillEvaluator

SkillEvaluator's three tiers are an excellent quality model:

1. deterministic validation
2. semantic deduplication/redundancy analysis
3. live sandboxed agent evaluation

AI-Verse should adopt this separation even if it implements its own evaluator.

Source:

- https://github.com/NVIDIA/SkillEvaluator

## Failure patterns to avoid

### Anti-pattern 1: one giant base prompt

Why it fails:

- high token cost
- lower tool/skill selection precision
- accidental cross-domain instruction collisions
- difficult versioning and rollback

### Anti-pattern 2: every skill contains shell snippets and arbitrary execution

Why it fails:

- poor portability
- hidden dependencies
- weak validation
- high supply-chain risk

Use deterministic typed toolpacks or scripts with explicit dependency manifests instead.

### Anti-pattern 3: workspace path passed as a normal model argument

Why it fails:

- the model can invent or mutate the path
- prompt injection can attempt traversal
- authorization and task arguments become conflated

Workspace scope should be attached by the trusted runtime out-of-band.

### Anti-pattern 4: skill frontmatter grants authority

`allowed-tools` is useful as a requested/preferred set but should never override runtime policy.

### Anti-pattern 5: AI-generated skills write directly into trusted production skills

Use proposals, quarantine, scans, evals, and promotion.

### Anti-pattern 6: skill discovery based only on keyword lists

Descriptions should be retrieval-friendly, but at scale the registry should support semantic search plus trigger/non-trigger evals.

### Anti-pattern 7: curation can rewrite vendor or human-authored skills

Curator authority should be ownership-scoped and reversible.

## Research-driven architecture decision

The recommended AI-Verse model is:

```text
Portable procedural layer       SKILL.md
          ↓ requests
Machine contract layer          aiverse.skill.yaml
          ↓ resolves
Capability/toolpack layer       typed JSON-schema tools
          ↓ constrained by
AI-Verse OS runtime             workspace + policy + secrets + approvals
          ↓ produces
Evidence + trace layer          structured result + verification + provenance
```

The skills repository can therefore evolve quickly without weakening the core OS isolation model.

## Sources and repositories reviewed

Primary and directly relevant repositories/docs reviewed for this snapshot:

1. https://github.com/NousResearch/hermes-agent
2. https://github.com/danielmiessler/LifeOS
3. https://github.com/openclaw/openclaw
4. https://agentskills.io/specification
5. https://github.com/anthropics/skills
6. https://github.com/openai/skills
7. https://github.com/langchain-ai/deepagents
8. https://github.com/pydantic/pydantic-ai
9. https://github.com/google-gemini/gemini-cli
10. https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills
11. https://github.com/cline/cline
12. https://github.com/OpenHands/software-agent-sdk
13. https://github.com/anomalyco/opencode
14. https://github.com/block/goose
15. https://github.com/block/agent-skills
16. https://github.com/browser-use/browser-use
17. https://github.com/letta-ai/letta-code
18. https://github.com/Aider-AI/aider
19. https://github.com/crewAIInc/crewAI
20. https://github.com/continuedev/continue
21. https://github.com/microsoft/agent-framework
22. https://github.com/agent0ai/agent-zero
23. https://github.com/NVIDIA/SkillSpector
24. https://github.com/NVIDIA/SkillEvaluator
25. https://github.com/JPeetz/agent-skills
26. https://github.com/RooCodeInc/Roo-Code
27. https://github.com/SWE-agent/SWE-agent

This list intentionally mixes skill-native frameworks, tool-runtime frameworks, coding agents, browser agents, memory-first agents, security scanners, and skill registries. The blueprint is based on patterns that recur across categories rather than assuming that any one repository has the complete answer.