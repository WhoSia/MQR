# MQR 5.4 · MQR44 R22 — Three parallel gates: source acquisition, real-world protein inference, Real-Lang experimental development

**Date: 2026-11-21 KST.** Research version 5.4 unchanged. The user required **simultaneously**: continued ambitious research, missing-source accountability and actual Real-Lang development (not abandon the language and not substitute engineering commits for world contact). This director note reconciles what was executed.

## 1. Real scientific evidence vs source location

- Rinaldelli et al. (2014) joint X-ray/NMR reported five different structural outcomes. Publication original is [PubMed](https://pubmed.ncbi.nlm.nih.gov/24699641/) / DOI [10.1107/S1399004713034160](https://doi.org/10.1107/S1399004713034160). Earlier R16 independently recomputed author Table 1 Q_RDC and R_free aggregates; **no independent raw refinement** of NMR restraint arrays or original R-free structure-factor split has been done.
- [RCSB File Download Services](https://www.rcsb.org/docs/programmatic-access/file-download-services) officially distinguishes mmCIF coordinates from structure factor downloads. Therefore simply obtaining deposited 1EXR (calmodulin) and 1IGD (GB3) coordinate files will NOT reproduce the 2014 joint refinement: require X-ray reflection factors and R-free flags, original solution NMR measured RDC/PCS, chain/residue mapping, conditions, weighting/geometry protocol.
- The official historical missing-source register has **17 heterogeneous groups**; Rinaldelli 2014 is additional targeted candidate, not a false 18th closure or general proof of absence. Direct Drive title search this turn did not find exact `Rinaldelli 2014`, `1EXR` or `1IGD` files. Search absence ≠ exhaustive nonexistence.

## 2. New genuine intake evidence

[00_INTAKE authenticated folder](https://drive.google.com/drive/folders/1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16) returned **one** PDF file id `18_dp4wTC7zCTkUfUnDwNuzH3Ui4yF_YD`, created timestamp 2026-11-21T13:59:46Z and size 2,646,521 bytes. Directly read full PDF extracted text: Arriagada, Prato & Munizaga (2025), *Incorporating the inertia effect into a route choice model using fare transaction data from a large-scale public transport network*, *Transportation Research Part A* 196, 104467, DOI [10.1016/j.tra.2025.104467](https://doi.org/10.1016/j.tra.2025.104467). The Santiago Metro line 6 2017 introduction is a real-world change to passengers' feasible action menu. **Authors state they lack permission to share individual fare data**. Consequently **paper HELD** and **original AFC/AVL per-passenger data not publicly supplied by paper** are distinct. It is useful as a cross-domain MQR R12 observational regime-change comparison, **not a published replication of our binary synthetic state model**. No move/import/delete. [Detailed R21 note](mqr_54_chat44_21_00_intake_new_transit_inertia_and_transport_gate.md); [canonical registry update](MQR_LIVE_MISSING_SOURCES_REGISTRY.md).

## 3. Actually implemented Real-Lang experimental features

The user requested not to abandon Real-Lang. We therefore read [existing Real-Language README](../language/real/README.md), [non-promoting Open Horizon Bridge](../language/real/experiments/OPEN-HORIZON-BRIDGE-V54.md), [canonical doctrine](../doctrine/CURRENT.md), [v0.25 inquiry-scaffold document](../language/real/V25-REFLEXIVE-ECOLOGY.md) **before** modifying surfaces. New code is deliberately scoped under `language/real/experiments/`, not falsely promoted to authoritative Rust packet grammar or a new release.

### Typed claim/receipt gate

[interfield_target_receipt_v54.py](../language/real/experiments/interfield_target_receipt_v54.py) defines typed claims and evidence receipts indexed by **target, specimen and regime**, explicitly requiring original-scope preservation, physical pairing, calibration and declared lineage. It rejects duplicate receipts, ill-typed flags and target substitutions; adverse evidence cannot be averaged away. Synthetic, published-summary, source-raw and claimed independent-replay source classes remain separately typed. Even two independently **named** lineages are not physically verified independent failures.

[General tests](../language/real/experiments/test_interfield_target_receipt_v54.py): **17** methods, including later fix for source-raw no-replay not being mislabeled `PUBLISHED_COMPATIBILITY_NOT_REPLAYED`. [Actual five-system publication tests](../language/real/experiments/test_interfield_published_refmac5_v54.py): **4** methods applying declared types to all five PDB entries and both Q_RDC/R_free source-summary targets; all remain **HOLD_PHYSICAL_PAIRING_UNVERIFIED** as an MQR independent replay claim. These are NOT assertions that the original experimental authors failed to pair their actual samples, only that our receipt set does not certify independent source pairing.

### Source-byte integrity gate

[frozen_byte_witness_v54.py](../language/real/experiments/frozen_byte_witness_v54.py) validates a **previously frozen, trusted** lowercase SHA-256 + exact byte count against a local file. [10 tests](../language/real/experiments/test_frozen_byte_witness_v54.py) cover matching bytes, mutation, truncation, append, missing file, invalid/uppercase digest, bool-as-size attack and empty file. The verifier's success status deliberately states `BYTES_MATCH_FROZEN_DIGEST_ONLY`. It does NOT prove specimen identity, laboratory independence or method-valid calibration. Merely computing the expected hash at check time from suspect bytes is insufficient.

[Experimental API, statuses and scientific boundary documentation](../language/real/experiments/INTERFIELD-TARGET-RECEIPT-V54.md).

### Execution receipt, deliberately scoped

The container could not resolve `raw.githubusercontent.com` via DNS; the source and tests were **manually reconstructed as matching local text**. Local Python `unittest` discovered **31 tests** and all passed, comprised of 17 general, 4 actual-published-table fixture, 10 byte-integrity. **A byte-for-byte equality check between GitHub blobs and the local reconstruction was not independently obtained.** This is not a successful whole-Real-Lang CI run, canonical Rust/Prolog concordance, P4 scientific claim, or Real-Lang release. Commit success must be separately checked by authenticated GitHub commit fetch.

## 4. Research-director decisions and next hard problem

**KEEP** Real-Lang experimental provenance/target gates and formal regression tests; **NOT PROMOTE** them as live authority on source data. The correct architecture is to translate validated external source manifests and explicitly typed targeted claims into a Rust/independent-reference adjudication only after there is real externally audited evidence and sufficient tests.

**KEEP** original MQR 5.4 scientific question: how different scientific practices can generate new observational and explanatory possibilities without being reduced to one supposedly universal language. An evidential mismatch may be a source artifact, an incompatible molecular regime, or a new productive scientific question; current source-linked data must discriminate, not make a label decide.

**BACKTRACK** from more binary automata toys. Next substantive research should locate original author 2014 supplementary NMR restraints for the 1IGD positive control and 1EXR negative control, original reflection data and conditions, then a preregistered same-target replay. If they are inaccessible, pivot to another public, auditable real dataset with independent controls rather than mint a fake 'real-world PASS'.

**Missing/Harvest:** Original official 17 groups unchanged, one fresh 00_INTAKE PDF classified but left in place, no new acquired file, no global Harvest number, no downstream epistemic authority transfer. MQR 5.4 OPEN; originality HOLD; external full physical replay HOLD.
