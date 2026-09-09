# Implementation Status

**Snapshot:** 2026-09-09

## Implemented

- permanent imported-source namespaces, including reserved `ai-verse/`
- 20 first-party foundation skill packages
- 80 employee skill acquisition records
- exact pinned source revisions
- complete-package acquisition
- support dependency catalog
- operator catalog
- role bundles
- installation profiles
- runtime adapter catalog
- transactional install
- transactional update
- rollback
- integrity doctor
- operator readiness
- safe uninstall with recoverable backup
- generic runtime adaptation
- external-only AI-Verse OS compatibility contract
- lightweight CI
- full E2E external install workflow
- durable project/research documentation

## Canonical acquisition state

`registry/packages.json` is authoritative for how the 80 employee skills are acquired.

- Six proof packages are physically vendored.
- The other selected employee packages are pinned upstream-fetch packages.
- The 20 AI-Verse foundation packages are physically implemented under `skills/foundation/`.

## Separation guarantee

AI-Verse-Skills does not copy or symlink its packages into AI-Verse OS.

AI-Verse OS installation does not automatically install AI-Verse-Skills. The optional distribution requires a separate explicit command.

## User-required steps

Repository automation cannot create third-party OAuth/app access on a user's behalf.

After installation, a user may still need to connect or install Google Workspace, Canva, Figma, HubSpot, Shopify, Airtable, Notion, Premiere Pro, After Effects, FFmpeg, and/or a host browser/computer-use capability.

Use `ai-verse-skills readiness` to see what is missing on a specific machine.
