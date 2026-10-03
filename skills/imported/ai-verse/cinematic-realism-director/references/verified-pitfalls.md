# Verified Pitfalls and Regression Lessons

Status: RUNTIME / EVAL SUPPORT
Task: 8.6

This file contains failure patterns actually exposed during implementation reviews, phase gates, schema integration, or provider/host integration work for this package.

It intentionally avoids hypothetical filler. Each item should become or support a permanent regression test.

## 1. Confidence Vocabulary Drift

### Failure

The structured shot schema initially carried a coarse parameter state plus numeric confidence, while the richer confidence policy used more nuanced semantic labels. Without an explicit bridge, different hosts could serialize the same evidence inconsistently or treat numeric confidence as a fake calibrated probability.

### Correction

Added `confidence-serialization.md` and fixed the rule:

```text
confidence != authority
numeric confidence is a carrier, not a calibrated probability by default
user lock outranks any confidence value
```

### Regression Requirement

Never let a high inferred confidence override a user or preservation lock.

---

## 2. Focal Length Used as a False Substitute for Perspective

### Failure

Common cinematic prompting collapses `wide lens`, camera proximity, perspective exaggeration, and fisheye into one concept.

### Correction

Phase 3 separated:

```text
camera position / distance -> perspective relationship
focal length + format -> field of view
projection / lens design -> rectilinear vs fisheye behavior
```

### Regression Requirement

A request for strong close foreground scale must not automatically curve the background or become fisheye.

---

## 3. Large Format / Wide Aperture Treated as Automatic Cinema

### Failure

Early design risk: generative conventions tend to equate large format and maximum aperture with cinematic quality.

### Correction

Depth is now story- and geometry-driven. Large format does not imply shallow depth, and `f/1.2` is not automatically preferable to `f/4`, `f/8`, or deeper focus.

### Regression Requirement

AUTO must choose deep/moderate focus when environmental information is narratively important.

---

## 4. Cinematic Effect Stacking

### Failure

The phrase `cinematic` can cause automatic addition of grain, haze, flare, bloom, halation, shallow depth, dramatic rim light, teal/orange separation, lifted blacks, or motion blur.

### Correction

Phase 4 separated all of these into optional systems with physical/story justification requirements.

### Regression Requirement

A clean bright commercial, neutral documentary frame, or hard-noon exterior must remain allowed to contain none of these effects.

---

## 5. Film Reduced to Warmth + Grain + Fade

### Failure

Generic prompt behavior often treats film response as one warm faded grain preset.

### Correction

Film/sensor response, color, grain, halation, bloom, exposure, and optical behavior are separate layers.

### Regression Requirement

A named film stock must not automatically add every stereotypical film artifact.

---

## 6. Realism Confused with Dirt, Damage, Pores, or Asymmetry

### Failure

An anti-AI repair can make a clean image worse by adding random pores, dirt, wrinkles, grain, scratches, flyaways, asymmetry, or surface noise simply to make it look less perfect.

### Correction

Phase 5 defined realism through material/light/contact/geometry coherence rather than imperfection quantity.

### Regression Requirement

A pristine commercial product or beauty image must be allowed to remain pristine and polished while still passing the Reality Gate.

---

## 7. Surface Texture Repaired Before Structural Geometry

### Failure

Adding skin/fabric microtexture can mask but not solve broken anatomy, perspective, contact, or lighting.

### Correction

The Reality Gate enforces dependency order, with geometry/focus/light before surface texture.

### Regression Requirement

A malformed hand or impossible reflection must not be `fixed` by grain, blur, pores, or sharpening.

---

## 8. Skin Repair Became Pore Overlay

### Failure

Synthetic skin repair can overcompensate by placing equally sharp pores everywhere.

### Correction

Skin realism now prioritizes anatomy, region-specific texture, tonal variation, source-consistent specular response, age/context, focus, and scale.

### Regression Requirement

`Make skin realistic` must not imply stronger pores, extra wrinkles, or forced aging.

---

## 9. Hair Realism Became Mandatory Flyaways

### Failure

Flyaways are often used as a generic realism token and can break hairstyle length or create floating disconnected strands.

### Correction

Hair hierarchy is mass/silhouette -> root direction -> gravity/clumps -> only then scale-appropriate strand detail/flyaways.

### Regression Requirement

A clean hairstyle can remain clean; flyaways are optional and physically attached.

---

## 10. Reflection / Shadow / Catchlight Incoherence

### Failure

Local beauty can hide scene-wide inconsistencies: catchlights with no source, wet reflections pointing incorrectly, shadows with incompatible direction/softness, or reflective materials behaving independently from environment geometry.

### Correction

Reflection/shadow coherence became its own physical-realism system and Reality Gate stage.

### Regression Requirement

All visible light evidence must agree with the plausible source geometry.

---

## 11. Repair Drifted Into Regeneration

### Failure

`Make this less AI-looking` can accidentally redesign identity, face, pose, wardrobe, framing, background, lighting, or product geometry.

### Correction

REALITY REPAIR requires:

```text
PRESERVE
-> DIAGNOSE
-> REPAIR
-> ALLOW CHANGE
-> VERIFY
```

### Regression Requirement

Local realism failures must use the smallest repair scope compatible with the request.

---

## 12. Missing Target Image Treated as If It Were Available

### Failure

A chat/host may refer to a previous image that is not actually available in the current tool context.

### Correction

The host/image-target contract forbids pretending to inspect or edit an unavailable image.

### Regression Requirement

When the target is unavailable, return a repair specification or request the image only when essential; never claim an edit occurred.

---

## 13. Beginner Workflow Turned Into a Camera Intake Form

### Failure

A one-sentence creative request can trigger unnecessary questions about focal length, aperture, camera body, lighting ratio, stock, or grade.

### Correction

Question-minimization policy: ask only when the missing answer materially changes the required deliverable, preservation boundary, or execution possibility.

### Regression Requirement

Beginner AUTO should normally complete the shot without requiring technical input.

---

## 14. Multiple References Collapsed Into One Undefined Style

### Failure

Identity, product, composition, lighting, color, and style references can fight each other when their roles are not explicit.

### Correction

Multi-reference behavior assigns roles and priorities to every reference.

### Regression Requirement

The skill must preserve role separation and target locks; one reference may not silently overwrite another domain.

---

## 15. Reference Hardware Hallucination

### Failure

A visually similar reference can tempt the system to claim an exact camera, lens, aperture, film stock, or LUT.

### Correction

Reference Match explicitly separates:

```text
observable trait
known metadata
hardware hypothesis
unknown
```

### Regression Requirement

Exact equipment claims require supplied metadata or documented evidence.

---

## 16. Frozen-Moment Multi-Camera Requests Became Pose/Action Variations

### Failure

When asked for multiple cameras around one frozen instant, generative reasoning can change pose, gaze, props, or time between views.

### Correction

Composition/blocking and multi-reference policies define:

```text
same T0
same scene state
same pose/action
only camera changes
```

### Regression Requirement

Camera variation must not become subject/action variation when the user locks the instant.

---

## 17. Provider Adapter Became a Second Cinematic Brain

### Failure

Provider-specific prompt advice can accidentally alter composition, lens choice, lighting, or grade to fit remembered provider preferences.

### Correction

Phase 7 enforces:

```text
Cinematic Shot Spec = creative truth
adapter = translation layer
```

### Regression Requirement

The same resolved shot must preserve its intent and locks across Generic, OpenAI, Gemini, Seedream, FLUX, Magnific, and Higgsfield adapters.

---

## 18. Stale Provider Controls Were Treated as Current

### Failure

Provider model names, enums, reference limits, editing controls, and product surfaces change over time.

### Correction

Every named adapter includes a verification/fallback rule; unknown or changed capability falls back to generic observable language rather than invented parameters.

### Regression Requirement

Never fabricate a current control solely because an older provider version exposed it.

---

## 19. Adapter Existence Mistaken for Provider Access

### Failure

Having `adapters/magnific.md` or another provider file could be misread as permission/connectivity to that service.

### Correction

Host action policy separates package knowledge from actual granted tools.

### Regression Requirement

Adapter presence alone must never trigger an external call or claim provider availability.

---

## 20. Tool Execution Mistaken for Visual Verification

### Failure

A successful generation/edit API call may still return a visually wrong image.

### Correction

Verification levels remain distinct:

```text
V1 = execution confirmed
V2 = actual visual inspection completed
```

### Regression Requirement

Never claim the visual target passed the Reality Gate merely because the tool returned successfully.

---

## 21. PROMPT ONLY Override Was At Risk of Being Ignored

### Failure

Tool-capable hosts naturally prefer execution and can generate despite a user explicitly asking for a prompt only.

### Correction

PROMPT ONLY is an absolute output-intent override.

### Regression Requirement

`Do not generate`, `prompt only`, `JSON only`, or equivalent instructions must prevent image execution.

---

## 22. Standalone Package Could Accidentally Depend on Repo Context

### Failure

A first-party package can unknowingly rely on sibling skills, repository-root docs, private paths, or OS-specific behavior.

### Correction

Phase 0 froze the standalone-folder invariant and all runtime references remain package-local.

### Regression Requirement

A capable agent receiving only this folder must still understand routing, workflows, shot design, realism, adapters, schemas, and fallback behavior.

---

# Maintenance Rule

When a new meaningful failure is found:

1. reproduce or document the evidence;
2. correct the smallest responsible contract/reference/workflow;
3. add the failure to this file only if verified;
4. add or update a regression eval in Phase 9;
5. never pad this file with theoretical pitfalls merely for completeness.
