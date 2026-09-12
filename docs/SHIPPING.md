# Shipping Status

> Provider integration status: [Capability Provider Contract v1](AI_VERSE_OS_INTEGRATION.md) is implemented. New immutable generations publish manifest schema 3 plus a bound capability index, and AI-Verse OS consumes the external provider directly. Skills remains a separate installation and lifecycle.

**Snapshot:** 2026-09-09

## Release standard

AI-Verse-Skills is considered shippable only when all of the following are true:

1. Registry validation passes.
2. All 20 foundation packages exist.
3. All 80 employee capabilities have a pinned acquisition record.
4. A full clean install can materialize 100 canonical capabilities under the external Skills root.
5. `doctor` verifies every installed package digest.
6. Update is transactional and creates a rollback point.
7. Rollback restores the previous verified library.
8. Operator readiness reports unavailable software/connections instead of pretending every skill is executable.
9. AI-Verse OS can discover/reference the external Skills installation without copying or symlinking skill packages into the OS repo.
10. Installing AI-Verse OS alone never installs AI-Verse-Skills.
11. CI contains a full networked E2E install test in addition to lightweight validation.

## Distribution model

The distribution is original-first.

- AI-Verse foundation skills are shipped directly from this repository.
- Redistributable proof imports can be vendored.
- Other selected employee skills are fetched from their exact pinned upstream revision.
- The installer copies the complete selected skill package directory, not only `SKILL.md`.
- Installed package digests are recorded in `.aiverse/installed.json`.

## Repository isolation

The Skills installer writes only to its own external installation/cache/tool locations unless the user explicitly invokes a generic runtime adapter with a target they chose.

AI-Verse OS compatibility does not use such an adapter. The OS references the external library directly.

## Safety boundary

Installation grants no permissions.

The host runtime owns filesystem/workspace scope, secrets, app connections, approvals, memory authority, cadence and durable write-back.

## Release verification

```bash
python scripts/validate_registry.py
python installer/aiverse_skills.py install --profile full --dry-run
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e install --profile full
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e doctor
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e e2e
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e update
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e rollback
python installer/aiverse_skills.py --root /tmp/aiverse-skills-e2e e2e
```
