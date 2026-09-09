# Implementation Status

**Snapshot:** 2026-09-09

## Locked decisions

- The original 20 Machine / Reliability capabilities remain part of the 100-capability foundation.
- The researched top 80 employee skills are additive to those 20.
- Original upstream skills are preferred over AI-Verse rewrites.
- `skills/imported/ai-verse/` is permanently reserved for future AI-Verse-authored skills.
- Canonical local install target is planned as `~/.aiverse/skills/`.
- One canonical installed library will be exposed to multiple agents through adapters.
- AI-Verse OS remains the authority for workspace scope, memory, secrets, permissions, cadence and durable write-back.
- Role bundles compose skills. They do not replace the underlying skill library with giant personas.
- Operator Packs are separate from professional capability skills.
- Full installation is the intended default for AI-Verse OS because discovery is progressive.

## Current slice

Completed or being committed in this slice:

- permanent source namespace structure
- source registry
- canonical 100-skill registry
- original-upstream import policy
- distribution/install architecture documentation
- first original vendored packages from Google, Hermes and LifeOS

## Import progress

Initial proof imports:

- Google `persona-exec-assistant`
- Hermes `email-inbox-triage`
- LifeOS `Council` complete package

These prove the distribution can preserve different upstream package styles without flattening them into one custom format.

The remaining researched employee skills stay catalogued until their exact package paths, complete file trees and provenance are resolved in the next import pass.

## Next slice

- resolve all remaining exact upstream package paths
- verify license state source-by-source
- vendor all directly redistributable original packages
- configure pinned upstream fetch for originals that should remain at source
- complete commit/hash provenance
- update registry package states from `catalogued` to `vendored` or `upstream-fetch`
