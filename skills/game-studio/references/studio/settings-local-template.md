> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# settings.local.json Template

## Example settings.local.json

```json
{
  "permissions": {
    "allow": [
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(npm run *)"
    ],
    "deny": [
      "Bash(git push *)"
    ]
  }
}
```

## Permission Modes

### During Development — Manual (`default`)
Claude asks before running most commands and before editing files. This is the
safest for production code.

### During Prototyping — `acceptEdits`
File edits and common filesystem commands such as `mkdir` and `mv` are accepted
without asking; other commands still ask. It applies to the whole working
directory, not only `prototypes/`, so switch back when you return to production
code.

### During Code Review — `plan`
Claude reads files and runs read-only commands to explore, but does not edit
your source files.

### `auto`
Runs without routine prompts: a background classifier checks each action before
it runs. A local `defaultMode` cannot start a terminal session in it; switch
during the session instead (`setup-requirements.md` lists the routes).

## Customizing Hooks Locally

You can add personal hooks in `settings.local.json` that extend (not override)
the project hooks. For example, a personal log line each time Claude finishes a
response:

A hook's output reaches Claude for only a few events, such as `SessionStart`
and `UserPromptSubmit`. For the others, including `Stop`, Codex writes
stdout to the debug log, so a hook that only prints shows nothing: write to a
file, as above, or to another tool. `Stop` fires at the end of every response,
not once per session.
