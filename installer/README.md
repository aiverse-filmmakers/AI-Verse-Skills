# Installer

`aiverse_skills.py` is the stable entrypoint for the AI-Verse Skills distribution installer.

Package bytes are committed into immutable generations under `<root>/.aiverse/generations/`. `active.json` is the single atomic activation pointer. `install`, `update`, `rollback`, and `uninstall` are serialized by a lifecycle lock.

Useful commands:

```bash
./aiverse-skills install
./aiverse-skills update
./aiverse-skills doctor
./aiverse-skills pin --json
./aiverse-skills rollback
./aiverse-skills uninstall
./aiverse-skills adapt --runtime codex --target ~/.codex/skills
./aiverse-skills adapter-verify --target ~/.codex/skills
```

A host must pin one generation before reading `SKILL.md` or any supporting script and keep using that generation for the entire execution.

See `docs/IMMUTABLE_GENERATIONS.md`.
