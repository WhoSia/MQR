# MQR-4.122 P6 — Finite-Source Observation Kernels and Oscillation-Weighted Geometric Separation

**2026-10-20 — P6 BOUNDED MATHEMATICAL/CI PASS. Actual BEST geometry and physical identification HOLD.**

## Authority and inheritance

- Inherit P4 equal-volume / different-inverse-square-path counterexample, actual CI #39347026768, without redefining it as BEST replication.
- Original primary-source target: Barinov et al., *Physical Review C* **105**, 065502 (2022), DOI https://doi.org/10.1103/PhysRevC.105.065502 ; original 52.03 ± 0.18 cm (inner), 54.41 ± 0.18 cm (outer).
- The current P6 code and proof are **constructed** models; the original Fig. 8 target mask, re-entrant tube, finite chromium source construction, real isotope capture factors and covariance are **NOT** reconstructed.
- Read-only independent GitHub Actions run [#39351160949](https://github.com/WhoSia/MQR/actions/runs/39351160949), HEAD \`0ea8999620f7b623396c8c919c3238f1d850319f\`: Rust 5/5 test PASS, Lean 4.24 lake build SUCCESS. Initial failed run [#39351004610](https://github.com/WhoSia/MQR/actions/runs/39351004610) found quadrature resolution intolerance (5.54e-5 > 5e-5) and missing Lake manifest. Both repaired openly, not hidden.

## Definitions and units

Let S and G be emitter and target sets in 3D, source probability density rho(s) integrate to 1, where rho has unit m^-3. For source-target distance d=|x-s| in metres, define the no-oscillation path functional

L_S(G) = integral_S rho(s) integral_G [1/(4 pi d²)] d³x d³s, in metres.

For an energy channel with survival probability P_ee(d,E;theta), define

L_S(G; E,theta) = integral_S rho(s) integral_G [P_ee(d,E;theta)/(4 pi d²)] d³x d³s.

Expected capture weights sum over lines p_i sigma_i L_S(G;E_i,theta); p_i are branching fractions and sigma_i are capture cross sections. Nuclear capture weights do NOT change the no-oscillation geometric length L_S(G).

For a uniform emitter ball S=B_a(0), a=0.05 m, and target radii r>a, the averaged spherical-shell kernel becomes

K_0(r) = integral_0^a (3s²/a³) (r/(2s)) log[(r+s)/(r-s)] ds
       = (3r/(2a³)) [ra + (a²-r²)/2 * log((r+a)/(r-a))].

The singular s=0 expression uses its continuous limit. This kernel is dimensionless and multiplies dr to yield metres. The restriction r>a excludes overlap of emitter and target; no singular-geometry numerical verification is claimed.

For synthetic survival P(d)=1-A sin²(kappa d), amplitude A=0.55 and kappa=8 rad/m, the oscillation kernel is

K_A,kappa(r)=integral_0^a ds (3s²/a³) integral_-1^1 du/2
  [r²/(r²+s²-2rsu)] [1-A sin²(kappa sqrt(r²+s²-2rsu))].

These are mathematical fixture parameters, not BEST fit parameters.

## Exact identifiability condition for radial occupancy

Suppose q(r) is the occupied solid-angle fraction of the target at radius r (0<=q<=1). Isotropy of the centered uniform source makes the forward kernel radial. Divide the target into three radial intervals I_1=[.20,.34], I_2=[.34,.49], I_3=[.49,.65] m with piecewise-constant occupancy q_j.

Set vectors V_j=4pi/3 (r_hi³-r_lo³), B_j=integral_Ij K_0(r)dr, C_j=integral_Ij K_A,kappa(r)dr.

Volume V(q)=V·q, no-osc L(q)=B·q, oscillation-weighted L_osc(q)=C·q.

**If det[V;B;C] != 0**, choose h=V×B !=0 and q±=(1/2,1/2,1/2) ± 0.3 h/||h||_infinity. Then all cell occupancies lie in [0.2,0.8], and V(q+)=V(q-), B(q+)=B(q-) exactly in the defining continuum integrals, yet C(q+)-C(q-)=0.6 det[V;B;C]/||h||_infinity != 0 (up to determinant orientation). This is elementary finite-dimensional linear algebra, not a novel universal physical law. If C lies in span(V,B), such a separation is impossible within this three-cell family.

The numerical implementation evaluates B by midpoint integration of the exact source-averaged K_0 and C by nested midpoint integration over source radius, relative angle, and target radius. It chooses the cross-product null vector of the numerical V and B, so the near-zero numerical equalities are not a rigorous bound on continuum quadrature error.

## Actual Rust execution and scope

Source: [continuous uniform-ball Rust fixture](../experiments/mqr-4.122/p6_finite_ball_oscillation_witness.rs).

The successful CI receipt reports:
- q_plus=(0.306197683570184, 0.8, 0.3889211580975371).
- q_minus=(0.6938023164298159, 0.2, 0.6110788419024629).
- volume difference 1.110223024625e-16 m³.
- no-oscillation path difference 2.775557561563e-17 m.
- oscillation-weighted path difference 0.02820016032888 m.
- Rust 5/5 tests PASS, including zero-kernel numerical check and refinement test.

These near-zero residuals are machine/quadrature-scale, NOT empirical volume measurements or certified 3D geometric input.

## Formal Lean proof: intentionally different abstraction layer

Source: [Lean 4.24 exact rational finite-support witness](../experiments/mqr-4.122/lean/MQR4122P6.lean), [project manifest](../experiments/mqr-4.122/lean/lake-manifest.json).

Two discrete equally weighted source atoms at s=-1,+1, detector cells at x=2,3,4, and discrete inverse-square responses B=(5/9,5/32,17/225). For the phase grid kappa=pi/2, sine-squared weights at integer distances are 0 or 1 by parity, giving an oscillation-suppressed part D=(5/9,0,17/225). The formal file treats these rational values as pre-evaluated constants, and does not prove analytical sine identities.

Define h=(B_2-B_3, B_3-B_1, B_1-B_2), and q±=(1/2,1/2,1/2) ± h/4. Exact rational arithmetic in Lean proves:
- q+ != q-, occupancies 0<=q±<=1.
- equal cell capacity/volume and equal no-oscillator flux.
- for survival 1-(1/2) sin²(kappa d), exact oscillation response difference = -3/160 (common physical factors omitted).
- a genuinely discriminating additional observation separates the combined records.

This establishes exact **finite-support discretized** separation, NOT formal verification of the continuum uniform-ball integral, real BEST target, uncertainty, or experimental inference.

## Writing Loop

**WRITE:** formulate the finite-emitter forward operator, isotropic uniform-ball shell kernel, and constrained nullspace-separation witness; add separate exact finite-support Lean proof.

**ATTACK:** continuum Rust near-zero constraints depend on quadrature; the Lean witness is a different discrete source with parity-evaluated oscillation weights; the real BEST source-target mask and isotope spectrum have not been ingested. An isolated synthetic separation does not imply sufficient statistical precision or unique reconstruction in BEST. CI success alone cannot authorize physical conclusions.

**REVISE:** state continuum and discrete theorems separately; quantify code convergence and first-run errors; preserve all experimental HOLDs and do not tune geometry toward published BEST paths.

**DRAFT-CLOSED (bounded):** Mathematical linear-algebra identifiability condition and two reproducible witnesses complete; physical reconstruction and independent interval-certified continuum integrals remain BACKLOG.

**BACKLOG:** (A) first obtain and validate Fig. 8/CAD-like target mask/filled gallium volume and wall/re-entry geometry, source distribution and original source branch provenance; then independently reproduce V, L_inner=52.03 cm, L_outer=54.41 cm with quantified convergence. (B) optionally extend continuous integral to interval-certified numerical enclosures and direct Lean proof of the analytic kernel or rank criterion, rather than treating numerical coincidence as a theorem. (C) only then test whether survival-weighted channels separate physical models under original measured uncertainties/covariance.

## Governance and provenance

The Actions workflow is read-only, checkout credentials not persisted, no GitHub Actions bot commits, no new branch. All GitHub source mutations come from authenticated WhoSia connector actor. GitHub is code/CI evidence, Notion is research judgement, Drive is source-byte archival authority. A paper/CI receipt is not real-gallium empirical identification.
