> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Your Path

Here's your path at rigor `[value]`. Every skill still runs at any rigor; rigor changes
what's required, not what's allowed.

**`minimal`: 4 steps to running code**
1. `$game-studio setup-engine`: choose and configure the engine
2. `$game-studio brainstorm`: write the one-page `design/game-brief.md`
3. `$game-studio create-stories`: turn the brief's MVP list into stories (no epics or sprint plan needed)
4. `$game-studio dev-story`: the first line of game code

**`standard`**
- Concept: `$game-studio setup-engine` → `$game-studio brainstorm` → `$game-studio prototype` → `$game-studio art-bible` → `$game-studio gate-check`
- Systems Design: `$game-studio map-systems` → `$game-studio design-system` (once per system) → `$game-studio review-all-gdds` →
  `$game-studio gate-check`
- Architecture: `$game-studio create-architecture` → `$game-studio architecture-decision` (once per decision) →
  `$game-studio create-control-manifest` → `$game-studio architecture-review` → `$game-studio test-setup` → `$game-studio ux-design`
  (accessibility and interaction patterns) → `$game-studio gate-check`
- Pre-Production: `$game-studio ux-design` (HUD and key screens) → `$game-studio create-epics` → `$game-studio create-stories` →
  `$game-studio sprint-plan` → `$game-studio gate-check`
- Production: `$game-studio dev-story`

Each `$game-studio gate-check` moves the project one stage, and only when it passes.

**`full`:** everything in `standard`, plus `$game-studio vertical-slice` and `$game-studio playtest-report` in
Pre-Production and `$game-studio design-review` after each GDD.

**Path D with existing work** (stage `Systems Design` or later, or code on disk) gets this instead.
Print only the steps that apply, and for the brief only the one source that applies. At `minimal`:
1. `$game-studio project-stage-detect`: what stage the project is at and what is missing
2. `$game-studio adopt`: whether the existing files are in the format the skills read
3. `$game-studio setup-engine`: only when no engine is set; leave it out when `engine` names one
4. The brief, only if `concept` is absent: `$game-studio reverse-document design [code_root]` when the code
   root holds 10 or more source files (it writes the brief from the game), and then do not mention
   `$game-studio brainstorm` at all; `$game-studio brainstorm` only when it holds fewer

At `standard` and `full`, steps 1 to 3, then `$game-studio design-system retrofit [path]`,
`$game-studio architecture-decision retrofit [path]`, `$game-studio architecture-review` and `$game-studio gate-check`.

`minimal` is the documented floor, not a lesser mode. Its trade: no GDDs, so design
problems show up in code.
