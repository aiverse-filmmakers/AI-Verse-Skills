# Native AI-Verse OS Integration

## Goal

AI-Verse-Skills remains a standalone distribution, while AI-Verse OS receives a first-class capability surface without duplicating authority or canonical user state.

## Canonical locations

Skill library:

```text
~/.aiverse/skills/
```

AI-Verse OS managed integration manifest:

```text
<OS>/runtime/skills/ai-verse-skills.json
```

Runtime surfaces:

```text
<OS>/.claude/skills/
<OS>/.agents/skills/
```

The integration manifest is derived/disposable. The canonical installed package manifest is:

```text
~/.aiverse/skills/.aiverse/installed.json
```

## Install

From AI-Verse OS:

```bash
./ai-verse-os skills install
```

The OS helper finds or acquires the AI-Verse-Skills repository and invokes:

```bash
aiverse-skills install --profile full --aiverse-os <OS_ROOT>
```

The installer:

1. resolves the full profile,
2. fetches exact pinned upstream revisions,
3. copies complete skill packages into a staging library,
4. computes package digests,
5. verifies the staged library,
6. atomically replaces the canonical library,
7. keeps the previous library as a rollback point,
8. exposes canonical packages to Claude and Codex OS surfaces,
9. records only the integration mapping under `runtime/`.

## Collision policy

The installer never silently overwrites an unmanaged OS skill.

A destination may be replaced automatically only when the previous AI-Verse-Skills integration manifest says it is managed by this distribution.

`--force-os` exists for deliberate collision takeover.

## Updates

```bash
./ai-verse-os skills update
```

An update is a fresh transactional materialization from the distribution's current pinned registry. Existing symlinked OS surfaces keep pointing at the stable canonical root.

## Rollback

```bash
./ai-verse-os skills rollback
```

Rollback swaps the active library with the newest rollback point and refreshes OS integration state.

## Readiness

```bash
./ai-verse-os skills readiness
```

Installed skills are split into:

- immediately ready
- conditional on an app
- conditional on a connection
- conditional on host runtime features

This is deliberately separate from installation.

## Authority boundary

AI-Verse-Skills can describe requested tools and workflows. It cannot grant itself:

- another workspace
- credentials
- connection access
- browser/computer-use
- external side effects
- memory write authority
- scheduling

AI-Verse OS remains the authority for all of those.
