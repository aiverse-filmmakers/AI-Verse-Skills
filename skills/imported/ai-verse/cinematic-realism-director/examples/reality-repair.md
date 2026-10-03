# Example - REALITY REPAIR

This example demonstrates preservation-aware repair. It is not a hidden mandatory template.

## User

```text
Make this portrait look less AI-generated. Keep the person's identity, pose, hairstyle, clothes, framing and background exactly the same.
```

## Routing

```text
workflow = REALITY REPAIR
actual target image required for visual diagnosis/editing
```

## Preservation Boundary

```text
PRESERVE
- identity
- facial proportions
- expression
- pose
- hairstyle and length
- wardrobe
- framing / camera position
- background layout
```

Only evidence-supported realism failures should enter `REPAIR`.

## Example Diagnosis

Assume visual inspection finds:

- waxy uniform skin with specular response inconsistent with the key light;
- flyaway strands disconnected from the main hair mass;
- catchlights that do not correspond to the scene's light source;
- coat fabric with arbitrary folds and plastic roughness;
- weak contact shadow where the subject meets the seat.

Do **not** diagnose unrelated features merely because the image is AI-generated.

## Repair Plan

```text
REPAIR
1. restore region-specific skin texture and source-consistent highlights without changing identity or age;
2. reconnect stray hair to believable root/mass/gravity behavior while preserving hairstyle and length;
3. make eye catchlights consistent with the actual source geometry;
4. restore coat material roughness, weight and fold causality;
5. strengthen only the physically required seat/body contact shadow.

ALLOW CHANGE
- local microtexture
- local specular response
- physically inconsistent flyaways
- catchlight geometry
- fabric fold/roughness details
- contact shadow density
```

## Example Edit Instruction

```text
Preserve the person's identity, facial proportions, expression, pose, hairstyle and hair length, wardrobe design, framing, camera viewpoint, background, and overall lighting setup.

Repair only the realism failures: restore natural region-specific skin texture with subtle tonal variation and highlights that follow the existing key light; remove/reconnect only physically impossible floating flyaways while keeping the same hairstyle; correct eye catchlights so they match the visible source; make the coat read as real fabric through weight-driven folds and material-appropriate roughness; restore the missing contact shadow at the seat/body junction.

Do not beautify, age, reshape, relight, recompose, restyle, add grain, add haze, add flare, change depth of field, or redesign the scene.
```

## Verification

A successful repair requires:

- all preservation locks unchanged;
- targeted failures corrected;
- no whole-scene style drift;
- no new anatomy/material/light inconsistencies;
- V2 visual inspection before claiming the repaired image looks correct.

If the target image is unavailable to the active host, return the repair specification instead of pretending the edit occurred.
