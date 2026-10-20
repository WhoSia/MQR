# MQR-4.122 P3 — BEST Response Reconstruction Boundary: Finite Emission Volume, Energy-Dependent Capture, and Non-Reproduction of Measured Path Lengths

**2026-10-20 · actual GitHub Actions numerical audit PASS; full BEST path lengths NOT independently reproduced; measured-data/ontology HOLD.**

## 1. Original-publication facts and formulas

Reference: Barinov et al., *Physical Review C* **105**, 065502 (2022), https://doi.org/10.1103/PhysRevC.105.065502 ; publisher-associated mirror https://arxiv.org/pdf/2201.07364 . Original Eq. (10) defines effective gallium path length as \(\langle L\rangle_j=\int_{V_j}d^3x/(4\pi d^2)\), with distance \(d\) between emission and capture positions; original source-volume averaging and actual target geometry are represented by their Monte Carlo implementation. Eq. (11) gives **52.03 ± 0.18 cm** inner and **54.41 ± 0.18 cm** outer based on \(10^7\) samples including apparatus dimensional uncertainties. Fig. 8 explicitly includes an empty inner-sphere segment and a re-entrant tube. Eq. (12) separately incorporates line-dependent neutrino capture cross section and energy-dependent survival probability; **cross section weights do not change a no-oscillation geometric path length** when \(L\) is defined through Eq. (10). Table IX lists Bahcall capture cross section **(5.81 +0.21/−0.16)×10⁻⁴⁵ cm²** per gallium-71 atom per source decay, with common correlated theoretical uncertainty.

The published *nominal* gallium volumes are **1.22545 m³ inner and 6.5561 m³ outer**. The measured and geometric masses are different and the collaboration explicitly tests sensitivity to the spherical wall thickness (0.50 cm nominal vs 0.68 cm). These geometry/model discrepancies are an evidentiary concern independent of nuclear cross-section modeling.

The 2022 paper's four emission energies and fractions (MeV, probability) are **(0.747, 0.8163), (0.427, 0.0895), (0.752, 0.0849), (0.432, 0.0093)**.

## 2. Independent audit implemented and actually executed

[Pure-standard-library Python](../experiments/mqr-4.122/p3_finite_source_geometry_and_line_cross_sections.py) implements a mathematically finite, uniform emission volume and quasi-Monte-Carlo source-to-target integration. It distinguishes:
- Inner **idealized spherical gallium region with a fixed 7.3-cm central spherical exclusion** from the *real* re-entrant-tube and nontrivial vessel wall. The cavity is a **predeclared toy sensitivity model** and is **not** a measured inner gallium boundary or a fit to the 52.03-cm target.
- Outer **ideal full cylinder minus ideal inner sphere**, omitting real pipe/channel offsets and wall dimensions.
- A finite mathematical source region with geometry sourced from the publication, versus a zero-volume centered mathematical point source.
- Energy-dependent cross-section numbers **(62.58, 26.72, 63.22, 27.14)×10⁻⁴⁶ cm²**, respectively, from *a different model and source*: Universe **7** (2021) 246, *Reactor Antineutrino Anomaly Reanalysis in Context of Inverse-Square Law Violation*, Table 4, https://www.mdpi.com/2218-1997/7/7/246 . Those values are **not identical to original BEST's adopted Bahcall aggregate**, so they are only a model sensitivity comparison and must not replace a BEST-authenticated cross-section table. Their emission-fraction-weighted sum is **5.9095274×10⁻⁴⁵ cm²**, about **1.713%** above the original BEST aggregate 5.81×10⁻⁴⁵ cm².
- In the oscillation-free case \(\langle L\rangle\) is **purely geometric**, so changing capture cross sections cannot cure a path-length mismatch. A change in line weights does alter the energy-averaged oscillation survival and predicted capture rates.

The code implements a deterministic low-discrepancy (Halton-type) integral, tests the limiting zero-volume source and ideal ray-integral outer cylinder. The workflow [.github/workflows/mqr-4.122-finite-source-geometry.yml](../.github/workflows/mqr-4.122-finite-source-geometry.yml) uses SHA-pinned checkout, \`persist-credentials: false\` and \`contents: read\`.

**Actually observed GitHub Actions [run #39345704705 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39345704705)** at head \`677f5de6ab803dd19879c415f87810ee4cf8f39f\` (job log read directly; 75,000 candidate points per zone):

| response | independently computed | collaboration original | difference |
| --- | ---: | ---: | ---: |
| Zero-volume centered source, **unrestricted solid inner sphere** | 66.75 cm | 52.03 ± 0.18 cm | +14.72 cm |
| Zero-volume centered source, ideal cylinder-minus-inner-sphere outer zone | 55.429495 cm | 54.41 ± 0.18 cm | +1.019495 cm |
| **Finite mathematical source**, inner *idealized 7.3 cm spherical hole* | **60.170541 cm** | **52.03 ± 0.18 cm** | **+8.140541 cm** |
| **Finite mathematical source**, outer cylinder-minus-sphere | **55.457997 cm** | **54.41 ± 0.18 cm** | **+1.047997 cm** |

At fixed toy oscillation parameters \(\sin^2(2\theta)=0.4\), \(\Delta m^2=10\ \mathrm{eV}^2\), four-line cross-section weighted **toy survival** is **0.791281 inner**, **0.803598 outer**. These are **not actual BEST observed/expected event ratios**, and are not a likelihood fit. The code prints **\`MQR_4122_FINITE_SOURCE_INTEGRAND_TEST=PASS\`** and **\`MQR_4122_INDEPENDENT_FULL_GEOMETRY_REPRODUCTION=HOLD\`**; do not misread success of the *software run* as matching the paper.

Additional shape-consistency audit: idealized toy inner volume **1.244154 m³** vs original **1.22545 m³** (+1.526%); idealized toy outer volume **6.637312 m³** vs original **6.5561 m³** (+1.239%). A seemingly small volume error can have a larger effect on \(1/d^2\)-weighted inner path length if near-source emptiness/re-entrant-tube geometry is wrong.

## 3. Strict interpretation and physical failure conditions

The strongest result is **quantified non-reproduction**, not a successful independent BEST reproduction. Two models can have similar total volume yet different effective path lengths because the integrand is strongly position-sensitive. The inner gap is not legitimate evidence of an error in the published collaboration: the mathematical toy geometry does not implement their Fig. 8. Neither a spherical exclusion radius tuned to 52.03 cm, nor a cross-section renormalization tuned to an expected event rate, would be a valid independent calibration.

The original paper explicitly reports nontrivial wall thickness / re-entrant tube geometry and a spatial Monte Carlo. The source PDF Fig. 8 was text-searchable but direct image retrieval was not reliable in this environment; the figure's full geometric contour was not faithfully digitized. **No missing dimensions were silently invented**. Missing current tasks: capture the original diagram with readable annotations; replicate actual available target volume and mass before comparing path lengths; handle finite emission region together with exact excluded target geometry; verify Monte Carlo seed and convergence; separately verify line-dependent nuclear cross section from original primary nuclear sources and propagating correlated uncertainties; only then test oscillation and no-oscillation event counts. A separate study might need original computational geometry or numerical data from collaborators.

## 4. Research-OS / epistemology

This is a concrete case of the distinction between **reproducible computation, source-grounded calibration, and target-level inferential warrant**. The numerical method and unit tests run, but the precise source-to-target geometry is not yet empirically or documentarily reproduced. The residual is a *representation and input completeness* limit, not a discovery of new physics or proof of error by BEST. This yields a useful philosophical negative result: reproducing the published outer diameter, nominal energy lines and a small cross-section perturbation does not imply reproduction of a source-sensitive observational functional.

**Writing Loop state: WRITE→ATTACK→REVISE/HOLD→DRAFT-CLOSED; mathematical audit complete, physical input gap unresolved.** Next: original Fig. 8 contours and primary line capture cross-section model, NOT more governance paperwork.
