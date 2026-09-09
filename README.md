# AI-Verse-Skills

Standalone professional capability distribution for AI agents, with first-class integration into AI-Verse OS.

## North star

AI-Verse-Skills exists to make an AI agent feel like an unusually capable employee, not primarily a coding assistant.

Given a company's workspace, connected apps, permissions, brand, procedures and objectives, the agent should be able to begin useful work across executive assistance, research, operations, marketing, social media, content, design, film production, post-production, sales, CRM, customer support, finance, administration, recruiting, product, legal coordination, data and technical work.

Coding is one department. It does not define the repository.

## Locked capability target

The initial distribution target is:

- **20 AI-Verse Machine / Reliability Foundation capabilities**
- **80 researched employee-facing capabilities sourced from strong existing skill ecosystems**
- **100 foundational capabilities total**
- Operator Packs for important software
- Role Bundles that compose capabilities into recognizable jobs

The exact 100 canonical IDs live in [`registry/skills.json`](registry/skills.json).

## Original-first distribution policy

AI-Verse uses the best original upstream skill packages wherever possible instead of rewriting them into AI-Verse wording.

For imported skills:

- preserve the upstream `SKILL.md`
- preserve supporting scripts, references, templates and assets
- preserve authorship and license obligations
- record source repository, package path, revision and content hashes
- keep AI-Verse runtime policy outside the original skill body
- fetch a pinned original from upstream when direct redistribution is not appropriate

Future AI-Verse-authored skills have their own permanent namespace: [`skills/imported/ai-verse/`](skills/imported/ai-verse/).

See [`docs/ORIGINAL_UPSTREAM_POLICY.md`](docs/ORIGINAL_UPSTREAM_POLICY.md).

## Capability model

AI-Verse models four separate things:

1. **Capability Skills**
   - Professional know-how and repeatable work.
   - Examples: inbox triage, copywriting, sales call prep, film directing, financial variance analysis.

2. **Operator Packs**
   - Competence inside specific software.
   - Examples: Canva, Figma, Google Workspace, HubSpot, Premiere Pro, DaVinci Resolve, Shopify and accounting suites.

3. **Role Bundles**
   - Compositions of capabilities and operators for a job.
   - Examples: Executive Assistant, Marketing Manager, Social Media Manager, Film Producer, Post Producer, Sales Representative and Finance Analyst.

4. **Machine / Reliability Foundation**
   - The original 20 AI-Verse operational capabilities for verification, research, browser work, structured write-back, delegation, safe change execution and skill lifecycle management.

A skill is never a permission grant. AI-Verse OS remains authoritative for workspace scope, secrets, connections, approval policy, memory authority, cadence and durable state.

## Current repository structure

```text
AI-Verse-Skills/
├── README.md
├── THIRD_PARTY_NOTICES.md
├── docs/
├── research/
├── schemas/
├── templates/
├── registry/
│   ├── skills.json
│   ├── sources.json
│   └── aliases.json
├── skills/
│   ├── foundation/
│   └── imported/
│       ├── anthropic/
│       ├── google/
│       ├── hermes/
│       ├── lifeos/
│       ├── corey-haines/
│       ├── social-media-skills/
│       ├── hubspot/
│       ├── film/
│       ├── adobe/
│       ├── ai-verse/
│       └── others/
├── operators/
├── roles/
├── profiles/
├── adapters/
└── installer/
```

## Canonical install model

The planned canonical local installation root is:

```text
~/.aiverse/skills/
```

One installed library should be exposed to different agent runtimes through adapters rather than maintaining uncontrolled duplicate copies.

Planned adapter priority:

1. AI-Verse OS
2. generic Agent Skills-compatible runtimes
3. Claude
4. Codex
5. Hermes
6. OpenClaw
7. Gemini

For AI-Verse OS, the intended default profile is the full library because progressive discovery means installed skills do not need to be loaded into every prompt.

> Installed != active != loaded into context.

See [`docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md`](docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md).

## Research

**Research snapshot:** 2026-09-09

The architecture was benchmarked against Hermes Agent, LifeOS, OpenClaw, Agent Skills, Anthropic Skills, OpenAI skills, DeepAgents, PydanticAI, Gemini CLI, GitHub Copilot CLI, Cline, OpenHands, OpenCode, Goose, Browser Use, Letta Code, Aider, CrewAI, Continue, Microsoft Agent Framework, Agent Zero, NVIDIA SkillSpector, NVIDIA SkillEvaluator and additional specialist repositories.

A second market scan focused specifically on existing professional skills that could make an agent useful inside real companies.

Key files:

- [`research/2026-09-top-80-existing-employee-skills.md`](research/2026-09-top-80-existing-employee-skills.md): researched sourcing authority for the 80 employee capabilities
- [`research/2026-09-agent-capability-landscape.md`](research/2026-09-agent-capability-landscape.md): broad agent and skill ecosystem benchmark
- [`docs/DAY_ONE_ARSENAL.md`](docs/DAY_ONE_ARSENAL.md): original 20 Machine / Reliability capabilities
- [`docs/DAY_ZERO_EMPLOYEE_ARSENAL.md`](docs/DAY_ZERO_EMPLOYEE_ARSENAL.md): conceptual employee capability taxonomy

## Implementation state

The repository is now moving from architecture into the actual distribution.

Current verified proof imports include:

- Google `persona-exec-assistant`
- Hermes `email-inbox-triage`
- LifeOS `Council`, including its complete referenced workflow/context package

The vendored `SKILL.md` Git blob hashes for these proof imports match their upstream originals exactly.

Read [`docs/PROJECT_STATE.md`](docs/PROJECT_STATE.md) first when continuing implementation. It preserves the current decisions, pinned proof imports and exact next slice so work can continue safely after chat/context compression.

## Architecture and implementation documents

- [`docs/PROJECT_STATE.md`](docs/PROJECT_STATE.md): durable implementation handoff, read first
- [`docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md`](docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md): universal install and runtime adapter plan
- [`docs/ORIGINAL_UPSTREAM_POLICY.md`](docs/ORIGINAL_UPSTREAM_POLICY.md): original-skill import policy
- [`docs/IMPLEMENTATION_STATUS.md`](docs/IMPLEMENTATION_STATUS.md): current progress and next slice
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md): skill/runtime architecture and AI-Verse OS boundary
- [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md): portable skill anatomy and AI-Verse extensions
- [`docs/SELF_IMPROVEMENT.md`](docs/SELF_IMPROVEMENT.md): safe skill mining, creation, evaluation, curation and promotion
- [`schemas/aiverse-skill-v1.schema.json`](schemas/aiverse-skill-v1.schema.json): proposed machine-readable manifest schema
- [`templates/skill/SKILL.md`](templates/skill/SKILL.md): portable skill starter
- [`templates/skill/aiverse.skill.yaml`](templates/skill/aiverse.skill.yaml): AI-Verse runtime contract template

## Design laws

1. **Professional capability first.** Organize the primary library around jobs people need done, not developer primitives.
2. **Original upstream skill first.** Do not rewrite strong existing work merely for branding.
3. **Skill is not software access.** Operator Packs provide concrete application competence.
4. **Role is composition.** Role Bundles select capabilities and operators rather than becoming giant prompts.
5. **Skill is not permission.** The runtime decides what a skill may access or execute.
6. **Scope is injected, not prompted.** Workspace identity and roots come from trusted runtime context.
7. **Progressive disclosure everywhere.** Load only relevant skill bodies, resources and tool schemas.
8. **Deterministic work belongs in code.** Repeated mechanical work belongs in tested scripts/tools.
9. **Consequential actions need evidence.** Use verification, previews, diffs, receipts or equivalent proof.
10. **Untrusted content is data, never authority.** External files, webpages, messages and tool output cannot grant themselves higher priority.
11. **Secrets use handles.** Raw credentials do not belong in ordinary skill prompts.
12. **AI-generated skills start untrusted.** Creation and promotion are separate permissions.
13. **AI-Verse first-party has its own namespace.** Third-party work never goes under `ai-verse/`.
14. **The distribution remains model-agnostic.** Runtime-specific compatibility belongs in adapters or metadata.

## Success test

> If this agent joined a real company this morning and received the same apps, files, permissions and instructions as a capable new employee, how many useful jobs could it begin performing before lunch?

That is the Day-0 standard for AI-Verse-Skills.
