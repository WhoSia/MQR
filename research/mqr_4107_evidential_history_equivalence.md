# MQR-4.107 — Evidential-History Equivalence, Statistical Sufficiency & Historical Warrant

**OPEN/HOLD · 2026-10-10.** Research follows MQR-4.106; do not seal as philosophical novelty.

## Strong statistical rival: Lindsey 1997
J.K. Lindsey, "Stopping rules and the likelihood function", *Journal of Statistical Planning and Inference* 59(1), 167–177. DOI 10.1016/S0378-3758(96)00096-1. Original full-text PDF independently opened and read at https://www.commanster.eu/Articles/stoprule.pdf . Original ScienceDirect abstract https://www.sciencedirect.com/science/article/pii/S0378375896000961 .

- Section 1: report of identical fixed realized likelihood does not by itself identify underlying experiment or a minimal sufficient statistic; sampling design must be specified.
- Section 2 Example 1: unknown Normal mean known variance, fixed n vs random N; same realized likelihood but distinct model families and possibly minimal sufficient stats. The author explicitly warns one must know which quantities were random.
- Section 2 Example 3: reported Bernoulli likelihood proportional to theta(1-theta)^2; proposed stop after three observations if fourth is failure, otherwise report all four, is non-adapted: it depends on an observation beyond the nominal stop. The reported likelihood hides discarded selection information. A different rule using third observed value to decide whether to take fourth can be a valid stopping time.
- This directly diminishes MQR-3.154's generic originality: need distinguish a genuine adapted stopping time, informative censoring/selection, and inference from the reported likelihood alone.
- The thesis is NOT that all stopping rules violate the Bayesian likelihood principle; for ordinary well-described, ignorable designs, proportional complete likelihood with same prior gives same posterior.

## Mathematical minimal rival separation
For IID Bernoulli Xi with P(Xi=1)=theta, fixed four observations (1,0,1,0) vs permutation (0,1,0,1) each yield theta^2(1-theta)^2 and uniform Beta(1,1) prior -> Beta(3,3); chronology alone is not evidential difference.
A single observed success has L(theta)=theta; a report of 'eventual success' under unbounded repetition with hidden attempt count has P(event)=1 for 0<theta<=1 and provides zero discrimination. If first success happens at t=3 and t is disclosed, L(theta)=theta(1-theta)^2. Such contrasts are within likelihood/selection/missingness theory, not novel MQR inference.
Future stricter replay: implement Lindsey's non-adapted Rule Example 3 on binary sequences, compare minimal filtration and outcome/reporting map, not just a toy.

## Chang 2004: historical strong rival
Hasok Chang, *Inventing Temperature*, chapters 1–5, especially ch2 "Spirit, Air, and Quicksilver" DOI 10.1093/0195171276.003.0002; chapter 5 Measurement, Justification, and Scientific Progress. Original full book already held on Drive as "Chang (2004) — Inventing Temperature - Measurement and Scientific Progress.pdf" (ID 1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV) and another original filename ID 14Gb6NUlrDzDy3ooOJVTFAavfd6xSb3bi: duplicates status NOT audited; do not delete or claim equivalent.
Oxford original chapter page https://academic.oup.com/book/5530/chapter-abstract/148466490 confirms tensions among different thermometric substances after fixed-point choice. Chang's epistemic iteration already addresses standards justified and repaired through historically inherited methods. Claims about Regnault or Kelvin precise passages await original PDF extraction before declaring page-specific support.
Compare epistemic *warrant for a measuring practice* versus statistical *inference conditional on a measuring model*, without pretending ontic states are altered by mathematical proof-checking.

## SNO primary historic case
Heeger 2002 University of Washington thesis §9.2, §9.4, tables 9.6 and 9.9 vs SNO 2002 PRL Table II; sources archived in Commons, with 4.106 comparison document research/mqr_4106_heeger_ch9_comparison.md . Selection, background constraints, energy model and common calibration ancestry differ, which is a standard robustness/inferential dependence issue. Never call two fits of the same events 'independent detector experiments'.

## Proposed 4.107 falsifiers
A. **Equality gate**: complete agreed likelihood, identical scientific-target semantics, explicit complete selection and calibration lineage -> MQR must not create arbitrary history-based authority inequality.
B. **Standard rival reduction**: if Lindsey 1997, Bayesian conditioning, selective inference and Chang 2004 together predict every MQR verdict, MQR has no demonstrated incremental explanatory advantage.
C. **Historically grounded divergence**: locate a case with two statistically equivalent end products where a real pre-outcome historical calibration distinction carries a defensible additional scientific realist commitment **not** already described by standard metrology and epistemic iteration. Required original pages, contemporary standards and specific changed conclusion.
D. **Non-instrumental cases**: do not treat changes in proof checker history as physical intervention into mathematical truth.

**Status:** Stage OPEN, philosophical distinctness HOLD, archive source evidence differentiated from inferences. No new GitHub Actions.
