# Shipping Status

**Snapshot:** 2026-09-09

## Release standard

AI-Verse-Skills is considered shippable only when all of the following are true:

1. Registry validation passes.
2. All 20 foundation packages exist.
3. All 80 employee capabilities have a pinned acquisition record.
4. A full clean install can materialize 100 canonical capabilities.
5. `doctor` verifies every installed package digest.
6. AI-Verse OS integration exposes all 100 capabilities to both `.claude/skills/` and `.agents/skills/`.
7. Update is transactional and creates a rollback point.
8. Rollback restores the previous verified library.
9. Operator readiness reports unavailable software/connections instead of pretending every skill is executable.
10. CI contains a full networked E2E install test in addition to lightweight validation.

## Distribution model

The distribution is original-first.

- AI-Verse foundation skills are shipped directly from this repository.
- Redistributable proof imports can be vendored.
- Other selected employee skills are fetched from their exact pinned upstream revision.
- The installer copies the complete selected skill package directory, not only `SKILL.md`.
- Installed package digests are recorded in `.aiverse/installed.json`.

## Safety boundary

Installation grants no permissions.

The host runtime owns:

- filesystem/workspace scope
- secrets
- app connections
- browser/computer-use authority
- approvals
- memory authority
- cadence/scheduling
- durable write-back

## Release verification

Lightweight:

```bash
python scripts/validate_registry.py
python installer/aiverse_skills.py install --profile full --dry-run
```

Full local verification:

```bash
python installer/aiverse_skills.py install --profile full --root /tmp/aiverse-skills-e2e
python installer/aiverse_skills.py doctor --root /tmp/aiverse-skills-e2e
```

AI-Verse OS verification:

```bash
python installer/aiverse_skills.py install --profile full \
  --root /tmp/aiverse-skills-e2e \
  --aiverse-os /path/to/AI-Verse-OS
python installer/aiverse_skills.py doctor \
  --root /tmp/aiverse-skills-e2e \
  --aiverse-os /path/to/AI-Verse-OS
python installer/aiverse_skills.py e2e \
  --root /tmp/aiverse-skills-e2e \
  --aiverse-os /path/to/AI-Verse-OS
```
