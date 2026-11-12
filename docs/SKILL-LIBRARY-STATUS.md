# Skill library status

The single record of the 2026 library cleanup. Last updated 12 November 2026.
Starting point: 118 catalogue skills (main at `bab2834`).

| Status | Count |
|---|---|
| Removed in this change | 49 |
| Kept and improved (owned by AI-Verse) | 21 |
| Kept as they are | 3 |
| Still to review | 45 |
| **Catalogue after this change** | **69** (24 kept + 45 to review) |

`notion` and `shadcn` were removed earlier (pull request #28) and are not counted here.

## Kept and improved (21)

None of these has been tested with and without the skill yet. Scores are estimates.

**Developer, rebuilt (9):** `root-cause-debugger` (now also covers environment, configuration and incident timelines), `deep-research-synthesis`, `structured-ingestion-normalization`, `api-integration-engineer`, `dependency-supply-chain-audit`, `change-review`, `verification-harness`, `transactional-refactor` (now also covers codebase mapping), `git-change-lifecycle` (now also covers the release checklist)

**Outside skills, now owned copies with `LICENSE` and `SOURCE.json` (12):**
- Anthropic, Apache 2.0: `review-contract` (now includes legal risk scoring), `account-research` (now includes call briefs), `cash-flow-snapshot`, `job-post-builder`, `business-pulse`, `draft-response`, `draft-outreach`, `write-spec`, `product-brainstorming`, `roadmap-update`
- Vercel, MIT: `composition-patterns`
- Emil Kowalski, MIT: `pick-ui-library`

## Kept as they are (3)

`react-best-practices` (Vercel), `animate-expo` (Emil Kowalski), `google-workspace` (Hermes; still to decide between porting it properly or relying on Claude's and ChatGPT's own Google connections).

## Removed (49)

- **Accounting (7):** `journal-entry-prep`, `reconciliation`, `close-management`, `3-statement-model`, `excel-author`, `financial-statements`, `variance-analysis`
- **Sales and support systems (6):** `customer-retention`, `deal-management`, `sales-execution`, `pipeline-review`, `ticket-triage`, `vendor-check`
- **Office personas (4):** `persona-event-coordinator`, `persona-exec-assistant`, `persona-hr-coordinator`, `persona-project-manager`
- **Wrong fit (7):** `brand-guidelines`, `internal-comms`, `Fabric`, `figma-use`, `figma-generate-design`, `airtable`, `shopify`
- **Developer stubs (6):** `skill-forge` (replaced by `/skill`), `skill-miner` (moving into `/learn`), `knowledge-writeback`, `delegation-orchestrator`, `database-migration-guardian`, plus `browser-workflow-operator`
- **Folded into kept skills (7):** `environment-doctor`, `configuration-contract-doctor`, `incident-forensics` (into `root-cause-debugger`), `semantic-codebase-sweep` (into `transactional-refactor`), `release-deploy-guard` (into `git-change-lifecycle`), `legal-risk-assessment` (into `review-contract`), `call-prep` (into `account-research`)
- **Second review (12):** `premiere-agent` (overlaps `video-editor`), `kanban-video-orchestrator` (Hermes only), `analytics`, `scheduling-and-queue` (WoopSocial only), `docx`, `xlsx`, `ppt-generation` (Claude and Codex have their own), `Council`, `Ideate` (broken outside the author's setup), `design-and-templates`, `baoyu-article-illustrator`, `theme-factory`

`interface-designer` no longer routes to the removed Figma skills: its Figma target now reports "unavailable" unless the runtime has its own Figma skills.

## Still to review (45)

Scores from a first read on 12 November (usefulness to members / craft, out of 10), with the recommended action.

### Film and video (9)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `video-editor` | 9 | 8 | Keep |
| `director-agent` | 9 | 7 | Keep. Clean up the mixed Chinese terms |
| `video-to-superprompt` | 8 | 7 | Keep |
| `ffmpeg-skill` | 8 | 8 | Keep. Strip the author's 12 stray `.claude/skills` files |
| `produce-ai-video` | 8 | 6 | Keep. Make it work outside Codex |
| `ai-storyboard-director` | 8 | 6 | Translate to English (it never triggers on English requests) |
| `after-effects-assistant` | 6 | 7 | Keep. Fix the inner name (`after-effects`) |
| `structure-screenplay` | 5 | 6 | Fold into `produce-ai-video` |
| `plan-camera-shots` | 5 | 6 | Fold into `produce-ai-video` |

### Marketing (12)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `community-marketing` | 8 | 8 | Keep |
| `copywriting` | 8 | 8 | Keep |
| `social-content` | 8 | 8 | Keep. Fix the inner name (`social`) |
| `cross-platform-repurposing` | 8 | 7 | Keep. Remove WoopSocial references |
| `product-marketing-context` | 7 | 8 | Keep. Fix the inner name (`product-marketing`) |
| `ad-creative` | 7 | 8 | Keep |
| `content-strategy` | 7 | 8 | Keep |
| `meta-ad-builder` | 6 | 7 | Keep (needs Meta API keys) |
| `customer-research` | 6 | 8 | Keep |
| `email-sequence` | 6 | 8 | Keep. Fix the inner name (`emails`) |
| `launch-strategy` | 5 | 8 | Keep. Fix the inner name (`launch`) |
| `seo-audit` | 4 | 8 | Optional |

### Web and interface design (13), recommended as one optional pack
| Skill | Use | Craft |
|---|---|---|
| `interface-designer` | 7 | 7 |
| `frontend-design` | 6 | 8 |
| `scroll-craft` | 5 | 8 |
| `ui-ux-pro-max` | 5 | 7 |
| `web-design-guidelines` | 5 | 7 |
| `design-first-ui-prompting` | 5 | 6 |
| `animate` | 4 | 9 |
| `prototype` | 4 | 9 |
| `apple-design` | 3 | 8 |
| `review-animations` | 3 | 9 |
| `stitched-full-page-capture` | 3 | 7 |
| `improve-animations` | 2 | 8 |
| `find-animation-opportunities` | 2 | 8 |

### Office (5)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `whisper` | 7 | 5 | Keep. Trim the GitHub star padding |
| `meeting-action-items` | 6 | 6 | Merge with `document-to-action-items`. Remove Hermes only tool names |
| `document-to-action-items` | 6 | 6 | As above |
| `email-inbox-triage` | 6 | 6 | Keep. Remove Hermes only tool names |
| `weekly-review-planning` | 6 | 6 | Keep. Remove Hermes only tool names |

### Thinking (4)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `ExtractWisdom` | 7 | 4 | Rewrite: remove the author's private voice server and folders, lowercase the name |
| `RedTeam` | 6 | 4 | Same |
| `one-three-one-rule` | 5 | 7 | Keep |
| `decision-questionnaire` | 5 | 7 | Keep |

### Visual design (2)
| Skill | Use | Craft | Recommendation |
|---|---|---|---|
| `canvas-design` | 6 | 7 | Keep |
| `canva` | 6 | 6 | Keep. Remove WoopSocial references |

## Open items

1. No skill in this change has been tested with and without the skill in fresh chats.
2. Six AI-Verse specific rules taken out of `change-review` should become AI-Verse OS project adjustments for that skill.
3. Library skills are not yet copied into `.claude/skills` and `.agents/skills`, so Claude and Codex cannot trigger them by themselves. This is the main reason the library has barely been used.
4. A usage counter (count and last used date per skill) does not exist yet.
