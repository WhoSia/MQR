# MQR-4.95 P2/P2b — Verified Original-GBIF Root Composition, Independent Swedish Binary Field Survey, Rust–Lean Nontransport Court

**Research:** MQR-4.95 — Independent Calibration Witnesses, Spatially Dependent Sampling & the Identifiability of Informative Target-Risk Bounds.

**P2/P2b status:** `CLOSED BOUNDED / LIVE ORIGINAL-PARENT PROVENANCE PASS / EXTERNAL SWEDISH SAME-TAXON PRESENCE–ABSENCE SURVEY PASS / SOURCE LABEL-MECHANISM HETEROGENEITY PASS / RUST 18 TESTS PASS / LEAN 5 DECLARATIONS COMPILED / FINLAND 64-TARGET DIRECT CALIBRATION HOLD / SPATIAL DESIGN-BASED INFERENCE HOLD`.

**Stage MQR-4.95 is STILL OPEN** because no independently field-collected, exact-site, protocol-matched true positive/negative labels for the original 64 Finnish target locations have been established. The positive result concerns a **genuine independent Swedish field-source**, not Finnish-site target calibration. This is an authorization distinction, not failure to locate any real independent ecological observations.

## I. What the original Serov GBIF parent ACTUALLY contains

Serov, Koldasbayeva & Zaytsev (2026), DOI [10.1038/s41598-026-36740-7](https://doi.org/10.1038/s41598-026-36740-7) cites original GBIF occurrence download `0031144-240626123714530`, its original DOI [10.15468/dl.7jsjca](https://doi.org/10.15468/dl.7jsjca). Its live [GBIF parent metadata API](https://api.gbif.org/v1/occurrence/download/0031144-240626123714530) confirms creation 2024-07-20, `SUCCEEDED`, country `FI`, `TAXON_KEY=3033263` (*Anemone nemorosa L.*), year range 2000–2024, `totalRecords=29543`, `numberDatasets=27`. The historical frozen author `anemone.csv` likewise has 29,543 original rows; count equality confirms scope-consistency but not original GBIF ID-level row equality after feature extraction.

The [live original download constituent dataset API](https://api.gbif.org/v1/occurrence/download/0031144-240626123714530/datasets?limit=100) returns exactly **27** original 2024 contributing dataset keys, whose recorded original counts sum **29,543**. The first two contribute 24,337 of 29,543, about **82.38%**. The source family is therefore heterogeneous and heavily concentrated even before examining label provenance.

### Full original 27-dataset lineage (historical 2024 download counts)

| # | Source dataset | Records in 2024 parent | Exact GBIF dataset UUID | Dataset DOI |
|---:|---|---:|---|---|
| 1 | The Finnish Nature League's Spring monitoring | 14,651 | `acf9b46d-e71a-4ccb-91d2-a021ffda4dd4` | 10.15468/v6atsx |
| 2 | Kastikka Floristic Archives (Kastikka Ark) | 9,686 | `f2e389da-39c3-4f21-8d72-b7d574d924a9` | 10.15468/kasmwk |
| 3 | Hatikka.fi observations | 2,308 | `b84a3711-b4ca-4e4f-adac-80dfaea98d1c` | 10.15468/te1t6l |
| 4 | iNaturalist Research-grade Observations | 1,560 | `50c9509d-22c7-4a22-a47d-8c48425ef4a7` | 10.15468/ab3s5x |
| 5 | Lajitietokeskus/FinBIF - Notebook, general observations | 585 | `df12ca07-f133-4550-ab3b-fde13f0e76ba` | 10.15468/4g56tp |
| 6 | LajiGIS: Species mapping and surveys | 301 | `687c05e9-96d6-40e3-b1c9-2e026d0b3fc0` | 10.15468/8ksd56 |
| 7 | LajiGIS: Species monitoring sites | 135 | `887bd779-6454-436f-b1f8-86b70488b59f` | 10.15468/eu3jye |
| 8 | Vascular plant observations of Turku university Herbarium | 110 | `e71a01d8-ab33-4ec4-96db-c3c3f0c5a364` | 10.15468/qjpg5s |
| 9 | Charismatic flowering plants - complete lists | 60 | `2ad36fad-f052-4f91-ad3a-0cecbdfbdf9a` | 10.15468/36r8zr |
| 10 | Löydös Open Finnish Observation Database | 22 | `956bc674-6022-4c52-833e-c5fb39dc837a` | 10.15468/8fzv2j |
| 11 | Botanical Collections of the Åbo Akademi (TUR-A) | 20 | `9f6be6a5-fa23-4471-97c6-67cd21bcf53a` | 10.15468/mpsjrk |
| 12 | TUR Vascular plant collections of the Turku University, Herbarium generale | 18 | `953c46c5-363c-4bcb-a065-86d66f7ffa77` | 10.15468/nsyt4y |
| 13 | Observation.org, Nature data from around the World | 16 | `8a863029-f435-446a-821e-275f4f641165` | 10.15468/5nilie |
| 14 | Vascular plant collections of the Botanical Museum, University of Oulu (OULU) | 14 | `3e44890f-f821-41a9-b09f-de1d22612db0` | 10.15468/2zbay3 |
| 15 | KUO Vascular plant collections (KUO) | 11 | `33484712-7b85-4cf5-9a98-5af51f44c255` | 10.15468/bps4gh |
| 16 | Vascular Plant Herbarium: Herbarium Fennoscandicum | 10 | `a86641c2-9381-4c1e-9d25-32b90f2b5a4b` | 10.15468/ekpyfw |
| 17 | Syke - PEBIHOITO species observations | 8 | `41833398-49a4-4ac7-97b6-c43a3bc60669` | 10.15468/2ct96d |
| 18 | 4th Finnish Bird Atlas 2022–2025, observations from FinBIF Notebook | 7 | `74b866a0-6bed-41f0-83be-f52bf16ad77a` | 10.15468/ndafsa |
| 19 | National Finnish butterfly monitoring scheme (NAFI) | 5 | `181eab51-9399-4baa-a0df-8de01a3acf19` | 10.15468/imsrtd |
| 20 | Bryophyte collection of the Botanical Museum, University of Oulu (OULU) (HERBARIUM UNIVERSITATIS OULUENSIS) | 3 | `711eec60-9b0d-42bc-9610-56604e0d7bd8` | 10.15468/rf55us |
| 21 | Kastikka Floristic Archives (OULU) | 3 | `94adc5b3-1892-432e-b17d-14ebe09d4072` | 10.15468/zy88tm |
| 22 | Vascular plant collections of Iisalmi Natural History Museum | 3 | `bcc660f8-0762-4fbf-80fb-c93890c2f0ee` | 10.15468/rjnu9u |
| 23 | Finnish Insect Database | 2 | `3b301884-51b9-443f-b63c-47feeccfb89f` | 10.15468/jlud8r |
| 24 | TUR Vascular plant collections of the Turku University, Herbarium Fennoscandicum | 2 | `bc27098e-0d4b-49a9-8bbc-64736877ec6f` | 10.15468/5wff5a |
| 25 | LajiGIS: Miscellaneous occurrences | 1 | `128e38cb-9d38-4ecf-989a-1d66175c20e6` | 10.15468/rww9jr |
| 26 | Porvoo Museum / Vascular Plant Collections | 1 | `20cb6dad-e98e-4980-a47b-5d878ea42664` | 10.15468/smnyn3 |
| 27 | Royal Botanic Gardens, Kew - Herbarium Specimens | 1 | `cd6e21c8-9e8a-493a-8a76-fbf7862069e5` | 10.15468/ly60bx |

Specific previously unrecognized source-root collision: dataset `df12ca07-f133-4550-ab3b-fde13f0e76ba`, **FinBIF Notebook general observations**, already contributed **585** *Anemone nemorosa* original-download records. Another 301 + 135 records came from distinct LajiGIS datasets. **Re-downloading from FinBIF or changing portal domains is not independent observation collection by itself.** The 27 original contributor counts belong to **one GBIF download** and must not be promoted to 27 independently drawn field studies.

## II. Actual independent **field-collected observed absence** was found, with a scope barrier

External survey institution: **Swedish National Forest Inventory (SLU)**, dataset [10.15468/b9c3d7](https://doi.org/10.15468/b9c3d7), GBIF original dataset UUID `d59ccafb-251e-46cf-9319-37b58d88e7c5`. The related discontinued 1995–2017 survey-sample dataset UUID is `e1a32bea-73df-4b9b-af2e-6e148ab2641b`. **Both are administered by the same Swedish NFI original field study family**, not two independent institutes and not in the original 2024 GBIF Finnish 27-dataset parent list.

[Swedish NFI original IPT sampling-method metadata](https://www.gbif.se/ipt/resource?r=forestinventory-event) describes a **systematic vegetation plot field inventory** where listed plants are marked `PRESENT` if observed and `ABSENT` if not detected. Survey contains spatially clustered permanent plots, repeated visits and intentionally geolocation-obfuscated field plots (reported **200–1000 m** generalization). Swedish sampling unit = plot/visit, not all ecosystem territory and not an IID specimen. Its recorded `ABSENT` means **non-detection under this survey protocol**, not verified absolute biological absence.

Live GBIF occurrence API filtered on `taxonKey=3033263` and **actual dataset UUID** returned, at audit time:

| Original field sample | GBIF Anemone PRESENT | GBIF Anemone ABSENT | Source field event records |
|---|---:|---:|---:|
| Swedish NFI harmonized current | **3,491** | **32,944** | **36,435** |
| Swedish NFI discontinued supplement | **2,434** | **23,668** | **26,102** |

Both statuses were not inferred from unrecorded plants; actual GBIF-indexed **individual records** were read. Current-survey example occurrenceIDs: `D8395EBA-88D9-4285-B477-7756B98EA771-126` (PRESENT) and `69730867-bafd-44f4-aa27-2345218eaf6c` (ABSENT), each with distinct `eventID`, `recordedBy=NFI Field Team`, documented `samplingEffort=1 day survey of a 100 m^2 area`, `taxonKey=3033263`, `country=SE`, and nonzero `coordinateUncertaintyInMeters`. Original live query receipts include these exact records; no need to download full 692MB DwC-A just to establish real records.

**Scientific PASS:** exact taxon *Anemone nemorosa*, origin at a distinct Swedish field survey, and original standardized **PRESENT/ABSENT** record semantics have actual source contact. The Swedish NFI field collection is distinct from the FI-filtered 2024 Serov parent. **Scientific HOLD:** these records have Swedish field positions, time and effort not matched to the original 64 Finnish target positions; source coordinates also deliberately distorted by 200–1000m. Even one shared species and independently collected field-source do **not** establish target-corresponding label observations, conditional calibration transport to Finnish environmental gradients, or design-based population risk uncertainty. The Swedish current/supplement sets come from one NFI survey family and may contain repeats; the raw filtered occurrence count is not number of independent geographic clusters.

## III. New second-stage P2b observation: source-label mechanism is heterogeneous

The live GBIF occurrence API was separately queried for **two actual constituents** of the original 2024 Serov download under `country=FI`, exact `taxonKey=3033263`, year **2000–2024**, and `PRESENT`/`ABSENT`, in a follow-up precommitted as **post-discovery**, not independently blind:

| Source present in original parent | Current indexed PRESENT | Current indexed ABSENT | Its RECORDS in original 2024 parent |
|---|---:|---:|---:|
| Finnish Nature League Spring monitoring (`acf9b46d-e71a-4ccb-91d2-a021ffda4dd4`) | **3,670** | **11,622** | **14,651** |
| Kastikka Floristic Archives (`f2e389da-39c3-4f21-8d72-b7d574d924a9`) | **9,862** | **0** | **9,686** |

The **current** presence+absence counts do **not** equal the 2024 contributor counts (15,292 vs 14,651 and 9,862 vs 9,686). GBIF source-index content changes over time. Never back-project these current class proportions into the fixed 2024 original author CSV. However, this is a live evidence-based **source-mechanism heterogeneity observation**: two big *same-taxon* sources in the original aggregate expose radically different `occurrenceStatus` availability, so an unexamined mixture of their original rows need not instantiate one homogeneous observed-non-detection measurement design. No causal explanation or particular conversion from GBIF status to the original CSV `presence` has been proven: that requires original `gbifID`, provenance/record lineages and pre-processing source transformation mapping (not retained in the current 19BIO reduced CSV).

## IV. Executed Rust P2 and Lean formal gates

**Preseal:** `docs/MQR-4.95-P2-GBIF-LIVE-SOURCE-AND-LEAN-PRESEAL.md`; post-discovery original-contributor comparison `docs/MQR-4.95-P2B-LABEL-MECHANISM-PRESEAL.md`.

**Rust:** new std-only binary `experiments/mqr-4.95/src/bin/gbif_p2.rs` receives live GBIF API metadata and actual representative record values. The GitHub Actions read-only workflow fetches JSON from GBIF unauthenticated GETs, `jq` projects structured API data to TSV (transport only), then Rust enforces: original parent UUID/date scope 27, original sum 29,543, contributing datasets' UUID identity and FinBIF root reuse; independently sourced Swedish status counts, real observationID/eventID and source taxon, country, sampling effort and geographic obfuscation; source-specific current two-mechanism contrasts; and typed verdict that externally observed Swedish records **cannot** be relabeled as 64 Finnish-site calibration. Full live raw JSON snapshots and derived Rust scientific receipts are archived. No Python experiment was used.

**Lean:** `experiments/mqr-4.95/lean/Mqr495Scope.lean` on Lean 4.24.0, no Mathlib dependencies, no `sorry`. Five named lemmas/theorems type-check:
1. `unmatched_frame_keeps_target_uncertainty`;
2. `missing_binary_label_keeps_target_uncertainty`;
3. `matched_observation_removes_exact_contribution`;
4. `distinct_unknown_label_worlds_same_observed_data`;
5. `audited_every_site_zero_residual`.

**Very important proof limit:** These are formally checked theorems about an **explicit abstract gate** and a `Nat` list of nonnegative remaining width contributions. They are not mathematical proofs of real-world ecological collection independence, all floating-point logloss inequalities or transport bias, and not new mathematics. Lean cannot infer that a Swedish `eventID` corresponds to an actual 64-site Finnish source risk observation when the site correspondence is absent.

**Successful integrated CI:** [GitHub Actions 37885012021](https://github.com/WhoSia/MQR/actions/runs/37885012021), **two jobs SUCCESS**, Rust 13 prior unit tests + 5 new GBIF binary/custody tests = **18 passing tests**, real source outcome PASS, Lean proof build PASS. Earlier [37884724410](https://github.com/WhoSia/MQR/actions/runs/37884724410) had Rust PASS and Lean PASS after correcting missing Lake manifest, and initial [37884640841](https://github.com/WhoSia/MQR/actions/runs/37884640841) preserved the missing-manifest failure. Intermediate P2b Rust runs failed while a fifth CLI argument was being integrated with the workflow; preserved and repaired. P1 workflow's explicit binary flag prevents extra Rust binary from breaking the earlier court. CI wrote **no bot-authored commits**.

**Immutable evidence receipts:** [Live GBIF Rust original source and record snapshots ZIP](https://drive.google.com/file/d/1z5ME4IJGR5Loutql4oGKvT50q4iGMSK2/view) and [Lean proof/check ZIP](https://drive.google.com/file/d/1d-wak_DBXjEm3t4AC1C6xKKIvP9QE1Ce/view) are the initial P2 passing copies (before added P2b). The **final combined P2b receipts**, each archived in the existing Drive `02_ANALYSIS_SAFE`, are [Rust live original GBIF/Swedish/heterogeneous-source JSON and verdict ZIP](https://drive.google.com/file/d/1Ge9zoHC8oUeGJ21OH5bJJe2QdW9hyAsJ/view) (22,935 bytes, GitHub artifact 11595069807) and [Lean target-frame proof/build ZIP](https://drive.google.com/file/d/1MSMoU4xLzo2ofYEo1lCDFL6JkJLkiA1Q/view) (1,367 bytes, GitHub artifact 11595737881). Earlier P2 receipts remain to document the initial successful scientific contact. Earlier P1 evidence `1vqbO4kcSAAiQrP1ksrBh4_U7hUsJWQFz` remains, same parent folder id `1szynM5kvA7sMExkaJ5sjvwrO3HPaXT1X`.

## IVa. Stronger independent survey-protocol criterion and Finnish-field-source candidate (bibliographic gate only)

The GBIF official [Guide for publishing biological survey and monitoring data](https://docs.gbif.org/guide-publishing-survey-data/en/), section 5.5.3, and [GBIF IPT Sampling Event Data manual](https://ipt.gbif.org/manual/en/ipt/latest/sampling-event-data) both make the **taxonomic sampling scope** a necessary part of legitimate negative-observation interpretation. A plant's absence from an arbitrary opportunistic occurrence table is **not** evidence of an observed `ABSENT` label. To use a standardized plot survey, the intended taxon must have been within the surveyed checklist and detection window, with an explicit recorded `occurrenceStatus=absent` (or a fully documented complete-taxon-scope event permitting reconstruction). This bolsters, but does not extend, the Swedish NFI's observed `ABSENT` contact: those records mean non-detection under a specified protocol.

A potential truly **Finnish** candidate is the Natural Resources Institute Finland (Luke) [Multi-Source National Forest Inventory of Finland — methods and results 2017/2019](https://jukuri.luke.fi/items/77a14c6e-06ce-469a-ba03-047f7e24e530), which states that its remotely sensed/model-derived product is tied to field data from the 11th–13th Finnish National Forest Inventories (2012–2019). **Current scope gate:** this report does not, on its own, release independent *Anemone nemorosa* target-matched true binary field non-detection at Serov's selected 64 Finnish sites or its exact sampling-event roster and inclusion probabilities. An aggregate inventory map, vegetation model or Excel summary is NOT an admissible site-by-site independent loss calibration label. Treat Luke as a *candidate institutional acquisition/contact route*, not an accomplished target-witness.

## V. Scientific admission and outstanding discriminant

**P2/P2b CLOSED BOUNDED:**
- `ORIGINAL_GBIF_PARENT_27_SOURCE_COMPOSITION_PASS`.
- `ACTUAL_DISTINCT_SWEDISH_FIELD_STUDY_ANEMONE_PRESENCE_ABSENCE_PASS`.
- `GBIF_CONTRIBUTOR_LABEL_MECHANISM_HETEROGENEITY_PASS-DESCRIPTIVE`.
- `RUST_SOURCE_CONTRACT_PASS`.
- `LEAN_ABSTRACT_FRAME_NONTRANSPORT_PASS`.

**HOLD without promotion:**
- `DIRECT_MATCHED_FINLAND_64_SITE_INDEPENDENT_CALIBRATION_HOLD`.
- `ORIGINAL_2024_SOURCE_RECORD_ID_TO_SEROV_PRESENCE_FLAG_MAPPING_HOLD`.
- `FINLAND_SPATIAL_TARGET_POPULATION_DESIGN_BASED_INFERENCE_HOLD`.
- `SOURCE_INDEPENDENCE_OF_SWEDISH_SUBSAMPLES_AND_TEMPORAL_PANEL_RISKS_HOLD`.
- `NEW_ALGORITHM_OR_GENERALIZATION_THEOREM_NOVELTY_HOLD`.

**One next real experiment (4.95 still open):** obtain the original 2024 GBIF download archive/IDs or the source R script generating `anemone.csv`, trace `presence=0/1` against source datasets' original `occurrenceStatus` and collection/protocol. A genuine separately observed Finnish presence/non-detection source with target-compatible frame/precision/effort would be another path. Both are missing before claiming native Finland risk calibration. Do not repeat same-root geographical re-splits or treat Swedish data as geographically aligned merely because its taxon is correct.

**Research OS:** canonical ONE Notion MQR Lab page `3c8ef561cf92815693b6fcf6de9955f7`, no additional Lab row/child page; GitHub `main` human-authored commits, Actions `contents:read`, no bot-generated commit/push/tag.
