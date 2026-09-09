# Native AI-Verse OS Compatibility

## Separation rule

AI-Verse-Skills and AI-Verse OS are separate repositories and separate installations.

AI-Verse-Skills must never:

- vendor AI-Verse OS files
- write skill packages into the AI-Verse OS repository
- create symlinks inside the AI-Verse OS repository
- make AI-Verse OS installation implicitly install the Skills distribution

AI-Verse OS may reference the external installed distribution when it exists.

## Canonical external location

```text
~/.aiverse/skills/
```

Canonical install manifest:

```text
~/.aiverse/skills/.aiverse/installed.json
```

AI-Verse OS can use that external manifest/root during capability discovery. No skill copy is required inside the OS repository.

## Explicit installation only

```bash
ai-verse-os install
```

installs only AI-Verse OS.

The optional Skills distribution is installed only by an explicit second command:

```bash
ai-verse-os skills install
```

That command acquires the separate AI-Verse-Skills tool checkout under the user's AI-Verse tools area and invokes its external installer.

## Lifecycle

```bash
ai-verse-os skills install
ai-verse-os skills update
ai-verse-os skills rollback
ai-verse-os skills doctor
ai-verse-os skills readiness
ai-verse-os skills list
ai-verse-os skills uninstall
```

All lifecycle state remains outside the OS repository.

## Capability discovery contract

When the external manifest exists, AI-Verse OS may treat its canonical packages as an additional capability catalog after the OS's own built-in capabilities.

Recommended discovery order:

1. identify scope and intent
2. consider built-in OS capabilities
3. if installed, inspect external AI-Verse-Skills metadata
4. select only the smallest relevant capability set
5. load only the required SKILL.md bodies/resources
6. execute under OS-owned permissions and workspace boundaries

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
