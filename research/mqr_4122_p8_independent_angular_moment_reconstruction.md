# MQR-4.122 P8 — Independent Angular-Moment Reconstruction and Certified-Integral Scope Audit

**2026-10-20 — Independent exact rational 102/102 PASS. Full continuum Lean kernel-level proof HOLD; BEST physical reconstruction HOLD.**

## Inheritance

P7-R2 [exact rational continuum enclosure](mqr_4122_p7r2_exact_rational_continuum_kernel_certificate.md) asserts that, for an idealized uniform spherical source of radius a=0.05 m and three synthetic radial target shells, a no-oscillation kernel power series and a Taylor expansion of oscillation-weighted kernels enclose the continuum determinant away from zero. Previous [Actions #39365476706](https://github.com/WhoSia/MQR/actions/runs/39365476706) succeeded with scaled outward determinant interval [268306392369768/10^18,268306392369769/10^18]. Neither that result nor this check is real BEST detector reproduction.

## Independent derivation and computation

For n≥1 and source radius s∈[0,a], relative angle u∈[-1,1] uniformly, d²=r²+s²-2rsu. Let M_n(I)=∫_I dr r² E[d^(2n-2)] where source radial s density 3s²/a³.

P7 used angular endpoint/binomial differences. P8 independently expands (r²+s²-2rsu)^(n-1) by multinomial expansion, retaining only even powers k of u, E[u^k]=1/(k+1). For each even k and t=0..(n-1-k), after integrating source radius and target radius the rational term is

binom(n-1,k) binom(n-1-k,t) 2^k/(k+1) * 3 a^(k+2t)/(k+2t+3) *
  (rhi^(2(n-1)-k-2t+3)-rlo^(2(n-1)-k-2t+3))/(2(n-1)-k-2t+3).

The formula differs in derivation and loop structure from P7 endpoint formula. All computations use Python standard-library Fraction.

For all n=1..34 (including the Taylor remainder moment M34) in each of the 3 shells, 102 independently constructed exact rational results match the original endpoint moment formula **exactly**, not within tolerance.

## Evidence

- [P8 independent source](../experiments/mqr-4.122/p8_independent_angular_moment_audit.py)
- [Read-only successful CI #39369735918](https://github.com/WhoSia/MQR/actions/runs/39369735918), job log confirms `MQR_4122_P8_INDEPENDENT_MOMENTS_102_OVER_102=PASS`.
- No new branch, no GitHub Actions bot commits; read-only checkout, `contents: read`.

## Attack / scope

This check strengthens P7's finite-source moment identity, not a new direct independent implementation of the overall continuum determinant or complete analytic remainder-bound proof. The two implementations share the idealized uniform-ball source and shell assumptions. It does not address off-center sources, source-target overlap, actual BEST Fig. 8 shapes, isotope weights or experimental uncertainties.

## Writing Loop

WRITE: derive target-integrated moments by direct multinomial expansion in the angular variable and exact rational radial moments.
ATTACK: it is possible for mutually agreeing code to share wrong foundational assumptions; the two calculations also compare symbolic expansions of the same ideal geometry rather than independent laboratory data.
REVISE: present 102/102 exact checks as independent algebraic audit only, not newly independent physical reproduction or full formal Lean integration proof.
DRAFT-CLOSED: constrained mathematical replication receipt.
BACKLOG: prove general moment formula, positive series tail and cosine remainder in Lean (or independently check interval enclosures); obtain original BEST Fig. 8/CAD-compatible source-target mask before physical numerical reconstruction. Upload/readback science artifacts to their appropriate canonical Drive locations when available.

**VERDICT: P8 EXACT RATIONAL MOMENT AUDIT PASS; LEAN CONTINUOUS-KERNEL FORMALIZATION HOLD; BEST ACTUAL GEOMETRY HOLD; BOT_CONTRIBUTION_ZERO.**
