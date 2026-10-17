# MQR-4.120 P8 — Authorial Sample-Size Confirmation and Missing-Row Provenance Gate

2026-10-17; SOURCE_CROSSCHECK_PASS_BOUNDED, SELECTION_RULE_HOLD.

## New primary-author check
Han, *Optimal Dynamic Treatment Regimes and Partial Welfare Ordering*, JASA 119 (2024), explicitly reports N=9,223 in the empirical analysis; the study combines JTPA with U.S. Census and National Center for Education Statistics local high-school-density information and constructs Y2, D2, Z2, Y1, D1 and Z1 (school density threshold). This confirms that the 9,223 rows in the Zenodo reconstructed CSV agree with the published analytic sample size; it does NOT disclose the transformation or indicate which exact 1,981 records were excluded. Sources: https://www.tandfonline.com/doi/full/10.1080/01621459.2023.2238941 and https://sukjinhan.com/optDTR .

## Source custody: official vs related third party
The primary author's page links official supplement and Han23_Replication_Files.zip at https://sukjinhan.github.io/Han23_Replication_Files.zip . A direct download was attempted but failed, so its content, hashes and preprocessing steps have NOT been inspected. Distinguish an author-controlled archive existence from actually inspected bytes.

The separate public third-party repository https://github.com/chensy123-sys/Additive-IV/tree/main/JTPA publishes jtpa_han.tab and data_change.R, which explicitly reads jtpa_han.tab, drops recid and n_hs2_abv, thresholds and transforms edu, prevearn, n_hs2 and earnings, then writes jpta_han.csv. That code is from a later research implementation, not verified as Han's original source-to-sample selection generator. Its transformation is downstream of already-selected jtpa_han.tab; it cannot by itself establish the upstream N=11,204 -> N=9,223 exclusion criterion. A reused filename is not authority ancestry. Original code should take precedence over the derivative for any causal provenance claim.

## Previously verified finite observational fiber
MIT original ASCII N=11,204, 19 columns; Zenodo N=9,223, 11 columns. Ordered four-key (earnings,Z,D,sex) subsequence matches all 9,223. Bidirectional earliest/latest matching fixes 9,208 source positions conditionally, while 15 zero-earnings observations have at least two possible source IDs; consequently an original-ID deletion roster is not certified. N=1,981 is the difference in counts, not an identified exclusion list.

## Methodological continuity
Original MQR noninjective observational representation and 4.101 selective verification are directly relevant. 4.107 acquisition history and 4.109 documentary warrant warn that even perfect ordered matches do not certify selection provenance. 4.89's Bernoulli causal nonidentification predates 4.120 P7; 4.113's statistical-experiment order does not establish physical/administrative source authenticity. P8 is a claim-specific empirical genealogy test, not a proof of institutional appeal legitimacy.

## Next falsifiable tasks
Obtain verified copy of official replication archive; inspect filenames and actual selection/merge scripts, source key, missingness condition and cohort restrictions; reconcile records and key ambiguities with MIT source IDs and published N=9,223. Do not invent an exclusion predicate based only on means, school density narrative or observed row counts. Reassess source comparison before design-aware causal estimates.

## Decision
PUBLISHED_SAMPLE_SIZE_CONFIRMED (9,223) / EXTERNAL_EDUCATION_MERGE_DOCUMENTED / OFFICIAL_REPLICATION_ARCHIVE_LOCATED / OFFICIAL_ARCHIVE_BYTES_HOLD / DERIVATIVE_PREPROCESS_CODE_READ / UPSTREAM_SELECTION_MECHANISM_HOLD. 4.120 ACTIVE/P8; Greenberg, CCQM, Harvest and 4.119 real-evaluator obligations untouched.
