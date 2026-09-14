# AI-Verse-Skills

AI-Verse-Skills is the reusable procedure and capability package owner for AI-Verse. It ships exact pinned packages, immutable generations, provider discovery metadata, live readiness reporting, package admission, runtime adapters, execution receipts, and the governed Skill Workshop self-learning lifecycle.

The default canonical install root is:

```text
~/.aiverse/skills/
```

AI-Verse OS, Skills, Memory, Brain, Gateway and Automations remain separate owners. Installing Skills does not grant permissions, credentials, approvals, workspace access, scheduling authority or strategic control.

## 1. Install

### macOS and Linux

```bash
git clone https://github.com/aiverse-filmmakers/AI-Verse-Skills.git
cd AI-Verse-Skills
./aiverse-skills install
```

### Windows PowerShell

```powershell
git clone https://github.com/aiverse-filmmakers/AI-Verse-Skills.git
Set-Location AI-Verse-Skills
.\aiverse-skills.ps1 install
```

Portable fallback:

```bash
python installer/aiverse_skills.py install
```

Install creates a complete verified immutable generation before changing the active pointer. It does not perform setup or grant runtime authority.

## 2. Setup

```bash
./aiverse-skills setup
./aiverse-skills setup --json
```

Setup verifies the currently active immutable generation, provider-v1 metadata, package admission metadata and the supported AI-Verse OS discovery route. The default root is dynamically discoverable. A custom root is reported as requiring explicit host/provider configuration rather than silently editing another repository.

Setup also initializes Skills-owned learning state with the public-beta default mode:

```text
propose
```

## 3. Verify

Fast state:

```bash
./aiverse-skills status
./aiverse-skills status --json
```

Deep verification:

```bash
./aiverse-skills doctor
./aiverse-skills doctor --depth structural
./aiverse-skills doctor --depth runtime
./aiverse-skills doctor --depth system --json
```

Runtime/operator readiness:

```bash
./aiverse-skills readiness
./aiverse-skills readiness --json
```

Machine-readable component descriptor:

```bash
./aiverse-skills descriptor --json
```

Public state vocabulary includes `absent`, `installed`, `setup-required`, `disabled`, `unhealthy`, `migration-required` and `ready`.

### Trust and authority are separate

AI-Verse Skills deliberately keeps these independent:

```text
integrity != admitted != trusted != ready != authorized
```

- **integrity** means bytes match immutable generation metadata.
- **admitted** means deterministic package admission did not block the package.
- **trusted** is the source/package trust class.
- **ready** means required runtime/operator support is usable now.
- **authorized** belongs to the host/user policy and is never granted by Skills.

Imported and external packages are statically scanned before admission. Secret-like material, unsafe symlink escapes and selected high-risk patterns are rejected or surfaced for review. Unknown redistribution rights are treated as fetch-only.

## Interface Designer

Members can use **AI-Verse Interface Designer** as one stack-neutral capability for websites, persistent HTML artifacts, dashboards, app interfaces, reference recreation, interaction design, immersive scroll work and visual QA.

See [docs/INTERFACE_DESIGNER.md](docs/INTERFACE_DESIGNER.md).

## Video Editor

Members can use **AI-Verse Video Editor** as one filmmaking capability for silence and mistake cleanup, Reels/Shorts, long-form talking-head edits, reference-led edits, motion graphics, website promos, captions/B-roll planning, HyperFrames assembly and final media QA.

Members do not need to choose HyperFrames, GSAP, FFmpeg, EDL tooling or the internal editorial specialists themselves.

See [docs/VIDEO_EDITOR.md](docs/VIDEO_EDITOR.md).

## 4. Use

Pin one immutable generation before loading a Skill:

```bash
./aiverse-skills pin --json
./aiverse-skills pin --package verification-harness --json
```

A consumer must use the returned generation for the entire execution. Do not load `SKILL.md` from one generation and helper files from another.

### Runtime support claims

Current public-beta support is intentionally precise:

- **AI-Verse OS:** end-to-end provider discovery, selection, generation-pinned load/invoke path and verified receipt acceptance are the current public-beta execution claim.
- **Agent Skills-compatible directories:** package exposure compatibility only.
- **Claude, Codex, Hermes, OpenClaw and Gemini adapters:** generation-pinned exposure/verification only until a maintained runtime-specific invocation acceptance exists.

Example explicit exposure:

```bash
./aiverse-skills adapt --runtime codex --target ~/.codex/skills
./aiverse-skills adapter-verify --target ~/.codex/skills
```

Adapter exposure never grants permissions or connection access.

### Governed self-learning

Inspect or set learning mode:

```bash
./aiverse-skills learning status
./aiverse-skills learning mode off
./aiverse-skills learning mode propose
./aiverse-skills learning mode auto
```

Explicit learning and refinement:

```bash
./aiverse-skills learn --envelope candidate.json --candidate-dir ./candidate-skill
./aiverse-skills refine --envelope repair.json --candidate-dir ./candidate-skill
```

Proposal workflow:

```bash
./aiverse-skills proposals list
./aiverse-skills proposals inspect <proposal-id>
./aiverse-skills proposals evaluate <proposal-id>
./aiverse-skills proposals apply <proposal-id> --approved-by <principal>
./aiverse-skills proposals reject <proposal-id> --reason "..."
./aiverse-skills proposals quarantine <proposal-id> --reason "..."
./aiverse-skills proposals rollback <proposal-id>
```

Curator:

```bash
./aiverse-skills curator status
./aiverse-skills curator run
./aiverse-skills curator archive <skill-id> --approved-by <principal>
./aiverse-skills curator restore <skill-id>
```

Usage:

```bash
./aiverse-skills usage record <skill-id> --success
./aiverse-skills usage record <skill-id> --failure
```

The Workshop stores proposals separately from active Skills. Production changes always create a new immutable generation. First-party, curated-upstream, user-authored and external Skills are protected from autonomous rewriting. In opt-in `auto` mode, a genuinely new low-risk `agent_learned` Skill may also promote automatically when deterministic security/admission, duplicate, provenance, confidence, permission/dependency/Connection/credential, scope and exact-generation gates all pass. `workspace_local` auto-create remains separately disabled unless owner configuration explicitly enables it. Every auto promotion retains the previous immutable generation as a rollback target.

See [docs/PUBLIC_BETA.md](docs/PUBLIC_BETA.md) and [docs/SELF_IMPROVEMENT.md](docs/SELF_IMPROVEMENT.md).

## 5. Update, disable and uninstall

Update software/package content transactionally:

```bash
./aiverse-skills update
./aiverse-skills update --json
```

Rollback active generation:

```bash
./aiverse-skills rollback
```

Disable without deleting preserved generations:

```bash
./aiverse-skills disable
./aiverse-skills enable
```

Uninstall product integration while preserving immutable state by default:

```bash
./aiverse-skills uninstall
```

Destructive retention cleanup is a separate explicit command:

```bash
./aiverse-skills purge --keep 2 --yes
```

Purge never runs automatically and preserves active/history generations plus generations referenced by learning rollback/archive provenance.

## 6. What setup does and does not grant

Setup does:

- verify the active immutable generation;
- verify provider and package admission metadata;
- report OS discoverability;
- initialize Skills-owned Workshop state;
- record that component setup completed.

Setup does not:

- transfer canonical authority;
- grant filesystem/workspace permissions;
- grant external account or secret access;
- authorize a Skill invocation;
- activate Brain goals;
- schedule background work;
- write into sibling repositories.

## Distribution and licensing

The repository-owned code is licensed under MIT. Third-party packages remain governed by their upstream terms.

`registry/trust-policy.json` is the public-beta redistribution/admission decision record. Packages with explicit redistribution permission may be vendored as recorded. Sources without a final redistribution grant are fetch-only from their exact pinned upstream revision.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Validation

Core validation:

```bash
python scripts/validate_registry.py
python -m unittest discover -s tests -v
```

The full networked E2E workflow verifies pinned upstream installation, provider metadata, package digests, immutable update, stale-adapter rejection, rollback, uninstall preservation and recovery. Public-beta lifecycle and learning acceptance runs on Linux, macOS and Windows across supported Python versions.
