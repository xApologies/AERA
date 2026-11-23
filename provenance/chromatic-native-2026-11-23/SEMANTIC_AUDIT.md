# Chromatic native capability reassignment — 2026-11-23

Baseline: `42437950ad2aa72ad885ff1a9129226da23d9286`, clean AERA `main` equal to fetched GitHub main; 201 tracked files. The user's request updates AERA only. Repository instructions, root constitution, README, framework index, decision ledger, relevant biology/operation files and the November 8 reconciliation were read before changes. The November vaen/Red clarification is retained.

## Package and execution boundary

The ZIP supplies [a README](PACKAGE_README.md), [Python source](apply_update.py) and compiled cache, with no `Executable.md` or checksum manifest. All five archive entries passed path/type/symlink/collision checks, ZIP CRC, and exact extraction verification inside ignored `_inbox`. Archive SHA-256: `e39d5f883e1809c7030cc31c6868fc62ae0ab70475c56a10347c8501bc3f37bc` (8,760 bytes). The [integrity record](INTEGRITY.json) contains locally calculated member hashes, not publisher-supplied checksums or an independent authenticity claim.

The source script was inspected in full. Its AERA branch changes only the biology index and creates the assignment note. Before execution, all expected old-text/marker occurrences were checked for uniqueness and the destination's absence was confirmed; this avoids the script's partial-write risk if a later replacement fails. It was run with `--aera` only. MK163 was not opened, cloned or modified. The bundled `.pyc` was neither executed nor published. Original ZIP, extracted package and validation artifacts remain local and ignored.

The generated [assignment note](../../L2/BIOLOGY/08_NATIVE_TRANSDUCTION_ASSIGNMENTS.md) matches the script's complete `NOTE` literal byte-for-byte in UTF-8/LF: 2,933 bytes, SHA-256 `1d474dede22c569ae33120c72da5c9a3ac3dd55ca9626185da38de17d5fe754f`. The script's initial index output was checked against the two exact prescribed substitutions; generated files use repository LF endings. The supplied README and Python source are archived unchanged.

## Reverse semantic comparison

| Scope | Result |
| --- | --- |
| Dragon allocation | Three native capabilities: Elemental Transduction, Dimensional Geometry including CSR flight, and Chirality. Genesis Field Topology, Genesis Expression and Resonance leave the current Dragon-native list. Individual energy and skill remain limiting; the population allocation does not grant mastery of all three to every Dragon. |
| Receiving populations | Primordials receive Resonance while retaining Persistence; Leviathans receive Genesis Expression while retaining Bandwidth; Unicorns receive Genesis Field Topology while retaining Genesis Field as primary structural emphasis. The update allocates capabilities without equating them to those structural roles. |
| Unchanged populations | Vaelith topology/coherence/decoherence, regeneration and restoration remain. Sprite Resolution/admissible-potential realization and collective recursion remain. Their detailed biology documents are untouched. Humanity is outside this decision; no human access, potion, Awakening, Afflicted or longevity rule changes. |
| Framework boundary | Optional inhabited-realm racial allocation does not replace the six universal operational categories, six energy basins, Seven+Black prophecies or six-stage lifecycle. Elemental Transduction is not installed as a seventh universal operation. Other admissible Transduction remains available under existing framework rules. |
| Structural and prophetic authority | Red Chirality, Orange Topology, Yellow Persistence, Green Resolution, Blue Bandwidth and Violet Genesis Field emphases are retained. The existing prophecy crosswalk is unchanged; Leviathan/Borrowed Hours remains weak/interpretive and grants no temporal manipulation. No upstream chain or L0 derivation is revised. |
| Drift reconciliation | The updater replaces the older Red table row but misses the November 8 paragraph asserting six population specializations. That live paragraph is also reconciled to the new three-capability allocation. Its Elemental Transduction correction, rejection of Red-primary Coherence–Decoherence, finite costs and separate Red–Chirality explanation are preserved. The Red row also retains the existing large, physically powerful, flight-capable description omitted by the supplied replacement; the package changes capabilities only, not physical morphology. The earlier source records and MK231 examples retain historical authority. |

No new semantic blocker was found. Exact spells, numerical capacities, additional racial repertoires and individual mastery remain OPEN or governed by existing sources. This update does not create absolute metaphysical prohibitions or resolve unrelated story and mathematical questions.

## Changed files and preservation

Five existing files change: `L2/BIOLOGY/00_READ_FIRST.md`, `FRAMEWORK_INDEX.md`, `L2/README.md`, `CHANGELOG.md` and `NEXT_THREAD_HANDOFF.md`. The biology index contains the prescribed capability/cross-reference edits, retained physical descriptors and one additional scoped paragraph correction. The other four files receive additions only.

Five files are added: `L2/BIOLOGY/08_NATIVE_TRANSDUCTION_ASSIGNMENTS.md` and this directory's `PACKAGE_README.md`, `apply_update.py`, `INTEGRITY.json` and `SEMANTIC_AUDIT.md`.

All 201 baseline paths remain; 196 untouched files are protected by local hashes and Git blob identity. This includes both constitutions, all L0/L1, concepts/prophecies, original images/PDFs, prior provenance, vaen/Alchemy, Mines, technology, humans, Vaelith/Sprites and historical MK231 examples. Verification covers the exact ten-path change set, source/note hashes, local Markdown links, whitespace and exclusion of `_inbox`, ZIPs and cache files. Publication uses a normal push to AERA `main`; the actual remote commit is checked afterward.

**Working-tree verification: PASS.** The complete assignment note, both archived source files and generated integrity record match their recorded bytes/hashes; all 196 untouched files retain their local hashes. All 146 local links in changed Markdown resolve, whitespace checks pass and no ZIP/cache/inbox path is tracked. The ten-path scope yields 206 files for publication. The final staged contents are verified against the same baseline and source bytes before commit, with remote equality checked after normal push.
