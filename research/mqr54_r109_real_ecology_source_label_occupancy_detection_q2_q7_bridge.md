# MQR 5.4 · R109 — A genuine 4.X–5.4 bridge under causal limits: dataset-source status versus ecological reality

**2026-11-23 KST · Main version MQR 5.4 OPEN · Prior art respected · Real source-root counts but new analysis derived from already-published MQR-4.95 table.**

## 1. The real original tabulation, not a hypothetical dataset

Source is [MQR-4.95 original 2024 GBIF 29,543-row closeout](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.95-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md), based on a previously acquired original GBIF ZIP, Serov publisher CSV, preserved IDs and 27 root dataset IDs. **This R107–R109 session has not re-downloaded the GBIF ZIP or reverified individual original records.** The following 3×2 is a transcription of a previously audited aggregate, not an independent 29,543-row reanalysis:

| Documented data provider | Recorded ABSENT (0) | Recorded PRESENT (1) | Total |
|---|---:|---:|---:|
| Finnish Nature League Spring monitoring | 11,165 | 3,486 | 14,651 |
| Kastikka Floristic Archives | 0 | 9,686 | 9,686 |
| Remaining 25 source datasets | 1 | 5,205 | 5,206 |
| All 27 providers | 11,166 | 18,377 | 29,543 |

Negative-label concentration: 11,165/11,166 = ~99.991% of all recorded ABSENT instances stem from a single contributor. The recorded absence conditional on provider Spring is 11,165/14,651 (~76.206%); for the other 26 combined, 1/14,892 (~0.0067%). These are **conditional proportions of source-reported records, not population ecological absence probabilities**.

## 2. A source-only diagnostic that one can calculate without inventing ecology

A retrospectively, outcome-informed rule predicts 'ABSENT' for Spring and 'PRESENT' for all other sources. Its exact in-sample confusion table against **recorded publisher labels**: TP=14,891, TN=11,165, FP=1, FN=3,486 (positive = PRESENT). Accuracy 26,056/29,543 ≈ .8819687, balanced accuracy ≈ .9051084, while an all-PRESENT majority baseline is 18,377/29,543 ≈ .6220424. In-sample lift ≈ 25.9926 percentage points. Pearson χ²≈18,239.34 and Cramér's V≈.785737 are **descriptive association** of 3 source groups and 2 *observed* label outcomes, not valid independent-cluster population hypothesis testing or proof of a causal labeling effect.

This score measures **how much status can be accounted for by the source/provider ID in the assembled dataset**. It is not the accuracy of Serov et al.'s trained published model; original model was **not run**. Because the simple rule is constructed after seeing outcomes, there is **no cross-validation, no prospective score and no independent target result**. The absence of originally defined negative observations in two provider groups is itself a reporting/sampling issue. Labelling an occurrence 'ABSENT' is not identical to verified biological absence of a population at a site.

Original official context: [GBIF data quality recommendations](https://techdocs.gbif.org/en/data-publishing/data-quality-recommendations) and [GBIF sampling-event guidance](https://ipt.gbif.org/manual/en/ipt/latest/sampling-event-data). They distinguish explicit nondetections after sampling effort from simply having no species record. Historical source membership, field coverage, effort, geography and site-selection can be confounded; one cannot regress away missing survey events by renaming the label.

**Exact R107 Git source:**
[Source-only 3×2 calculation](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r107_gbif_source_only_label_diagnostic.py). The first commit R107 contained a mistaken confusion-matrix marginal test (`tp+fp==pos`); executing this exact code in a local Python reconstructed file raised `AssertionError`. It was corrected in R107b to `tp+fn==pos, tn+fp==neg`. The corrected Python executed successfully, including two invalid-input controls, and local Git SHA1 matched fetched remote blob `192348568c3794917b5f0a85168cfc54f691e026`. Preserve the initial failure and verified fix as research evidence.

## 3. A mathematically explicit causal identification objection

For the **Spring monitoring** aggregate alone, denote observed reported-PRESENT fraction
r=3486/14651=498/2093≈.237936.
Under a *hypothetical* closed-site model, assume latent true occupancy q, conditional per-attempt detection d, zero false positives, a genuinely surveyed defined sample and independent detections across repeat visits conditional on stable occupancy. Then **r=q d**. Three complete world hypotheses agree *exactly* on the historical one-visit marginal r:

| Hypothetical world | Occupancy q | Detection d | P(next PRESENT \\| first ABSENT) |
|---|---:|---:|---:|
| Low occupancy, perfect detection | 498/2093 ≈ .2379 | 1 | 0 |
| Intermediate | 1/2 | 996/2093 ≈ .4759 | 546306/3338335 ≈ .16365 |
| All sites occupied, lower detection | 1 | 498/2093 ≈ .2379 | 498/2093 ≈ .23794 |

The last column derives from conditional probability:
P(Y₂=1 \\| Y₁=0) = q(1−d)d/(1−qd).
It is a prospective *model-specific* contrast, not an observed outcome or a sufficient test across all possible ecological models. Any environmental movement, detection dependence, selection on the initial report, covariate imbalance, changing sites, or false positives breaks the derivation. **The existing 4.95 row table has not been shown to contain authentic paired repeated survey attempts at the same stable unit**, so its data cannot be plugged into the last column as if measurements were already made. This problem was already studied by occupancy/detection statistics and MQR 4.97; no first theorem is claimed.

**Exact R108 Git source:** [Three-world test](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r108_occupancy_detection_same_margin_worlds.py). Local Python ran source copied byte-identically from GitHub; SHA1 matched remote `15b7ae9d296ab79a3455195386675c9c6fa82e27`. Both controls and all three exact-world equalities PASS. No raw survey sites newly obtained.

## 4. Two strong prior-art rivals and the Q2/Q7 lesson

**Rival A: source selection and ordinary sampling bias.** A highly source-predictive original label is already expected in GBIF aggregations where different providers publish presence-only archives or monitored absences. GBIF's field-protocol guidance directly explains this. Our calculation supports auditing the **target estimand and sampling frame**, not a new unique MQR law. A standard analyst could identify the same nonidentifiability using source-aware cross-validation and occupancy/detection methods. External novelty currently **HOLD**.

**Rival B: true geographic/ecological prevalence shift.** A contributor's areas might genuinely differ in abundance, so a status–source correlation is not automatically label leak or incompatible measurement ontology. Without source-aligned repeated visits and documented effort, geographic/seasonal controls, and common field target, the two explanations are observationally confounded. Do **not** describe source association as causal evidence of model shortcut learning.

**Q2 interpretation:** adopting the same machine-readable `occurrenceStatus` and same `presence` symbol across independent contributor practices can create apparent shared measurement language even when their sampling tasks, absence eligibility and effort differ. This is a **real, bounded illustration of cross-practice reference/measurement mapping**, not a proof of genuinely alien scientific language contact. The difference between *same digital label* and *same measured physical property* is now not only a 4-bit counterexample but grounded in historical real-world source records.

**Q7 interpretation:** a new procedure must expose new information, rather than merely rename an existing status. A documented same-site, same-season repeated survey could discriminate certain q/d worlds; its first value is constructing an observation capable of answering a previously underidentified *specific* question. This is a standard known ecological design; MQR can at most systematize its relation to concept/measurement governance until it demonstrates additional distinct external prediction.

## 5. Prospective falsification plan (NOT APPROVED OR EXECUTED FIELD WORK)

1. Reopen the full held original GBIF + source Spring event metadata, **not only a source-only label table**. Determine which records actually belong to a coherent same-site repeated detection protocol. If no valid repeat IDs, **HOLD** occupancy inference, do not manufacture paired observations.
2. Identify a truly independent target with explicit site ID, taxon, year/season, geo-coordinate and uncertainty, effort, event date, sampling method and repeated independent trials. Specify conditional detection model and missing/censoring before looking at outcomes.
3. Fit prespecified conventional occupancy/detection and source-selection baselines **first**. MQR's distinct predicted warning or design decision must improve on those baselines in a falsifiable heldout case. If the ordinary methods explain the entire finding, **do not claim MQR scientific novelty**.
4. Keep Faraday/Maxwell separate but still active: source historical question is **what newly executable question/discrimination followed from a revised concept**, not whether two printed equations can be normalized to look alike.

## 6. Bounded PI/LIRA judgments (0 to 1)

| Claim / candidate | C support in scope | G generalization | L research value | Decision |
|---|---:|---:|---:|---|
| Original 4.95 source-to-observed-status contingency, transcribed from certified historical work | .98 | .12 | .90 | PASS bounded |
| Retrospective source-only classifier achieves 88.19687% in the SAME source corpus | .99 | .07 | .85 | PASS descriptive, not external accuracy |
| Provider identity caused differences in true species abundance or the Serov classifier learned a source shortcut | .08 | .03 | .34 | HOLD/NO CAUSAL CLAIM |
| Distinct q/d worlds are observationally indistinguishable on one-visit Spring aggregate | .99 | .12 | .93 | PASS synthetic under assumptions |
| The same-site repeated-survey prediction differs among these three stipulated worlds | .99 | .13 | .94 | PASS synthetic prediction only |
| This result is a *new* method rather than existing occupancy/detection and sampling bias | .07 | .03 | .18 | NOVELTY HOLD |
| Q2 can use this as bounded actual source-practice illustration; not as proof of alien translation | .85 | .15 | .92 | KEEP |
| Q7 would require a real new discriminating event/protocol beyond retrospectively recoded records | .87 | .16 | .94 | KEEP |

**Current conclusion:** Most valuable R107–R109 advance is source-anchored **separation of labels, detection process, ecological occupancy and prospective discrimination**, with executable arithmetic and audit-ready provenance. It *does not* earn an independent new philosophical law or field result. Reuse existing 4.95/4.97 literature rather than minting a duplicate Harvest authority fragment. **MQR 5.4 OPEN.**
