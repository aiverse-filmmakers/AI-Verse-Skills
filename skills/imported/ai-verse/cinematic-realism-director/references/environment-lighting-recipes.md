# Environment-Specific Lighting Decision Recipes

Status: RUNTIME KNOWLEDGE
Task: 4.3

These are decision patterns, not fixed prompt templates. Each recipe decomposes the environment into source motivation, source geometry, ambient/fill behavior, exposure hierarchy, material response, and common failure modes.

Use with:

- `references/motivated-lighting.md`
- `references/lighting-roles.md`

## 1. Governing Rule

A recipe is a starting hypothesis.

The user request, location, time, weather, subject, wardrobe, material, and locked parameters always outrank it.

Do not paste every recipe ingredient into every shot.

## 2. Overcast Exterior

### Physical idea

Cloud cover turns the sky into a very large source, reducing hard direct-sun shadows.

### Default structure

```text
key: broad sky direction
ambient: sky + ground/environment bounce
fill: naturally high unless negative fill is introduced
edge: weak or absent
contrast: low to moderate
```

### Good uses

- documentary;
- natural portrait;
- fashion with soft skin;
- automotive with broad sky reflections;
- architecture with controlled exterior contrast.

### Avoid

- hard noon-like cast shadows;
- bright artificial rim light;
- fake sun shafts without a break in cloud/haze logic;
- flattening every surface to identical value.

## 3. Hard Noon Sun

### Physical idea

Small apparent solar source, high elevation, strong direct/ambient separation.

### Default structure

```text
key: hard overhead/high sun
fill: blue sky + ground bounce
shadows: defined and directionally coherent
speculars: strong on glossy surfaces
contrast: high but environment-dependent
```

### Design choices

- embrace graphic shadow geometry;
- move subject into shade if flattering portraiture is required;
- use architecture/trees as negative/positive shaping elements;
- allow some hot highlights rather than forcing HDR recovery everywhere.

### Avoid

- magically soft facial light while keeping hard ground shadows;
- multiple incompatible sun directions;
- crushed shadows with zero sky contribution;
- sunset color at noon without stylization request.

## 4. Golden Hour

### Physical idea

Low sun angle, longer atmospheric path, warm direct component, cooler sky fill often available.

### Default structure

```text
key/backlight: low sun
fill: sky/environment
color: warm direct light with potentially cooler ambient
shadow length: long
contrast: variable depending haze and orientation
```

### Good uses

- travel;
- portrait;
- automotive;
- landscape;
- emotional narrative.

### Avoid

- making every surface uniformly orange;
- mandatory lens flare;
- perfect rim regardless of sun position;
- visible god rays without atmosphere.

## 5. Blue Hour

### Physical idea

Sun below horizon; sky provides cool broad illumination while artificial sources become visually important.

### Default structure

```text
ambient: cool sky
practicals: warm or colored local sources
key: may be sky, storefront, streetlight, or production enhancement
contrast: controlled low-light separation
```

### Good uses

- urban travel;
- architecture;
- moody portrait;
- automotive.

### Avoid

- pitch-black sky at true blue hour;
- neon color on surfaces that do not face neon sources;
- making all practicals equally bright.

## 6. Natural Window Daylight Interior

### Default structure

```text
key: window side
ambient: room bounce
fill: environment or controlled card
negative fill: optional opposite side
practicals: secondary motivation/depth
background: naturally falls with distance from window
```

### Exposure logic

Interior may be prioritized while exterior remains brighter.

Do not force both interior and exterior into perfectly equal exposure unless the setup intentionally balances them.

### Avoid

- perfectly lit face far from tiny window without added source;
- contradictory shadow direction;
- completely neutralized mixed practical/daylight color.

## 7. Tungsten Practical Interior

### Default structure

```text
key: practical lamp or production source motivated by it
ambient: warm room bounce + optional cooler exterior spill
falloff: local and spatially noticeable
```

### Good uses

- intimate narrative;
- hospitality;
- evening lifestyle;
- warm commercial interiors.

### Avoid

- one table lamp illuminating huge room evenly;
- pure orange wash across all surfaces;
- perfectly clean white shadows if environment is genuinely warm.

## 8. Fluorescent / Office Interior

### Default structure

```text
key/ambient: overhead fixtures
fill: floor/wall environment
contrast: often flatter vertically, stronger eye-socket/top-down effects
color: may be neutral, green-biased, or mixed depending fixture
```

### Creative options

- embrace institutional flatness;
- selectively shape with negative fill;
- add window side-source if location supports it.

### Avoid

- generic cinematic rim that contradicts overhead-only setting;
- forcing warm tungsten mood into cool office without source.

## 9. Neon City Night

### Source inventory

- signs;
- storefronts;
- streetlights;
- headlights;
- screens;
- city ambient.

### Default logic

Choose one or two dominant source families.

Color contamination should be strongest on surfaces facing or near those sources.

### Avoid

- equal cyan left / magenta right by default;
- full-face uniform neon paint;
- random colored highlights unrelated to signs;
- identical color split on every object.

## 10. Moonlit Exterior

### Realism note

Literal moonlight is weak, but cinematic moonlight is commonly enhanced.

Use M1-M2 motivation:

```text
key: cool directional moon-equivalent or motivated night source
ambient: sky/environment
practicals: optional warm local sources
```

### Avoid

- treating moonlight as daylight with blue filter;
- hard multiple moon shadows;
- excessive cyan saturation;
- bright sky and pitch-black landscape with no exposure logic.

## 11. Candlelight / Firelight

### Default structure

```text
key: small warm local source
falloff: rapid
ambient: minimal unless another source exists
speculars: warm and source-local
```

### Good uses

- intimate face close to source;
- table scene;
- historical atmosphere;
- firelit environment.

### Avoid

- one candle evenly lighting a large hall;
- zero falloff;
- huge cool rim with no second source;
- eye highlights inconsistent with flame position.

## 12. Commercial Soft Source

### Physical idea

Large controlled source designed to flatter surfaces while retaining dimensionality.

### Default structure

```text
key: large soft source
fill: deliberate and restrained
negative fill: used to preserve shape
edge: optional
background: independently controlled only if spatially plausible
```

### Product/beauty goal

Clarity and form take priority over darkness or mood.

### Avoid

- making `commercial` synonymous with flat light;
- making `cinematic` synonymous with low-key;
- impossible specular reflections.

## 13. Documentary Available Light

### Default structure

```text
use existing sources
preserve imperfections
avoid polished multi-light look unless source actually supports it
```

Prioritize:

- believable exposure compromises;
- practical falloff;
- mixed color;
- real shadow density;
- natural asymmetry.

### Avoid

- beauty rim;
- excessive fill;
- pristine studio catchlights;
- local relighting of every face.

## 14. Product Studio - Glossy

### Goal

Describe geometry through reflected source shape.

### Structure

```text
large strip/card reflections
controlled edge highlights
clean contact shadow
background separation
label/brand legibility
```

### Avoid

- random sparkle;
- highlights painted where no source could reflect;
- floating object contact;
- perfectly uniform glass brightness.

## 15. Product Studio - Matte

Use broad directional light to reveal:

- surface relief;
- edges;
- printing;
- texture.

Avoid excessive specular treatment.

## 16. Automotive Day Exterior

### Default structure

```text
sun/sky/environment are the source system
body shape revealed by sky gradients and environment reflections
```

### Choose orientation deliberately

- front three-quarter for face/body relationship;
- side for profile and wheelbase;
- low sun for long gradients;
- overcast for smooth paint reflections.

### Avoid

- arbitrary white reflection streaks;
- sky reflection inconsistent across body panels;
- wheels/ground shadow indicating different sun direction.

## 17. Automotive Controlled Night

Use:

- long soft sources;
- edge reflections;
- selective pools of background light;
- wet ground only if requested/contextual.

Avoid cyberpunk neon unless the concept actually requires it.

## 18. Food / Tabletop

### Default structure

Side/back-side light often reveals texture well.

Use:

```text
soft directional source
controlled fill
specular management on sauces/liquids
natural contact shadows
```

### Avoid

- overhead flatness unless graphic look is intended;
- every surface sparkling;
- steam illuminated without plausible back/side source.

## 19. Architecture Interior

### Source hierarchy

- windows;
- practical fixtures;
- skylights;
- reflected daylight;
- designed architectural lighting.

### Priorities

- believable window/exterior relationship;
- coherent room falloff;
- readable materials;
- verticals and spatial depth preserved;
- fixtures influence nearby surfaces plausibly.

### Avoid

- impossible global fill;
- hidden beauty light on furniture;
- every room zone independently exposed.

## 20. Architecture Exterior

Resolve:

- sun orientation;
- sky condition;
- facade material;
- glass reflection;
- surrounding environment;
- interior practical visibility at dusk/night.

Avoid reflections that ignore sky/buildings/camera position.

## 21. Dense Forest / Dappled Sun

Direct light is broken by foliage.

Use:

- coherent sun direction;
- irregular occlusion;
- cooler sky fill;
- local dapple patterns that follow geometry.

Avoid evenly distributed random light spots.

## 22. Snow Exterior

Snow becomes a powerful bounce surface.

Expect:

- strong upward fill;
- bright environment;
- potentially cooler shadow contamination;
- highlight clipping risk.

Avoid dark eye sockets that ignore snow bounce unless negative fill or headwear explains them.

## 23. Desert / Sand

Sand provides warm/high-reflectance ground bounce.

Hard sun can produce:

- strong direct key;
- warm lower fill;
- high brightness range;
- atmospheric dust/haze if present.

Avoid applying warm haze everywhere automatically.

## 24. Rain / Wet Night

Wet surfaces increase visible reflections.

Use local light sources to create:

- stretched ground reflections;
- specular edges;
- color pools.

Reflection direction and color must correspond to actual sources.

## 25. Recipe Adaptation Questions

Before using any recipe, ask internally:

1. Is the time/weather actually specified?
2. Does the subject need different exposure than environment?
3. Are there reflective/translucent materials?
4. Is the goal narrative, documentary, fashion, product, automotive, food, architecture, or travel?
5. Are any lighting parameters locked?
6. Does the location supply natural fill or negative fill?
7. Should the shot embrace imperfect available light or polished production control?

## 26. Environment Recipe Reality Gate

A recipe passes only if:

- source direction matches environment;
- softness matches source size/weather;
- ambient fill matches surroundings;
- exposure hierarchy remains plausible;
- materials respond to the source system;
- practicals influence only plausible areas;
- shadows/reflections are coherent;
- no recipe cliché was added merely because of the environment label.

The recipe must serve the actual shot, not become the shot.