# Verified Pitfalls and Regression Lessons

Status: RUNTIME / EVAL SUPPORT

This file records meaningful failure patterns actually exposed during implementation, review, provider integration, or real use. Every item must support a permanent regression test.

## 1. Confidence Vocabulary Drift

Failure: inferred confidence could be confused with authority.

Correction:

```text
confidence != authority
user/preservation locks outrank inferred confidence
```

Regression: high-confidence inference must never override a lock.

---

## 2. Focal Length Used as Perspective

Failure: wide lens, camera proximity, perspective exaggeration, and fisheye were collapsed into one concept.

Correction: camera position/distance drives perspective relationship; focal length + format drives field of view; projection determines rectilinear/fisheye behavior.

Regression: close-foreground scale exaggeration must not automatically curve architecture or become fisheye.

---

## 3. Large Format / Wide Aperture Treated as Automatic Cinema

Failure: cinematic quality was equated with large format and maximum aperture.

Correction: depth is story/information/geometry-driven.

Regression: AUTO must choose moderate/deep focus when context matters.

---

## 4. Cinematic Effect Stacking

Failure: `cinematic` triggered a fixed bundle of shallow DOF, haze, flare, bloom, halation, rim light, teal/orange, motion blur, and visible grain.

Correction: professional finish is separated from optional visible effects. Subtle organic base texture may be normal; heavy/obvious effects still require a reason.

Regression: clean professional imagery must avoid unjustified effect stacking while still receiving premium tonal/color/texture finishing.

---

## 5. Film Reduced to Warmth + Grain + Fade

Failure: film response became a warm/faded/grain preset.

Correction: film/sensor response, color, grain strength, halation, bloom, exposure, and optics are separate systems.

Regression: named film stock must not automatically add every film stereotype.

---

## 6. Realism Confused with Dirt, Damage, Pores, or Asymmetry

Failure: anti-AI repair added random pores, dirt, wrinkles, scratches, flyaways, asymmetry, or noise.

Correction: realism is material/light/contact/geometry coherence, not imperfection quantity.

Regression: pristine product/beauty images may remain pristine.

---

## 7. Surface Texture Repaired Before Structure

Failure: microtexture was used to mask broken anatomy, perspective, contact, reflection, or light.

Correction: Reality Gate dependency order keeps structure/light before surface finish.

Regression: malformed geometry cannot be `fixed` by grain, pores, blur, or sharpening.

---

## 8. Skin Repair Became Pore Overlay

Failure: synthetic skin repair added equally sharp pores everywhere.

Correction: anatomy, regional texture, tonal/specular behavior, age/context, scale, and focus govern skin realism.

Regression: `make skin realistic` must not force pores, wrinkles, or aging.

---

## 9. Hair Realism Became Flyaway Spam

Failure: random flyaways were used as a realism token.

Correction: hair mass/root direction/gravity/clumps precede strand/flyaway detail.

Regression: a clean hairstyle may remain clean.

---

## 10. Reflection / Shadow / Catchlight Incoherence

Failure: local prettiness hid impossible scene-wide source geometry.

Correction: reflections, shadows, catchlights, wet surfaces, and material response share one plausible lighting geometry.

Regression: visible light evidence must agree.

---

## 11. Repair Drifted Into Regeneration

Failure: `make this less AI-looking` changed identity, pose, wardrobe, framing, background, light, or product geometry.

Correction:

```text
PRESERVE -> DIAGNOSE -> REPAIR -> ALLOW CHANGE -> VERIFY
```

Regression: use the smallest repair scope compatible with the request.

---

## 12. Missing Target Treated as Available

Failure: an unavailable prior image was treated as inspectable/editable.

Correction: never claim inspection/edit without the real target.

Regression: return a handoff spec or request the target only when essential.

---

## 13. Beginner Workflow Became a Camera Intake Form

Failure: one-line requests triggered unnecessary questions about focal length, aperture, body, light ratio, stock, grade, or provider.

Correction: infer safe professional choices automatically.

Regression: beginner AUTO normally asks zero technical questions.

---

## 14. Multi-Reference Roles Collapsed

Failure: identity, product, composition, light, color, and style references competed as one undefined style source.

Correction: assign explicit roles/priorities.

Regression: one reference must not silently overwrite another domain.

---

## 15. Reference Hardware Hallucination

Failure: exact camera/lens/aperture/stock/LUT was claimed from appearance alone.

Correction:

```text
observable trait != known metadata
```

Regression: exact hardware claims require evidence.

---

## 16. Frozen Moment Became Action Variation

Failure: multi-camera same-T0 requests changed pose/gaze/hands/props/time.

Correction: scene state remains frozen; only camera/parallax/framing may change.

Regression: camera variation must not become subject/action variation.

---

## 17. Provider Adapter Became a Second Creative Brain

Failure: provider advice changed composition, lens, light, grade, or concept.

Correction:

```text
Professional Quality Floor + universal shot = creative truth
adapter = translation only
```

Regression: normal provider translation may change syntax/verified controls, not the resolved image design.

---

## 18. Stale Provider Controls Treated as Current

Failure: cached model names/enums/reference limits were assumed current.

Correction: live verified surface > cached adapter > generic language.

Regression: never fabricate current controls from memory.

---

## 19. Adapter Existence Mistaken for Provider Access

Failure: provider file presence was treated as tool/account authorization.

Correction: package knowledge is separate from granted execution capability.

Regression: adapter presence alone cannot trigger external execution.

---

## 20. Tool Execution Mistaken for Visual Verification

Failure: successful API/tool return was equated with a successful image.

Correction:

```text
V1 = execution confirmed
V2 = actual visual inspection
```

Regression: do not claim the visual target passed without inspection.

---

## 21. PROMPT ONLY Override At Risk

Failure: image-capable hosts could generate despite explicit prompt-only output.

Correction: PROMPT ONLY is absolute.

Regression: `prompt only`, `JSON only`, `do not generate` must prevent execution.

---

## 22. Standalone Package Could Depend on Repo Context

Failure: first-party package could accidentally rely on siblings/root docs/private paths/OS services.

Correction: all runtime intelligence remains package-local.

Regression: the folder must remain independently understandable and useful.

---

## 23. External/MCP Tool Took Priority Over Native/Local Image Generation

Failure: when both native/local generation and an external MCP/provider were available, the system could choose the external provider because it appeared more specialized or cinematic.

Correction: `execution-priority.md` now requires:

```text
explicit provider lock
> native/local image capability
> external fallback only for a missing material capability
> prompt/spec
```

Regression: MCP/external execution must never preempt an adequate native/local path without an explicit provider lock or genuine missing capability.

---

## 24. Competitor Provider Became the Default Backend

Failure: Magnific Cinematic and Higgsfield Soul Cinema were listed as ordinary execution adapters, allowing the skill intended to compete with them to outsource final generation to them.

Correction: both adapters are explicit-target/benchmark-only.

Regression: ordinary image requests may not auto-route to Magnific or Higgsfield.

---

## 25. Missing Professional Quality Floor

Failure: AUTO optimized for coherent/neutral photography but did not guarantee world-class execution when the user gave a simple prompt.

Correction: every photographic request now receives the best-professional interpretation appropriate to its medium.

Regression: users must not need to add `professional`, `cinematic`, `Hollywood`, `ARRI`, `good lighting`, or `high quality` to get professional-grade direction.

---

## 26. Professionalization Erased the Requested Medium

Failure risk: fixing the quality floor could turn an iPhone selfie/candid/mobile request into a generic cinema-camera frame.

Correction: professionalization is medium-aware. Mobile stays mobile, candid stays candid, architecture follows architecture discipline, etc.

Regression: an iPhone selfie must look like elite mobile photography/editing, not an Alexa shot pretending to be a selfie.

---

## 27. Anti-Cliche Restraint Produced Sterile / Ordinary Output

Failure: grain and other finishing decisions were suppressed so aggressively that AUTO could produce clean but synthetic/ordinary images instead of polished professional imagery.

Correction: subtle organic filmic texture is now a normal photographic finishing layer for most imagery, while heavy grain/halation/flare/haze and other visible effects remain optional.

Regression: anti-cliche rules must prevent effect stacking without removing professional tonal/color/texture finishing.

---

# Maintenance Rule

When a new meaningful failure is verified:

1. document the evidence;
2. correct the smallest responsible runtime layer;
3. add/update the permanent regression requirement;
4. keep the eval corpus aligned;
5. do not add hypothetical filler.
