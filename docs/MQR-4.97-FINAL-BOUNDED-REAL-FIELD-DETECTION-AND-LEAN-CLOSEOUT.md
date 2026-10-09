# MQR-4.97 — Final Bounded Scientific Closeout

**User-confirmed name:** MQR-4.97 — Detection-Protocol Identifiability, Spatial Observation Footprints & Risk Transport Across Sampling Frames.

**Final ruling (2026-10-09):** CLOSED / INDEPENDENT REAL FIELD REPEATED-DETECTION PASS / RUST TWO-SPECIES OBSERVATION-CONTRACT PASS / VISIT-ORDER NONSTATIONARITY PASS-DESCRIPTIVE / LEAN CONDITIONAL ONE-VISIT NONIDENTIFICATION + TWO-VISIT SEPARATION PASS / LATENT ECOLOGICAL OCCUPANCY AND SPATIAL POPULATION RISK HOLD / FINLAND 64-SITE DIRECT TRANSPORT HOLD / METHOD NOVELTY HOLD.

## 1. Real original source, and one transparently retained failed source

- Original candidate Rhinehart et al. (2025), Dryad DOI 10.5061/dryad.djh9w0wdr, version 413222, actual field archive file ID 4504994, advertised SHA256 9ffb3dac7de8a01b30a46ece1a8702b646db7dad2724a2496fac9d3d4b4516f8; [GitHub original archive attempted CI #37888314998](https://github.com/WhoSia/MQR/actions/runs/37888314998) returned **HTTP 401**. Official Dryad files API requires authenticated access. NO original acoustic raw file was downloaded or used; do not fabricate or claim acquisition. Its metadata and paper are useful context only.
- **Real obtained alternate source**: 2001 Delaware USGS North American Amphibian Monitoring Program (NAAMP) field auditory surveys, recognized original data source in the published unmarked frogs package. Public USGS monitoring program/data release DOI 10.5066/F7G44NG0, unmarked exact git commit fc0c7119d86c53c9e48a4db10ff2170819cd245f. Original source files:
  - inst/csv/frog2001pcru.csv, Git blob SHA1 646002a2d1e829dd59754447b3704b7edca7941f, 9121 bytes, Pseudacris crucifer.
  - inst/csv/frog2001pfer.csv, Git blob SHA1 0f28c4472a2a229b7ca433fc8be2bfa35d1ded47, 9121 bytes, Pseudacris feriarum.
- These two species were observed at the SAME 2001 NAAMP station-visits. Do not count them as two independent source studies, and do not confuse separate curated unmarked CSVs with USGS full 1994–2015 program release. Original package license GPL >=3 and USGS data release CC0 must be acknowledged appropriately.
- The source switch occurred AFTER Dryad file access failure and was precommitted explicitly in [P1A source switch](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.97-P1A-NAAMP-AUTHENTIC-FIELD-REAUTHORIZATION.md); it was not retrospectively presented as blind source selection.

## 2. Exactly what the authentic repeated field visits measure

Original actual field columns: RouteNumStopNum (site key, preserved as string), JulianDate, ordinal species call index (0..3), MinAfterSunset, Wind, Sky, Temperature. Call index 0 means not heard during that listening event; call values 1–3 mean heard. This is NOT direct ecological occupancy.

For EACH of the two species: **337 original field survey records at 130 source sites**, of which 20 have one visit, 13 have two and 97 have three; 110 sites have at least two visits; Julian days 72–179. The 337 visits are the same between species and do not imply 674 independent physical station events. No original coordinates, site footprint polygon, precise site geolocation error bound or probability-sampling inclusion weight are present in these two CSV files. Swedish NFI 10-year vegetation survey revisits and the old Finnish Anemone sites are different observation regimes and cannot silently substitute for within-year NAAMP repeated detections.

| Actual 2001 original observations | P. crucifer | P. feriarum |
|---|---:|---:|
| Ever-heard sites / 130 | 96 | 43 |
| Naive ever-heard fraction | 0.738461538 | 0.330769231 |
| Positive acoustic-call observations / 337 | 140 | 43 |
| Negative acoustic-call observations / 337 | 197 | 294 |
| Within-site next-visit transition not-heard to heard | 4 | 4 |
| Within-site next-visit transition heard to not-heard | 76 | 40 |

Detection was strongly occasion-dependent but this may combine calendar phenology, effort, site selection, observation protocols and other covariates. Do not interpret it as 76 biological extinctions.

## 3. Classical conditional occupancy risk likelihood and boundary diagnostics

Original P1 study was predeclared before seeing NAAMP field values in [original P1 preseal](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.97-ORIGINAL-FIELD-REPEAT-DETECTION-AND-LEAN-PRESEAL.md). Model assumes Bernoulli site occupancy psi fixed across 2001 spring visits, conditional-independent homogeneous p given occupancy, and no false detections. For site i with m_i visits and k_i positives: when k_i > 0, likelihood psi * p^k * (1-p)^(m-k); when k_i = 0, likelihood (1-psi) + psi*(1-p)^m. Rust std-only source fits grid/refined maximum likelihood; this is a CLASSICAL model and estimates remain conditional on unverified assumptions.

| Fitted conditional model, ALL observed sites | P. crucifer | P. feriarum |
|---|---:|---:|
| Homogeneous psi | 0.950600000 | 0.999999990 (boundary) |
| Homogeneous per-visit p | 0.437960000 | 0.127600000 |

The P. feriarum boundary is NOT evidence the species truly occupies all source sites. P. crucifer naive 0.738 vs homogeneous model psi 0.951 is likewise only an assumption-dependent model fit.

The frozen ORIGINAL 100-training-site vs 30-heldout-site FNV hash split (77 heldout field visits, never visits split across the same station) yields full-history heldout NEGATIVE log-likelihood:

| Predeclared P1 contract | P. crucifer | P. feriarum |
|---|---:|---:|
| Homogeneous conditional occupancy psi,p | 51.71976875 | 27.83877412 |
| Independent visit Bernoulli q estimated on all training visits | 51.65821579 | 27.83886092 |
| Independent q estimated on first site visit only | 70.97998838 | 35.77297717 |

Thus the homogeneous occupancy model does NOT improve on the all-visit q predictor for P. crucifer here. Do not present q trained on one visit as a fair same-information comparison; its worse heldout likelihood is an observation about different training information.

## 4. Postdiscovery visit-specific detection diagnostic

After inspecting P1 results, we explicitly wrote [P1B postdiscovery preseal](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.97-P1B-POSTDISCOVERY-OCCASION-HETEROGENEITY-PRESEAL.md) and used the exact same real original sites, fixed train/test split and original visits. P1B was NOT a second blind preplanned trial; it is an exploratory diagnostic motivated by observed detection-order heterogeneity. Rust additional src/bin/visit_order.rs fits (a) one independent recorded detection probability q_j per visit order and (b) classical latent occupancy psi with visit-order-dependent p1,p2,p3 via EM.

| Field visit ordinal | Number of actually sampled sites | P. crucifer positive | P. feriarum positive |
|---|---:|---:|---:|
| First visit | 130 | 95 (73.08%) | 39 (30.00%) |
| Second visit | 110 | 40 (36.36%) | 4 (3.64%) |
| Third visit | 97 | 5 (5.15%) | 0 (0.00%) |

Using 100 training original stations:
- P. crucifer: psi=0.7505498022, conditional p1=0.9726203349, p2=0.5252548159, p3=0.0671555758. 30-heldout-station whole-history negative loglikelihood **33.507229890** vs independent visit-specific q_j **36.948811213**, and old homogeneous psi,p 51.71976875.
- P. feriarum: psi=0.9999999900, conditional p1=0.3100000031, p2=0.0352941180, p3=0.0000000100 (boundary). Whole-station heldout negative loglikelihood **21.739272256** vs visit-specific independent q_j **21.739272252**, effectively identical.

**Critical result:** Repeated visits reveal heterogeneity of the OBSERVED detection mechanism. They can improve heldout recorded-history prediction in a model that allows visit-order p_j (P. crucifer, exploratory). They do NOT automatically identify latent biological occupancy; parameter psi shifts 0.95 to 0.75 just by changing detection contract in one species, while remaining a boundary 1 in the other. Since site selection and visit date differ and source routes cluster, neither survey closure nor independent conditional repeats are proven. This is an observed-data and conditional model contrast, NOT a new occupancy estimation theorem or a statistically validated multi-domain advantage.

## 5. Lean formal scope and geographic footprint

Lean 4.24.0 standard library, no Mathlib and no sorry in experiments/mqr-4.97/lean/Mqr497Detection.lean, verified in final GitHub CI:
- Construct two latent parameter worlds psi=1/2,p=1 and psi=1,p=1/2 with equal one-visit probability psi*p=1/2; under explicitly homogeneous independent repeat detection, the two-visit both-positive probabilities differ 1/2 vs 1/4.
- Silent observation can be true absence or occupied with detection failure.
- A recorder station key that omits exact geographic footprint can represent distinct actual footprints; erasing the footprint makes different source sites observationally equivalent.
- These are constructive finite examples/conditional elementary theorems, NOT a proof that arbitrary field samples identify true occupancy or physical location. The actual NAAMP p_j varies strongly across occasions, so the simple identical-p numerical distinction does not automatically apply to the real data.

## 6. Exact completed execution and custody

Final GitHub CI: [37889026748](https://github.com/WhoSia/MQR/actions/runs/37889026748), both Rust and Lean jobs SUCCESS. Rust main 5 tests and P1B visit-order 2 tests PASS, original source Git blob and content checks PASS, two species field model/result files PASS; Lean proof typecheck PASS. Preserve failures, do not claim they never existed:
- [37888314998](https://github.com/WhoSia/MQR/actions/runs/37888314998) Dryad HTTP401.
- [37888584924](https://github.com/WhoSia/MQR/actions/runs/37888584924) Rust float-literal compile issue.
- [37888643220](https://github.com/WhoSia/MQR/actions/runs/37888643220) P1 Rust and Lean successful.
- [37888911067](https://github.com/WhoSia/MQR/actions/runs/37888911067) second Rust bin selection issue.
- [37888936423](https://github.com/WhoSia/MQR/actions/runs/37888936423) malformed YAML due to an unsafe string-replacement operation; repaired and final CI passed.

All ACTUAL independent USGS NAAMP 2001 original CSV bytes and derived Rust source files, complete field visit receipts, FNV site role, original SHA manifest, P1/P1B training/heldout likelihood logs, and error evidence preserved in existing canonical Google Drive 02_ANALYSIS_SAFE:
- [First complete REAL source and P1 experiment ZIP](https://drive.google.com/file/d/1bU2woFMjvPIsJs-I2V7BRmNRRa2HNKbb/view).
- [FINAL REAL source and full Rust P1/P1B field model ZIP](https://drive.google.com/file/d/1DGgL_7yQUlDqvllox_lHJBA-BQ_L_PPp/view).
- [Lean proved source and execution receipt ZIP](https://drive.google.com/file/d/1_vAOSl-aj9CXgOl26jt4J4NmjctvVypL/view).
The Dryad original field ZIP is NOT archived because authenticated retrieval was denied.

**Scientific verdict:** independently field-collected real repeated auditory detection PASS; true field occupancy outside explicit closure/conditional-independence assumptions HOLD; direct 64-site Finnish Anemone transport HOLD; precise geolocation/footprint and design-based spatial population CI HOLD; new algorithm/theorem novelty HOLD. Reanalysis is source-local, not source-root independent replication across the two frog species.

**MQR-4.97 CLOSED BOUNDED.** Next possible distinct authorized research name (PROPOSE ONLY, do NOT open 4.98 without PI confirmation): **MQR-4.98 — Closure-Sensitive Detection Models, Survey-Effort Transport & the Identifiability of Ecological Risk Across Observation Regimes**. Need additional field data bearing explicit repeat effort or independent closure-season evidence rather than endlessly refitting the same NAAMP observations.

**Single-Lab custody:** Notion canonical MQR one Labs row ID 3c8ef561cf92815693b6fcf6de9955f7. GitHub main human-authored commits and read-only Actions, no bot authored changes; do not create extra Notion Lab or child pages.
