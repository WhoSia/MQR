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
