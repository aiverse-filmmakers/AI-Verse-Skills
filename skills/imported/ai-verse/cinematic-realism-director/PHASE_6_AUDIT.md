# Phase 6 Audit - Decision Engine and Workflows

Status: PASSED

Scope: verify that the same skill behaves naturally for a novice sentence, an expert camera specification, a synthetic-looking image repair, a reference-match task, prompt-only handoff, and multi-reference work while preserving the Phase 0-5 contracts.

## Files Audited

- `references/workflows/auto-direct.md`
- `references/workflows/cinematize.md`
- `references/workflows/reality-repair.md`
- `references/workflows/reference-match.md`
- `references/workflows/manual-camera.md`
- `references/workflows/prompt-only.md`
- `references/progressive-disclosure-router.md`
- `references/question-minimization.md`
- `references/multi-reference-behavior.md`
- `references/reality-gate.md`
- Phase 0 lock/host/success contracts
- Phase 2 schemas and confidence/conflict semantics

## Gate Requirement

> The same skill behaves naturally for a novice sentence, expert camera specification, bad AI image, or reference frame.

Result: PASS.

---

# Test 1 - Beginner AUTO, One Sentence

Input class:

```text
A tired chef standing alone in his closed restaurant after midnight.
```

Expected behavior:

- AUTO DIRECT selected;
- no camera questionnaire;
- intent and viewer relationship inferred;
- environment retained as story context;
- camera, lens, depth, light, exposure, color and realism filled only as needed;
- no mandatory grain, haze, teal/orange, anamorphic flare or razor-thin DOF;
- provider adaptation happens after universal shot design.

Result: PASS.

Question-minimization violation: 0.
Generic-cinema-cliche requirement: 0.

---

# Test 2 - Expert Locked Camera

Input class:

```text
Alexa 35, Signature Prime 35mm, T2.8, eye-level medium shot, deep focus, hard noon sun in the desert.
```

Expected behavior:

- MANUAL CAMERA selected;
- every explicit technical value becomes a lock;
- AUTO fills only missing values;
- depth logic reconciles T2.8/deep-focus through scene distance and focus strategy rather than changing locks;
- lighting uses hard-sun/desert logic;
- unsupported provider controls become semantic translations, not silent substitutions.

Result: PASS.

Explicit-lock violations: 0.
Hidden conflict resolution: 0.

---

# Test 3 - CINEMATIZE Without Concept Drift

Input class:

```text
Make this simple family beach photo feel like a premium travel commercial, but keep the exact people, moment and location.
```

Expected behavior:

- CINEMATIZE selected;
- people/moment/location become preservation constraints;
- upgrade composition/light/exposure/color/physical coherence only where allowed;
- no scene replacement or wardrobe redesign;
- no automatic vintage artifacts.

Result: PASS.

Preservation violations: 0.
Concept-drift violations: 0.

---

# Test 4 - REALITY REPAIR

Input class:

```text
Fix the plastic skin and floating hair in this image. Change nothing else.
```

Expected behavior:

- REALITY REPAIR selected;
- target image availability checked truthfully;
- preserve list created before diagnosis;
- skin/hair failures diagnosed with evidence;
- smallest repair path chosen;
- no beautification, identity redesign, pose change, background rewrite or global regeneration unless local repair is impossible;
- V2 Reality Gate only if image is actually inspectable.

Result: PASS.

Repair-overreach violations: 0.
False visual-inspection claims: 0.

---

# Test 5 - REFERENCE MATCH With Hardware Uncertainty

Input class:

```text
Make my product shot feel like this reference.
```

Reference exhibits:
- low camera height;
- broad soft side light;
- dense neutral shadows;
- restrained saturation;
- smooth focus falloff.

Expected behavior:

- REFERENCE MATCH selected;
- observable DNA transferred;
- exact camera/lens/film not claimed from pixels;
- product identity/geometry remains target-locked;
- provider adapter receives visual traits, not invented metadata.

Result: PASS.

Hardware-certainty violations: 0.
Product-drift violations: 0.

---

# Test 6 - PROMPT ONLY Override

Input class:

```text
Give me only a Seedream-ready prompt for this shot. Do not generate anything.
```

Expected behavior:

- PROMPT ONLY selected even if host has image tools;
- shot designed and V0 checked;
- provider adapter may translate syntax if known;
- no image tool invocation implied;
- final output is prompt/spec only.

Result: PASS.

Prompt-only override violations: 0.

---

# Test 7 - Multi-Reference Role Separation

Input class:

```text
Image 1 = character identity. Image 2 = wardrobe. Image 3 = lighting. Keep the setting from the target image.
```

Expected behavior:

- each reference gets a role;
- identity, wardrobe, lighting and target setting are not averaged together;
- target locks outrank style/reference tendencies;
- provider reference-count limits preserve hard identity/product/edit target first and translate lower-priority DNA textually if needed.

Result: PASS.

Reference-role collapse: 0.
Priority inversion: 0.

---

# Test 8 - Frozen-Moment Multi-Camera Reference

Input class:

```text
Same exact instant and poses, but move the camera over the father's shoulder.
```

Expected behavior:

- pose/action/gaze/expression/object positions/time/lighting locked;
- only camera position, visible occlusion, framing and resulting perspective change;
- no action sequence or character turnaround.

Result: PASS.

Scene-drift violations: 0.

---

# Progressive Disclosure Audit

Verified routing subsets can operate package-locally:

```text
AUTO DIRECT -> core contracts + active camera/light references + Reality Gate + adapter
REALITY REPAIR -> repair workflow + diagnosis schema + relevant realism modules + Reality Gate + edit adapter
REFERENCE MATCH -> reference schema + role/confidence rules + relevant visual systems + adapter
MANUAL CAMERA -> locks + camera/lens/perspective/depth + conflicts if needed + adapter
PROMPT ONLY -> active workflow + required visual modules + adapter; no image execution
```

External runtime dependency introduced: 0.
Sibling-skill dependency introduced: 0.

---

# Phase 6 Result

```text
scope violations: 0
standalone violations: 0
provider-core contamination: 0
explicit-lock violations: 0
preservation violations: 0
false hardware-certainty violations: 0
false visual-verification violations: 0
question-bloat violations: 0
reference-role violations: 0
prompt-only override violations: 0
```

Verdict: **PASSED**.

Phase 6 provides a complete workflow layer. Phase 7 may now translate this one cinematic brain into provider-specific instructions without redesigning the shot.