# MQR-4.95 — P2b Post-Discovery Source-Label-Mechanism Audit

**Timing:** 2026-10-09; follows the successful P2 source-root and Swedish independent-field binary tests. This second-stage audit is **post-inspection**, not blind prospective discovery. It is justified by a new observed fact: the 2024 GBIF parent bundles heterogeneous types of occurrence source datasets, not one uniform field non-detection protocol.

**Data source:** LIVE GBIF occurrence search, filtered by original Anemone nemorosa taxonKey 3033263, country FI, year `2000,2024`, and original 27-dataset contributor datasetKey, **NOT** the exact frozen 2024 historical record-level status table. The original 2024 downloaded dataset counts remain from immutable parent metadata.

Two candidate mechanisms to contrast (these are different datasets within one parent download):
- Finnish Nature League Spring monitoring `acf9b46d-e71a-4ccb-91d2-a021ffda4dd4`, 2024 parent 14,651 records; CURRENT GBIF matching records `PRESENT=3670`, `ABSENT=11622`.
- Kastikka Floristic Archives `f2e389da-39c3-4f21-8d72-b7d574d924a9`, 2024 parent 9,686 records; CURRENT GBIF matching records `PRESENT=9862`, `ABSENT=0`.

The sum of source-status counts in 2026 does NOT equal corresponding 2024 historical parent counts: source registries and current GBIF indexes change. Never infer that the 2024 14,651/9,686 rows had identical present/absent ratios, nor that the binary Serov CSV has preserved GBIF source dataset IDs or the correct semantic treatment of each negative. These current live source differences establish **observable cohort-definition/protocol heterogeneity**, not the particular 2024 negative-label cause.

**Precommitted Rust/P2b rule:** read current 4 live query source×status total counts as a new TSV; fail if original listed datasetKeys not in the 2024 parent; report `SPRING_REPORTS_BINARY_P_AND_A`, `KASTIKKA_REPORTS_P_ONLY_IN_FILTERED_CURRENT_API`; both correspond to same taxon/year/country but different observation processes. A deterministic cross-source estimator must not freely exchange negative label semantics without field protocol/custody audit.

**Direct independent Sweden binary source remains PASS under original P2:** Swedish National Forest Inventory collects field observed non-detections, but its sites are Swedish and spatially blurred; Finnish Serov exact 64-site calibration and spatial population inference remain HOLD. 4.95 scientific status OPEN.
