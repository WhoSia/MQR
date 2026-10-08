# MQR-4.94 — Final Bounded Scientific Closeout

**Author-confirmed title:** MQR-4.94 — Spatial Dependence, Conditional-Loss Shift, Partial Target-Risk Identification & Geographic Holdout Robustness.
**Date:** 2026-10-09 KST.
**Scientific verdict:** `CLOSED / FIVE GEOGRAPHIC CONTRACTS EMPIRICAL PASS-DESCRIPTIVE / FIXED-PREDICTOR VALIDATION SENSITIVITY PASS / SHARP FINITE-TARGET LABEL-BOUNDS PASS / GENERAL SPATIAL CAUSAL IDENTIFICATION HOLD / METHOD NOVELTY HOLD`.

No further 4.94 experiments are authorized by the existence of this file. The verdict is a **bounded empirical and mathematical result**, not a general-purpose transportability estimator, new theorem or population-level statistical interval.

## 1. Historical question, external original source and ex ante admission

MQR began from UV–Vis: what world-state distinctions an instrumentation/representation chain justifies. 4.91 source-matched ten Matsui cases and forty *within one publication* fitted-fold vs final AUC comparisons; the source-original raster map correlation stayed on Zenodo 502/503/504 HOLD. 4.92 original Serov author-code temporal source-risk contact found a covariate-mean-balance versus actual target-risk ranking disagreement, but never spatial. 4.93 built an original-species WEST/EAST geographic sample with site-level deduplication, verified source author estimator functions, and observed NW closer than KMM on one fixed split; it did not establish spatial independence or why a reweighting estimator erred.

4.94 accepted the user's confirmed title and froze its grid in `docs/MQR-4.94-OPENING-CONSTITUTION-AND-PRECOMMIT.md` **before executing 4.94 analyses**, but AFTER the full 4.93 geographic target loss had already been observed. Its results are *retrospective corroboration/challenge within the same published source*, not independently blinded replication. Original Serov et al. (2026), DOI `10.1038/s41598-026-36740-7`, original repository `egorser0v/Importance-reweighting` Git commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`; `anemone.csv` blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`; `source/estimations.py` blob `9ce9a0c4639bdce4faace03a4b9236e92aa0f446`. This is **one publisher root**. Our longitude-based site split is not the publisher's exact original temporal experiment. Roberts et al. (2017), *Ecography* 40:913–929 DOI `10.1111/ecog.02881`, is direct prior art for spatial blocking and its extrapolation consequences.

## 2. Prespecified four geography cases and one blocked source validation

Same original 2013–2024 finite coordinate/19-BIO eligible Anemone frame, hash-deduplicate to one site row per 6-decimal lat/lon, no labels in location selection; site-hash-selected source model FIT=512, source validation G=64, EAST target=64. Model source-FIT scaler + LogisticRegression C=1.0 with the original author's unmodified MCE/NW, KMM RBF B=10 functions; original KMM directly checked against weighted source log-loss /64, NW against source loss mean. Target labels read after all source estimates and mathematical target-label bounds were computed. Five contracts combine WEST longitude q40 or q50 and EAST q75 or q85; the fifth keeps q50/q75 but uses source FIT from WEST latitude <=65th site percentile and source G from WEST >=80th site percentile (15-point latitude buffer). If infeasible, the design forbade posthoc substitutions.

CI **[37804850478](https://github.com/WhoSia/MQR/actions/runs/37804850478)** SUCCESS with original source and no sample-selection retries; original q50/q75 case numerically reproduces 4.93 NW `0.4587061383023344`, KMM `0.41023871824198993`, oracle `0.7495034100861271`.

| Frozen contract | NW risk | KMM risk | Posthoc target loss | NW absolute gap | KMM absolute gap | Winner |
|---|---:|---:|---:|---:|---:|---|
| WEST q40 / EAST q75 | 0.487212 | 0.410604 | 0.664493 | 0.177281 | 0.253890 | NW |
| WEST q40 / EAST q85 | 0.487212 | 0.428009 | 0.729364 | 0.242152 | 0.301355 | NW |
| WEST q50 / EAST q75 | 0.458706 | 0.410239 | 0.749503 | 0.290797 | 0.339265 | NW |
| WEST q50 / EAST q85 | 0.458706 | 0.447597 | 0.803310 | 0.344603 | 0.355713 | NW |
| WEST q50 / EAST q75; latitude-blocked G | 1.103075 | 0.795898 | 0.899859 | 0.203216 | 0.103961 | KMM |

**Admitted result:** method ordering is **not invariant over these five source/target evaluation contracts**: NW is closer in four ordinary site-hash source validation cases and KMM in the latitude-blocked source-validation case. **These are not five independent results**: same publisher root, overlapping records and, for changed geography, changed target estimands. The blocked G design changes FIT model, source validation G and source geography; the winner flip cannot be attributed solely to the spatial gap.

Source G-to-FIT nearest location distances in the q50/q75 ordinary split: min **0.01861399 km**, median **2.22924 km**, G fraction within 1km **0.265625**, within 5km **0.734375**. Blocked G: min **51.41543 km**, median **91.23028 km**, fractions within 1/5km both zero. Target from source separation remains ~31.50km or more. Geographic distance is not a measured spatial correlation range, so neither design establishes statistical independence. Source/target ecological conditional label mechanisms remain uncontrolled.

## 3. Source FIT/target fixed, source validation only: postresult ablation

Following the first five actual outcomes, we registered another **explicitly post-result** exploratory sensitivity in `docs/MQR-4.94-FIXED-PREDICTOR-ABLATION-PRESEAL.md` to control the confound from different trained models. The **exact same** northern-block experiment FIT512, learned classifier, target EAST P64 and target oracle `0.89985903200522` were retained. Source validation G64 alone changed from the original far-northern spatial block to held-out near-southern sites, still no identical training/validation positions. Original author KMM and NW methods re-executed. CI **[37805160916](https://github.com/WhoSia/MQR/actions/runs/37805160916)** SUCCESS, replays earlier far-G risk and target oracle to numerical tolerance.

| G-only comparison | G nearest FIT minimum/median | Source G positives | NW risk (gap) | KMM risk (gap) |
|---|---|---:|---|---|
| Near southern G | 0.156km / 1.324km | 57/64 | 0.304327 (0.595532) | 0.438598 (0.461261) |
| Far northern G | 51.415km / 91.230km | 28/64 | 1.103075 (0.203216) | 0.795898 (0.103961) |

**Critical interpretation:** With the learned predictor and target held fixed, KMM is closer in BOTH validation cohorts. Thus the initial five-contract winner reversal **cannot solely be identified with G geographic distance**, and it also coincides with changed source FIT/model and validation composition. Even after fixing the model, the G label mixture changes from 57/64 to 28/64 positive, as do time/year and environmental composition. G distance and class prevalence are not independently intervened on. No causal `spatial dependence caused KMM improvement` statement is admitted. The scientific contribution here is the negative identification result, not declaring a winner.

## 4. Mathematically sharp target-label impossibility

For a fixed **64-site target** covariate set, source-fitted model predicts `p_i∈(0,1)`. Without ANY target labels, its realized **finite target log loss** for an arbitrary binary label vector `y` is `R(y)=n^-1 Σ_i [ -y_i log(p_i) -(1-y_i)log(1-p_i)]`. Let `a_i=-log(1-p_i)`, `b_i=-log(p_i)`. Sharp extremes over all binary assignments:
`L_lo=n^-1 Σ min(a_i,b_i)`, `L_hi=n^-1 Σ max(a_i,b_i)`.
Both extrema attain via explicit label vectors, so they are **sharp bounds** for this fixed finite score vector. The entire achievable risk set is *discrete*: `[L_lo,L_hi]` is its tight convex-hull envelope, **not proof of attainment of every intermediate real number**.

Examples of exact first five source/model/target score contracts:
- Original q50/q75: unlabeled sharp envelope **[0.245401, 1.857398]**, width **1.611997**, posthoc oracle **0.749503**.
- Latitude-blocked G: sharp envelope **[0.160355, 2.481105]**, width **2.320750**, posthoc oracle **0.899859**.
The intervals encompass substantially different target risks. This is a **constructive target-label nonidentifiability witness** for each fixed model and unlabeled target X. It does not show those endpoint assignments are ecologically plausible. No label assumptions means broad, often noninformative bounds.

Once the number k of target positives is revealed **posthoc only**, a tighter *retrospective* sharp bound is formed by sorting `d_i=b_i-a_i`: `[(Σa_i+Σ k smallest d_i)/n,(Σa_i+Σ k largest d_i)/n]`. For q50/q75 k=37, **[0.516017,1.349908]**; for latitude-blocked k=37, **[0.626611,1.729774]**. k is unknown in true target-unlabeled deployment: these bands are **not** available prospectively as estimator constraints.

A six-site exhaustive 2^6=64 assignments, including 20 cases with exactly k=3 positives, validated unconditional and prevalence-restricted sharp extrema `PASS` in CI 37804850478. This mathematical fact follows elementary finite optimization and **is not a new theorem in the partial-identification literature**.

## 5. Explicit conditional-loss/calibration shift sensitivities

The original code computes target expected loss bounds under the **extra unverified assumption** of per-site target conditional prevalence q_i within ±η of the source-learned model p_i, η fixed at `0,0.1,0.25,0.5,1`. This assumption concerns expected risk, not realized 64-label sample losses; it is neither source-identified nor justified by KMM covariate mean matching. For original q50/q75 predictions, illustrative conditional *expected-risk* bands:
- η=0: **[0.448101,0.448101]**; identical to the model's own mean predictive entropy.
- η=0.10: **[0.322949,0.609300]**.
- η=0.25: **[0.259723,0.851100]**.
- η=1: **[0.245401,1.857398]**, the label-free outer envelope.
The observed finite-sample oracle `0.749503` exceeding the η=.10 **expected** upper number does **not** by itself falsify the assumption; sampling variation and spatial dependence are unquantified. These are **assumption-sensitivity descriptions, not statistical CIs or prediction intervals**.

In standard loss transport notation, `R_Q-R_{P,w}=E_{Q_X}(m_Q-m_P)+E_{Q_X}m_P-E_{P_X^w}m_P`. No measured summary or KMM ESS here identifies the conditional-loss shift term: that would require additional source/target conditional comparability, independent labeled target data or strong structural assumptions. Covariate-matching and target-risk identification remain different claim types.

## 6. Scientific stop and evidence roots

**PASS bounded:** five fully executed original-author risk comparisons, faithful q50/q75 baseline recovery, explicit source geography proximity diagnostics, a same-predictor G ablation with negative causal interpretation, and mathematically sharp *finite-site* label bounds verified by exhaustive small examples.

**HOLD:** true spatial autocorrelation range/cluster interval, causal attribution to spatial distance rather than changing model or source label mix, conditional `P_Q(Y|X)` transport or target population risk identification, confidence bands with known coverage, sharp population-level risk bounds without sampling/transport assumptions, general NW/KMM ranking, original Serov full paper comparison, unblocked Matsui original map pair correlations, method novelty, and newly independent paper roots.

**Bigger lesson:** Different admissible measurement/validation regimes return different authorized statements, and an unlabeled target cannot adjudicate predictive loss without restrictions on missing target labels. The sharp finite-score envelope is useful for exposing this barrier but not sufficiently informative to license a new risk-correction method. Therefore **4.94 is closed with a scoped nonidentifiability + empirical contract-sensitivity result**, not prolonged for repetitions or decorative polyglot code.

**Evidence custody:** first code `experiments/mqr-4.94/spatial_risk_identification.py`; ablation `experiments/mqr-4.94/fixed_predictor_g_ablation.py`; independent CI runs [37804850478](https://github.com/WhoSia/MQR/actions/runs/37804850478) and [37805160916](https://github.com/WhoSia/MQR/actions/runs/37805160916) SUCCESS. Artifacts (ZIP logs + JSON) preserved in canonical Drive `02_ANALYSIS_SAFE`: five-contract source id `1Qrj5rftHxgTa2Oqg2bw6FSkh28VAvqY0` (5,902 bytes); fixed-model ablation id `1AchEkt2Bg7SZjfVAz7kT586B7qXJcsbz` (2,448 bytes). These are derived-source receipts, NOT the entire publisher raw data.

**Research OS:** all 4.94 semantics must be recorded as headings inside one existing Notion canonical MQR Lab page id `3c8ef561cf92815693b6fcf6de9955f7`; no new MQR Labs row, Notion version child or folder. GitHub default `main` human-authored commits only, Actions `contents:read`, no bot-created commit/push/tag. Future 4.95 does not open merely by this closing file.
