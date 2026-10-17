# MQR-4.120 P8 — Dual Falsification of Imputation-Only and Block-Only Sample Rules

2026-10-17. Conditional full-text comparison of MIT original jtpa.raw (11,204 rows) and independently hosted third-party jtpa_han.tab (9,223 distinct recids); official Han ZIP equality and raw cryptographic custody still HOLD.

## Question
Can the 1,981-row discrepancy be explained by a one-field imputation exclusion rule or by dropping contiguous MIT record-ID prefix blocks? Prior P8 audits have recovered original ID identity and decoded MIT col10 as wkless13 (imputed fewer-than-13-weeks-worked indicator); original science-theory distinction remains observation versus acquisition lineage, per MQR 4.101, 4.107 and 4.109.

## Exact empirical cross-tab for MIT col10
- fractional values: source n=1,178, retained 310, excluded 868: exclusion fraction **73.6842%**.
- binary 0/1 values: source n=10,026, retained 8,913, excluded 1,113: exclusion fraction **11.1011%**.
- exclusion risk ratio (descriptive association, not causal): approximately **6.64**.
- exactly 868 of the 1,981 excluded records show this imputation footprint; **1,113 excluded observations have binary wkless13 values**.
Thus an **imputation-only** deletion rule is directly falsified. The stronger claim that a particular external variable is the selection cause is **not established**.

## Prefix-block negative control
Partition original MIT recid by its first three decimal digits (300 to 320 inclusive). All **21** prefix blocks contain BOTH retained and excluded cases. This rejects the simple rule of dropping entire three-digit recid blocks and rejects a single contiguous prefix-only retention cutoff over those coarse blocks. It does **not** reject more complex within-block selection or unobserved merge keys.

## Distinguish causal warrant and source authority
The conditional correlations are reproducible finite calculations on observed source-text rows but do not demonstrate which documentary merge / sample-construction algorithm the original author ran. A good classifier of included records would not by itself reveal the actual protocol. MQR 4.89 already supplies causal nonidentifiability, not a novel theorem of this turn; MQR 4.113 reminds us experiment equivalence and original-source custody differ. 4.119/4.120 J1 (conditional accuracy) does not imply J2 (legitimate authority and revisable decision standards).

## Research direction
Inspect author-side official binary ZIP and original supplementary methods/code to distinguish: local-school-density join missingness, schooling information exclusions, experimental subgroup definition, imputation exclusions, or multiple stages. Look for **original row selection commands/merge-key completeness with verifiable 1,981-ID output**. If no original algorithm survives, define observationally compatible historical mechanisms and maintain a nonidentification result, rather than infer one from association.

## Status
COLUMN10_IMPUTATION_ASSOCIATION_PASS_BOUNDED; IMPUTATION_ONLY_RULE_REFUTED; ID_3DIGIT_WHOLE_BLOCK_RULE_REFUTED; HISTORICAL_SELECTION_PREDICATE_HOLD; OFFICIAL_ZIP_CHECKSUM_HOLD; JTPA_ORIGINAL_ESTIMATOR_REPRODUCTION_HOLD; J2_REAL_REMEDY_TRANSPORT_HOLD. MQR 4.120 ACTIVE/P8; inherited Greenberg/CCQM/Harvest/actual human assessor HOLDs untouched.
