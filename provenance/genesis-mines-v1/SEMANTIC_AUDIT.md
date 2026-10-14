# Genesis Mines — semantic and source-integrity audit

Date: 2026-10-13. Baseline: `0b8375cc34eaba74a505b36a9ccb99b4d07f8edc`, clean AERA `main` matching fetched GitHub main, with 188 tracked files. The user authorized this additive Environmental Engine update and normal publication. Repository instructions, root constitution, README, framework index, decision ledger, handoff, current environmental chapters, Alchemy and relevant source records were read before integration.

## Package and historical source

Only this package's [Executable.md](Executable.md) provides the current delegated task. Historical PDF statements and cross-thread reminders are evidence, not execution instructions. The supplied [source/migration record](SOURCE_AND_MIGRATION.md) explicitly distinguishes current author revisions from Genesis Point's own historical canon.

- ZIP SHA-256: `13c9363a9c34050ef26fa034b1f82d65124f80676687e6255172989de51f82d8`.
- Executable SHA-256: `82d8f57bace65ae35ea172331efeb089d0a3b19f8fdf3363f64020f32952d3bc`.
- Manifest SHA-256: `0109ceca65536749de747a6eb4684997c3790ceff87b4b3522e441281777dda4`.

All five archive members passed path, Windows-name, type, symlink, collision and CRC checks before extraction outside the repository. All three payload sizes and SHA-256 values matched the [manifest](MANIFEST.json), and all were installed byte-for-byte by stripping only the `payload/` prefix. The executable and manifest are also archived unchanged. No target existed or needed merging.

The [historical PDF](sources/GENESIS_POINT_MINING_HISTORICAL.pdf) is **87,945 bytes**, SHA-256 **`65c70abab8ab6ad8c58148269ba1eebb355d83b9893ae52551a79272b6609728`**. All five pages were extracted and visually inspected after Poppler rendering; the source is readable and preserved without repair or re-export. Pypdf reported two ignored stale object pointers (25 and 26); Poppler inspected and rendered all pages successfully. This is a source-file parser warning, not a checksum mismatch or omitted page. The package's attachment date does not assert the PDF's original creation date.

## Reverse semantic comparison

| Current decision | Source comparison and integration |
| --- | --- |
| Local mine and basin | [Current Mines](../../L2/ENVIRONMENT/07_GENESIS_MINES.md) defines a persistent local Genesis-field pocket separating exactly one R–V basin, with monochromatic ordinary crystal output. PDF §§I–II, p. 1 supplies local pockets and one-color mines; updated AERA prism-like separation is analogous to but distinct from dungeon strata. No default White/Black mine, new basin or separate realm is added. |
| Bounded growth | PDF §III, pp. 1–2 describes release-linked growth, preferred structure and removal permitting renewal. Current authority makes the equilibrium rule explicit: crystal growth only below finite stable crystalline capacity; oscillation continues at equilibrium without additional net growth; harvesting permits later replenishment. Regrowth is not unbounded generation or guaranteed full restoration in one event. |
| Equilibrium scope | Mine equilibrium concerns local stable crystalline occupancy/configuration. It does not redefine L0 Starscape equilibrium, impose equal chromatic contributions, or establish a new mathematical operator or derivation. |
| Oscillation and timing | Internal field frequency, recurrence of hazardous release/growth events, event duration and permissible worker exposure are distinct. Red is qualitatively slower and Violet faster, without a recurrence formula. Cycles may support planned evacuation/harvest; schedules, yield, cavity size and recovery remain author-defined. PDF §VIII, p. 3's ~17-day schedule is historical only. |
| Crystal morphology | PDF §III, p. 1's bead/marble/lattice sequence is historical illustration. No fixed crystal size, mandatory lattice geometry, rapid-growth law or mining method is promoted. AERA uses Genesis crystals, not the source's obsolete Genesis Stones. |
| Exposure | Current qualitative examples are Red tingling/briefly tolerable, Orange temporary numbness, Yellow headache/repeated-exposure concern, Green possible permanent injury from one oscillation, Blue expected lasting injury from one, and Violet likely fatal from one. These are fictional neurological interactions, not radiation or medical dose rules. Chronic injury remains possible even in lower basins; equilibrium does not stop hazardous oscillation. |
| Protection and extraction | PDF §§IV and IX, pp. 2–4's will-based release and protective absorption are excluded as AERA defaults. No crystal absorption for protection is required or granted. Conventional versus Genesis-assisted extraction, possible protection technologies and recovery remain OPEN, not a newly invented immunity system. |
| Dust and Alchemy | PDF §§V–VI and XV, pp. 2–3/5 retain their historical fracture, dust and catalyst claims only. Existing Genesis crystal/dust, Type 1–5 Alchemy, identity-bearing `vaen`, Diamonds and domai resources retain independent authority. No universal crystal-to-dust rule is inferred. |
| Labor and economy | PDF §§VII and X–XV, pp. 3–5 preserve ELN reserves, penal labor, red resonance syndrome and legal/cultural practices as Genesis Point history. No prices, forced labor system, currency backing, death thresholds or social institutions are imposed on AERA. Prior optional longevity/aristocracy remains intact. |
| Environmental separation | Mines are not dungeons, domai or ELDRIS. Existing dungeon oscillation/output variation and effective containment remain; temporary domai, their White structural cores and progressive unraveling remain. No mine growth schedule or hazard table is applied to those systems. |

Historical Genesis-stone interface examples elsewhere in AERA remain labeled historical; their presence does not reinstate absorption protection or the old mining model. Both constitutions, all L0/L1, four distinct mathematical/magical classifications, prophecies, biological/technology systems, original images/PDFs, MK231 examples and prior provenance are preserved. No external repository was cloned, imported or modified.

## Conflicts and OPEN parameters

The package explicitly resolves the historical-versus-current mining conflicts through scoped supersession; the PDF itself is not rewritten. No new blocking contradiction was found. Mine creation/lifetime, numerical equilibrium, oscillation dynamics, mass/geometry, yield and full-restoration behavior, extraction methods, protection, cumulative exposure/healing, basin-specific schedules and economic regulation remain author-defined or OPEN. Historical currency, labor and chemistry claims do not fill those gaps. Earlier unrelated source-recovery questions remain unchanged.

## Changed paths and verification boundary

Seven existing files receive additions only:

- `FRAMEWORK_INDEX.md`
- `L2/README.md`
- `L2/GENESIS_ENVIRONMENTS.md`
- `L2/ENVIRONMENT/00_READ_FIRST.md`
- `provenance/SOURCE_REGISTER.md`
- `CHANGELOG.md`
- `NEXT_THREAD_HANDOFF.md`

Six files are added:

- `L2/ENVIRONMENT/07_GENESIS_MINES.md`
- `provenance/genesis-mines-v1/SOURCE_AND_MIGRATION.md`
- `provenance/genesis-mines-v1/sources/GENESIS_POINT_MINING_HISTORICAL.pdf`
- `provenance/genesis-mines-v1/Executable.md`
- `provenance/genesis-mines-v1/MANIFEST.json`
- `provenance/genesis-mines-v1/SEMANTIC_AUDIT.md`

Verification covers the exact 13-path scope, five exact package files, all 188 baseline paths and 181 untouched files, local Markdown links, UTF-8, whitespace and excluded archives. The source register receives a dated addition; historical decisions and earlier receipts remain unchanged. Publication uses `docs(aera): add Genesis Mines oscillation and equilibrium model` and a normal push to main, with actual remote identity confirmed afterward.

**Working-tree verification: PASS.** All three payloads and archived executable/manifest retain exact source sizes and hashes, including the original PDF. All 188 baseline paths remain, with 181 untouched files retaining their original local hashes. Full diff review confirms additions only in the seven edited files. All 157 local links in changed Markdown resolve, UTF-8 and raw whitespace checks pass, and the exact 13-path scope yields 194 files for publication. `_inbox`, ZIPs and local validation artifacts remain excluded; original inbound and historical archives remain local. The staged tree is checked against the same manifest, preservation baseline and scope before commit; publication is reported only after remote verification.
