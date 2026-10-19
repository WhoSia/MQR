# MQR-4.122 P1 — Calibration Repair, Rival Overlap and the Nonmonotonic Frontier of Warrant

**2026-10-19 · P1 conceptual counterexample and intervention-design specification · mathematical reasoning only · no new laboratory data.**

## 1. Why the 4.121-to-4.122 move is substantive

The P0 proposal defines \(\mathcal O_H(U;C,N)\), an admissible observation family under interventions \(U\), calibration lineage \(C\) and nuisance assumptions \(N\). It does **not** imply that a better calibration must monotonically shrink the set of defensible scientific claims: correcting an instrument can make previously apparently decisive data *less* discriminating, or reveal previously invisible phenomena. Nor does the same operation imply a Kuhnian disciplinary crisis. The research must separate **source repair**, **target-model change**, **operational kind change**, and **historical community change**.

## 2. Exact counterexample: more accurate calibration can destroy apparent discrimination

Let rival hypotheses \(H_0:\theta=0\) and \(H_1:\theta=1\). Suppose a scientist treats a measured intensity \(y=1\) as the target quantity \(\theta\) because their instrument model is \(y=\theta\), with negligible measurement noise. Then \(H_1\) fits and \(H_0\) is excluded.

An independently performed blank/source calibration later establishes an additive baseline \(b=1\), so the correct model is \(y=\theta+b\). At the *same raw observation* \(y=1\), \(H_0\) now fits and \(H_1\) fails. The empirical record did not change, but the accepted target attribution **reversed**.

More generally, if an independently measured \(b\in[0.8,1.2]\), then \(y=1\) implies \(\theta\in[-0.2,0.2]\) rather than \(\theta=1\). The inference about target \(\theta\) changes without any change in raw detector reading. The instrument correction is local (D1); it is not evidence of changed chemistry (D2) or changed paradigm (D4). An independent blank *matters* because fitting \(b=1\) after seeing the target result would be post-hoc model accommodation.

**Defeater:** if the calibration procedure shares the same unknown bias as the original target reading, the claimed independent \(b\) interval has not been established. The example is a logical counterexample, not historical evidence that a named laboratory actually did this.

## 3. Rival overlap is intervention-relative, not a permanent metaphysical equivalence

Let \(H_0:y(u)=a\) and \(H_1:y(u)=a+\gamma u\), with \(\gamma\ne0\). If the only feasible intervention is \(u=0\), then the models make the same prediction for every observed datum. If \(u=1\) becomes feasible and independent source error is bounded by \(|e|\le\delta\), the predicted observation sets are \([a-\delta,a+\delta]\) and \([a+\gamma-\delta,a+\gamma+\delta]\). They are disjoint if \(|\gamma|>2\delta\). This is a **design-dependent** distinction, not a universal ontological order.

**Countercase:** if nuisance is allowed to vary as \(q(u)=-\gamma u\) without an independent bound, the same intervention cannot separate them. The more flexible optical model can explain every datum but gains no uniquely warranted explanatory content from that flexibility. This directly generalizes the MQR-4.121 missing-out-of-band-light problem.

## 4. Two distinct notions of scientific repair

- **Retrodictive accommodation:** fit a baseline or optical kernel to existing discrepancies; in-sample fit improves. This alone cannot distinguish source correction from a hidden target change.
- **Independent predictive repair:** fix calibration parameters using standards or held-out source/filter experiments *before* seeing the new target results; then test out-of-sample across matched interventions. It can establish bounded instrument validity, but still does not prove a particular chemical ontology.

An independent calibration can also **expand** uncertainty when previously ignored drift/correlation is discovered. A newly widened error bar is not regression in scientific rationality; it may be more accurate acknowledgement of uncertainty. Do not force a scalar 'progress' claim.

## 5. Optical P1 minimal falsifiable experimental matrix

A useful *pilot*, not an assured globally minimal design, crosses two chemical states \(pH_L,pH_H\), two independently calibrated optical bandpass settings \(B_n,B_w\), and two independently tested out-of-band suppression settings \(F_0,F_1\): **2×2×2 = 8 acquisition cells**, each recording sample, reference and dark raw counts. Include multiple wavelengths around an expected absorption slope/isosbestic region, randomized order, matched sample batches, fixed path length, recorded T/ionic strength and concentration, instrument response matrix with covariance/credible enclosure, source spectral distribution and time-synchronized independent chemical-state assay. Replication and blanks must be designed based on measured drift and noise; 8 cells alone do not provide statistical power.

Predicted signatures conditional on rival constraints:
- Pure chemical contrast: after independently corrected optics, pH contrast should be approximately stable across B and F; *not* literally invariant if bandpass nonlinearity interacts with pH-dependent spectrum.
- Bandpass-only artifact: signal depends on B and spectral slope/curvature, possibly nonlinearly with concentration, and may appear without chemical-state changes.
- Stray-light artifact: filter F changes the response in a manner consistent with separately measured off-band flux; effects often grow in high absorbance regime.
- Mixed model: interactions across pH×B×F can occur; main effects alone cannot identify one unique mechanism.
- Unbounded missing light: no unconditional separation is possible. It must be independently bounded or explicitly retained as an identified set.

**Hard failure condition:** if optical settings also alter sample temperature, illumination-driven chemistry, detector gain, or acquisition time, then observed interactions are not specific to optical correction. The 8-cell factorial is only a *starting* design; source and material controls are essential.

## 6. Historical-philosophical opposition (not invented quotations)

**Kuhn:** normal science can absorb anomalies through puzzle-solving and apparatus refinement; neither an isolated residual nor its local repair alone establishes a paradigm shift. However, what counts as a stable problem, exemplar and legitimate instrument can itself depend on the disciplinary matrix. Our 'independent calibration' criterion is therefore not an ahistorical external oracle.

**Lakatos:** a local repair can be a legitimate auxiliary modification or a degenerating accommodation; distinguish by its independently corroborated novel consequences, not by whether it leaves the central target ontology unchanged. The P1 intervention test is a *candidate* for a discriminating prediction, not an operationalized Lakatosian research-program appraisal.

**Laudan:** problem-solving adequacy and standards of appraisal can change historically; 'science/non-science' demarcation and epistemic warrant should not be conflated. The four D1–D4 categories are analyst reconstructions, not a claim that Laudan himself defined them.

**Chang:** calibration standards and measurement practice can co-constitute stabilized quantities; a new thermometric standard need not simply measure a fixed pre-existing target more accurately. This challenges any naïve reading of a single immutable \(F_H\) as 'the' instrument's true map.

**Source status:** these are preliminary argumentative reconstructions, not direct quotation or line-by-line primary-text verification in P1. A dedicated original-text concordance is required before making claims about exact terminology or historical episode.

## 7. First research decision and holds

**Provisional P1 result:** There is a precise counterexample to monotone claim survival under calibration correction, and an intervention-relative set-separation criterion with a nuisance-dependent failure case. These are elementary formal constructions, not a discovery of a new physical law. The decisive new question is **which source/standard lineage and feasible intervention set can actually constrain nuisance without presupposing the theory under test?**

**Next:** construct an explicit *shared calibration genealogy* counterexample (two 'independent' instruments sharing one common source standard); re-examine source documents for optical response/linearity and Kuhn's original distinctions; compare at least two independent historical reconstructions of a disputed scientific change. Avoid generating more gates as a substitute for physical/archival evidence.

**HOLD:** no actual methyl-red instrument data; no measured covariance for 8-cell design; no independent chemical assay; no complete primary-text concordance; no new physical discovery; no universal scientific demarcation rule.
