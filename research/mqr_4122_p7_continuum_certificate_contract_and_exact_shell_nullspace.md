# MQR-4.122 P7 — Continuous-Kernel Certification Boundary and Exact Shell Nullspaces

2026-10-20. **FORMAL ALGEBRA PASS; VERIFIED CONTINUUM INTEGRAL ENCLOSURE HOLD.**

## Inherited authority
P6 Rust continuous-uniform-ball forward approximation and exact discrete-source Lean witness: https://github.com/WhoSia/MQR/blob/main/research/mqr_4122_p6_finite_source_oscillation_kernel_and_nullspace_witness.md . Original physical BEST geometry reproduction and oscillation attribution HOLD.

## Completed this stage
Extended `experiments/mqr-4.122/lean/MQR4122P6.lean` by introducing abstract shell-weight triples, `dot3`, `cross3`, and explicit exact rational tests:
- the null vector is orthogonal to volume;
- it is orthogonal to the no-oscillation shell weights;
- the independent oscillation shell weights do not annihilate the null vector.
Lean 4.24 compile: read-only GitHub Actions [#39352862925](https://github.com/WhoSia/MQR/actions/runs/39352862925), SUCCESS. This proves the algebraic **post-integration** witness for exact rational shell weights, not that a continuous 3D physical integral equals those weights.

## Rigorous continuum certificate contract (NOT YET SATISFIED)
For a fixed centered source S=B_a, a=0.05 m, and three radial target intervals I_j, define exact continuum weights

B_j = ∫_{I_j} K_0(r) dr,
C_j = ∫_{I_j} K_{A,kappa}(r) dr,
V_j = 4π/3 (b_j³-a_j³).

K_0 and K_{A,kappa} are explicitly defined in P6 and do not assume BEST geometry. We must compute rational outward bounds [B_j^-, B_j^+] and [C_j^-, C_j^+] by a mathematically justified integration algorithm. A valid certificate consists of (i) exact/reproducible rational endpoints and covering proof; (ii) controlled Taylor/analytic-truncation and quadrature errors; (iii) interval evaluation of D=det([V;B;C]) excluding zero and checked without unsafe floating rounding; (iv) computed occupancy bounds 0≤q_j≤1. Numeric refinement alone, or choosing h from an approximate B vector, does not certify exact no-oscillation equality for the continuum model.

An algebraic sufficiency condition is D≠0; taking h=V×B gives V·h=B·h=0 and C·h=D up to cross-product orientation. For q±=1/2 ± εh with ε>0 small enough to maintain occupancy bounds, the two volumes and baseline responses agree exactly and the additional channel differs by 2εD. This is a conditional theorem; a certified enclosure D∈[d-,d+] with 0 outside is still required.

## Writing Loop
WRITE: formalize shell-integrated kernel linear algebra independently of any finite quadrature grid.
ATTACK: pre-evaluated rational Lean weights are not continuous integrals; double-precision output and convergence comparisons are not self-validating.
REVISE/HOLD: preserve finite-support formal success and separate continuum interval validation as unsatisfied obligation.
DRAFT-CLOSED: conditional analytic theorem and exact rational shell-nullspace example.
BACKLOG: prove kernel analytic representation on r>a; implement interval-safe source radius/angle/radial integration; calculate outward determinant range; only after this claim continuum validated. BEST Fig. 8 exact mask and physical fit remain separate HOLD.

## Candidate missing literature (Drive exact title search on 2026-10-20; no matching title confirmed)
- Fredrik Johansson (2018), *Numerical integration in arbitrary-precision ball arithmetic*, https://arxiv.org/abs/1802.07942
- Knut Petras (2002), *Self-validating integration and approximation of piecewise analytic functions*, https://doi.org/10.1016/S0377-0427(01)00586-6
- Fredrik Johansson (2017), *Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic*, https://doi.org/10.1109/TC.2017.2690633
- Fredrik Johansson and Marc Mezzarobba (2018), *Fast and Rigorous Arbitrary-Precision Computation of Gauss–Legendre Quadrature Nodes and Weights*, https://doi.org/10.1137/18M1170133
- Original BEST primary technical paper, Barinov et al. 2022, https://doi.org/10.1103/PhysRevC.105.065502 (already considered, do not duplicate).

Final authority: P7 LEAN ALGEBRA PASS / CONTINUUM INTERVAL CERTIFICATION HOLD / BEST GEOMETRY HOLD / BOT_CONTRIBUTION_ZERO.
