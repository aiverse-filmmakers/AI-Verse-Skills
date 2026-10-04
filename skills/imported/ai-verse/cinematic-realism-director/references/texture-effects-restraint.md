# Grain, Halation, Bloom, Flare, and Texture Restraint

Status: RUNTIME KNOWLEDGE

Purpose: govern photographic texture so the image receives a premium finished character without collapsing cinema into a bundle of fashionable artifacts.

Use with:

- `references/professional-quality-floor.md`
- `references/film-and-sensor-response.md`
- `references/lens-character.md`
- `references/color-science-and-grading.md`
- `references/exposure-and-dynamic-range.md`

## Governing Principle

Professional photographic finishing should usually avoid sterile AI cleanliness, but each optical/capture effect remains physically distinct.

Reason in this order:

```text
requested medium
-> professional specialty
-> capture intent
-> optics
-> exposure / bright-source behavior
-> tonal/color finish
-> subtle base texture
-> optional stronger effects only when justified
```

## Subtle Organic Texture Is the Normal Photographic Baseline

For most photographic and cinematic outputs, AUTO should include a **subtle organic filmic texture** unless the user or medium clearly calls for pristine digital cleanliness.

Target character:

- fine rather than coarse;
- low-amplitude rather than obvious;
- non-uniform rather than pasted noise;
- luminance-aware;
- compatible with the apparent capture medium;
- barely-to-gently visible at normal viewing size;
- never strong enough to hide skin/material defects.

Its function is to support photographic cohesion and avoid sterile synthetic smoothness—not to advertise a `film look`.

### Normally retain subtle texture

- narrative/cinematic frames;
- candid/documentary/street images;
- portraits;
- fashion/editorial;
- lifestyle/commercial scenes;
- travel/hospitality;
- mobile/phone photography when it improves naturalness;
- environmental product/automotive work where texture does not damage required detail.

### Normally reduce/remove texture

- explicit `no grain`, `pristine digital`, `noise-free`, `clinical`, `sterile`, `perfectly clean` instructions;
- technical/medical documentation;
- pure e-commerce packshots where a spotless background and exact microdetail are the priority;
- certain beauty/product macros where visible grain interferes with material readability;
- non-photographic screens/graphics outside this skill's main scope.

The user can always override AUTO.

## Grain

Grain should read as structured photographic texture, not uniform digital noise.

Consider:

- apparent capture medium/format;
- exposure;
- output size;
- luminance region;
- professional specialty;
- requested cleanliness;
- whether the user explicitly named a stock/format.

### Strong/coarse grain still needs a reason

Use stronger visible grain when:

- a film/analog medium is explicitly requested;
- a stock/format/reference visibly supports it;
- period/archival intent benefits from it;
- a deliberate rough/tactile aesthetic is part of the brief.

### Avoid

- identical noise everywhere;
- giant 16mm-style grain on clean large-format digital work without intent;
- using grain to hide structural errors;
- treating grain strength as the only difference between digital and film;
- adding obvious grain to a pristine clinical/product requirement.

## Digital Sensor Noise

Digital noise and filmic texture are different.

Low-light digital capture may show luminance/chroma noise, denoising artifacts, pattern noise, or shadow detail loss. Only add these when the requested medium/conditions benefit from imperfect digital capture.

Premium digital-cinema or elite mobile finishing usually controls ugly sensor noise while retaining enough texture to avoid waxy smoothness.

## ARRI-Like Tonal Finish vs Grain

`ARRI-like` in this skill refers to observable tonal goals such as:

- smooth highlight rolloff;
- gentle highlight-to-mid transition;
- natural skin-tone separation;
- rich readable shadows;
- controlled color density.

It does **not** mean:

- literal ARRI sensor simulation;
- mandatory ARRI camera naming in prompts;
- mandatory grain;
- mandatory warmth;
- a single LUT/preset.

Subtle filmic texture may complement this tonal goal, but the two are separate systems.

## Halation

Halation is never a default consequence of the base texture layer.

Use visible halation only when:

- film/medium reference plausibly supports it;
- bright sources/edges motivate it;
- the provider can express it without global glow;
- the user/reference calls for it.

Keep it localized and exposure-dependent.

Avoid red/orange outlines on every bright edge.

## Bloom

Bloom is bright-value light spread, not global blur.

It may come from optical diffusion, mist/filter behavior, bright-source scatter, or provider-specific post behavior.

Tie bloom to genuinely bright regions and source context. Do not soften the whole image under the label `cinematic`.

## Lens Flare

Flare requires source/lens geometry.

Possible forms include veiling glare, ghosts, streaks, reduced local contrast, and internal reflections.

AUTO flare should remain absent unless a plausible source and lens behavior justify it.

```text
cinematic != flare
anamorphic != mandatory blue streak
vintage lens != flare everywhere
```

## Optical Diffusion

Diffusion may reduce brittle high-frequency detail while preserving the focus plane.

Possible consequences:

- gentler facial microcontrast;
- highlight spread;
- smoother tonal transitions;
- less brittle edges.

Do not turn diffusion into missed focus.

## Sharpness and Microcontrast

Professional detail is material-specific and focus-dependent.

Avoid:

- crunchy skin;
- pore halos;
- fake fabric weave;
- HDR-like local contrast;
- oversharpened hair;
- indiscriminate softness.

Faces can retain real structure without every pore being edge-enhanced.

## Mobile / iPhone Texture

For phone/selfie/social photography:

- preserve believable phone acuity, depth, and computational-processing character;
- suppress ugly oversharpening, fake HDR, denoising waxiness, and cutout portrait blur;
- a very subtle organic finishing texture may be added when it keeps the image natural;
- do not force obvious 35mm grain or cinema-camera softness onto a phone image.

The professional goal is elite mobile photography/editorial finishing, not disguise of the medium.

## Clean Commercial Work

Clean commercial does not mean sterile plastic.

A premium clean result may have:

- nearly invisible or absent grain where product clarity requires;
- controlled highlights;
- exact material microtexture;
- clean color separation;
- restrained sharpening;
- subtle natural surface variation;
- professional tonal polish.

For lifestyle/commercial scenes, subtle organic texture may remain if it strengthens cohesion without damaging product readability.

## Documentary / Candid / Naturalistic Drama

These normally benefit from:

- subtle organic texture;
- realistic optical/focus transition;
- believable available/motivated light;
- non-plastic skin/material response;
- professional color/exposure finishing.

They do not automatically require heavy grain, flare, haze, or vintage damage.

## Vintage / Period Intent

Choose one coherent medium/period rather than stacking unrelated old-media artifacts.

Do not combine 35mm grain + VHS chroma bleed + modern anamorphic streak + Polaroid color shift unless the user intentionally wants a hybrid.

## Texture Hierarchy

Texture strength should vary by material, focus, light, and depth.

- skin texture follows lighting/focus;
- fabric weave depends on distance/focus;
- brushed metal has directional response;
- glass is primarily defined by reflection/refraction;
- stone/walls can retain fine irregularity;
- background detail should follow depth/motion.

Global overlays are a common AI-look amplifier.

## Reality Gate

Check:

1. Is subtle base texture appropriate to the requested medium?
2. If texture is absent, does the image risk sterile/waxy AI cleanliness?
3. If texture is visible, is it fine and non-uniform rather than pasted noise?
4. Does strong grain have a specific reason?
5. Is halation localized to sufficiently bright boundaries?
6. Is bloom tied to bright values?
7. Does flare geometry correspond to a plausible source?
8. Does sharpness follow focus/depth/motion/material?
9. Are media artifacts internally consistent?
10. Did any effect appear because `cinematic` was treated as an effects preset?

## Hard Rules

```text
subtle organic texture = normal photographic finish unless medium/user says otherwise
strong grain = intentional choice
film != grain + warmth + fade
halation != universal red glow
bloom != global blur
flare != mandatory cinema token
anamorphic != blue-streak preset
diffusion != missed focus
sharpness != edge halos
realism != dirtiness
professional finish != sterile AI cleanliness
provider effect control != reason to use it
```
