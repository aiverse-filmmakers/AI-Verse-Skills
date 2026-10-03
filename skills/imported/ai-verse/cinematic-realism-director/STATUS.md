# Cinematic Realism Director - Implementation Status

Branch: `feat/cinematic-realism-director`

Canonical plan: `IMPLEMENTATION_PLAN.md`

## Current State

- Phase 0: IN PROGRESS
- Task 0.1: COMPLETE
- Task 0.2: COMPLETE
- Next task: 0.3 - Define host capability degradation rules

## Task 0.1 - Freeze package identity and routing scope

Status: COMPLETE

### Frozen identity

```text
name: cinematic-realism-director
display_name: AI-Verse Cinematic Realism Director
location: skills/imported/ai-verse/cinematic-realism-director
ownership: AI-Verse first-party
primary_medium: still images
primary_role: cinematic still-image direction and photorealism intelligence
```

### Evidence

Created `references/routing.md` with:

- stable package identity;
- primary still-image scope;
- positive activation boundaries;
- negative activation boundaries;
- Video Editor ownership boundary;
- Interface Designer ownership boundary;
- video/temporal boundary;
- borderline routing rules;
- routing authority order;
- positive and negative activation fixtures;
- explicit scope-change rule.

### Acceptance check

- [x] name is stable
- [x] scope does not overlap unnecessarily with Video Editor
- [x] scope does not overlap unnecessarily with Interface Designer
- [x] still-image creation/editing is primary
- [x] video is discussed only where it changes a still-frame decision or belongs to future/adjacent workflow ownership

### Verification notes

The Video Editor package describes itself as the authority for real video editing, transcript truth, source-time mapping, EDL construction, scene order, editorial continuity, captions, A/V sync, and final media verification. Cinematic Realism Director does not claim those responsibilities.

The Interface Designer package describes itself as the authority for websites, dashboards, application interfaces, product UI, interaction design, persistent HTML artifacts, and related implementation/QA. Cinematic Realism Director does not claim those responsibilities.

The new skill's routing contract assigns it the frozen-frame visual layer: cinematic still generation, still-image realism repair, reference-frame analysis, shot recipes, expert camera locks, and still-image provider prompting.

## Task 0.2 - Define standalone portability contract

Status: COMPLETE

### Evidence

Created `references/portability.md` with the V1 standalone invariant and package-boundary rules.

The contract defines:

- the package folder as the canonical portable runtime unit;
- package-local relative paths as the only allowed required knowledge references;
- no required repository-root files or scripts;
- no required sibling skills;
- no AI-Verse OS requirement for prompt-only/reasoning operation;
- no MCP requirement for V1 core operation;
- no API-key requirement for prompt-only operation;
- host-independent, provider-neutral core logic;
- local adapter and local schema requirements;
- generic adapter fallback requirement;
- optional external research as provenance rather than runtime dependency;
- data/privacy and filesystem boundaries;
- equivalent standalone distribution forms;
- portability failure conditions;
- an isolated-folder V1 acceptance checklist for the later release gate.

### Acceptance check

- [x] no required parent-directory references
- [x] no required sibling skills
- [x] no required AI-Verse OS
- [x] no required MCP
- [x] no required API key for prompt-only operation

### Verification notes

The contract follows the repository's two-contract skill architecture: portable behavior belongs in `SKILL.md` plus local references, while `aiverse.skill.yaml` is an AI-Verse-specific sidecar that other hosts may ignore.

The contract intentionally does not claim that every host can directly generate or edit images. It freezes only the portability boundary. Exact capability degradation and execution behavior are deferred to Task 0.3 so tool availability does not become a hidden portability assumption.

Final proof of the invariant is reserved for the isolated-folder acceptance test after the full V1 package exists. At that stage, the skill will be copied into a temporary standalone directory and all required local references and workflows will be checked without the surrounding repository.

## Change Discipline

Implement one numbered task from `IMPLEMENTATION_PLAN.md` at a time.

Do not mark a task complete until its acceptance criteria are satisfied and evidence is recorded here.
