> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Team Release

When this skill is invoked, orchestrate the release team through a structured pipeline.

## Team Composition
- **release-manager** — Release tag, versioning, changelog, patch notes, deployment
- **qa-lead** — Test sign-off, regression suite, release quality gate
- **devops-engineer** — Build pipeline, artifacts, deployment automation
- **security-engineer** — Pre-release security audit (invoke if game has online/multiplayer features or player data)
- **network-programmer** — Netcode stability sign-off (invoke if game has multiplayer)
- **analytics-engineer** — Verify telemetry events fire correctly and dashboards are live
- **localization-lead** — Verify every shipped string is translated
- **performance-analyst** — Benchmark the release build against its performance targets
- **community-manager** — Launch announcement and player-facing messaging, written from the patch notes
- **producer** — Go/no-go decision, stakeholder communication, scheduling

## Pipeline

### Phase 1: Release Planning
Delegate to **producer**:
- Confirm all milestone acceptance criteria are met
- Identify any scope items deferred from this release
- Set the target release date and communicate to team
- Output: release authorization with scope confirmation

### Phase 2: Release Candidate
Delegate to **release-manager**:
- Bump version numbers in all relevant files on `main`; the commit carrying the bump is the release candidate. Development is trunk-based — a release is a tag on `main` (applied in Phase 6), not a branch
- Confirm the release checklist from Polish (`$game-studio release-checklist`, run before `$game-studio gate-check release`) is complete for this candidate; run it now only if none exists
- Cut a `release/[version]` branch from the candidate only if this release needs stabilising (a freeze, platform certification) — bug fixes only there, and every fix lands on `main` as well
- Output: release candidate commit (plus the `release/*` branch, if one was cut) and checklist

### Phase 3: Quality Gate (parallel)
Delegate in parallel:
- **qa-lead**: Execute full regression test suite. Test all critical paths. Verify no open bugs at the severities `$game-studio gate-check release` blocks for this `workflow`: S1 at every tier, S2 and S3 too at `full`. Sign off on quality.
- **devops-engineer**: Build release artifacts for all target platforms. Verify builds are clean and reproducible. Run automated tests in CI.
- **security-engineer** *(if game has online features, multiplayer, or player data)*: Conduct pre-release security audit. Review authentication, anti-cheat, data privacy compliance. Sign off on security posture.
- **network-programmer** *(if game has multiplayer)*: Sign off on netcode stability. Verify lag compensation, reconnect handling, and bandwidth usage under load.

When either agent is in the active set, decide its condition from `platform.online` and `platform.multiplayer` in `project.yaml`, plus whether the game stores player data. A key that is absent is not a `false`: ask the user rather than assume an offline game. An agent skipped on these grounds says so by name in the Phase 3 output — e.g. `security-engineer: not spawned — platform.online: false, platform.multiplayer: false, no player data`.

### Phase 4: Localization, Performance, and Analytics
Delegate (can run in parallel with Phase 3 if resources available):
- Verify all strings are translated (delegate to **localization-lead** if available)
- Run performance benchmarks against targets (delegate to **performance-analyst** if available)
- **analytics-engineer**: Verify all telemetry events fire correctly on release build. Confirm dashboards are receiving data. Check that critical funnels (onboarding, progression, monetization if applicable) are instrumented.
- Output: localization, performance, and analytics sign-off — one file per agent (table above)

### Phase 5: Go/No-Go
Before delegating, get the **technical-director** release sign-off. The producer
cannot spawn agents, so the orchestrator does: spawn `technical-director` at
`review_mode: full` only — this is a director review, not a PHASE-GATE, so `lean`
and `solo` skip it. Ask for GO, CONCERNS or NO-GO on the release candidate's
technical state, or NOT ASSESSED naming what it could not read. When it is not
spawned, the go/no-go record says `technical-director sign-off: not run
(review_mode: <mode>)` instead of listing it as given; a NOT ASSESSED answer is
recorded as such and never counted as a sign-off.

Delegate to **producer**, passing every sign-off collected so far:
- Collect sign-off from: qa-lead, release-manager, devops-engineer, security-engineer (if spawned in Phase 3), network-programmer (if spawned in Phase 3), and technical-director (if spawned above)
- Carry a stage-check override, if there was one, into the go/no-go record as its `Stage override:` line
- Evaluate any open issues — are they blocking or can they ship?
- Make the go/no-go call
- Output: release decision with rationale

After the user selects "Override NO-GO with documented rationale":
- Ask (plain text, not widget): "Please describe the justification for overriding the NO-GO verdict. This will be embedded in the release record."
- Wait for the user's written justification.
- Embed the justification text in the partial approval record before Phase 6: append a "⚠️ Override Justification: [user's text]" field.
- Only then proceed to Phase 6.

### Phase 6: Deployment (if GO)

In parallel with deployment, delegate to **release-manager**:
- Finalize the patch notes drafted in Polish using `$game-studio patch-notes [version]` — release-manager carries that skill and the Bash access its `git log` step needs; `community-manager` has neither

Then hand those patch notes to **community-manager**:
- Prepare launch announcement (store page updates, social media, community post)
- Draft known issues post if any S3+ issues shipped
- Output: all player-facing release communication, ready to publish on deploy confirmation

### Phase 7: Post-Release
- **release-manager**: Generate release report (what shipped, what was deferred, metrics)
- **producer**: Update milestone tracking, communicate to stakeholders
- **qa-lead**: Monitor incoming bug reports for regressions
- **community-manager**: Publish all player-facing communication, monitor community sentiment
- **analytics-engineer**: Confirm live dashboards are healthy; alert if any critical events are missing
- Keep the 48-hour monitoring window from Phase 6: bugs, dashboards and community sentiment are watched for 48 hours after release (release-manager's own watch runs to its 72h report)
- Schedule post-release retrospective if issues occurred

## Error Recovery Protocol

**First, verify the artifact.** If the return contract named a path, check the
path exists before treating the phase as done — **a named artifact that is not
on disk is a failed phase, however fluent the response reads.** An agent can
burn a full phase and return a plausible preamble having written nothing, which
is neither BLOCKED nor an error nor "cannot complete", so the trigger below
never fires. Resume it naming the unmet contract; the context is
usually still there.

If any spawned agent returns BLOCKED, errors, or cannot complete: **surface it
immediately, don't proceed past a dependency it blocks, and always produce a
partial report.** Full procedure: `<skill-root>/references/studio/error-recovery-protocol.md`.

Common blockers:
- Input file missing (story not found, GDD absent) → redirect to the skill that creates it
- ADR status is Proposed → do not implement; accept it with `$game-studio architecture-decision accept ADR-NNNN` once decided
- Scope too large → split into two stories via `$game-studio create-stories`
- Conflicting instructions between ADR and story → surface the conflict, do not guess

## Output

A summary report covering: release version, scope, quality gate results, go/no-go decision, deployment status, and monitoring plan.

Verdict: **COMPLETE** — release executed and deployed.
Verdict: **BLOCKED** — release halted; the stage check stopped it, go/no-go was NO, or a hard blocker is unresolved.

## Next Steps

- Monitor post-release dashboards for 48 hours.
- Run `$game-studio retrospective` if significant issues occurred during the release.
- `project.stage` reads `Release` unless the stage check was overridden: `$game-studio gate-check release` is the Polish → Release readiness gate, run before this skill. After an override the stage still reads what it did. Only `$game-studio gate-check` changes `project.stage` (on a PASS, or a CONCERNS whose risks the user accepted), so this skill never writes it or `production/stage.txt`. `Release` is the terminal stage in the `project.stage` enum — there is no post-launch stage value. Record live/post-launch status in the release report, not in `project.stage`.
