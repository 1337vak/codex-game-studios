# Native Codex contract

The studio's domain procedures, report verdicts, and evidence requirements carry
over. Use the tools, concurrency limits, engine, and authorization available in
the current Codex session. Read the plugin's `COMPATIBILITY.md` for recorded
conversion decisions. `<plugin-root>` is two directories above this skill folder;
in any other installed skill, it is two directories above that skill's folder.

## Authorization and scope

The user's existing instructions and authorization govern the task. Continue
authorized implementation across phases. Source phrases such as “May I write”
describe the original collaboration procedure; they do not reset existing
authorization or impose a fresh prompt for each file. Preserve actual product
decisions, user preferences, missing inputs, and explicit approval conditions.
Ask when information or authorization is materially missing. Do not infer that a
director's approval authorizes a publication or account change.

## Tool and role translation

| Source mechanism | Codex adaptation |
| --- | --- |
| Named `Agent` / role brief | Read the matching `references/roles/` file and pass its relevant expertise to a native subagent if available; otherwise perform the role directly. |
| Claude model tiers | Inherit the current session model. Source model metadata is provenance, not an instruction to choose a different provider model. |
| Task and team APIs | Use available native task/delegation tools or concise local tracking. Do not invent an API from a source tool name. |
| Slash workflow | Invoke the corresponding native skill explicitly, such as `$game-studio:prototype`. `$game-studio:game-studio` also finds it through the catalog. |
| Source shell preprocessing (`!` followed by a backtick) | It is not executed. Read the needed project configuration explicitly; do not claim that a source “resolved above” block ran. |
| Source tool allowlists and permissions | Advisory source metadata only; actual host permissions apply. |
| Role hierarchy | Select relevant expertise within actual limits. Do not spawn every named role or stop authorized work merely because another role title owns it. |

## Shared resources and automation

Generated `shared/docs/` and `shared/rules/` retain the upstream studio's domain
guides, templates, and conventions. They are references loaded when relevant,
not active project instructions. `shared/scripts/` and `shared/source-hooks/`
retain source helpers for inspection and attribution. They are not installed as
commands or lifecycle handlers. Their `.claude` paths and project-template state
assumptions need review before any explicit execution in another project.

The plugin adapts one useful QA check: after a supported file-write tool event,
`hooks/validate_assets.py` validates changed JSON data under `assets/`, `Assets/`,
or `Content/`. It shares the read-only parser used by the authored asset-audit
helper, accepts UTF-8 BOM files, reports malformed data to the model, and changes
no files. This is a narrower adaptation of `validate-assets.sh`; naming standards
and asset budgets still come from the actual project. Installing the plugin does
not trust its hook automatically. Review the definition through Codex's hook
trust flow before expecting it to run. Direct fixture execution is distinct from
testing hook activation through Codex.

The other project-template hooks are inventoried as reference-only rather than
silently enabled: session logs, update checks, source registry/write guards,
director artifacts, and Windows notifications depend on the original layout,
policy, or unsupported events. The generated conversion report records this
limitation. Do not claim those checks ran.

## Evidence and engine behavior

Repository paths such as `design/`, `production/`, and `project.yaml` are optional
upstream conventions. Use the existing game's organization and engine version.
Do not create a documentation hierarchy as a prerequisite to improving a game.

Current project requirements and measured evidence take precedence over broad
source defaults. Unity non-power-of-two textures, Resources, the built-in pipeline,
and legacy input are not defects merely because a source brief prefers something
else. Assess suitability for the actual prototype and target.

Keep domain decisions intact: a prototype without playtest evidence is
`NOT ASSESSED`, a missing measurement is not a clean audit, and a director's
`NOT ASSESSED` verdict is not approval. For visual changes inspect native renders,
pose extremes, transitions, and motion. Still frames cannot establish real-time
smoothness or subjective audio quality.
