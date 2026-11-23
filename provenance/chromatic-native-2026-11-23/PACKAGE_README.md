# AERA / MK163 — Six Chromatic Native Capability Reassignment

Author decision: 2026-11-23. Scope: six chromatic native races only; humanity excluded.

| Realm | Race | Established primary specialization | Updated native capabilities |
|---|---|---|---|
| Red | Dragons | Chirality | Elemental Transduction; Dimensional Geometry (CSR flight); Chirality |
| Orange | Vaelith | Topology | Existing coherence, topology, regeneration and healing retained; no change |
| Yellow | Primordials | Persistence | Resonance reassigned from Dragon capability list |
| Green | Sprites | Resolution | Existing Resolution/possibility realization retained; no change |
| Blue | Leviathans | Bandwidth | Genesis Expression reassigned from Dragon capability list |
| Violet | Unicorns | Genesis Field | Genesis Field Topology reassigned from Dragon capability list |

This updates *racial native capabilities* only, not the universal six operational Transduction categories, chromatic basins, seven prophecies, or upstream chain. Do not infer temporal manipulation for Leviathans from Borrowed Hours. Do not assign unapproved spells or make each Dragon master all three.

## Applying with Codex

Unpack this ZIP into a temporary directory. With AERA and MK163 repositories checked out, run:

`python apply_update.py --aera /path/to/AERA --mk163 /path/to/MK163`

The script checks expected existing text before editing and fails safely on drift. Review `git diff` in each repo, commit and push separately. If you only want to update AERA first, run `python apply_update.py --aera /path/to/AERA`.

The AERA update adds `L2/BIOLOGY/08_NATIVE_TRANSDUCTION_ASSIGNMENTS.md` and replaces outdated six-capability wording in `L2/BIOLOGY/00_READ_FIRST.md`. The MK163 update replaces the active six-Dragon capability statement and adds a canonical assignment table; historical inherited passages remain intact.
