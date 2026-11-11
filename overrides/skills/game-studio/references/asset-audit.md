# Asset audit

Resolve the actual asset root from the game project. The helper measures PNG,
WAV and JSON assets without modifying them. It reports observations and parse
errors, not compliance verdicts or guessed budgets.

Compare source image dimensions and alpha with runtime importer settings and
atlas coordinates. Unity NPOT textures are valid; disabling unwanted NPOT
rescaling can be essential for precise atlas registration. Check filtering,
compression and color space against the intended appearance. A compression or
memory recommendation needs a measured budget and target, not a blanket rule.

Measure audio duration, channels, sample rate, PCM format and peak/clipping when
appropriate. Confirm synthetic sample provenance, dialogue onset and silent
tail. Rendered output audio and player audio should use matching timing and mix.

Check referenced files exist using the actual manifest and engine references.
Code text search alone cannot prove a Unity asset is orphaned; scenes, prefabs,
Resources paths and Addressables may reference it. Never delete from a scan.

Report missing budgets or unmeasured usage as not assessed. Keep original assets
and reference provenance distinct; reference-study artwork must not enter the
game's production assets accidentally.
