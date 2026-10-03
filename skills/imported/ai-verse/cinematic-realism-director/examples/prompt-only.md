# Example - PROMPT ONLY

This example demonstrates an explicit no-generation request. It is not a hidden mandatory template.

## User

```text
Give me the final Seedream prompt only for a luxury watch product shot. Do not generate anything.
```

## Routing

```text
workflow = PROMPT ONLY
provider target = Seedream
execution = forbidden by explicit user instruction
```

Even if the host has image tools, the skill must not generate.

## Shot Resolution Before Adaptation

The skill first resolves the provider-neutral shot, for example:

- premium tabletop hero image;
- three-quarter product angle with accurate circular/watch geometry;
- moderate close framing;
- rectilinear perspective with no exaggerated wide-angle distortion;
- enough depth to keep the watch face, crown, and key bracelet links legible;
- large soft key motivated as a studio source, controlled edge/reflection shaping, restrained fill;
- dark neutral environment with selective specular separation;
- pristine materials allowed because this is a luxury commercial product;
- metal, crystal, dial, brushed/polished surfaces and contact shadows must respond differently and coherently;
- no automatic grain, dust, fingerprints, flare, haze, or fake vintage treatment.

Only then is the shot translated into Seedream-appropriate language.

## Example Final Prompt

```text
Luxury wristwatch hero photograph on a dark neutral studio surface, photographed from a refined three-quarter product angle with rectilinear perspective and accurate circular case geometry. Frame close enough for premium detail while keeping the full watch silhouette, crown, dial, crystal edge and several bracelet links clearly readable. Use moderate depth with a precise focus plane through the dial and front case, followed by smooth natural falloff rather than aggressive background blur.

Light with one large soft studio key from upper camera-left, producing broad controlled gradients across the polished metal and crystal, plus restrained opposing fill and narrow reflection shaping so brushed and polished surfaces remain visibly distinct. Keep specular highlights elegant and source-consistent; preserve dark negative space around the product without crushing important edge detail. The watch must sit with believable weight on the surface and cast a coherent soft contact shadow.

Render physically plausible materials: clean polished metal, directional brushed metal, transparent crystal with controlled reflection/refraction, crisp dial printing and markers, realistic micro-roughness without procedural noise. Premium commercial finish with neutral-to-slightly-warm highlights, deep clean blacks, restrained saturation and smooth highlight rolloff. Pristine product presentation: no dust, fingerprints, scratches, haze, lens flare, heavy grain, fake HDR halos, or exaggerated bloom.
```

## Output Rule

Return the prompt only unless the user also requested settings/JSON.

Do not append generation claims, tool results, or an unsolicited image.
