# AI-Verse Cinematic Realism Director

A portable Agent Skill for directing, generating, editing, diagnosing, and adapting cinematic still images with grounded cinematography and physical-realism logic.

It works from either a one-sentence beginner request or a detailed expert camera setup. The core direction system is provider-independent; adapters translate the same resolved shot for OpenAI Images, Gemini, Seedream, FLUX, Magnific Cinematic, Higgsfield Soul Cinema, or a generic image model.

## Start Here

### One sentence is enough

```text
woman waiting for a taxi in London at night
```

The skill can infer composition, camera position, optics, depth, motivated lighting, exposure, color, materials, atmosphere, and realism treatment without requiring technical camera knowledge.

Default behavior is **AUTO DIRECT**.

### Lock technical choices when they matter

```text
Low-angle medium-wide frame. 35mm capture character, 24mm rectilinear lens, f/4, deep enough focus to keep the environment readable, hard side sunlight, no flare, no haze.
```

Explicit technical values become locks. AUTO fills only the unspecified compatible decisions.

### Repair an existing image without redesigning it

```text
Make this image feel less AI-generated. Preserve the identity, pose, wardrobe, framing, background geometry, and lighting direction. Repair only the realism problems.
```

Reality Repair follows:

```text
PRESERVE
-> DIAGNOSE
-> REPAIR
-> ALLOW CHANGE
-> VERIFY
```

### Prompt only

```text
Give me the final Seedream prompt only. Do not generate anything.
```

`PROMPT ONLY` prevents generation even when the host has image tools available.

## What It Does

The skill can:

- direct a complete cinematic still from a minimal idea;
- cinematize an ordinary prompt without changing its concept;
- diagnose and repair AI-looking images while preserving important content;
- reverse-engineer observable visual DNA from references;
- obey locked camera, lens, focal, aperture, shot, lighting, stock, color, and texture choices;
- explain a professional shot recipe;
- output provider-specific prompts without generating;
- generate or edit directly when the current host exposes a suitable image capability.

It does not depend on one provider, one camera aesthetic, or a fixed `cinematic` preset.

## Workflows

- **AUTO DIRECT** — minimal idea to complete shot.
- **CINEMATIZE** — strengthen an existing concept without concept drift.
- **REALITY REPAIR** — preserve, diagnose, repair minimally, verify.
- **REFERENCE MATCH** — transfer observable visual DNA without inventing exact hardware facts.
- **MANUAL CAMERA** — lock explicit technical values and complete only the missing ones.
- **PROMPT ONLY** — return the adapted prompt/spec and never generate.

See `references/INDEX.md` for the progressive-loading map.

## Core Architecture

```text
USER INTENT
-> CINEMATIC SHOT SPEC
-> REALITY GATE
-> PROVIDER / HOST ADAPTER
-> IMAGE OR PRODUCTION-READY PROMPT
```

The universal shot remains authoritative. Provider syntax never becomes the creative brain.

## Reality Gate

Before final handoff, the skill checks whether a real camera could plausibly record the scene under the requested conditions while respecting the intended stylization.

The gate evaluates, in dependency order:

```text
locks / preservation
-> geometry / perspective
-> focus / depth / motion
-> lighting
-> exposure / color
-> shadows / reflections
-> anatomy / skin / hair / eyes
-> fabric / materials
-> contact / gravity / environment
-> atmosphere
-> optical effects
-> stylization restraint
-> provider integrity
```

Realism does not mean automatically adding grain, pores, dirt, haze, flare, asymmetry, or vintage artifacts.

## Provider Adapters

Included adapters:

- Generic
- OpenAI Images
- Gemini
- Seedream
- FLUX
- Magnific Cinematic
- Higgsfield Soul Cinema

Provider adapters translate the resolved shot into current provider behavior. They do not override user locks or grant access to a provider by themselves.

If a provider changes or an exact control is unavailable, the skill falls back to observable natural-language intent rather than inventing unsupported settings.

## Standalone Installation

The **entire `cinematic-realism-director/` folder is the portable unit**.

Copy that folder into an Agent Skills-compatible environment that can load a `SKILL.md` package.

Core prompt/spec operation requires only files inside this directory. It does not require:

- AI-Verse OS;
- sibling AI-Verse skills;
- repository-root documents;
- MCP;
- an API key;
- a private filesystem path;
- any particular image provider.

Image generation and editing remain optional host capabilities.

Start with `SKILL.md`. A capable loader can then use `references/INDEX.md` to load only the knowledge relevant to the active task.

## Package Layout

```text
SKILL.md             portable behavior contract
aiverse.skill.yaml   AI-Verse runtime sidecar
references/          cinematography, realism, workflow, and provenance knowledge
adapters/            provider translation only
schemas/             structured shot, diagnosis, and reference-DNA contracts
examples/            usage examples
evals/               behavioral and regression evaluation corpus
CHANGELOG.md          release history
```

## Design Principles

- story before prestige camera/lens tokens;
- explicit user value = lock;
- AUTO fills only missing decisions;
- perspective comes primarily from camera position, not focal length alone;
- wide rectilinear is not fisheye;
- cinematic does not automatically mean shallow depth, grain, flare, haze, rim light, or teal/orange;
- observable reference traits are not exact hardware facts;
- preserve before transforming;
- provider syntax stays downstream of the universal shot design;
- successful tool execution is not proof of visual-quality success.

## Examples

- `examples/beginner-auto.md`
- `examples/expert-locks.md`
- `examples/reality-repair.md`
- `examples/reference-match.md`
- `examples/prompt-only.md`

## Evaluation

The package includes routing, beginner AUTO, expert-lock, repair, reference-match, provider-consistency, anti-cliche, physical-plausibility, adversarial, and regression evals.

`evals/benchmark-matrix.md` defines the matched benchmark required before making any claim that this skill outperforms another cinematic image system.

## Scope

This is a **still-image** cinematic direction and realism skill. Video timelines, cuts, temporal continuity, lip-sync, and motion choreography remain outside its primary authority.

## License

MIT. See the repository license for details.
