# Implementation Status

**Snapshot:** 2026-09-09

## Locked decisions

- The original 20 Machine / Reliability capabilities remain part of the 100-capability foundation.
- The researched top 80 employee skills are additive to those 20.
- Original upstream skills are preferred over AI-Verse rewrites.
- `skills/imported/ai-verse/` is permanently reserved for future AI-Verse-authored skills.
- Canonical local install target is planned as `~/.aiverse/skills/`.
- One canonical installed library will be exposed to multiple agents through adapters.
- AI-Verse OS remains the authority for workspace scope, memory, secrets, permissions, cadence and durable write-back.
- Role bundles compose skills. They do not replace the underlying skill library with giant personas.
- Operator Packs are separate from professional capability skills.
- Full installation is the intended default for AI-Verse OS because discovery is progressive.
- Dependencies required by ranked skills do not inflate the canonical 100-skill count; they are dependency/operator packages.

## Phase completed

The first distribution implementation phase is complete:

- permanent source namespace structure
- source registry
- canonical 100-capability registry
- authoritative package acquisition registry
- original-upstream import policy
- distribution/install architecture documentation
- roles/operators/profiles/adapters/installer scaffolding
- first original vendored packages from Google, Hermes and LifeOS
- pinned current revisions for the major source ecosystems already inspected
- durable project-state handoff for future context compression

## Import progress

Six original upstream capabilities are physically vendored:

- Google `persona-exec-assistant`
- Google `persona-project-manager`
- Google `persona-hr-coordinator`
- Google `persona-event-coordinator`
- Hermes `email-inbox-triage`
- LifeOS `Council` complete package

These preserve original upstream skill bodies rather than AI-Verse rewrites. The imported Google, Hermes and LifeOS `SKILL.md` proof files have been hash-checked against the upstream Git blobs. `Council` also preserves the complete referenced multi-file package.

Current acquisition/import state is authoritative in `registry/packages.json`. `registry/skills.json` remains the canonical 100-capability identity/ranking catalog; its bootstrap `state` field can lag until bulk reconciliation.

## Source pin progress

Pinned current revisions already captured for:

- Anthropic Skills
- Anthropic Knowledge Work Plugins
- Google Workspace CLI
- Hermes Agent
- LifeOS
- Corey Haines Marketing Skills
- Social Media Skills
- HubSpot Agent CLI Skills
- ByteDance DeerFlow
- AI Film Skills
- Film Production Skills
- FFmpeg Skill
- Premiere Agent
- Adobe Agent Skills

Additional specialist source pins and exact package paths continue in the next source-completion pass.

## Dependency discovery

The original Google persona skills depend on utility skills such as Gmail, Calendar, Drive, Chat and Sheets. These dependencies will be acquired as Operator/dependency packages and will not increase the canonical 100-capability count.

This dependency rule applies across every ecosystem.

## Next slice

- resolve all remaining exact upstream package paths and package trees
- verify license state source-by-source
- vendor directly redistributable originals where sensible
- configure pinned upstream-fetch for originals better kept at source
- complete commit/hash provenance
- reconcile canonical registry package states in bulk
- extend `THIRD_PARTY_NOTICES.md`
- resolve and register dependency/operator packages required to make the selected originals runnable
- after the 80 are source-complete, package the 20 AI-Verse foundation capabilities
- then build aliases/collision policy, Role Bundles and Operator Pack catalog
- only after package catalog completion, implement installer/runtime adapters/doctor/update
