# MQR-4.106 — Heeger Chapter 9 vs SNO (2002) and a strong rival-reduction test

## Provenance
Read the original PDF of K. M. Heeger (2002), *Model-Independent Measurement of the Neutral-Current Interaction Rate of Solar 8B Neutrinos with Deuterium in the Sudbury Neutrino Observatory*, University of Washington dissertation (Drive 1VrbgUykxR_DUrEQMl7gB6vbmP17Paucv), specifically §9.2, §§9.4.1–9.4.3, Eqs. 9.18–9.19, Tables 9.6 and 9.9. Contrasted to SNO Collaboration (2002), *Direct Evidence for Neutrino Flavor Transformation from Neutral-Current Interactions*, arXiv nucl-ex/0204008, Table II (Drive 1zDBfrf1Ex3a8yOVwSzGDfov-dOVQpakh).

## Different fits; not interchangeable 'replications'
| Component | Heeger Table 9.6 | Heeger Table 9.9 | SNO PRL Table II |
|---|---|---|---|
| Selection | NHIT >= 65, Rfit <= 550 cm, CC/ES | NHIT >= 46, Rfit <= 590 cm, CC/ES/NC | Teff >= 5 MeV, R <= 550 cm, CC/ES/NC |
| CC energy scale | -5.5/+6.5% | -5.5/+6.5% | -4.2/+4.3% |
| NC energy scale | n/a | -7.6/+7.6% | -6.2/+6.1% |
| NC neutron capture | n/a | -3.6/+4.0% | -4.0/+3.6% |
| CC cross-section | +/-3.0% | +/-3.0% | +/-1.8% |
| NC low-energy background | n/a | -18.3/+20.7% (tabulated) | not an identical standalone entry |

**Source cautions:** Heeger Table 9.9 marks low-energy background for CC and ES as 'in fit to PDF'; NC shows asymmetric shift. Distinct event thresholds, nuisance treatments, and flux assumptions mean that 'the PRL version of Table 9.9' is *false provenance*. Heeger §9.4.2 Eq. (9.18) models CC/ES/NC plus AV and H2O spatial-background PDFs with positive background amplitudes, and Eq. (9.19) expresses log L = sum_j log N(z_j) - sum_i f_i. §9.4.3 reports shape-unconstrained rates in units of 5.05*10^6/cm2/s: CC=0.344 +/-0.021(stat) -0.022/+0.025(syst); NC=1.261 +/-0.279(stat) -0.119/+0.117(syst); ES=0.483 +/-0.081(stat) -0.025/+0.031(syst). These are NOT SNO PRL standard-spectrum joint values.

## MQR-3.154 adversarial test: stopping history versus terminal likelihood
Take iid X_i ~ N(theta,1), known variance. Suppose two datasets have identical observed n and sum X_i. Their likelihood functions L(theta|x) are proportional in theta even if observation order differs. Any proper Bayesian analysis with common prior and sampling/stopping rules independent of theta MUST yield the same posterior. Claiming a distinct 'realist authority' for these histories solely because their chronology differs would be a mistake.

If selection/stopping depends on unseen parameter-linked processes, outcome-dependent data selection, or calibration adjustments, the likelihood must include those dependencies; divergence is already explicable by standard informative sampling, conditional likelihood, and selective inference. MQR's candidate contribution is narrowed to explicit **lineage auditing that reveals unrecorded dependence** before quantitative correction—not a new statistical inference rule.

**Required discriminating test:** identify actual two histories whose complete relevant likelihood and protocol constraints are judged equivalent by mature rival frameworks, but for which MQR offers a defensible different verdict. Nothing in Heeger/SNO so far establishes this.

## Archival policy (applied)
Classify a PDF by its *contained edition*: original dissertation/BA/MA thesis -> 11_SOURCES; published monograph or edited book/proceedings -> 11_BOOKS; independent journal or proceedings paper/preprint -> 10_PAPERS; institutional handbook/report -> 11_SOURCES; individual book chapter/article reprint -> 10_PAPERS when paper-like, with parent-volume metadata. A revised, commercially published book based on a thesis is a book ONLY if the PDF is that published book edition. Keep uncertain cases on HOLD, do not delete.

## Status
MQR-4.106 OPEN, independent MQR philosophical novelty HOLD. Not a reanalysis of SNO raw events, does not reconstruct the 5.3 sigma result. No new Actions workflow requested.
