# MQR 5.4 R125 — Reconstructing FinBIF document-level spring-phenology panels from the exact 2024 GBIF occurrence archive

**Date 2026-11-23 KST. Source-pinned result, not a new occupancy theorem. MQR 5.4 OPEN.**

## Source ancestry and correction to R114/R119–R122

The exact earlier archived GBIF download 0031144-240626123714530 ZIP, SHA256 `5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836`, was reopened and scanned. As previously established, its 50-column occurrence core lacks explicit `eventID`, `locationID`, `samplingProtocol`, and `samplingEffort`. **That remains correct but does not mean there is no source hierarchy.** Spring monitoring dataset UUID `acf9b46d-e71a-4ccb-91d2-a021ffda4dd4` has `catalogNumber` linked to FinBIF **Document ID**, with the exact same URI as the prefix of `occurrenceID` before `#Unit…` in **all 14,651** relevant rows. FinBIF's official [record variables](https://luomus.github.io/finbif/reference/variables.html) differentiate Document ID (`catalogNumber`), Event ID and individual Record ID. A Document is **not necessarily one survey event or stable physical site**.

Original first-hand aggregate, [R123 machine-readable original-document receipt](https://github.com/WhoSia/MQR/blob/main/research/data/mqr54_r123_original_finbif_2272_documents_and_2024_weekend_slots.json), independently checked with [R124 original-source SHA-pinned executable](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r124_finbif_document_panel_audit.py):

| Across 2013–2024 records in the original 2024 export | Original source count |
|---|---:|
| Spring records / FinBIF Document IDs | **14,651 / 2,272** |
| Records whose occurrence URI starts with corresponding Document URI | 14,651 |
| Documents containing more than one recorded date | 2,269 |
| Documents containing both ABSENT and PRESENT values | 2,260 |
| Documents with exactly one non-interval PRESENT timestamp | 1,873 |
| Documents with zero such timestamps | 399 |
| Documents with unchanged **exported coordinates** inside document | 2,272 |
| Documents that contain records from more than one calendar year | 0 |
| Published coordinate uncertainty | 10km (917 docs), 25km (177), 50km (560), 100km (618) |

Important date clarification: **2024 is the GBIF archive/download year, not the year of every observation**. The Spring subset includes original observational years **2013 through 2024**, with 2024 only 975 original rows grouped into 131 documents. Actual source-level time series reflect a mixture of campaign years and repeated form slots, not identical ecological site visits. The 2024 original GBIF ZIP was obtained from existing Drive historical custody, not a newly produced GBIF export.

## The 2024 spring schedule: panels of form slots, not proven field visits

| 2024 scheduled weekend | Recorded ABSENT | Recorded PRESENT | Records |
|---|---:|---:|---:|
| Feb 24–25 | 131 | 0 | 131 |
| Mar 9–10 | 130 | 0 | 130 |
| Mar 23–24 | 130 | 0 | 130 |
| Apr 6–7 | 130 | 0 | 130 |
| Apr 20–21 | 126 | 2 | 128 |
| May 4–5 | 79 | 32 | 111 |
| May 18–19 | 45 | 32 | 77 |
| Jun 1–2 | 25 | 4 | 29 |
| **All scheduled-interval rows** | **796** | **70** | **866** |

Correction receipt: R125 initial totals incorrectly summed ABSENT/PRESENT as 771/95 even though each dated row and grand total were correct; R125b fixes the subtotals to 796/70. Do not silently erase the error.

Additionally, **109** original 2024 rows have non-interval source records (generally first sighting). 131 documents total: scheduled slot rows 866 + 109 other rows = 975. The separate derived first-weekend tally in the previous R123 initially said 130; **R123b corrected it to 131** after detecting an otherwise excluded single-row document. This failure and fix are retained, not silently erased.

The 131 documents have scheduled-period slot lengths distributed as 1 record in 1 document, 4 records in 2, 5 in 17, 6 in 34, 7 in 48, and 8 in **29** documents. In the **29 complete eight-slot documents**, first four weekends all have 0 PRESENT; the remaining weekends have 0, 8, 12, and 4 PRESENT respectively. 'Eight recorded slots' is **not equivalent** to eight verified field excursions. Across all 131 documents, 52 have at least one weekend PRESENT and 79 none. Late-slot completion is highly selective (131 early slots vs 29 late), so naive ratio of PRESENT among available records is not a fixed cohort estimate.

## Producer's measurement target and two distinct reporting modes

The campaign's official [instructions](https://luontoliitto.fi/kevatseuranta/ohjeet/) and [current form](https://loydos.luomus.fi/forms/kevatseuranta) distinguish **first observations (Ensihavainto)** from **fortnightly weekend observation/abundance (Kevätseuranta-viikonloput)**. For plants the target is specifically **flowering**; current form labels wood anemone as 'valkovuokko kukkii' and differentiates not observed from observed. The contemporaneous [2024 April campaign report](https://luontoliitto.fi/polyttajat-ovat-liikkeella-vaihtelevasta-kevatsaasta-huolimatta/) mentions first observations plus reports during official monitoring weekends. Thus the same species-name/status in GBIF may compress **phenological flowering / monitoring-slot nondetection**, not an ecological statement that the species truly does not occupy a fixed site.

Form location instructions state that one form is for observations within one **municipality**, and to open a new form if traveling >10 km from the starting area within a municipality. Observers are explicitly encouraged to visit different habitats; precise coordinates are optional and approximate (even a center point of an observation area). This source rule explains why **exported coordinates are constant within a Document without certifying identical physical survey sites**. Caution: the current form is not a version-controlled identical copy of every 2013–2024 form, and 2024 first-hand source form-to-event conversion is not reconstructed in full. Therefore label semantic inference must remain conditional.

## Rivals, limitations and outstanding decisive experiment

**Rival 1 — Ordinary phenology:** A first flowering and a later weekend signal are naturally different events, and the 2024 document panel may primarily encode phenological transitions and how often observers submit reports. This is standard field science, **not an MQR discovery of new biology**.

**Rival 2 — Observation/nonparticipation selection:** A scheduled slot with an ABSENT status might be an actual negative report, an untouched field, or a generated/default value from an upstream form. Current public instructions say not all weekends require field trips and explain both leaving unobserved slots empty (general text) and reporting not observed in a current form. This distinction is unresolved without the original producer's event-/document-level submission flags and effort. The visible raw GBIF 50-column TSV has neither. Do not infer true ecological zero, probability of nonflowering, or independent detection probability from a status alone.

**Rival 3 — Site heterogeneity:** Different habitats within one municipality, 10–100km coordinate uncertainty, geographical/seasonal confounding and survey-selection can explain strong source/date/status associations. No fixed-site occupancy `q` has been identified. 4.97 NAAMP repeated frog visits are a separate actual field-root, not a matched geographic/taxonomic validation.

For genuine Q1/Q2/Q7 innovation, ask a sharply testable question: *Does a source-standardized presence/absence label preserve the same physical observational target, sampling event, and exposure duration when moved into a supervised ML training set?* Pre-register a competing traditional data-quality/occupancy audit and an explicit MQR-specific additional decision. Without actual source producer form-level event facts and the paper's original modeling pipeline, **only bounded provenance and observation-semantics conclusions are licensed**.

**Decision:** Revoke the overstrong interpretation 'no usable grouping information exists' from R114/R119, preserve correct factual finding 'explicit eventID/locationID columns absent', adopt '2,272 FinBIF document-level, scheduled-slot candidates but zero certified same-physical-site revisits'. Do not raise general-Q2 evidence merely from rediscovering ordinary FinBIF document hierarchy. Continue Faraday/Maxwell Q3/Q4/Q5/Q7 in parallel; no 5.5 version promotion.
