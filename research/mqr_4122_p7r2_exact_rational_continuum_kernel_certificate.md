# MQR-4.122 P7-R2 — Exact Rational Enclosure of a Continuous Uniform-Ball Source Kernel

2026-10-20. **CONTINUUM MATHEMATICAL ENCLOSURE PASS_BOUNDED; BEST REAL GEOMETRY HOLD; LEAN PROOF OF CONTINUOUS INTEGRATION HOLD.**

## Context and scope

Follow-up to [P6](mqr_4122_p6_finite_source_oscillation_kernel_and_nullspace_witness.md) and [P7 first formal-algebra audit](mqr_4122_p7_continuum_certificate_contract_and_exact_shell_nullspace.md).
Original published BEST effective path lengths: inner 52.03 ± 0.18 cm, outer 54.41 ± 0.18 cm, Barinov et al., Phys. Rev. C 105, 065502 (2022), DOI https://doi.org/10.1103/PhysRevC.105.065502 . These are **not reproduced** here. The source is an ideal uniform ball, radius a=1/20 m; targets are three radial shells [1/5,17/50],[17/50,49/100],[49/100,13/20] m. Oscillation model P_ee(d)=1-A sin²(kd) with A=11/20, k=8 rad/m is constructed, NOT a BEST parameter fit.

## Complete analytic bounds

For r>a and uniformly distributed s∈B_a, the angular-averaged inverse-square response is

K0(r) = E_{s,u}[r²/(r²+s²-2rsu)]
      = sum_{n≥0} 3 a^(2n) / [(2n+1)(2n+3) r^(2n)].

Derivation: angular average (r/(2s)) ln((r+s)/(r-s)) = sum_{n≥0}(s/r)^(2n)/(2n+1), then radial source moments E[s^(2n)]=3 a^(2n)/(2n+3). Terms are strictly nonnegative and converge uniformly on our target (r≥0.2 m > a=0.05 m). To enclose shell baseline Bj=∫_I K0(r)dr, truncate n=0..11 exactly in rational arithmetic. For n0=12 and ξ=(a/rmin)²≤1/16, the omitted positive tail is bounded by

0 ≤ Bj-Bj^(11) ≤ (rmax-rmin)*3/((2*n0+1)*(2*n0+3)) * ξ^n0/(1-ξ).

The formula is a simple coefficient monotonicity bound; the evaluation uses rational exponents and exact integration of each r^(-2n) term.

For oscillation, define source-distance moments

Mn(I)=∫_I dr r² E_{s,u}[d^(2n-2)], n≥1.
Integrating angular u and source radius s by the binomial theorem yields

Mn(I)= ∑_{j=1,3,...,2n-1}
  [3*binom(2n,j)/(2n*(j+2))] a^(j-1)
  * (rmax^(2n-j+2)-rmin^(2n-j+2))/(2n-j+2).

Therefore for the oscillation-weighted shell response Cj,

Cj = Bj + (A/2) ∑_{n≥1} (-1)^n (2k)^(2n) / (2n)! Mn(I).

Truncate n=1..33. The Taylor–Lagrange bound for cos(2kd) after order 66 (identical to order 67 because odd terms vanish), with remainder bounded pointwise by |2kd|^68/68!, gives

|Cj - [Bj + (A/2) Sum_1^33]| ≤ (A/2) (2k)^68/68! * M34(I).

All coefficients, sums, powers, integrations and interval determinant products are exact fractions (Python standard-library Fraction), avoiding binary floating-point roundoff in certification. Floats appear **only** in human-readable decimal receipts, never in sign tests.

Volume weights use Vj/(4π)=∫_Ij r²dr=(hi³-lo³)/3, a common positive scaling of the first determinant row that does not affect its sign.

## Interval determinant certificate

Define interval-enclosed B and C as above, V rational exactly. Perform ordinary endpoint interval arithmetic on the Leibniz determinant

D = det([V/(4π);B;C]).

The checked certificate shows D > 0 with determinant about 0.000268306392369768 (units correspond to the scaled V row and two length rows). It does **not** rely on observed convergence or rounded decimals. The corresponding two occupied fraction vectors can be chosen q±=(1/2,1/2,1/2)±ε(V×B), with sufficiently small rational/real ε>0 ensuring 0≤q±≤1, and then V·q+=V·q-, B·q+=B·q-, and C·q+≠C·q-.

**Logical status:** the analytic series identities, Taylor bound and arithmetic enclosure together yield a rigorous mathematical continuum witness under the stated idealized geometry. The analytic integration identities and proof of remainder are documented on paper and executed by a rational script, NOT yet kernel-verified in Lean. An independent derivation and/or translated proof is still desirable.

## Reproducibility

- [Exact rational audit script](../experiments/mqr-4.122/p7_certified_finite_source_integrals.py)
- [Read-only CI first SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39365396419), with no user/Actions bot write permissions. The additional outward-rounded decimal certificate display is audited by a further push run.
- [P7 prior Lean shell-weight arithmetic](../experiments/mqr-4.122/lean/MQR4122P6.lean) CI #39352862925 SUCCESS. **It does not establish the continuous integrals or their error bounds in Lean**.
- CI does not read any original BEST CAD, detector target mask, raw gallium counts or nuclear-physics covariance.

## Writing Loop

WRITE — formalize source-averaged inverse-square kernel as a uniformly convergent positive power series; integrate radial moments of cosine oscillation exactly and enclose Taylor remainder; form a rational interval determinant of shell weights.
ATTACK — the source/target are hypothetical and disjoint; if actual source overlaps target the r>a expansion and tail bound need replacement; pointwise cosine remainder must be propagated through the physically weighted integral; Lean verified only discrete and post-integral algebra; the original BEST geometry may have completely different separation properties.
REVISE — state validated theorem only for the explicitly defined continuum uniform-ball / three-shell family, never for BEST. Print rational outward decimal bounds rather than misleading equal-looking float endpoints. Preserve original BEST path-length reproduction HOLD.
DRAFT-CLOSED — a mathematical case study and conditional continuum identification result, not empirical sterile-neutrino evidence.
BACKLOG — independent formal derivation of analytic shell moments and tail inequalities, Lean kernel-level continuous theorem, source-target overlap handling, original BEST Fig. 8 mask/CAD and independent experimental geometry reconstruction, multi-energy line uncertainty/covariance, and archival Drive readback.

**VERDICT: P7 CONTINUUM INTEGRAL BOUNDED MATH PASS; LEAN CONTINUOUS INTEGRAL PROOF HOLD; BEST RECONSTRUCTION HOLD; BOT_CONTRIBUTION_ZERO.**
