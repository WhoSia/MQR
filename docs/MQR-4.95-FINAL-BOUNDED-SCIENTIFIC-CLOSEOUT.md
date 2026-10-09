# MQR-4.95 — FINAL BOUNDED SCIENTIFIC CLOSEOUT

**Author-confirmed name:** MQR-4.95 — Independent Calibration Witnesses, Spatially Dependent Sampling & the Identifiability of Informative Target-Risk Bounds.

**Court date:** 2026-10-09. **Final stage verdict:**
`CLOSED / ORIGINAL 2024 GBIF 29,543-ROW SOURCE-LABEL ORDINAL RECONSTRUCTION PASS / INDEPENDENT SWEDISH SAME-SPECIES PRESENCE–NONDETECTION PASS-BOUNDED / RUST FINITE-TARGET IDENTIFICATION PASS / LEAN FRAME-SCOPE THEOREM PASS / SOURCE-MECHANISM CONFOUNDING IDENTIFIED DESCRIPTIVELY / UNKEYED AUTHOR-ETL IDENTITY HOLD / FINNISH 64-SITE INDEPENDENT CALIBRATION HOLD / SPATIAL POPULATION RISK INFERENCE HOLD / METHOD NOVELTY HOLD`.

**Stop:** 4.95 CLOSED at its originally bounded scientific question. Reauthorization of independent Finland field site risk can move into **4.96**, with an explicitly new scientific estimand and source-mechanism model. Do not prolong 4.95 for repetitive same-root splits, extra cosmetic language or indefinite external data fishing.

## 1. From missing measurements to original-data access

Previous scientific context:
- 4.94 showed NW/KMM risk-estimator ranking was sensitive to admissible geography contracts, but no causal effect of mere geographic distance was isolated; unlabeled target loss remained only partially identified within a wide but sharp finite-score interval.
- 4.95 P1 used a **new Rust-only source fitted logistic model** and retrospective masking of 64 Finnish `Anemone nemorosa L.` labels inside the SAME original Serov publisher CSV; a 32-site score-span audit narrowed a 64-site sharp loss-convex-hull width from 1.411120 to 0.322811 compared with hash-selection width 0.733988. All 64 original labels yield finite oracle 0.656484555903. **Neither source-independent external witness nor population CI.**
- 4.95 P2/P2b read original GBIF parent 27 constituent sources, identified 2024 original `FinBIF Notebook` as an ancestor rather than presumed independent calibration, and found distinct Swedish NFI *Anemone* actual field `PRESENT` and `ABSENT` records. They are an independent observational-source contact but Swedish plots are NOT exact matched Finland 64 target locations. Formal Lean `Nat` frame mismatch lemmas compile; not a theorem of ecological transport.

User explicitly authorized source-root source data recovery, actual 2024 GBIF-ID→publisher `presence` reconstruction with Rust, major original files retained in Drive, and prompt stage handoff to 4.96 rather than re-opening 4.95 repeatedly.

## 2. Historical 2024 original immutable acquisition and custody

The actual historical GBIF original **2024-07-20 occurrence archive still exists**, despite metadata `eraseAfter=2025-01-20`. Original cited GBIF download [0031144-240626123714530](https://www.gbif.org/occurrence/download/0031144-240626123714530) DOI `10.15468/dl.7jsjca`, country Finland, taxon `Anemone nemorosa L.` (`3033263`), year 2000–2024, 27 contributing datasets and 29,543 records. Direct original ZIP `https://api.gbif.org/v1/occurrence/download/request/0031144-240626123714530.zip` returned HTTP **200**, passed `unzip -t`, contains `0031144-240626123714530.csv` tab-delimited **17,894,968 uncompressed bytes** and original explicit `gbifID`, `datasetKey`, `occurrenceID`, `occurrenceStatus`, `decimalLatitude`, `decimalLongitude`, `year` fields.

Original *published Serov author* `egorser0v/Importance-reweighting` commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8` frozen `datasets/species/anemone.csv`: Git blob SHA1 `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`, **7,463,025 bytes**, 29,543 data rows; original author `notebooks/datasets.ipynb` Git blob SHA1 `5d9dc434b2bf7d070f44501b2e97f8ce3abd9ec0`. Author notebook directly reads `anemone.csv` and uses the binary `presence` column, but the pinned upstream repo tree does NOT disclose a standalone original GBIF occurrence ingestion/feature extraction/ID-preserving generation script. Absence of the generator in the pinned public tree is NOT a proof that the authors never had such a script elsewhere.

**Actual full-source preservation:** [Drive original GBIF 2024 ZIP + FULL pinned author `anemone.csv` + publisher notebook + SHA receipts](https://drive.google.com/file/d/1OBJ7DJqNKUH5-GgMX5I10xlyr6erVj3v/view) in existing `02_ANALYSIS_SAFE`, parent `1szynM5kvA7sMExkaJ5sjvwrO3HPaXT1X`, derived from successful read-only CI [37885876228](https://github.com/WhoSia/MQR/actions/runs/37885876228). The source files are **not** merely 3KB execution logs. GBIF license on original download metadata is `unspecified`; retain historical GBIF DOI/collection attribution and do not assume free redistribution rights beyond applicable GBIF source conditions.

## 3. 29,543 original IDs → original publisher binary `presence`: executable result

The original **historical** GBIF raw occurrence download was compared directly with pinned Serov author CSV using std-only Rust source `experiments/mqr-4.95/src/bin/gbif_p3b.rs`. The full raw originals were re-downloaded in CI with Git blob hash check, GBIF ZIP tested and expanded; no synthetic 2026 GBIF observations substituted for original 2024 records.

The author CSV has **23 columns**: `lat,long,presence,year,bio1…bio19`. It preserves no `gbifID`, `occurrenceID`, `datasetKey`, `eventID`, or raw `occurrenceStatus`. The historical raw ZIP has all these IDs/statuses. A positional row-correspondence audit with independent cross-checks of **every row's numeric latitude, longitude, year and binary status** found:

| Original-row comparison (all 29,543) | Result |
|---|---:|
| Raw GBIF records/unique `gbifID` | **29,543 / 29,543** |
| Source datasetUUIDs | **27** |
| Original GBIF `occurrenceStatus=ABSENT` and Serov `presence=0` | **11,166** |
| Original GBIF `occurrenceStatus=PRESENT` and Serov `presence=1` | **18,377** |
| `ABSENT→0`, `PRESENT→1` ordinal class mismatches | **0** |
| Original row-year mismatches | **0** |
| Original coordinate mismatches, after normalizing `NA`↔blank and equal `25`↔`25.0` numeric formatting | **0** |
| Coordinate missing in both original sources | **36 rows** |
| Duplicate identical `lat/lon/year/presence` tuples | **3,031 groups / 15,938 rows**, maximum tied group **117** |

This is **near-complete historic observational source reconstruction**: frozen row sequence together with all shared recorded variables validates `occurrenceStatus=ABSENT→presence0`, `PRESENT→presence1` for **all 29,543** rows. However, because the author CSV itself has no durable observation ID and many rows have identical shared covariates/labels, the **GBIF-ID ↔ individual author row identity is still dependent on the frozen original row ordering**. An independently keyed join from the author CSV to the original GBIF `gbifID` cannot be made from the author CSV alone. The original ETL/feature generation script also remains unavailable. Thus **source status conversion is confirmed on the two original artifacts, but causal proof of every historical ETL operation, ID-retention, or uniqueness of unordered join is not admitted**.

**Final CI [37886218033](https://github.com/WhoSia/MQR/actions/runs/37886218033) SUCCESS**, with original GBIF historical archive and 29,543-row Rust mapping. The first run [37886105430](https://github.com/WhoSia/MQR/actions/runs/37886105430) failed because exact string comparison `25` versus `25.0` treated equal numeric coordinates as different; fixed in commit `95fde5b435e4d7afb3c9f8bf21b13fd5adbd9895`, with independent Rust regression tests. All original source files remain unchanged.

**Reconstructed durable derived data:** [Drive ALL 29,543 GBIF observation IDs, dataset keys, occurrenceIDs → Serov binary labels and 27-dataset 2024 source/status breakdown](https://drive.google.com/file/d/1VzoJYfMnp17cDBKXD3MPLRyJ0-w4YHNy/view) (read-only CI artifact, zipped 573,392 bytes); original sources stored separately. Each mapping row denotes a **positional correspondence supported by exact checked observables**, not an independently preserved publisher-side keyed ID. Full data receipt and Rust tests are archived, not only the manuscript prose.

## 4. New key empirical result: the negative label is almost a collection-source marker

Unlike P2b's current **2026** index query which cannot reconstruct original 2024 label fractions, P3/P3b used the **actual 2024 frozen GBIF raw records**. Therefore the original status composition for the two dominant 2024 source datasets is now known:

| Publisher source in 2024 original | Raw `ABSENT` → author 0 | Raw `PRESENT` → author 1 | Total |
|---|---:|---:|---:|
| Finnish Nature League Spring monitoring, dataset `acf9b46d-e71a-4ccb-91d2-a021ffda4dd4` | **11,165** | 3,486 | 14,651 |
| Kastikka Floristic Archives, dataset `f2e389da-39c3-4f21-8d72-b7d574d924a9` | **0** | 9,686 | 9,686 |
| ALL remaining 25 source datasets combined | **1** | **5,205** | **5,206** |
| **Full 2024 original** | **11,166** | **18,377** | **29,543** |

**11,165/11,166 = 99.991% of all negative labels originate from ONE contributor's monitored non-detections**, not a geographically balanced plurality of independent survey protocols. Almost all other original GBIF datasets supply only `PRESENT` records. This **source-label association** is empirically documented on the original immutable download and is an important caveat for supervised classification, risk transfer and covariate-shift assumptions.

**Not yet identified:** This does **not** demonstrate the classifier *causally* learned a source shortcut, that the dataset is erroneous, that any individual non-detection is biologically false, or that source provenance is the unique cause of a KMM/NW result. Source membership, site ecology, survey effort, collection year, geographic coverage, and label interpretation are potentially confounded. No general population loss or independent Finland direct calibration is licensed. It is also not a new universal theorem.

## 5. Rust and Lean evidence scope

**Rust:** standard library only for all numeric and source-schema matching; Rust court tests cover exact label mapping, missing/numeric coordinates, original source keys and duplicate ID exceptions; P1 finite-target identification/HT capability tests and P2 original parent/independent Swedish source contracts remain preserved. CI content read-only; GitHub commits author/committer human `WhoSia`, never Actions bot.

**Lean 4.24.0:** previously source-frozen P2 abstract theorems in `experiments/mqr-4.95/lean/Mqr495Scope.lean` established (under an explicit definition of admissible target observation receipts) that observations from a mismatched target frame and absent binary observations cannot narrow the finite target admitted-width sum. A matched observation can remove one site contribution; distinct hidden worlds can retain different risks. This formal consistency check does **not** certify real-world site correspondence, GBIF provenance or ecological sampling independence; all P2 Lean CI passed in [37885012021](https://github.com/WhoSia/MQR/actions/runs/37885012021). Original 4.95 P3 Rust reconstructions now expose a stronger **empirical observation-process heterogeneity** that is a suitable 4.96 target, not a reason to pretend Lean solved ecology.

## 6. Final bounded admission, artifacts and successor handoff

**CLOSED PASS:** all complete original author/GBIF source artifacts recovered with hashes and safely archived; full row-order comparison and `PRESENT/ABSENT ↔ 1/0` correspondence is verified for 29,543 records; all 27 actual 2024 source dataset statuses recovered; source-dependent negative-label concentration directly measured; previous Rust sharp label bounds and external Swedish same-species survey confirmed; Lean defined scope court passed.

**HOLD retained:** exact author CSV keyed ID lineage without row-order assumption (GBIF ID column removed), original unpublished GBIF-to-19BIO feature ETL, target Finland 64-site external observation custody/effort matching, source-label conditional shifts identified causally, statistical population coverage/variance, independent Finland target risk calibration, method/theorem novelty.

**User-authorized successor:** close 4.95 now, open **MQR-4.96** to investigate source-origin-conditioned label semantics and scientifically justified calibration transfer. No new 4.95 resampling or source reshuffling to prolong a completed phase.

**Research OS:** this report is GitHub canonical. Append full factual verdict inside **one existing Notion MQR Labs row** `3c8ef561cf92815693b6fcf6de9955f7`; update metadata to `4.95 CLOSED; 4.96 OPEN` only once 4.96 constitution written. Preserve previously displaced 4.84–4.91 documents under the same Lab; no new MQR Labs duplicate row. Original and reconstructed data archived in existing Drive `02_ANALYSIS_SAFE`. Hand-authored GitHub main commits and no bot contributions.
