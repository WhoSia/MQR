# MQR-4.113 P2-A — Calibration-Path Noncommutativity, Endpoint Equivalence & Limits of Historical Inference

**Date:** 2026-10-11 KST. **Scientific verdict:** FINITE CONSTRUCTED CHANNEL MATHEMATICS PASS_BOUNDED / PHYSICAL CALIBRATION, ACTUAL MEASURAND EQUIVALENCE, INDEPENDENT STANDARD AND NEW THEOREM NOVELTY HOLD. MQR-4.113 remains OPEN; MQR-4.112 remains separately OPEN. This P2-A is a finite mathematical precursor to the *empirical* P2 program, not completion of the user's requested empirical measurement-channel identification.

## Actual new source and executable receipts

- [Rust exact 2-state, 2-observation kernel composition and six tests](../experiments/mqr-4.113/p2_calibration_path_exact.rs): arithmetic overflow checks, row stochasticity, deterministic composition, exact cross-denominator comparison, max-over-state binary total-variation discrepancy, and declared non-identification firewall.
- [GitHub Actions #38140464011 — SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38140464011) on exact HEAD `09f66467a4d853c013ac4531af7a370a69c11c80`. Job 114473111188 native Rust tests **6 passed / 0 failed**, bounded executable receipt emitted, artifact #11702606785 successfully uploaded. Workflow is read-only `permissions: contents: read` and checkout persists no credentials; source and workflow commits author and committer `WhoSia`, never github-actions[bot].
- [Lean 4 constructed-arithmetic and noninjective-observation proof candidate](../experiments/mqr-4.113/lean/MQR4113CalibrationPaths.lean) and standalone pinned `v4.24.0` toolchain; [GitHub Actions Lean proof #38140849240 — SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38140849240) on exact HEAD `61ed53fa9d98bf40e22fa6cd17953f4e6e399f6a`: pinned Lean 4.24.0 `lake build` passed (`Built MQR4113CalibrationPaths`), with initial manifest-missing CI #38140749888 failing for packaging, not for proof semantics; corrected by adding `lake-manifest.json`. This checks finite arithmetic and a classical noninjectivity proof, not physical measurement equivalence.

## Finite mathematical P2-A

All matrices are **synthetic Markov kernels**, rows index the same two declared latent states, columns two declared observations. Let

`C=[[3,1],[1,3]]/4` and `D=[[2,0],[1,1]]/2`.

All rows sum to 1. Stochastic channel composition with row vectors gives

`CD=[[7,1],[5,3]]/8` and `DC=[[6,2],[4,4]]/8`.

Consequently `CD != DC`; the worst-state binary total-variation gap is **1/8**, exactly (the Rust execution prints the unreduced rational 8/64). This tests *noncommuting statistical transformations*, **not** that any two actual laboratory calibration/drift operations have this structure. No instrument, physical SI unit, drift process, or reference standard was observed for this construction.

Conversely `C*C=[[10,6],[6,10]]/16` is the same final statistical channel as the single-stage model `E=[[5,3],[3,5]]/8`. Distinct *stipulated* factorization paths therefore induce identical conditional observations. They may be distinguishable by independent chronological records, external intermediate readouts, or calibration certificates; the endpoint alone does not choose a unique path. Formally, distinct paths `p != q` with `observe(p)=observe(q)` witness noninjectivity of `observe`. This is standard mathematical nonidentifiability, not a new theorem.

No contradiction with 4.113 P1 Blackwell–Le Cam statistics: channel order is a mathematical relation conditional on a fixed shared state index, whereas physical operational identity and calibration lineage require external evidence.

## What must be attacked next (P2-B; status OPEN/HOLD)

Select one genuine published primary instrument-comparison dataset reporting **repeated calibrated observations of the same operationally defined physical measurand** with individual measurement values, standards, uncertainties, apparatus and time/order metadata, sufficient for source-pinned channel estimation.

Freeze prior to empirical inspection:
1. **Measurand and model:** SI quantity/dimension, reference model, state indexing, nuisance factors, definition of threshold or binning, channel estimator with uncertainty. Do not conflate an observed noisy surrogate with latent physical truth.
2. **Matched source identity:** the same object/sample IDs, raw readings, replicates, units, measurement order, environment, exclusion roster and calibration dates; hash actual raw source bytes. A PDF title, DOI and SHA pointer alone do not establish physical correctness.
3. **Calibration ancestry:** certificates/standard lots, instruments, shared roots, reference uncertainty correlations, within-day drift and possible intervention back-action. Compare a shared-standard world and an independently evidenced standard world rather than naming 'independent' instruments.
4. **Three rival predictions:** endpoint statistical equivalence; real same-measurand agreement with residual differences; apparent equivalence from a common drift/reference root. Test with independent diagnostic observations and between-day held-out units.
5. **Proof limits:** zero fitted deficiency can arise from discretization/coarse grouping or finite-sample uncertainty; not proof of physical equivalence. Reverse inequality in a finite example is not a universal law. Distinguish observed-data assertions, model-fitted quantities, and philosophical interpretation.

**4.112 remains separate:** real public FER1/FER3 49+49 physical-grain keys and JAGS correspondence PASS_BOUNDED, whole original BIN/BINX and full selection/exclusion roster and complete cohort age effect HOLD. Do not rebrand the 98 public keys as whole experiment or use this constructed P2 fixture to settle historical luminescence.

**Programming division:** Rust = checked exact stochastic kernels and source integrity; Lean = noninjectivity and algebraic formal proof; Haskell or Prolog only when a genuinely distinct proof/search or semantic-model bottleneck is identified; R/JAGS retained for authentic historical statistical models. Existing 0.44 Python front end is preserved as P1-reproduced predecessor, not first-choice future implementation. **REALCHANNEL v0.44 remains UNPROMOTED_CANDIDATE.**

**Method lineage:** 4.107–4.110 source-history and reference ancestry; 4.111 irreversible measurement; 4.112 observed public FER key map; 4.113 P0/P1 classical comparison and physical-warrant gap. Fisher–Neyman sufficiency, Blackwell–Le Cam experiments, JCGM VIM/GUM, Tal's calibration modeling, Chang's historical calibration and van Fraassen's representation are serious prior art and active rivals, not names to relabel as original MQR discoveries.
