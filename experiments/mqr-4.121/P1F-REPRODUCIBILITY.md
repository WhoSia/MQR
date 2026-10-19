# MQR-4.121 P1F — reproducibility contract (synthetic only)

## Provenance
- Canonical Zong et al. (2006) source: DOI 10.1364/AO.45.001111, equations 1–10; original archived in Research OS 10_PAPERS.
- Executable: [p1f_outside_range_identifiability_stress.py](p1f_outside_range_identifiability_stress.py)
- Runs in Python with NumPy. Local tested environment: Python 3.13.5 / NumPy 2.3.5, 2026-10-19. The code is not coupled to local paths or private data.
- Command: `python experiments/mqr-4.121/p1f_outside_range_identifiability_stress.py`.
- Fixed random seed `4121` and 20,000 independent Gaussian noise draws. Std calculation is sample std (ddof=1).

## Acceptance checks executed locally
1. Signal-domain matrix inversion with correct D and no off-array q recovers true in-band intensity within 1e-14 absolute tolerance.
2. A second different true physical-intensity vector and a nonnegative q vector produce identical in-model observations.
3. 20,000-trial noise Monte Carlo agrees with first-order covariance propagation within rtol=0.07 for all three absorbance channels.
4. Any nonpositive inferred intensities cause the log-transform check to reject the input.

## Reference outputs (synthetic)
- 2-norm condition number of I+D: 1.0354767965325962.
- First-channel absorbance bias with q=[0.0008, 0.0004, 0.0002]: -0.033173566 AU.
- First-channel bias with Dhat=0.8 D: -0.020765178 AU.
- Empirical absorbance SD: [0.000434796, 0.0000431994, 0.0000087371] AU.
- First-order predicted SD: [0.000434424, 0.0000434466, 0.0000086878] AU.

## Failures, applicability and things not established
- This proves no physical property about a real optical instrument. The model treats q as a free additive nonnegative vector, while an actual off-array light spectrum depends on filter, grating, source, wavelength and geometric constraints.
- A bounded condition number does not certify that the operator was accurately calibrated or that an unknown term vanishes.
- The same observable intensity is not enough to determine whether chemistry or optics changed. Do not use this as a chemical-species assay or a Kuhnian revolution classifier.
- No real Zong LSF/D matrix or Griffiths–Potts detector trace was obtained. GitHub Actions were not executed for this script; **local execution PASS_BOUNDED / external CI HOLD**.
- A physical pilot needs independent laser characterization of D, a source cutoff that bounds q, calibrated blank/dark/reference, matched sample history, independently measured chemistry and blinded/replicated controls. Any measured claim must have actual instrument provenance and uncertainty.
