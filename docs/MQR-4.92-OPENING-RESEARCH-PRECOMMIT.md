# MQR 4.92 — Opening Research Precommit (Proposed Formal Name)
**Proposed formal name, subject to author confirmation:**
**MQR-4.92 — Cross-Study Evaluation Contracts, Spatial Prediction–Performance Discordance, Source-Root Dependence & Falsifiable Evidence-Repair Benchmarks**

Korean: **연구 간 평가 계약, 공간 예측과 성능의 불일치, 자료 계보 의존성 및 반증 가능한 증거 복구 벤치마크**.

**Version status:** `OPEN / P0 PRECOMMIT / TITLE PROPOSED, NOT YET CONFIRMED`.
**Predecessor:** 4.91 `CLOSED / SOURCE-SCOPED EMPIRICAL PASS / METHOD NOVELTY HOLD` as `docs/MQR-4.91-FINAL-SCIENTIFIC-CLOSEOUT.md`.
**Research form:** Within the existing MQR single-Lab Notion page only; this GitHub file is an admissible research artifact, not permission to create Notion 4.92 pages or Labs rows. Four or more experiments may follow within this ONE version, not new numbered Labs.

## Explanandum lock: what is not yet explained

In original Matsui (2026) source replay, four fitted CV-fold models of the same source calibration lineage have sharply different rank AUCs on the SAME external target (Digitaria Europe→Oceania fold range ~0.610) and model rank reversals across deployment targets. MQR 4.91 proved numeric reproduction and a restricted fixed-target comparability contract, but did NOT explain the rank-score divergence as a spatial feature, identify causal direction, quantify true independent transport bias, measure actual pixel-level spatial stability, prove method novelty, or benchmark evidence repair against existing methods. Explanandum: **what extra empirically falsifiable scientific information a source-attested evaluation contract provides beyond ordinary paired AUC and spatial stability metrics**.

## Precommitted research axes and outcome requirements

### A. Source-root transfer is a hard second-data boundary
- Obtain and independently replay at least ONE external publication/dataset with its own original evaluation table and source-root identity *distinct from Matsui*. First candidate Serov, Koldasbayeva & Zaytsev (2026), *Kernel mean matching enhances risk estimation under spatial distribution shifts*, with public code `https://github.com/awesomeslayer/Importance-reweighting`, PDF already Drive 10_PAPERS. Verify repository tag, license, reported data/selection policy, exact metric and original held-out design before any comparison.
- If independent datasets expose *risk* rather than AUC, prohibit pooling numeric effects or treating risk difference as rank-AUC. Either construct an appropriate **typed risk contract** for the independent source or report `METRIC_INCOMPATIBILITY_HOLD`. This is a valid result if well documented.
- A public GitHub code repository without original data and executable baseline **does not count** as an independent source-replay PASS. Preserve raw and generated provenance.

### B. Spatial rank–performance discordance: empirical rival rather than discovery claim
- On original published maps with hash-verified source and matched valid raster masks, compute all six pairwise original fitted-fold spatial Spearman rank correlations, raw-score Pearson correlations and score absolute differences, alongside the same-target source-labelled AUC differences from 4.91.
- Report any models with similar AUC but materially different spatial maps and, conversely, different AUC but similar spatial maps. All thresholds defining “similar” or “different” must be predeclared or explicitly analysed as thresholds, not selected after seeing the matrix.
- Compare to pre-existing Grimmett, Whitsed & Horta (2020), which used replicate **thresholded-map Fleiss' kappa**, treating it as a competing *concept* and (if possible) a separate explicit thresholded-map metric, NOT conflating it with our continuous rank score.
- This is descriptive raster comparison over spatially correlated locations; forbid cellwise iid CIs and post-hoc threshold promotion.

### C. Source dependency and selection contract
- Each evidence object declares publication root, training cohort root, final/fold fitted model identity, external region, positive source, negative reference, source selection screen, target label use, mask, raster coordinate system, sample unit and metric.
- Test hard cases: same file path but different geographic target suffix, wrong base-map vs actual external-map type, target/reference mismatch, fold vs final model identity change, dataset reuse labelled as independent, missing/filtered target regions, ambiguous GIS boundary points. For each, ensure invalid claims are rejected and valid paired contrasts are admitted.
- Root-robust uncertainty must treat nested targets/folds within one study as dependent. If independent roots <2, report no cross-study CI; if two or more, predeclare an actual cluster-level approach supported by the small number of roots, no asymptotic iid miracle.

### D. Falsifiable evaluation-contract repair benchmark
Compare a restricted automated source-repair judge against meaningful baselines on **the same manually curated source-inventory tasks**:
1. plain metadata/path/filename matching;
2. independent fixed-reference numeric source comparison;
3. optional blinded human source audit where bounded and possible.

Predetermine and report false admissions (most serious), false rejections, diagnosis correctness, number of extra source artifacts required, source replay pass rate and review/compute cost, including ordinary time-to-repair. A typed refusal is allowed; treating “always reject” as high quality is forbidden. **Novelty claim remains HOLD** until comparator and real independent source case show added practical value beyond routine domain practice.

## Non-goals and prior-art guards

- Do NOT claim an original general transportability algorithm: Lee, Correa & Bareinboim (2020) GTR/GTRU is sound/complete for an explicitly different **conditional interventional causal** identification problem under SCM assumptions.
- Do NOT claim first spatial model agreement or AUC limitations: Grimmett et al. (2020), Phillips et al. (2009), VanDerWal et al. (2009) and ecology SDM literature predate the experiment.
- Do NOT claim a new universal minimal evidence witness: Calautti et al. (2024) and provenance theory distinguish subset-minimal, minimum-cardinality and least-cost derivations. Only accept proven minima under an explicit finite source-task universe and cost oracle.
- Do NOT turn source-model-vs-target matched AUC difference into the **causal effect of CV strategy**, signed spatial CV optimism or identifiable transport bias absent the actual identification assumptions.

## Controlled resumption of blocked source computation

MQR 4.91 source original fold-raster map correlation numerical replay was blocked by repeated original Zenodo HTTP 504/502/503. Synthetic map agreement tests passed run `37791461167`. Retain earlier original ten-target AUC confirmed PASS (`37786496173`). Before any 4.92 repeated ~96MB + 47MB transfers, prefer a separately checksum-verified existing original source archive cache if legitimately stored and accessible; otherwise bounded retries with original digest verification. Never lower source checksum, write to friend server outside user-owned directory, or “fix” a source rejection by redefining sample to improve a desired result.

## Stop rules

- **PASS/BOUNDED:** at least one genuinely independent study source has a defensible typed metric/mask/selection contract plus actual baseline comparison; novel utility, if any, supported by before/after benchmark with failures disclosed.
- **NEGATIVE/BOUNDED:** existing published methods and simple baselines match or surpass added type rules; document that the incremental scientific value is unsupported and close rather than continue indefinitely.
- **HOLD:** independent original study source inaccessible or incompatible, blocked map replay, missing evaluation identity, lack of independent root count for statistical uncertainty, or no honest comparator.

**Execution ethic:** reason judgment up front, cheap bounded source tests, no bot-authored commits, no new Notion pages/folders, no Notion Labs duplicates. Keep title provisional until user confirms; next MQR version beyond 4.92 is not authorized by this document.
