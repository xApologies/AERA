# AERA upstream reconciliation 001 — integration audit

Date: 2026-11-25. Target: `xApologies/AERA`, `main`. Baseline local HEAD, fetched `origin/main` and remote branch all matched `a77d050141b2db3eaa8f3dc7f520306400096748`; the baseline was clean with 206 tracked files and matches the package's AERA pin.

## Sources and publication authority

The author supplied `AERA_UPSTREAM_RECONCILIATION_001_CLEAN.zip` and requested its AERA integration. Its [work order](package/EXECUTABLE.md) explicitly targets AERA; the earlier MK163-only Genesis Systems author package remains unapplied. The [original audit ledger](package/AUDIT_LEDGER.md) and [package README](package/README.md) are retained exactly. Historical instructions in these files do not replace the user's scope or current constitutions.

- ZIP SHA-256: `bacb3a3e7455bb80c65f527bcb599109c89869f66822ffd291706422aa6ad2c5`.
- [Original manifest](package/MANIFEST.json): nine declared files, all SHA-256 checks passed. Extraction checked paths, case collisions, special-file types, sizes and ZIP CRC before writing to ignored local staging.
- Catalogue: author-uploaded **Genesis Cards and Bindings.csv**, renamed to [SHAPINGS_MASTER.csv](../../L1/SHAPINGS/SHAPINGS_MASTER.csv) without changing any bytes. SHA-256 `4e7d13925b024f679aca369a08a8ca2b064b4794cde3654431e28bee531edab3`; 1,943,317 bytes. No older catalogue or second catalogue copy is published. Its CRLF line endings are preserved by a path-specific `-text` attribute.
- MK163 source pin: `dc4ef8440e18f39f89bc0a15dd1d26942c1258ec`. Retrieved only the two specified AERA-targeted workshop documents, without cloning or changing MK163. Their source text explicitly identifies the 2026-11-17 author workshop and AERA scope.
- MK727 lineage/ownership inspection pin: `8e5f5fead9621c81cf2064190cc732dbd399f7f1`. Inspected repository ownership metadata, tree, README and INHERITANCE. The source is under the same `xApologies` owner; INHERITANCE identifies the 1,016 Binding/229 Summon MK157 lineage. The supplied master is newer author-uploaded data, not asserted to match the older MK727 CSV. Older CSVs were not retrieved or imported.

No incompatible license was found in the inspected MK727 tree or source notices. Publication proceeds under the author's explicit supplied-package instruction, not under an assumed public-repository license. AERA's [license-pending record](../../LICENSE_PENDING.md) is unchanged; no license or unrestricted third-party reuse grant is created. This is a bounded ownership/source inspection, not an exhaustive rights audit of every historical reference.

The [integrity map](INTEGRITY.json) records package-to-publication paths, SHA-256 values, byte counts, source URLs and Git blob IDs. All five payload files are installed unchanged. The original package validator is archived at [package/validate.py](package/validate.py); it was executed from the complete local extracted package. Its original relative `payload/` paths intentionally describe that package, while INTEGRITY.json maps them to repository destinations.

### Exact recovered source bytes

| Source | Git blob | SHA-256 | Bytes |
|---|---|---|---:|
| [Binding/Card supply and CSR](https://github.com/xApologies/MK163/blob/dc4ef8440e18f39f89bc0a15dd1d26942c1258ec/PROVENANCE/WORKSHOP/VIOLET_CUMULATIVE_007/AERA/L1/INTERFACES/05_BINDING_CARD_BASIN_SUPPLY_AND_CSR.md) | `632e741fb027b4b94fd06e3a574ddf1fce939624` | `f70e8354caa938fbf12e0f26f4568bb97ba89904d3028e4ae555f50cc87e2ed2` | 5,215 |
| [CSR and dimensional expedition equipment](https://github.com/xApologies/MK163/blob/dc4ef8440e18f39f89bc0a15dd1d26942c1258ec/PROVENANCE/WORKSHOP/VIOLET_CUMULATIVE_007/AERA/L2/TECHNOLOGY/CSR_AND_DIMENSIONAL_EXPEDITION_EQUIPMENT.md) | `ea1173d9c152b2c818e0a2b58d08c9978924a82c` | `f2c14522d2547ff462208ee892632ffad292c6cbf56a7a77d3f63a7a575b2a9c` | 1,881 |

Both retrieved byte streams were checked against their Git blob hashes and archived unchanged under `sources/`. Current canonical derivatives below incorporate only compatible missing deltas and explicitly scope local examples.

## Reverse semantic comparison

| Ledger item | Destination and coverage | Disposition |
|---|---|---|
| 001 Weapons | [Enhanced weapons](../../L2/TECHNOLOGY/GENESIS_ENHANCED_WEAPONS.md): independent handling inertia/gravitational load, impact recoupling, optional amplification, recoil and combined-system momentum/energy accounting. Maul arithmetic checked: 136/1,360 kg·m/s, 680/6,800 J, differences 1,224 kg·m/s and 6,120 J. | Payload exact; conceptual architecture selected, field/Shield topology remains a hypothesis, quantitative engineering OPEN. |
| 002 Augmentation | [Bodily augmentation](../../L1/NEUROGENESIS/06_BODILY_AUGMENTATION.md): local body anchoring, compatible Resonance/Coherence, temporary muscle/strength/support effects, dissipation and return to native state, duration distinct from fatigue. | Payload exact; profession link reconciled; no fixed growth/duration law, invulnerability or continuous-per-movement channeling requirement. |
| 003 Catalogue | [Catalogue introduction](../../L1/SHAPINGS/README.md) and [authority/open records](../../L1/SHAPINGS/AUTHORITY_AND_OPEN.md). | Exact bytes/IDs/schema preserved; source scope retained. Two contradictory OPEN-status records flagged below; no invented entries or blanket effect approval. |
| 004 Collapse activation | [White Genesis Collapse](../../L1/NEUROGENESIS/05_WHITE_GENESIS_COLLAPSE.md): trained White Awakened, all six closed rings, widening unnecessary, coherent equal output at Violet reference with unequal extraction effort, singular recursion, black containment silhouette and White interior light. | Payload exact; distinct from automatic Awakening, Afflicted biology, Black ontology, operational domains and chromatic armor ranks. |
| 004 Collapse damage/equipment | Same document: localized weakening/breach; normalized reinforcement; slightly extended envelope, incorporated equipment rematerialization, selective exclusion with skill; incorporated armor adds no independent robustness. | No invulnerability, unlimited storage or assumed healing; breach/injury transfer, boundary and enchantment behavior OPEN. |
| 004 Collapse endurance/concurrency | Same document and linked training/fatigue/concurrency records: selected ~17-hour ordinary-sustainment benchmark, illustrative ~11–13-hour combat example, cumulative basin-specific fatigue and exhaustion exit. Native/compatible Binding work possible; active operational Cards incompatible. | No variable recursion depth, exact fatigue coefficients, derived endurance law or forced Card cancellation. Unexhausted basins remain accessible. |
| 005 CSR | [Binding supply and CSR](../../L1/INTERFACES/05_BINDING_CARD_BASIN_SUPPLY_AND_CSR.md): O/Y/B/V shared requirements, access-Binding accounting OPEN, finite White emergency supply, conditional same-basin concurrency and no Card inventory cap. | Existing PSSP, ~60% illustrative bandwidth, global Card exclusivity and no `aen` Card boost preserved. Old O/Y source assignment superseded. Source economics remain scoped. |
| 005 Flight/logistics | Same document: illustrative ordinary-speed 1–2 / 3–5 / 5–8-hour bands, speed/load/maneuver fatigue, rest and exposure to eldris after exhausting flight. | No exact formulas or guaranteed endurance; Binding bandwidth and Card basin locks remain distinct. |
| 006 Expedition | [CSR and dimensional equipment](../../L2/TECHNOLOGY/CSR_AND_DIMENSIONAL_EXPEDITION_EQUIPMENT.md): relay roles, equipment/crossings, alternate bracelet, optional backup ring, endpoint deployment and logistical OPENs. | Ring master/reconciliation unchanged. Greater bracelet capacity, source no-hauled-boat choice, possessions and costs remain setting examples; no 2–3× ratio or fixed 300-mile deployment range adopted. |

## Catalogue verification and outstanding decisions

Verified 1,245 unique `mk727_card_id` values and 1,245 unique source IDs, 65 columns, valid row widths and preserved empty fields. Record distribution: 1,016 INDUSTRIAL_BINDING, 229 SUMMON. Required-basin cardinalities: one single-basin, 352 two-basin, 799 three-basin and 93 four-basin records. Every set is nonempty, contains distinct R/O/Y/G/B/V names, and matches its supplied basin-draw profile where present. CSR DG-0031 is exactly Orange/Yellow/Blue/Violet. All structured recipe/legacy-override references resolve to matching IDs and names.

Preserved source statuses: 990 domain-normalized ALPHA candidates, 232 other ALPHA candidates, 15 LOCKED, six WORKING, two APPROVED CONCEPT with OPEN costs/rank expressions/basins. These are not a universal approval list. All 1,016 industrial records retain higher-rank Binding pricing as proposed; 229 Summon records retain OPEN Binding pricing.

**Affected promotion deferred:** GE-0598 and GE-0599 retain populated basin/pricing data despite explicitly OPEN source status. Their numerical/configuration fields need author reconciliation before being treated as settled AERA decisions. No row is edited to choose an answer. PE-001/002/003 preserve historical `illi_white_legacy_override` data without granting omitted prerequisites, changing ordinary recipes or importing story mechanics. The sole single-basin row, SE-0133, is a candidate Summon, not a new access Card. See the [authority notes](../../L1/SHAPINGS/AUTHORITY_AND_OPEN.md).

The audit covers structural completeness, source-status boundaries, structured cross-references and the mechanics affected by this package. Full engineering/admissibility adjudication of every candidate effect remains pending. Existing source-specific exceptions cannot override AERA interface constraints by inference.

## Deferred candidate backlog

The original [ledger](package/AUDIT_LEDGER.md) remains intact. Items 007 sigil manufacturing, 008 maege glass architecture, 009 denizen/realm biology, 010 domai geometry and 011 enhanced armor are not promoted. Their listed paths remain future comparison targets. No optional 3/5/7/11/13/17-mile domai radius profile, 1.7 interior factor or bracelet multiplier is installed. Further alchemy, cardsmithing, civic, civilization, ecology, economic, cultural and agriculture comparisons remain unperformed. City mapping is unapproved; L3/L4 remain source-owned. This is not exhaustive upstream semantic closure.

## Preservation and checks

The package validator passed all nine hashes, catalogue row/column/ID/type counts, basin distribution, CSR set and single-master checks. Exact source hashes and source-to-publication mappings passed. Original ZIPs remain local and unchanged; existing ignore rules cover `_inbox/` and `*.zip`.

Worktree verification passed: all 206 baseline files retained, all 186 files outside the intended modifications unchanged, 12 exact copied files matched, and 287 relative Markdown links in changed documents resolved. Both constitutions, L0, L3/L4, prophecies, existing biology/source assets and unrelated provenance are protected by baseline byte/blob comparisons. The intended change set is 20 modified plus 17 added paths, yielding 223 tracked files. No general repository test suite was found; the supplied validator and focused integrity/catalogue/link checks cover this documentation/data update.

The catalogue's path-specific whitespace setting recognizes its source CRLF endings while retaining checks for actual trailing spaces, blank lines at EOF and spaces before tabs. Its bytes remain unchanged. Staged/published verification compares the same inventory and exact hashes against Git blobs, including all untouched baseline blobs. Publication SHA is reported only after normal push and a live remote comparison; this report does not claim its own future commit identifier.

## Changed paths

### Modified

- `.gitattributes`
- `CHANGELOG.md`
- `FRAMEWORK_INDEX.md`
- `L1/FATIGUE_CONCEPT.md`
- `L1/INTERFACES/00_READ_FIRST.md`
- `L1/INTERFACES/02_BINDING_CIRCLES.md`
- `L1/INTERFACES/03_GENESIS_CARDS.md`
- `L1/INTERFACES/04_CONCURRENCY_AND_AUTHORITY.md`
- `L1/NEUROGENESIS/00_READ_FIRST.md`
- `L1/NEUROGENESIS/02_WHITE_AWAKENING_AND_AEN.md`
- `L1/NEUROGENESIS/03_AEN_TRAINING_AND_FATIGUE.md`
- `L1/README.md`
- `L2/CIVILIZATION.md`
- `L2/ENCHANTING/04_AUTHORITY_AND_OPEN.md`
- `L2/GENESIS_TECHNOLOGY.md`
- `L2/README.md`
- `NEXT_THREAD_HANDOFF.md`
- `README.md`
- `provenance/DECISION_LEDGER.md`
- `provenance/SOURCE_REGISTER.md`
### Added

- `L1/INTERFACES/05_BINDING_CARD_BASIN_SUPPLY_AND_CSR.md`
- `L1/NEUROGENESIS/05_WHITE_GENESIS_COLLAPSE.md`
- `L1/NEUROGENESIS/06_BODILY_AUGMENTATION.md`
- `L1/SHAPINGS/AUTHORITY_AND_OPEN.md`
- `L1/SHAPINGS/README.md`
- `L1/SHAPINGS/SHAPINGS_MASTER.csv`
- `L2/TECHNOLOGY/CSR_AND_DIMENSIONAL_EXPEDITION_EQUIPMENT.md`
- `L2/TECHNOLOGY/GENESIS_ENHANCED_WEAPONS.md`
- `provenance/upstream-reconciliation-001/INTEGRATION_REPORT.md`
- `provenance/upstream-reconciliation-001/INTEGRITY.json`
- `provenance/upstream-reconciliation-001/package/AUDIT_LEDGER.md`
- `provenance/upstream-reconciliation-001/package/EXECUTABLE.md`
- `provenance/upstream-reconciliation-001/package/MANIFEST.json`
- `provenance/upstream-reconciliation-001/package/README.md`
- `provenance/upstream-reconciliation-001/package/validate.py`
- `provenance/upstream-reconciliation-001/sources/05_BINDING_CARD_BASIN_SUPPLY_AND_CSR.md`
- `provenance/upstream-reconciliation-001/sources/CSR_AND_DIMENSIONAL_EXPEDITION_EQUIPMENT.md`
