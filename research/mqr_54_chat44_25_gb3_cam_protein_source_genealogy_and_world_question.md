# MQR 5.4 · MQR44 R25 — Actual experimental genealogy rather than invented paradigm birth

**Date:** 2026-11-21 KST. Claim type: original publisher- and repository-supported **chronological source map**, NOT demonstration of direct laboratory sample continuity. Links and names checked; no new structure coordinate, NMR time-domain or BMRB raw bytes downloaded in this session.

## Scientific provenance family, explicitly independent of rhetoric

| Publication / record | Nature of experimentally supported object | Why it matters to MQR |
|---|---|---|
| Derrick & Wigley (1994), [PDB 1IGD](https://www.rcsb.org/structure/1IGD) | GB3 high-resolution crystal structure | A crystallographic reference model with its own physical crystals and reflection metadata |
| Ulmer et al. (2003), [PDB 1P7F](https://www.rcsb.org/structure/1P7F) | NMR dipolar-coupling-informed solution refinement of GB3 crystal model | **NMR/X-ray hybrid refinement existed at least by 2003**, therefore MQR cannot assign all such joint inference to the 2014 REFMAC5 implementation |
| Bertini et al. (2009), [journal DOI 10.1021/ja8080764](https://doi.org/10.1021/ja8080764), [PDB 2K61](https://www.rcsb.org/structure/2K61) | Solution NMR structure of calmodulin–DAPk peptide, with associated restraint/shifts via [BMRB deposition summary](https://bmrb.pdbj.org/data_library/summary/index.php?bmrbId=7424) | Demonstrates a **public deposited solution-structure witness separate from crystal PDB 1YR5**; chemical/sequence and target preparation matching remain to be audited |
| Rinaldelli et al. (2014), [primary DOI 10.1107/S1399004713034160](https://doi.org/10.1107/S1399004713034160) | REFMAC5 integration of NMR RDC/PCS with original PDB diffraction factors, five author-reported protein systems | Specific algorithmic integration plus published positive GB3/negative calmodulin outcomes, not first scientific discovery of protein dynamics |
| Carlon et al. (online **2018**, journal **2019**), [DOI 10.1007/s10858-018-0212-3](https://doi.org/10.1007/s10858-018-0212-3) | Improved multidomain/multisubunit NMR orientation/magnitude tensor controls, multi-target/calmodulin comparisons | Follow-on *method adjustment and rival-error explanation*, not simply confirmation of a final common protein ontology |

## Crucial mismatches for future original-data work

1. **PDB crystal entry ≠ solution model**. 1IGD is an X-ray starting model. 1P7F and related NMR-solution models may have different residue constructs or isotope conditions. 1YR5 is the *calmodulin–DAPk peptide* X-ray entry, whereas 2K61 is the corresponding solution structure; 2X0G is calmodulin bound to the **whole DAPk protein**, not the same peptide-only physical object. [Carlon full publisher original](https://link.springer.com/article/10.1007/s10858-018-0212-3) explicitly says NMR used in the latter cross-comparison is **peptide-bound sample** data and NOT an independent solution measurement on whole DAPk.
2. A secondary BMRB search result for 2K61 returns multiple different BMRB record IDs; without verifying the exact experimentally linked BMRB data accession and original sample metadata, one must **not invent an exact BMRB raw restraint archive association** from search snippets. The [official 2K61 PDB entry](https://www.rcsb.org/structure/2K61) and [wwPDB DOI](https://doi.org/10.2210/pdb2K61/pdb) are firmer immediate anchors.
3. 2014 IUCr paper's source material **explicitly locates supplement ZIP and DOC**. [R23 audit](mqr_54_chat44_23_iucr_supplement_primary_source_discovery_and_access_hold.md) records URL verification but no bytes. Distinguish a published available file from a file MQR has actually fetched and hashed.
4. Same research team continuing a problem across years establishes a **scholarly research genealogy**, not evidence that one sample, one scientific question or one specific measured error caused the later software feature. Historical causation would need contemporary design notes, dated experiment receipts and direct author attributions.

## Strongest currently demonstrable intellectual trajectory

The field did not progress along a crude line 'no shared language -> one new REFMAC5 dictionary -> all proteins identical'. Original studies show:
- early cross-method comparison of structures and RDC constraints (GB3);
- a separate peptide-bound target with measured structural heterogeneity (CaM);
- a joint-likelihood refinement method permitting **simultaneous use of raw original diffraction factors and model-dependent NMR restraints**;
- cases of **incompatibility** whose resolution may require a material-regime distinction, not linguistic harmonization;
- a later **measurement condition/parametric tensor** correction in another complex.

The MQR founding issue is therefore **not** the count of newly coined terms but the creation of **reusable instrument-model checks that make previously ambiguous discrepancies scientifically discriminable**, with both false-conflict and real-conflict cases. This program is anticipated by actual biophysical scientists, Galison, Nersessian, Mitchell, Weiskopf and others; novelty MUST remain HOLD.

## Source priority and open gates

Priority 1: original official 2014 [DOC instructions](https://doi.org/10.1107/S1399004713034160/dz5299sup1.doc) and [ZIP](https://doi.org/10.1107/S1399004713034160/dz5299sup2.zip); retrieve and inspect when bytes accessible.
Priority 2: exact deposit coordinate and NMR restraint/map/measurement metadata for GB3 positive (1IGD vs 2003 solution structures) and CaM peptide negative (1YR5 vs 2K61), with source-specific setup and independent frozen test.
Priority 3: original 2019 supplementary tensor-parameter data and version-specific REFMAC5 source, independent solver replay if available.

**Note:** original official missing-source ledger remains 17 heterogeneous groups; this is a new target-specific archival radar, no automatic denominator increase. No source moved/uploaded, MQR 5.4 OPEN.
