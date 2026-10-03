# PROMPT ONLY Workflow

Status: RUNTIME KNOWLEDGE
Task: 6.6

Purpose: produce the strongest usable cinematic image prompt/spec without triggering image generation or editing, even when the host has image tools.

Use when:

- the user explicitly asks for a prompt;
- the user names a target provider/model but does not ask the current host to execute;
- the host has no image-generation/editing capability;
- the user wants a reusable prompt, shot recipe, or provider handoff.

## Hard Rule

```text
PROMPT ONLY = never auto-generate or auto-edit
```

Host capability does not override this user instruction.

## Entry Resolution

Before writing the prompt:

1. identify task type: new generation, edit, repair, or reference-conditioned generation;
2. extract explicit locks and preservation requirements;
3. infer only missing values using the Cinematic Shot Spec;
4. determine target provider/model if named;
5. if provider is unknown, use the generic adapter;
6. run a V0 Reality Gate on the designed shot before prompt serialization.

## Prompt Construction Order

Provider-neutral default order:

```text
1. subject / action / story beat
2. environment / production design / time / weather
3. composition / camera position / shot size / framing
4. capture format / lens character / focal / depth
5. motivated lighting / exposure
6. color / tone / grade
7. skin / hair / fabric / materials / physical realism
8. motion / atmosphere / justified texture
9. preservation / change boundaries for edits
10. output / aspect / orientation requirements
```

Do not stuff every field into every prompt. Include only information that materially controls the result.

## Generation Prompt Behavior

For a new image:

- state the visual subject and action early;
- make spatial relationships concrete;
- describe camera position before relying on focal-length shorthand;
- describe the visible consequence of camera/lens/film references;
- describe motivated sources rather than generic `cinematic lighting`;
- include realism requirements positively where possible;
- add grain/halation/flare only when justified;
- preserve AUTO restraint: unspecified effects stay absent unless needed.

## Edit / Reality Repair Prompt Behavior

Always separate:

```text
WHAT TO PRESERVE
WHAT TO CHANGE
```

For targeted repair:

- preserve identity, pose, composition, product, wardrobe, text, background, and lighting unless the diagnosis requires a specific change;
- change the smallest possible region/system;
- describe the desired corrected state, not only the defect;
- include provider-specific regional controls only when the target adapter confirms support.

## Reference-Match Prompt Behavior

- state the role of each reference;
- transfer observable visual DNA, not hidden metadata claims;
- preserve target subject/product identity unless explicitly asked to copy content;
- convert uncertain hardware inference into visible traits instead of asserting exact gear.

## Provider Naming

If a provider/model is named:

```text
Cinematic Shot Spec
-> provider adapter
-> provider-ready prompt
```

If the exact model is unknown, outdated, or unsupported:

- do not invent syntax;
- fall back to the generic prompt structure;
- optionally note that provider-specific controls were not assumed.

## Negative / Avoidance Guidance

Avoid universal negative-prompt dumping.

Use:

- explicit `negative prompt` only when the target provider supports it and the adapter recommends it;
- otherwise translate avoidances into positive desired-state language.

Example:

```text
Avoid: plastic skin
```

becomes:

```text
natural unretouched skin with region-specific pores, fine texture, subtle tonal variation, and source-consistent specular response
```

## Output Contract

Return only what the user needs:

### Minimal prompt request
- final provider-ready prompt;
- optional compact negative/avoidance line if useful.

### Advanced/expert request
May additionally include:
- Cinematic Shot Spec summary;
- locked vs AUTO values;
- provider translations / unsupported controls;
- Reality Gate notes.

### Text-only host
A prompt/spec is a complete successful output when generation was not requested from the current host.

## Failure / Partial States

`partial` when:
- a named provider has unknown current capabilities;
- a reference image was described but not actually available;
- a hard contradiction remains unresolved.

`blocked` only when the requested prompt fundamentally depends on missing information that cannot be safely inferred, such as an edit prompt requiring preservation of a specific unseen target image whose content is not described.

## Verification

Before final prompt delivery, confirm:

- user locks preserved;
- no unsupported hardware facts invented;
- perspective/camera position coherent;
- lighting source logic coherent;
- depth/motion physically plausible;
- effects restrained;
- edit preservation boundaries explicit where relevant;
- provider syntax is adapter-owned, not core truth.

Acceptance: a user can request a prompt for any supported workflow and receive a portable, provider-adapted result without the skill attempting generation.