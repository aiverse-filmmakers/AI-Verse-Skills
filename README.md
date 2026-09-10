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
- immutable-generation install, update, rollback and uninstall lifecycle
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

Installed package bytes live in immutable generations beneath that root. The active generation is selected by one atomic pointer rather than by replacing a live package tree.

## Install

### Standalone

```bash
git clone https://github.com/aiverse-filmmakers/AI-Verse-Skills.git
cd AI-Verse-Skills
./aiverse-skills install
./aiverse-skills doctor --readiness
```

### AI-Verse OS integration status

The agreed [provider v1 contract and implementation mapping](docs/AI_VERSE_OS_INTEGRATION.md) defines external discovery without copying packages into OS. The current OS CLI does not yet expose `ai-verse-os skills` commands, and this installer does not yet emit the v1 capability index. Use the standalone commands above today.

OS installation remains independent and never implicitly installs this distribution.

## Immutable generation safety

`install` and `update` build a complete profile in staging, verify it, commit it under:

```text
~/.aiverse/skills/.aiverse/generations/<generation-id>/
```

and then atomically replace only:

```text
~/.aiverse/skills/.aiverse/active.json
```

The previous generation is retained unchanged. `rollback` switches that pointer back; `uninstall` deactivates the library without deleting generation bytes that an in-flight execution may still be using.

Lifecycle mutations are serialized with a per-install lock so install, update, rollback and uninstall cannot interleave.

```bash
./aiverse-skills update
./aiverse-skills rollback
./aiverse-skills uninstall
```

A runtime must pin the active generation before loading a skill or one of its helper scripts:

```bash
./aiverse-skills pin --json
./aiverse-skills pin --package document-authoring --json
```

Once pinned, use the returned generation path for the entire execution. Never resolve `SKILL.md` from one active generation and a later script from another.

See [`docs/IMMUTABLE_GENERATIONS.md`](docs/IMMUTABLE_GENERATIONS.md).

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

The current report provides dependency hints. It does not verify workspace access or authorize actions; the provider v1 contract separates these host-owned checks from package readiness.

## Original-first policy

Strong upstream skills are kept original. AI-Verse does not rewrite them merely for branding.

The distribution records:

- upstream repository
- pinned revision
- upstream package path
- acquisition mode
- operator dependencies
- local content digest after installation
- immutable generation ID and generation digest

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

Each adapter manifest is bound to the generation it materialized. If the canonical active generation changes, a copied adapter becomes stale and must not be treated as current until refreshed. Check it with:

```bash
./aiverse-skills adapter-verify --target ~/.codex/skills
```

`--allow-stale` verifies that an older adapter still matches its own immutable generation without claiming it is current.

The planned AI-Verse OS integration uses external discovery and does not materialize the distribution inside the OS repository. See the provider contract for implementation status.

## Important design rule

> Installed != active != loaded into context.

A host should discover skill metadata progressively and load only skill bodies relevant to the current task.

## Validation

Normal CI validates registry integrity, generation-lifecycle adversarial tests and full-profile planning.

The full E2E workflow performs a real pinned upstream install and verifies all package digests. It pins an execution generation, creates a copied adapter, updates the distribution, proves the old execution remains complete, rejects the now-stale adapter, rolls back to the exact previous generation, uninstalls without deleting pinned bytes, and recovers the installation.

See:

- `docs/IMMUTABLE_GENERATIONS.md`
- `docs/SHIPPING.md`
- `docs/AI_VERSE_OS_INTEGRATION.md`
- `docs/PROJECT_STATE.md`
- `research/2026-09-top-80-existing-employee-skills.md`
- `research/2026-09-agent-capability-landscape.md`
