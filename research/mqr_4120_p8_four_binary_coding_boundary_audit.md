# MQR-4.120 P8 — Four Derived Binary Fields: Exact Boundary Audit

2026-10-17. All claims CONDITIONAL on the public textual Zenodo CSV (9,223 observations), not certified original bytes.

## Rowwise empirical checks
Original Han JASA 2024 paper specifies binary terminal earnings, baseline earnings and schooling/school-density variables. Public reconstructed CSV: https://zenodo.org/records/18836198/files/jtpa.csv?download=1 . Third-party educational source: https://github.com/chensy123-sys/Additive-IV/blob/main/JTPA/jtpa_han.tab .

All 9,223 rows were compared for:
- Y2 == indicator(earnings > 11,187) (observed median) : **0 errors**. 4,611 positive Y2; one observation exactly at median.
- D1 == indicator(edu >= 12) : **0 errors**. Coding of education years does NOT independently prove verified diplomas/GED.
- Y1 == indicator(prevearn >= 6,000) : **0 errors**. Using strict > 6,000 makes **220 errors**, all at the tied value 6,000. Y1 positives: 1,932.
- Z1 == indicator(n_hs2 > 35) : **0 errors**. Z1 positives: 1,248; observed n_hs2 range 0–346.

The percentile tie in Y1 illustrates that an unspecified greater-than versus greater-than-or-equal convention can shift binary evidence in 220 observations even when both are informally called an 80th-percentile threshold.

## Relation to original research
Han's counterfactual welfare partial-ordering analysis is based on derived binary histories and IV restrictions, not the earlier P8 dollar-valued mean difference. These coding identities do NOT reproduce Han's LPs, original instrumental validity or published policy order. MQR's original quotient problem, 4.101 target/rubric conditionality, 4.107 evidence history, 4.109 documentary authority and 4.113 target-relative experiment informativeness are directly relevant.

## Selection gap
The four deterministic coding rules characterize the released 9,223 records; none identifies the upstream exclusion/merge predicate responsible for 1,981 MIT source IDs. Han's official ZIP literal bytes, Census/NCES join/geo keys, unobserved exclusions and source checksum remain HOLD. The third-party recid mapping is fully consistent on source fields but not a substitute for author-certified source lineage.

## Verdict
FOUR_BINARY_FIELDS_9223_EXACT_PASS_BOUNDED / Y1_TIED_BOUNDARY_EXPOSED / 1981_SOURCE_SELECTION_RULE_HOLD / AUTHOR_ZIP_CUSTODY_HOLD / HAN_LP_REPRODUCTION_HOLD / REAL_REMEDY_EFFECT_HOLD. ACTIVE P8.
