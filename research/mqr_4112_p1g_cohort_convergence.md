# MQR-4.112 P1-G — Cohort Ancestry and MCMC Convergence (2026-10-11)

**Verdict:** Genuine native computation succeeded; public example cohort convergence PASS_BOUNDED; original published full cohort identity and published posterior replication HOLD. This is P1-G, not a new formal version.

## Original author provenance

[Guérin et al. (2021) actual original paper](https://drive.google.com/file/d/1hgzZlM8HbVyq5l_auJyS36mQo2u3nAZb/view), Sect. 3, states the supplement contains only a small fraction of measured grains. [Original author ZIP](https://drive.google.com/file/d/1BCujdWongKH2nA2RJjnBRao1dsJHGzJg/view) embeds PracticalGuideToBayLum.Rmd with the explicit warning that FER1 and FER3 example datasets are shortened and omit the full original samples. ZIP SHA256 `25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228`; Rmd SHA256 `3b744bc5d069e111d742d8d20a331252c984bd834a3b3240756cb2d39e8603d8`. The original examples' DiscPos files contain 49 unique (position,grain) keys per FER sample. Original author Rmd: Iter=5000, thin=5, three chains, lognormal_A. Published FER3 independent 95% credible interval [36.6,47.8] ka, *not a proven same-cohort reference* for public example reproduction.

## Actual native evidence

[Read-only CI #38081723267 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38081723267), code `ecda98bf114ef9ab1963c42e25df40e55f42ac2c` (WhoSia). [Posterior + custody artifact #11680449255](https://github.com/WhoSia/MQR/actions/runs/38081723267/artifacts/11680449255), ZIP sha256 `f346a0e6c1999ea6a5655ba7f2e4808f8a617de04fc1e621b31352d08a4da908`, verified by independent redownload. Contains full per-chain posterior RDS, exact JAGS model input RDS, original-cohort JSON, convergence CSV and raw logs. [Audit code](../experiments/mqr-4.112/p1/cohort_source_audit.py), [seeded R experiment](../experiments/mqr-4.112/p1/seeded_jags_diagnostics.R).

Same P1-F frozen mathematical model `AgesMultiCS2_EXPZO/lognormal_A` and publicly supplied 49+49 observations. Two independent runs, each 3 different explicit JAGS Mersenne-Twister chain seeds; 5000 adaptation + 5000 burnin + 5000 sampling, thin5; 3000 saved draws per run.

| Repeat | FER1 mean [HPD95] ka | FER1 ESS / PSRF upper | FER3 mean [HPD95] ka | FER3 ESS / PSRF upper |
|---|---|---|---|---|
| 1 | 39.05938 [33.22874,45.03809] | 473.5 / 1.0047 | 31.40732 [27.82651,35.26704] | 991.2 / 1.0042 |
| 2 | 39.01934 [33.58405,44.96730] | 505.1 / 1.0217 | 31.29706 [27.32658,34.77029] | 1137.0 / 1.0043 |

Each row adaptation=TRUE and prespecified numerical gate ESS>=400, upper Gelman PSRF<1.05 PASS. FER3 between-run shift 0.11026ka, MCSE 0.06111 vs 0.05613ka. Replication of P1-F produced a different stochastic old-vs-modern FER3 mean difference (+0.16193ka), so do not claim an exact wrapper causal effect.

**Conclusions:** short 49-grain subset's ~31ka posterior is robust to the tested per-chain RNG and convergence objections; full-cohort original paper 36.6-47.8ka vs subset remains incomparable as a same-source reproduction. Neither physical effect nor new MQR law shown. **Next:** obtain full original FER1/FER3 measured BIN, complete (position,grain) selection lists, 2021 executable environment, and only then compare source-matched posterior distributions.