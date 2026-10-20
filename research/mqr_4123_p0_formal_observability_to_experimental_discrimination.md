# MQR-4.123 P0 — From Formal Observability to Experimental Discrimination: Robust Witnesses, Nuisance-Relative Identifiability, Independent Calibration & the Limits of Physical Model Transfer

**Opened 2026-10-20. Status: NEW RESEARCH QUESTION OPEN / SYNTHETIC MATHEMATICAL PILOT; EMPIRICAL DISCRIMINATION HOLD.**

## Why this is genuinely different from 4.122

4.122 demonstrated that even equal volume and no-oscillation path response can correspond to distinct oscillation-weighted responses for mathematical finite-source targets. The P7 rational determinant certificate and P9 independent cosine-integral numerical check established formal separation **inside the constructed uniform-source model**. Neither identifies true BEST geometry, experimental likelihood, or a sterile-neutrino explanation.

4.123 studies a further mapping: *does separation of idealized forward operators survive physical nuisance variables, calibration error, and finite-noise observations?* A nonzero determinant is **not** the same claim as disjoint observable prediction sets under uncertainty, much less finite-sample statistical power.

## Core definitions

Let H0,H1 be rival world/model classes, U independently specified interventions, C calibration protocols, N_h(u,C) allowed nuisance parameters for model h, and observable map F_h(u,n) ∈ R^d. Define the model's admissible prediction set
O_h(U,C) := {F_h(u,n): n∈N_h(U,C)}
for a **fixed common intervention schedule U**, preserving covariance and shared nuisance coupling across all channels. Write experimental error set E_h, optionally dependence constraints E_shared, separately and use enlarged sets O_h ⊕ E_h. A robust deterministic discrimination certificate is non-overlap of the enlarged sets with a positive margin under an explicitly fixed metric/norm. If sets overlap then there is no uniformly zero-error deterministic decision for the pair based solely on this readout. A nonempty overlap is *not* a claim that all probabilistic testing is useless, and positive deterministic separation alone is not a statistical power calculation.

## P0 exact rational counterexample

Let reference-free common bias b be unconstrained, and scalar readout under H0/H1 be:
Y0(u,b)=b ; Y1(u,b)=δu+b, δ=3/10 and u∈{0,1}.

At only u=0, Y0=Y1 for equal b. At u=1 with b allowed independently for each rival in [-1,1], the prediction intervals [-1,1] and [-7/10,13/10] overlap, so raw apparent 0.3 shift does not yield robust classification. 

Crucially, a *paired* measurement at u=0 and u=1 with the **same shared bias b** has a contrast D=Y(1,b)-Y(0,b). Then D0=0 and D1=3/10, exactly separated despite unknown b. If b is not stable but changes between measurements with |b1-b0|≤η, and independent readout errors have |e_i|≤ε, the contrast sets become [-η-2ε,η+2ε] and [δ-η-2ε,δ+η+2ε]. Their disjointness for δ>0 requires δ>2η+4ε. This bound is a scoped exact 1D result, not an experimental calibration for BEST.

If η=1/20 and ε=1/100 then δ=3/10 exceeds 2η+4ε=7/50, and a positive contrast gap remains 4/25. If η=1/5, ε=1/100, the sets overlap. This illustrates that instrument drift bounds can destroy the inference even when a formal readout contrast exists.

P0 calculations are to be checked with an exact Fraction fixture, not a physical experimental measurement.

## Independent calibration and attack cases

1. **Common reference correlation:** two instruments sharing calibration bias are not independent witnesses. A paired contrast cancels common b only if the same b applies to both observations or a separately bounded drift model holds.
2. **Protocol-relative meaning:** the same shared-bias cancellation need not work with distinct source geometry, isotope-specific response or changing detector efficiency.
3. **Unbounded nuisance erasure:** if an admissible nuisance enters the exact direction of the model contrast, the observation sets can overlap regardless of how nonzero the nominal model contrast is.
4. **Finite-sample gap:** deterministic interval separation requires a bounded-error model; Gaussian-like errors with unbounded support invalidate literal disjoint-support claims, even when tests with useful power exist.
5. **Transport restriction:** demonstration with synthetic P0 scalar observations grants no physical identification authority to BEST or the MQR-4.121 optical experiment.

## Research work streams

P1: exact nuisance-set and paired-intervention examples with read-only CI, independent audit and Lean proof of rational interval inequalities.
P2: multichannel covariance/shared-nuisance geometry and optimal separating linear contrasts with robustness under uncertain calibration.
P3: distributional testing and finite-sample power; distinguish probability distributions from deterministic admissible supports.
P4: physically grounded calibration case using original measured raw source data and independent standards (physical data admission gate).
P5: bounded connection to original BEST geometry and line-specific nuclear cross section uncertainties, only after independent source/target mask reproduction.

## Writing Loop
WRITE: formulate formal-vs-experimental discrimination and exact paired/common-nuisance counterexample.
ATTACK: if shared-bias stability is inferred rather than independently established, pair differencing is not entitled to remove the error; one-dimensional bounded-error cases do not prove data-level efficacy.
REVISE: P0 mathematical/synthetic PASS at most, empirical source/calibration/covariance HOLD, statistical power HOLD, original BEST source geometry HOLD.
DRAFT-CLOSED: a new target-specific research question and one exact pilot result; no demarcation theorem or true sterile-neutrino attribution.
BACKLOG: exact independently runnable fixture and proof; nuisance admissibility from real metrology; rigorously checked noise-model assumptions.

**4.123 OPEN authorized by user.** No new branch, no bot commits. 4.122 physical and Lean-continuum holds persist.
