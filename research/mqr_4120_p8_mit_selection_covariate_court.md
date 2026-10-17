# MQR-4.120 P8 — Exact Recid Selection Matrix and Column-10 Anomaly

2026-10-17. Original-to-third-party MIT recid link; complete source-text conditional descriptive analysis. **No identified exclusion predicate**.

## Prior work and methodological requirement
MQR 4.101 selective adjudication, 4.107 evidential acquisition history, 4.109 source-sensitive sufficiency, and 4.113 model-relative information order require that an observed selection association be distinguished from a historical record-generation rule. The MQR 4.89 Bernoulli nonidentification was already established; new synthetic worlds are not progress. The present analysis uses reconstructed recid memberships, not a new causal identification procedure.

## Original source and linkage
MIT jtpa.raw at https://economics.mit.edu/sites/default/files/publications/jtpa.raw, 11,204 rows, 19 whitespace-separated numeric columns. Third-party copy https://github.com/chensy123-sys/Additive-IV/blob/main/JTPA/jtpa_han.tab contains exactly 9,223 distinct MIT recids; all match original earnings/assignment/participation/sex. Set difference has 1,981 recids, only conditionally recovered as the third-party file is not byte-certified against Han official archive. Re-read entire textual sources and computed source-field-conditioned retention.

## First concrete selection-correlate audit
In original MIT col10 (1-indexed; **semantic label not independently verified**), four observed values partition all N=11,204:
- value 0: total 5,395; retained 4,730; retention 0.87674
- value 0.4073359: total 454; retained 143; retention 0.31498
- value 0.5332298: total 724; retained 167; retention 0.23066
- value 1: total 4,631; retained 4,183; retention 0.90326
The two fractional-value groups together contain N=1,178; retained 310; excluded 868, which accounts for 868/1,981 (43.82%) of excluded observations. The two 0/1 groups combined contain N=10,026; retained 8,913; excluded 1,113. Therefore **one simplistic rule excluding all fractional col10 rows is disproved**: 310 fractional rows are retained, and 1,113 binary rows are excluded. Strong differential retention does not license assigning col10 a causal or institutional meaning. Need original codebook.

Other observed fields are less discriminatory in a one-column descriptive scan: MIT col6 value 0.716404 has retention 252/370=68.1%, value .6876773 245/325=75.4%, while 0 or 1 groups have 79.2%/84.6%. MIT col9 fractional groups retain 370/517 and 179/247 (~71.6%/72.5%). All these are post hoc explorations and should be assessed with multiple-comparisons and competing-source caution before inferential statements.

## Causal and documentary reservations
The numeric association does not establish a structural selection cause, merger-key criterion, missingness mechanism, or a well-defined target treatment effect. The field may be an estimation weight, imputation-related variable, experimental subgroup statistic or anything else; no meaning may be invented. The original program's 19 columns and official Han ZIP preprocessing/coding instructions are the next documents to inspect. Observational classification precision is not data-custody proof.

## Forward falsification
Obtain original MIT variable labels, locate Han official record-selection/preprocessing statements or code, test proposed predicate on every ID with held-out confirmation; compare selection by source identifier and external school-density join; recover official binary bytes/checksums and Han ZIP contents. No actual original IV-QTE reproduction or appeal-remedy analysis is claimed.

## Verdict
RECORD_ID_SET_DIFFERENCE_PASS_BOUNDED / MIT_COL10_RETENTION_CORRELATE_CONFIRMED / SIMPLE_ALL_FRACTIONAL_FILTER_REFUTED / COL10_SEMANTICS_HOLD / SELECTION_RULE_HOLD / OFFICIAL_SOURCE_CUSTODY_HOLD. MQR 4.120 ACTIVE/P8; Greenberg, CCQM, Harvest, 4.119 human assessment HOLD.
