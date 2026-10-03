# Cinematic Realism Director - Source Ledger Addendum

Status: PHASE 1 PROVENANCE ADDENDUM

Retrieval date: 2026-10-03

This file records authoritative sources discovered after the initial `source-ledger.md` snapshot. It is part of the Phase 1 provenance record and should be read together with `source-ledger.md`.

Future consolidation may merge these entries into the primary ledger without changing their evidence class.

| ID | Source | Authority | Class | Supports | Notes |
| --- | --- | --- | --- | --- | --- |
| COLOR-ACES-001 | https://docs.acescentral.com/ | Academy / ACES official documentation | CONFIRMED | ACES as production color-management framework, scene-to-output separation | Standards/official project source |
| COLOR-ACES-002 | https://docs.acescentral.com/background/about-rendering/ | ACES official documentation | CONFIRMED | ACES 2 rendering goals: gentler highlight rolloff, hue preservation, gamut mapping, clipping reduction | Useful for display-independent tonal principles |
| COLOR-ACES-003 | https://docs.acescentral.com/system-components/output-transforms/technical-details/tone-mapping/ | ACES official technical documentation | CONFIRMED | Tone scale / shoulder-toe / display mapping concepts | Do not turn exact transform math into provider prompt syntax |
| COLOR-ACES-004 | https://docs.acescentral.com/system-components/output-transforms/technical-details/chroma-compression/ | ACES official technical documentation | CONFIRMED | Hue-preserving colorfulness compression concepts | Supports saturation/highlight discipline |
| LEN-LEITZ-001 | https://www.leitz-cine.com/product/summilux-c | Leitz Cine first-party | CONFIRMED | SUMMILUX-C clarity, color, contrast, low distortion/CA/breathing, warm natural skin, gentle focus rolloff | Manufacturer qualitative language translated cautiously |
| LEN-MP-001 | https://www.arri.com/en/cine-lenses/arri-zeiss-fujinon-lenses/master-primes/master-primes | ARRI first-party | CONFIRMED | Master Prime T1.3 family, resolution/contrast, low distortion, reduced flare, near-zero breathing | Primary optical-family source |
| LEN-MP-002 | https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/arrizeiss.html | ZEISS first-party | CONFIRMED | ARRI/ZEISS Master Prime performance and breathing behavior | Cross-first-party corroboration |
| MODEL-SEED-004 | https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro-editing-guide | BytePlus/ModelArk first-party Seedream documentation | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Seedream 5.0 Pro/Flash point/bounding-box spatial editing and explicit unchanged regions | Version/API specific |
| MODEL-BFL-004 | https://github.com/black-forest-labs/skills/blob/master/skills/flux-image-best-practices/SKILL.md | Black Forest Labs official GitHub | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Official FLUX prompt structure, positive-description rule, model-specific editing/prompting practices | Recheck before adapter release |
| MODEL-BFL-005 | https://docs.bfl.ml/ | Black Forest Labs official docs | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Current FLUX family overview and prompting documentation index | Model surface changes over time |
| MODEL-OAI-003 | https://developers.openai.com/api/docs/guides/image-generation | OpenAI first-party docs | MODEL-BEHAVIOR / PROVIDER-SPECIFIC | Current GPT Image generation/editing surface, Sunburst/Flare model variants, Responses/Image API routing, output controls | Rechecked on 2026-10-03; model names and parameters are version-sensitive |

## Addendum Rule

Entries in this addendum have the same authority semantics as entries in `source-ledger.md`.

A later runtime reference must still:

- paraphrase rather than copy substantial source text;
- distinguish manufacturer marketing language from measured physics;
- keep provider behavior provider-specific;
- preserve retrieval/version sensitivity;
- avoid using an addendum entry as evidence for unrelated claims.
