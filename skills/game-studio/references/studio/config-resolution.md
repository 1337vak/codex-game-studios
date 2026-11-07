> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Config Resolution

How a skill learns its effective settings. **One command, no prose chain.**

## The rule

A skill that needs config puts this near the top of its **body** (not frontmatter):

`

**and** pre-approves exactly that command in its own frontmatter, with its own
directory name in the path:

`

The command runs as preprocessing *before the model sees the skill*, and its
output replaces the placeholder inline. The skill then reads the resolved values
and **does not re-derive them**.

Skills that resolve a per-system tier pass the system name: `resolve_config combat`.

## Why the body, not `context:`

## Why exactly this command — the permission check

Codex permission-checks every injected command **before** the skill
renders. Outside auto mode, anything that does not come back "allow" — including
a command that would normally just prompt — **aborts the whole invocation**, and
the model never sees the skill. A read-only command such as `git status`, which
Codex approves on its own, comes back "allow" and runs without a grant. A preloaded skill (`skills:` on an agent) is
checked the same way at agent launch, so a failing bootstrap line stops the agent
from starting. In default
mode, the bootstrap forms behave as follows:

What that table rules out:

Auto mode can approve the old form on its own, which is how v1.1.0 shipped with
it. Test bootstrap changes in default mode, in a project without a
`settings.local.json`.

`disableSkillShellExecution: true` replaces every injected command with a
placeholder message. If a skill sees no config block, it falls back to the
defaults below.

## The block

```
=== CCGS Resolved Config ===
review_mode: lean (production/review-mode.txt)
automation: guided (project.local.yaml)
workflow: standard (project.yaml)
docs.density: balanced (rigor:standard)
story_granularity: balanced (rigor:standard)
qa.level: standard (rigor:standard)
team.size: individual (rigor:standard)
project.stage: Systems Design (production/stage.txt)
automation_always_ask: scope_changes, file_deletions, schema_changes (default)
engine: Godot 4.7 (project.yaml)
testing.strict: logic=true integration=false visual=unset ui=unset config=unset (unset = each skill applies its own default)
system_overrides: combat=full inventory=minimal
notes: none
Values above are fully resolved (local -> yaml -> legacy -> default). Use as-is.
An inline --review flag, if passed, overrides review_mode.
=== end CCGS config ===
```

Every knob line ends with its **provenance** in parentheses. That is what makes a
wrong value diagnosable — `review_mode: solo (rigor:minimal)` when `project.yaml` says
`full` points straight at the problem.

## Resolution chain

| Step | Source | Applies to |
|---|---|---|
| 1 | `project.local.yaml` | any setting on the `$game-studio settings --local` whitelist (12 keys — `modes.review_mode`, `modes.automation`, `modes.automation_always_ask`, `team.size`, all five `testing.strict.*`, `performance.enforce`, `features.*`) |
| 2 | `project.yaml` | all keys |
| 3 | legacy plain-text mirror | `modes.review_mode` → `production/review-mode.txt`; `project.stage` → `production/stage.txt` |
| 4 | **`modes.rigor` expansion** | the six knobs `rigor` fronts — `modes.workflow`, `docs.density`, `qa.level`, `modes.story_granularity`, `modes.review_mode`, `team.size` |
| 5 | documented default | the table below |

An **enum-invalid value does not win** — the chain continues past it and the
rejected value is named on the `notes:` line. A typo degrades to the documented
default rather than propagating a nonsense mode into every skill.

> **Step 4 sits below every explicit source and above the terminal default, and
> that ordering is the whole back-compat guarantee.** A `project.yaml` that
> already sets `docs.density: terse` resolves exactly as it did before `rigor`
> existed, because step 2 answers first. Invert steps 4 and 5 and `rigor` becomes
> a no-op; hoist step 4 above step 2 and it silently overrides settings people
> already have.
>
> Derived values report their provenance as **`rigor:<level>`**, so the source
> vocabulary is `{project.local.yaml, project.yaml, <legacy path>, rigor:<level>,
> default, unset}`. `docs.density: balanced (rigor:standard)` says the value was
> never written down anywhere — it follows the project's rigor level and will
> move if that level moves.

> **Read scope == write whitelist.** Anything `$game-studio settings --local` may *write*
> is also *read* during resolution. If the read scope were ever narrower,
> `$game-studio settings --local modes.review_mode=solo` would write a value
> that `$game-studio settings` accepted and displayed and every skill then ignored. The
> test suite asserts the two lists stay in step — adding a setting to one
> without the other reproduces that bug.
>
> This matches the spec: `effects-map.md` § "Local Override Pattern" has always
> stated the chain applies to *every* setting. The narrow read scope was an
> implementation gap, not a design.

> **A key OUTSIDE the whitelist, hand-written into `project.local.yaml`, is
> reported rather than swallowed.** `$game-studio settings --local` refuses to
> write one, but the file exists to be edited by hand, so that path needs its own
> guard. `modes.rigor: full` written there is a real key with a legal value, so
> `validate_yaml_enum` passes it — and then resolution never consults the local
> file for that path, so the setting vanishes and the user sees the default they
> were trying to override, with no error anywhere. Every check in the chain
> validated the **value**; nothing validated the **location**.
>
> `validate_local_scope` now names such keys on `notes:`. It **warns and never
> reconciles**, the same shape as the stage-mirror check: it does not edit the
> file, does not begin honouring the key, and does not change resolution. A
> locked setting is locked because it decides which artifacts exist on disk, so
> a helper that quietly applied one would let two developers' checkouts diverge
> — the exact thing the whitelist prevents. The user moves the key to
> `project.yaml` or deletes it.
>
> `schema_version` and `framework.*` are exempt: `effects-map.md` classes them as
> file metadata rather than preferences, and a `project.local.yaml` carrying
> `schema_version: 1` is correct as written.

## Defaults

| Knob | Default |
|---|---|
| `modes.automation` | `collaborative` |
| `modes.rigor` | `minimal` |
| `modes.automation_always_ask` | `scope_changes`, `file_deletions`, `schema_changes` |

**The six knobs `rigor` fronts have no terminal default at all.** `modes.workflow`,
`docs.density`, `qa.level`, `modes.story_granularity`, `modes.review_mode` and `team.size` are
deliberately absent from `_yaml_helper_defaults`: a default there would answer at step 5 before the
expansion at step 4 ever ran, making `rigor` a no-op for anyone who had not also
set the sub-knob. Their effective values come from the rigor level:

| `modes.rigor` | `modes.workflow` | `docs.density` | `qa.level` | `modes.story_granularity` | `modes.review_mode` | `team.size` |
|---|---|---|---|---|---|---|
| `minimal` (default) | `minimal` | `terse` | `minimal` | `coarse` | `solo` | `individual` |
| `standard` | `standard` | `balanced` | `standard` | `balanced` | `lean` | `individual` |
| `full` | `full` | `thorough` | `full` | `fine` | `full` | `studio` |

> **The flip DOES reach existing projects.** A `project.yaml` that sets some of
> the six explicitly but never sets `rigor` keeps its explicit values and takes
> the new `minimal` row for the rest -- so an unset `qa.level` that used to
> resolve `standard` now resolves `minimal`.
> Pin the old behaviour by setting `modes.rigor: standard` explicitly; see
> UPGRADING.md.

`modes.workflow` is **fronted, not replaced**: it keeps
`workflow_overrides.system_overrides`, which still beats the derived value.
Setting any of the six explicitly overrides just that one and leaves
its siblings on the rigor level, which is how "comprehensive but compact"
(`rigor: full` + `docs.density: terse`) stays expressible. Two of the six —
`modes.review_mode` and `team.size` — are personal-experience knobs that also
remain overridable from `project.local.yaml` (that source sits above the
expansion), unlike the four on-disk knobs, which are locked.

> **Keep this table in step with the helper.** Every knob listed here must carry
> the value `_yaml_helper_defaults` returns (read it through `get_yaml_default`),
> and none of the six fronted knobs may appear in it.

**`testing.strict.*` has no central default on purpose.** Its unset default
differs per skill by design: `$game-studio smoke-check` treats unset as **blocking** (it is a
build-health gate), while `$game-studio story-done` and `$game-studio dev-story` apply the per-story-type
table in `<skill-root>/references/studio/coding-standards.md`. The `testing.strict` line therefore
reports only the *configured state* (`unset` where absent). The `gate_level` line
(below) applies that table and names `$game-studio smoke-check`'s own default beside `config`.

**The `engine` line is reported from `project.yaml` only.** The `engine_values`
line (below) adds the per-field fallback to `<skill-root>/references/studio/technical-preferences.md`,
which also remains the sole source for forbidden patterns and allowed libraries —
those never migrated.

## Derived lines (named only)

Six more lines answer steps skills would otherwise work out by hand. Each prints
**only when named** in `--keys`; the full block never includes them. Each value carries its source in parentheses, and YAML `null`
or `~` reads as unset (the reader returns them as strings, which are not empty).

| Label | What it prints |
|---|---|
| `gate_level` | The gate level per story type: `testing.strict.<type>` (`project.local.yaml`, then `project.yaml`), then the plain `testing.strict: true\|false`, then the default table in `coding-standards.md`. `gate_level: logic=blocking(default) integration=advisory(project.yaml) visual=blocking(default) ui=blocking(default) config=advisory(default; $game-studio smoke-check: blocking)` |
| `engine_values` | `engine.name`, `.version` and `.language`, each falling back to `technical-preferences.md` (its Engine line holds name and version together). `engine_values: name=Godot(project.yaml) version=4.7(project.yaml) language=GDScript(project.yaml)` |
| `specialists` | The engine specialists: `primary` from the engine, the rest from the `specialists` block, where `null` is unset and never an agent name; `technical-preferences.md` only when the block is absent. `specialists: primary=godot-specialist(engine.name) code=godot-gdscript-specialist shader=unset ui=godot-specialist additional=none (project.yaml; unset = skip that specialist)` |
| `review_gate` | Whether a skill's own director gate and the PHASE-GATEs run at the resolved `review_mode` (`director-gates.md`): `solo` none, `lean` the PHASE-GATEs only, `full` all. `review_gate: skill-gates=skip phase-gates=run (review_mode lean, rigor:standard; a --review flag overrides)` |
| `input_methods` | The input methods from the `platform` block, each listed once: keyboard/mouse when `PC` or `Web` is a target, gamepad and touch when their support is Full or Partial, plus the primary input, where a primary input such as `Keyboard`, `Controller` or `Touchscreen` is read as keyboard/mouse, gamepad or touch; else `technical-preferences.md`'s Input Methods line. `input_methods: keyboard/mouse, gamepad (project.yaml platform; primary: Gamepad)` |
| `perf_budgets` | The four `performance.*` budgets (`target_framerate`, `frame_budget_ms`, `draw_call_limit`, `memory_ceiling_mb`), from `project.yaml` only: they are not locally overridable. `perf_budgets: target_framerate=60 frame_budget_ms=16.67 draw_call_limit=unset memory_ceiling_mb=unset (project.yaml)` |

## Failure modes

`resolve_config` **always exits 0 and always emits a complete block.** Each
condition below degrades to defaults and is named on `notes:`:

A skill must never treat a missing block as "config is unset in an interesting
way". It means the block did not render; the defaults apply. The exception is
that task notice: the settings line ran out of time, not the settings, so read
the files as that row says instead of taking the defaults. If it keeps
happening, exclude the project folder from real-time scanning.

### An input that resolves without a note

Here `resolve_config` follows a fixed rule and emits no note, so it does not tell
you that something you wrote was not used.

| Input | What happens | Note emitted |
|---|---|---|
| **Wrong shape** — a list where a scalar belongs (`rigor:` followed by `- standard`) | key resolves empty, falls through to the default | **none** |

An enum-*invalid* value is announced (`modes.workflow: 'medium' is not a valid
value … — ignored, chain continued`), and so is a duplicate key. A wrong shape
is not: the key is present but resolves to nothing, which is also what a key
with an empty value does on purpose (the "Key present, value empty" row above),
and `resolve_config` does not tell the two apart. When a setting seems ignored,
check the structure of its key in the file: one scalar on the key's own line and
no list under it. `$game-studio settings` shows the value that is actually in effect.

Merging a repeated block and taking the last value of a repeated key are fixed
rules here, but most other YAML tools keep only the last block. Combine repeated
blocks rather than rely on the merge.

## Why not inject at session start

`resolve_config` is also safe to call from a hook, but session-start does **not**
call it. The block would cost tokens on every session whether or not any skill
needs config, and it would go stale mid-session as `$game-studio settings` writes land. The
per-skill body call is fresher and only loads where it is used. Session start
still prints the resolved review mode and any schema errors, which is the part a
human reads.

## Testing

The resolution chain, the legacy reader, enum fall-through, block shape and
every failure mode above are covered by the framework's own test suite under
`tests/`, along with the `modes.rigor` expansion and its precedence in both
directions. Two properties are asserted that are easy to lose:

- The local **read** scope and the `$game-studio settings --local` **write** whitelist stay
  in step. If they drift, `$game-studio settings` accepts and displays a value that every
  skill then ignores.
- The expansion is *reachable* (`$game-studio start` asks about it) and *legible*
  (`$game-studio settings` reports derived values rather than "(not set)"). A correct
  expansion nobody is asked about and no view displays would be worth nothing.
