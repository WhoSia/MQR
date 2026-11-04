# MQR-5.3 R35 — Historical actors, evidence interfaces and claim-relative identifiability

**2026-11-04 · research analysis · historical sources and constructed model must not be conflated**

## 1. Source genealogy and historical-authority boundary

- The Royal Society (1777) report is *The report of the Committee appointed by the Royal Society to consider of the best method of adjusting the fixed points of thermometers; and of the precautions necessary to be used in making experiments with those instruments*, *Philosophical Transactions* **67**, 816–857; DOI **10.1098/rstl.1777.0038**. Its 42-page manuscript is catalogued as **L&P/6/257**, read on **19 June 1777**, by the Royal Society: https://makingscience.royalsociety.org/items/l-and-p_6_257/paper-report-on-the-graduation-of-thermometers-by-the-royal-society-commitee ; original printed publication indexed at https://www.jstor.org/stable/106261 . This round verifies **bibliographic provenance**, not line-by-line readings of the original manuscript/printed 1777 pages; attempted source PDF retrieval was blocked by access limits.
- Hasok Chang (2004), *Inventing Temperature*, Chapter 1 (Drive: https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view), discusses pressure, immersed columns, container conditions, dissolved gases, De Luc's account and saturation-vapor fixed-point practices. This is an **historian's reconstruction**, not an unedited eighteenth-century primary document.
- Chang's public research site (dated **18 October 2007**) describes a later empirical replication program in **2004 and 2007**, distinct from historic actors' 1770s observations: https://www.sites.hps.cam.ac.uk/boiling/ . Chang (2008), *Science Progress* 91(3):219–240 DOI 10.3184/003685008X360632, describes replications: https://journals.sagepub.com/doi/10.3184/003685008X360632 . These provide substantial prior art for replicating historic thermometric anomalies and for reflecting on circular calibration.
- Eran Tal (2017), *Calibration: Modelling the Measurement Process* (Drive: https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view), explicitly treats calibration as predictive-model construction and tests rather than mere reference-value comparison. Neither standard-free calibration nor epistemic iteration is newly introduced here.

**Evidence classification:** (A) 1777 source catalogue and printed-publication bibliographic metadata = independently verified; (B) 1777 detailed experimental claims = currently mediated by Chang (2004) until direct primary-text collation; (C) 2004/2007 modern replication = Chang's own 2007 public account and 2008 article abstract; (D) all quantitative formal models below = constructed MQR illustrations, NOT historic data.

## 2. What is and isn't identified from a paired contrast

At fixed physical pressure p, preparation condition n in {0,1}, let

L(n) = a[T_sat(p)+delta(n)] + b_L; V(n) = a[T_sat(p)+gamma(n)] + b_V,

with an identical stable gain a>0, channel-specific but preparation-invariant b_L,b_V. Observe only the paired difference-in-differences

D = (L(1)-V(1))-(L(0)-V(0)) = a[(delta(1)-delta(0))-(gamma(1)-gamma(0))].

Define DeltaDelta and DeltaGamma for the condition changes. Fix a known a for this **particular** comparison, set d=D/a. For each t in R, rival pairs

(DeltaDelta, DeltaGamma) = (d+t,t)

produce the same d. Hence the claim psi1 = 'DeltaDelta - DeltaGamma != 0' is identified from d, but psi2 = 'the steam reference is invariant: DeltaGamma=0' is not. The two witnesses (d,0) and (0,-d) refute uniqueness for d !=0. If d=0, infinitely many common shifts are still equivalent; both pathways may vary together.

If gain a is unknown but positive, the *sign* of DeltaDelta-DeltaGamma is identified by the sign of D under these exact assumptions, but its numerical magnitude is not. Absolute temperature, common offsets and general cross-context transport are not identified by this contrast.

**Adversarial model:** if channel offset depends on preparation n, its drift produces an additional Delta b_L - Delta b_V; a nonzero D then cannot uniquely refute the physical reference invariance hypothesis. If pressure p changes with condition, an extra saturation-temperature term may enter the raw readouts and must be controlled or modelled. This is a constructed signal-identification result, not validation of any historical device.

## 3. Claim-relative equivalence and an authority ladder

For an observation map O: Theta -> Data, define observational equivalence theta ~_O theta' iff O(theta)=O(theta'). A claim psi is **identified relative to O** iff psi is constant on every equivalence class. This is a standard definition in identification theory, not an MQR theorem.

Three claims to keep apart:
1. The **relative-invariance null** (D=0) can be tested, within uncertainty, if stable instrumental/pressure assumptions are warranted.
2. **Which reference is superior** is not entailed by D alone; it requires independent stability or external physical restrictions and a declared operating domain.
3. **Whether the concept of temperature changed** is not entailed by either (1) or (2); historical evidence about redefined quantities, valid inferential moves, and explanatory models is necessary. Even a wholesale new apparatus may realize the same temperature concept.

This is an *analysis contract*, not a fabricated claim that the 1777 historical committee endorsed any such explicit ladder.

## 4. Prior art and negative cases

- Chang's epistemic iteration and 2004/2007 replication already diagnose important reference-instability and circular-justification problems.
- Tal's predictive calibration already addresses the model-mediated relation between indication and outcome.
- Conventional parameter identifiability and experimental design already yield the quotient/equivalence-class reasoning above.
- A **negative case**: externally independently justified steam stability (DeltaGamma=0), gain a and instrument invariance render DeltaDelta=d identified; no extra philosophical category is necessary. Conversely, D=0 is consistent with shared variations, so mutual agreement does not certify either channel's stability.
- Distinctively new historical or methodological results are **NOT established**. A candidate future contribution must demonstrate a genuinely informative historical reconstruction or a sharply stated question that survives Chang/Tal/system-identification subsumption.

## 5. Next source-and-theory tests (R36)

1. Obtain legible 1777 printed source pages (Phil. Trans. 67:816–857) and compare key terms to the manuscript (L&P/6/257); record exact printed-page anchors, authorship and changes. **Do not claim this has happened.**
2. Recover De Luc (1772) directly and verify which claims are contemporaneous predictions versus Chang's retrospective analytical reconstruction.
3. Read Chang (2008) in full with figures and delimit how its actual replication differs from the constructed model; do not confuse later replication with independent eighteenth-century predictions.
4. Find a historical **counterexample** where an operational reference was improved without reconstituting the concept, and an episode where the concept changed without instrument superiority, then assess whether existing literature already answers the comparison.
5. Strengthen the reference-choice framework using explicit ranges of claims, model assumptions, uncertainty and out-of-domain defeaters, without promising a universal scalar epistemic score.

**Authority:** Notion = proposition/defeater ledger; Drive = historic raw bytes when deposited/readback; GitHub = human-authored research/code. No raw source moved or deleted in this round. No physical experiments performed, no new primary manuscript readings claimed, no GitHub Actions bot commits.
