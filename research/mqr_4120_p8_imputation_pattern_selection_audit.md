# MQR-4.120 P8 — Imputation-Footprint Selection Audit

2026-10-17. CONDITIONAL DESCRIPTIVE PASS / HISTORICAL EXCLUSION RULE HOLD.

## Verified primary variable dictionary
The econdata AAI2002 19-variable codebook https://kvasilopoulos.github.io/econdata/variables.html defines MIT original jtpa.raw col6=hsorged (high-school graduate/GED, imputed), col9=married (imputed) and col10=wkless13 (worked fewer than 13 weeks in preceding year, imputed). Their fractional values are plausibly imputation footprints rather than continuous person-level measurements. The author's MIT program/code archive is https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive.

## Actual computed source-to-reconstructed matching
MIT original 11,204 rows, identified by original recid. Third-party Additive-IV jtpa_han.tab contains 9,223 distinct verified matching recids; excluded set size 1,981. Official Han ZIP equality remains unverified; the findings below are **conditional on the third-party file**.

Imputation indicator I is defined as a value not exactly `0` or `1` for corresponding MIT source columns 6, 9 and 10, in that order. B denotes binary 0/1.
Pattern | MIT rows | Retained | Excluded | Retention
BBB | 8920 | 7964 | 956 | 89.283%
BBI | 953 | 263 | 690 | 27.597%
BIB | 547 | 475 | 72 | 86.837%
IBB | 489 | 424 | 65 | 86.708%
BII | 89 | 24 | 65 | 26.966%
IBI | 78 | 23 | 55 | 29.487%
IIB | 70 | 50 | 20 | 71.429%
III | 58 | 0 | 58 | 0%

Every pattern total sums to 11,204 and retained counts to 9,223. Any imputation footprint 2,284 rows, retained 1,259; no footprints 8,920, retained 7,964. Col10 fractional and col6/9 fractional are NOT interchangeable in retention pattern. Strong col10 association persists across imputation strata, but a deterministic one-column exclusion rule is false; some col10 fractional records remain, and binary records can be excluded. All-III=58/58 omitted is a source-conditional **zero-cell**, not evidence of a historical protocol.

## Philosophical and inferential ceiling
MQR-4.101 selective reference; 4.107 and 4.109 acquisition history/provenance; 4.113 experiment comparison; 4.89 causal nonidentifiability all require a historical selection mechanism to be demonstrated, not reverse-engineered from predictive correlations alone. Classifying imputed values is not observing source construction: imputation status may proxy measurement missingness, cohort history, or other variables. No external school density merge mechanism, random sampling, causal selection effect, or original QTE replication has been established.

## Next discriminating tests
1. Read author-side Han preprocessing and original JTPA covariate construction; test exact rule against all recids.
2. Check whether fractional covariate values identify historically missing responses versus assigned expectation values in the original experiment and whether imputation is pre/post assignment.
3. Verify source immutable bytes and official archive equality.
4. Assess target-population and causal-estimand shifts only after inclusion predicate and design reconstructed.

Verdict: IMPUTATION_FOOTPRINT_ASSOCIATION_PASS_BOUNDED / ALL_III_58_ZERO_CELL_CONFIRMED_CONDITIONALLY / SELECTION_PREDICATE_HOLD / SOURCE_CUSTODY_HOLD / CAUSAL_TRANSPORT_HOLD. 4.120 ACTIVE/P8.