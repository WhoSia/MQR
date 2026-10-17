# MQR-4.121 P1A — Two Physical Routes to Nonlinear UV–Vis Absorbance

**2026-10-18 · Conceptual/analytical worked example · no laboratory observations claimed.**

## Point
An absorbance–concentration curve that bends below the monochromatic Beer–Lambert line need not uniquely diagnose either a failed chemical law or a faulty instrument. Two distinct physical/instrument models can share the same qualitative curvature while making different predictions under a controlled change in optical bandpass, wavelength, or added information. This reconstructs the original MQR question of what a reported number *licenses*, using existing spectrophotometry and standard mathematical calculus.

### Route I — nonabsorbed stray light
With true monochromatic A(c)=k c (c in arbitrary concentration units, k inverse units) and true T=10^{-kc}, assume fractional stray light s>=0 compared with reference signal:
T_obs(c)=[10^{-kc}+s]/[1+s],
A_obs(c)=-log10(T_obs(c)).
For k>0 and s>0,
A_obs'(c)=k 10^{-kc}/[10^{-kc}+s]>0,
A_obs''(c)=-(ln 10) k² s 10^{-kc}/[10^{-kc}+s]^2<0.
Thus A is concave and approaches a finite asymptote -log10[s/(1+s)] at high c. This is a simplified model; stray fractions can vary with wavelength, optical configuration and sample properties. An apparent plateau does **not** prove a specific cause.

NIST/NBS donor *Accuracy in Analytical Spectrophotometry*, SP 260-81, https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication260-81.pdf ; first-party digital search excerpt describes negative Beer–Lambert deviations from unabsorbed stray light and bandpass-related errors. The PDF open timed out and original-page screenshot was **not** verified this session. More specific spectroradiometer correction technology is described by NIST Zong et al. (2007) https://www.nist.gov/publications/correction-stray-light-spectroradiometers-and-imaging-instruments and Zong (2010) https://www.nist.gov/publications/analysis-uncertainties-stray-light-correction . Do not conflate instruments.

### Route II — finite spectral bandwidth, perfectly linear underlying species
For finitely many spectral channels i with individually Beer–Lambert-ideal attenuation, positive reference weights w_i summing to one, and k_i=ε_i ℓ>0,
T_band(c)=Σ_i w_i 10^{-k_i c},
A_band(c)=-log10 T_band(c).
Define conditional weights
p_i(c)=w_i 10^{-k_i c}/Σ_j w_j 10^{-k_j c}.
Differentiation gives
A_band'(c)=Σ_i p_i(c) k_i,
A_band''(c)=-(ln 10) Var_{p(c)}(k_i) <= 0.
Proof: differentiate log partition function; p_i' = -ln(10) p_i(k_i - E_p[k]), hence derivative of E_p[k] equals -ln(10) variance. The curvature is strictly negative whenever at least two distinct k_i retain positive weight. **Each wavelength component obeys the linear physical attenuation law; the nonlinearity appears when mixed intensities are logged.**

Jensen also implies A_band(c) <= c Σ_i w_i k_i for c>=0, equality only with degenerate k values or c=0. For all k_i>0, A_band(c) grows unbounded as c→∞, asymptotically at min_i k_i, unlike the simple positive-constant-s stray-light saturation. However, if a band includes k_i=0, finite-bandpass transmission may also plateau. Moreover finite detector dynamic range can defeat asymptotic discrimination. **Curve shape alone and a short concentration range do not give robust mechanism identification.**

### Independently calculated finite example
Take w=(1/2,1/2), k=(1,3). Calculated values (not observed):
| c | A_band(c) | naive mean-coefficient prediction 2c |
|---:|---:|---:|
| 0.25 | 0.4316989476 | 0.5 |
| 0.5 | 0.7596373105 | 1 |
| 1 | 1.2967086219 | 2 |
| 2 | 2.3009865684 | 4 |
| 3 | 3.3010295614 | 6 |
At c=0.75, p≈(0.96934657,0.03065343), A'≈1.06130686 and A''≈-0.27367419. A centered finite-difference derivative at step 10^-4 gives -0.27367422; agreement confirms the arithmetic illustration, **not** a science experiment.

For stray light choose s=0.01, k=2: at c=1 A_obs=1.7032913781; a no-stray instrument measuring an alternative monochromatic sample with k=1.7032913781 has exactly the same single displayed A. At c=1/2 their conditional predictions diverge: 0.9629286886 versus 0.8516456891. This **conditional separation** depends on linear concentration scaling for each physical model. It does not establish which explanation holds in any real sample.

## A third physically distinct rival: solution chemical equilibria
Griffiths and Potts (1974), *Analytica Chimica Acta* 71(1):1–16, DOI 10.1016/S0003-2670(01)82866-X, accessible abstract reports that methyl red spectra varying with pH/temperature can be understood using three solution species and a pseudo-two-species equilibrium. Therefore an isosbestic-looking pattern, even with a sensible fit, is not automatic evidence for exactly two molecular species. **2026-10-18 P1B source-state correction:** The complete 16-printed-page paper PDF is now VERIFIED OWNED and its text close-read in [P1B-I](mqr_4121_p1b1_griffiths_potts_1974_annotated_close_read.md). Its Tables I–III/figures still need visual parity checks; original digitized spectrum arrays were not located, so numerical curve reconstruction and independent chemical species identification remain HOLD. Earlier 'not source-owned' statement is superseded, not erased from Git history.

## 1.12–1.15 interpretations and measurement paths
1.12: optical bandpass adjustment followed by dilution need not lead to the same mathematical summary as dilution followed by a sample-changing chemical intervention. Explicitly identify when experiment order is interchangeable and when physical kinetics/equilibrium introduce order dependence. Mere noncommutation is not a failure.
1.13: pH or heating interventions may modify the relevant species definition; an intervention is physically realizable without preserving an earlier two-species model.
1.14: a vial may remain the same tracked specimen while constituent chemical forms/species change. Material continuity does not guarantee *species-concentration* predicate continuity.
1.15: if a pH/temperature cycle restores A but not next-step response, test for a compact measurably anchored internal variable and controlled drift before calling the difference irreducible history. The magnetic random-field Ising return-point memory result (Sethna et al. 1993, DOI 10.1103/PhysRevLett.70.3347) is an **analogical donor, not evidence that this chemical system has memory**.

## Three positive experimental discriminators, no premature causal claims
- Instrument: independent spectral-line spread / spectral bandwidth / stray-light characterization and matched cuvettes; two instrument configurations can help separate an instrument-specific distortion from sample-state explanation.
- Physical sample: multi-wavelength spectra, controlled pH and temperature histories, independent chemical/speciation measurement; explicitly verify pre/post sample identity and measurement scope.
- Prospective prediction: fit candidate mechanisms on one domain, freeze them, then challenge in a held-out condition using a prediction that the competing mechanism does not automatically share; compare with original successful normal domain too.

## Limits / paper custody
This work is **a rigorous, cited synthesis and finite mathematical reconstruction**. It adds a useful explicit pair of mechanisms to MQR's original question but does not claim an unprecedented mathematical theorem, actual spectra acquisition, calibrated stray-light coefficient, or hysteresis measurement. MQR-4.121 ACTIVE / P1A analysis ready; P1 source custody and physical evaluation remain HOLD. In Drive search, canonical copies of the 1974 Griffiths–Potts complete paper, NBS SP 260-81, NIST Zong 2007/2010 and Sethna 1993 were not confirmed, although search misses do not prove absence.
