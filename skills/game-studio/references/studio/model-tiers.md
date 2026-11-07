> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Model Tier Assignment

Skills and agents are assigned tiers by task complexity. A tier is written as
the alias `model:` takes, never as a model ID: Codex resolves each alias
to the current model in that family, so this table does not change when a new
model ships.

**Agent model tiers.** 30 agents use `model: inherit` and run on the session's
model. 19 are pinned:

Every agent not named above is `inherit`. The `model:` line in the agent's own
file is what runs.

```json
{ "env": { "CLAUDE_CODE_SUBAGENT_MODEL_FORCE": "1" } }
```
