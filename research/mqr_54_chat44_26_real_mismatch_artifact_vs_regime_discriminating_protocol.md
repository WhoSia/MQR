# MQR 5.4 · MQR44 R26 — A falsifiable historical question: when does a discrepant scientific readout warrant a new physical entity or process?

**2026-11-21 KST; scientific-history analysis, no original experimental replication.**

## Three mechanisms that identical wording 'NMR and X-ray disagree' can conceal

**H1. A real environmental/conformational difference.** The same protein (with target-specific chemical preparation) may have different conformational ensembles or interdomain orientations in crystal and solution. Evidence: [Rinaldelli et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/), CaM joint refinement retains RDC mismatch under attempted preservation of R_free and chemistry; [Bertini et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19317469/) reports solution structure of CaM–DAPk peptide and [PDB 2K61](https://www.rcsb.org/structure/2K61). **Authors' interpretation; physical cause not independently verified by MQR.**

**H2. A measurement-system difference.** Separate isotope-labelled samples may have differing concentrations of the RDC alignment medium, which alters alignment tensor magnitudes and creates an apparent mobility/mismatch. [Carlon et al. 2018 online/2019 volume](https://link.springer.com/article/10.1007/s10858-018-0212-3) model the Sxl–CSD1 complex (PDB 4QQB) using common tensor orientation while allowing different magnitudes and report improved joint refinement. **The new operation is a conditional physical interpretation of a model constraint, not a guarantee of rigidity.** Their published Table 1 is independently re-arithmetized in [R24](mqr_54_chat44_24_carlon_tensor_alignment_false_mobility_primary_comparison.md).

**H3. Source/representation mismatch.** One group may be comparing different sample stoichiometries, chain constructs, NMR restraints or REFMAC versions. The 2019 study explicitly compares whole DAPk and a DAPk-derived peptide while reusing the **peptide-bound NMR source**, an intentional modeling comparison, not same-form whole-protein solution measurement. Even the starting PDB 3NHE is a USP2a–ubiquitin complex rather than an isolated ubiquitin crystal [R17](mqr_54_chat44_17_pdb_chain_specimen_and_refinement_identity_gate.md).

## Prospective discriminating test (not performed)

Under a pre-specified common protein construct and matching temperature, solution and ion conditions:
- Hold **sample identity, concentration, alignment medium, hardware calibration and NMR treatment** fixed across a set of independent replicates; vary alignment-medium concentration in a planned experimental factor, with reference sample controls.
- Independently measure tensor **orientation** and **magnitude** across samples. If magnitude changes in a predictable way while orientation remains stable and the same rigid structure accommodates measured RDCs, H2 obtains support for that particular system; the distinct-domain dynamics hypothesis is not thereby universally refuted.
- Change protein's physical preparation regime (crystal vs solution; peptide vs full target only where chemically justifiable), and compare prespecified residue-specific RDC/PCS discrepancies while retaining crystal held-out R_free and geometry. Stable mismatches under calibration and model controls support H1.
- Ensure comparison targets and data lineage are the same, including PDB chain, residue offset, and which structure-factor/R-free flags were used. A disappearing discrepancy after correcting a mismatched identity or software version supports H3.
- Negative controls: independently prepared same-concentration samples, blinded specimen labels, deliberately mismatched sample ID caught in validation, reprocessed common original source with alternate tensor assumptions, and soft geometry constraints used only to diagnose possible overfit.
- Do not infer that a **successful joint fit** identifies a unique true physical model: both H1/H2 might be compatible with in-sample RDCs under different parameterizations. Genuine leverage requires external, held-out, independently calibrated observational consequences.

## Distinct historical-philosophical payoff

The author of an old conceptual vocabulary can recognize a new scientific question **without first adopting an entirely new ontology** when joint scientific practice makes a *specific residual* interpretable and testable. The sequence need not be chronological 'mismatch -> instrument -> final unified science'; it can branch:
1. apparent conflict explained by sample or model artifact, so claims about physical dynamics withdrawn;
2. persistent material disagreement, opening domain-motion, timescale and crystalline-packing research;
3. unresolved because genuine measurements are absent or multiple models underdetermined.

This follows a classical philosophy of experimental error and model selection, strongly preceded by Galison, Mitchell, Nersessian, Rheinberger, and the original experimental authors. It is an MQR **cross-field research question/gate**, not a novel biological finding or philosophical theorem. **Do not award 5.5, Real-Lang release or global source-transfer authority.**

## Actual missing witnesses

2014 IUCr supplementary [instructions DOC](https://doi.org/10.1107/S1399004713034160/dz5299sup1.doc) and [protocol/data ZIP](https://doi.org/10.1107/S1399004713034160/dz5299sup2.zip), 2019 Carlon Springer [supplementary DOCX](https://static-content.springer.com/esm/art%3A10.1007%2Fs10858-018-0212-3/MediaObjects/10858_2018_212_MOESM1_ESM.docx), original matched NMR datasets and reflection data all have verified **web source locations** and unverified **current MQR byte custody**. Container download and web archive direct retrieval were unsuccessful, no hashes/manifest entries fabricated. A new original publicly hosted 2014 data archive can be substantially better than a hypothetical future lab experiment for methodology checking once retrievable, but it is no proof of independent measurement.

**Remaining official missing ledger:** 17 heterogeneous original groups, unchanged. MQR 5.4 OPEN.
