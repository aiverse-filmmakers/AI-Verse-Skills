# AUTO DIRECT Workflow

Status: RUNTIME WORKFLOW
Task: 6.1

Purpose: turn a minimal still-image idea into a complete cinematic shot without interrogating a beginner for camera knowledge.

## Entry
Use when the user supplies a subject, situation, or simple visual idea and has not requested strict manual camera control, reference matching, or repair of an existing image.

One sentence is sufficient.

## Governing rule

```text
user intent -> story priority -> shot design -> capture -> optics -> light -> exposure/color -> realism -> provider adaptation -> Reality Gate
```

Do not begin by choosing prestige camera/lens names.

## Procedure
1. Extract the literal subject, action, environment, mood/purpose, and any explicit constraints.
2. Convert every explicit technical or preservation choice into a lock.
3. Infer the viewer relationship and visual hierarchy using `visual-intent.md`.
4. Design composition and camera position before focal length.
5. Choose provider-neutral capture character. Named hardware is optional, never decorative.
6. Choose lens character, focal length, aperture, focus/depth, and still-motion behavior coherently.
7. Build lighting from plausible motivation, then fill/negative-fill/bounce/practicals only as needed.
8. Choose exposure hierarchy, white balance, grade, and optional capture/texture response.
9. Add physical-realism requirements appropriate to subject/material/environment.
10. Populate the Cinematic Shot Spec. Mark inferred choices as AUTO/inferred, not user supplied.
11. Run the Reality Gate at V0 before output/adaptation.
12. Adapt to the active provider/host only after the universal shot is coherent.
13. If a usable image tool exists and the user asked for an image, generate. Otherwise return the strongest adapted prompt/spec. Never pretend generation occurred.
14. If output can be visually inspected, run the Reality Gate again at V2 and repair only material failures.

## Beginner behavior
Do not ask about camera, lens, aperture, film stock, lighting ratio, white balance, grain, or grade unless an unresolved choice materially changes the requested result and cannot be safely inferred.

AUTO must prefer coherent ordinary photographic decisions over conspicuous cinematic effects.

## Anti-cliche defaults
AUTO does not automatically add:
- shallow DOF;
- anamorphic flare;
- grain;
- halation;
- haze;
- rim light;
- teal/orange;
- extreme contrast;
- motion blur;
- named camera/lens tokens.

## Output
Minimum useful result:
- resolved cinematic shot concept;
- provider-neutral shot decisions;
- adapted prompt/instructions if execution is unavailable or prompt-only is required;
- truthful verification state.

Success requires coherent intent, camera geometry, optics, lighting, exposure/color, physical realism, and preserved locks. A pretty but internally contradictory frame is not AUTO DIRECT success.