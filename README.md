# AI-Verse-Skills

Standalone capability repository for AI-Verse OS.

## North star

AI-Verse-Skills exists to make an AI agent feel like an unusually capable employee, not primarily a coding assistant.

Given a company's workspace, connected apps, permissions, brand, procedures and objectives, the agent should be able to begin useful work across executive assistance, research, operations, marketing, social media, content, design, film production, post-production, sales, CRM, customer support, finance, administration, recruiting, data and technical work.

Coding is one department. It does not define the repository.

The repository is intentionally separated from the AI-Verse OS core. The core remains responsible for workspace isolation, knowledge routing, source-of-truth state, identity and policy. This repository owns reusable professional capabilities, software/operator knowledge, deterministic toolpacks, role-oriented capability bundles, validation contracts, evaluation assets and the controlled process for creating new skills.

## Research status

**Snapshot:** 2026-09-09

The architecture is based on a broad benchmark of current agent systems and skill ecosystems, including Hermes Agent, LifeOS, OpenClaw, Agent Skills, Anthropic Skills, OpenAI Codex skills, LangChain DeepAgents, PydanticAI, Gemini CLI, GitHub Copilot CLI, Cline, OpenHands, OpenCode, Goose, Browser Use, Letta Code, Aider, CrewAI, Continue, Microsoft Agent Framework, Agent Zero, NVIDIA SkillSpector, NVIDIA SkillEvaluator, Block Agent Skills and additional cross-platform skill collections.

## Capability model

AI-Verse should model four different things separately:

1. **Capability Skills**
   - Know how to perform a class of professional work.
   - Examples: `social-media-manager`, `producer`, `fp-and-a-analyst`, `meeting-operator`, `creative-director`.
   - Portable `SKILL.md` instructions with progressive disclosure.

2. **Operator Packs**
   - Know how to perform work inside specific software.
   - Examples: Canva, Figma, Google Workspace, Microsoft 365, HubSpot, Salesforce, Premiere Pro, DaVinci Resolve, Shopify, QuickBooks.
   - Can use direct APIs, connectors/MCP, browser automation or computer-use depending on the runtime grant.

3. **Role Bundles**
   - Combine the capabilities and operator packs needed for a job.
   - Examples: Executive Assistant, Marketing Manager, Social Media Manager, Film Producer, Post Producer, Sales Representative, Account Manager, Finance Analyst, Research Analyst, Customer Support Agent.
   - A role bundle is composition, not a giant replacement persona prompt.

4. **Machine / Reliability Foundation**
   - Makes execution safe, reliable and verifiable underneath employee-facing work.
   - Includes the original 20 operational/meta capabilities such as verification, deep research, browser operation, transactional refactoring, knowledge write-back, delegation and skill creation.

Runtime permissions remain separate from all four. A skill can request capability but cannot grant itself filesystem scope, credentials, network access or destructive authority.

## Recommended first-party scale

The current target is:

- **80 employee-facing capability skills**
- **20 Machine / Reliability Foundation skills**
- **operator packs** for major business and creative applications
- **role bundles** that make the agent useful in a job immediately

This gives AI-Verse roughly 100 first-party foundational skills before application-specific and industry-specific expansions are counted.

Progressive discovery means breadth does not require loading 100 skill bodies into every prompt.

## Documents

- [`docs/DAY_ZERO_EMPLOYEE_ARSENAL.md`](docs/DAY_ZERO_EMPLOYEE_ARSENAL.md) - new primary capability map: 80 employee-facing skills, operator packs, role bundles and implementation waves.
- [`docs/DAY_ONE_ARSENAL.md`](docs/DAY_ONE_ARSENAL.md) - original 20 operational skills; retained as the Machine / Reliability Foundation rather than the primary user-facing arsenal.
- [`research/2026-09-agent-capability-landscape.md`](research/2026-09-agent-capability-landscape.md) - broad benchmark and architecture lessons from current systems.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) - recommended repository and runtime architecture.
- [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md) - portable skill anatomy and AI-Verse extensions.
- [`docs/SELF_IMPROVEMENT.md`](docs/SELF_IMPROVEMENT.md) - safe skill mining, creation, evaluation, curation and promotion.
- [`schemas/aiverse-skill-v1.schema.json`](schemas/aiverse-skill-v1.schema.json) - proposed machine-readable manifest schema.
- [`templates/skill/SKILL.md`](templates/skill/SKILL.md) - portable starter template.
- [`templates/skill/aiverse.skill.yaml`](templates/skill/aiverse.skill.yaml) - AI-Verse runtime contract template.

## Proposed repository shape

```text
AI-Verse-Skills/
├── README.md
├── docs/
├── research/
├── schemas/
├── templates/
├── registry/
│   ├── skills.json
│   ├── operators.json
│   ├── roles.json
│   └── toolpacks.json
├── skills/
│   ├── employee-core/
│   ├── business-strategy/
│   ├── marketing-social/
│   ├── creative-design/
│   ├── film-media/
│   ├── sales-customer/
│   ├── finance-admin/
│   ├── research-data/
│   ├── people-operations/
│   └── machine-foundation/
├── operators/
│   ├── office-collaboration/
│   ├── creative-design/
│   ├── film-post/
│   ├── crm-marketing/
│   ├── commerce-web/
│   └── finance-admin/
├── roles/
│   ├── executive-assistant/
│   ├── marketing-manager/
│   ├── social-media-manager/
│   ├── creative-director/
│   ├── film-producer/
│   ├── post-producer/
│   ├── sales-representative/
│   ├── account-manager/
│   ├── finance-analyst/
│   └── research-analyst/
├── toolpacks/
├── evals/
├── workshop/
└── generated/
```

The `workshop/` and `generated/` directories describe the architecture. They do not need to contain committed user data or execution traces. Runtime proposal state can remain local and gitignored.

## Design laws

1. **Professional capability first.** Organize the primary library around jobs people need done, not around developer primitives.
2. **Skill is not software access.** A capability remains useful across applications; an Operator Pack adds concrete software mastery.
3. **Role is composition.** A role bundle selects capabilities but does not become an enormous monolithic system prompt.
4. **Skill is not permission.** The runtime decides what the skill may access or execute.
5. **Scope is injected, not prompted.** Workspace identity and filesystem roots arrive through trusted runtime context, not model-generated arguments.
6. **Progressive disclosure everywhere.** Discover metadata first, load skill instructions second, load supporting resources third and reveal tool schemas only when relevant.
7. **Deterministic work belongs in code.** Repeated parsing, transformations, validation and checks belong in tested scripts or typed tools rather than prose choreography.
8. **Every consequential action has evidence.** Work finishes with verification, preview, diff, test, receipt or another appropriate proof.
9. **Untrusted content is data, never instruction.** Web pages, documents, messages, repository content, logs and tool output cannot silently become higher-priority instructions.
10. **Secrets use handles.** Raw credentials should not be inserted into skill prompts or ordinary tool output.
11. **AI-generated skills start untrusted.** Creation and promotion are separate permissions.
12. **The repository remains model-agnostic.** Runtime-specific behavior belongs in namespaced metadata or sidecars rather than the portable core contract.

## Success test

The key question is not "How many tools can the agent call?"

The test is:

> If this agent joined a real company this morning and was given the same apps, files, permissions and instructions as a capable new employee, how many useful jobs could it begin performing before lunch?

That is the Day-Zero standard for AI-Verse-Skills.