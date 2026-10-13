# Codex Execution — AERA Chromatic Denizens v1.0

**Target:** `https://github.com/xApologies/AERA`, existing `main` branch.
**Action:** INCREMENTAL publication of new Orange/Green biological canon and accepted concept art. Do not reinitialize repository, clone donors, or modify MK231.

## Preflight
1. Locate existing local AERA checkout (typically `%USERPROFILE%\_AERA`), verify `git remote -v` and clean worktree. If overlapping local modifications exist, STOP and request direction; no reset/force push.
2. Unpack this ZIP in a temporary **untracked** directory, preferably outside the checkout. Never stage `_inbox`, ZIP archives or staging files.
3. Read this entire `Executable.md`, `MANIFEST.json`, and `payload/L2/BIOLOGY/00_READ_FIRST.md`. Verify SHA-256 and byte sizes for all payload files before copying. Abort on mismatch.
4. Read current AERA `CONSTITUTION.md`, `AGENTS.md`, `FRAMEWORK_INDEX.md`, `L2/README.md`, `L2/GENESIS_BIOLOGY.md`, `examples/MK231/README.md`, `examples/MK231/SEVEN_REALMS_AND_SPECIES.md`, `provenance/DECISION_LEDGER.md`, `PROPHECIES.md`, and `prophecies/README.md` if present. These govern scope and prevent contamination.

## Apply
5. Copy the exact contents of `payload/L2/BIOLOGY/` into tracked `L2/BIOLOGY/`, the three image references into `visuals/chromatic_denizens/`, and `payload/provenance/CHROMATIC_DENIZENS_DECISION_RECORD_v1.0.md` into `provenance/`. Preserve filenames and binary bytes.
6. Add minimal links to new `L2/BIOLOGY/00_READ_FIRST.md` in `L2/README.md` and `FRAMEWORK_INDEX.md`. Add a brief dated entry to `CHANGELOG.md` and, if appropriate, a short pointer in `NEXT_THREAD_HANDOFF.md`.
7. Update only *current AERA framework default-denizen summary wording* in existing docs if it explicitly asserts Phoenix/Kitsune remain the new default. Preserve historical MK231 example descriptions and story chronology verbatim, adding a clearly labeled note pointing to the new optional AERA denizens if necessary. **Do not** rewrite `examples/MK231` character arcs, Black Phoenix Egg, story progression, first Binding, Black prophecy trigger, or historical source quotations.
8. Do not modify L0 mathematics, L1 six domains, the eight literary prophecy manuscripts, chat constitutions, source PDFs, or external repositories. Keep the White superposition distinction intact. Do not force all authors to use inhabited realms.
9. The author's approved art may contain rejected/illustrative elements: the Vaelith sheet's color-variation swatches are NOT accepted biological variants; Sprite sheet's green-glowing shadow dragons/trees are NOT the correct transformed appearance; the Black Crystal scale is NOT locked. Markdown definitions are authoritative over incidental image text.
10. Existing naming `Vaelith` is exact; do not change to `Vaelithe`. Preserve `maege`/`maegi` and other established lexicon.

## Verification and publication
11. Validate that the exact nine payload files exist in tracked locations and all three images match payload SHA-256. Ensure no unintended tracked ZIPs or `_inbox` contents.
12. Check current AERA summaries correctly state: Red Dragon, Orange Vaelith, Yellow Primordial (Inorganic/Organic/Process), Green Sprite, Blue Leviathan, Violet Unicorn; optional realm denizens, NOT new energy basins.
13. Check Green Sprite collective transformations are genuine functioning biological forms without mandatory shadow glow; normal Sprite is a dark-gray Green-leaking bounded recursion; Black Sprite crystal is a separate exceptional artifact.
14. Check proposed MK231 Black Sprite first Binding is clearly **not yet enacted**. Verify prophecies and historical MK231 examples are unmodified.
15. Run `git diff --check`, inspect `git diff --stat` and substantive changes. Stage only intended files; commit `docs(aera): establish Vaelith and Sprite native denizens` and push to `origin main` normally. If branch protection blocks push, prepare a PR and report.
16. Report remote commit SHA, list of modified/new files, verification results, and open MK231 migration decisions. Never claim success without remote confirmation.
