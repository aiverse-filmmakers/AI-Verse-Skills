# CINEMATIZE Workflow

Status: RUNTIME WORKFLOW
Task: 6.2

Purpose: upgrade an existing idea or ordinary prompt into a stronger cinematic still while preserving the concept rather than rewriting it into a different scene.

## Entry
Use when the user already has a concept/prompt and asks to make it more cinematic, professional, realistic, photographic, film-like, or better directed.

## Preservation rule
First separate:

```text
PRESERVE: concept, subject, required action, identity/product, required environment, explicit style/technical locks
AUTO-UPGRADE: shot design, camera position, hierarchy, optics, lighting, exposure, color, texture, realism
```

Do not equate `cinematize` with adding effects.

## Procedure
1. Parse the original prompt into literal content, creative intent, existing technical choices, and ambiguity.
2. Lock all explicit user choices. Do not silently replace a specified focal length, camera, lens, angle, composition, lighting condition, or preservation requirement.
3. Identify what is weak or underspecified: story hierarchy, framing, geometry, optics, light motivation, exposure, color, materials, or realism.
4. Upgrade only those weak/unspecified layers using the Phase 3-5 knowledge base.
5. Preserve the original creative premise and recognizability.
6. Replace vague prestige adjectives such as `cinematic`, `epic`, `film look`, or `professional lighting` with observable shot behavior.
7. Resolve conflicts using `parameter-conflicts.md`; solve through AUTO fields before touching locks.
8. Build/update the Cinematic Shot Spec.
9. Run Reality Gate V0.
10. Adapt to provider/host. If execution is available and requested, generate/edit; otherwise return the adapted prompt/spec.
11. If visual output is inspectable, run Reality Gate V2 and apply the smallest correction necessary.

## Upgrade priorities
Prefer improvements in this order:

```text
story / hierarchy
camera position / composition
perspective
focus / depth / motion
lighting motivation
exposure
color / grade
materials / contact / reflections
optional optical texture
```

Never try to rescue weak geometry with grain, haze, flare, bloom, or a LUT.

## Anti-overdirection rule
If the original prompt is already precise and coherent, do not inflate it with unnecessary technical detail. CINEMATIZE may produce a cleaner prompt rather than a longer one.

## Output
Return or execute a version that is recognizably the same concept but has stronger cinematographic causality and physical plausibility.

Failure conditions include concept drift, silent lock changes, gratuitous cinematic effects, or replacing the user's visual identity with a generic house style.