# Real-Language MQR 5.4 — Interfield Target-Receipt Gate (experimental)

**Status 2026-11-21:** NON-PROMOTING EXPERIMENTAL TOOL, not a canonical Real-Packet parser, grammar release, Rust authority implementation or external calibration. Existing Real-Lang v0.25 scaffold, v0.31 transport semantics and latest 4.114 P2 source-independence research take precedence. No import into Rust's authoritative evaluator.

## Purpose

MQR44 R16–R20 audited a real peer-reviewed report of joint X-ray/NMR structure refinements, but the numerical inputs are **published Table 1 summaries**, not downloaded raw X-ray structure factors, free-R reflection flags, and solution NMR restraints. A claim that a machine can make from those summaries is different from a separately replayed measurement. This helper prevents accidental **target, specimen, regime or ancestry laundering** when creating an interfield evidence bridge.

Input is one Claim specifying the exact target, specimen, regime and expected lineage identifiers and any EvidenceReceipt entries. The caller declares whether original scope was retained, physical pairing was authenticated, calibration verified, reproduction truly independently executed and the reported result passed. **These flags are supplied claims**, not verified by the script.

### Source kinds
- SYNTHETIC: model-specified inputs and synthetic reports.
- PUBLISHED_SUMMARY: an author's printed aggregate or table. It does not mean paper bytes constitute detector traces.
- SOURCE_RAW: claimed actual original source bytes, not necessarily independently analysed. Without an independent replay, report `RAW_SOURCE_BYTES_CLAIMED_NOT_REPLAYED` (never use the published-summary label).
- INDEPENDENT_REPLAY: a claimed independent reproduction with distinct processing/provenance. Lab independence **still not certified** by its label or Boolean.

### Targets
- X_RAY_R_FREE: independent holdout-reflection statistic relative to author-specified reflection flags and experimental preparation.
- NMR_Q_RDC: model-to-RDC restraint fit. Do not equate this in-sample fit with held-out R_free.
- LOCAL_TASK: a specific native task.
- CROSS_FIELD_TRANSPORT: source-target transported relation, rather than in-domain refitting.

All string IDs are exact and intentionally must be stable at the receipt interface; same name does not certify same source. No universal truth-distance scalar, no final ontology PASS.

### Guard ordering

1. Validate complete receipt types, IDs, Boolean fields, source kinds, uniqueness.
2. Select by **target + specimen + declared regime**; refuse accidental borrowing of different protein and metric.
3. Preserve original scope, verify matched physical sample and calibration.
4. Any reported contradiction is exposed; majority of positive records cannot suppress it.
5. Preserve declared lineage coverage, distinguish synthetic from published-source agreement.
6. Require independent replay before any bounded replay status; **never** assert that two named lineages truly break noncommon error ancestry.

Status `BOUNDED_REPLAY_REPORTED_ANCESTRY_NOT_EXTERNALLY_CERTIFIED` is NOT WORLD_AUTHORITY_PASS. A missing signed source receipt, unverified measurement mapping, hidden calibration lineage or new rival prevents scientific promotion.

### Reproduction (from repository root)
```sh
python -m unittest discover -s language/real/experiments -p 'test_interfield_target_receipt_v54.py' -v
python -m unittest discover -s language/real/experiments -p 'test_interfield_published_refmac5_v54.py' -v
```

A container where outbound GitHub raw downloads were blocked by DNS was supplied a local text reconstruction of exactly these modules/tests; **31 local unit tests passed** after adding 10 frozen-byte tests and 1 raw-source-kind regression: 17 general, 4 published-case, 10 byte-integrity. The GitHub commits themselves are verified using authenticated repository reads. **Bitwise identity of local copy to repo blobs was not independently established**, and no full repo or Rust CI passed in this work session.

### Published original example

Rinaldelli et al. (2014), [original 2014 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/), five systems 3SHI, 3NHE, 1IGD, 1EXR, 1YR5. Tests confirm for each protein's X-ray R_free and NMR Q_RDC published entries that the current status is `HOLD_PHYSICAL_PAIRING_UNVERIFIED`, **not** independent experiment pass. Matching PDB entry IDs do not verify paired solution/crystal specimens; PDB 3NHE includes USP2a–ubiquitin complex and PDB 1EXR is Ca-bound calmodulin. A publication's original authors may themselves have performed the experiment; the HOLD concerns MQR's *own independent replay evidence*.

Next change in this experimental lane should be a **source-backed signed provenance receipt loader** and optional SHA-256 manifest checks, not new arbitrary types alone. External physical evidence still requires human/disciplinary scrutiny; do not equate checksums with a verified molecule, timebase or calibration.

### Research and governance

[Original protein source analysis](../../../research/mqr_54_chat44_16_primary_refmac5_five_protein_success_and_failure.md), [PDB scope correction](../../../research/mqr_54_chat44_17_pdb_chain_specimen_and_refinement_identity_gate.md), [Real-Lang existing experimental bridge](OPEN-HORIZON-BRIDGE-V54.md), [live Real-Lang doctrines](../../../doctrine/CURRENT.md). No new Harvest authority and no MQR5.5 / Real-Lang release promotion.

## Addition R22 — Frozen byte manifest gate

[Source-byte verifier](frozen_byte_witness_v54.py) validates an explicitly *previously frozen* lowercase SHA-256 digest and byte count against a local file, reads in chunks and fails on mutation, truncation, extension or absent data. [10 integrity regression tests](test_frozen_byte_witness_v54.py) passed locally. The calling workflow must establish that the expected hash was independently sealed before new evidence; computing an expected hash from the same suspect file at check time proves nothing useful. **Byte identity does not establish molecule/sample identity, sensor calibration, lineage independence or physical correctness.** No network access or external provider login is needed for these local tests.

Source-order distinction is preserved: `SOURCE_RAW` still needs a separately reproducible process; `INDEPENDENT_REPLAY` source-kind can be *declared* but must not become scientific authority without external provenance. Unit tests are not a production release signoff.
