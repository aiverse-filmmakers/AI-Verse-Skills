# Color Science and Grading Strategy

Status: RUNTIME KNOWLEDGE
Task: 4.6

This reference converts the Phase 1 color research into provider-neutral runtime decisions. It describes visible color relationships rather than one LUT, one camera transform, or one fashionable grade.

Use with:

- `references/visual-intent.md`
- `references/motivated-lighting.md`
- `references/exposure-and-dynamic-range.md`
- `references/film-and-sensor-response.md`
- `references/research/color-and-tone.md`

## 1. Governing Principle

Color design follows the scene and lighting system.

Reason in this order:

```text
story / product intent
-> source colors and production design
-> white-balance strategy
-> exposure / density
-> subject-background separation
-> saturation strategy
-> highlight / shadow color behavior
-> creative grade
-> display-safe restraint
```

Do not begin from:

```text
teal-orange
film LUT
warm cinematic
cool shadows
```

unless the user explicitly locks that treatment or the story/source design supports it.

## 2. Capture Color vs Final Grade

Keep acquisition and rendering separate.

```text
camera / stock response
!=
creative grade
```

Examples:

- LogC4 is not a finished ARRI look.
- S-Log3 is not a low-contrast aesthetic instruction.
- tungsten-balanced stock does not require an orange final image.
- a wide-gamut capture reference does not imply maximum saturation.

Default AUTO output should be a finished image, not an ungraded log frame, unless the user explicitly requests log/ungraded output.

## 3. White Balance Strategy

Choose what, if anything, is treated as perceptually neutral.

Possible strategies:

### Neutral dominant source

Useful for:

- products;
- commercial beauty;
- architecture;
- documentary clarity;
- clean daylight.

Keep secondary source differences believable rather than neutralizing every light.

### Preserve warm/cool mixed light

Useful for:

- tungsten practical interior + daylight window;
- sunset exterior + cool sky fill;
- warm streetlight + blue-hour ambient;
- candle/fire + cool room ambience.

Do not force both sources to white.

### Deliberate non-neutral balance

Allowed when the story calls for a perceptual bias.

Examples:

- cool institutional interior;
- sodium-heavy street;
- warm nostalgic room;
- underwater or stylized monochromatic environment.

The shift must still respect source relationships and material response.

## 4. Color Separation

Prefer separation created by the whole scene rather than post-color gimmicks.

Useful mechanisms:

- warm/cool source contrast;
- luminance separation;
- production-design hue contrast;
- neutral subject against saturated environment;
- saturated subject against restrained environment;
- selective local saturation;
- material-specific highlight color.

Color separation should clarify hierarchy.

It should not automatically become equal cyan on one side and orange on the other.

## 5. Saturation Strategy

Saturation is contextual.

### Restrained

Useful for:

- documentary;
- overcast drama;
- naturalistic interiors;
- dense low-key work.

### Moderate / natural

Useful default for:

- portraits;
- travel;
- food;
- narrative daylight;
- architecture.

### High but controlled

Useful for:

- pop commercial;
- colorful fashion;
- vivid production design;
- reversal-film references;
- neon environments.

High saturation still requires tonal variation and material texture.

Avoid flat neon color patches caused by clipping.

## 6. Density

Treat density as a multi-factor perceptual quality, not a darkening slider.

A dense image may combine:

- substantial midtones;
- deep but differentiated shadows;
- controlled highlight rolloff;
- stable color in midtones;
- non-lifted blacks;
- visually weighted production-design color.

Avoid:

```text
density = lower exposure everywhere
```

A bright commercial image may still feel dense through stable color, dimensional highlights, and substantial midtones.

## 7. Skin Handling

Skin belongs inside the lighting and color system, not outside it.

Preserve:

- natural hue differences across the face/body;
- source-colored specular highlights;
- subtle redness and cooler areas;
- subsurface warmth where plausible;
- environmental color contamination;
- ethnicity and age-specific variation;
- makeup when actually present.

Avoid:

- uniform peach/orange skin;
- whitening highlights until all chroma disappears;
- aggressively isolating skin from environmental color;
- beauty-grade smoothing disguised as color correction.

Task 5.2 defines skin surface realism in more detail.

## 8. Highlight Color

Bright regions should keep source/material identity as long as plausible.

Examples:

- warm practicals retain warmth before their hottest core approaches white;
- neon retains hue and local texture before clipping;
- metallic reflections inherit source/environment color;
- skin speculars track the source and become less saturated than diffuse skin without becoming arbitrary white paint.

Hard clipping is allowed when motivated. The goal is not to recover color from every emissive core.

## 9. Shadow Color

Shadow color comes from ambient/environmental illumination and material response.

Possible behavior:

- cool sky-filled exterior shadow;
- warm wood-room bounce;
- green fluorescent contamination;
- neutral controlled studio shadow;
- near-black low-key shadow with remaining chroma.

Do not uniformly paint shadows cyan or remove all chroma from them.

## 10. Black Level

Choose black behavior deliberately:

- open natural shadows;
- dense differentiated blacks;
- intentionally crushed areas;
- faded/lifted blacks only when a specific aesthetic calls for them.

Cinematic realism does not require lifted blacks.

Dense blacks do not require destroying every low-end detail.

## 11. Highlight Rolloff

Prefer gradual transitions where the capture/look intent supports them.

Visible target:

```text
midtone
-> bright tone
-> colored highlight
-> near-white highlight
-> optional clipped core
```

Avoid sudden digital-looking boundaries or local-HDR halos used to preserve every bright detail.

## 12. Neutral Grade

A neutral grade is not a lack of authorship.

It should still decide:

- white balance;
- contrast;
- density;
- black level;
- highlight behavior;
- saturation;
- skin placement;
- color separation.

Use neutral grades when accurate products, believable environments, documentary truth, architecture, or clean commercial work matter more than conspicuous stylization.

## 13. Stylized Grade

Stylization may alter:

- palette;
- hue relationships;
- saturation;
- density;
- contrast distribution;
- highlight/shadow tint;
- black level.

But preserve:

- source logic unless intentionally surreal;
- skin/material plausibility when realism remains a goal;
- tonal hierarchy;
- hue stability;
- non-clipped texture where important.

Stylized does not mean physically random.

## 14. Common Grade Families as Decision Patterns

### Clean commercial

- neutral-to-pleasant white balance;
- controlled bright values;
- natural skin/product color;
- clean separation;
- no unnecessary vintage contamination.

### Naturalistic drama

- source-led white balance;
- moderate or restrained saturation;
- deliberate density;
- smooth highlights;
- believable mixed-light contamination.

### Documentary

- minimal conspicuous grading;
- preserve environmental light color;
- avoid beautification that changes scene truth;
- allow imperfect practical/source balance.

### Fashion/editorial

- stronger palette design allowed;
- preserve skin/material dimensionality;
- avoid plastic global color smoothing.

### Night / neon

- preserve source-specific hue zones;
- avoid universal cyan/magenta split;
- protect emissive color before clipping;
- keep dark regions genuinely dark where appropriate.

### Warm nostalgia

- warmth can come from source, production design, stock reference, or grade;
- do not make whites uniformly orange;
- preserve hue separation.

## 15. Monochrome

True B&W should be treated as a luminance and spectral-response design, not just `saturation = 0`.

Reason about:

- skin-to-background luminance separation;
- fabric/material tonal separation;
- highlight and shadow density;
- grain character if requested;
- source direction and specular behavior.

Do not add a sepia tint unless requested.

## 16. Product / Brand Accuracy

When product color is a preservation lock:

- do not shift brand color for cinematic harmony;
- allow environmental reflections without changing the base material color;
- keep whites and neutrals sufficiently truthful;
- use lighting/separation rather than destructive hue shifts.

Brand/product color has higher authority than an AUTO grade.

## 17. Reference Match

When matching a reference:

Observe and transfer:

- white-balance relationship;
- palette;
- saturation distribution;
- density;
- skin/environment relationship;
- highlight/shadow color;
- black level;
- contrast distribution.

Do not claim the exact LUT, CDL, color space, stock process, printer lights, or camera transform unless metadata/source evidence provides it.

## 18. Provider Translation

Adapters may convert these visible goals into provider-specific language or controls.

The core brain should store:

```text
white_balance
palette
color_separation
saturation
density
highlight_treatment
shadow_treatment
skin_tone_treatment
```

Provider syntax remains downstream.

If a provider offers a named grade preset, use it only when it meaningfully matches the locked/selected intent. The preset must not silently redefine the universal color design.

## 19. Color Reality Gate

Before accepting a result, check:

1. Does white balance make sense for the source design?
2. Are mixed sources preserved rather than accidentally neutralized?
3. Is skin plausible under those sources?
4. Are brand/product colors preserved when locked?
5. Do bright saturated colors retain believable hue/texture before clipping?
6. Are shadows colored by plausible ambient/environment light?
7. Is the image too uniformly saturated or desaturated?
8. Do black levels support the intended density?
9. Is highlight transition coherent with exposure/capture intent?
10. Has an AUTO grade introduced teal/orange or another cliché without a reason?
11. Does stylization preserve the chosen realism target?

## 20. Hard Rules

```text
log != final grade
cinematic != teal-orange
cinematic != desaturated
film != warm faded LUT
skin != one orange hue
density != simply darker
mixed light != normalize every source
highlight protection != suppress every bright core
provider preset != universal color truth
```
