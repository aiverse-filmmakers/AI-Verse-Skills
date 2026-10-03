# REALITY REPAIR Workflow

Status: RUNTIME WORKFLOW
Task: 6.3

Purpose: diagnose why an existing still feels synthetic or physically inconsistent, preserve what must remain, and repair the smallest necessary set of failures without uncontrolled regeneration.

## Entry
Use only when an actual target image is available for inspection/editing, or when the user explicitly asks for diagnosis based on a description. Never pretend an unavailable prior image is still attached.

## Mandatory stages

```text
1. identify preservation targets
2. diagnose artificiality
3. prioritize repairs
4. avoid scene drift
5. adapt edit instructions to host/model
6. Reality Gate
```

## Procedure
1. Confirm the analysis basis: direct visual inspection, user description only, or both.
2. Build explicit `preserve`, `repair`, and `allow_change` boundaries before proposing edits.
3. Diagnose using `anti-ai-artifact-taxonomy.md` and `realism-diagnosis.schema.json`.
4. Record visual evidence, severity, region, confidence, likely cause, and whether a repair conflicts with preservation.
5. Fix dependencies in order: geometry/anatomy before surface texture; lighting before reflections; contact before added dirt; focus/motion before sharpening.
6. Prefer local/targeted repairs over global restyling.
7. Use domain systems for skin, hair/eyes, fabric/materials, contact/gravity, reflections/shadows, and optical imperfection.
8. Never add pores, flyaways, grain, asymmetry, dirt, wrinkles, scratches, or vintage artifacts merely to signal realism.
9. Preserve identity, pose, composition, product geometry, wardrobe, text, environment, and other locked elements exactly to the degree requested.
10. If a required repair conflicts with a preservation lock, surface the conflict. Do not silently break the lock.
11. Translate the repair plan to the host/model's actual edit capabilities. If editing is unavailable, return a precise repair prompt/plan rather than claiming a modification.
12. Run Reality Gate before handoff at V0.
13. After an edit, inspect at V2 when possible. Compare preservation and realism separately.
14. Iterate only on material remaining failures and retain successful regions.

## Repair priority

```text
structural plausibility
-> lighting / shadow / reflection coherence
-> material/contact behavior
-> human surface realism
-> color / texture restraint
-> optional optical cleanup
```

## Regeneration threshold
Regeneration is a last resort for structural failures too entangled for targeted editing. Even then, preservation constraints remain active.

## Output
A complete repair result includes:
- diagnosis;
- preservation boundary;
- prioritized repair list;
- minimal edit strategy;
- provider/host handoff;
- Reality Gate outcome;
- truthful success/partial/blocked state.

A visually attractive image that changes the wrong person/product/pose/composition is a failed Reality Repair.