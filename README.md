# AI-Verse-Skills

Standalone operational capability repository for AI-Verse OS.

This repository is intentionally separated from the AI-Verse OS core. The core remains responsible for workspace isolation, knowledge routing, source-of-truth state, identity, and policy. This repository owns reusable operational capabilities: portable skills, deterministic toolpacks, validation contracts, evaluation assets, and the controlled process for creating new skills.

## Research status

**Snapshot:** 2026-09-09

The initial architecture is based on a broad benchmark of current agent systems and skill ecosystems, including Hermes Agent, LifeOS, OpenClaw, Agent Skills, Anthropic Skills, OpenAI Codex skills, LangChain DeepAgents, PydanticAI, Gemini CLI, GitHub Copilot CLI, Cline, OpenHands, OpenCode, Goose, Browser Use, Letta Code, Aider, CrewAI, Continue, Microsoft Agent Framework, Agent Zero, NVIDIA SkillSpector, NVIDIA SkillEvaluator, Block Agent Skills, and additional cross-platform skill collections.

## Core conclusion

AI-Verse-Skills should not be one giant prompt library and it should not be one giant tool registry.

The strongest architecture is a layered capability system:

1. **Portable Skills**
   - `SKILL.md` compatible with the Agent Skills ecosystem.
   - Lean discovery metadata.
   - Instructions loaded only when relevant.
   - References, scripts, examples, and assets loaded only when needed.

2. **Typed Toolpacks**
   - Deterministic executable primitives.
   - JSON Schema inputs and outputs.
   - Explicit side effects and permission classes.
   - Workspace scope injected by the runtime, never invented by the model.

3. **Runtime Policy Boundary**
   - A skill can request capabilities but cannot grant itself capabilities.
   - AI-Verse OS remains the authority for workspace scope, connections, secrets, approvals, network access, and write permissions.
   - Tool visibility and tool execution approval are separate decisions.

4. **Verification and Evals**
   - Every consequential skill defines what successful completion means.
   - Deterministic checks where possible.
   - Behavioral evals for model-dependent workflows.
   - Security scanning before installation or promotion.

5. **Controlled Self-Improvement**
   - Agents may propose new skills from successful repeated work.
   - Proposals enter a workshop/quarantine area first.
   - No autonomous direct promotion into trusted skills.
   - AI-generated skills are statically scanned, deduplicated, live-evaluated in isolation, then approved or policy-promoted.

## Documents

- [`research/2026-09-agent-capability-landscape.md`](research/2026-09-agent-capability-landscape.md) - broad benchmark and architecture lessons from current systems.
- [`docs/DAY_ONE_ARSENAL.md`](docs/DAY_ONE_ARSENAL.md) - prioritized top 20 operational skills for day one.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) - recommended repository and runtime architecture.
- [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md) - portable skill anatomy and AI-Verse extensions.
- [`docs/SELF_IMPROVEMENT.md`](docs/SELF_IMPROVEMENT.md) - safe skill mining, creation, evaluation, curation, and promotion.
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
│   └── toolpacks.json
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
│   ├── fixtures/
│   └── harness/
├── workshop/
│   ├── proposals/
│   ├── quarantine/
│   └── reports/
└── generated/
    └── README.md
```

The `workshop/` and `generated/` directories above describe the architecture. They do not need to contain committed user data or execution traces. Runtime proposal state can remain local and gitignored.

## Design laws

1. **Skill is not permission.** A skill describes how to perform work. The runtime decides what it may actually access or execute.
2. **Scope is injected, not prompted.** Workspace identity and filesystem roots arrive through trusted runtime context, not model-generated arguments.
3. **Progressive disclosure everywhere.** Discover metadata first, load skill instructions second, load supporting resources third, reveal tool schemas only when relevant.
4. **Deterministic work belongs in code.** Repeated parsing, transformations, validation, migrations, and checks belong in tested scripts or typed tools rather than prose choreography.
5. **Every write has evidence.** Consequential work finishes with verification, diff, test, receipt, or another machine-checkable proof.
6. **Untrusted content is data, never instruction.** Web pages, repository content, documents, issue text, logs, and tool output cannot silently become higher-priority instructions.
7. **Secrets use handles.** Raw credentials should not be inserted into skill prompts or ordinary tool output.
8. **AI-generated skills start untrusted.** Creation and promotion are separate permissions.
9. **Human-authored and vendor skills are protected from autonomous curation.** AI curation may operate only on explicitly AI-owned material unless a user directs otherwise.
10. **The repository remains model-agnostic.** Runtime-specific behavior goes in namespaced metadata or sidecar manifests, not in the portable core contract.

## What is deliberately not here

This repository does not define AI-Verse OS identity, long-term goals, the Brain, workspace truth, user memory, global policy, or scheduling semantics. Skills consume those capabilities through narrow runtime interfaces.

It also does not prioritize generic chatbot utilities such as weather, calculator, or generic search. The day-one arsenal is focused on heavy operational work that materially expands what an autonomous local-first OS can accomplish.