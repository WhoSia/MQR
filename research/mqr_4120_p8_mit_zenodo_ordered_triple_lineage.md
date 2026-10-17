# MQR-4.120 P8 — Cross-Archive Original-Program and Ordered Triple-Lineage Court

2026-10-17 · BOUNDED SOURCE-READ / TRIPLE MATCH PASS_BOUNDED · RAW HASH / TRANSFORMATION HOLD

## Verified upstream code semantics
MIT Angrist Data Archive: https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive ; original ASCII https://economics.mit.edu/sites/default/files/publications/jtpa.raw ; MATLAB https://economics.mit.edu/sites/default/files/inline-files/qeffectsfinal.m . The actual MATLAB file explicitly declares outcome for male/female as jtpa(:,2), randomized assignment as jtpa(:,3), realized training as jtpa(:,4), and sex as jtpa(:,5); separates subsamples and calculates IV quantile-treatment effects at q in [0.15, 0.25, 0.50, 0.75, 0.85]. This confirms numerical column interpretation from primary *code*, not just an author summary.

## Cross-archive full-row ordered test
Retrieved complete public *rendered text* for both source files using Firecrawl (not raw byte download). MIT: 11,204 records × 19 numeric tokens; Zenodo 18836198: 9,223 data rows × 11 columns, plus CSV header. For each Zenodo row the ordered triple (earnings, Z2, D2) was compared to MIT (jtpa col2, col3, col4), respectively. A greedy forward subsequence scan matched **all 9,223 triples in order**. This is stronger than the earlier earnings-only ordered-subsequence match. It confirms a concrete observable correspondence consistent with selecting and augmenting records from the MIT data. It does NOT prove unique row identity or identical data ancestors: repeated identical triples, transformations, or omitted rows can yield more than one matching assignment. No exact per-person join yet, since the Zenodo CSV lacks MIT's first-column original row ID. MIT sample exceeds Zenodo by 1,981 records, but the exact selection/exclusion logic has not been audited. Zenodo metadata 9,224 may include the header; this is plausible, not independently attested.

## Explicit scientific-philosophy genealogy
MQR origin: quotient under observational mapping. MQR-4.89: observationally equal SCMs with different interventions; no causal inference from receipts. MQR-4.101: target unit and error-prone reference restriction. MQR-4.107: observed sufficient data and actual acquisition/stopping history differ. MQR-4.109: statistic sufficiency and documentary physical warrant are separate. MQR-4.111: an intervention can alter the pre-state evidential object. MQR-4.113: Blackwell/Le Cam experiment comparison cannot certify physical quantity/calibration history. MQR-4.119: evaluative rule itself remains challengeable. Current triple match is a **data-lineage positive witness conditional on rendered sources**, not an inference-validating or causal-estimand warrant.

## Remaining discriminating tasks
1. Obtain source literal bytes of MIT jtpa.raw and Zenodo jtpa.csv, verify their checksums and preserve immutable receipts; no raw-byte authentication performed in this turn.
2. Inspect the MIT MATLAB replication functions qregkb.m and quantlsf.m and Han's sequential regime code; original quantitative effects have NOT been replicated.
3. Recover a unique row mapping, if possible, from additional observed covariates; do not call an ordered triple subsequence an original individual-ID join.
4. Obtain and evaluate schooling-density variable provenance, sample exclusion rules, changes in observation definition, treatment positivity and target population.
5. Only then consider design-aware original-sample vs selected-sample estimand comparison. No source transport to actual scientific appellate remedy J2 is warranted.

## Decision
ORIGINAL_PROGRAM_VARIABLE_SEMANTICS_PASS; ORDERED_TRIPLE_SUBSEQUENCE_PASS_BOUNDED (9,223/9,223); UNIQUE_IDENTITY_HOLD; RAW_BYTES_AND_CHECKSUM_HOLD; SELECTION_MECHANISM_HOLD; ORIGINAL_IV_QTE_REPLICATION_HOLD; HAN_POLICY_ORDER_REPLICATION_HOLD; REAL_REMEDY_CAUSAL_TRANSPORT_HOLD. MQR 4.120 remains ACTIVE P8 and all inherited Greenberg, CCQM, Harvest and 4.119 actual-human evaluation HOLDs persist.