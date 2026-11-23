#!/usr/bin/env python3
"""Safe, narrow AERA/MK163 native-race capability update. Python stdlib only."""
from pathlib import Path
import argparse

NOTE = '''# Chromatic native Transduction assignments — author decision 2026-11-23

**Scope:** AERA optional inhabited-realm realization / MK163 six chromatic native populations. **Humans excluded.** This is a race-level allocation of native capabilities, not a revision to the universal L1 operation categories, the six L0 chromatic basins, or the seven prophecies.

| Realm | Native race | Established primary structural specialization | Native capability allocation after author revision |
| --- | --- | --- | --- |
| Red | Dragons | Chirality | **Elemental Transduction**, **Dimensional Geometry** (including CSR flight), **Chirality** |
| Orange | Vaelith | Topology | Existing persistent topology, coherence/decoherence, regeneration and restorative focus **unchanged** |
| Yellow | Primordials | Persistence | **Resonance**, moved out of the Dragon native list |
| Green | Sprites | Resolution | Existing admissible-potential realization and collective recursion **unchanged** |
| Blue | Leviathans | Bandwidth | **Genesis Expression**, moved out of the Dragon native list |
| Violet | Unicorns | Genesis Field | **Genesis Field Topology**, moved out of the Dragon native list |

## Interpretive boundaries

- Dragons now have **three**, not six, listed native capabilities. Do not describe Genesis Field Topology, Genesis Expression or Resonance as Dragon-native capabilities under this allocation. Individual ability and mastery remain limited by skill and energy; the allocation does not make every Dragon master all three.
- The Primordials' Resonance allocation does **not** erase their Persistence specialization. Likewise Leviathan Bandwidth and Unicorn Genesis Field remain primary structural emphases.
- Vaelith and Sprite mechanisms and established healing/restoration descriptions are retained without alteration.
- The universal L1 operational taxonomy remains available across the framework; this document specifies native racial allocation for the selected inhabited-realm realization, **not** an absolute metaphysical prohibition on other forms of Transduction.
- The prophecy crosswalk remains unchanged. Leviathan association with III Borrowed Hours is weak/interpretive and **does not establish time manipulation**.
- Exact spells, quantitative capacities and additional racial magical repertoires remain OPEN unless established elsewhere.

## Provenance

Author's explicit 2026-11-23 decision: remove Genesis Field Topology, Genesis Expression and Resonance from Dragons; move them to Unicorns, Leviathans and Primordials respectively. Retain Dragon Elemental Transduction, Dimensional Geometry and Chirality.

Related sources: `L2/BIOLOGY/00_READ_FIRST.md`, `L1/OPERATIONS.md`, `L2/BIOLOGY/01_VAELITH.md`, `L2/BIOLOGY/02_SPRITES.md`, `L2/BIOLOGY/07_VAELITH_PROPHECY_CROSSWALK.md`. The source documents' older descriptions are preserved where historical; this newer explicit decision governs only its stated scope.
'''

def replace_once(path, old, new):
    s=path.read_text(encoding='utf-8')
    if s.count(old)!=1:
        raise RuntimeError(f'Expected unique old text not found in {path}: {s.count(old)} matches; no write')
    path.write_text(s.replace(old,new),encoding='utf-8')
    print('UPDATED',path)

def update_aera(root):
    readme=root/'L2/BIOLOGY/00_READ_FIRST.md'
    old='| Red | Dragons | Retained; large, physically powerful, flight-capable, six distinct operational specializations across population; each dragon has one native specialization per MK231 authority, not all six per individual. Further physical redesign pending. |'
    new='| Red | Dragons | Native capabilities: **Elemental Transduction, Dimensional Geometry (including CSR flight), Chirality**. Three Dragon-native capabilities after the 2026-11-23 author revision; finite energy and skill constrain individuals. Further physical redesign pending. |'
    replace_once(readme,old,new)
    marker='## Reproductive framework'
    insertion='**Current six-race native capability assignments (2026-11-23):** see [Chromatic native Transduction assignments](08_NATIVE_TRANSDUCTION_ASSIGNMENTS.md). Dragons retain three native capabilities; Resonance is assigned to Primordials, Genesis Expression to Leviathans, and Genesis Field Topology to Unicorns. These are race-level assignments, not edits to the universal L1 taxonomy.\n\n'
    replace_once(readme,marker,insertion+marker)
    note=root/'L2/BIOLOGY/08_NATIVE_TRANSDUCTION_ASSIGNMENTS.md'
    if note.exists():
        raise RuntimeError(f'{note} already exists; inspect and reconcile manually')
    note.write_text(NOTE,encoding='utf-8')
    print('CREATED',note)

def update_mk163(root):
    path=root/'WORLD_CLOCK/L1_FANTASY/OPERATIONAL_DOMAINS.md'
    old='For MK163 the six **Dragon-associated capabilities** are Elemental Transduction (ordinary elemental fire), Dimensional Geometry (including CSR flight), Genesis Field Topology (Architect-like organization), Genesis Expression (raw beams/orbs), Resonance (biological reinforcement), and Chirality (admissibility). Finite energy and skill remain limiting.'
    new='For MK163 the **three Dragon-native capabilities** are **Elemental Transduction** (ordinary elemental fire), **Dimensional Geometry** (including CSR flight), and **Chirality** (orientation/admissibility). Finite energy and skill remain limiting. **Genesis Field Topology**, **Genesis Expression**, and **Resonance** are removed from the Dragon-native allocation and assigned to Unicorns, Leviathans, and Primordials respectively.'
    replace_once(path,old,new)
    marker='Source and decisions: [Book Red reconciliation]'
    insert='''## Chromatic native capability redistribution (author decision · 2026-11-23)

| Realm | Race | Primary specialization (unchanged) | Native capabilities assigned in this revision |
| --- | --- | --- | --- |
| Red | Dragons | Chirality | Elemental Transduction; Dimensional Geometry; Chirality |
| Orange | Vaelith | Topology | Existing coherence/topological restoration unchanged |
| Yellow | Primordials | Persistence | Resonance |
| Green | Sprites | Resolution | Existing Resolution capabilities unchanged |
| Blue | Leviathans | Bandwidth | Genesis Expression |
| Violet | Unicorns | Genesis Field | Genesis Field Topology |

This updates racial native capability allocation only. The inherited six universal operational categories below are preserved for provenance and remain valid framework-wide; they are **not** the Dragon-native repertoire. Prophecy correspondences, the upstream chain, and the existing Vaelith/Sprite mechanisms remain unchanged. No new specific spells or temporal powers are implied.

'''
    replace_once(path,marker,insert+marker)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--aera',type=Path)
    p.add_argument('--mk163',type=Path)
    args=p.parse_args()
    if not (args.aera or args.mk163): p.error('Specify --aera and/or --mk163')
    # Preflight: ensure required paths exist before touching any files.
    if args.aera and not (args.aera/'L2/BIOLOGY/00_READ_FIRST.md').is_file(): p.error('AERA path incorrect')
    if args.mk163 and not (args.mk163/'WORLD_CLOCK/L1_FANTASY/OPERATIONAL_DOMAINS.md').is_file(): p.error('MK163 path incorrect')
    if args.aera: update_aera(args.aera)
    if args.mk163: update_mk163(args.mk163)
    print('Done. Review git diffs and commit/push explicitly.')
