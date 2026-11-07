> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Active Hooks

Warnings from the `validate-*` hooks are shown to you and passed to Claude (only
to you from `validate-agent-artifact.sh`)
as hook JSON (`hook_warn` in `yaml-helper.sh`); only a problem that must be fixed
now exits 2, and the read guard's refusal. See `hooks-reference/hook-input-schemas.md` for why stderr is not
enough.

### Subagent cost visibility

The three hooks above form one chain. `log-agent.sh` writes a record per spawn
to `production/session-logs/agent-audit.log` in a fixed three-field shape:

```
YYYYMMDD_HHMMSS | <session_id> | Agent invoked: <agent_type>
```

`session-stop.sh` greps the literal string `" | $SESSION_ID | Agent invoked: "`
to tally the current session, then writes a count plus a per-agent breakdown to
`production/session-logs/session-cost.md`.

The field order of that record is fixed. `session-stop.sh` matches it literally,
so a different order silently zeroes the spawn count instead of raising an error.

When the hook input has no session id, `session-stop.sh` writes no total. A
total spanning every session in the log would look plausible and be wrong, which
is worse than none.

`agent_type` — not `agent_name` — is the field carrying the agent name. See
`hooks-reference/hook-input-schemas.md`.

## Events considered and deliberately not added

Codex offers many more hook events than the eight the hooks above use. These were
evaluated and not adopted, for the reasons given.

Hook reference documentation: `<skill-root>/references/studio/hooks-reference/`
Hook input schema documentation: `<skill-root>/references/studio/hooks-reference/hook-input-schemas.md`
