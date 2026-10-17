# MQR-4.121 P1B-II — NBS (1983) 140pp reading map, Zong 2007/2010 and operator-order audit

**2026-10-18. Source status:** All three canonical PDF byte objects already located under Research OS 10_PAPERS. This entry is a selective, section-grounded first tranche for the 140pp NBS book plus a body-text reading of both Zong papers. **Not a claim that every appendix page was inspected, nor permission to reproduce sources verbatim.**

## Canonical source objects
- [Burke & Mavrodineanu (1983), NBS SP 260-81, Accuracy in Analytical Spectrophotometry](https://drive.google.com/file/d/1nKOizJsxxrf_b8M8BmPe82s_bBOT8xbY/view) (9,083,273 bytes; 140 printed pages; NBS first-party archival publication). Text length ~390,406; front matter, complete TOC, Parts I/II outline and selected Part I technical sections examined. Table/image fidelity not yet checked.
- [Zong, Brown, Lykke & Ohno (2007), CIE Beijing, Correction of Stray Light in Spectroradiometers and Imaging Instruments](https://drive.google.com/file/d/1kCcVlmzuiBZrWCtoAo2Q-VnEVebuj-7b/view) (~549,690 bytes); original text readable; section 2 spectral/spatial calibration, source tests, section 3 application.
- [Zong (2010), CIE x036, Uncertainty Analysis of Stray-Light Correction](https://drive.google.com/file/d/1ZdD7HYmmyp24-AoEuuGj7Ov2DILWvwGr/view) (32,080 bytes); main uncertainty taxonomy and LED source comparison read.

## NBS 140-page source: explicit division and completeness audit

### Intake/volume audit
Printed volume **140 pages**, but TOC divides its own central authored exposition into PART ONE (printed pp.1–32) and PART TWO (printed pp.33–43), with certificates and selected publications appended afterwards. **140pp != 140 pages of continuous main argument.** The correct reading unit is chapter/figure/table, not arbitrary fixed byte count. Front matter TOC is readable even where PDF formatting/OCR is irregular.

### Reading tranche A — Part I §§1–2.1 (pp.1–7), checked by text
Authors distinguish multiple major sources of spectrophotometric uncertainty: wavelength setting, spectral bandpass, optical radiation path length, stray radiant energy, and transmittance scale. They built a dedicated NBS high-accuracy single-beam spectrophotometer (completed circa 1970 in the document's chronology) to validate these factors and support SRM certification. Instrument organization includes radiation source, monochromator (a pre-dispersing prism/double monochromator arrangement to reduce stray radiation), specimen and blank control, integrating sphere/photomultiplier, current-to-voltage measurement and digital readout. A radiation addition / two-aperture arrangement checks detector response linearity.

**Notebook:** This is not a single scalar 'machine accuracy' datum. Each constituent error mechanism can alter the forward kernel differently. Inverse chemical claim validity must be tracked through **instrument architecture**, not merely mathematical absorbance transformation. A nominal instrument readout that is well calibrated at some wavelengths is not necessarily transportably accurate at all sample spectra.

### Reading tranche B — Part I §2.2 SRM family (pp.7–29), selected paragraphs + TOC checked
The volume distinguishes physical standards with different transfer functions: SRM 930 visible glass filters (approximately 440–700nm), SRM 931 liquid absorbance standard for UV contact, SRM 932 quartz cuvette path-length specification, SRM 935 potassium dichromate requiring accurate prepared solution and known path length, and metal-on-quartz/didymium-type or related filter/wavelength checks in subsequent subsections. The **explicit limitations** subsection §2.2.6 (printed p.25) acknowledges that no one SRM covers every range/parameter: visible-only glass, limited UV calibration points, preparation and geometry burdens for solution reference standards. The document also discusses transmittance transfer between NBS and UK's NPL, and selected inter-center comparisons.

**Notebook:** Calibration and traceability are typed and *parameter-specific*. Source 4.114 CCQM lesson reappears in the earlier material world: same word 'standard' need not imply same measurand, range, geometry or independence. This is a **strong existing literature connection**, not a MQR exclusive novel claim. Audit standard authorization for the spectral neighborhood actually used.

### Reading tranche C — Part II §§5–9 (pp.33–43), heading/figure inventory only, full close-read STILL OPEN
Part II turns to cuvettes, temperature control, selected assays and reference-method comparisons for antimony/arsenic, nickel, copper and simultaneous Co/Ni/Cu. Lists original figure/table targets: cuvette rinse reproducibility; 20-month K2Cr2O7 solution stability; temperature difference between bath and actual cuvette; nickel SRM comparison and IDMS; simultaneous multielement determinations. Those are **excellent** choices for source-grounded physical coupling and measurement comparability. **DO NOT label their values replicated yet.**

### Reading tranche D — appended reprints and calibration certificates (after main pp.43; many of the 140 printed pages), NOT READ
The foreword states the appendices reproduce selected related publications and SRM certificates. Requires page/record-level catalog, extraction and visual inspection before treating any appended certificate as contemporaneously applicable to a particular apparatus. Do not conflate NBS-1983 certificates with later NIST revisions.

## Zong et al. 2007: detailed mechanism and reported performance
- §2.1: characterize an instrument using **line-spread functions** (LSFs) from near-monochromatic line sources; derive stray-light distributions, interpolate and form spectral correction matrix C_spec; apply to **raw signal vector** y_raw. Recompute when dispersion/scattering behavior changes.
- §2.2: similar method for imaging instrument **point-spread functions** (PSFs), corrected on vectorized spatial raw response with separate C_spat. Spectral and spatial matrices are **not interchangeable**.
- Authors report example using CCD array device and a green bandpass filter: below ~420nm, raw relative spurious signal of order >4e-4 reduced to order 5e-6. Another UV calibration example at 300nm: reported spectral stray-light calibration error ~32% reduced below 1% after correction. These are author-reported **specific instruments, sources and validation regimes**, not universal certified error rates nor UV–Vis absorbance observations on chemical samples.
- Scientific contact: calibration-source spectrum unlike test-source spectrum is a concrete regime transport hazard. More than one physical validation setup was described, supporting a *conditional* correction procedure.

## Zong 2010: why correction is not absolute certainty
- §§1–2: C depends on measured spectral line-spread functions (SLSFs). Dominant uncertainties: instrument-intrinsic out-of-range light, detector blooming/smearing, response nonlinearity, dark signal and finite ADC range; input-fiber/filter response; illumination geometry; long-term stability; line-source background/power/bandwidth; interpolation of SLSFs between sampled wavelengths.
- Electronic bracketing extends effective SLSF dynamic range as discussed by author, but no exemption from uncertainty.
- Table 1: comparisons of blue/green/red/white LEDs using corrected CCD device and double-grating scan reference show relatively small CIE coordinate differences. This validates that *particular* chromaticity application, not the full chemical spectrophotometer model from P1A.
- Distinguish correction matrix point estimate from covariance and calibration history; correlated matrix errors should not be counted as independent at each corrected wavelength.

## Worked new MQR transfer counterexample — operator order matters
Let the true positive **raw** two-channel sample intensities be x=(0.1,0.4), and reference x0=(1,1). Suppose spectral mixing H=[[0.9,0.1],[0.1,0.9]]; measured raw sample y=Hx=(0.13,0.37), and reference y0=H x0=(1,1).
Correct inverse mixing matrix C=H^{-1}=[[1.125,-0.125],[-0.125,1.125]]. Then **raw-first correction** xhat=C y=(0.1,0.4) returns true absorbances A_true=(-log10(0.1), -log10(0.4))=(1,0.397940...).
**Wrong alternative:** log first A_meas=(-log10(.13), -log10(.37))≈(0.886057,0.431798), then C A_meas≈(0.94284,0.37502) ≠ A_true.
Thus generally C[-log(y/y0)] ≠ -log[(C y)/(C y0)]. Both transformations are legitimate mathematical operations, but not equivalent corrective interventions. A correction matrix defined in radiometric raw-signal space does not automatically transfer to absorbance-log space. This is an original **constructed** example using the literature method, not a claim Zong's device committed that error.

**Connection to MQR-1.12:** instrument correction, wavelength mixing, calibration and the nonlinear report coordinate have order-dependent semantics. If an experiment reverses operations without verifying a commutation relation, 'same stated absorption' need not have the same physical warrant.

## NBS Part II close-reading update — printed pp.33–43, text read (2026-10-18)

**Source-scoped correction of previous TOC-only status:** after the first tranche, printed Part II text (§§5–9, including descriptions and tabulated examples) was read. Figures/tables remain OCR extraction-level, not visually verified. Update does not apply to the 140-page appended reprints/certificates, still OPEN.

**Cuvette / thermometry is not incidental (§6, printed pp.33–34):** sample-cuvette positioning and orientation can dominate precision; experimental differences may be caused by cuvette handling or blank subtraction. Authors' reproducibility Table 9 reports different blank/sample cycles even under an NBS high-accuracy apparatus. Table 11 reports bath and *actual solution* temperature differences: one text-extracted example is nominal bath 40.0°C vs solution 37.0°C, a **3.0°C discrepancy**. This difference makes stated treatment temperature a poor proxy for sample temperature if not measured. As a measurement-ontology case, the controlled bath is **not** automatically the sample's thermodynamic state; a physical transport/lag relation is needed. No procedures for handling hazardous reagents are reproduced here.

**NBS trace-element results uncover common preparation bias (§7.2, printed pp.37–39, Table 13 and Fig.21):** for Ni in NBS trace-element glass, authors compare spectroscopy and polarography against isotope-dilution mass spectrometry (IDMS). Text-extracted averages:
- 500-ppm-class SRM: spectrophotometry **451 ppm**, polarography **450 ppm**, IDMS **458.7 ppm**. Spectrophotometry/IDMS ratio ≈0.9832, polarography/IDMS ≈0.9810.
- 50-ppm-class SRM: spectrophotometry **37.6 ppm**, polarography **37.8 ppm**, IDMS **38.8 ppm**. Spectrophotometry/IDMS ratio ≈0.9691, polarography/IDMS ≈0.9742.

The paper considers the *shared* sample dissolution/preparation route a plausible source of missing nickel rather than positing two independent optical/polarographic instrument biases of precisely the same magnitude. **It explicitly presents a mechanistic explanation, not definitive source-specific proof.** This is a good historically real, multi-method **common-mode** example for MQR-1.5 nonduplication, 4.109 provenance, 4.114 cross-laboratory dependent calibration; far stronger as an epistemic lesson than a further invented example.

**Analyst’s alternative hypotheses / falsifiers:** Shared sample recovery issue, independent calibration of the IDMS source, sample heterogeneity, matrix-dependent extraction or standards could contribute. A discriminating design would compare independently prepared aliquots, independently traceable methods and matched specimens with disclosed cross-method covariance. The exact chemistry/reagents are **not** necessary for the conceptual analysis, and the cited paper does not quantify every covariance. It is legitimate to distinguish agreement conditional on a shared preparation step from truly noncommon measurement contact.

**Additional Part II cases (§§7.3–7.4, printed pp.39–40):** simultaneous multi-element optical analysis uses different colorimetric response spectra and changes chemical context; different analyte-specific response bands plus controlled changes can provide separate constraints, but interferences mean the inverse problem is not automatically full rank. A comparison of copper values with an isotope dilution method is presented in Table 15; numerical transcription and causal interpretation remain OCR/visual HOLD. These are source-based examples of a state/target-specific intervention bridge, not claims of chemically invariant coefficients.

**Most important new synthesis:** Two measurements can be close because both correctly track **the same biased prepared analyte**, not because each independently reveals the original specimen’s true concentration. The route
specimen -> shared preparation -> {optical signal, electrochemical signal}
can generate correlated failure. Measurement-independence is a property of the **evidence-generating causal graph**, not the names of the instruments.

## Next bounded reading segments
1. NBS printed pp.7–29: table-by-table SRM identity, bandpass, uncertainty, calibration conditional; photographic audit.
2. NBS printed pp.33–43: chemical procedure and IDMS comparison, real source figures; separate original chart images.
3. NBS appended certificate inventory/edition linkage; avoid claiming all 140 pages fully read.
4. Zong 2007 Fig.1–4 and 2010 Table 1: figure/signal units and percent reductions visually audit where possible; no transposition of spectral irradiance into solution absorbance without explicit bridge.
