# MQR 5.4 R114 — Original event-identity gate: 4.95 GBIF versus 4.97 NAAMP

2026-11-23 KST. MQR 5.4 OPEN. This is an audit specification, not a new experimental result.

## Empirically grounded comparison

| Evidence condition | MQR 4.95 Finland 2024 GBIF Anemone | MQR 4.97 USA 2001 NAAMP frogs |
|---|---|---|
| Data ancestry | Original 29,543-row archive audited and preserved historically; **not reopened this turn** | Frozen original frog records checked in 4.97; no new raw collection this turn |
| Individual data rows | GBIF source 29,543 unique GBIF IDs; publisher CSV omits event/source IDs | 337 physical source field visits, same visits observed for two species |
| Sampling unit | Author CSV only lat, long, presence, year, bio1..bio19; site/event keys lost | RouteNumStopNum original key across 130 sites |
| Actual revisits | UNKNOWN: original eventID and locationID completeness NOT yet inspected | 20 sites one visit, 13 twice, 97 three visits, total 337 |
| Scope | Finnish Anemone source heterogeneity, source-only label association | Delaware frog listening observations, different species, setting and year |
| Identification | Biological q and p not identified by status-only aggregate | Conditional repeated-detection model, biological truth still assumption-bound |

## Source standards and strong negative control

[GBIF occurrence download schema](https://techdocs.gbif.org/en/data-use/download-formats) offers eventID, samplingProtocol, effort and other fields as optional occurrence fields; this does **not** certify their presence or non-emptiness in the 2024 exact ZIP. [GBIF sampling-event standards](https://www.gbif.org/data-quality-requirements-sampling-events) describe individual sampling-event identifiers, dates, protocols and event IDs. Same coordinates and year do not mean same physical survey event; a GBIF occurrence ID is not an event ID. [CRAN unmarked vignette](https://cloud.r-project.org/web/packages/unmarked/vignettes/unmarked.html) documents real 2001 NAAMP site-specific repeated records. Neither official schema nor 2001 US frog repeat visits proves Finnish Anemone revisit availability.

## Executable gate

[R112 strict candidate-only field-audit source](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r112_gbif_event_metadata_screen.py) examines original ZIP/CSV rows, counts nonempty fields, enforces distinct gbifID and source dataset, and requires explicit locationID + eventID + complete calendar date + protocol + effort or sample size for a candidate site. It needs two eventIDs with different dates at same original locationID and protocol; cross-site event-ID collisions are flagged. It always sets certified_repeated_site_count=null. Even candidates need external provenance validation of real site, effort, season closure and taxon. Never manufacture repeats by grouping latitude, longitude and year. The expected 29,543 source records can be enforced with a CLI option.

Usage if the precise original ZIP is available: python language/real/experiments/mqr54_r112_gbif_event_metadata_screen.py path/to/0031144-240626123714530.zip --expect-original-29543

Earlier recovered [GBIF 2024 original download page](https://www.gbif.org/occurrence/download/0031144-240626123714530); [MQR 4.95 completed source custody](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.95-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md). Do not replace the historical source with a new 2026 download. The exact ZIP was NOT mounted or reopened this pass. A separate local Python implementation was run on synthetic scenarios with two negative controls. The exact GitHub-committed R112 bytes were NOT yet downloaded and run; no CI pass claimed.

## Causal rivals and success criterion

Source influences geography/season and reporting protocol. True occupancy also depends on geography; recorded detection depends on occupancy plus effort, measurement and selection. Therefore a 3×2 provider/status contingency cannot identify whether provider identity caused any biological effect or whether an original author's classifier learned a shortcut. A real follow-up must locate source-authenticated independent same-site repeat surveys and source/effort documentation. Run standard occupancy, source selection and transport baselines first. A MQR-specific warrant is possible only if it produces a predeclared empirical decision not obtainable from those standards, with matched heldout measurements.

## LIRA 0–1 director decisions

| Decision | C | G | L |
|---|---:|---:|---:|
| Author publisher CSV lacks necessary physical event IDs | .96 | .21 | .94 |
| Original GBIF format permits event metadata; fill rate still unknown | .98 | .26 | .94 |
| Original 2024 29,543 records have verified same-site revisits | .12 | .04 | .08 HOLD |
| NAAMP 2001 130 sites/337 occasions is an actual repeat-survey contrast | .98 | .31 | .89 |
| Check original event fields rather than redo in-sample 88.2% score | .95 | .23 | .94 |
| Protect Faraday/Maxwell question-generation research in parallel | .86 | .18 | .92 |

These are declared director judgments, NOT calibrated probabilities. [R113 evidence-source-family and 0–1 ledger](https://github.com/WhoSia/MQR/blob/main/research/data/mqr54_r113_eventid_siteeffort_lira_scores.json) has six evidence records from four conservatively distinct source families. No new independent data acquired, MQR 5.4 OPEN, authority transferred NONE.