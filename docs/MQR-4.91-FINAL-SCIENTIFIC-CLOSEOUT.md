# MQR 4.91 — Final Bounded Scientific Closeout
**Ruling date:** 2026-10-08. **Canonical state:** `CLOSED / SOURCE-SCOPED EMPIRICAL PASS / METHOD NOVELTY HOLD`. The scientific closure is **bounded**, not the admission of all ambitions originally enumerated in the opening constitution. Parent research MQR 4.90 already had a distinct bounded closeout; successor research is MQR 4.92. This file is a GitHub source record, **not a new Notion Lab/page**.

## 1. Empirically admitted, source-attested

The original Matsui (2026) *Ecology and Evolution* experiment, original DOI `10.1002/ece3.73534` and correction `10.1002/ece3.73828`, was audited against Zenodo `10.5281/zenodo.19970795`, archived original Maxent final and four fitted CV model `.lambdas` per biological calibration family, original target climate rasters and original positive/reference-negative evaluation coordinates, official Maxent 3.4.4 and pinned source content digests.

- **10 / 10** original author-published external target final model prediction cases were reproduced and their author final AUCs independently validated to source-published precision. The correct author target ASC, where necessary separately tagged with a destination-region name, was used. This repaired a previous **source artifact identification error**: comparing the base/calibration map instead of the author target-region projection; it did NOT show target missingness or irreproducibility.
- **Four original CV fitted models** from the same source calibration family were projected to each of the ten original external target raster regions. Source labelled positives and unrecorded reference-negative geographic coordinates were aligned to the **same target** per model and evaluated with tied-pair AUC.
- **40 matched-target fold-vs-separately-fitted-final AUC contrasts**, within **10 target cases, three species calibration families, and one publisher study/source root**. These are NOT 40 independent effects or ten independent studies. GitHub Actions [original replay SUCCESS](https://github.com/WhoSia/MQR/actions/runs/37786496173), [descriptive factor & guard SUCCESS](https://github.com/WhoSia/MQR/actions/runs/37786929506).
- **Descriptive model × target interaction** on the four fitted source CV models: for Digitaria Europe→Oceania, same original external reference AUC values span approximately 0.265959–0.875743 (range ~0.609783). Within Digitaria, three of six fold-model rank pairs reverse across the four external target regions. Digitaria balanced four-target×four-fold raw AUC descriptive sum-of-squares consists of ~21.9% target mean, ~34.6% fitted model mean and ~43.5% double-centred interaction; these are purely arithmetic finite-matrix fractions, NOT independent variance components or a causal attribution.
- **GIS point-in-cell audit**: original final author points reproduce to small numerical error; observed borderline raster cells were uniquely resolved with original source final model scores only for a source-consistency audit. An independently predetermined edge-exclusion sensitivity based only on coordinates, not source scores, was computed on all original target cases. This does NOT independently establish the original author's point-on-edge rule.
- **Typed evaluation precheck** admitted same-target matched P+, Q−, model lineage, metric, mask and scoring contracts while correctly rejecting attempts to treat original native-calibration CV AUC as the identical external deployment AUC. This is a **restricted executable engineering contract**, not a transportability theorem, complete causal fusion algorithm, globally minimal witness proof or selection-bias identification.
- The full empirical matrix, scripts and study-root limitations are preserved in `docs/MQR-4.91-TEN-TARGET-SOURCE-REPLAY-AND-INTERACTION.md`; original 10-case source numeric CSV `experiments/mqr-4.91/matsui_2026_ten_source_matched_fold_auc.csv`; descriptive SS CSV `experiments/mqr-4.91/ten_target_fold_interaction_descriptive.csv`. Exact primary and secondary CI original source receipts were mirrored to Drive `02_ANALYSIS_SAFE`, original replay ID `1JrllZVj-JpMrlFlAGbohp3jabJFYt8Q-`, typed/decomposition ID `1Kp_q3YzJhAqEgUwA8jD0tQdfcWAPODsb`.

## 2. Negative courts and explicit remaining nonadmissions

**Do not extend 4.91** by restating its P0 ambitions as accomplished. Specifically not proved:
- signed spatial-CV optimism, generally partially identified transport bias, empirically justified pooled cross-study effects, independent biological precision or iid cell uncertainty;
- new mathematical discovery of fixed-reference AUC normalization (VanDerWal et al. 2009 and Phillips et al. 2009 already supply critical prior art);
- new discovery that AUC alone does not fully evaluate geographical stability (**Grimmett, Whitsed & Horta 2020**, DOI `10.1016/j.ecolmodel.2020.109194`, already evaluated replicate maps including Fleiss' kappa);
- general/sound/complete algorithm for causal transport from arbitrary observational and experimental source domains (**Lee, Correa & Bareinboim 2020**, DOI `10.1609/aaai.v34i06.6582`, gives GTR/GTRU soundness/completeness within their SCM task);
- inclusion-minimal or globally least-cost evidence repair witness (Calautti et al. 2024 gives independent provenance minimality distinctions);
- independent second original publication source replay or superior performance to manual source audit and published competing evaluators.

**Important open-source-data block:** New code `experiments/mqr-4.91/spatial_map_agreement.py` plus integrated original ten-target source runner attempts six fold-pair Spearman map rank, score-Pearson and absolute map-score gaps on the identical source target intersection. Adversarial/synthetic tests PASS [37791461167](https://github.com/WhoSia/MQR/actions/runs/37791461167), but **actual original spatial map agreement NOT MEASURED**; publisher Zenodo GET returned 504/502/503 across bounded retries (CI 37790731384 and 37790954815). No scientific PASS inferred from the synthetic tests. Defer that empirically testable item explicitly to 4.92; do not silently rerun indefinitely or keep 4.91 open for it. Earlier AUC dataset replay PASS remains historically valid.

## 3. Citable direct rival reading already conducted

- Phillips et al. (2009), VanDerWal et al. (2009): source/background and fixed evaluation design already established.
- Baker, Maclean & Gaston (2024): meta-analytic uncertainty over independent-test-free spatial bias correction, not automatic proof of model fairness.
- Serov, Koldasbayeva & Zaytsev (2026): spatial shift risk-estimation weighting comparators (KMM, IW, etc.) with selection screens; different numeric estimand from source-matched external AUC; their public repository requires independent source audit.
- Bareinboim & Pearl (2013), Lee, Correa & Bareinboim (2020): causal-effect meta/general transportability with different formal assumptions and query targets.
- Calautti et al. (2024): why-provenance minimality concept, not equivalent to low-cost repairs.
- Grimmett, Whitsed & Horta (2020): replicate spatial prediction stability beyond AUC. Acquired original Grimmett PDF Drive `1X5oYSlVVcCwR1xkUI0ld16PUt6JYjYoA`; original Lee/Correa/Bareinboim PDF Drive `1kfiCHsh6ZERktdK309y7GShaNRUU9YS4`; both renamed and moved from 00_INTAKE to canonical 10_PAPERS. The Lee & Bareinboim (2020) `Causal Effect Identifiability under Partial-Observability` PDF is a DIFFERENT work; don't merge them.

## 4. Scientific verdict

**MQR 4.91 CLOSED with experimentally reproduced original-source identity and target-locked model sensitivity**, valuable bounded findings and source-linked negative controls. It does NOT establish that the evaluation-contract language is a novel publishable method. Its P0 broad scope was pruned by empirical and prior-art challenge. The conclusion is **negative/limited for universal transport bias identification and minimal repair**, **positive for source-attested target-locked empirical reconstruction**.

This is a terminal scientific handoff, not a running protocol: no more new 4.91 experiments beyond correcting material errors in historical receipts. Cross-paper reproducibility, spatial-stability comparator and benchmarked repair utility are successor version 4.92 questions.

## 5. Research OS structural invariant

**One MQR Lab row, one existing MQR canonical Notion root** page ID `3c8ef561-cf92-8156-93b6-fcf6de9955f7`, all version histories and P substeps are sections inside that root. GitHub version-specific files are allowed source artifacts, not authorization to open new Notion version page/folder or Labs row. For any next write query `Labs WHERE Lab LIKE 'MQR%'`; if count is not exactly one or page ID differs, FAIL CLOSED. Preserve human-authored GitHub commits; never let GitHub Actions bot author commits.
