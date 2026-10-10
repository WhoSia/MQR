# MQR-4.109 — Provenance-Sensitive Sufficiency & Calibration-Graph Transport: Model-Relative Information Loss, Cross-Standard Warrant, Historical Reconstruction and Adversarial Rival Discrimination

**Official user-approved title, OPEN (2026-10-10).** Distinctness/novelty **HOLD**, not an assertion of new measurement theory. Sole working branch: `main`; no new Actions workflow.

## Primitive question and migration from 4.108

MQR-4.108 showed that a graph-mediated table `D=S(G(R))` can retain sufficient information for one statistical target and lose information for another. MQR-4.109 asks whether and how evidential *authority for a specified measurement result* transports across the separate documentary/calibration graph, even if a statistical experiment is Blackwell-equivalent after tabulation.

Do not conflate: (1) statistical sufficiency relative to family E_θ and target θ; (2) Blackwell comparison of experiment kernels on a common Θ, with Markov garbling independent of θ; (3) measurement-result reference traceability requiring certificate/documented unbroken calibration chain and uncertainty; (4) accuracy of the measurand model and soundness of ontology; (5) authenticity of the historical source/transcription.

## Inherited primary-source audit

Regnault 1847 original full-volume DjVu in Google Drive 11_SOURCES `1yvgpg_U6giXU-zzag7FFctTzQKhnMbLT`, 15,049,344 bytes, not yet byte/page audited. A converted 361 MiB PDF in 11_SOURCES `1oMK9-9K_f4SIxLkOtZpTzW2Dxhr_6OAe`, above 256 MiB connected-download limit; preservation != complete page certification. Original online facsimile p181 / DjVu 215 shows printed A′ H0 785.21 mmHg at 95.57°C; Chang 2004 Table 2.5 says 782.21 mmHg, cause unknown. Printed p240 / DjVu 274 says p241 table derived by carefully executed graphical constructions based on immediate experimental results (Plate VIII / DjVu 820); individual raw points / smoothing methods not reconstructed; do not categorize each p241 entry as an observed datum.

Predecessors: [4.108](mqr_4108_calibration_model_underdetermination.md), [4.107](mqr_4107_evidential_history_equivalence.md).

## Strongest existing rival court

- Fisher–Neyman factorization: sufficiency is model family/parameter-relative; mean-only table is sufficient for Gaussian known-variance location but insufficient for unknown variance. An identical summary does not claim preservation of all other questions.
- Blackwell comparison: two observation kernels on *the same θ and decision problem family* may be equivalent via mutual Markov kernels. Adding a certificate *external to the observation kernel* need not change ordinary θ-decision performance. Changes in permitted assertions reflect augmented evidence/authority contracts, not Blackwell's failure.
- JCGM 200:2012 VIM 2.41–2.42: traceability is a property of results with documented calibrated reference chains and contributed uncertainty. It does not itself prove adequate uncertainty or eliminate mistakes.
- JCGM 100:2008 GUM §§5.2.4–5.2.5: reference sharing and calibration curves induce covariance; include relevant correlated input quantities and propagate uncertainty.
- Eran Tal (2017), *Calibration: Modelling the Measurement Process*, §5.4: reference/calibration coherence and robustness depend on statistical and theoretical background assumptions.
- Hasok Chang (2004), *Inventing Temperature*, chs 2 and 5: thermometry, scale comparability, historical model choices and epistemic iteration.
- Regnault original documents are evidence about what was reported, not automatic certificates of modern traceability.

### P1 finite falsification: same information kernel, different external receipts

Let Θ={0,1}, observe X∈{0,1} with `P(X=θ)=3/4`; tabular Y=X. Both experiments are literally identical and hence trivially Blackwell equivalent. Attach *out-of-band* metadata `c∈{audited,uncertified}`, not asserted to be an observed random variable from E_θ. Same `X,Y` gives identical θ likelihood and equal-risk decision for θ, but different **documentary warrant to assert an audited reference chain**. This is only a typed reporting rule *assuming a genuinely validated audit exists*. It is not a new statistical theorem, does not itself certify accuracy, and is already covered by VIM traceability.

Negative control: do not regard a mere string 'audited' as authentic. Authenticity is required as a separate premise, ideally independently checked. If both certificates are unverified, both remain unverified. If the claim at issue is θ alone, there is **no difference**. If the claim is certified traceability, there can be a difference, but this is an *explicit change in target proposition*, not the discovery that Blackwell equivalence fails.

### P1 second court: information loss depends on model

Raw pairs A=(0,2), B=(1,1), mean table=1 for both. Known-variance Gaussian location: mean remains sufficient for μ. Unknown-variance Gaussian: mean-only table insufficient for (μ,σ²) (likelihood ratio at μ=1 is exp(-1/σ²)). This is an inherited standard illustration, not a unique MQR result.

## Distinctness criteria and STOP

A novel MQR judgment requires a **named same-target** contrast under explicit shared premises, at least one physically grounded historical case, and a rival forecast by GUM/VIM/Tal/Chang/Blackwell which cannot reproduce it under reasonable auxiliary assumptions. Merely adding a provenance type to already known experiment/certificate machinery is useful software engineering, not philosophical novelty.

- P1 exact finite checks: code `experiments/mqr_4109/provenance_blackwell_court.py`. Verify locally; do not run Actions by default.
- Source/p241 graph-to-table trace: historical evidence only; no imaginary digitization.
- Certificate authenticity, real instrument calibration ancestry, uncertainty and independent material tests **HOLD**.
- `MQR-4.109 OPEN / DISTINCTNESS HOLD`. `MQR-4.108 OPEN/HOLD` unchanged.

## P2 next falsification

Seek a defensible historical claim with equal statistical information and genuinely different **same-target** warranted scientific conclusions after controlling for certificate existence, reference basis, estimation target, and source selection. If every case collapses into VIM traceability, GUM correlated uncertainties, Tal coherence, or Chang epistemic iteration, mark that local originality route NEGATIVE and migrate question rather than repeating synthetic tests.

## P2 — Actual published Regnault same-target four-material contrast, 2026-10-10

### Primary historical boundary
Regnault (1847), printed pp240-241, describes p241 as a mercury-vs-air table drawn from graphical constructions based on immediate experiments (Plate VIII). At reported AIR thermometer value T=250 degrees C, the published p241 mercury readings are **253.00** (Choisy crystal), **250.05** (ordinary glass 5), **251.85** (green glass 10), **251.44** (Swedish glass 11). Thus the observed *published table* offsets t-T are **+3.00, +0.05, +1.85, +1.44 degrees C** and maximum tabular spread **2.95 degrees C**. Exact Fraction arithmetic checked locally; code experiments/mqr_4109/p2_regnault_same_target_court.py, commit 57ba26aed5b26f6e39b6da1959b3fb8feb8474c2. These are real historical *table values*, not reconstructed direct experimental observations, individually digitized Plate VIII points, or certified thermodynamic true temperatures. At T=250 four reported devices disagree, but no manufacturer-specific ground-truth judgment follows.

### Same-target rival comparison — strongest charitable interpretation
| Rival | What the p241 contrast supports / method | Why no distinct MQR verdict |
|---|---|---|
| Fisher-Neyman sufficiency | Requires a declared statistical family and target parameter; p241 readings are processed graph-derived summaries and original likelihood/variance are not supplied. Cannot assert sufficiency or its failure for the historical raw experiment. | The previous 4.108 Gaussian synthetic examples are classical, not evidence of Regnault actual likelihood. |
| Blackwell comparison | Requires indexed experimental kernels on a common state space, and a specified stochastic garbling relation; four fixed tabular numeric readings do not define those kernels. | No Blackwell order or equality between thermometers can be inferred from a single graph-derived table row. |
| GUM §5.2.4–5.2.5 | Consider correlated instrument/reference influences, glass-dependent corrections, covariance and uncertainty budgets, if requisite calibration information is available. | Without original calibration input uncertainties cannot quantify which thermometer's indicated temperature is closer to physical target. |
| VIM §2.41 | Document actual result-specific chain to a reference, including contributing uncertainties. | A shared 'air reference' numerical abscissa is not a modern verified traceability certificate. |
| Tal (2017) §5.4 | Treat agreement/disagreement as model-mediated calibration coherence test and question background assumptions. | Material disagreement and need to examine reference coherence are already in Tal's rival. |
| Chang (2004), ch2 and ch5 | Analyzes Regnault thermometers, material differences, air-vs-mercury comparability and epistemic iteration. | Historical variation is central to Chang's existing account. |
| MQR-4.109 | Separates source ink, graph processing, calibrated result, and proposition-warrant status. | No identified same-target verdict that mature rivals cannot replicate; uniqueness **HOLD**. |

### Falsification conclusion
An apparent MQR-specific finding 'the same thermometer reading does not imply identical metrological authority' is explicitly reducible to VIM's chain notion and Tal's model-coherence account. Regnault four-material disagreement is historical evidence **for demanding calibration**, not evidence for a novel MQR law. Thus **P2 source table arithmetic PASS_BOUNDED; same-target independence / novel discrimination HOLD**. Historical p181 printed A-prime pressure 785.21 versus Chang (2004) Table 2.5 782.21 remains a textual discrepancy without established causal provenance.

### Prospective Flowing Version name — NOT OPENED
**MQR-4.110 — Provenance-Sensitive Calibration Transport & Historical Measurement Warrant: Model-Relative Information Preservation, Cross-Standard Comparability, Source-Graph Reconstruction and Independent Rival Falsification**

This is intentionally an *incremental renaming* of 4.109. It cannot be justified as migration of a genuinely new primitive question until the concrete intervention object changes, e.g. obtaining independent raw-to-graph or authenticated calibration-chain evidence rather than repeating algebra on the same p241 readings. 4.109 stays OPEN/HOLD, and 4.110 is merely a proposal, not an opened/closed scientific stage.

## P3 maintenance: 4.109 P2 Python fixture retired to Drive after Rust replacement

4.109 P2 source-only fixed-decimal arithmetic was migrated to Rust canonical successor `experiments/mqr-4.110/src/main.rs` with a dedicated CI workflow. The one-off historical Python `experiments/mqr_4109/p2_regnault_same_target_court.py` is retired after Drive archive of full source content [MQR-4.109 P2 Python archive](https://drive.google.com/file/d/199mFVqJAn19rvRBVySGlNTTLp1LRrIJf/view). Original Git blob `7bbce363725b0d25a95a66e9c0aff2ab647e15e7` survives in Git history; Drive export reflows whitespace. Earlier file links represent *historical paths*, not active executables. Do not retire 4.109 P1 theoretical counterexample or live 4.108 tools without separately proving no dependency.
