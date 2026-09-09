# AI-Verse Skills Distribution and Install Architecture

**Status:** locked architecture for implementation  
**Snapshot:** 2026-09-09

## Purpose

AI-Verse-Skills is becoming a distributable professional capability library, not just a research repository.

The distribution must work well on a generic skill-capable agent from day 0, while giving AI-Verse OS deeper integration through its existing workspace, memory, Brain, connections, permissions, cadence, verification and durable write-back layers.

The central product idea is:

> Install one curated skill distribution, keep one canonical library, and expose the right capabilities to many agents through adapters.

## Permanent source namespace layout

The approved imported-skill layout is:

```text
skills/
├── foundation/
└── imported/
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

`skills/imported/ai-verse/` is reserved for future first-party AI-Verse-authored skills. It must never be used for copied third-party work.

`skills/imported/others/` is the curated holding namespace for excellent sources that do not yet justify a dedicated top-level source namespace.

## Original-first policy

The user explicitly chose to use the best original upstream skills rather than rewrite them into AI-Verse wording.

Therefore the preferred order is:

1. Preserve the complete original skill package when redistribution is permitted.
2. Preserve upstream filenames, subfolders, scripts, references, templates and assets.
3. Add provenance outside the original body using `SOURCE.json` and the central registry.
4. Do not insert AI-Verse runtime authority into the upstream `SKILL.md`.
5. If a package should not be redistributed directly, keep a pinned upstream source record and let the installer fetch the original package.
6. Future AI-Verse-native skills live under `skills/imported/ai-verse/`.

The installer should make vendored and upstream-fetched originals feel identical to the end user.

## Canonical local installation

The long-term default canonical installation root is:

```text
~/.aiverse/skills/
```

This is the one authoritative local copy of the installed distribution.

Agent-specific adapters should expose this canonical library by:

- symlink or directory link when the agent supports it
- generated index/manifest when the agent supports an external skill root
- managed copy only when the target runtime requires physical copies
- upstream fetch into the canonical root for source-linked packages

Do not maintain independent unmanaged copies for Claude, Codex, Hermes, OpenClaw and AI-Verse OS.

## Major repository layers

```text
AI-Verse-Skills/
├── skills/          original capability packages
├── registry/        canonical catalog, provenance, aliases and source records
├── operators/       application-specific software competence
├── roles/           job-oriented compositions of skills and operators
├── profiles/        install presets
├── adapters/        runtime-specific exposure of the canonical library
├── installer/       install, update, doctor and uninstall implementation
├── schemas/         package and runtime contracts
├── evals/           compatibility, routing, safety and quality tests
├── docs/            architecture and operating documentation
└── research/        preserved research and sourcing evidence
```

## Install profiles

Planned profiles:

- `universal`
- `creator`
- `business`
- `filmmaker`
- `marketing`
- `sales`
- `finance`
- `full`

For AI-Verse OS, `full` should be the normal default because progressive discovery means installed skills do not need to be loaded into every prompt.

Key rule:

> Installed != active != loaded into context.

## Role bundles

Role bundles are compositions, not giant persona prompts.

Examples:

- Executive Assistant
- Project Manager
- Marketing Manager
- Social Media Manager
- Creative Director
- AI Filmmaker
- Film Producer
- Post Producer
- Sales Representative
- Account Manager
- Customer Support Agent
- Finance Analyst
- Research Analyst
- HR Coordinator

A role can select professional skills plus software Operator Packs. The underlying original skills remain reusable outside the role.

## Operator Packs

Professional skill and application access are separate.

Examples:

- `social-content` is a professional skill
- Canva, Meta Business Suite, TikTok Studio and YouTube Studio are operators/connections

- `financial-analysis` is professional capability
- Excel, Xero and QuickBooks are operators

- editing and post-production are professional capabilities
- Premiere Pro, DaVinci Resolve, After Effects and FFmpeg are operators

This separation keeps the skill portable when a company uses a different software stack.

## Registry responsibilities

`registry/skills.json` is the canonical 100-capability catalog:

- 20 AI-Verse Machine / Reliability Foundation capabilities
- 80 researched employee-facing capabilities

Each employee skill records:

- canonical ID
- rank
- category
- source namespace
- upstream repository
- upstream package path when already resolved
- implementation type
- package state
- preferred installation strategy

`registry/sources.json` defines the approved source namespaces and repositories.

Later registry files will add:

- aliases
- roles
- operator dependencies
- exact pinned upstream revisions
- content hashes
- license records
- dependency metadata
- adapter compatibility
- readiness state

## Package states

The installer and registry should distinguish at least:

- `vendored`: complete original package is physically present in this repository
- `upstream-fetch`: installer retrieves the original pinned package
- `catalogued`: source selected but package import is not complete yet
- `first-party`: AI-Verse-authored package
- `disabled`: known package intentionally excluded from install
- `dormant`: installed but required software/connection is unavailable
- `ready`: installed and executable with current dependencies

## Day-0 dependency behavior

Missing optional software must not make the whole installation fail.

Example:

```text
email-inbox-triage   READY
ffmpeg-skill         READY
premiere-agent       DORMANT
hubspot-sales        DORMANT
blender-3d           DORMANT
```

Connecting software later should promote the capability to `READY` without reinstalling the skill distribution.

## Runtime discovery

The installer should eventually detect supported runtimes such as:

- AI-Verse OS
- Claude Code
- Codex
- Hermes
- OpenClaw
- Gemini CLI
- other Agent Skills-compatible runtimes

AI-Verse OS gets the deepest adapter first.

## AI-Verse OS integration

Generic runtime:

```text
User
-> skill resolver
-> original SKILL.md
-> runtime tools
```

AI-Verse OS:

```text
User
-> AI-Verse OS
-> workspace/context/memory/Brain/connections/policy
-> AI-Verse skill resolver
-> relevant original skills
-> relevant operators
-> execution
-> verification
-> OS-controlled write-back
```

The Skills repository does not take over workspace identity, memory authority, secret storage, approval policy or cadence.

## Progressive discovery

A 100-skill install must not inject 100 full skill bodies into every prompt.

Discovery should happen in layers:

1. compact registry metadata
2. ranked candidate skills
3. selected `SKILL.md`
4. supporting references/scripts only when required
5. relevant tool/operator schemas only when required

This keeps the architecture viable at 100, 500 or thousands of installed capabilities.

## Collision handling

Different ecosystems will contain overlapping names and workflows.

Do not arbitrarily rewrite upstream package names.

Instead the registry owns canonical capability mapping.

Example:

```text
canonical capability: document-authoring

implementations:
- anthropic/docx
- hermes/docx

preferred implementation:
- selected by distribution policy/evals
```

Aliases should resolve user language without destroying source identity.

## Update model

Every imported/fetched package should eventually be pinned by:

- upstream repository
- upstream path
- upstream commit/tag
- file/package content hash
- imported timestamp

Planned command:

```bash
aiverse-skills update
```

Updates must be diffed and admitted rather than silently replacing trusted skill code.

## Health check

Planned command:

```bash
aiverse-skills doctor
```

It should check:

- catalog integrity
- missing packages
- broken references
- hash/provenance mismatches
- duplicate canonical IDs
- optional dependencies
- runtime adapters
- AI-Verse OS integration
- upstream updates
- dormant vs ready capabilities

## Implementation sequence

### Slice A - current

1. Lock permanent package layout.
2. Create source/provenance registry.
3. Create canonical 100-skill registry.
4. Preserve the full research and install architecture in-repo.
5. Start vendoring original packages from approved sources.

### Slice B

1. Resolve exact upstream path for every one of the 80.
2. Verify source/package licenses.
3. Import all redistributable original packages with complete supporting files.
4. Mark source-linked originals for pinned install-time fetch.
5. Record exact source commits and hashes.

### Slice C

1. Package the 20 AI-Verse foundation capabilities.
2. Build collision/alias maps.
3. Create role bundles.
4. Create Operator Pack catalog.

### Slice D

1. Build universal installer.
2. Build runtime detection.
3. Build AI-Verse OS adapter first.
4. Add generic Agent Skills adapter.
5. Add Claude, Codex, Hermes, OpenClaw and Gemini adapters as needed.

### Slice E

1. Add dependency resolver.
2. Add `doctor`.
3. Add update/uninstall.
4. Add clean-machine install tests.
5. Run a zero-to-100 fresh-agent acceptance test.

## Acceptance test

The distribution is successful when a fresh machine can install AI-Verse-Skills once and a supported agent can immediately discover professional capabilities without manually copying skill folders.

For AI-Verse OS, the stronger test is:

> Give a fresh AI-Verse agent a company workspace, connections and permissions, then verify it can discover and perform useful work across multiple departments before any custom company-specific skills are created.
