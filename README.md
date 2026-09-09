# AI-Verse-Skills

A curated, original-first professional skill distribution for AI agents, with native integration for AI-Verse OS.

## What it ships

- **20 AI-Verse Machine / Reliability skills**
- **80 researched employee-facing skills** sourced from strong existing ecosystems
- **100 canonical capabilities total**
- 5 support dependency packages
- Role Bundles
- Operator Packs
- install profiles
- runtime adapters
- transactional install, update and rollback
- integrity doctor and operator-readiness reporting

The goal is an AI worker that can become useful across a real company from Day 0: executive assistance, operations, research, marketing, social, design, filmmaking, post-production, sales, CRM, support, finance, product, HR, legal coordination and technical work.

Coding is one department, not the identity of the agent.

## Fastest install

### AI-Verse OS

From the root of an AI-Verse OS checkout:

```bash
./ai-verse-os skills install
```

This installs the full distribution into `~/.aiverse/skills/`, then exposes the managed skill set to:

```text
<AI-Verse-OS>/.claude/skills/
<AI-Verse-OS>/.agents/skills/
```

AI-Verse OS remains authoritative for workspaces, context, permissions, secrets, connections, approvals, memory, cadence and durable write-back.

Useful commands:

```bash
./ai-verse-os skills doctor
./ai-verse-os skills readiness
./ai-verse-os skills update
./ai-verse-os skills rollback
./ai-verse-os skills uninstall
```

### Standalone / other agents

Clone the distribution and use the included CLI:

```bash
git clone https://github.com/aiverse-filmmakers/AI-Verse-Skills.git
cd AI-Verse-Skills
./aiverse-skills install
./aiverse-skills doctor --readiness
```

The default canonical install root is:

```text
~/.aiverse/skills/
```

For another runtime:

```bash
./aiverse-skills adapt --runtime claude --target ~/.claude/skills
./aiverse-skills adapt --runtime codex --target ~/.codex/skills
./aiverse-skills adapt --runtime hermes --target ~/.hermes/skills
```

The runtime remains responsible for its own permissions.

## Transaction safety

`install` and `update` build the complete requested profile in a staging directory first. The staged library is verified before the active library is replaced. The previous install is moved to a rollback point.

```bash
./aiverse-skills update
./aiverse-skills rollback
```

A failed staging or swap operation leaves the previous working installation recoverable.

## Readiness is not the same as installation

A professional skill can be installed while its external software is unavailable.

Examples:

- Figma skills need Figma access.
- HubSpot skills need a HubSpot CLI/connection.
- Canva skills need an authorized Canva/browser path.
- Premiere and After Effects skills need the local Adobe applications.
- FFmpeg needs `ffmpeg` and `ffprobe`.
- Google Workspace skills need the Google Workspace CLI or an authorized host connection.

Check the current machine:

```bash
./aiverse-skills readiness
```

The report separates skills that are immediately usable from skills waiting on an app, connection or host runtime.

## Original-first policy

Strong upstream skills are kept original. AI-Verse does not rewrite them merely for branding.

The distribution records:

- upstream repository
- pinned revision
- upstream package path
- acquisition mode
- operator dependencies
- local content digest after installation

Six proof packages are vendored directly. The remainder of the employee arsenal is acquired from pinned upstream revisions at install time. The 20 AI-Verse foundation skills are first-party.

Future AI-Verse-authored employee skills belong only in:

```text
skills/imported/ai-verse/
```

Third-party work never goes there.

## Architecture

```text
AI-Verse-Skills
├── registry/       canonical identities, sources, packages, roles, profiles, operators
├── skills/
│   ├── foundation/ 20 first-party reliability skills
│   └── imported/   vendored originals + reserved source namespaces
├── installer/      transactional installer and adapters
├── roles/          human-readable role bundle definitions
├── profiles/       installation profiles
├── operators/      software/operator documentation
├── adapters/       runtime integration notes
├── docs/           product and integration contracts
└── research/       preserved research and sourcing evidence
```

## Important design rule

> Installed != active != loaded into context.

A host should discover skill metadata progressively and load only the skill bodies relevant to the current task.

## Validation

Lightweight registry validation runs on normal CI.

A separate full E2E workflow performs a real full-profile upstream install, runs integrity checks, integrates a clean AI-Verse OS checkout, and verifies that both Claude and Codex surfaces expose all 100 canonical capabilities.

See:

- `docs/SHIPPING.md`
- `docs/AI_VERSE_OS_INTEGRATION.md`
- `docs/PROJECT_STATE.md`
- `research/2026-09-top-80-existing-employee-skills.md`
- `research/2026-09-agent-capability-landscape.md`
