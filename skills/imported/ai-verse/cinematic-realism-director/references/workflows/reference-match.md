# REFERENCE MATCH Workflow

Status: RUNTIME WORKFLOW
Task: 6.4

Purpose: transfer observable visual DNA from one or more reference stills into a target shot without inventing exact unavailable hardware metadata or copying incidental content unintentionally.

## Entry
Use when the user provides or identifies a reference for composition, lens feel, lighting, color, texture, atmosphere, production design, identity, product, or overall visual language.

## Governing distinction

```text
OBSERVED VISUAL TRAIT != KNOWN CAMERA/LENS/STOCK FACT
```

Exact hardware is fact only when supplied by the user, trustworthy metadata, or another authoritative source.

## Procedure
1. Determine what each reference is for: identity, product, composition, perspective, lens character, depth, lighting, color, texture, environment, or overall look.
2. Build `reference-dna.schema.json` data from direct observations only.
3. Separate transferable DNA from content-specific details that should not automatically be copied.
4. Record any camera/lens/stock guess only as `hardware_hypothesis`, never fact.
5. Extract geometry first: camera height, angle, distance relationship, shot size, foreground/background scale, projection behavior.
6. Extract focus/depth and optical character separately from focal-length guesses.
7. Extract lighting motivation/direction/softness, exposure hierarchy, white balance, color separation, density, texture, atmosphere, and material response.
8. Apply target-scene locks before transfer. Target user locks outrank reference tendencies.
9. Resolve conflicts through `parameter-conflicts.md`. Never silently force the target to imitate a reference trait that contradicts a hard target requirement.
10. Build the target Cinematic Shot Spec using observable reference traits plus target-specific content.
11. Run Reality Gate V0, especially geometry, light, materials, and stylization restraint.
12. Adapt to provider/host. If the provider supports actual reference images, attach/use them as intended; otherwise translate DNA into text instructions.
13. After generation/edit, run V2 comparison when possible: evaluate composition/perspective, light, color, optical behavior, and preservation independently.

## Multiple references
Assign explicit roles and priorities. Do not average incompatible references into visual mush.

Example:

```text
ref A = identity
ref B = composition/perspective
ref C = lighting/color
```

If two references conflict in the same role, choose according to user priority or preserve the most important observable relationship and mark remaining uncertainty.

## Output
A valid reference-match result states or encodes:
- what was observed;
- what was transferred;
- what was intentionally not copied;
- what remains uncertain;
- which target locks overrode reference traits;
- provider handoff and verification state.

Failure includes claiming an exact lens/camera solely from appearance, copying incidental subject matter without instruction, or sacrificing target identity/product requirements to chase the reference look.