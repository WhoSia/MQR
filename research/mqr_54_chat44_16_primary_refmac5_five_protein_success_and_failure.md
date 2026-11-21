# MQR 5.4 — MQR44 R16: world-facing five-system joint X-ray/NMR case, author-published measurements audited

Date 2026-11-21 KST. Status **PUBLISHED PRIMARY SCIENTIFIC RESULTS READ / EXACT TABLE ARITHMETIC VERIFIED / ORIGINAL RAW REFINEMENT NOT REPRODUCED**. This is the first non-synthetic, same-author positive/negative protein-comparison witness in MQR44 R11–R16. Still **not an independently measured laboratory test**.

## Original scientific study
Mauro Rinaldelli, Enrico Ravera, Vito Calderone, Giacomo Parigi, Garib N. Murshudov and Claudio Luchinat (2014), 'Simultaneous use of solution NMR and X-ray data in REFMAC5 for joint refinement/detection of structural differences', *Acta Crystallographica Section D* **70**:958–967, DOI [10.1107/S1399004713034160](https://doi.org/10.1107/S1399004713034160), author full text at [PubMed Central PMC4306559](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/), especially **Table 1** and §§3–4. Accepted Dec 18 2013, published March 19 2014. Research case includes five systems in the same paper; this permits a more grounded side-by-side comparison than our previous one-bit toy.

The authors used diffraction structure factors for Protein Data Bank IDs 3SHI (MMP-1 catalytic), 3NHE (ubiquitin), 1IGD (GB3), 1EXR (calmodulin), 1YR5 (calmodulin–DAPk peptide). The publication provides **model-quality summaries**, not here a full independently rerun refinement. Model is jointly fit to X-ray diffraction and NMR pseudocontact shifts (PCSs) / residual dipolar couplings (RDCs), subject to geometry-weight controls. The protein preparation may differ between crystalline/solution states.

## Exact Table 1 pairwise reconstruction
Values below are **published author results directly transcribed from Table 1**, not AI-generated observations. Q_RDC is an NMR restraint agreement statistic (lower is better); R_free is the X-ray holdout-reflection cross-validation statistic (lower is better). See [reproducible Decimal code](../experiments/mqr-5.4/mqr44_r16_published_refmac5_table.py).

| protein (PDB crystal entry) | Q_RDC X-ray only | Q_RDC joint | R_free X-ray only | R_free joint | scoped interpretation |
|---|---:|---:|---:|---:|---|
| MMP-1 catalytic (3SHI) | 0.414 | 0.160 | 0.264 | 0.267 | NMR improves with small X-ray holdout change |
| ubiquitin (3NHE) | 0.360 | 0.121 | 0.158 | 0.160 | agreement at reported test scope |
| GB3 (1IGD) | 0.146 | 0.081 | 0.132 | 0.134 | already low baseline Q_RDC; improved |
| calmodulin (1EXR) | 0.398 | 0.308 | 0.142 | 0.147 | NMR mismatch remains despite improvement |
| calmodulin–DAPk (1YR5) | 0.540 | 0.201 | 0.304 | 0.307 | borderline, authors point to a small remaining state difference |

Published authors describe Q_RDC below roughly **0.2** as useful for their joint structure compatibility analysis, **not** a universal law or ontological truth metric; **0.201 is slightly above** this heuristic. Authors explicitly say that CaM solution vs crystal structural heterogeneity is known and that for free CaM Q remains 0.308 under acceptable X-ray fit/geometry. For CaM–DAPk the 0.201 case is borderline; their independent alternative fits with relaxed structural constraints can achieve lower Q while violating preservation conditions. A reduction in one metric is NOT proof of common structure.

Measured published summary patterns, independently re-arithmetized with Decimal:
- All five Q_RDC decrease under joint refinement, **five of five**.
- **Three of five** joint Q_RDC below 0.2; **two** at 0.308 / 0.201.
- All five R_free increase slightly by **+0.002–+0.005**. This is a small trade-off; no statistical significance or uncertainty interval inferred.
- For MMP-1 Q_RDC 0.414→0.160 is ~61.35% relative reduction, but this is a **reported objective fit improvement after reoptimization**, not held-out NMR generalization.

The computation was run in Python Decimal with eight exact assertions; output verified. These are exact arithmetic assertions **on rounded author table entries** and should not be misrepresented as exact source measurement uncertainty.

## Genuine philosophical discrimination

Compared to [Mitchell 2020 'Through the Fractured Looking Glass'](https://drive.google.com/file/d/1LnEhdfgvcOQtIwGmL1arFveInkE2AZXm/view), the direct original experiment produces both an **integrative success** (compact proteins with compatible constraints) and a **productive integrative non-success** (CaM mismatches indicate potential genuine crystal/solution conformational differences). That is a more informative stress case than asserting 'all integration produces one superior model.' A failed joint single-structure fit can itself supply a **new, specific physical question**: which conditions and protein-domain motions explain the mismatch, not merely which method should be discarded?

Compare [Deulofeu & Suárez 2023](https://drive.google.com/file/d/1bgd9vw84e3tZ80MEGBPmonjg0xUk-Kb_/view): integration may not be desirable for all targets. Do not claim the five protein systems refute Mitchell/Deulofeu, since their arguments already acknowledge purpose-relative success/limits. The researcher (not the author) proposes a new research **diagnostic**: distinguish (1) single-structure joint compatibility; (2) mismatch productively generating a regime-specific conformational question; (3) mere weighted objective overfit; (4) insufficient evidence/poor calibration. This is an analytical classification, not a proven exhaustive taxonomy.

## Essential controls and evidence custody

- The PDB identifiers are **crystallographic structure factor starting points** used by the authors, not five independently downloaded/refined crystal+NMR datasets in this conversation. Corresponding raw structure factors, deposited NMR restraint sets, exact software environment and parameter searches have NOT been downloaded and rerun.
- The NMR Q_RDC values after fitting are **in-sample restraint fits**, while crystallographic R_free provides an X-ray-side holdout; they are not two parallel out-of-sample test sets.
- Some flexible residues were excluded and authors adjusted geometry/PCS/RDC weights; failure or success cannot be treated as wholly independent of these modeling decisions.
- Solid versus solution structures are not guaranteed identical material preparations. Differences can reflect genuine physical regime variation instead of a philosophical language barrier.
- DOI, PDB IDs, numbers come from original primary paper; author reported claims treated as published evidence, not newly instrument certified truth.

## Successor tasks
A. Locate same-paper deposited diffraction source bytes for **one** PDB entry and the article's exact NMR RDC/PCS records; only then attempt a chosen raw->refinement replay. Prefer a case near the compatibility boundary (free calmodulin vs GB3), with a frozen evaluation plan.
B. Ask whether the disagreement prompted an independently executable new experiment (solution state/domain changes, orientation media, mutation, temperature) rather than merely lowering a fit statistic. Require first-hand dated lab follow-up.
C. Compare the source's scientific tradeoff and Fagan's different **normative goal** dispute: instrument data disagreement may be epistemically productive while goals disagreeing can block common evaluation.

**Originality:** HOLD. **MQR 5.4:** OPEN. **Raw 2014 bytes:** NOT ACQUIRED. **Source paper exact Drive PDF:** targeted search no exact confirmed match; original open publisher/PMC full text read. **Official 17 missing-source groups:** unchanged, new source candidate not blindly counted. **Harvest authority:** no transfer.
