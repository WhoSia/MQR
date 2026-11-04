# MQR-5.3 R34 — The steam-point transition as a claim-relative discrimination problem

**2026-11-04 · historical source audit + constructed identifiability argument · no new historical measurement, no claim of priority**

## Historical source boundary

Hasok Chang, *Inventing Temperature* (2004), ch. 1, pp. 8–56 (Drive source: https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view) distinguishes unstable bulk-water boiling from the alternative steam-point reference, discussing De Luc, Cavendish, pressure and nucleation-related complications. The Royal Society 1777 committee report is identifiable in the Society's archival catalogue as L&P/6/257 (https://makingscience.royalsociety.org/items/l-and-p_6_257/paper-report-on-the-graduation-of-thermometers-by-the-royal-society-commitee). **The archival catalogue, not a full collation of the 42-page manuscript, was independently checked in this round.**

Critical prior art: Chang (2008), *The Myth of the Boiling Point*, *Science Progress* 91(3):219–240, DOI 10.3184/003685008X360632 (https://pmc.ncbi.nlm.nih.gov/articles/PMC10361150/), explicitly reports historical experimental replications and container/dissolved-air dependence. Accordingly MQR must not claim to have first proposed or first replicated such experiments. Tal (2017), *Calibration: Modelling the Measurement Process* (Drive https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view), treats calibration as constructing/testing predictive models; standards can be useful without being logically obligatory.

## Exact analytic question

Can an observation distinguish (i) correction of an instrument, (ii) reconstruction of a material reference realization, and (iii) conceptual replacement of the quantity being measured, **without presuming that one historical method already yields true temperature**?

A carefully limited *retrospective* thought experiment compares liquid and steam measurement channels at fixed ambient pressure and varying, historically motivated preparation conditions. This is a mathematical comparison of possible data, **not an instruction to reproduce pressurized or superheated boiling**.

Let n label reference-realization conditions; suppose stable instrument gain a>0 and channel offsets b_L,b_V, and define

- L(n)=a[T_sat(p)+delta(n)]+b_L;
- V(n)=a[T_sat(p)+gamma(n)]+b_V.

Here delta, gamma are deviations from the ideal equilibrium saturation model; they are not empirical values supplied by Chang. Two conditions n0,n1 yield a *difference of differences*:

D=[L(n1)-V(n1)]-[L(n0)-V(n0)]
 =a{[delta(n1)-delta(n0)]-[gamma(n1)-gamma(n0)]}.

Under the narrowly specified null hypothesis of no preparation-dependent differential displacement, D=0. D!=0 rejects this null if channel gain/offset stability, pressure comparability and uncertainty bounds hold. This is established contrasts/identification algebra, not a new theorem. Instrument drift or a change in actual pressure can yield the same apparent D.

**Adversarial equivalence:** D/a=d can arise from liquid deviation changes (Delta delta=d, Delta gamma=0) or from steam deviation changes (Delta delta=0, Delta gamma=-d). The *same differential observation* alone does NOT establish that steam is the invariant reference. A source-independent equilibrium/pressure calibration, stable channel controls, or separately warranted saturation-physics restrictions are needed for that directional conclusion. A common bias can remain after crossing reference realization with device.

If absolute channel readouts and independently justified stable calibration are available, some of these rivals may become distinguishable. Identifiability is relative to the specified observation interface; do not describe it as universal impossibility.

## Discrimination, selection and conceptual change: three separate verdicts

1. **Defeat a narrow model:** A significant D can defeat the model that both channels differ by a preparation-invariant constant. It cannot uniquely assign fault to liquid versus steam.
2. **Select an operational reference:** Demonstrating steam robustness over a bounded preparation/pressure domain can justify choosing a steam-point *practice* for specified metrological claims. Correlated failures, supersaturation and domain extrapolation remain live defeaters.
3. **Claim a conceptual innovation:** A new operational reference does not logically entail a new concept of thermodynamic temperature. Establishing conceptual change requires evidence that the scientific target, admissible inferences, laws or explanatory practices were reorganized beyond numerical calibration or apparatus replacement.

The last distinction connects R34 to the early MQR commitment REALITY != RESISTANCE and to R32 (information versus computational accessibility) and R33 (relative contrast versus global bias). These distinctions may already be thoroughly subsumed by Chang, Tal, conventional metrology and historical epistemology; novelty status **HOLD**.

## Historically testable research agenda, non-operational

- Collate Cavendish et al. (1777) original manuscript / print report against Chang ch.1 for exact apparatus descriptions, pressure restrictions and reference terminology.
- Verify whether De Luc (1772), Cavendish and later competing accounts *actually predicted* opposing observations before observing outcomes, rather than constructing retrospectively rationalized "rivals."
- Investigate Chang (2008) replication in relation to his 2004 historical interpretations; label the former as later experiments rather than eighteenth-century historical observations.
- Test whether the relative contrast can be interpreted without smuggling in a superior calibration standard as a premise; record negative and inconclusive cases.
- Compare this analytical reconstruction with Chang's epistemic iteration and Tal's predictive calibration. Explicitly report any prior-art subsumption.

## Scientific authority and recording

**Established in this round:** a documented historical source distinction; a transparent constructed difference-in-differences argument and its countermodel; a previously underweighted Chang (2008) replication prior-art check.

**Not established:** an independently verified nineteenth-century primary numerical dataset; actual measured D; a novel theorem; evidence that steam-point measurement is universally invariant; an independent new empirical discovery; a new theory of conceptual change.

**Research custody:** Notion for claim/defeater status, Drive for original paper and source-byte storage, GitHub for this authored research note. No GitHub Actions bot commits; no raw historical file deletion. Next: R35 adversarial reconstruction of the 1777 committee's evidential warrant and independent historical-source collation.
