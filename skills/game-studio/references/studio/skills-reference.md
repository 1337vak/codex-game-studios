> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Available Skills (Slash Commands)

74 slash commands organized by phase. Type `/` in Codex to access any of them.

## Onboarding & Navigation

| Command | Purpose |
|---------|---------|
| `$game-studio start` | First-time onboarding — asks where you are, then guides you to the right workflow |
| `$game-studio help` | Context-aware "what do I do next?" — reads current stage and surfaces the required next step |
| `$game-studio project-stage-detect` | Full project audit — detect phase, identify existence gaps, recommend next steps |
| `$game-studio setup-engine` | Configure engine + version, detect knowledge gaps, populate version-aware reference docs |
| `$game-studio adopt` | Brownfield format audit — checks internal structure of existing GDDs/ADRs/stories, produces migration plan |
| `$game-studio settings` | View or change project config — the effective merged values, or a local override in `project.local.yaml` |

## Game Design

| Command | Purpose |
|---------|---------|
| `$game-studio brainstorm` | Guided ideation using professional studio methods (MDA, SDT, Bartle, verb-first) |
| `$game-studio map-systems` | Decompose game concept into systems, map dependencies, prioritize design order |
| `$game-studio design-system` | Guided, section-by-section GDD authoring for a single game system |
| `$game-studio quick-design` | Lightweight design spec for small changes — tuning, tweaks, minor additions |
| `$game-studio review-all-gdds` | Cross-GDD consistency and game design holism review across all design docs |
| `$game-studio propagate-design-change` | When a GDD is revised, find affected ADRs and produce an impact report |

## Art & Assets

| Command | Purpose |
|---------|---------|
| `$game-studio art-bible` | Guided, section-by-section Art Bible authoring — creates visual identity spec before asset production begins |
| `$game-studio asset-spec` | Generate per-asset visual specifications and AI generation prompts from GDDs, level docs, or character profiles |
| `$game-studio asset-audit` | Audit assets for naming conventions, file size budgets, and pipeline compliance |

## UX & Interface Design

| Command | Purpose |
|---------|---------|
| `$game-studio ux-design` | Guided section-by-section UX spec authoring (screen/flow, HUD, or pattern library) |
| `$game-studio ux-review` | Validate UX specs for GDD alignment, accessibility, and pattern compliance |

## Architecture

| Command | Purpose |
|---------|---------|
| `$game-studio create-architecture` | Guided authoring of the master architecture document |
| `$game-studio architecture-decision` | Create an Architecture Decision Record (ADR) |
| `$game-studio architecture-review` | Validate all ADRs for completeness, dependency ordering, and GDD coverage |
| `$game-studio create-control-manifest` | Generate flat programmer rules sheet from accepted ADRs |

## Stories & Sprints

| Command | Purpose |
|---------|---------|
| `$game-studio create-epics` | Translate GDDs + ADRs into epics — one per architectural module |
| `$game-studio create-stories` | Break a single epic into implementable story files |
| `$game-studio dev-story` | Read a story and implement it — routes to the correct programmer agent |
| `$game-studio sprint-plan` | Generate or update a sprint plan; initializes sprint-status.yaml |
| `$game-studio sprint-status` | Fast 30-line sprint snapshot (reads sprint-status.yaml) |
| `$game-studio story-readiness` | Validate a story is implementation-ready before pickup (READY/NEEDS WORK/BLOCKED) |
| `$game-studio story-done` | 8-phase completion review after implementation; updates story file, surfaces next story |
| `$game-studio estimate` | Structured effort estimate with complexity, dependencies, and risk breakdown |

## Reviews & Analysis

| Command | Purpose |
|---------|---------|
| `$game-studio design-review` | Review a game design document for completeness and consistency |
| `$game-studio code-review` | Architectural code review for a file or changeset |
| `$game-studio balance-check` | Analyze game balance data, formulas, and config — flag outliers |
| `$game-studio content-audit` | Audit GDD-specified content counts against implemented content |
| `$game-studio scope-check` | Analyze feature or sprint scope against original plan, flag scope creep |
| `$game-studio perf-profile` | Structured performance profiling with bottleneck identification |
| `$game-studio tech-debt` | Scan, track, prioritize, and report on technical debt |
| `$game-studio gate-check` | Validate readiness to advance between development phases (PASS/CONCERNS/NOT ASSESSED/FAIL) |
| `$game-studio consistency-check` | Scan all GDDs against the entity registry to detect cross-document inconsistencies (stats, names, rules that contradict each other) |
| `$game-studio security-audit` | Audit the game for security vulnerabilities: save tampering, cheat vectors, network exploits, data exposure, and input validation gaps |

## QA & Testing

| Command | Purpose |
|---------|---------|
| `$game-studio qa-plan` | Generate a QA test plan for a sprint or feature |
| `$game-studio smoke-check` | Run critical path smoke test gate before QA hand-off |
| `$game-studio soak-test` | Generate a soak test protocol for extended play sessions |
| `$game-studio regression-suite` | Map test coverage to GDD critical paths, identify fixed bugs without regression tests |
| `$game-studio test-setup` | Scaffold the test framework and CI/CD pipeline for the project's engine |
| `$game-studio test-helpers` | Generate engine-specific test helper libraries for the test suite |
| `$game-studio test-evidence-review` | Quality review of test files and manual evidence documents |
| `$game-studio test-flakiness` | Detect non-deterministic (flaky) tests from CI run logs |
| `$game-studio skill-test` | Validate skill files for structural compliance and behavioral correctness |
| `$game-studio skill-improve` | Improve a skill using a test-fix-retest loop — diagnose, propose fix, rewrite, verify |

## Production

| Command | Purpose |
|---------|---------|
| `$game-studio milestone-review` | Review milestone progress and generate status report |
| `$game-studio retrospective` | Run a structured sprint or milestone retrospective |
| `$game-studio bug-report` | Create a structured bug report |
| `$game-studio bug-triage` | Read all open bugs, re-evaluate priority vs. severity, assign owner and label |
| `$game-studio reverse-document` | Generate design or architecture docs from existing implementation |
| `$game-studio playtest-report` | Generate a structured playtest report or analyze existing playtest notes |

## Release

| Command | Purpose |
|---------|---------|
| `$game-studio release-checklist` | Generate and validate a pre-release checklist for the current build |
| `$game-studio launch-checklist` | Complete launch readiness validation across all departments |
| `$game-studio changelog` | Auto-generate changelog from git commits and sprint data |
| `$game-studio patch-notes` | Generate player-facing patch notes from git history and internal data |
| `$game-studio hotfix` | Emergency fix workflow with audit trail, bypassing normal sprint process |
| `$game-studio day-one-patch` | Prepare a focused day-one patch for known issues discovered after gold master but before or at public launch |

## Creative & Content

| Command | Purpose |
|---------|---------|
| `$game-studio prototype` | Concept prototype — throwaway build right after brainstorm to validate core idea (Phase 1) |
| `$game-studio vertical-slice` | Pre-Production validation — production-quality end-to-end build before committing to Production (Phase 4) |
| `$game-studio onboard` | Generate contextual onboarding document for a new contributor or agent |
| `$game-studio localize` | Localization workflow: string extraction, validation, translation readiness |

## Team Orchestration

Coordinate multiple agents on a single feature area:

| Command | Coordinates |
|---------|-------------|
| `$game-studio team-combat` | game-designer + gameplay-programmer + ai-programmer + technical-artist + sound-designer + qa-tester |
| `$game-studio team-narrative` | narrative-director + writer + world-builder + level-designer |
| `$game-studio team-ui` | ux-designer + ui-programmer + art-director + accessibility-specialist |
| `$game-studio team-release` | release-manager + qa-lead + devops-engineer + producer |
| `$game-studio team-polish` | performance-analyst + technical-artist + sound-designer + qa-tester |
| `$game-studio team-audio` | audio-director + sound-designer + technical-artist + gameplay-programmer |
| `$game-studio team-level` | level-designer + narrative-director + world-builder + art-director + systems-designer + qa-tester |
| `$game-studio team-live-ops` | live-ops-designer + economy-designer + community-manager + analytics-engineer |
| `$game-studio team-qa` | qa-lead + qa-tester + gameplay-programmer + producer |

## Overlap with Codex's bundled skills

Codex ships its own skills, and one name collides with CCGS's.

| You type | You get | Use it for |
|---------|---------|-----------|
| `$game-studio code-review` | **CCGS's** — project skills take the bare name | Architectural review against this project's coding standards, SOLID, testability and the control manifest. Knows about ADRs, stories and `docs/architecture/`. |
| `/review` | **Codex's bundled** review — the alias of its `$game-studio code-review`, which CCGS's skill shadows | Reviewing a pull request or a plain diff for correctness bugs, with no knowledge of CCGS's design documents or gates. |

Both are useful; they answer different questions. Reach for the CCGS one during
`$game-studio dev-story` and before `$game-studio story-done`, because it checks the things the gates
later check. Reach for the bundled one when you want a general review of a diff
that has nothing to do with a story.
