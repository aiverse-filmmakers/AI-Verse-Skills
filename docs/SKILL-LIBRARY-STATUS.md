# Skill library status

The single record of the 2026 library cleanup. Last updated 13 November 2026 (Group B marketing tidy and Group C small fixes added).
Starting point: 118 catalogue skills (main at `bab2834`).

| Status | Count |
|---|---|
| Removed outright | 60 |
| Old filmmaking entries combined into one | 2 |
| Kept and improved (owned by AI-Verse) | 45 |
| Kept as they are | 2 |
| Still to review | 9 |
| Added 13 November (new, owned by AI-Verse) | 2 |
| Added to the catalogue 14 November (already owned by AI-Verse) | 1 |
| **Catalogue after this change** | **59** (49 kept + 9 to review + `cinematic-realism-director`) |

`notion` and `shadcn` were removed earlier (pull request #28) and are not counted here.

## Kept and improved (45)

None of these has been tested with and without the skill yet. Scores are estimates.

Approved 13 November: `director-agent` is an English adapted copy. `ai-storyboard-director` and `produce-ai-video` are merged into `ai-video-director`, with a shared storyboard process and no fixed minimum shot count. Old explicit identifiers are no longer in the catalogue; runtime alias compatibility is not established. These filmmaking skills have not been tested in a live filmmaking workflow. `after-effects-assistant` is kept, with its version detection corrected.

Approved 13 November: `whisper` and `ExtractWisdom` are kept as adapted copies. Both retain their existing identifiers for compatibility. Whisper now provides a practical transcription workflow; ExtractWisdom uses available source tools and preserves attribution and uncertainty. Neither has been tested in a live member workflow.

**Developer, rebuilt (9):** `root-cause-debugger` (now also covers environment, configuration and incident timelines), `deep-research-synthesis`, `structured-ingestion-normalization`, `api-integration-engineer`, `dependency-supply-chain-audit`, `change-review`, `verification-harness`, `transactional-refactor` (now also covers codebase mapping), `git-change-lifecycle` (now also covers the release checklist)

**Outside skills, now owned copies with `LICENSE` and `SOURCE.json` (17):**
- Anthropic, Apache 2.0: `review-contract` (now includes legal risk scoring), `account-research` (now includes call briefs), `cash-flow-snapshot`, `job-post-builder`, `business-pulse`, `draft-response`, `draft-outreach`, `write-spec`, `product-brainstorming`, `roadmap-update`
- Vercel, MIT: `composition-patterns`
- Emil Kowalski, MIT: `pick-ui-library`, and from 13 November `review-animations`, `improve-animations`, `find-animation-opportunities`, `apple-design` (kept by decision; structure fixes only, the author's rules, values and tone are untouched)
- Corey Haines, MIT: `social-content` (13 November; inner name fixed, repurposing references added), and from the 13 November marketing tidy `copywriting`, `ad-creative`, `content-strategy`, `customer-research`, `email-sequence` (inner name was `emails`), `seo-audit`, `community-marketing` (pointers to skills and tools not in the library removed; the marketing advice is unchanged; the lines that read the shared brand file now read the current project's marketing notes)
- Hermes, MIT (13 November, Group C): `email-inbox-triage`, `weekly-review-planning`, `one-three-one-rule` (everyday example instead of a coding one), and `action-items`, which merges `meeting-action-items` and `document-to-action-items` into one skill (the two old names are gone, so the catalogue is 59). Each got a plain "use when" description and Hermes only tool names replaced with plain wording
- Meng To, MIT: `video-to-superprompt` (description now says it rebuilds a site or app from a screen recording)
- Adobe skills author, Apache 2.0: `after-effects-assistant` (inner name fixed; the fixed folder path replaced with the folder the skill is loaded from)
- Novoads, MIT: `meta-ad-builder` (the Novoads requirement removed; it needs only Meta credentials)
- kajisho5, MIT: `ffmpeg-skill` (only the skill itself kept: 49 files instead of 124)

## Added 13 November (2)

`ai-realism` (Seedance 2.5 prompt writing) and `higgsfield-acting` (performance direction for AI video). Both are written for AI-Verse and registered for the full, creator and filmmaker profiles and the ai-filmmaker role. They work in a fixed chain with `director-agent`, `ai-video-director` and `cinematic-realism-director`: the creative brief outranks locked references, which outrank acting, which outranks prompt structure, which outranks platform limits. Triggering in a fresh Claude or Codex chat has not been verified.

Added to the catalogue 14 November: `cinematic-realism-director` (still images). It was already an AI-Verse owned skill in this repository, but it sat outside the catalogue, so it never reached members even though `ai-realism` and the chain send still image work to it. It is now skill 59, in the full, creator and filmmaker profiles and the ai-filmmaker role. Its description now says when to use it.

Retired names now redirect: `ai-storyboard-director` and `produce-ai-video` to `ai-video-director`, `meeting-action-items` and `document-to-action-items` to `action-items`.

## Kept as they are (2)

`react-best-practices` (Vercel) and `animate-expo` (Emil Kowalski).

## Removed (60)

- **Accounting (7):** `journal-entry-prep`, `reconciliation`, `close-management`, `3-statement-model`, `excel-author`, `financial-statements`, `variance-analysis`
- **Sales and support systems (6):** `customer-retention`, `deal-management`, `sales-execution`, `pipeline-review`, `ticket-triage`, `vendor-check`
- **Office personas (4):** `persona-event-coordinator`, `persona-exec-assistant`, `persona-hr-coordinator`, `persona-project-manager`
- **Wrong fit (7):** `brand-guidelines`, `internal-comms`, `Fabric`, `figma-use`, `figma-generate-design`, `airtable`, `shopify`
- **Developer stubs (6):** `skill-forge` (replaced by `/skill`), `skill-miner` (moving into `/learn`), `knowledge-writeback`, `delegation-orchestrator`, `database-migration-guardian`, plus `browser-workflow-operator`
- **Folded into kept skills (7):** `environment-doctor`, `configuration-contract-doctor`, `incident-forensics` (into `root-cause-debugger`), `semantic-codebase-sweep` (into `transactional-refactor`), `release-deploy-guard` (into `git-change-lifecycle`), `legal-risk-assessment` (into `review-contract`), `call-prep` (into `account-research`)
- **Second review (12):** `premiere-agent` (overlaps `video-editor`), `kanban-video-orchestrator` (Hermes only), `analytics`, `scheduling-and-queue` (WoopSocial only), `docx`, `xlsx`, `ppt-generation` (Claude and Codex have their own), `Council`, `Ideate` (broken outside the author's setup), `design-and-templates`, `baoyu-article-illustrator`, `theme-factory`
- **Replaced 13 November (1):** `product-marketing-context`. Each project now keeps its own marketing notes (the `marketing` adjustments); the setup interview moved into `copywriting/references/marketing-project-setup.md`, and the eight marketing skills read the current project's notes instead of one shared file. The old name redirects to `copywriting`.
- **Decided 13 November (1):** `google-workspace` (Claude and ChatGPT have their own Google connections; the five `gws-*` helper packages went with it. The connection readiness entry stays for now).
- **Third review, 13 November (9):** `structure-screenplay`, `plan-camera-shots` (built for an outside software pipeline; `director-agent` and `ai-storyboard-director` cover the same jobs), `cross-platform-repurposing` (mostly pointers to skills not in the library; `social-content` covers repurposing, and its reference files are to be reused there), `launch-strategy` (software product launches), `canva` (mostly pointers to WoopSocial and missing skills; Canva's own connection does the work), `RedTeam` (32 agents per run, outside voice server and folders; a small replacement is to be built), `ui-ux-pro-max` (commands fail outside a Claude plugin, 3.6 MB), `design-first-ui-prompting` (a thin image prompt template), `stitched-full-page-capture` (tied to its author's own article workflow)

`interface-designer` no longer routes to the removed Figma skills: its Figma target now reports "unavailable" unless the runtime has its own Figma skills. The same now applies to Canva. The interface designer does the UI and UX reasoning and the design specification itself, since `ui-ux-pro-max` and `design-first-ui-prompting` are gone.

## Still to review (9)

Decided 13 November: keep all of them. Group A (nine skills) is left as it is, Group B (marketing, seven skills) is done above, Group C (small fixes, nine skills) is done above, Group D is complete in the current branch; project adjustments and the replacement red team remain separate work. See entry D33 of the skills plan.

Scores from a first read on 12 November (usefulness to members / craft, out of 10), with the recommended action. A second read of every skill in full gave different scores and recommendations for several of these; that review is entry D31 of the skills plan in the AI-Verse OS development workspace. Decided on 13 November: `product-marketing-context` will be replaced by per project adjustments once those exist. The four animation and Apple skills that review recommended removing were kept by decision on 13 November.

### Film and video (1)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `video-editor` | 9 | 8 | Keep |

### Web and interface design (6), recommended as one optional pack
| Skill | Use | Craft |
|---|---|---|
| `interface-designer` | 7 | 7 |
| `frontend-design` | 6 | 8 |
| `scroll-craft` | 5 | 8 |
| `web-design-guidelines` | 5 | 7 |
| `animate` | 4 | 9 |
| `prototype` | 4 | 9 |

### Thinking (1)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `decision-questionnaire` | 5 | 7 | Keep |

### Visual design (1)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `canvas-design` | 6 | 7 | Keep |

## Open items

1. No skill in this change has been tested with and without the skill in fresh chats. The English filmmaking translations have not had an independent full accuracy audit.
2. Six AI-Verse specific rules taken out of `change-review` should become AI-Verse OS project adjustments for that skill.
3. Done 14 November: `install` and `update` with `--expose-default` list every skill in `~/.claude/skills` and `~/.agents/skills`, and the AI-Verse OS setup guidance points to it. Tested in fresh Claude Code and Codex chats on 14 November: all 59 skills were visible in both, with no cut off.
4. A usage counter (count and last used date per skill) does not exist yet.

## Every skill is stored in this repository (13 November)

Eight catalogue skills used to be fetched from outside at install, so a member's install held fewer skills than the catalogue listed. They are now owned copies stored here, each with its licence and a `SOURCE.json` record: `decision-questionnaire`, `canvas-design`, `frontend-design`, `react-best-practices`, `animate`, `prototype`, `animate-expo` and `scroll-craft`. A new test fails if any catalogue skill is not stored in the repo, or has no description that tells a chat when to use it.

Changes made to them: `decision-questionnaire` has a new description (the original had no trigger). `react-best-practices` has its inner name matched to the folder and its duplicate compiled file removed. The rest are unchanged copies. `canvas-design` ships 5.5 MB of fonts with their own licence files. `scroll-craft` includes eight helper scripts that call an outside image service (kie.ai) with the member's own key.
