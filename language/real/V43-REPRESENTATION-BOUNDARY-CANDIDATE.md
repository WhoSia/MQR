# REALREPRESENT 0.43-CANDIDATE — Representation-Invariant Measurement Warrant

**Development status:** native Rust + independently enumerated finite countermodels **PASS_BOUNDED**, **NOT PROMOTED**. New separate executables `real-v43-represent` and `real-v43-crosswalk`, no changes to existing `REALPACKET 0.2/0.3`, `REALACQUIRE 0.29`, `REALREFERENCE 0.41-CANDIDATE` or `REALHISTORY 0.42-CANDIDATE`. MQR-4.112 OPEN; **MQR-4.113 PROPOSAL ONLY**, not created/approved.

## Core scientific question

When one data representation is converted into another, what exactly remains invariant: a token, a physical unit, an operation, a distribution of observations, or the warrant for a particular claim?

We refuse `SAME NUMBER ⇒ SAME QUANTITY` and `SAME COMPUTED POSTERIOR ⇒ SAME PHYSICAL GRAIN`. We also refuse the opposite overstatement `ANY LOSS OF OBSERVATION BITS ⇒ ALL CLAIMS LOSE IDENTIFICATION`.

For finite declared possible histories (H), let source observation (A:H\to X), representation map (g:X\to Y), target claim (Q:H\to T), and new observation (B=g\circ A). The model-independent classical deterministic facts are:

1. (ker(A)\subseteq\ker(B)). Deterministic post-processing cannot split two histories previously indistinguishable by (A).
2. If (Q) factors through (B), it factors through (A).
3. If (g) is injective **on the attained source image** (A(H)), (ker(A)=ker(B)), so (Q) factors through one iff it factors through the other.
4. For a **particular** (Q), a non-injective (g) may still preserve factorization. Information-order equality is stronger than target-specific adequacy.

These are familiar finite sufficiency and Blackwell-style deterministic garbling facts, **not new theorems**. They do **not** establish stochastic Blackwell/Le Cam comparisons, a physical calibration, an adequately represented empirical relation, an independent operation, or completeness of (H).

## Executable packet and conservative authority gates

```text
REALREPRESENT 0.43-CANDIDATE
id calibrated_dose_units
basis FINITE_COUNTERMODEL
target latent_dose_state
source instrument_Gy
destination published_mGy
quantity_source DOSE
quantity_destination DOSE
unit_source Gy
unit_destination mGy
operation_source SAME_MEASUREMENT
operation_destination SAME_MEASUREMENT
transform AFFINE 1000 1 0
world a instrument_Gy=1 published_mGy=1000 latent_dose_state=LOW
world b instrument_Gy=2 published_mGy=2000 latent_dose_state=HIGH
END
```

The checker first verifies a **small explicit unit registry**: Gy↔mGy, s↔ms, m↔cm/mm, and same-unit identity; exact integer affine transformations checked using overflow-aware `i128`. `FLOOR_DIV` models lossy integer post-processing without changing units, and `TABLE` models explicitly declared symbolic recodings. This registry is a toy subset of metrology, **not a globally complete ontology or legally certified unit conversion authority**.

All worlds use the same source/destination/target keys. Duplicate world fields and alias conflicts are rejected. `SOURCE_REPORTED` demands a source SHA256 but **does not** certify the claimed custodian. Different operation labels get `HOLD_DIFFERENT_OPERATION`; the same operation label emits `SAME_LABEL_ONLY_UNVERIFIED`, NOT an empirical proof. Numerical correctness, physical-quantity semantics, target-relative factorization and operational ancestry are separate dimensions.

Outputs include `type_contract`, `numeric_or_label_transform`, `observation_partition` (EQUIVALENT/DESTINATION_COARSER/etc.), `source_target_factors`, `destination_target_factors`, and a **conditional finite-model** transport verdict. Irrespective of local structural PASS, **`representation.world_authority=HOLD`** and `real_language_promotion=UNPROMOTED_CANDIDATE`.

## Executed source + finite results

[Final read-only CI #38137710993 **SUCCESS**](https://github.com/WhoSia/MQR/actions/runs/38137710993), executed head `b9ab5fd2574a78653072db518571ffa648b70a2b`:

- Two Rust binaries' **22 unit tests PASS**, all older Real-Language binary builds PASS; **seven direct** independently interpreted typed-syntax countermodels PASS. Cases: genuine Gy/mGy transform, wrong conversion, numerically equal values with different physical quantity, lossy rounding destroying a specific target, lossy rounding retaining a coarser target, different measurement operations despite numerically commuting values, lossless symbolic recoding.
- The independently written Python `independent_v43_finite.py` exhausted **19,683** triples of 3-history source (A), deterministic postprocessor (g), and target (Q). `FINITE_SCIENTIFIC_INFORMATION_ORDER_EXHAUSTIVE_19683_PASS`, without making random-sampling claims. Among its 4,860 source-identifiable genuinely coarsened cases, **1,512 target-preserving** and **3,348 target-defeating** cases. Those are counts in this *chosen enumeration*, NOT frequencies in the physical world.
- The only actual scientific data were the **official 2021 FER1/FER3 tutorial** prior [P1-J physical-key/likelihood-row CI #38132359197](https://github.com/WhoSia/MQR/actions/runs/38132359197), artifact `#11699408026`, with original-authored ZIP SHA256 already source-custodied. A separate read-only GitHub job retrieved the original metadata crosswalk and pinned exact CSV SHA256 `883b538f9ee5e457f41d89d291a7a6b92c2db70cae762447e23cf70a390128a4`. Rust and independent Python verified **98 unique physical (sample, disc position, grain) keys**, FER1 **21/49** modern row position differences, FER3 **49/49**, and exact jags row origin alignment. This proves a source-dependent permutation **of the existing 49+49 tutorial observations**; source signal equality itself was inherited from the earlier independent P1-J witness. **Full original FER1/FER3 97/96 population HOLD**.
- [Machine-readable 13-file CI artifact #11701762003](https://github.com/WhoSia/MQR/actions/runs/38137710993/artifacts/11701762003), SHA256 `df4f0616a378d848d00057cee1d0ebc083ae3e05665351f2137821afefbc55bd`. Actually downloaded and ZIP byte digest rechecked.

The first two 0.43 runs failed from an inserted Rust source formatting mistake, then non-ASCII instrument label parsing (RISØ); both were repaired. These were engineering failures, **not evidence for or against a physical theory**. Only the successful head-bound run above certifies v0.43 tested source.

## Prior art, where novelty stops

- <https://doi.org/10.1007/s13194-021-00365-6> — Elina Vessonen (2021), *Representation in Measurement*, [original in Drive](https://drive.google.com/file/d/1jkafhd23yHYGUZYzXZtd32Pmy76fcTLu/view). Measurement's relevant relations and attributes cannot be certified by syntactic bijection.
- [David Blackwell (1951), *Comparison of Experiments*, original Drive](https://drive.google.com/file/d/1AabK3bac9aNuX5ASeEqkRDRucQSDZ7JB/view), [1953 bibliographic DOI](https://doi.org/10.1214/aoms/1177729032); [Torgersen (1991), *Comparison of Statistical Experiments*](https://drive.google.com/file/d/112DN9KJ-JdKpRhLIbIDeusmejZ99msAX/view). All finite deterministic information-order tests are a **small special case**. Blackwell 1953 original PDF is held in Drive but its extracted text only supplies a JSTOR cover marker; it was NOT claimed fully read.
- [Eran Tal (2017), *Calibration: Modelling the Measurement Process*](https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view): operational calibration cannot be verified by a mere unit conversion table.
- [Bas van Fraassen (2012), empirical grounding](https://drive.google.com/file/d/1hP92t9SNeHh-gI6IIDA_o0m8cK_69xGr/view), [Hasok Chang (2004), *Inventing Temperature*](https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view), [Mayne (2026), domain-local operational realism](https://drive.google.com/file/d/1IaYIYMToo6uxxhzr3WMFEd5p8U4Zb7-J/view). The operational identity/target relation remains the principal independent world-facing question; local realism is not new.

## Return to natural science, not just programming

The real FER counterexample is a **representation-level** result under fixed public physical grain ancestry: an index can change without the grain changing. It neither explains the original paper's full-cohort FER3 chronology interval nor proves unrestricted transport of Bayesian inferences. The measured light outputs may depend on old/new preprocessing, covariance and legitimate signal semantics; all require separate checks.

**Live theory competitors**: (a) empirical operation–quantity mapping is required beyond a nominal code/type, (b) stochastic sensor channel equivalence may be weaker than deterministic image bijection, (c) post-selection can change the physical likelihood/cohort even if each retained key has a correct representation, and (d) historical calibration ancestry may make mathematically commuting maps physically non-commuting. The next formal question deserves 4.113 *only as a scientific target and with user approval*, not as a reward for compiler CI success.

**Verdict:** Real Lang 0.43 **DEVELOPMENT_TESTS_PASS / FINITE_MATH_PASS / ACTUAL_TUTORIAL_KEY_MAPPING_PASS**; **EMPIRICAL_REALIST_WARRANT_HOLD / STOCHASTIC_BLACKWELL_EXPERIMENT_HOLD / FULL_FER_SOURCE_HOLD / LANGUAGE_PROMOTION_HOLD**.
