# MQR 5.4 R120 — An empirical information-loss boundary in the archived 2024 GBIF occurrence core

**2026-11-23 KST | status 5.4 OPEN | original source SHA verified and 29,543 original rows actually inspected.**

## Source, custody, and exact executable verification

Recovered the **already archived** 4.95 P3 bundle from connected Drive ID `1OBJ7DJqNKUH5-GgMX5I10xlyr6erVj3v`, which yielded a mountable outer ZIP, nested original-source tar.gz and the **actual historic 2024 GBIF ZIP** `original-author-source/GBIF-2024-0031144.zip`. Exact original source SHA256 **5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836** matches the original immutable 4.95 source manifest. Uncompressed internal TSV `0031144-240626123714530.csv` had **29,543 records and 50 header columns**, 27 dataset providers, 11,166 ABSENT / 18,377 PRESENT statuses. The original pinned Serov author CSV also survived in the bundle; its hash is **35b7195ee19b8087497eb44fe4e47c8676376d2a6aad2ad94e4bd3091b2f3d0c**. Its published 23 columns retain geographic/year and model climate features but **not eventDate, eventID or sampling effort**.

GitHub original R112 checker copied into the local Python runtime and verified by `git hash-object` **246a08fab3b4cb20ff50e32f043a7839fe2c310c**. Original self-test initially PASS but an adversarial date `2024-13-01` generated a false repeat-site candidate. That is a **real source code bug** discovered through exact-byte runtime test. R118 repaired calendar validation, malformed TSV/header detection and status input checking, with **6 negative checks**, and the corrected exact local Git SHA **0af526a272418bda6bf8e10e9a55b3c6579169c9** matched the updated remote commit. Corrected R118 then **ran on the actually extracted original 2024 ZIP** with the enforced 29,543 record count, not a synthetic reenactment. Output was row count 29,543, provider count 27, correct status counts, and:

| Occurrence-core field | Present in historical 2024 original? | Nonblank rows |
|---|---|---:|
| gbifID / occurrenceID / datasetKey | YES | 29,543 each |
| occurrenceStatus / eventDate / year | YES | 29,543 each |
| decimalLatitude and Longitude | YES | 29,507 each |
| **eventID / locationID** | **NO SUCH COLUMN** | 0 |
| **samplingProtocol / samplingEffort** | **NO SUCH COLUMN** | 0 |
| **sampleSizeValue / sampleSizeUnit** | **NO SUCH COLUMN** | 0 |

Consequently **strict explicitly documented repeat-site candidates = 0; certified repeat-site count = unknown/null**. A zero of *identifiable candidates* is **NOT proof that actual sites were never revisited**. Upstream Spring-monitoring event tables may exist outside this exported GBIF occurrence ZIP; they have NOT been found here. [Machine-readable exact receipt and 50-field inventory](data/mqr54_r119_original_gbif_2024_source_eventdate_29543_receipt.json).

## New original observed temporal encoding table: date notation and recorded label

| EventDate syntax in 2024 original | ABSENT | PRESENT | Sum |
|---|---:|---:|---:|
| ISO-8601 date **interval with slash** | **11,165** | 3,012 | **14,177** |
| ISO timestamp (with time, no slash) | 1 | **15,325** | **15,326** |
| Standalone YYYY-MM-DD date | 0 | 40 | 40 |
| **Total** | **11,166** | **18,377** | **29,543** |

All **11,165 absent records from Finnish Nature League Spring monitoring** are interval-coded. Its 3,486 PRESENT records comprise 1,613 intervals and 1,873 timestamps. The one remaining ABSENT from another provider is timestamp-coded. Of 14,177 slash-delimited intervals, 12,941 have exactly a 1-day recorded timestamp span; 1,236 span more than one day, including 243 with span at least 365 days. **Neither a one-day timestamp interval nor its two endpoint timestamps proves two independent site visits.**

Standard temporal interpretation: [GBIF temporal processing](https://techdocs.gbif.org/en/data-processing/temporal-interpretation) describes slash-delimited ISO intervals, and [Darwin Core eventDate definition](https://dwc.tdwg.org/terms/) defines it as the time or interval *during which* an event occurred. Thus all these records have `eventDate` values but it is **false** to infer that every eventDate is a unique single-day survey visit. For R112, the strict event/site/effort missing columns alone are sufficient to fail its candidate gate. A separate date-only parser must not silently reinterpret interval start/end as two site visits. A timestamp does not prove independent biological discovery either.

The historical source has **1,824 groups / 6,007 rows** sharing contributor+coordinates+the same full original eventDate string, and **2,283 groups / 16,782 rows** sharing contributor+coordinates+year, with largest same-year group **149 rows**. These are duplicates of a *descriptor*, not proof of biological repeat observations. No physical site identity, visit independence or season closure can be inferred from them.

## Can date notation predict recorded absence?

**Only as a retrospective in-sample association**. Choose `ABSENT` for `eventDate` containing slash, `PRESENT` for timestamp or single date. On *these very same original 29,543 records*:
- True PRESENT predicted correctly: 15,365.
- True ABSENT predicted correctly: 11,165.
- One recorded ABSENT miscalled PRESENT; 3,012 recorded PRESENT miscalled ABSENT.
- **26,530/29,543 = 0.8980131 (89.80%) apparent accuracy**, compared with previously source-only in-sample 26,056/29,543 = 88.20% and majority-PRESENT baseline 62.20%. It is **not** independent validation, causal identification, genuine ecological prediction or an original author machine-learning model result.

Critical falsifier: the author's released `anemone.csv` has **no eventDate column**, hence this date-format rule **cannot be attributed to the original fitted Serov model as a used feature**. It is a *metadata provenance diagnostic* available only by revisiting the archived raw GBIF source.

This exact documented date-format/source-label association strengthens MQR's narrowly scoped Q1/Q2 measurement-language warning: two data-origin practices mapped into the same standard `occurrenceStatus` may imply different sampling-time semantics; yet even this association does not reveal true occupancy or a unique scientific ontology.

## Two live rival explanations, explicitly retained

1. **GBIF/TDWG routine processing and source-protocol variation**: many observers correctly use interval `eventDate` for an assessment period while sightings are timestamped. This is ordinary standard-compliant reporting, not automatically a data error, methodological novelty, or model cheating. [GBIF documentation](https://techdocs.gbif.org/en/data-processing/temporal-interpretation) is explicit.
2. **True geography and temporal selection**: source-differential covariates and sampling frames could produce real ecological prevalence differences; date encoding and source labels are confounded. The 29,543-record association alone cannot isolate any individual causal pathway.

Next meaningful validation must identify original **event-core** or survey source archive with stable site IDs, effort and recording process; the 2024 **occurrence-core** export lacks these identifiers. A *new* GBIF export would not be an exact substitute for the pinned historical source. If event tables cannot be recovered, issue a documented HOLD on 4.95 ecological occupancy, rather than fabricating revisit histories from coordinates and dates. Other 4.X real field results (4.97/4.98) remain valid **within their own physical source roots**, not independent Finland 2024 verification.

## Scientific and governance verdict

- **Actual new forensic result**: sample-source date-format/recorded-status association and concrete **lack of event/site/effort columns in the complete recovered 2024 original**; reliable source SHA and code execution receipt.
- **Not achieved**: new ecological field measurement, individual-level occupancy identification, original Serov model causal shortcut evidence, independently new identifiability theorem, or universal Q2/Q7 mechanism.
- Preserve 5.4 OPEN. LIRA must score high local original-source warrant and **low generalization/novelty warrant**, not inflate G because source-raw access improved.
