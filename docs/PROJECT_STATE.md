# AI-Verse-Skills Project State

**Read this file first when continuing implementation.**  
**Last updated:** 2026-09-09

## Product identity

AI-Verse-Skills is the standalone professional capability distribution for AI agents. It is especially compatible with AI-Verse OS, but remains a completely separate repository and installation.

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

## Critical separation decisions

These are explicit user requirements and must not regress:

1. AI-Verse-Skills and AI-Verse OS stay in separate repositories.
2. No AI-Verse-Skills package is copied, vendored or symlinked into the AI-Verse OS repository.
3. No AI-Verse OS file is copied into AI-Verse-Skills.
4. `ai-verse-os install` installs only the OS.
5. AI-Verse-Skills is installed only through a separate explicit action such as `ai-verse-os skills install` or the standalone Skills CLI.
6. AI-Verse OS references/discovers the external Skills installation when present.

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

## AI-Verse OS compatibility

The OS may reference:

```text
~/.aiverse/skills/.aiverse/installed.json
```

and load selected external packages directly from `~/.aiverse/skills/` during capability discovery.

There is no OS-repo materialization step.

## Operator readiness

Installation does not imply software availability.

`readiness` checks local dependencies where deterministic detection is possible and reports connector/host requirements otherwise.

## Validation

Normal CI validates registry integrity and full-profile dry-run planning.

Full E2E CI performs a real full upstream install and checks:

- 100 canonical installed packages
- package digests
- transactional update
- rollback
- full-profile integrity after rollback

AI-Verse OS's own CLI smoke/E2E verifies that its optional `skills` subcommand installs externally and leaves the OS repository unchanged.

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

- add more first-party AI-Verse employee skills under `skills/imported/ai-verse/`
- add additional role bundles/operator packs
- add signed release manifests
- add richer connector-specific readiness probes
- add package-manager distribution
- expand automated live skill evaluations

Do not restart the original market research unless intentionally refreshing the September 2026 snapshot.
