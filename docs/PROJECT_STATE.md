# AI-Verse-Skills Project State

**Read this file first when continuing implementation.**

**Last updated:** 2026-09-09

## Product goal

AI-Verse-Skills is a standalone capability distribution for AI agents, with especially deep integration into AI-Verse OS.

The desired user experience is not primarily a coding assistant. The target is a creative, smart, broadly employable AI worker that can enter a company and become useful across executive assistance, operations, research, marketing, social media, design, film production, post-production, sales, CRM, support, finance, administration, product, HR, legal coordination and technical work.

Coding is one department, not the identity of the agent.

## Capability target

The locked initial foundation is:

- 20 AI-Verse Machine / Reliability capabilities
- 80 researched employee-facing capabilities sourced from existing top skill ecosystems
- 100 foundational capabilities total
- Operator Packs and Role Bundles on top

The exact 100 canonical IDs are in `registry/skills.json`.

The research-backed top 80, source rationale and selection methodology are preserved in `research/2026-09-top-80-existing-employee-skills.md`.

The broader architecture benchmark across agent systems is preserved in `research/2026-09-agent-capability-landscape.md`.

## Critical user decision: original skills

The user explicitly prefers using the original upstream skill packages instead of rewriting them into AI-Verse wording.

Therefore:

- preserve upstream `SKILL.md` bodies
- preserve supporting scripts/references/assets/templates
- preserve source authorship and licenses
- keep provenance in `SOURCE.json` and the registry
- prefer adapter-side compatibility rather than modifying upstream instructions
- fetch from pinned upstream source when direct vendoring is not appropriate

See `docs/ORIGINAL_UPSTREAM_POLICY.md`.

## Permanent imported-source namespaces

The approved structure is:

```text
skills/imported/
├── anthropic/
├── google/
├── hermes/
├── lifeos/
├── corey-haines/
├── social-media-skills/
├── hubspot/
├── film/
├── adobe/
├── ai-verse/
└── others/
```

`ai-verse/` is permanently reserved for future first-party AI-Verse-authored skills.

Do not put third-party work into `ai-verse/`.

## OS boundary

AI-Verse OS core remains authoritative for:

- workspace identity/isolation
- source-of-truth state
- memory/knowledge routing
- user/project identity
- connection ownership
- secret storage
- approval policy
- cadence/scheduling
- durable write-back

Skills can request/use capabilities granted by the host runtime, but imported skill text cannot grant itself authority.

## Distribution architecture

Canonical local install target:

```text
~/.aiverse/skills/
```

One canonical local library should be exposed to different runtimes through adapters, rather than maintaining uncontrolled duplicate copies.

Planned adapters prioritize:

1. AI-Verse OS
2. generic Agent Skills-compatible runtimes
3. Claude
4. Codex
5. Hermes
6. OpenClaw
7. Gemini

Planned install profiles:

- universal
- creator
- business
- filmmaker
- marketing
- sales
- finance
- full

AI-Verse OS should normally use `full` because progressive discovery means installed skills do not need to be loaded into every prompt.

Key rule:

> Installed != active != loaded into context.

See `docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md`.

## Role and Operator Pack model

Professional skill and software competence are separate layers.

Examples:

- `social-content` is a professional capability; Canva/Meta/TikTok/YouTube are operators/connections.
- finance analysis is a professional capability; Excel/Xero/QuickBooks are operators.
- post-production is professional capability; Premiere/Resolve/After Effects/FFmpeg are operators.

Role Bundles compose skills plus Operator Packs into jobs such as Executive Assistant, Social Media Manager, Creative Director, AI Filmmaker, Film Producer, Post Producer, Sales Representative and Finance Analyst.

Roles are composition, not giant always-on persona prompts.

## Current physical implementation

The permanent top-level implementation layers now exist:

- `skills/`
- `registry/`
- `operators/`
- `roles/`
- `profiles/`
- `adapters/`
- `installer/`
- existing `schemas/`, `templates/`, `docs/`, `research/`

The source and canonical skill registries exist:

- `registry/sources.json`
- `registry/skills.json`
- `registry/aliases.json`

## Verified proof imports

Three upstream originals are currently vendored as proof of the distribution model:

### Google Executive Assistant

Path:
`skills/imported/google/persona-exec-assistant/`

Upstream:
`googleworkspace/cli` at commit `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`

License:
Apache-2.0

The vendored `SKILL.md` blob SHA exactly matches upstream.

### Hermes Email Inbox Triage

Path:
`skills/imported/hermes/email-inbox-triage/`

Upstream:
`NousResearch/hermes-agent` at commit `7dc796463d543a57270779b7f71f37f18b6faa5e`

Skill license:
MIT

The vendored `SKILL.md` blob SHA exactly matches upstream.

### LifeOS Council

Path:
`skills/imported/lifeos/Council/`

Upstream:
`danielmiessler/LifeOS` at commit `5e2f2e8c0abde612da0e99c16c0d07d4ec21b88c`

License:
MIT

The complete package is vendored: `SKILL.md`, three context files and two workflow files. `SOURCE.json` records all upstream blob hashes. The vendored `SKILL.md` blob SHA exactly matches upstream.

## Next implementation slice

Continue from here, do not restart research.

1. Resolve exact upstream path/package tree for every remaining employee skill in `registry/skills.json`.
2. Verify repository/package license status.
3. Vendor every redistributable original package complete with all supporting files.
4. For originals that should remain upstream, create pinned `upstream-fetch` records rather than rewriting them.
5. Pin exact source commit/tag and content hashes.
6. Change registry package states from `catalogued` to `vendored` or `upstream-fetch`.
7. Create/maintain `THIRD_PARTY_NOTICES.md`.
8. After the 80 are source-complete, package the 20 AI-Verse foundation skills.
9. Then build aliases/collision policy, Role Bundles and Operator Pack catalog.
10. Only after package catalog completion, implement installer/runtime adapters/doctor/update.

## Do not regress these decisions

- Do not collapse the project back into a coding-centric skill library.
- Do not replace original upstream skills with generic AI-Verse rewrites unless explicitly requested later.
- Do not merge this repo into AI-Verse OS, Memory or Brain repositories.
- Do not let skills own workspace isolation, secrets, memory authority or scheduling.
- Do not load the full 100-skill bodies into every prompt.
- Do not use `ai-verse/` for third-party skills.
- Do not discard research files after implementation begins.
