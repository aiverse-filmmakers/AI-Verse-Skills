# AI-Verse-Skills Project State

**Read this file first when continuing implementation.**  
**Last updated:** 2026-09-09

## Product identity

AI-Verse-Skills is the standalone professional capability distribution for AI agents, with native integration into AI-Verse OS.

The target is a creative, smart, broadly employable AI worker. Coding is one department, not the personality of the system.

## Locked v1 capability set

- 20 AI-Verse Machine / Reliability foundation skills
- 80 researched existing employee-facing skills
- 100 canonical capabilities total
- support dependencies do not increase the canonical count
- software Operator Packs remain separate from professional capability skills
- Role Bundles compose skills and operators

Canonical identity: `registry/skills.json`  
Acquisition authority: `registry/packages.json`

The older bootstrap `state` fields inside `registry/skills.json` are descriptive only; actual installability is determined by the physical 20 foundation packages plus `registry/packages.json`.

## Original-first decision

The user explicitly chose original upstream skills instead of AI-Verse rewrites.

Therefore:

- preserve original package content
- use exact pinned source revisions
- copy complete selected package directories
- keep source/runtime adaptation outside original skill bodies
- use upstream-fetch where direct vendoring is not appropriate
- reserve `skills/imported/ai-verse/` for future AI-Verse-authored skills only

## Shipping architecture

Canonical install root:

```text
~/.aiverse/skills/
```

Installer:

```text
installer/aiverse_skills.py
```

Supported lifecycle:

```text
install
update
rollback
doctor
readiness
list
adapt
uninstall
e2e
```

Install and update are transactional. A complete verified staged library is swapped into place only after successful acquisition.

## AI-Verse OS integration

Native user command:

```bash
./ai-verse-os skills install
```

OS integration exposes all canonical packages into:

```text
.claude/skills/
.agents/skills/
```

and writes derived integration state to:

```text
runtime/skills/ai-verse-skills.json
```

The OS remains authoritative for scope, permissions, secrets, connections, memory, scheduling and write-back.

## Operator readiness

Installation does not imply software availability.

`readiness` checks local dependencies where deterministic detection is possible and reports connector/host requirements otherwise.

Current operator catalog includes Google Workspace, Canva, Figma, HubSpot, Premiere Pro, After Effects, FFmpeg, Shopify, Airtable, Notion, spreadsheet tooling and browser/computer-use.

## Validation

Normal CI validates registry integrity and full-profile dry-run planning.

Full E2E CI performs a real full upstream install and clean AI-Verse OS integration, then checks:

- 100 canonical installed packages
- package digests
- Claude surface count
- Codex surface count
- native OS integration manifest
- transactional update
- rollback

## Research preservation

Do not delete:

- `research/2026-09-top-80-existing-employee-skills.md`
- `research/2026-09-agent-capability-landscape.md`
- `docs/DAY_ONE_ARSENAL.md`
- `docs/DAY_ZERO_EMPLOYEE_ARSENAL.md`
- `docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md`
- `docs/ORIGINAL_UPSTREAM_POLICY.md`

These are the durable research/decision record.

## Future work after v1

Future work is additive, not required to reconstruct v1:

- add more first-party AI-Verse employee skills under `skills/imported/ai-verse/`
- add additional role bundles/operator packs
- add signed release manifests
- add richer connector-specific readiness probes
- add package-manager distribution
- expand automated live skill evaluations

Do not restart the original market research unless intentionally refreshing the September 2026 snapshot.
