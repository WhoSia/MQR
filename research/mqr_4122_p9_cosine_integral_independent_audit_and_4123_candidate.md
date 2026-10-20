# MQR-4.122 P9 — Independent Cosine-Integral Cross-Method Audit and 4.123 Promotion Scent

2026-10-20. **P9 INDEPENDENT NUMERICAL CROSS-METHOD PASS; INDEPENDENT RIGOROUS ENCLOSURE HOLD; ACTUAL BEST REPRODUCTION HOLD.**

## New independent evidence
The original P7-R2 uses positive power series for source-averaged inverse-square response and exact rational cosine Taylor moments, yielding an exact rational enclosure for D=det([V/(4π),B,C]) of [268306392369768/10^18,268306392369769/10^18].

P9 independently eliminates the angular coordinate by the cosine integral function. For r>a, fixed emitter radius s and oscillation wavenumber k>0:

E_u[r² cos(2k d)/d²]=r/(2s)[Ci(2k(r+s))-Ci(2k(r-s))],

because d²=r²+s²-2rsu and dCi(z)/dz=cos(z)/z. Integrate emitter radial weight 3s²/a³ and radial target r separately using 45-digit mpmath Gauss–Legendre quadrature. Formula for oscillation kernel:
Kosc(r)=(1-A/2)K0(r)+(A/2)E_{s,u}[r² cos(2k d)/d²].

Parameters remain synthetic: source ball a=.05 m, occupancy shells [.2,.34],[.34,.49],[.49,.65] m, A=.55, k=8 rad/m.

[Independent code](../experiments/mqr-4.122/p9_cosine_integral_independent_numerical_audit.py) and [actual read-only CI #39374190438 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39374190438) show D≈0.000268306392369768051745111723178, inside P7 rational bounds.

**Attack:** mpmath quadgl convergence and working precision do not constitute independently validated outward rounding or rigorous quadrature truncation bounds. P9 is an independent *analytic-reduction/numeric* reproduction, not a second rigorous enclosure. Both P7 and P9 assume the same idealized homogeneous centered ball source and three radial target shells, NOT actual BEST Fig. 8 shapes or experimental neutrino rates.

## The 4.123 promotion smell — provisional research thesis

4.122 has shown a mathematical issue: a new oscillation-weighted functional may separate idealized geometries sharing total volume and no-oscillation response. The potentially DISTINCT 4.123 research question is whether and when this **mathematical observability** survives uncertain instruments and real experimental observation protocols. Suggested provisional title:

**MQR-4.123 — From Formal Observability to Experimental Discrimination: Robust Witnesses, Nuisance-Relative Identifiability, Independent Calibration and the Limits of Physical Model Transfer.**

Candidate promotion criterion: specify independent physical/source geometry, source and target kernel with independently constrained nuisance set N, at least one original-data observable and uncertainty/covariance model; prove or bound the observation sets of rivals under N; demonstrate either a robust separation or explicit impossibility with original evidence; confront a plausible alternative physical explanation. Only then a new physical research programme would have a distinctive empirical license. This threshold is a local research planning criterion, NOT universal philosophy-of-science demarcation.

Historical inherited HOLD: 4.121 optical/chemical real data, BEST original Fig. 8 reconstruction, Gallium nuclear cross-section correlations, 4.120 JTPA population/estimand issues, and earlier FER1/FER3 replication remain separate. No aggregate numeric progress index.

**Promotion verdict:** 4.123 **CONCEPT STRONGLY CANDIDATE / OPEN NOT AUTHORIZED**. Continuing Lean formalization and P7 numerical rigor alone is within 4.122, not yet a new distinct generational programme. Do not conflate conceptual promise with completion of physical reproduction.

## Writing Loop
WRITE — independent cosine integral kernel and test of the P7 determinant; frame rival robust-witness research question.
ATTACK — new calculation lacks certified bounds; physical source masks are unverified; 4.123 may simply duplicate 4.122 intervention-relative identifiability without independent nuisance/calibration novelty.
REVISE — P9 only exact-method-diverse numerical corroboration; 4.123 requires a genuinely distinctive nuisance-relative experimental discrimination question.
DRAFT-CLOSED — P9 independent calculation audit.
BACKLOG — independently certified adaptive quadrature; Lean rigorous integral/remainder theorem; physically grounded original BEST and other measuring apparatus; nuisance robust sets and independent standards.
