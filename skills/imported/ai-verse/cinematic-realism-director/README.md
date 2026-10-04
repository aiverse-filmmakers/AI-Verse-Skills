# AI-Verse Cinematic Realism Director

A portable Agent Skill that turns simple or expert still-image requests into professional photographic or cinematic direction with strong composition, motivated lighting, premium tonal/color finishing, physical realism, and provider-independent control.

The core promise is simple:

> **The user should not need to know cinematography or photography language to receive professional-quality output.**

A one-line request should be interpreted the way the best professional for that exact image type would approach it.

## Professional by Default

Examples:

```text
iPhone mirror selfie in a hotel room
```

The skill should treat this like elite mobile photography/editing—not disguise it as a cinema-camera frame.

```text
candid photo of two friends laughing outside a restaurant
```

The skill should behave like a top candid/editorial photographer: decisive moment, believable access, layered context, excellent exposure/color, natural body language, subtle photographic texture.

```text
woman waiting for a taxi in London at night
```

The skill should behave like feature-film cinematography: intentional narrative hierarchy, motivated practical light, premium highlight rolloff, rich readable shadows, professional color separation, natural skin/material response, realistic depth, subtle organic filmic texture, and a restrained movie-grade finish.

You should not have to append:

```text
professional
cinematic
Hollywood
ARRI
high quality
good lighting
good composition
realistic
```

AUTO DIRECT fills that gap automatically.

## Medium-Aware Excellence

The Professional Quality Floor adapts to the requested medium:

- **iPhone / selfie / mobile** → elite mobile photographer + editor
- **candid / documentary / street** → elite documentary/editorial photographer
- **narrative / movie-like scene** → feature-film cinematographer
- **portrait / beauty** → top portrait/beauty photographer
- **fashion / editorial** → top editorial/fashion photographer
- **product** → world-class commercial product photographer
- **automotive** → specialist automotive campaign photographer
- **food** → specialist food photographer
- **architecture / interiors** → elite architectural photographer
- **travel / hospitality** → top travel/hospitality photographer or cinematographer

Professionalization does **not** erase the requested medium. A phone image remains a phone image; a candid remains candid; architecture follows architectural-photography logic.

## Default Photographic Finish

For normal photographic/cinematic work, AUTO generally aims for:

```text
intentional professional composition
professional exposure hierarchy
controlled highlight rolloff
natural shadow density
clean color separation
credible skin/material response
realistic optical/focus transition
subtle organic filmic texture
high-end restrained color finishing
physical realism
```

For cinematic/narrative work, premium digital-cinema tonal behavior and **ARRI-like highlight rolloff / skin-tone response** may be used as observable targets. This does not claim literal ARRI capture or simulation.

Subtle organic filmic texture is normally present on photographic output unless the user or medium calls for pristine/no-grain cleanliness. Strong grain, halation, flare, haze, bloom, teal/orange, rim light, or other visible effects are still optional—not automatic.

## Native-First Image Generation

If the user does **not** name a provider, execution priority is:

```text
1. host-native/local image generation or editing
2. permitted external MCP/plugin/connector only when native/local lacks a material required capability
3. production-ready prompt/spec fallback
```

If the user explicitly names a provider, that provider becomes a lock when actually available/permitted.

An MCP/external tool is never preferred merely because it looks more cinematic, specialized, premium, or exposes more controls.

## Magnific and Higgsfield

Magnific Cinematic and Higgsfield Soul Cinema are **competitor/reference systems**, not automatic backends for this skill.

Their adapters exist only for:

- explicit user-requested prompt export;
- explicit user-requested execution when connected;
- controlled comparative benchmarking;
- provider compatibility/research.

Ordinary image generation must not auto-route to Magnific or Higgsfield.

## Workflows

- **AUTO DIRECT** — minimal idea → professional complete shot.
- **CINEMATIZE** — strengthen an existing concept without concept drift.
- **REALITY REPAIR** — preserve → diagnose → repair minimally → verify.
- **REFERENCE MATCH** — transfer observable visual DNA without inventing hardware facts.
- **MANUAL CAMERA** — lock explicit camera/optical/lighting choices and fill only the missing decisions.
- **PROMPT ONLY** — return the adapted prompt/spec and never generate.

## Expert Locks

You can still specify as much technical detail as you want:

```text
Low-angle medium-wide frame. ARRI ALEXA 35 character, 24mm rectilinear lens, f/4, deep enough focus to keep the environment readable, hard side sunlight, no flare, no haze.
```

Explicit technical values become locks. AUTO fills only unspecified compatible fields.

## Reality Repair

For existing AI-looking images:

```text
Make this image feel less AI-generated. Preserve identity, pose, wardrobe, framing, background geometry and lighting direction. Repair only the realism problems.
```

The workflow is:

```text
PRESERVE
-> DIAGNOSE
-> REPAIR
-> ALLOW CHANGE
-> VERIFY
```

Local problems should not trigger unnecessary scene redesign.

## Prompt Only

```text
Give me the final Seedream prompt only. Do not generate anything.
```

`PROMPT ONLY` prevents all image execution, even when native/external image tools are available.

## Core Architecture

```text
USER INTENT
-> REQUESTED / IMPLIED IMAGE MEDIUM
-> PROFESSIONAL QUALITY FLOOR
-> CINEMATIC SHOT SPEC
-> REALITY GATE
-> EXECUTION PRIORITY
-> PROVIDER ADAPTER FOR THE CHOSEN PATH
-> IMAGE OR PRODUCTION-READY PROMPT
```

Provider syntax never becomes the creative brain.

## Anti-Cliche Discipline

Professional quality does not mean stacking every stereotypical cinema effect.

AUTO does not automatically add:

- anamorphic blue streaks;
- teal/orange grading;
- haze/fog;
- dramatic rim light;
- maximum background blur;
- Dutch angle;
- heavy bloom;
- obvious halation;
- strong vignette;
- crushed blacks;
- arbitrary motion blur.

The goal is **professional finishing without cliché stacking**.

## Provider Adapters

Normal translation adapters:

- Generic
- OpenAI Images
- Gemini
- Seedream
- FLUX

Explicit-target / benchmark-only adapters:

- Magnific Cinematic
- Higgsfield Soul Cinema

Adapters translate an already-resolved shot. They do not select the provider or invent the creative direction.

## Standalone Installation

The entire `cinematic-realism-director/` folder is the portable unit.

Copy it into an Agent Skills-compatible environment that can load `SKILL.md`.

Core prompt/spec operation requires only files inside this folder. It does not require:

- AI-Verse OS;
- sibling AI-Verse skills;
- repository-root docs;
- MCP;
- an API key;
- any specific image provider.

Image generation/editing remains a host capability.

Start with `SKILL.md`; `references/INDEX.md` provides the progressive-loading map.

## Package Layout

```text
SKILL.md             portable behavior contract
aiverse.skill.yaml   AI-Verse runtime sidecar
references/          professional-quality, cinematography, realism and workflow knowledge
adapters/            provider translation only
schemas/             structured shot, diagnosis and reference-DNA contracts
examples/            usage examples
evals/               behavioral and regression evaluation corpus
CHANGELOG.md          release history
```

## Evaluation

The package includes evals for:

- routing;
- Professional Quality Floor;
- native-first execution priority;
- beginner AUTO;
- expert locks;
- Reality Repair;
- Reference Match;
- adapter behavior;
- anti-cliche behavior;
- physical plausibility;
- adversarial boundaries;
- permanent regressions.

`evals/benchmark-matrix.md` defines the controlled benchmark required before making any claim that the skill outperforms Magnific/Higgsfield or another cinematic system.

## Scope

This is a **still-image** visual-direction and realism skill. Video timelines, cuts, temporal continuity, lip-sync, and motion choreography remain outside its primary authority.

## License

MIT. See the repository license for details.
