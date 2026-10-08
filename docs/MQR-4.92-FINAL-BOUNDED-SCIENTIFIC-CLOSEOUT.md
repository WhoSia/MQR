# MQR 4.92 — Final Bounded Scientific Closeout and Original-Data Discordance Receipt

**Date:** 2026-10-09 KST. **Formal title (author-confirmed):** MQR-4.92 — Cross-Study Evaluation Contracts, Spatial Prediction–Performance Discordance, Source-Root Dependence & Falsifiable Evidence-Repair Benchmarks.

**Scientific verdict:**
`CLOSED / INDEPENDENT SOURCE CONTACT PASS-BOUNDED / TEMPORAL RISK–FEATURE-BALANCE DISCORDANCE PASS-DESCRIPTIVE / SPATIAL-MAP CONTACT HOLD / METHOD NOVELTY HOLD`.

This is a bounded terminal scientific receipt for the **same existing MQR research version**, not a new Notion Lab or child page. A successful CI run is not a philosophical result. Closure means the research question has been given a defensible finite disposition with preserved negative evidence, not that every goal in the opening constitution was achieved.

## 1. Inherited question and historic constraints

The founding MQR question began with UV–Vis/circuits and whether an instrument-mediated representation licenses any assertion about unmediated states. The later quotient/identifiability/authority genealogy treats measurement-induced distinctions as *claim-relative*, never an ontic totalization. Historical source: MQR Origin & Drift Audit, Notion page `3c8ef561cf9281dbb35df667343ed15a`. Earlier 4.90/4.91 taught that independent files and fitted models do not imply independent study roots. The original Matsui 2026 `Ecology and Evolution` source root yielded 10 original external target AUC reproductions and 40 matched fitted-fold vs final contrasts; all came from **one publication root**, not 40 independent studies. Original Matsui raster map agreement remained empirically blocked by repeated Zenodo HTTP 502/503/504. 4.91 bounded closeout is `docs/MQR-4.91-FINAL-SCIENTIFIC-CLOSEOUT.md`.

4.92 source-independent publication was Serov, Koldasbayeva & Zaytsev (2026), *Kernel mean matching enhances risk estimation under spatial distribution shifts*, `Scientific Reports`, DOI `10.1038/s41598-026-36740-7`, original author GitHub `egorser0v/Importance-reweighting`, immutable upstream commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`. Matsui rank AUC and Serov risk/loss are different mathematical estimands: no numeric pooling, inferred meta-effect, or alleged population-equivalent cross-paper replication.

## 2. Independent author-code and original-data admissibility

Original source `source/estimations.py` blob `9ce9a0c4639bdce4faace03a4b9236e92aa0f446` checked before executing unmodified original MCE/KMM/QP functions; synthetic numerical smoke CI [37793832383](https://github.com/WhoSia/MQR/actions/runs/37793832383) SUCCESS. Synthetic fixed fixture KMM underperformed unweighted source risk; it was **not** original paper-number replication. Three original active species CSVs were hash-checked and year×class×19-BIO missingness audited, CI [37794756586](https://github.com/WhoSia/MQR/actions/runs/37794756586), [37795655846](https://github.com/WhoSia/MQR/actions/runs/37795655846) SUCCESS.

The original inactive `oxalis.csv` has 7,507 rows, all observed `presence=0`; its token is *not* Matsui's Oxalis species/population identity. Earlier than 2013, complete climate+label source samples for all three active species had no class 0. The original Anemone source-only split attempts therefore failed first through insufficient complete cases (758 < planned 1200), then through absence of a second class, **before any target risk reveal**; these are retained as true failures, not overwritten by a retroactive success.

A third source-only prespecified design uses the original author `anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`, all 19 original BIO feature columns, original observed labels, fit 2013–2018 (512 sampled), source validation 2019–2020 (64), temporal target oracle 2021–2024 (64); source-only scaler and fixed logistic regression C=1.0. Target labels are forbidden from fitting, weight choice or source risk estimation and used only for post-hoc loss oracle. The temporal split is not the published authors' protocol and does NOT test spatial generalization. CI [37796041048](https://github.com/WhoSia/MQR/actions/runs/37796041048) SUCCESS.

- Target held-out oracle mean log-loss: **0.9844141078434838**.
- Original author unweighted source estimator MCE/NW risk: **0.9084266190158496**; oracle absolute gap **0.07598748882763418**.
- Original author KMM risk: **0.4249084025150559**; oracle absolute gap **0.5595057053284279**.
- KMM normalized weight effective sample size: **5.485779506094814** for 64 source validation observations; highly concentrated weights.
- Exact author KMM risk was independently checked against original weighted source-loss dot product. This is a **one-split original-data negative result** for a universal algorithm-dominance narrative, not refutation of Serov's original published aggregate claims.

## 3. Within-version, after-prior-reveal source-only weight diagnostics

After viewing the first original-data outcome, a **conditional follow-up** was prospectively specified for its own weight transformations in the same canonical MQR Notion root. It is not independent confirmation, nor blind to the earlier KMM-vs-NW loss gap. Immutable source/data/split/fitted model/unmodified upstream functions are retained. Only the diagnostic variants clip original KMM weights using **source-only** 90%/95% weight quantiles and renormalize weights to sum to 64; neither is called original KMM. The target-label oracle is calculated only after the fixed diagnostic estimates and summaries have been computed. New code `experiments/mqr-4.92/serov_anemone_weight_sensitivity.py`; CI [37798943621](https://github.com/WhoSia/MQR/actions/runs/37798943621) **SUCCESS**, log contains `MQR492_WEIGHT_DIAGNOSTIC=PASS`, original MCE/KMM numeric concordance and exact weight-change absolute risk shift bounded by `max(loss) * L1(weight_change)/64`.

| Estimator/diagnostic | ESS | Mean abs standardized BIO-mean imbalance | Held-out oracle absolute loss gap | Source risk |
|---|---:|---:|---:|---:|
| Original author KMM | 5.485779506094814 | 0.6317018748082613 | 0.5595057053284278 | 0.424908402515056 |
| Original author unweighted | 64 | 1.6654618369521899 | 0.07598748882763462 | 0.9084266190158492 |
| Diagnostic source-only clip p90 | 8.150691681747944 | 0.7966227447750217 | 0.32386581283196514 | 0.6605482950115187 |
| Diagnostic source-only clip p95 | 6.941002877956322 | 0.6990685465276177 | 0.2959847930475302 | 0.6884293147959536 |

**Empirically defensible discordance:** original KMM substantially reduced the *declared first-moment standardized BIO-feature imbalance proxy* relative to unweighted source validation, while making held-out target risk estimation much worse. Both weight caps increased ESS and reduced the oracle gap relative to unmodified KMM, but did not surpass unweighted source risk. Further, p90 produced a larger ESS than p95 while yielding a *larger* oracle gap. This is a descriptive example of (i) proxy-feature balance versus target loss ranking disagreement and (ii) ESS improvement failing to enforce monotone risk accuracy. It is **not** empirical proof of a conditional label-shift mechanism, causal contribution of ESS, statistical significance, a better algorithm, or published KMM failure.

Mathematical failure boundary: for a predictor and loss, with `m_P(x)=E_P[L|X=x]`, `m_Q(x)=E_Q[L|X=x]`, and normalized weighted source marginal `P_X^w`,
`R_Q - R_{P,w} = E_{Q_X}[m_Q-m_P] + (E_{Q_X}[m_P]-E_{P_X^w}[m_P])`.
This identity needs well-defined conditional expectations/integrability. Matching source/target X means or even their full marginals cannot control the first term unless a conditional-loss invariance assumption holds; exact population density-ratio correctness is not established by a finite KMM proxy. The decomposition is standard covariate-shift reasoning, **not a new MQR theorem**.

## 4. Adversarial evaluation-contract comparator and methodological nonadmission

CI [37794048359](https://github.com/WhoSia/MQR/actions/runs/37794048359) SUCCESS on **20 stipulated constructed mutations** (4 admissible, 16 inadmissible) of schemas motivated by Matsui and Serov. Weak filename+metric baseline false-admitted 15; metadata-only baseline 12; full typed field matcher 0 on the specifically chosen cases. The labels are **stipulated**, not independent human or real source audit verdicts. Some fixtures use a schematic `oxalis` token despite the actual Serov `oxalis.csv` being inactive/one-class; no such fixture is allowed to claim it represents a fully admissible *real* Serov case. Comparators are deliberately weak, not the best existing manual/domain-practice rivals, so no novelty, scientifically validated repair advantage, or general error-rate superiority is admitted.

## 5. Failure, remaining uncertainty and authority ceiling

**PASS (bounded):** truly distinct publisher source root and hash-verified original source functions/data, independent source function numerical checks, honest source-feasibility failures, source-original one-split real target risk counterexample, and executed conditional sensitivity diagnosis that exposes proxy-risk discordance.

**HOLD:** full original Serov author-table replication; actual Matsui spatial map correlation (Zenodo original-source availability failures); comparable real spatial holdout; source feature coordinate-axis audit; independent root-level interval/generalization with n=2 distinct study roots but incompatible estimands and designs; causal mechanism for KMM error; algorithm superiority; serious external audit-baseline comparison and blinded human audit; globally minimal evidence repair, cross-study pooled causal/transport effect, new transportability theorem or final ontology.

**Research judgment:** The strongest contribution is a *source-replay-grounded negative discrimination* showing where superficially compatible representations or improved covariate-balance proxies fail to identify target performance. It is an instance of measurement-mediated scientific warrant, not a new general-purpose correction algorithm. Preserving explicit scoped HOLD is a scientifically legitimate bounded closure. Further repetitions of essentially the same single case without new independent source/space-dependent data or a genuine strong rival should not prolong 4.92.

## 6. Source and receipt custody

- Existing final 4.92 study risk court: `docs/MQR-4.92-FIRST-INDEPENDENT-SOURCE-AND-RISK-COURT.md`.
- Existing GitHub original evidence and four Drive ZIP receipts in the canonical MQR Drive `02_ANALYSIS_SAFE`: IDs `1_nELQEPNIq8XnXhLm5J0mXi93eaobaTS`, `1EPzX88O4b_wTB-RalQWAxp7Ya7z1Lm_b`, `1VWZSq4qNPLoYiVBu11pweKqLbzTihO0p`, `15douq9UXvqf7b29-vaEK1JP4n9LmvoL1`.
- New diagnostic code commit [c41f9c48](https://github.com/WhoSia/MQR/commit/c41f9c48bc0ee1e8cbd05af5283c52865af1247f), CI-workflow commit [1159c689](https://github.com/WhoSia/MQR/commit/1159c689ff71bb11e0d7c2b61d72f8ab69eb6e83), [Actions 37798943621](https://github.com/WhoSia/MQR/actions/runs/37798943621) SUCCESS, artifact id `11560315344`, immutable-derived ZIP **3,092 bytes**, moved into the same existing Drive folder with metadata-verified file ID `1dCPSPMpZfaQUUr6uI1_dNOu2LaONNSso`.
- No publisher full-raw dataset claimed stored in these small ZIP receipts. All GitHub commits are human-account authored, CI has read-only `contents` and never authors/forces commits.
- Canonical Notion Research OS Lab page remains ID `3c8ef561cf92815693b6fcf6de9955f7`. The exact sole active `Lab LIKE 'MQR%'` Labs-row invariant was queried on 2026-10-09. All stage narratives are sections in that one root.

## 7. Future without version inflation

Do not open a new version merely to continue research administratively. A successor could be considered only for (1) actual, grounded original raster-based spatial map AUC/agreement discordance on paired target masks, (2) independently audited published author source-risk experiment with serious rival, or (3) a formally useful and genuinely independent mathematical identification counterexample beyond routine covariate-shift literature. These are prospective *questions*, not results or reserved titles. Any future author-approved successor must separately specify its source, falsifier, affected authority and stop rule. MQR-4.92 is scientifically **CLOSED bounded**; novelty/spatial/generalization subclaims remain **HOLD**.
