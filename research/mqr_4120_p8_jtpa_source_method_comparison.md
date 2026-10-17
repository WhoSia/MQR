# MQR-4.120 P8 — JTPA Reconstructed Data vs Original Design: Primary-Method Source Court
2026-10-17. SOURCE-COMPARISON PASS_BOUNDED; REPRODUCTION and causal interpretation HOLD.

## Source identity and methodological distinctness
1. **Abadie, Angrist & Imbens (2002)**, *Econometrica* 70(1), 91–117, DOI 10.1111/1468-0262.00270. The published paper develops instrumental-variable quantile treatment-effect estimation for the distribution of trainee earnings. MIT Angrist Data Archive explicitly lists **jtpa.raw** and the MATLAB files **qeffectsfinal.m**, **qregkb.m**, **quantlsf.m**, for recreating published Tables 2 and 3. https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive
2. **Han (2024)**, *JASA* 119(547), 2000–2010, DOI 10.1080/01621459.2023.2238941. It studies sequential education/training regimes under instrumental-variable assumptions, partial welfare ordering, maximal policy elements, and linear programs. https://www.tandfonline.com/doi/full/10.1080/01621459.2023.2238941
3. **Zenodo 18836198**, created 2026-03-02, explicitly describes a **constructed dataset**, combining JTPA training data with local high-school-density data for educational IV. Its variable dictionary identifies Z1 (school density threshold), D1 (schooling), Z2 (randomized training assignment), D2 (training received), and earnings. https://zenodo.org/records/18836198

## Why the previous calculated contrast does NOT reproduce either study
The preceding P8 full-text parse yielded 9,223 observations, group means USD 15,310.52 and 16,487.49, and unadjusted Z2 contrast USD 1,176.97, plus arithmetic first-stage and Wald ratios. These are descriptive statistics from a *third-party extracted textual view* of Zenodo's reconstructed CSV. Neither the Abadie–Angrist–Imbens IV quantile estimator nor Han's sequential dynamic-regime partial-order LP was implemented. Therefore do not call this a replication, design-correct ITT, LATE, quantile effect or optimal welfare policy finding.

## Source and method mismatch gates
- **Dataset lineage:** Zenodo jtpa.csv -> Han reconstruction/transformation -> underlying JTPA study; MIT jtpa.raw is a separate archived original-analysis source. No equality or identical cohort is presumed; require row-level joins, identifiers, restrictions and transformations.
- **Estimand:** assignment mean contrast, mean receipt effect, quantile treatment effect, and regime-level counterfactual welfare are distinct functions. Fix population, treatment, outcome and counterfactual policy before asking whether a method identifies a target.
- **Instrument status:** Z2 randomized assignment is described by Zenodo; Z1 school density threshold is a proposed schooling instrument. A dataset field labeled 'instrument' is not independent validation of IV exclusion or monotonicity.
- **Data integrity:** Zenodo reports 9,224 x 11 while the extracted text produced 9,223 observation rows and 1 header. Metadata convention unresolved; direct literal bytes / MD5 verification outstanding. The published file record lists MD5 1be2247cff05b2e6791ee330462bc181. A preview or scraped text cannot certify that checksum.
- **Design:** clustering, strata, eligibility, exclusions, attrition, baseline variables and variance estimator must be checked against the original protocols and the reconstruction before claiming design-aware inference.
- **Scope veto:** JTPA is not an institutional scientific evaluation appeal; a welfare-policy causal study does not confer J2 legitimacy or real remedial effects.

## Scientific genealogy / non-novelty
This source court reuses MQR-4.89's causal nonidentification, MQR-4.101 fallible label/target restrictions, MQR-4.107 source versus acquisition-history distinction, MQR-4.111 intervention-altered state, MQR-4.113 Blackwell experiment comparison, and MQR-4.119/4.120 claim-versus-authority separation. In particular **Han's partial welfare order is an established methodological comparator**, not a new MQR theorem. MQR-4.53's nonuniversal scalar-progress issue is related philosophically but does not prove or derive Han's treatment-ordering result.

## Verdict / next discriminating action
SOURCE_METHOD_COMPARISON_PASS_BOUNDED; RAW_MD5_HOLD; TRANSFORMATION_LINEAGE_HOLD; ORIGINAL_ESTIMATOR_REPRODUCTION_HOLD; DESIGN_AWARE_ITT_HOLD; REAL_REMEDY_TRANSPORT_HOLD.
Compare first-party MIT jtpa.raw and supplied original code with Zenodo's reconstructed file *only after downloading and authenticating each source*. Do not add synthetic Bernoulli regressions, assert progress from file creation, or lift inherited Greenberg, CCQM, Harvest, and 4.119 assessor HOLDs.
