# MQR-4.93 — Candidate Entry Contract (NOT OPENED)

**Working title — proposed, not author-confirmed:**
**MQR-4.93 — Spatial Holdout Admissibility, Coordinate Semantics & Target-Risk Identifiability**

**2026-10-09 — PREPARED / NOT AUTHORIZED AS FORMAL OPENING.**
No 4.93 empirical success, new Lab, Notion subpage, new branch, or future title commitment is implied. The only currently operative scientific closeout is MQR-4.92 [bounded final receipt](MQR-4.92-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md).

## One question worth a short version

**Can a claimed geographical deployment-risk contrast be made scientifically admissible on an independently pinned, original species dataset when coordinate meaning, geographic separation, class/time/complete-case selection, source-root ancestry, and withheld target labels must all survive falsification?**

4.92 measured an original-data **temporal** holdout, not a spatial one. Its single-split result demonstrated that better mean balance on 19 BIO covariates need not track target log-loss estimation accuracy. It did **not** show original spatial-map instability, a general KMM failure, conditional loss shift identification or methodological novelty. 4.93 cannot silently relabel 4.92's temporal evidence as spatial.

## Precise empirical target

**Source candidate:** Serov, Koldasbayeva & Zaytsev (2026), `Scientific Reports`, DOI `10.1038/s41598-026-36740-7`, original repository `egorser0v/Importance-reweighting` at fixed upstream commit `46c4d011c9f0cd0614c08e7edb68ac2491f659c8`. Start with active `anemone.csv` Git blob `0e1c83dda391229ffd3cb69573d184eebf1c7bdd`; `caltha.csv` and `tussilago.csv` are sensitivity specimens from the *same publication root*, never independent publications. Existing original-script source is reusable from `experiments/mqr-4.92` without modifying upstream data, model, or historical receipts.

### Gate 0 — Semantic and data-root admissibility, BEFORE target risk

1. Audit raw `lat` / `long` values, documented decimalLongitude/decimalLatitude renaming in the author notebook, range plausibility, units, geographic sign and actual downstream coordinate use. A swapped **column name** is a flagged risk, **not** proof that physical coordinates or published results are wrong. Confirm geography against a source-independent description or original code semantics.
2. Identify duplicated or quasi-duplicated geographic positions, invalid coordinates, complete-case selection, class presence and year distributions by candidate spatial region. Do not assume the original CSV supports genuine independently separated spatial regions from a nonempty coordinate field.
3. Frozen source Git blobs and original author function hashes are mandatory; source asset modifications or availability failure -> `SOURCE_HOLD`.
4. **Fail closed:** geographic coordinate semantics unresolved -> `COORDINATE_SEMANTICS_HOLD`; no eligible binary labeled source/target spatial blocks -> `SPATIAL_HOLDOUT_INFEASIBLE`. No opportunistic target or region choice after inspecting loss outcomes.

### Gate 1 — Prespecified geographic experiment

After Gate 0 passes, but BEFORE oracle target labels or any source/target risk are viewed, preseal a deterministic geographic blocking rule, source and target partitions, feature/missingness mask, train/validation/target sample sizes or clear minimum thresholds, model hyperparameters, random hash seeds, buffer/adjacency rules, original KMM/MCE estimators and evaluation metric (average held-out log-loss). Selection may use source labels for *train feasibility* only, not the target's observed outcomes to select a favorable block. Avoid label-based target geography selection, target tuning, spatial train-test near-duplicates and source-only baseline mismatches.

Compute original-author KMM/MCE estimates from the same untouched source validation loss and unlabeled target covariates, with target labels withheld until post-hoc oracle calculation. Report estimation gaps, ESS, weight mass/concentration, feature-balance proxy, source–target separation, and held-out prediction agreement **on truly matched point coordinates only**. Point-level predictions are **not** a native published continuous raster map: never call point agreement full spatial map replication.

### Gate 2 — Identifiability challenge and best rival

- Explicitly distinguish source/target covariate balance, conditional-loss invariance, spatial sampling bias and support overlap; do not identify the source of error from single-run ESS.
- Predefine one strong competitor: *geographically blocked holdout evaluation with direct labeled target audit*, if available, and original unweighted estimator as comparator. A direct labeled target oracle evaluates estimates; it is not an available unlabeled-deployment estimator.
- Document `n_study_roots`, block dependence and spatial correlation; forbid iid-cell confidence intervals, "40 independent effects" rhetoric, automatic cross-study pooled effects or methodological superiority from source-shared specimens.
- If a mathematical counterexample earns a precise falsifier, verify a small typed statement in **Lean 4** or Rust properties, rather than making a broad theorem/novelty promise. Keep numerical original-function replay in **Python**; Rust can encode authoritative claim-contract state; Prolog remains optional for ancestry queries. Multiple languages do **not** imply independent science.

## Predefined short stop rule — version discipline

- **PASS-BOUNDED/CLOSE** if coordinate semantics and original source hashes pass, genuinely spatially held-out target point data are verified, original author risk estimates and target oracle are reproduced numerically under a frozen design, and a falsifiable comparison is reported with dependence bounds and complete receipts. A negative/non-dominance result is acceptable.
- **NEGATIVE/CLOSE** if source selection or true spatial separation fails on the original pinned dataset; this identifies an actual source-admissibility limit, not an algorithm failure.
- **HOLD/CLOSE** if coordinate meaning or external source assets cannot be verified within bounded effort. Do not fill the hole with arbitrary remaps, convenient geometry or synthetic PASS.
- **NO 4.93 opening yet:** author must approve title/stage; move candidate to `OPEN` only with an explicit opening receipt. One source semantic audit and one prespecified empirical comparison are preferred to endless within-version patches. A material protocol correction gets its own receipt; do not repair outcomes post-reveal.

## Preservation and Research OS governance

- MQR has **exactly one** canonical Notion Lab page, ID `3c8ef561cf92815693b6fcf6de9955f7`. Place candidate notes as a heading inside that page only; never create version Lab rows, subpages, or folders.
- `main` only, no GitHub Actions bot-authored commits, no workflow self-write/push/tag, all published receipts linked and failures retained.
- Original publisher code/data immutable and pinned; read-only CI may test; large raw assets and execution ZIP receipts belong in the canonical Drive custody path with metadata/hashes.
- Source and historical discipline: preserve origin instrumentation/measurement question, earlier 4.91 failed Zenodo original raster transfer and 4.92 finite genuine temporal counterexample; neither grants a spatial verdict automatically.
