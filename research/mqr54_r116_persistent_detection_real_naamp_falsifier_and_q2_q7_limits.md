# MQR 5.4 R116 — Real NAAMP falsification of two extreme repeat-survey stories; why repeat ≠ intervention

**2026-11-23 KST · 5.4 OPEN · source-bounded ecological result and a synthetic exact countermodel.**

## R115 exact-source verification

[Committed exact Fraction test](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r115_persistent_detection_nonidentifiability.py) was replicated byte-for-byte in the local executable runtime. Git SHA-1 remote = local git hash-object **63804ac702ad74e930ad797ccd40e0d06476902c**. Python completed the 2,046 possible binary sequences across k=1..10 checks (2^1+...+2^10=2046) and the exogenous reset contrast. The test is synthetic, not a real experiment.

Two worlds share exactly the same distribution for **every k** (not merely ten, by direct formula):
- World A: site occupancy Z~Bernoulli(r), perfect observation Y_j=Z at each repeat.
- World B: site occupancy always true, but latent persistent availability H~Bernoulli(r), observation Y_j=H for all j.
Both have P(Y_1...Y_k = 1...1)=r and P(0...0)=1-r, with all mixed histories probability zero.

Changing the measurement process **independently of H** on a final visit (with site state stable) predicts P(Y_1=0,Y_2=1)=0 in A and (1-r)r>0 in B. Merely collecting ten identical observation repeats **cannot** make that distinction. This is a standard heterogeneity/non-identifiability model, not an original theorem. r=3486/14651 is borrowed only as a numerical anchor from the 4.95 original-record table and **is not a certified site prevalence**.

## Real 4.97 2001 Delaware NAAMP frog records challenge both extreme worlds — locally

Original frozen [4.97 scientific closeout](https://github.com/WhoSia/MQR/blob/main/docs/MQR-4.97-FINAL-BOUNDED-REAL-FIELD-DETECTION-AND-LEAN-CLOSEOUT.md) on 130 actual sites and **337 shared physical station visits** (not 674 independent frog-visit events) records:
- *Pseudacris crucifer*: consecutive negative→positive transitions **4**; positive→negative transitions **76**.
- *Pseudacris feriarum*: negative→positive **4**; positive→negative **40**.
- First/second/third visits: 130/110/97 sites; positive records respectively 95/40/5 for crucifer, 39/4/0 for feriarum.

The R115 **extreme** worlds both predict precisely **zero within-site mixed histories**, thus the real NAAMP recorded mixed histories rule out using either extreme as a literal complete generative model of these frog listening records (under correct site ID and faithful call-index mapping). This result says NOTHING about the 2024 Finnish *Anemone* source's revisits, which have not been verified. Nor does it establish the cause of changing detection: visit order, season, call phenology, observer, movement, environmental factors, reporting-selection and heterogeneity remain alternatives.

A more realistic site-level random-effect model, time-varying detection, false-positive process or hidden transition process may explain these histories; compare all these classical models **before** proposing a uniquely MQR additional explanation. In particular the old 4.97 report already notes visit-order nonstationarity and original 100-site training/30-site heldout likelihood changes: this is prior MQR work, not a new independent heldout run.

## Strong established scientific adversaries

- [Fitting and Interpreting Occupancy Models](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052015) directly discusses identifiability and imperfect detection, explaining why separate estimation of occupancy is assumption-dependent.
- [Fractional replication in single-visit multi-season occupancy models](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14275) warns even repeat-like information and spatiotemporal correlations may create fragile identifiability under model misspecification.
- [Site occupancy models with false positives and heterogeneous detection](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210x.12442) explicitly considers multiple visit and detection independence conditions.
- [GBIF formal occurrence download formats](https://techdocs.gbif.org/en/data-use/download-formats) provides event fields in schema but does not verify old 2024 ZIP actual population.

## Consequence for Q2 and Q7

- **Q2:** identical status codes, stable location IDs and repeated visits are *not sufficient*, when the observation processes may contain persistent latent filters. A shared physical site and source-aware record are necessary steps but not sufficient for identifying the physical quantity, calibration or ontology.
- **Q7:** adding a *new independently discriminating intervention* is an example of changing the experimentally askable question, but this exact ecological problem and solution family already exist in occupancy science. Claim only an MQR cross-case conceptual organization until independent novel incremental prediction is found.

## World-facing decision and stop

1. **Do not promote 4.95 to identified ecological occupancy** until original 2024 GBIF ZIP row metadata is read. Tool environment network DNS denied the original API download; Drive search found references but did not locate an exact raw ZIP as independently readable bytes. Do not treat a 2026 re-export as identical original.
2. To test 4.95 actual event structure, use the [R112 original-file checker](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r112_gbif_event_metadata_screen.py) but first independently test **its own raw ZIP parsing, date parsing and false-negative handling**; R112 strict criteria only return *candidates*, never true site identities.
3. For 4.97, model already-recorded visit order and covariates, using site-heldout likelihood and source ancestry. The mixed-record negative control is real but NOT a new original data acquisition.
4. Preserve Faraday→Maxwell as **independent protected Q3/Q4/Q5/Q7 research**, and explicitly compare whether an allegedly 'new' question is already answered by a standard model. No endless four-bit examples without new discriminating method.

**Boundary:** MQR 5.4 OPEN, no new 2024 original ZIP data in runtime, two-source roots NAAMP and GBIF do not become same target; external validation, prior-art advantage and independent theoretical law all HOLD.
