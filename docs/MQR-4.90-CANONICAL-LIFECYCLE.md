# MQR-4.90 — Canonical Runtime, Evidence Family Registry and Safe Repository Lifecycle

## Current operative decision (2026-10-08)

**State: MQR-4.90 OPEN.** We have source-verified *reporting* differences and mathematical nonidentifiability counterexamples, but no admissible, pooled signed CV-minus-independent-target optimism effect. Falsely pooling target-oracle AUC maxima or cross-negative-design AUC is prohibited. The computational **authority order is Rust canonical → Lean proof obligations and Prolog lineage court → Python exploratory/fixture extraction**. None substitutes for independent measurement or sample-design provenance.

### Track A — Rust canonical authority

- `experiments/mqr-4.90/canonical/Cargo.toml` and `src/main.rs` are the main scientific decision executable, dependency-free edition 2021, with fixed-decimal AUC and explicit reject reasons.
- `cargo test --offline`; `cargo run --offline`. Source inputs are versioned CSV in `experiments/mqr-4.90/`.
- Deterministic source checks: Koldasbayeva et al. 2025 Tables 2–3, 36 source rows / 144 algorithm AUC cells, test-oracle maximum marked ineligible for the target estimand; Matsui 2026 Appendix A1–A4, 10 native-only score pairs across 3 source/calibration families, negative sampling incompatibility.
- A target claim is admitted only after claim-relative target routing: prospective evidence can support **future forecasting**, geographically disjoint test evidence may support **spatial transport**, and retrospective evidence may support **historical backcasting**. The temporal orientation is not promoted across these claim types. All scopes separately require development-only model selection, matched reference-negative design, compatible deployment policy, paired uncertainty/covariance, audited cohort genealogy and an appropriately independent target. This is deliberately narrower than arbitrary descriptive comparisons, without illegitimately demanding future holdouts for a purely spatial claim.

### Track B — Lean kernel proof boundary

- `language/real/lean/MQR/Empirical490.lean` proves the exact six-case null-AUC selection fixture and reject implications without new axioms, admits, or sorry. It also proves an unchanged ranking can yield AUC 1 versus AUC 0 when the sample designated as negative changes.
- These are **conditional mathematical theorems** about precisely defined fixtures and the declared admissibility predicate; they are **not proofs of empirical ground truth** or of a method's clinical/scientific causal impact.
- Run: `cd language/real/lean && lake env lean MQR/Empirical490.lean`; no implicit conversion of Lean theorem success to source reliability.

### Track C — Prolog evidence-family and authority checks

- `language/real/prolog/empirical490.pl` uses SWI-Prolog and plunit to challenge illicit evidence promotions, retrospective-to-future inference, shared data roots and reference-design mismatch.
- `swipl -q -s language/real/prolog/empirical490.pl -g 'run_tests(mqr490),halt(0)' -t 'halt(1)'`.
- Known dependency: Wang 2023 Amazon AGB directly inherits the Wadoux 2021 Amazon source family. Ploton 2020 Congo AGB is **not** to be labelled the same raw dataset merely because both are biomass studies.
- Prolog's historical facts and source links are **assertions backed by citations** and require review when the repository/data versions move. A passing logic program does not independently verify those assertions.

### Track D — Empirical source alignment and countermodels

- Koldasbayeva & Zaytsev 2025: 36 descriptive source rows, not 36 studies; test-oracle-max selection is distinct from ordinary CV selection. Fish historical test 2003–2005 versus 2006–2012 train is retrospective, not forward forecasting.
- Matsui 2026: Appendix A4 random-holdout CV uses Maxent presence/background scoring; Appendix A1–A3 external scoring treats unrecorded target cells as negative. Thus `AUC_CV - AUC_target` does **not** have a common reference-sampling design. One Oxalis native-only calibration produces reported differences +0.34 (Oceania) and −0.02 (Europe); neither is automatically causal spatial leakage.
- Serov et al. 2026: specific model selection demonstration filters a pool by target test AUC. Exact independent six-ranking null counterexample has unconditional mean AUC 0.5 and target-selected mean AUC 0.875, but these values are **not** the paper's measured effects.
- Further fixed-predictor reference-negative counterexample: identical scores for positives [3,4] yield AUC 1 against negative scores [1,2], but AUC 0 against negative scores [5,6]. Thus without fixing the negative-reference distribution, the difference between reported AUCs alone does not identify a spatial-transfer effect.
- Python `audit_reported_oracle_auc.py`, `audit_matsui_external_auc.py`, `target_oracle_selection_counterexample.py` remain **ACTIVE AUXILIARIES** (source extraction, independent check) and are NOT retired until their useful contracts are transferred and audited. Rust has the last word on admission and pooled claims.

### Track E — Git, Drive and retirement governance

- Prior to cleanup the only three live refs were `main`, `mqr-4.90-empirical-source-reanalysis` (fully merged, no unique ahead commits), and `archive-attribution-20261002` (1,154 ahead of current main; NOT redundant history).
- Pinned retirement heads: `4cdf33cf1a647c3fe11c2d5f8825dbb4d02d2589` and `4a3c9cf59b6756d3e241f26193df71a677243d4c`. Both were independently exported to Git bundles. GitHub Action run 37723008838 performed SHA matching, per-bundle restore/clone, `git fsck --full --strict`, SHA256 verification. External local verification repeated the archive SHA256 and `git bundle verify`.
- Recovered history Drive archive: [MQR Pinned Branch History Bundles](https://drive.google.com/file/d/1BmwQ-HhEzzeVjx3HK-MfIDbLdU3DVRVX/view). GitHub Actions artifact 11526249593, sha256:4799f5525878aa168d028eadf18857d7cd85b4b00a7081b763eddee3039dce9a.
- Branch removal used one-time human-initiated workflow, locked with `--force-with-lease` to those exact refs and approved Drive archive ID, and CI run 37723287220 SUCCESS. Post-readback: only **main** remained.
- Retired one-time operational scripts `.github/workflows/mqr-branch-archive.yml`, `mqr-one-time-branch-retirement.yml`, `mqr-retired-ops-snapshot.yml` have a second Drive archive: [MQR Retired Operations Sources](https://drive.google.com/file/d/1-vTwATrkyoj8cnARShcmAv_1ftphCWQN/view). Source tar/hash restore verified; GitHub run 37723456225 SUCCESS, artifact 11526676884. After Drive upload and verification, all three scripts were removed from active main by the authenticated human author.
- **No bot-authored commits.** Do not enable automated source/branch cleanup in CI. Any future deletion requires (1) exact hash and content inventory, (2) verified Drive archive and restore, (3) human authorization, (4) exact branch/file guard, (5) independent post-deletion readback.
- Historic Lean/Prolog/Rust files from earlier MQR stages are FROZEN RESEARCH RECORDS, **not automatically retired**. Source-path references and old workflows may still depend on them; a new Rust canonical layer does not license blanket deletion of the prior proof genealogy.

## Regression anchors

- Read-only Rust/Lean/Prolog workflow: `.github/workflows/mqr-4.90-multilanguage.yml`, latest known source after reference-design countermodel: run 37723428828 SUCCESS (all three jobs).
- Rust-first source-reanalysis workflow: `.github/workflows/mqr-4.90-source-reanalysis.yml`, legacy Python extraction follows canonical Rust acceptance; run 37723418216 SUCCESS for Rust addition.
- Primary scientific claim status remains `HOLD_NO_COMPARABLE_PAIRED_EFFECTS`. Neither zero admitted effects nor failure to pool is a claim that the true bias is zero.

## Bounded next-action court

1. Retrieve corrected Matsui raw predictions / species-region fixture from Dryad and normalize positive/negative reference selection; retain nominal AUC reporting gap separately from common-functional estimates.
2. Retrieve Koldasbayeva S4.1–S4.2 *CV-selected configuration*-matched independent test AUC and validate selection performed without target test labels, on a frozen holdout.
3. Materialize Wang's complete repeated spatial sample IDs, spatial-target reference RMSE, cross-CV draw covariance and shared-root graph with Wadoux.
4. Add equivalence/cross-language differential tests so Rust and Prolog cannot silently disagree on the same case; formalize required Lean invariants without using proof output as a substitute for empirical replay.
5. At bounded exhaustion, close as `SCOPED_NONIDENTIFIABILITY` only after a documented source-acquisition court, or close as `ESTIMAND_COMPARABLE` if matched effects and uncertainty become available. Do not open MQR-4.91 by continuity alone.

### P7 — Claim scope refinement and cross-language concordance

- Rust `Direction` supports prospective, geographically disjoint, retrospective and overlapping target evidence; `ClaimScope` distinguishes future forecasting, spatial transport and historical backcasting. Type-matched evidence is evaluated under its declared scope, not forced to pass an unrelated future-forecast gate.
- Prolog `admit_for_scope/2` mirrors the same distinctions with explicit idealized positive/negative controls. A geographic holdout does not thereby prove a forward forecast. A past holdout is legitimate for a bounded historical backcast when reference definitions and other evidence constraints match.
- Lean `scopeCompatible` has kernel-checked claims establishing future/space/backcast separation. Common-output CI `cross-language-concordance` requires canonical Rust and Prolog to agree on no currently eligible primary signed effects and HOLD pooling, alongside a Lean kernel receipt. This is a regression-level concordance check, not yet a complete proof of software equivalence across all inputs.
- Scientific meaning: the P6 test `prospective_only` restriction would have excluded all spatial targets even under fully matched scoring; P7 explicitly repairs that category error while retaining strict exclusion for the current Matsui cross-negative-design pairs. No actual source result is promoted by this routing change.
