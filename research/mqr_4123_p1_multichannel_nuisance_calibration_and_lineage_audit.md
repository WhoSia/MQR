# MQR-4.123 P1 — Multichannel Nuisance Annihilation, Signal-Aligned Failure and Independent Calibration

**2026-10-20. P1 EXACT RATIONAL SYNTHETIC PASS; EMPIRICAL IDENTIFICATION HOLD.**

## Historian's audit / proof inheritance

- **4.113**: Blackwell–Le Cam comparison is a statement about statistical experiments/information order, not sameness of a physical world or instrument.
- **4.114–4.119**: measurement comparability, provenance, selection and community validation demand warrant beyond algebraic equivalence.
- **4.120**: JTPA selection and excluded observations illustrate estimand/data-admission failures; that case is not mathematically resolved by this P1.
- **4.121**: sensor calibration, nonlinear state and reference sufficiency; physical original optical spectral source records remain unverified here.
- **4.122 P4–P5**: equal-volume shapes can differ in no-oscillation response, and distinct occupancy profiles can share both volume and unoscillated response.
- **4.122 P6**: ideal finite-source oscillation-weighted discrimination in Rust, separate finite-rational Lean proof.
- **4.122 P7-R2**: exact-rational continuous uniform-source determinant strictly positive in [268306392369768/10^18,268306392369769/10^18] in one synthetic configuration; continuous analytical integration not yet kernel-proved in Lean.
- **4.122 P8**: 102/102 independent exact moment checks.
- **4.122 P9**: cosine-integral numerical alternative matches determinant but is not a second rigorous bound.
- **4.123 P0**: shared bias removed by pairing; instability/measurement error can defeat the contrast. Actual calibration validity not established.

This lineage is a **scope audit**, not a claim that every archive file has been reread in full during P1. The newest repository reports were directly inspected.

## P1 precise model and result

Define a 3-vector output Y_h=b n1+c n2+h g+e for H_h∈{H0,H1}, with
n1=(1,1,1), n2=(0,1,2), g=(3/10,0,3/10), unrestricted b,c∈Q (or R). Let w=(1,-2,1). Then

w·n1=0, w·n2=0, w·g=3/5.

Hence the contrast T=w·Y_h equals h·3/5+w·e, independent of b,c, as long as **the same n1,n2 coefficients generate all channels for each observation**. For coordinate-wise error |e_i|≤ε, |w·e|≤4ε. The possible T values under the two hypotheses are contained in [−4ε,4ε] and [3/5−4ε,3/5+4ε]. They are disjoint if 3/5>8ε. For ε=1/20, gap=1/5. This is a constructed deterministic instrument model, not an experimental observation.

**Signal-aligned nuisance erasure:** allowing an additional additive t g nuisance with unrestricted t, the same observable Y can arise from H0 and H1: choose t to shift by one unit. The nominal ideal signal's nonzero contrast is then not enough to discriminate.

**Independent calibration:** if t is independently restricted to |t|≤η=1/10 for each hypothesis, while |e_i|≤ε=1/20, then projected error radius is 4ε+(3/5)η=13/50. The prediction-set separation is 3/5−2(13/50)=2/25. This certificate is valid ONLY if the admissible t bounds are established **before** testing the rivals by independent calibration evidence, not fitted from the same experimental observations being used to claim discrimination.

**General finite-dimensional condition** (conditional mathematical statement): For a linear nuisance space N=im(A), there exists a linear contrast w annihilating all nuisance directions but preserving a hypothesis difference g iff g∉N. This is a standard annihilator theorem over finite-dimensional real vector spaces. Given bounded error set E, the projected possible sets separate if the contrast signal exceeds the projected error widths from both rivals. Presence of a contrast does not imply high finite-sample test power for unbounded error distributions.

## Execution receipt

[P1 exact rational source](../experiments/mqr-4.123/p1_multichannel_nuisance_contrast.py) / [read-only actual Actions #39396468299 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/39396468299). Exact fraction assertions include w·n1=w·n2=0, w·g=3/5, 1/5 robust margin, erasure by aligned nuisance, recovery margin 2/25 with independent bound, loss of separation under larger error. No GitHub Actions bot commits; main only.

## Attack and promotion safeguards

- **Calibration independence** is an evidential claim that cannot be created by mathematical stipulation. If the calibration comes from the same data or shares latent systematic uncertainties, the recovery certificate might not be physically valid.
- **Nuisance geometry** can be misidentified: an unknown direction outside assumed nuisance span could erase the witness.
- **Three-channel rank** is not equivalent to three independently measured information channels; common detector electronics and reference standards can make them redundant.
- **Data-level admission** remains unsatisfied for BEST, original 4.121 optical experiment, and JTPA.
- No individual scalar universally measures progress or research quality (inherit 4.53's stop-rule warning). No inflation of CI success into physical reproduction.

## Writing Loop
WRITE — construct nuisance-annihilating contrast and aligned-nuisance counterexample.
ATTACK — synthetic nuisance span may be underfitted; bounded errors and calibration ranges cannot be asserted experimentally without provenance; 1D contrast does not exhaust multivariate statistical testing.
REVISE — classify exact linear algebra P1 PASS_BOUNDED; physical calibration and statistical power HOLD.
DRAFT-CLOSED — conditional contrast / nuisance erasure and recovery theorem with exact sample witness.
BACKLOG — Lean exact algebra / abstract annihilator lemma; partially identified nuisance directions; multivariate correlated bounded sets; independently measured instrument calibration; distributional likelihood comparison and finite sample power; reconnect only after physical primary data.

**P1 VERDICT: EXACT MULTICHANNEL SYNTHETIC PASS / INDEPENDENT CALIBRATION CONDITIONAL / EMPIRICAL IDENTIFICATION HOLD / BOT_CONTRIBUTION_ZERO.**
