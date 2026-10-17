# MQR-4.120 P8 — Four-Variable Ordered Lineage and Exclusion-Fiber Audit

2026-10-17. SYNTHESIS OF TWO PUBLICLY RENDERED FULL-TEXT DATA SOURCES. NO RAW BYTE HASH VERIFICATION.

## Exact question and prior genealogy
A previous P8 three-variable ordered subsequence witness matched 9,223 Zenodo rows to MIT's 11,204 rows, but could not identify which rows were missing or separate duplicate values. We extended the observable key from (earnings, assigned Z, received D) to (earnings, Z, D, sex). This follows MQR's original measurement-quotient question: which latent identities remain compatible with the observed representation? MQR-4.101's selection-dependent target and 4.107/4.109's distinction between retained statistics and evidence history are directly relevant. MQR-4.89's Bernoulli counterexample is pre-existing, so this report does not claim a new causal identification theorem.

## Sources and method
MIT official ASCII jtpa.raw: https://economics.mit.edu/sites/default/files/publications/jtpa.raw (11,204 rows × 19 columns) and 2002 paper replication MATLAB code defining columns 2=earnings, 3=randomized assignment, 4=received training, 5=sex.
Zenodo 18836198 jtpa.csv: https://zenodo.org/records/18836198/files/jtpa.csv?download=1 (9,223 observations × 11 variables, plus header). Both files inspected in full as rendered text via Firecrawl, not directly authenticated bytes.
Greedy *forward* scan matches quadruples (MIT cols 2,3,4,5) to (Zenodo earnings,Z2,D2,sex). **All 9,223 / 9,223 rows matched in source order.** The preceding triple-only greedy alignment had five mismatched sex values; extending the key resolves them and still matches every row. A quadruple is not a primary unique participant identifier, and equality of four fields does not prove other columns or transformations.

## Selection-fiber decomposition (relative to the greedy four-field matching)
MIT full source n=11,204; retained n=9,223; not matched n=1,981. Based on this alignment:
- Full MIT Z=0: 3,717 observations, D=1: 54, mean earnings 15,040.50363196; Z=1: 7,487, D=1: 4,804, mean earnings 16,199.93695739; unadjusted Z earnings difference 1,159.43332543.
- Retained Z=0: 3,090, D=1: 43, mean earnings 15,310.52006472; Z=1: 6,133, D=1: 4,015, mean earnings 16,487.49274417; unadjusted Z difference 1,176.97267945.
- Not matched Z=0: 627, D=1: 11, mean earnings 13,709.80063796; Z=1: 1,354, D=1: 789, mean earnings 14,897.44091581; unadjusted Z difference 1,187.64027785.
- Under triple key alone 2,073 Zenodo rows had at least one duplicate quadruple-independent triple in the full MIT source; this is a warning about individual identity. Four-variable matching resolves five mismatches in greedy alignment but does not establish uniqueness of the matching subsequence.

## Interpretation and adversarial limits
Different marginal means and assignment rates across selected and excluded sets demonstrate that the source and reconstructed sample do not represent numerically identical empirical summaries. This does not establish the mechanism of exclusion or selection bias in a counterfactual estimand. The reconstructed set differs by 1,981 from source row count; whether these rows are excluded by measured schooling density, missingness, Han's eligibility rule, or another transformation remains an *unanswered* scientific/source question.
The exact list of excluded MIT IDs depends on resolving ambiguity in duplicate quadruples and obtaining the transformation script or row IDs; our current unmatched rows are **alignment-conditioned**, not a certified historical deletion log. Original ITT study design, independent assignment, clustering, IV exclusion, Han sequential regime assumptions, and any J2 appellate legitimacy remain HOLD.
A stronger proof would use row IDs or additional original fields and a verified transformation to map each row one-to-one. Pure agreement of finite observables can never by itself certify independent documentary authority or the entire acquisition history.

## Verdict
FOUR-FIELD_ORDERED_MATCH_PASS_BOUNDED 9223/9223; SELECTION_NUMERICAL_DECOMPOSITION_PASS_BOUNDED; UNIQUE_ID_JOIN_HOLD; ACTUAL_EXCLUSION_RULE_HOLD; DIRECT_FILE_BYTES_MD5_HOLD; CAUSAL_EFFECT_IDENTIFICATION_HOLD. Remain MQR 4.120 ACTIVE/P8. Greenberg, CCQM, 4.118 Harvest and 4.119 real-evaluator HOLD persist.
