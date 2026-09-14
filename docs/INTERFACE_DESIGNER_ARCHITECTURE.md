# Interface Designer Maintainer Architecture

## Purpose

AI-Verse Interface Designer is a first-party composite Skill that routes interface work to the smallest relevant set of specialist Skills.

It is not a second Skills runtime.

It uses the existing AI-Verse Skills registry, exact source pins, immutable generations, admission/trust model, runtime adapters and authorization boundary.

Canonical package:

`skills/imported/ai-verse/interface-designer/`

Canonical machine graph:

`skills/imported/ai-verse/interface-designer/references/orchestration.json`

## Ownership

Interface Designer owns:

- scope classification guidance;
- delivery-target classification guidance;
- conditional stage ordering;
- design-specific conflict priority;
- project `DESIGN.md` persistence rules;
- originality/fingerprint policy;
- signature-interaction policy;
- experience-curve policy;
- visual QA policy;
- scroll QA policy;
- mobile art-direction policy;
- selection of design specialists.

Interface Designer does not own:

- filesystem or workspace authority;
- credentials or Connections;
- external tool approval;
- package admission;
- source trust;
- immutable generation mechanics;
- runtime authorization;
- deployment hosting;
- general Memory;
- scheduling;
- canonical telemetry/cost accounting.

Those remain with their existing AI-Verse owners.

## End-to-end routing model

```text
user request + project context + references
                |
                v
        local authority read
                |
                v
          scope classifier
                |
                v
         target classifier
                |
                v
      conditional stage graph
                |
                +--> reference specialists, only if needed
                +--> visual/UI specialists, only if needed
                +--> target implementation specialists
                +--> interaction/motion specialists, only if needed
                |
                v
       rendered verification gates
                |
                +--> state-based QA
                +--> scroll QA, only when scroll drives state
                +--> mobile art direction, when mobile applies
                +--> motion review, when significant motion exists
                +--> web/accessibility review, for substantial web UI
                |
                v
          fix + reverify
```

The graph is conditional. Scope pipelines are maximum legal stage sets, not instructions to execute every stage.

Each stage's `when` condition still has to be true.

## Scope classifier

Supported primary scopes:

| Scope | Intended use |
|---|---|
| `MICRO_CHANGE` | Tiny local edit such as spacing, copy or one narrow style adjustment |
| `COMPONENT` | One bounded component |
| `SCREEN` | One substantial screen/page |
| `MULTI_SCREEN_FLOW` | Several connected screens or a meaningful staged flow |
| `FULL_PRODUCT` | New product/interface direction |
| `REFERENCE_RECREATION` | Screenshot/video/reference-led work |
| `INTERACTION_HEAVY` | Direct manipulation, gestures, drag/snap, spatial interaction |
| `DESIGN_SYSTEM_CHANGE` | Product-wide visual grammar change |
| `SCROLL_IMMERSIVE` | Scroll is the primary storytelling/state mechanism |
| `MOBILE_EXPO` | React Native/Expo mobile interaction work |

The smallest sufficient scope wins.

A micro task must never be promoted to a full-product workflow merely because more specialists are available.

## Delivery targets

Supported targets:

| Target | Meaning |
|---|---|
| `PLAIN_HTML_CSS_JS_ARTIFACT` | Persistent/static artifact with no framework requirement |
| `EXISTING_WEB_STACK` | Preserve whatever web stack is already present |
| `REACT_WEB_APP` | React/Next-style implementation target |
| `PWA` | Progressive web app |
| `FIGMA` | Figma implementation/tooling target |
| `CANVA_OR_STATIC_DESIGN_TOOL` | Canva/static design surface |
| `DESKTOP_WEBVIEW_APP` | Desktop app backed by a web UI surface |
| `NATIVE_DESKTOP_APP` | Native desktop UI target |
| `REACT_NATIVE_EXPO` | React Native/Expo |
| `PROTOTYPE_ONLY` | Divergence/prototype output only |
| `DESIGN_ONLY_HANDOFF` | Design/spec output without implementation |
| `CODE_DRIVEN_VIDEO_MOTION_HANDOFF` | Interface/design work intended for the separate AI-Verse Video Editor pipeline |

Target detection preserves the existing project.

A specialist's existence never authorizes a stack migration.

## Canonical stage order

The maximum stage set is:

1. `local_authority`
2. `target_detection`
3. `reference_analysis`
4. `design_specification`
5. `ui_ux_intelligence`
6. `experience_curve`
7. `visual_direction`
8. `prototype_divergence`
9. `originality_gate`
10. `signature_interaction`
11. `design_system_persistence`
12. `library_selection`
13. `target_implementation`
14. `interaction_physics`
15. `motion_build`
16. `render_preview`
17. `visual_state_qa`
18. `scroll_state_qa`
19. `mobile_art_direction_qa`
20. `motion_review`
21. `web_review`
22. `fix_and_reverify`

Do not reorder a stage when the order is part of its correctness.

Examples:

- design direction precedes persistent `DESIGN.md` updates;
- implementation precedes rendered QA;
- failures are fixed before affected verification is considered complete.

## Specialist provider map

Exact pins are canonical in `registry/packages.json`.

Preservation expectations are canonical in:

`skills/imported/ai-verse/interface-designer/references/expert-preservation.json`

### Visual/UI direction

| Capability | Source role |
|---|---|
| `frontend-design` | Distinctive frontend visual/art direction |
| `ui-ux-pro-max` | Broad UI/UX intelligence, patterns, palette/type/product reasoning |

### Reference analysis

| Capability | Source role |
|---|---|
| `design-first-ui-prompting` | Turns fuzzy UI intent into design-first specification |
| `video-to-superprompt` | Extracts interface/motion system from reference video |
| `stitched-full-page-capture` | Reliable capture for lazy/animated/WebGL/reference pages |

### Interaction and motion

| Capability | Source role |
|---|---|
| `apple-design` | Physical direct-manipulation and interaction principles |
| `animate` | Builds motion from purpose through implementation |
| `prototype` | Genuine design divergence |
| `review-animations` | High-craft motion review |
| `pick-ui-library` | Curated UI dependency selection |
| `improve-animations` | Codebase-level motion improvement audit |
| `find-animation-opportunities` | Identifies worthwhile missing motion |
| `animate-expo` | Expo/Reanimated/Gesture Handler motion implementation |

### Frontend engineering

| Capability | Source role |
|---|---|
| `react-best-practices` | React/Next performance and engineering guidance |
| `composition-patterns` | Reusable React component architecture |
| `shadcn` | shadcn project/component correctness |
| `web-design-guidelines` | Final web interface quality/accessibility review |

### Immersive scroll

| Capability | Source role |
|---|---|
| `scroll-craft` | Dedicated scroll-driven experience methodology and tooling |

### Existing target specialists retained

| Target | Existing AI-Verse capabilities |
|---|---|
| Figma | `figma-use`, `figma-generate-design` |
| Canva/static design | `canva` |

These capabilities were not replaced by Interface Designer.

## Current source pins

| Source ID | Repository | Commit |
|---|---|---|
| `anthropic-frontend` | `anthropics/skills` | `34040c9c568585f6929bedeaad110ad08f079624` |
| `nextlevelbuilder-ui` | `nextlevelbuilder/ui-ux-pro-max-skill` | `7f69fed6a2717900085f1bc3b263721f8ba025e2` |
| `vercel-design` | `vercel-labs/agent-skills` | `063bee94c3f4df8453406c830b0a7df0f2860278` |
| `shadcn-ui` | `shadcn-ui/ui` | `2b3e6d4f8d9161fe5c19340dc383aade392012dd` |
| `mengto-ui` | `MengTo/Skills` | `321c769739b823de5eb94eb3a52aa1974fe783a2` |
| `emil-design` | `emilkowalski/skills` | `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7` |
| `scroll-craft` | `nateherkai/scroll-craft` | `0b816225945e45380397d6a0487efa3c98916858` |

Do not replace a commit pin with `main`, `master`, `HEAD`, `latest` or a tag that can move.

## Conditional provider rules

### React specialists

Use `react-best-practices` and `composition-patterns` only when the real target is React/Next.

### shadcn

Use `shadcn` only when:

- the project already uses it; or
- it is intentionally selected.

### Scroll Craft

Use `scroll-craft` only when scroll is the primary storytelling or interaction mechanism.

It does not become the implementation engine for normal app screens.

### Apple Design

Use `apple-design` for direct manipulation, gesture physics, drag/swipe/sheet interactions or spatial continuity.

It provides interaction reasoning, not a mandatory Apple visual skin.

### Prototype

Use `prototype` only for actual divergence/choice work.

Do not invoke it for a tiny fix.

### Motion audits

Use `improve-animations` or `find-animation-opportunities` only for explicit audit/polish requests.

They are not default implementation stages.

## Design persistence

Project-local `DESIGN.md` is persistent product visual grammar.

Canonical contract:

`skills/imported/ai-verse/interface-designer/references/design-md-contract.md`

Rules:

- read an existing file before substantial design work;
- create one only when reusable product design decisions are being established;
- update only the sections whose accepted product grammar changed;
- never rewrite it for a one-off micro fix;
- keep mobile, accessibility and interaction rules intentional.

## Originality

Canonical policy:

`references/originality-policy.json`

The originality gate detects accidental structural re-skins.

It does not override:

- exact reference fidelity;
- an established product `DESIGN.md`;
- platform conventions;
- accessibility;
- explicit user intent.

Fingerprint comparison is workspace/user scoped and cannot use another member's private design history.

## Visual QA

Three explicit QA surfaces exist:

1. `visual-qa-policy.json`
2. `scroll-qa-policy.json`
3. `mobile-art-direction-policy.json`

A verified visual pass requires rendered evidence.

Source inspection alone is not visual evidence.

Blocked rendering must remain `UNVERIFIED_BLOCKED`.

## Conflict priority

When design recommendations conflict, use this order:

1. explicit current user instruction;
2. repository/project authority;
3. accepted project `DESIGN.md`;
4. chosen exact-reference boundary;
5. target/runtime correctness;
6. specialist domain authority;
7. general visual taste;
8. optional polish.

Specialists are not peers when one owns the relevant domain.

Example: React implementation correctness beats generic frontend advice inside a React-specific engineering decision, while the visual-direction specialist still owns visual art direction.

## Security boundary

Interface Designer uses the existing Skills security model.

```text
integrity != admitted != trusted != ready != authorized
```

It may select a Skill.

It cannot grant that Skill authority.

A Skill's upstream `allowed-tools` or similar declaration is not a runtime grant.

Canonical security evidence:

- `installer/admission.py`
- `installer/generation_lifecycle.py`
- `registry/trust-policy.json`
- `references/security-boundaries.json`

## Existing-design replacement result

Canonical compatibility record:

`references/existing-design-compatibility.json`

Current result: **zero destructive removals**.

Existing design capabilities remain available because their jobs are distinct or target-specific.

If a future provider truly supersedes an existing public capability, the removal process must:

1. document the exact overlap;
2. identify useful unique behavior;
3. migrate that behavior if needed;
4. add regression coverage;
5. provide compatibility handling for public IDs if necessary;
6. only then remove the old entry.

## How to add or replace a provider

Do not edit only the orchestrator prose.

### 1. Prove the need

State:

- capability gap;
- why an existing provider is insufficient;
- intended stage;
- intended trigger;
- target/scopes where it is legal.

### 2. Verify source and licensing

Record:

- upstream repository;
- exact 40-character commit SHA;
- package path;
- license decision;
- redistribution decision;
- trust classification.

Update:

- `registry/packages.json`
- `registry/trust-policy.json`
- `THIRD_PARTY_NOTICES.md`

### 3. Preserve methodology

Update `expert-preservation.json` with the provider's key identity signals.

Do not paraphrase its full method into Interface Designer.

### 4. Route conditionally

Update `orchestration.json`.

Prefer an existing stage unless the new provider represents a genuinely new stage of interface work.

### 5. Add routing/regression fixtures

Update:

- `routing-fixtures.json`;
- Interface Designer contract tests;
- context/bloat tests;
- provenance/trust tests.

### 6. Run admission and full CI

A provider update is not accepted until registry validation, runtime readiness and clean-install immutable-generation E2E pass.

### 7. Update System evidence

Record the accepted ref and behavior change in the canonical System implementation plan and any affected component spec/QC docs.

## Video Editor handoff

`CODE_DRIVEN_VIDEO_MOTION_HANDOFF` exists as a cross-composite design target for the separately planned AI-Verse Video Editor.

The `video-editor` capability is not part of the accepted Interface Designer inventory yet.

Until Video Editor is implemented and registered:

- Interface Designer may prepare design/motion assets or a design handoff;
- it must not claim that the Video Editor stage executed;
- unresolved `video-editor` routing must be reported as unavailable/blocked rather than silently replaced by a different editing system.

When Video Editor lands, this target must receive a dedicated integration regression.

## Canonical supporting files

| Purpose | File |
|---|---|
| Stage graph | `references/orchestration.json` |
| Routing explanation | `references/routing.md` |
| Routing regression fixtures | `references/routing-fixtures.json` |
| `DESIGN.md` contract | `references/design-md-contract.md` |
| Originality | `references/originality.md`, `originality-policy.json` |
| Signature interaction | `references/signature-interaction.md`, `signature-interaction-policy.json` |
| Experience curve | `references/experience-curve.md`, `experience-curve-policy.json` |
| Visual QA | `references/visual-qa.md`, `visual-qa-policy.json` |
| Scroll QA | `references/scroll-qa.md`, `scroll-qa-policy.json` |
| Mobile QA | `references/mobile-art-direction.md`, `mobile-art-direction-policy.json` |
| Provider preservation | `references/expert-preservation.json` |
| Existing capability compatibility | `references/existing-design-compatibility.json` |
| Security boundary | `references/security-boundaries.json` |
