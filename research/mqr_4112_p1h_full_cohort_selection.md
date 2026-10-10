# MQR-4.112 P1-H — Original full-cohort genealogy and observed-only selection sensitivity

**Status 2026-10-11 KST:** P1-H native source and 5-case Bayesian ablation complete; full-author-grain acquisition HOLD; MQR-4.112 OPEN. This is a bounded P-stage, not a new physical law.

## Two-stage original measurement and selection lineage

**Original primary [Guérin et al. 2015, Journal of Archaeological Science 58, pp.147-166, DOI 10.1016/j.jas.2015.01.019, Table 4]:** [peer-reviewed accepted manuscript](https://backend.orbit.dtu.dk/ws/files/127388858/JASC14_624R1_post_print.pdf), [independently indexed original manuscript](https://files01.core.ac.uk/download/pdf/43249736.pdf). The Table 4 transcribed source text (image screenshot unavailable) reports each FER1 and FER3 initially measured 2400 single grains. FER1 first-test signal error <20%: 101, saturation exclusions 4 => n=97 accepted; FER3 first-test <20%: 97, saturation exclusions 1 => n=96 accepted. D0>100Gy was an additional original selection criterion. The source abstract alone is not enough; these are actual original Table 4 rows. **This 2015 manuscript was not in the user's 10_PAPERS according to the indexed Drive check; original direct PDF URL verified, but it has not been ingested into Drive.**

**Original primary [Guérin et al. 2021, Geochronology 3, 229-245, DOI 10.5194/gchron-3-229-2021]:** [Drive original paper](https://drive.google.com/file/d/1hgzZlM8HbVyq5l_auJyS36mQo2u3nAZb/view), Section 3, says the public BIN supplement contains only a small fraction of original measured grains and refers to the 2015 grain lists. [Actual author original ZIP in Drive](https://drive.google.com/file/d/1BCujdWongKH2nA2RJjnBRao1dsJHGzJg/view), ZIP SHA256 `25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228`; embedded author Rmd explicitly states the example is substantially shortened and not the full set. Each public DiscPos contains 49 unique (position,grain) entries.

**Cohort accounting:** 2015 accepted 97/96 vs 2021 tutorial examples 49/49; apparent gaps 48/47 and fractions 49/97=50.515%, 49/96=51.042%. **Conditional only:** The physical key mapping from the 2015 full accepted sets to the 2021 published BayLum posterior is not recovered. We have counts but NOT the real 48/47 unobserved grain identities or responses; do not assert exact full-2021 inclusion without source. Public `DiscPos` position coverage: FER1 range 1–13, 11 distinct positions, keys sorted; FER3 range 1–23, 21 distinct positions, keys unsorted. These distinct public layouts prevent the assumption of an identical public pedagogical thinning process.

## Actual native pre-registered source / selection stress

[GitHub read-only CI #38083088966 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38083088966) on exact source HEAD `9579e66e09710a4c0d9c993deb124c83c94f8d12`; [artifact #11681542022](https://github.com/WhoSia/MQR/actions/runs/38083088966/artifacts/11681542022), downloaded ZIP SHA256 `848b54489f763039195000c4a3efa6168c3dac68d81c62af21e5d36809c26e9c`. Rust first-principle cohort-key audit 2 tests PASS, original ZIP hash PASS; initial [#38083022259 FAILURE](https://github.com/WhoSia/MQR/actions/runs/38083022259) was CSV trailing empty rows, repaired by skipping blank lines while preserving original data; not a scientific failure. Rust comparison outputs historical 2400/97/96 versus real 49+49 public key counts.

[Native R observed-only grain thinning source](../experiments/mqr-4.112/p1h_observed_thinning.R) uses authentic 2021 public 98 observations, exactly original P1-F mathematical JAGS contract `AgesMultiCS2_EXPZO/lognormal_A`, prior/THETA/strata fixed. FER1 always retains all 49 observed grain-response rows as negative control; FER3 remains at 49 or randomly retains 37 and 25 rows in two distinct deterministic source-derived subsets each. 3 independent JAGS chains per scenario, 4000 adapt + 4000 burnin + 4000 sample iterations / thin5, explicit separate JAGS RNG streams. No synthetic data, no guessed full grain or contamination. Changes are grain-response row inclusion only; per-physical-grain ID linking for the numeric rows remains separately HOLD.

| FER3 scenario | FER3 mean ka | FER3 HPD95 ka | FER3 ESS | FER3 PSRF upper | FER1 placebo diagnostic |
|---|---:|---|---:|---:|---|
| full49 | 31.12595 | [27.64461,34.98218] | 797.2 | 1.0133 | PASS |
| first37 | 30.82628 | [26.96669,34.60967] | 810.4 | 1.0201 | **HOLD**, upper=1.07779 and ESS=320.7 |
| second37 | 32.05370 | [28.12643,36.00088] | 932.8 | 1.0253 | PASS |
| first25 | 30.05681 | [25.63907,34.48598] | 570.4 | 1.0328 | PASS |
| second25 | 30.69063 | [26.58634,35.24075] | 472.6 | 1.0364 | PASS |

Numerical gate: adaptation complete, ESS>=200, PSRF upper<1.05; FER3 5/5 PASS, FER1 4/5 PASS and one honest numerical control HOLD. Source-selected example FER3 posterior remains ~30–32 ka and none of these 5 mean/HPD estimates matches the **different full-observation-cohort** original paper FER3 [36.6,47.8] ka. This is neither the causal effect of the 47 absent grains nor proof their inclusion would produce a ~10ka shift: observed-grain random thinning is not the historical selection mechanism, and real 2015 quality screen depends on measured uncertainty/curvature/saturation.

## The explanatory target and active rivals

Two distinct selections must be reconstructed: **physical quality-filter eligibility** (measurement-dependent: ST error, D0, saturation) and **2021 public tutorial reduction** (membership/selection mechanism unknown). Previous P1 evidence excludes row-permutation alone as the 10ka discrepancy; P1-F does not support wrapper-only vintage as explanation; P1-G and P1-H support genuine ~31ka convergence in the restricted 49-grain example. The remaining real-world target is **identify original full 2021 FER3 96-ish selected grains and their raw signal/dose-rate/rejection decisions** and fit the actual full data under the exact historical model. 2015 aggregate age 39.7±2.3 ka and independent radiocarbon belong to different model/calibration estimands, not substituted observation rows.

Source acquisition conditions and draft (NOT SENT) recorded in [primary source custody ledger](mqr_4112_primary_source_custody.md). No novelty claim; no physically identified missing-grain age effect until actual full-cohort bytes received.