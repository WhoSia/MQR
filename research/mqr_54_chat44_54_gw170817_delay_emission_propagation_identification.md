# MQR 5.4 · MQR 44 · R54 — A real multiscience discovery and an exact emission-versus-propagation identification limit

**2026-11-23 KST**. Derived exact toy structural identification result and ran local standard-library Python with PASS. This is not a re-fit of GW170817 physical signals. MQR 5.4 OPEN.

## 1. Primary empirical anchor and original research
The joint 2017 publication *Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A*, original [LIGO publication record P1700308](https://dcc-llo.ligo.org/LIGO-P1700308/public), [arXiv original abstract 1710.05834](https://arxiv.org/abs/1710.05834), confirms arrival difference **+1.74 ± 0.05 s** and derived conditional limits on gravitational/light propagation speed and related foundational-gravity tests. The quoted bound in the original is -3×10^-15 to +7×10^-16 in a fractional speed difference under explicit emission-time modeling assumptions. This should not be represented as the unconstrained raw ratio 1.74s/cosmic travel time.

**A preexisting theoretical question becomes experimentally constrained in 2017**, not necessarily logically newly inventable in 2017. This is a disconfirming case for the simple thesis 'every new experimental question requires a new named concept'. Original peer-reviewed journal text indexed online, official LIGO summary and original abstracts read; no raw detector streams imported/reanalyzed.

## 2. The exact underidentification of a single linked event
In simplified Euclidean-distance and common-frame units, observed gamma minus GW arrival-time offset is:
  d_obs = e_src + D (1/v_gamma − 1/v_GW) = e_src + k D,
where e_src is gamma minus GW intrinsic **emission-time** delay, D the travel distance, and k a relative propagation slowness. A paired measurement of d_obs from ONE event at D supplies one equation in **two unknowns** e_src and k: for any assumed k, choose e_src=d_obs−kD. Even perfect arrival clocks and unquestionable event matching **do not identify a unique speed difference** absent assumptions on source emission. This is an explicit distinction between **measurement linkage** and **physical inference**, consistent with published analysis.

If TWO distinct events at distances D1≠D2 have **exactly the same intrinsic emission delay e**, then
  k=(d2−d1)/(D2−D1)
and e=d1−kD1 are identified. But the common-emission-delay assumption across astrophysical sources is a substantive and possibly false physical constraint, not a free experimental right. If source delays e1 and e2 are independently unknown, any k still fits both event observations, hence no identification without astrophysical priors or other data. Real cosmological propagation needs expansion, source redshifts, dispersion and timing-model uncertainties; this toy deliberately abstracts those away.

## 3. Exact computational witness
`language/real/experiments/mqr_multimessenger_emission_delay_v54.py` uses exact rational arithmetic:
Event 1 (D=1,d=2): both (e=1,k=1) and (e=2,k=0) fit.
Event 2 (D=3,d=4): under shared e, both events identify e=1,k=1; if independent event-specific e_i, slopes -3,0,1,6 all fit perfectly by choosing e_i appropriately.
Local result: `PASS: 1-event emission/propagation confounding; 2 distances identify slope ONLY with shared source-lag assumption`.
The values 1,2,3,4 are **invented dimensional-normalized toy numbers**, not measured distances/delays of GW170817. This is familiar multi-event confounding/statistical identification, not a new theorem.

## 4. Implications for the MQR seven-question program
- Q2 bridging different scientific styles: gravitational and electromagnetic observatories link a shared world event without global representational isomorphism.
- Q5 mathematical effectiveness: algebra exposes precisely which new experiments/assumptions change identification rank; mathematical form alone cannot determine the physical source lag.
- Q6 resistance of the world: measured delay restricts *combinations* of emission and propagation hypotheses; actual external physics constraints require independent astrophysical modeling.
- Q7 unformulated questions: a new answerable test can predate its material realization in mathematical conception; not every expansion of experimental capability is a concept birth.

The 'new question' claim must stay operationally restricted and contemporaneously historical, not retrospectively inflated.

## 5. Severe rival checks
Timing coincidences might be random unless trigger-rate and sky-position evidence support common progenitor; association p-values/false-alarm rates are not directly Bayesian probability of same source without base rates. Selection based on events triggering two messengers may bias astrophysical populations. The source emission process can vary with viewing angle, ejecta properties and other unknown conditions. These are **potential confounders**, not evidence the original LIGO collaboration overlooked them. Real 2017 bounds must be reported in their original conditional model, not as conclusively measured v_GW.

**Status:** original primary publication metadata & source statements verified; synthetic exact identification PASS; event physical-model-independent speed inference REJECTED; 5.4 OPEN.
