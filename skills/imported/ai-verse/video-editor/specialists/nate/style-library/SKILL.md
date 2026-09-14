---
name: style-library
description: Select, customize, or extend reusable motion-graphics styles for an AI-Verse Video Editor project without assuming Nate's example style registry or importing demonstration brand assets. Use when an edit needs a reusable card/takeover language, a project-local style pack, or a style choice that should persist across beats.
---

# AI-Verse Adaptation of Nate's Style-Library Method

Use this specialist to choose and preserve a reusable motion-graphics language for the current video project.

This is an editorial/presentation methodology, not a bundled asset catalog.

## Hard Boundary

Nate's pinned source contains AIS demonstration brand materials that are explicitly not licensed for reuse. AI-Verse does **not** import or redistribute those assets as generic styles.

Do not assume that Nate's root `style-library/`, `style-templates/`, manifests, cards, fonts, logos, or example-project media exist inside AI-Verse.

Use only:

- user-supplied assets;
- project-owned assets;
- licensed assets available through approved providers;
- current HyperFrames registry items whose provenance/compatibility is accepted;
- newly authored project-local graphics.

## Select a Style

Before creating another one-off card:

1. read the current project brief and any `DESIGN.md`;
2. inspect existing video graphics and approved visual decisions;
3. inspect available project-local reusable components and approved HyperFrames registry items;
4. choose the smallest reusable style that supports the editorial beat;
5. record why it fits the story, speaker framing, density, and target format.

Do not replace an approved visual language merely because another style is more novel.

## Overlay Versus Takeover

For overlays:

- preserve transparency outside the graphic;
- protect the speaker's face and important source action;
- keep text glance-readable;
- verify the maximum real copy length, not only a short placeholder.

For takeovers:

- use an intentional full-frame background;
- make the reason for leaving the speaker clear;
- keep the takeover duration proportional to the spoken idea.

## Reuse Contract

A reusable project style should define, as applicable:

- typography roles;
- color/accent roles;
- spacing and surface rules;
- lower-third bounds;
- takeover composition;
- caption treatment;
- motion language;
- allowed text/content slots;
- maximum slot lengths;
- asset dependencies;
- aspect-ratio behavior.

Keep reusable style mechanics generic. Keep project-specific copy and brand content in the project.

## HyperFrames Integration

When a style is implemented in HyperFrames:

- use the canonical 0.8.40 provider contract;
- prefer approved registry components/blocks when they fit;
- localize required project assets;
- keep GSAP deterministic and seek-safe;
- use `data-duration` for visible timing;
- run `npx hyperframes lint` and `npx hyperframes check`;
- preview and render at the actual project resolution before treating a style as proven.

A catalog entry or source snippet is not proof that a style has passed rendered QA.

## Extending the Project Style Library

When the project needs a new reusable style:

1. define a narrow purpose;
2. derive tokens from the current project visual system;
3. define named content slots and bounds;
4. build one representative card or scene;
5. test minimum and maximum realistic copy;
6. test speaker-safe placement and alternate aspect ratios when requested;
7. inspect hero frames and transitions;
8. add it to the project's own reusable style inventory only after it passes.

Do not create global AI-Verse styles from one client's or demonstration brand's assets.

## AI-Verse Adaptation Notes

Adapted from Nate Herk's MIT-licensed `style-library` Skill at `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`.

Preserved:
- reuse-before-rebuild;
- overlay versus takeover distinction;
- slot-bound content;
- project-localized dependencies;
- actual-resolution lint/render QA;
- generic reusable mechanics with project-specific copy kept outside the library.

Deliberately not imported:
- AIS brand materials;
- Nate example style registry;
- Nate project templates/assets;
- root-level style-library build scripts.

Those exclusions are required by provenance, package closure, and the AI-Verse one-provider/one-project-authority model.
