# MQR-4.90 P8 — S4 Supplement Provenance and Admissibility

Primary publication: Koldasbayeva & Zaytsev, *Foundation for unbiased cross-validation of spatio-temporal models for Species Distribution Modeling*, *Ecological Informatics* 92 (2025) 103521; DOI: 10.1016/j.ecoinf.2025.103521.

Published online supplement **MMC S1, sections S1–S4**, original publisher PDF: https://ars.els-cdn.com/content/image/1-s2.0-S1574954125005308-mmc1.pdf . Specifically source Tables **S4.1** and **S4.2**, source PDF text extracted and source CSV parsed 2026-10-08. Dataset, CV, policy and metric fields are transcribed; all numbers printed to three decimals.

**108 rows** = 2 independent biological source families × 2 final training strategies × 9 CV variants × 3 metrics (MAE, Pearson, Spearman); each row contains four algorithm values and one printed average. All 108 rows have a computed four-algorithm arithmetic mean within at most 0.00105 of published rounded average. Mean absolute error is defined by authors across 100 hyperparameter configurations per algorithm and CV, not an uncertainty interval and not 100 independent studies. Pearson and Spearman are ranking/association measures across configurations; they are not signed CV-optimism effects.

**Primary signed bias pooling remains HOLD.** Descriptive MAE differences may be compared within source/policy as *validation–test fidelity contrasts*, not as causal superiority of a CV approach. Aggregated tables do not include per-configuration covariance or independent source cohort replications. Supplement S4 describes testing over historical out-of-time target; infer only the corresponding retrospective target scope where supported by main methods.

The published article Tables 2–3 use a different operator: maximum external test AUC over 100 model configurations (test oracle). Do not mix with S4.1–S4.2 averaged MAE/correlation observations or infer that published maxima are untouched test scores for a CV-selected model.

Reproduction recipe: run the stdlib Rust canonical court and P8 table audit after loading `koldasbayeva_2025_s4_validation_fidelity.csv`. Preserve upstream PDF URI and checksummed source artifact; read these numbers as source-reported, not fresh independent model reruns.
