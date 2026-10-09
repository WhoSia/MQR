# MQR-4.108 — Calibration-Model Underdetermination, Cross-Principle Traceability & Historical Warrant

**Formal status: OPEN / DISTINCTNESS HOLD.** Authorized successor to MQR-4.107, not a closure of predecessor.

## Primitive question
When two physical measurement procedures appear independent, which documented evidence licenses quantitative agreement as metrological traceability and realist warrant? When are they only instrumentally different but dependent on one common reference, mapping or uncertain correction?

## Original-source custody inherited from MQR-4.107
- Regnault (1847) printed p181, Wikimedia/Wikisource DjVu /215, original ink *A-prime H0 785,21 mmHg* at 95.57°C; Chang 2004 Table 2.5 *782.21 mmHg*. Confirmed printed-versus-secondary textual discrepancy; cause unknown.
- Regnault printed p239, scan /273, glass expansion coefficients, **not** Chang Table 2.4 mercury temperatures. Printed p240 /274 expressly states general table from carefully executed graphic constructions on immediate observations, x-axis 10°C air and y-axis 1°C mercury-minus-air; p241 /275 contains comparison table reproduced in Chang Table 2.4. Plate VIII original image, volume plate scan /820, 838×924 Commons PNG, visually viewed; graph-digitized values and which readings coincide with actual observed points remain HOLD.
- Original full Chang 2004 book Drive 1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV; Heeger/SNO source comparison in research/mqr_4106_heeger_ch9_comparison.md. Full predecessor [MQR-4.107 note](mqr_4107_evidential_history_equivalence.md).

## Mature competitive theory court
1. **JCGM 200:2012 VIM 2.41:** metrological traceability is a property of *a measurement result*, requiring a documented unbroken calibration chain to a reference, with each calibration contributing uncertainty; branches/networks possible when multiple inputs. Section 2.41 note 5 specifically does NOT promise adequate uncertainty or freedom from mistakes. https://jcgm.bipm.org/vim/en/2.41.html
2. **JCGM VIM 2.42:** the traceability chain is the actual reference-linked sequence of measurement standards and calibrations. https://jcgm.bipm.org/vim/en/2.42.html
3. **NIST:** a calibrated instrument per se does not make arbitrary downstream measurement results traceable; result-target and uncertainty matter. https://www.nist.gov/metrology/metrological-traceability
4. **JCGM 100:2008 GUM section 5.2:** correlated uncertainty and covariance of shared input references must be propagated; independent-looking instruments can share reference error. https://www.bipm.org/en/committees/jc/jcgm/publications
5. **Tal (2017):** Calibration: Modelling the measurement process, *Studies in History and Philosophy of Science Part A*, https://doi.org/10.1016/j.shpsa.2017.09.001 . Calibration itself models and tests a measurement process, and robustness is already used to secure objectivity. Important philosophical direct rival, not a proof MQR unique.
6. **Chang (2004):** *Inventing Temperature* ch2 and ch5 provide instrument comparability, epistemic iteration and correction as historical rivals.
7. **Lindsey (1997):** Stopping Rules and the Likelihood Function, relevant to informational sufficiency; do not misinterpret proportional likelihood as unlimited realist warrant.

## P1 finite falsification court
Construct two nominally independent measurement principles A and B with shared reference error b, Y_A=T+b+e_A, Y_B=T+b+e_B. Contrast D=Y_A-Y_B=e_A-e_B cancels b, so agreement of A and B alone does NOT identify b, no matter how accurate D. For correlated reference error Var(b)=u_b², Var(mean(A,B)-T)=u_b²+(u_A²+u_B²)/4 under independent readout errors. Naive independence misses u_b². A third method C=T+e_C with **certified independent reference and independently traced uncertainty** offers contrast containing b, but merely claiming C independent without certification does not. If C=T+b+e_C, pairwise differences still cancel b.
This is GUM-compatible standard covariance logic and not novel by itself. Python test at experiments/mqr_4108/traceability_counterexample.py.

## Falsification gates
- G1: Source: preserve historical ink, processed graphs, secondary analysis and synthetic model categories.
- G2: Same reference ancestry despite two physically distinct transduction mechanisms => do NOT infer independent calibration authority.
- G3: Independent reference cannot be posited by declaration; require reference certificate, interval, uncertainty and scope, per VIM/NIST.
- G4: If GUM+Tal+Chang predict every MQR verdict, *DISTINCTNESS HOLD*. Find and falsify a specific nontrivial historical realist claim before moving to PASS.
- G5: No CI run is evidence for scientific novelty, and 4.107 remains OPEN/HOLD.

## Next
Locate original Gallica master for Plate VIII, reconstruct plotted curves only with legible source, identify direct/graph-derived values and numeric uncertainties; compare source-backed Regnault and calibrated SNO physical targets to fully specified VIM/GUM/Tal rivals, and pre-register divergence court.
