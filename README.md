# AI-Verse-Skills

A curated, original-first professional skill distribution for AI agents, with first-class compatibility with AI-Verse OS while remaining a completely separate repository and installation.

## What it ships

- **20 AI-Verse Machine / Reliability skills**
- **80 researched employee-facing skills** sourced from strong existing ecosystems
- **100 canonical capabilities total**
- support dependencies
- Role Bundles
- Operator Packs
- install profiles
- runtime adapters
- transactional install, update and rollback
- integrity doctor and operator-readiness reporting

The goal is an AI worker that can become useful across a real company from Day 0: executive assistance, operations, research, marketing, social, design, filmmaking, post-production, sales, CRM, support, finance, product, HR, legal coordination and technical work.

Coding is one department, not the identity of the agent.

## Repository separation rule

AI-Verse-Skills and AI-Verse OS remain independent.

- Installing AI-Verse OS does **not** install AI-Verse-Skills.
- Installing AI-Verse-Skills does **not** copy, symlink or vendor skills into the AI-Verse OS repository.
- AI-Verse OS does not get copied into this repository.
- The optional integration is reference/discovery based.

Canonical Skills install root:

```text
~/.aiverse/skills/
```

## Install

### Standalone

```bash
git clone https://github.com/aiverse-filmmakers/AI-Verse-Skills.git
cd AI-Verse-Skills
./aiverse-skills install
./aiverse-skills doctor --readiness
```

### Optional command through AI-Verse OS

AI-Verse OS exposes a convenience command, but it is deliberately separate from OS installation:

```bash
ai-verse-os install
```

installs **only AI-Verse OS**.

Later, only if the user explicitly wants the skill distribution:

```bash
ai-verse-os skills install
```

That command installs AI-Verse-Skills externally under `~/.aiverse/skills/`. It does not modify the OS repository with skill packages.

Other lifecycle commands:

```bash
ai-verse-os skills doctor
ai-verse-os skills readiness
ai-verse-os skills update
ai-verse-os skills rollback
ai-verse-os skills uninstall
```

## Transaction safety

`install` and `update` build the complete requested profile in a staging directory first. The staged library is verified before the active library is replaced. The previous install becomes a rollback point.

```bash
./aiverse-skills update
./aiverse-skills rollback
```

## Readiness is not installation

A professional skill can be installed while its required software is unavailable.

Examples:

- Figma skills need Figma access.
- HubSpot skills need HubSpot access.
- Canva skills need Canva/browser access.
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

Future AI-Verse-authored employee skills belong only in:

```text
skills/imported/ai-verse/
```

Third-party work never goes there.

## Runtime compatibility

Generic agents can explicitly adapt the external library into a runtime-owned skill directory when desired:

```bash
./aiverse-skills adapt --runtime claude --target ~/.claude/skills
./aiverse-skills adapt --runtime codex --target ~/.codex/skills
./aiverse-skills adapt --runtime hermes --target ~/.hermes/skills
```

AI-Verse OS is intentionally different: it references/discovers the external library directly and does not materialize the distribution inside the OS repository.

## Important design rule

> Installed != active != loaded into context.

A host should discover skill metadata progressively and load only skill bodies relevant to the current task.

## Validation

Normal CI validates registry integrity and full-profile planning.

A full E2E workflow performs a real full-profile pinned upstream install, verifies all package digests, exercises transactional update and rollback, and confirms the full profile contains all 100 canonical capabilities.

See:

- `docs/SHIPPING.md`
- `docs/AI_VERSE_OS_INTEGRATION.md`
- `docs/PROJECT_STATE.md`
- `research/2026-09-top-80-existing-employee-skills.md`
- `research/2026-09-agent-capability-landscape.md`
