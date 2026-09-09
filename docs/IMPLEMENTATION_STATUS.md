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
- native AI-Verse OS integration
- AI-Verse OS managed integration manifest
- lightweight CI
- full E2E install workflow
- durable project/research documentation

## Canonical acquisition state

`registry/packages.json` is authoritative for how the 80 employee skills are acquired.

- Six proof packages are physically vendored.
- The other selected employee packages are pinned upstream-fetch packages.
- The 20 AI-Verse foundation packages are physically implemented under `skills/foundation/`.

## User-required steps

Repository automation cannot create third-party OAuth/app access on a user's behalf.

After installation, a user may still need to:

- connect Google Workspace
- connect Canva
- connect Figma
- connect HubSpot
- connect Shopify
- connect Airtable
- connect Notion
- install/authorize Premiere Pro
- install/authorize After Effects
- install FFmpeg
- provide a host runtime with browser/computer-use where required

Use `ai-verse-skills readiness` to see what is missing on a specific machine.
