# MQR 5.4 — MQR44 R17: PDB provenance collision in the joint-refinement comparison

2026-11-21 KST. **Status:** official repository metadata cross-check, NOT source-coordinate download or new refinement computation. This extends [R16 five-system primary-paper reconstruction](mqr_54_chat44_16_primary_refmac5_five_protein_success_and_failure.md).

## Concrete two-entry inspection

The Rinaldelli et al. (2014) *Acta Crystallogr D* Table 1 names **3NHE** as the crystal source for the 'ubiquitin' refinement. The authoritative [RCSB PDB entry for 3NHE](https://www.rcsb.org/structure/3NHE) explicitly titles it **'High Resolution Structure (1.26A) of USP2a in Complex with Ubiquitin'**. The deposited structure is not a free purified ubiquitin-only crystal, and it is crucial not to equate the file's entire complex with isolated ubiquitin coordinates or claim exact sample equivalence to independent solution-NMR ubiquitin records. The study may use/extract a **particular ubiquitin chain** for refinement; the actual model preparation, chain selection, diffraction data extraction and residue mapping must be checked before any structure-to-structure RMSD analysis. The word 'ubiquitin' in the authors' Table 1 is a scientific target label, **not a complete machine-readable specimen identity**.

Likewise the [official RCSB entry 1EXR](https://www.rcsb.org/structure/1EXR) is **'The 1.0 Angstrom Crystal Structure of Ca2+ Bound Calmodulin'**. The deposited protein is crystallized calcium-bound calmodulin (Paramecium tetraurelia). Comparing with solution-state NMR calmodulin conditions is not automatically 'same specimen in two methods'; salt, target peptide, calcium loading, crystal packing, dynamics and organism/specimen distinctions must be acknowledged. The [official RCSB experimental metadata](https://www2.rcsb.org/experimental/1EXR) includes deposited and revalidated R-free values that need not numerically equal Table 1's **post-REFMAC5 recalculation**. Directly comparing deposited R-free 0.163 with Rinaldelli's in-paper recalculated 0.142/0.147 without matching reflection sets and refinement protocol would be a false exact-repeat audit.

## Critical scientific implication

**Matching a PDB accession is not a guarantee of matching experimental estimand.** A raw crystallographic coordinate file, deposited structure factors and a crystal model refined again with different restraints are separate artifacts. Likewise an NMR restraint file has its own alignment/paramagnetic tag, ensemble, conformational timescales, reference conditions and selection. To justify a strong MQR cross-field success claim one must track:
1. which exact molecule/chain and preparation was evaluated;
2. which diffraction intensities, R-free flags and re-refinement protocol were used;
3. which original NMR restraints and calibrations are held and their physical sample/source;
4. the sequence/region/residue mapping between the two models;
5. which statements were **authors' interpretation** versus our own arithmetic/checks.

This is precisely why MQR R11–R15's requirement **target-preservation + receipt/custody + cross-regime transfer** is not redundant philosophy. The 2014 case supplies a real published observation that can **both** accommodate joint refinement **and** reveal differences, but no direct raw-data reenactment was executed in this chat.

## Raw acquisition attempt and exact status

A public repository mmCIF endpoint for 1EXR was attempted through the container's download action, but the URL had not been previously accepted in the browsing context; after a browsing open attempt, the endpoint still reported inaccessible. **No bytes downloaded**, no fallback authenticated bypass, no file invented and no SHA asserted. That block affects **raw-coordinate acquisition**, not primary-paper full-text reading or the published PDB metadata. Continue to record raw structure and NMR restraint files as unverified. No official 17-missing-group status change.

New domain lessons include biological specimen identity, model/data ancestry and correction against overinterpretation. **Originality HOLD, external direct raw validation HOLD, MQR 5.4 OPEN.**
