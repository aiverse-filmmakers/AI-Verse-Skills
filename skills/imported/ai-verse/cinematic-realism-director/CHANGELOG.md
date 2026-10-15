# Changelog

## 1.1.0 — 2026-10-04

### Changed

- Added a mandatory **Professional Quality Floor** so one-line prompts receive the strongest professional execution appropriate to the requested medium without requiring `professional`, `cinematic`, `Hollywood`, `ARRI`, or similar quality keywords.
- Added medium-aware professional direction for mobile/selfie, candid/documentary, narrative/cinematic, portrait, fashion, product, automotive, food, architecture, travel and hospitality imagery.
- Changed default image execution to **native/local first** unless the user explicitly locks a provider or native execution lacks a material required capability.
- External MCP/plugin/connector image tools are now fallback execution surfaces rather than quality-preference routes.
- Magnific Cinematic and Higgsfield Soul Cinema are now **explicit-target / benchmark-only** adapters and are never automatic backends for ordinary image requests.
- Added premium default cinema DNA for narrative/general photographic AUTO: controlled highlight rolloff, rich readable shadows, professional color separation, natural skin/material response, realistic optical falloff and restrained high-end grading.
- Added ARRI-like highlight/skin response as an observable tonal target for appropriate cinematic work without claiming literal ARRI capture/simulation.
- Changed subtle organic filmic texture to the normal finishing baseline for most photographic/cinematic output while keeping strong grain, halation, flare, haze, rim light and other visible effects optional.
- Preserved anti-cliche safeguards so professional finish does not become a fixed teal/orange/anamorphic/haze/shallow-DOF preset.

### Added

- `references/professional-quality-floor.md`
- `references/execution-priority.md`
- professional mobile/selfie and candid examples
- dedicated Professional Quality Floor evals
- dedicated native-first execution-priority evals
- permanent regressions for native-before-MCP routing, competitor-backend leakage, missing professional quality, medium drift and sterile anti-cliche output

## 1.0.0 — 2026-10-03

Initial public release of **AI-Verse Cinematic Realism Director**.

### Added

- Beginner-first **AUTO DIRECT** workflow from one-sentence prompts.
- Expert **MANUAL CAMERA** workflow with explicit technical locks.
- **CINEMATIZE**, **REALITY REPAIR**, **REFERENCE MATCH**, and **PROMPT ONLY** workflows.
- Provider-neutral Cinematic Shot Spec, realism diagnosis, and reference-DNA schemas.
- Cinematography knowledge for composition, capture formats, lens character, focal length/perspective, aperture/depth, and still-frame motion.
- Motivated-lighting, exposure, film/sensor response, color, texture, and physical-realism systems.
- Reusable Reality Gate for photographic plausibility and anti-AI verification.
- Provider translation adapters and standalone Agent Skill operation.
- Behavioral, regression, adversarial, physical-plausibility, and provider-consistency evaluation coverage.

### Core Invariants

- Explicit user values remain locks.
- AUTO fills only missing decisions.
- Provider syntax stays downstream of universal image design.
- Perspective is not inferred from focal length alone.
- Reference observations are not exact hardware facts without evidence.
- Preserve before transforming.
- Tool/API success is not visual verification.
