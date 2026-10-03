# MANUAL CAMERA Workflow

Status: RUNTIME WORKFLOW
Task: 6.5

Purpose: let an expert specify any subset of camera, lens, focal, aperture, angle, framing, lighting, stock, grade, or other technical choices while AUTO intelligently fills only what remains unspecified.

## Entry
Use when the user supplies explicit technical capture choices or asks to work in manual/pro camera mode.

## Governing rule

```text
explicit user value = LOCK
unspecified compatible value = AUTO
```

Never silently improve, replace, normalize, or reinterpret a lock merely because another combination would be more conventional.

## Procedure
1. Parse every explicit technical choice into a field-level parameter state.
2. Mark hard user values `user_supplied + locked` and preservation requirements `preservation_supplied + locked`.
3. Distinguish literal hardware/reference names from requested observable behavior.
4. Run conflict classification before AUTO completion:
   - C0 compatible;
   - C1 tension but reconcilable;
   - C2 direct contradiction;
   - C3 provider execution conflict.
5. For C1, solve through unlocked fields first: camera distance, subject/background spacing, focus plane, lighting fill, exposure, framing, or other AUTO choices.
6. For C2, preserve the locks and explain the consequence or required tradeoff; do not claim full success if all locked outcomes cannot coexist.
7. Fill missing shot decisions from story/intent using Phase 3-5 runtime knowledge.
8. Keep perspective tied to camera position, not focal-length mythology.
9. Keep aperture/depth, lens family/focal length, capture response/grade, and stock/grain/halation/flare as separate systems.
10. Build the complete Cinematic Shot Spec with explicit provenance for locked vs inferred values.
11. Run Reality Gate V0, treating deliberate user locks as constraints rather than defects unless they create an impossible requested outcome.
12. Adapt to provider controls. Native controls may encode locks directly; unsupported controls require semantic translation and must be listed as unsupported/translated.
13. If the user requested prompt only, never auto-generate. If image execution was requested and available, execute; otherwise provide the adapted prompt/spec.
14. If output is inspectable, run V2 and verify locks before judging general aesthetics.

## Canonical conflicts

### 14mm + no fisheye / clean rectilinear background
Compatible when the user means rectilinear projection. Keep 14mm locked and control camera position/composition; do not substitute a longer lens.

### f/1.2 + deep focus across a large scene
Potential C1/C2 depending geometry. Keep f/1.2 locked; increase subject/background distance relationships, focus placement, or camera distance where possible. If the requested depth remains physically contradictory, surface the limitation.

### 65/70mm reference + VHS artifacts
These can coexist when capture-scale intent and downstream/finish artifacts are treated as separate axes. Do not reject an unusual combination merely because it is unconventional.

## Expert behavior
Do not explain basic camera theory unless requested. Return concise decisions and consequences. Precision must not become verbosity.

## Output
A successful manual workflow preserves every feasible lock, fills only missing values, exposes genuine contradictions/provider limitations, and maintains one coherent physical shot model.

A result that looks good but silently changed a locked focal length, lens, aperture, framing, camera angle, or preservation requirement is failure.