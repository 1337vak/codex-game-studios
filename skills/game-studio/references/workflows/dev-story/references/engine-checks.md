> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Phase 6: Parse check and capture on Unity and Unreal

Read only when the engine is Unity or Unreal. Report the command, its exit code
and any error lines. No executable: `parse NOT VERIFIED — engine binary not
available`.

## Unity

**Parse check:** the `commands.smoke` command (`-batchmode -quit -projectPath .
-logFile -`). Exit 1 with `error CS…` lines means a script does not compile.

## Unreal

**Parse check:** build the editor target. A compile error fails it (`Result:
Failed`, non-zero exit).

- Windows: `"<UE root>/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.exe" <Project>Editor Win64 Development -Project="<absolute path>/<Project>.uproject"`
- Linux: `"<UE root>/Engine/Build/BatchFiles/Linux/Build.sh" <Project>Editor Linux Development -Project=…`
- macOS: `"<UE root>/Engine/Build/BatchFiles/Mac/Build.sh" <Project>Editor Mac Development -Project=…`

The commands are from Epic's documentation, as recorded in
`docs/engine-reference/unreal/current-best-practices.md` ("Command Line").

**Capture:** launch straight into the map the story touched, as
`run-and-observe.md` gives it.
