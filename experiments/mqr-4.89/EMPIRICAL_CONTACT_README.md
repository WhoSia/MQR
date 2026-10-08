# MQR-4.89 — Executable Data-Leakage Contact Court

**Stage:** OPEN / METHOD-LEVEL EMPIRICAL-MECHANISM PASS / ORIGINAL-CAPSULE REPLAY HOLD

This is the executable *methodological* counterpart to MQR-4.87–4.88's provenance, dependence, warrant, scoped-use, and reopening formalism. It does not claim to reproduce Kapoor & Narayanan (2023)'s civil-war experimental data, code, or original AUC values.

## Source

Kapoor & Narayanan, *Leakage and the reproducibility crisis in machine-learning-based science*, Patterns 4 (2023), 100804, DOI 10.1016/j.patter.2023.100804.

The authors link Code Ocean capsule **6282482/tree/v1**, DOI **10.24433/CO.4899453.v1**. In the current research runtime this provider returns HTTP 403, so original data/code and their specific experiment outputs have not been downloaded, hashed, inspected or rerun.

## Executable contact

Run `python experiments/mqr-4.89/empirical_leakage_reproduction.py --seeds 12` after installing dependencies from `empirical_requirements.txt`.

The script actually trains classifiers on four frozen-seed **synthetic generators** (12 replicates each):

| Category | Constructed invalid evaluation | Constructed controlled evaluation | Mean AUC invalid vs controlled (local study) |
|---|---|---|---|
| L2 | Target-derived retrospective proxy supplied at prediction time | Exclude unavailable target proxy | 0.985 / 0.765 |
| L1.3 | Supervised feature selection sees test labels | Supervised selection trained on train labels only | 0.807 / 0.481 |
| L3.2 | Identical synthetic entities occur in train and test | Hold out entire entities | 1.000 / 0.500 |
| L3.1 | Random sample includes future outcome regime in training | Chronological future holdout | 0.889 / 0.102 |

These are **engineered contrasts, not estimated average causal impacts of leakage in science**. In L3.2 the entity label is deliberately non-transferable and L3.1 deliberately reverses the feature-label association; their huge gaps reflect the generator design. In the null feature-selection case the data contains no predictive information and the invalid selection uses test labels.

Additional local artifacts (separate downloadable archive in the associated research session) include a **20-split public Wisconsin Breast Cancer Diagnostic benchmark with an artificially injected hindsight variable**, 24 falsification controls showing that properly generalizable signals do not automatically collapse under group/time splits, a directly observable imputation L1.2 information-flow witness, eight declared-protocol audits, a deterministic second replay, and SHA-256 self-consistency/tampering checks. Those additional controls are not yet claimed to have passed hosted GitHub Actions.

## Authority and falsification boundary

- SOURCE_REPORTED: the authors describe or criticize original civil-war studies.
- SYNTHETIC_ML_EXECUTION: this repository's script directly trains and compares synthetic ML models.
- REAL_BENCHMARK_WITH_ARTIFICIAL_LEAK: secondary local control using scikit-learn bundled data.
- ORIGINAL_CAPSULE_REPRODUCTION: **NOT PERFORMED**.
- INDEPENDENT_VALIDATION: **NOT PERFORMED**.

A published paper, a matching hash, a successful script execution, and scientific authorization are not interchangeable receipts. Reopening a specific evaluation-dependent claim does not establish that every predictor of the studied kind is invalid.

The run manifest is self-generated and cannot authenticate an external reviewer or prove identity of the unavailable Code Ocean input. A CI PASS, even once observed, confirms only that the committed **tests** ran, not that original scientific analyses were reproduced.

## Sources of methodological strength and weakness

**Strength:** paired corrupt/correct protocols with repeated actual training, negative controls against over-generalization, deterministic output checks, and explicit error-source typing.

**Weakness:** all four main mechanisms are deliberately synthetic and cannot calibrate natural leakage prevalence. The small benchmark deliberately injects a proxy, and the CI setup cannot create an authenticated external attestation. True original-capsule reproduction requires immutable original bytes and runnable provenance from Code Ocean.

See canonical Notion MQR-4.89 for the full scientific audit and stage verdict.
