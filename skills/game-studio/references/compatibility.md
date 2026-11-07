# Native Codex contract

The original studio used Claude-specific tools, lifecycle hooks, model routing,
permission modes and shell interpolation. This port loads reusable expertise
through one skill and delegates through the tools available in the current Codex
session. It does not emulate those APIs or silently enable any hook.

## Authorization and scope

The user's existing instructions and authorization govern the task. Proceed with
authorized reversible edits and implementation; record reasonable assumptions.
Ask for material missing information only when it cannot be inferred or checked.
Existing autonomy instructions continue across phases. Source references to
approvals or decision gates mean a quality decision within that scope, not a
mandatory new user prompt. External publication, communications and account
changes require their own authorization. Do not alter security configuration.

## Tool and role translation

| Upstream mechanism | Codex behavior |
| --- | --- |
| Named `Agent` / `subagent_type` | Load a role brief into a native subagent task, if available; otherwise perform that role directly. |
| Claude model tiers | Inherit the current model; do not add provider-specific model overrides. |
| Task lists and team messages | Use native task/delegation tools that actually exist; otherwise concise local tracking. |
| Slash workflow | Invoke `$game-studio` with the workflow name; these are not registered slash commands. |
| Automatic shell interpolation | Read inputs explicitly; execute only inspected, relevant commands. |
| Lifecycle hooks and tool allowlists | Not installed or enforced. Run the relevant checks explicitly and report their result. |
| Mandatory per-file approvals | Follow current user authorization; routine authorized writes proceed. |
| Role hierarchy | Select expertise as useful; obey actual agent limits, never spawn 49 roles automatically. |

## References and checks

The converted references retain domain procedures; transport-specific sections
were removed with an auditable log in `docs/codex-port/conversion-log.json` in the
port repository. The original `.claude` tree is retained there for comparison.
The upstream shell scripts and 18 hook-directory files are not installed or
automatically run. Some references describe legacy helper observations; obtain
equivalent evidence through current tools or mark the check not assessed.

Repository paths such as `design/`, `production/` and `project.yaml` are optional
upstream conventions. Use the existing game's organization. Do not manufacture
a complete documentation hierarchy before improving a working game. Do not
read engine-version pins from this template as facts about another project:
inspect that project's installed engine and project settings.

Current project requirements and measured evidence take precedence over broad
upstream preferences. In particular, Unity non-power-of-two textures, Resources,
the built-in pipeline and legacy input are not defects merely because the source
brief prefers alternatives. Assess fitness for the actual prototype and target.

For visual changes, inspect native renders, pose extremes, transitions and motion.
Still or sampled-frame review cannot establish real-time smoothness or subjective
audio quality. Distinguish observations, hypotheses, checks not run and defects.
