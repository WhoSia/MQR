# MQR-4.122 P4 — Equal Target Volume Does Not Identify Inverse-Square Effective Path Length

**2026-10-20 · independently executed mathematical counterexample PASS; original BEST source-target geometry reproduction HOLD.**

## Exact source distinction

BEST original technical paper: Barinov et al., *Physical Review C* 105, 065502 (2022), DOI https://doi.org/10.1103/PhysRevC.105.065502 , especially Fig. 8, Eq. (10)–(12) and Table IX; [public NIST-hosted article](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=934459). Original published effective paths are 52.03 ± 0.18 cm inner and 54.41 ± 0.18 cm outer. Original *nominal calculated* gallium volumes are 1.22545 and 6.5561 m³, while physical weighed masses and geometric masses are not identical. The article identifies an empty segment of the sphere associated with the thickened inner wall and end of a re-entrant tube, and discusses sensitivity to spherical wall thickness (nominal 0.50 cm, alternative 0.68 cm). These are source-reported facts and cannot be substituted with a spherical cavity invented by MQR. The text describes 10⁷-sample numerical integration. We attempted direct web PDF screenshots of Fig. 8, but the renderer returned a cache error; no reliable visual tracing of contour coordinates was completed.

## Mathematical counterexample and closed-form proof

For a **mathematical point at the center of an otherwise ideal spherical region** of radius R, the inverse-square path functional is (L=int_V d^3 x/(4pi r^2)). A complete radial spherical shell [a,b] has volume (Delta V=(4pi/3)(b^3-a^3)), but its contribution to path length is (Delta L=b-a). Thus (Delta V) does not determine (Delta L); radial location matters. This is a deterministic theorem for the stated simplified model, not a claim to BEST's real re-entrant tube.

At R=0.6675 m, choose **equal hypothetical missing volume** ΔV=0.015 m³:
- near source: shell starts a=0.10 m and ends at b≈0.16608088935 m, removes 6.608089 cm effective path length;
- farther away: shell starts a=0.50 m and ends at b≈0.50472976585 m, removes 0.472977 cm path length;
- in both idealized cases remaining target volume = 1.230783055 m³; paths respectively 60.141911 and 66.277023 cm. **Path difference = 6.135112 cm at strictly identical target volume**.
- Original BEST inner volume 1.22545 m³ and inner path 52.03 cm are reference values only; neither constructed geometry equals the original target and these shells were not tuned to reproduce it.

**Source / execution:** [pure standard-library Python and independent midpoint integration](../experiments/mqr-4.122/p4_equal_volume_distinct_inverse_square_paths.py) and [actual read-only CI run #39347026768 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39347026768). Read CI job logs confirmed `MQR_4122_P4_EQUAL_VOLUME_LOCATION_COUNTEREXAMPLE=PASS`, the exact volume/path numbers, and `MQR_4122_P4_ACTUAL_BEST_PATH_REPLICATION=HOLD`. SHA-pinned checkout and `contents: read`, no workflow write permission.

## Consequence for the previous P3 numerical run

Earlier P3 [finite-source mathematical audit](mqr_4122_p3_finite_source_ga_capture_and_best_path_length_gap.md) computed toy 60.170541 cm inner / 55.457997 cm outer against published 52.03 / 54.41 cm; these are **not** independent BEST reproduction. The simulated *spherical* inner cavity of 7.3 cm was never substantiated as the real re-entrant tube. The P4 theorem explains why its near-source position and contour can matter much more to inverse-square response than 1–2% total volume differences would suggest. **It does not establish that the full P3 residual is due to the re-entrant tube**: source emission distribution, vessel walls, actual target mask and numeric estimation details remain uncoupled.

Likewise, line-dependent cross section weights change oscillation-averaged capture predictions, but they do **not** change the no-oscillation geometric path functional defined by original Eq. (10). Do not fit the published path by changing the nuclear cross sections.

## Writing Loop: write / attack / revise / close

**WRITE:** prove the nonidentifiability of an inverse-square geometric functional from volume alone, with exact two-shell counterexample checked independently by numerical integration.

**ATTACK:** realistic BEST has a finite, non-point source and a complicated nonspherical, partially empty target; a spherical-shell counterexample cannot identify its particular missing geometry, and equality of volume is insufficient to specify spatial response in either case.

**REVISE:** do not claim a BEST path-length reproduction, prove only that volume agreement cannot certify it. Even a volume-matched toy can differ dramatically in source-weighted response. No path-fitting, undocumented replacement dimensions, or hypothetical cavity promoted as observed.

**DRAFT-CLOSED:** a mathematical and methodological negative result; **BEST source/target geometry and observed physical rates remain HOLD**.

**BACKLOG:** review original Fig. 8 at readable visual resolution; obtain an independently documented spatial target mask/available CAD in source scope; verify total gallium volume and surface geometry *before* computing path; only after complete geometry, compare finite-source response and uncertainty/convergence. This task does not require adding another governance layer or a universal progress index.

## Research-OS lesson

Scientific reconstruction is not achieved by matching easy observables like total volume while leaving source-sensitive spatial response underdetermined. The strength of a calculation depends on the representation being right for the target functional. The result is a formal model sufficiency counterexample, not an empirical verdict about BEST or a scientific crisis.
