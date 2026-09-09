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

Dependencies required by selected skills are treated as Operator/dependency packages and do not inflate the canonical 100-capability count.

## Current physical implementation

The permanent top-level implementation layers exist:

- `skills/`
- `registry/`
- `operators/`
- `roles/`
- `profiles/`
- `adapters/`
- `installer/`
- existing `schemas/`, `templates/`, `docs/`, `research/`

The registries are:

- `registry/sources.json` - approved source namespaces/repositories
- `registry/skills.json` - canonical 100 capability identities/ranks
- `registry/packages.json` - authoritative current acquisition/import state and source pins
- `registry/aliases.json` - canonical alias layer, initially empty

`registry/packages.json` is authoritative for whether a package is actually vendored/fetched. The bootstrap `state` values inside `registry/skills.json` can lag until bulk reconciliation.

## Verified original imports

Six upstream originals are physically vendored.

### Google Executive Assistant

Path: `skills/imported/google/persona-exec-assistant/`  
Upstream: `googleworkspace/cli` at `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`  
License: Apache-2.0  
Original `SKILL.md` verified by Git blob hash.

### Google Project Manager

Path: `skills/imported/google/persona-project-manager/`  
Upstream: `googleworkspace/cli` at `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`  
License: Apache-2.0  
Original `SKILL.md` is vendored with exact upstream blob provenance.

### Google HR Coordinator

Path: `skills/imported/google/persona-hr-coordinator/`  
Upstream: `googleworkspace/cli` at `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`  
License: Apache-2.0  
Original `SKILL.md` is vendored with exact upstream blob provenance.

### Google Event Coordinator

Path: `skills/imported/google/persona-event-coordinator/`  
Upstream: `googleworkspace/cli` at `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`  
License: Apache-2.0  
Original `SKILL.md` is vendored with exact upstream blob provenance.

### Hermes Email Inbox Triage

Path: `skills/imported/hermes/email-inbox-triage/`  
Upstream: `NousResearch/hermes-agent` at `7dc796463d543a57270779b7f71f37f18b6faa5e`  
Skill license: MIT  
Original `SKILL.md` verified by Git blob hash.

### LifeOS Council

Path: `skills/imported/lifeos/Council/`  
Upstream: `danielmiessler/LifeOS` at `5e2f2e8c0abde612da0e99c16c0d07d4ec21b88c`  
License: MIT  
The complete package is vendored: `SKILL.md`, three context files and two workflow files. `SOURCE.json` records all upstream blob hashes. Original `SKILL.md` verified by Git blob hash.

## Source pins already captured

Current September 2026 source revisions have been recorded for:

- `anthropics/skills` -> `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`
- `anthropics/knowledge-work-plugins` -> `34e1eae3e1cca0be18bc85067cc6dd78d1f5d4e5`
- `googleworkspace/cli` -> `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd`
- `NousResearch/hermes-agent` -> `7dc796463d543a57270779b7f71f37f18b6faa5e`
- `danielmiessler/LifeOS` -> `5e2f2e8c0abde612da0e99c16c0d07d4ec21b88c`
- `coreyhaines31/marketingskills` -> `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`
- `social-media-skills/skills` -> `6e30eeb2f6736bda8683b6bbaa674af3641d7945`
- `HubSpot/agent-cli-skills` -> `71f2bdefcc0247b1f378cb98186800dc57b6f6b1`
- `bytedance/deer-flow` -> `3c7d3303d3ef9335b6d91b49acff1a6f6609936c`
- `62656456/ai-film-skills` -> `678edc06d3318c1516f6eb73503f740427fdd831`
- `zhangzhangco/film-production-skills` -> `47b2a6a432235e716fa2aa0d08eefae76fdb34fd`
- `kajisho5/ffmpeg-skill` -> `0055f7b295ab4d5ef4dc30af76638775eccd0667`
- `Kemerd/premiere-agent` -> `77ed50f4bff14b67b054a64d26aedd7ec217b701`
- `aedev-tools/adobe-agent-skills` -> `00f131ee5481cd597e6f63f997d92c6fe26586a0`

Do not re-research these pins unless intentionally updating the snapshot.

## Dependency discovery

The four Google persona packages reveal an important install rule: ranked employee capabilities can depend on upstream utility/operator skills.

Known Google dependencies include:

- `gws-gmail`
- `gws-calendar`
- `gws-drive`
- `gws-chat`
- `gws-sheets`

These will be acquired as dependency/operator packages. They do not increase the canonical 100-capability count.

## Next implementation slice

Continue from here, do not restart research.

1. Resolve exact upstream path/package tree for every remaining employee skill in `registry/skills.json`.
2. Verify repository/package license status.
3. Vendor every directly redistributable original package where that is the cleanest distribution choice.
4. For originals better kept upstream, create pinned `upstream-fetch` records rather than rewriting them.
5. Pin exact source commit/tag and content hashes.
6. Use `registry/packages.json` as authoritative package acquisition state and later reconcile `registry/skills.json` in bulk.
7. Maintain `THIRD_PARTY_NOTICES.md` as packages are added.
8. Register dependency/operator packages required by the originals.
9. After the 80 are source-complete, package the 20 AI-Verse foundation skills.
10. Then build aliases/collision policy, Role Bundles and Operator Pack catalog.
11. Only after package catalog completion, implement installer/runtime adapters/doctor/update.

## Do not regress these decisions

- Do not collapse the project back into a coding-centric skill library.
- Do not replace original upstream skills with generic AI-Verse rewrites unless explicitly requested later.
- Do not merge this repo into AI-Verse OS, Memory or Brain repositories.
- Do not let skills own workspace isolation, secrets, memory authority or scheduling.
- Do not load the full 100-skill bodies into every prompt.
- Do not use `ai-verse/` for third-party skills.
- Do not count dependencies/operators as extra canonical employee capabilities.
- Do not discard research files after implementation begins.
