> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Asset Spec

---

## Phase 0b: Entity & Screen Inventory (runs when no arguments and no existing inventory)

This flow produces `design/assets/entity-inventory.md` — the master list of everything
the game needs visually. Run once before asset spec work begins.

### Step 1 — Gather from docs
Read all available source material in parallel, each doc by section: find the
headings you need with the Grep tool (pattern `^#`, content mode) and Read those
ranges with offset and limit.
- `design/gdd/systems-index.md` — extract every system listed
- GDD asset content — do **not** full-read every GDD. The two wanted sections are
  standard headings, and named entities live in the registry:
  ```
  Grep pattern="## (Visual/Audio Requirements|UI Requirements)" glob="design/gdd/*.md" output_mode="content" -A 25
  ```
  For named entities (characters, enemies, buildings, items), read
  `design/registry/entities.yaml` (`entities`/`items`) if it exists and has
  entries; otherwise grep the GDDs for named content. Full-read a GDD only when
  its Visual/Audio section is missing or reads `[To be designed]` (Phase 1 already
  handles that case). VFX events surface in the Visual/Audio grep context.
- `design/art/art-bible.md` — extract: any named visual categories, asset type expectations
- `design/narrative/` — scan for any character or world entity documents if they exist (optional — not required)

### Step 2 — Build proposed inventory
Organize everything found into categories:

```
Characters / Protagonists
Enemies / Creatures
Buildings / Structures
Environment / Terrain
Items / Props
VFX / Particles
UI Screens (list each screen by name)
HUD Elements
Audio (SFX, music — descriptions only, no generation prompts)
Other
```

For each item, note the source doc it was found in.

If [B] or [D]: ask the user to describe additional items. Accept brief descriptions ("a medieval keep, used as a level background") or detailed ones — either works. Work through them collaboratively until the user is satisfied.

If [C] or [D]: ask which items to remove and why. Remove them from the list.

Write the file:

```markdown
# Visual Entity & Screen Inventory

> Generated: [date]
> Sources: [list of source docs read]

## Entities

| # | Name | Type | Description | Source | Status |
|---|------|------|-------------|--------|--------|
| 1 | [name] | Character / Enemy / Building / Environment / Item / Other | [brief description] | [source doc] | Needed |

## UI Screens

| # | Screen Name | Description | Source | Status |
|---|-------------|-------------|--------|--------|
| 1 | Main Menu | [description] | [source] | Needed |

## HUD Elements

| # | Element | Description | Source | Status |
|---|---------|-------------|--------|--------|

## Audio

| # | Name | Type (SFX / Music / Ambient) | Description | Source | Status |
|---|------|------------------------------|-------------|--------|--------|
```

After writing, tell the user:
> "Entity inventory saved. Next steps:
> - Run `$game-studio ux-design [screen name]` for each UI screen in the inventory
> - Run `$game-studio asset-spec system:[name]`, `level:[name]` or `character:[name]` for each
>   visual entity — whichever of the three the entity belongs to
> - Or run `$game-studio asset-spec` again to work through the inventory one item at a time"

---

## Phase 0: Parse Arguments

Extract:
- **Target type**: `system`, `level`, or `character`
- **Target name**: the name after the colon (normalize to kebab-case)
- **Review mode**: `--review [full|lean|solo]` if present

The effective mode is the one already resolved at the top of this skill via
`resolve_config --keys review_mode`, which applies the full chain; with nothing
set it follows `modes.rigor` — `solo` at `minimal` (the default), `lean` at
`standard`, `full` at `full`. A `--review` argument overrides it for this
run only.

**Mode behavior:**
- `full`: spawn both `art-director` and `technical-artist` in parallel
- `lean`: spawn `art-director` only — faster, skips technical constraint pass
- `solo`: no agent spawning — main session writes specs from art bible rules alone. Use for simple asset categories or when speed matters more than depth.

---

## Phase 1: Gather Context

Read all source material **before** asking the user anything. Read the art bible and
the GDD by section: find the headings you need with the Grep tool (pattern `^#`,
content mode) and Read those ranges with offset and limit.

### Required reads:
- **Art bible**: Read `design/art/art-bible.md` — fail if missing:
  > "No art bible found. Run `$game-studio art-bible` first — asset specs are anchored to the art bible's visual rules and asset standards."

  **Exception — the minimal path.** If there is no art bible but
  `design/game-brief.md` exists (at `rigor: minimal` no art bible is required),
  do not fail: anchor the specs in the brief's **Art & audio direction** line,
  and say so at the top of the output — "Anchored to the brief's one-line art
  direction; there is no art bible, so colour, shape and asset-standard rules
  below are proposals, not constraints." Offer `$game-studio art-bible` once, as optional.
  The written spec follows the same anchor: its header reads
  `> **Art direction**: design/game-brief.md (Art & audio direction) — no art bible`
  in place of the `> **Art Bible**:` line, each asset carries
  `**Brief anchor:** [the brief line applied]` in place of the **Art Bible
  Anchors** block, and no spec cites an Art Bible section or §8 tier.
  Extract: Visual Identity Statement, Color System (semantic colors), Shape Language, Asset Standards (art bible Section 8 — dimensions, formats, polycount budgets, texture resolution tiers).

- **Project config**: Read `performance.*` and `naming.*` from `project.yaml`; for any key absent or empty (including when `project.yaml` has no `performance` or `naming` block), fall back to `<skill-root>/references/studio/technical-preferences.md`. Extract performance budgets and naming conventions.

### Optional reads:
- **This target's existing spec**: if `design/assets/specs/[target-name]-assets.md` exists, read it — this is a re-run, and Phase 2 proposes only what is new or changed since (Phase 5 updates the file in place).
- **Existing manifest**: Read `design/assets/asset-manifest.md` if it exists — extract already-specced assets for this target to avoid duplicates.
- **Related specs**: Glob `design/assets/specs/*.md` — scan for assets that could be shared (e.g., a common UI element specced for one system might apply here too).

### Present context summary:
> **Asset Spec: [Target Type] — [Target Name]**
> - Source doc: [path] — [N] asset types identified
> - Art bible: found — Asset Standards at Section 8
> - Existing specs for this target: [N already specced / none]
> - Shared assets found in other specs: [list or "none"]

---

## Phase 2: Asset Identification

From the source doc, extract every asset type mentioned — explicit and implied.

**For systems**: look for VFX events, sprite references, UI elements, audio triggers, particle effects, icon needs, and any "visual feedback" language.

**For levels**: look for unique environment props, atmospheric VFX, lighting setups, ambient audio, skybox/background, and any area-specific materials.

**For characters**: look for sprite sheets (idle, walk, attack, death), portrait/avatar, VFX attached to abilities, UI representation (icon, health bar skin).

Group assets into categories:
- **Sprite / 2D Art** — character sprites, UI icons, tile sheets
- **VFX / Particles** — hit effects, ambient particles, screen effects
- **Environment** — props, tiles, backgrounds, skyboxes
- **UI** — HUD elements, menu art, fonts (if custom)
- **Audio** — SFX, music tracks, ambient loops *(note: audio specs are descriptions only — no generation prompts)*
- **3D Assets** — meshes, materials (if applicable per engine)

Do NOT proceed to Phase 3 without user confirmation of the asset list.

---

## Phase 3: Spec Generation

Spawn specialist agents based on review mode. **Issue all `Agent` calls simultaneously — do not wait for one before starting the next.**

### Full mode — spawn in parallel:

**`art-director`** via `Agent`:
- Provide: full asset list from Phase 2, art bible Visual Identity Statement, Color System, Shape Language, the source doc's visual requirements, and any reference games/art mentioned in the art bible Section 9
- Ask: "For each asset in this list, produce: (1) a 2–3 sentence visual description anchored to the art bible's shape language and color system — be specific enough that two different artists would produce consistent results; (2) a generation prompt ready for use with AI image tools (Midjourney/Stable Diffusion style — include style keywords, composition, color palette anchors, negative prompts); (3) which art bible rules directly govern this asset (cite by section). For audio assets, describe the sonic character instead of a generation prompt."

**`technical-artist`** via `Agent`:
- Provide: full asset list, art bible Asset Standards (Section 8), performance budgets (`performance.*` from `project.yaml`, else `technical-preferences.md`), engine name and version
- Ask: "For each asset in this list, specify: (1) exact dimensions or polycount (match the art bible Asset Standards tiers — do not invent new sizes); (2) file format and export settings; (3) naming convention (`naming.*` from `project.yaml`, else `technical-preferences.md`); (4) any engine-specific constraints this asset type must respect; (5) LOD requirements if applicable. Flag any asset type where the art bible's preferred standard conflicts with the engine's constraints."

### Lean mode — spawn art-director only (skip technical-artist).

### Solo mode — skip both. Derive specs from art bible rules alone, noting that technical constraints were not validated.

**Announce every skipped agent by name in the output**, before the specs:
"technical-artist skipped — Lean mode: technical constraints not validated." /
"art-director and technical-artist skipped — Solo mode: specs derived in this
session; technical constraints not validated." A spec drafted without an agent
must not read like one an agent reviewed.

**Collect both responses before Phase 4.** If any conflict exists between art-director and technical-artist (e.g., art-director specifies 4K textures but technical-artist flags the engine budget requires 512px), surface it explicitly — do NOT silently resolve.

---

## Phase 4: Compile and Review

Combine the agent outputs into a draft spec per asset. Present all specs in conversation text using this format:

```
## ASSET-[NNN] — [Asset Name]

| Field | Value |
|-------|-------|
| Category | [Sprite / VFX / Environment / UI / Audio / 3D] |
| Dimensions | [e.g. 256×256px, 4-frame sprite sheet] |
| Format | [PNG / SVG / WAV / etc.] |
| Naming | [e.g. vfx_frost_hit_01.png] |
| Polycount | [if 3D — e.g. <800 tris] |
| Texture Res | [e.g. 512px — matches Art Bible §8 Tier 2] |

**Visual Description:**
[2–3 sentences. Specific enough for two artists to produce consistent results.]

**Art Bible Anchors:**
- §3 Shape Language: [relevant rule applied]
- §4 Color System: [color role — e.g. "uses Threat Blue per semantic color rules"]

**Generation Prompt:**
[Ready-to-use prompt. Include: style keywords, composition notes, color palette anchors, lighting direction, negative prompts.]

**Status:** Needed
```

If [B]: ask which asset and what to change. Revise inline and re-present. Do NOT re-spawn agents for minor text revisions — only re-spawn if the visual direction itself needs to change.

If [C]: ask what direction to change. Re-spawn the relevant agent with the updated brief.

---

## Phase 5: Write Spec File

Write the file with:

```markdown
# Asset Specs — [Target Type]: [Target Name]

> **Source**: [path to source GDD/level/character doc]
> **Art Bible**: design/art/art-bible.md
> **Generated**: [date]
> **Status**: [N] assets specced / [N] approved / [N] in production / [N] done

[all asset specs in ASSET-NNN format]
```

Then update `design/assets/asset-manifest.md`. If it doesn't exist, create it:

```markdown
# Asset Manifest

> Last updated: [date]

## Progress Summary

| Total | Needed | In Progress | Done | Approved |
|-------|--------|-------------|------|----------|
| [N] | [N] | [N] | [N] | [N] |

## Assets by Context

### [Target Type]: [Target Name]
| Asset ID | Name | Category | Status | Spec File |
|----------|------|----------|--------|-----------|
| ASSET-001 | [name] | [category] | Needed | design/assets/specs/[target]-assets.md |
```

If the manifest already exists, append the new context block — on a re-run for this target, add the new rows to its existing block instead of appending a second one — and update the Progress Summary counts.

---

## Phase 6: Close

---

## Asset ID Assignment

Asset IDs are assigned sequentially across the entire project — not per-context. Read the manifest before assigning IDs to find the current highest number:

```
Grep pattern="ASSET-" path="design/assets/asset-manifest.md"
```

Start new assets from `ASSET-[highest + 1]`. This ensures IDs are stable and unique across the whole project.

If no manifest exists yet, start from `ASSET-001`.

---

## Shared Asset Protocol

Before speccing an asset, check if an equivalent already exists in another context's spec:

- Common UI elements (health bars, score displays) are often shared across systems
- Generic environment props may appear in multiple levels
- Character VFX (hit sparks, death effects) may reuse a base spec with color variants

If a match is found: reference the existing ASSET-ID rather than creating a duplicate. Note the shared usage in the manifest's referenced-by column.

> "ASSET-012 (Generic Hit Spark) already specced for Combat system. Reusing for Tower Defense — adding tower-defense to referenced-by."

---

## Error Recovery Protocol

If any spawned agent returns BLOCKED or cannot complete:

1. Surface immediately: "[AgentName]: BLOCKED — [reason]"
2. In `lean` mode or if `technical-artist` blocks: proceed with art-director output only — note that technical constraints were not validated
3. In `solo` mode or if `art-director` blocks: derive descriptions from art bible rules — flag as "Art director not consulted — verify against art bible before production"
4. Always produce a partial spec — never discard work because one agent blocked

---

## Recommended Next Steps

- Run `$game-studio asset-spec [next-context]` to continue speccing remaining systems, levels, or characters
- Run `$game-studio asset-audit` to validate delivered assets against the written specs and identify gaps or mismatches
