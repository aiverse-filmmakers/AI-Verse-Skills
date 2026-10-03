# Phase 1 Research - Secondary Public Skills and Workflows

Status: SECONDARY EVIDENCE ONLY

This file intentionally sits below first-party/manufacturer/provider research in authority.

The purpose is to identify useful architecture, empirical prompting patterns, failure modes, and test ideas. Nothing in this file may override stronger evidence in `source-ledger.md`.

## Hard Contamination Rule

Third-party skill text is never imported as cinematic truth merely because it sounds plausible.

A secondary source may contribute only one of these:

1. architecture pattern;
2. workflow idea;
3. terminology worth independently checking;
4. empirical hypothesis to test;
5. example of a common failure mode;
6. provider-version clue that must be reverified against official evidence.

It may not independently establish:

- real lens physics;
- real camera color behavior;
- film-stock chemistry;
- hidden provider implementation;
- current undocumented controls;
- exact model capability.

## Source A - fal-ai-community Cinematography Skill

Source:

`https://github.com/fal-ai-community/skills/blob/main/skills/cinematography/SKILL.md`

Classification: secondary public implementation.

Useful ideas:

- separate subject, context, lens/framing, motion, atmosphere, mood/color and output controls;
- use concrete visual direction instead of generic `cinematic` prestige language;
- check physical plausibility between camera/lens/shot choices;
- treat lighting, blocking and environment specificity as stronger correction levers than adding more adjectives;
- keep model routing separate from cinematography reasoning.

What we do **not** inherit automatically:

- its provider/model ranking;
- its video-first scope;
- exact prompt acronym/order as a mandatory reasoning chain;
- any camera/lens claim not independently supported.

Usefulness to this project:

`CORROBORATING ARCHITECTURE`.

It supports our decision to keep the universal shot description structured while retaining a separate provider adapter layer.

## Source B - Replicate `prompt-images` Skill

Source:

`https://github.com/replicate/skills/blob/main/skills/prompt-images/SKILL.md`

Classification: secondary implementation maintained by a model platform; useful for transferable prompting observations but not a primary cinematography source.

Useful empirical ideas:

- natural-language prompts outperform keyword-stuffing for many modern models;
- explicit material descriptions improve control;
- reference-image roles should be clear;
- edits benefit from explicit preservation language;
- perspective/angle changes are often harder than local edits;
- model capability differs substantially by task, so fighting the wrong model with more prompt text is inefficient;
- iteration is often better than attempting every correction in one edit.

What we do **not** inherit automatically:

- exact model recommendations;
- generic claims that all current models behave the same;
- any film/lens examples as physical evidence;
- broad prompt-length prescriptions as universal law.

Usefulness to this project:

`EMPIRICAL CROSS-CHECK` for prompt construction and Reality Repair design.

## Source C - OSideMedia Higgsfield Cinema Skill

Source:

`https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/skills/higgsfield-cinema/SKILL.md`

Classification: unofficial third-party Higgsfield workflow package.

Useful ideas:

- aggressively version provider-specific workflows because Cinema Studio surfaces can change;
- separate UI controls from prompt text rather than duplicating everything in both places;
- treat hero-frame creation as an important visual anchor;
- keep recurring character/location/prop references role-specific;
- validate prompt/control compatibility against the active provider version.

Important caution:

The skill contains detailed version-specific statements. Those statements are **not** accepted into our provider adapter unless reverified against official Higgsfield docs, public schema, or official Higgsfield skill/CLI evidence.

Usefulness to this project:

`VERSION-DRIFT WARNING` and `WORKFLOW HYPOTHESIS`, not authority.

## Official Public Agent Skills as Architecture References

Two public skills reviewed during Phase 1 are actually first-party provider material rather than third-party evidence:

- `higgsfield-ai/skills`;
- `black-forest-labs/skills`.

They are recorded elsewhere as provider-specific evidence.

They are especially useful architecturally because they demonstrate:

- a small routing `SKILL.md` plus deeper references;
- progressive disclosure;
- provider-specific prompt rules separated from task routing;
- model/version validation instead of assuming stale capabilities.

We may reuse these **architecture concepts**, but not copy their prose.

## Rejected Patterns

Phase 1 explicitly rejects these common public-prompt patterns unless later testing proves a narrow provider benefit:

### Prestige-word stacks

```text
masterpiece, award winning, 8K, ultra detailed, cinematic, hyper realistic
```

These are not a substitute for optical, physical or compositional direction.

### Universal camera suffixes

```text
ARRI Alexa 35 + 50mm + f/1.4 + Kodak 500T
```

appended to every scene regardless of story.

The shot must choose the capture package, not the other way around.

### Anamorphic caricature

```text
blue streak flare + huge oval bokeh + warped edges
```

applied whenever the word anamorphic appears.

### Maximum-shallow-DOF default

A cinematic image may require deep focus, moderate depth, or environmental readability.

### Mandatory teal/orange

Color separation is not synonymous with teal/orange grading.

### Negative prompt dumping

Some providers do not support negative prompts or handle them inconsistently. Avoidance logic belongs in adapters.

### Fake exact metadata from references

A reference frame cannot establish an exact lens/camera/stock solely from appearance with sufficient certainty for a hard factual claim.

## Secondary Evidence Promotion Rule

A secondary insight may become a runtime rule only when one of the following occurs:

### Route A - Primary confirmation

An official/manufacturer/standards source supports it.

### Route B - Cross-source corroboration

Multiple strong independent sources agree and the claim is not contradicted by primary evidence.

### Route C - Empirical eval

The behavior is explicitly classified as `MODEL-BEHAVIOR` and repeatable tests demonstrate it improves results for the target provider.

In Route C, the runtime rule must remain provider-specific rather than being presented as physical truth.

## Test Ideas Harvested from Secondary Sources

Add to later eval design:

- compare natural-language cinematic specification against prestige-word-heavy prompting;
- compare one-pass edit against staged preservation-sensitive edits;
- test explicit preserve/change separation;
- test camera/lens name alone versus name + observable optical traits;
- test provider-native UI controls versus duplicating those same values in prompt text;
- test unknown-provider fallback with no model-specific syntax;
- test deep-focus scenes to ensure the skill does not default to shallow DOF;
- test reference matching without exact-hardware hallucination;
- test provider version mismatch failure behavior.

## Task 1.10 Conclusion

Secondary public skills are useful for architecture and empirical hypotheses, but the project remains intentionally uncontaminated by weaker unverified cinematic claims.

Primary knowledge authority remains:

1. user locks/current task;
2. physical/technical principles;
3. first-party manufacturer evidence;
4. official provider evidence;
5. corroborated technical/practitioner evidence;
6. empirical provider evals;
7. secondary public workflows.
