---
name: interface-designer
description: Orchestrate end-to-end interface design for websites, GitHub-hosted HTML artifacts, dashboards, web apps, desktop or native-app UI, prototypes, redesigns, reference recreations, and interaction-heavy or immersive experiences. Classifies scope and the existing delivery target first, then loads only the relevant specialist design, implementation, motion, reference, and QA Skills. Use for broad or multi-stage interface work. Do not use it to force React, Vercel, shadcn, Figma, or any other stack onto a project.
version: 1.0.0
license: MIT
metadata:
  ai-verse:
    ownership: first-party
    category: interface-design
    composite: true
---

# AI-Verse Interface Designer

## Purpose

Design the right interface for the user's actual product and delivery target, then coordinate the smallest set of specialist Skills needed to build and verify it.

This Skill is the orchestrator. It does not replace the taste or methodology of the expert Skills it routes to.

## When to Use

Use for broad or multi-stage requests such as:

- build or redesign a website, dashboard, app interface, persistent HTML artifact, or product UI;
- recreate or adapt an interface from screenshots, video, a URL, or a named reference;
- establish or change a design system;
- design an interaction-heavy component or flow;
- build an immersive scroll-driven experience;
- take a vague interface idea through design direction, implementation, and QA.

For a narrow specialist request, route directly when the specialist is obvious. Examples: animation audit, a single Figma operation, or a React-only performance review.

## Non-Lock-In Rule

The implementation target comes from the user's request and the existing project.

Never migrate a plain HTML/CSS/JavaScript artifact to React merely because React Skills exist. Never require Vercel hosting because a Vercel-authored Skill provides engineering guidance. Never introduce shadcn unless the project already uses it, the user selects it, or a separately justified stack decision chooses it.

Design intelligence is portable. Implementation specialists are conditional.

## Step 1: Read Local Authority

Before substantial design work:

1. Read repository/project instructions.
2. Read an existing `DESIGN.md` if present.
3. Inspect the current implementation stack when code already exists.
4. Treat current user instructions and locked references as authoritative.

Do not redesign an established product accidentally.

## Step 2: Classify Scope

Choose one primary scope:

- `MICRO_CHANGE`
- `COMPONENT`
- `SCREEN`
- `MULTI_SCREEN_FLOW`
- `FULL_PRODUCT`
- `REFERENCE_RECREATION`
- `INTERACTION_HEAVY`
- `DESIGN_SYSTEM_CHANGE`
- `SCROLL_IMMERSIVE`
- `MOBILE_EXPO`

The scope controls pipeline depth. A padding change must not invoke a full-product workflow.

## Step 3: Classify Delivery Target

Choose the actual target before loading implementation experts:

- `PLAIN_HTML_CSS_JS_ARTIFACT`
- `EXISTING_WEB_STACK`
- `REACT_WEB_APP`
- `PWA`
- `FIGMA`
- `CANVA_OR_STATIC_DESIGN_TOOL`
- `DESKTOP_WEBVIEW_APP`
- `NATIVE_DESKTOP_APP`
- `REACT_NATIVE_EXPO`
- `PROTOTYPE_ONLY`
- `DESIGN_ONLY_HANDOFF`
- `CODE_DRIVEN_VIDEO_MOTION_HANDOFF`

When the project already exists, detect rather than assume. Do not change stacks unless the user asks or the existing target cannot satisfy the requirement.

## Step 4: Select Stages

Read [references/routing.md](references/routing.md) for expert meanings and [references/orchestration.json](references/orchestration.json) for the canonical conditional stage graph. Choose only the stages needed for the current scope and target.

The maximum full-product path is:

1. reference analysis when a reference exists;
2. UI/UX intelligence;
3. frontend art direction;
4. prototype divergence when the decision is substantial or ambiguous;
5. create or update `DESIGN.md`;
6. component/information architecture;
7. library/primitives selection when needed;
8. target-specific implementation;
9. interaction physics when relevant;
10. motion construction when relevant;
11. render/preview in the real target;
12. state-based visual QA;
13. animation review when motion exists;
14. web/accessibility review when the target is web;
15. fix failures and rerun affected gates.

This is not a checklist to run blindly.

## Step 5: Preserve Expert Authority

When an expert Skill is selected, use its actual package rather than paraphrasing it from memory.

Do not merge all expert bodies into this context.

Specialist correctness beats generic taste inside its domain. Examples:

- React experts apply only to React targets.
- shadcn rules apply only to shadcn projects.
- Scroll Craft owns its immersive scroll methodology when selected.
- Apple Design contributes interaction physics; it does not force an Apple visual style.
- Video-specific HyperFrames/runtime rules outrank generic UI animation advice after a video handoff.

## Step 6: Persist Design Intent

For substantial products, screens, flows, or design-system changes, use the project-local `DESIGN.md` contract in [references/design-md-contract.md](references/design-md-contract.md). Use [references/DESIGN.template.md](references/DESIGN.template.md) only as a starting structure, never as mandatory empty ceremony.

An existing `DESIGN.md` must be read before design changes.

Persist stable visual grammar such as:

- design principles;
- color roles/tokens;
- typography;
- spacing;
- radii and surfaces;
- layout/navigation grammar;
- component rules;
- motion language;
- responsive/mobile decisions;
- accessibility constraints;
- signature interaction when one exists.

Do not create DESIGN.md ceremony for a tiny one-off fix. Update an existing DESIGN.md only when the accepted reusable product grammar actually changed.

## Step 7: Originality Without Randomness

For a new substantial visual direction, run the design fingerprint gate in [references/originality.md](references/originality.md) and use [references/originality-policy.json](references/originality-policy.json) for its canonical dimensions and bypass conditions.

Check whether the proposal merely repeats a familiar AI template across:

- navigation model;
- information architecture;
- layout grammar;
- density;
- typography hierarchy;
- surfaces/materials;
- interaction model;
- motion language;
- primary composition;
- signature element.

Revise accidental template repetition.

For experience-led marketing, launch, portfolio, or immersive work, apply [references/signature-interaction.md](references/signature-interaction.md). A signature interaction is optional and must be functional for dashboards, admin tools, CRUD, settings and other utility applications.

For onboarding, major agent flows, launches, immersive stories and other meaningful multi-stage experiences, apply [references/experience-curve.md](references/experience-curve.md). Skip this ceremony for routine CRUD, settings, ordinary dashboard inspection and micro changes.

Do not force novelty when reference fidelity, an established DESIGN.md, accessibility, platform convention, or explicit user intent requires consistency. Fingerprint comparison stays inside the current authorized workspace/product context and must not use another member's private design history.

## Step 8: Verify the Actual Experience

For substantial interfaces, apply the evidence contract in [references/visual-qa.md](references/visual-qa.md) and inspect the states that matter to the feature, including as applicable:

- loading, empty, populated and error;
- disabled, hover, focus and active;
- expanded/collapsed and overlays;
- desktop, tablet and intentionally authored mobile;
- light/dark when supported;
- reduced motion.

For scroll experiences, inspect multiple real scroll positions rather than only the top of the page.

Do not claim visual verification when the runtime did not actually render or inspect the result.

## Conflict Order

Resolve conflicting recommendations in this order:

1. explicit current user instruction;
2. repository/project authority and locked constraints;
3. existing project DESIGN.md;
4. the user's chosen exact-reference boundary;
5. target/runtime correctness;
6. specialist domain authority;
7. general visual taste;
8. optional polish.

## Success Contract

Claim completion only when:

- the selected target was preserved or an authorized migration was made;
- required specialist stages actually ran or were explicitly unnecessary;
- the requested states and responsive targets were verified to the extent the runtime allows;
- unresolved visual, accessibility, runtime, or reference-fidelity risk is reported rather than hidden;
- no vendor, framework, or hosting dependency was introduced merely because its Skill was available.
