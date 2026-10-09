# MQR-4.99-P2 — Independent Oregon Original Source, Observation-Regime Separation and Retired-Code Dependency Audit

Date: 2026-10-09. This document is a POST-RETRIEVAL forensic source audit, not a blind pre-result preregistration.
STATUS: SOURCE BYTE IDENTITY / PROTOCOL-FIELD CUSTODY PASS; BIOLOGICAL AVAILABILITY GROUND TRUTH, SOURCE-TARGET ECOLOGICAL RISK, GENERAL PARAMETRIC IDENTIFICATION and NEW THEOREM HOLD.

## 1. Source ancestry, original byte and DOI

Kéry et al. (2024), Integrated distance sampling models for simple point counts. Ecology. DOI: https://doi.org/10.1002/ecy.4292. Independent original data and code v1.0: https://doi.org/10.5281/zenodo.10666980, published 2024-02-15.

Canonical Zenodo archive key: kenkellner/IDS-v1.0.zip; original archive size 2,693,380 bytes; MD5 186026a0b887cb2ed953d9030dda836c; independently downloaded original SHA256 279a67cf8c763a1ba5166497ed223ac5feb656b5a6e7f110dae3c0d1a11e001d. Source archive contains 26 entries: four semicolon-delimited CSVs, GIS assets, original R and JAGS scripts, project README, and unmarked package snapshot. Old GitHub location kenkellner/IDS is no longer accessible as a live public repository; Zenodo is the durable canonical origin.

The source is separate from the 2005 Alder Flycatcher source in MQR-4.98. Its true available-bird states are NOT independently observed by an oracle. Dataset identity is not a ground-truth availability license.

## 2. Actual original dataset and author transformation (independent source-byte replay)

| Source/contract | Direct original audit |
| --- | ---: |
| amro_obsdetection.csv, original positive DS rows | 2,090 |
| DS histories with Distance <= 300m (author's newB=0.3 km truncation) | 2,020 |
| DS histories at distance >300m | 70 |
| amro_sitecovs_simplified.csv, DS site-visit rows with zeros | 2,912 |
| Sum of site-table Count | 2,076 |
| Site visits with Count exactly zero | 1,498 |
| Positive DS histories absent from the site-table Checklist_ID key | 14 (all 2011) |
| Site Count vs counted matching DS histories per present Checklist_ID | 0 disagreements |
| amro_ebird_simplified.csv point-count rows | 1,059 |
| eBird count sum | 819 |
| eBird positive checklists | 440 |
| env_centroids.csv rows | 7,227 |

The original author's IDS1_CaseStudy.R sets newB=0.3km and ignores individual distances beyond the cutoff; therefore 2,090 original detection rows versus the paper's 2,020 retained detections are not a field-data contradiction. The 2,076 site counts equal the 2,090 raw histories minus the 14 absent source keys. The paper prose reports 1,060 eBird point counts, while this pinned v1.0 CSV has 1,059; the sum 819 agrees. Preserve the discrepancy rather than fabricate a 1,060th row. The original files must be parsed as semicolon-separated, not comma-separated.

Pinned input SHA-256:
- amro_obsdetection.csv = 274a466d00b5eb58146515cbab76575a69e927c37dec48fdabc1dd1a16a3f208
- amro_sitecovs_simplified.csv = ef047fd2c5ada813f42fbde8f4e5bd4a19ae52e9cb191454c43962df5ab84647
- amro_ebird_simplified.csv = 7505768fe88ac09d597a2ad590f85725c9e69586b3edbe855c566e8a61771307
- env_centroids.csv = 143473ef293852d79c7b1243cf0df8072924602ea545ca681c66a480af690ffc

The original fields and fixed hashes are independently rechecked via Python stdlib and a separate Rust reconstruction. Successful implementation concordance is not an independent biological instrument.

## 3. Four prior-art roles and protocol comparison

- Diefenbach et al. (2007), DOI https://doi.org/10.1093/auk/124.1.96: marked grassland sparrows were independently monitored for singing and visibility during 2002-2003. Available detection events are explicitly grounded in independently witnessed bird behavior. This supports protocol-specific a, NOT species-independent universal a.
- Stanislav et al. (2010), DOI https://doi.org/10.5751/ACE-00372-050103: time-of-detection plus multi-observer design; requires explicit shared availability/observer matching, conditional independence, and time model. Identifying observer perceptibility need not identify availability from positive-only overlap.
- Amundson, Royle & Handel (2014), DOI https://doi.org/10.1642/AUK-14-11.1: first-detection time + detection distance under hierarchical N-mixture/Bayesian specifications. Biological availability, perception and abundance are not separately direct empirical ground truth.
- Kéry et al. (2024), DOI https://doi.org/10.1002/ecy.4292: distance-sampling 5-minute 2011-2014 records, eBird opportunistic stationary PCs 2011-2017, varying PC 3-30-minute duration; original 2011-2013 described protocol versus 2014 rows in v1.0 raw must be preserved. Availability/activity can be fitted under model assumptions but this does not create independent bird vocalization ground truth or guarantee target-population invariance. Their reported 1-minute estimated availability 0.295, 95% credible interval 0.133-0.795, remains THEIR model estimate and is NOT a new P2 calibration.

Observed data regimes must retain distinct definitions of survey area, duration, observer, species, location, year, selection, target population, individual matching and positive/zero encoding. Across-protocol predictive risk is a different estimand from parameter-level detectability; it requires defensible target distribution, outcome/label semantics and positivity/transport assumptions.

## 4. Drive canonical scholarly paper custody (no re-encoding)

The user-provided four PDFs were individually byte hashed before moving them by metadata only from Research OS 00_INTAKE to the central 10_PAPERS location, preserving their original Drive IDs.

- Diefenbach et al. (2007): sha256 551008f2817324158a43675c1064b5f967ee9b6c2e072dda338c46c44264faed
- Stanislav et al. (2010): sha256 4c0b5d1fb44808c18c45276dcf2f190ff2f0c194ab6962f7174ec7b3be298a75
- Amundson et al. (2014): sha256 b029addfba9d95fddde8d5670c127f1de823fad731a98e8c8cb3c3a0aa8e7ad3
- Kéry et al. (2024): sha256 3cbf74ab310afcb1b35b0f50c68072978fcf1e87c6665b413bcbc654b3f21327

## 5. Dependency gate for retiring more GitHub code

MQR main snapshot before P2: 1,216 Git tree entries after prior documented retirement of MQR 4.36–4.40's 29 safely archived files. A first static reverse-reference inspection found direct retained links:
- real-language-ci.yml references experiments/mqr-4.41, mqr-4.52–4.55 and mqr-4.59–4.62.
- real-language-proof-ci.yml references experiments/mqr-4.52–4.55.
- Real-Language uses old-stage named example and regression paths without requiring the corresponding experiment folders to be equivalent or disposable.
- Other old experiment directories and stage-specific workflows may still supply source and proof receipts or independently triggered CI.

Decision: keep every currently referenced folder; keep all not-yet-archived candidates until a complete SHA-verified byte archive plus reverse-reference and CI impact audit permits safe removal. Version age or historical CLOSED status is NOT sufficient. Do not fabricate a new Drive ZIP merely from a tree listing. GitHub main only; bot-authored commits forbidden, work in current human account; no automatic MQR-5.00.

## 6. Judgment

P2 source custody and reconciliation may PASS when the pinned source ZIP is reacquired in GitHub CI, Python and Rust agree, and an artifact is preserved in Drive. The empirical separate true-availability measurement is STILL HOLD. Do not mistake fitting a singing-rate latent variable for verifying an independent physical availability sensor. Next gate: behavior/singing independently watched, or an explicitly sharp partial-identification analysis with measured external calibration and protocol correspondence.
