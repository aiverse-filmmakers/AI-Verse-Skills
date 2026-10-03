# AI-Verse Cinematic Realism Director

A portable Agent Skill for designing, generating, editing, diagnosing, and adapting cinematic still images with grounded cinematography and physical-realism logic.

It works from either a one-sentence beginner request or a detailed expert camera setup. The core skill is provider-independent; provider adapters translate the same resolved shot into OpenAI Images, Gemini, Seedream, FLUX, Magnific Cinematic, Higgsfield Soul Cinema, or a generic natural-language prompt.

## What It Does

The skill can:

- direct a complete cinematic still from a minimal idea;
- cinematize an ordinary prompt without changing its concept;
- diagnose and repair AI-looking images while preserving important content;
- reverse-engineer observable visual DNA from references;
- obey locked camera, lens, focal, aperture, shot, lighting, stock, color, or texture choices;
- explain a professional shot recipe;
- output provider-specific prompts without generating;
- generate or edit directly when the current host actually exposes a suitable image capability.

It does **not** depend on one provider, one camera aesthetic, or a fixed `cinematic` preset.

## Beginner Use

A beginner can simply say:

```text
woman waiting for a taxi in London at night
```

The skill should infer the missing composition, camera position, optics, depth, motivated lighting, exposure, color, materials, atmosphere, and realism treatment without asking unnecessary technical questions.

Default beginner behavior is **AUTO DIRECT**.

## Expert Use

An expert can lock any values explicitly:

```text
Low-angle medium-wide frame. 35mm capture character, 24mm rectilinear lens, f/4, deep enough focus to keep the environment readable, hard side sunlight, no flare, no haze.
```

Every explicit technical value becomes a lock. AUTO fills only unspecified compatible values.

The skill never silently changes a locked value merely because another choice would be easier for a provider.

## Main Workflows

- **AUTO DIRECT** — minimal idea to complete shot.
- **CINEMATIZE** — strengthen an existing concept without concept drift.
- **REALITY REPAIR** — preserve, diagnose, repair minimally, verify.
- **REFERENCE MATCH** — transfer observable visual DNA without inventing exact hardware facts.
- **MANUAL CAMERA** — lock explicit technical values and complete only the missing ones.
- **PROMPT ONLY** — return the adapted prompt/spec and never generate.

See `references/INDEX.md` for the progressive-loading map.

## Direct Generation vs Prompt-Only

The package separates cinematic reasoning from host execution.

```text
WHAT THE SHOT SHOULD BE
!=
WHAT THE CURRENT HOST CAN EXECUTE
```

If the user requests an image and the host has a suitable permitted image tool, the skill should generate or edit directly.

If no suitable image tool exists, it returns the strongest executable prompt/specification instead.

If the user explicitly asks for prompt-only, JSON-only, settings-only, or no generation, that instruction is absolute even when image tools are available.

An adapter file does not grant access to that provider.

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

Realism does not mean adding grain, pores, dirt, haze, flare, asymmetry, or vintage artifacts.

## Standalone Installation

The **entire `cinematic-realism-director/` folder is the portable unit**.

Copy that folder into any Agent Skills-compatible environment that can load a `SKILL.md` package.

Core prompt/spec operation requires only files inside this directory. It does not require:

- AI-Verse OS;
- sibling AI-Verse skills;
- repository-root documents;
- MCP;
- an API key;
- a private machine path;
- any particular image provider.

Image generation/editing remains optional host capability.

Start with `SKILL.md`. A capable loader should then use `references/INDEX.md` to load only the knowledge relevant to the active task.

## Using It Inside AI-Verse-Skills

Within the full repository, the canonical package lives at:

```text
skills/imported/ai-verse/cinematic-realism-director/
```

`aiverse.skill.yaml` declares AI-Verse runtime expectations. The manifest describes possible capabilities; it does not authorize them.

The portable `SKILL.md` remains the behavioral contract.

## Package Layout

```text
SKILL.md                 portable behavior contract
aiverse.skill.yaml       AI-Verse runtime sidecar
references/              progressively loaded cinematography/realism knowledge
adapters/                provider translation only
schemas/                 structured shot, diagnosis, and reference-DNA contracts
examples/                illustrative usage, never hidden mandatory rules
evals/                   behavioral and regression evaluation corpus
PHASE_*_AUDIT.md          implementation verification records
STATUS.md                 authoritative build/restart state
```

## Important Principles

- story before prestige camera/lens tokens;
- explicit user value = lock;
- AUTO fills only missing decisions;
- perspective comes primarily from camera position, not focal length alone;
- wide rectilinear is not fisheye;
- cinematic does not mean shallow depth, grain, flare, haze, rim light, or teal/orange;
- observable reference traits are not exact hardware facts;
- preserve before transforming;
- provider syntax stays downstream of the universal shot design;
- successful tool execution is not proof of visual-quality success.

## Examples

See:

- `examples/beginner-auto.md`
- `examples/expert-locks.md`
- `examples/reality-repair.md`
- `examples/reference-match.md`
- `examples/prompt-only.md`

## Current Scope

V1 is a **still-image** cinematic direction and realism skill. Video timelines, cuts, temporal continuity, lip-sync, and motion choreography are outside its primary authority.
