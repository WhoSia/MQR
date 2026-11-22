# MQR 5.4 · MQR 44 · R52 — Real biomedical pairing: sci-CAR joint RNA/chromatin profiles and the exact limit of cross-omics interpretation

**2026-11-23 KST** · BFS molecular biology with direct original source indexed text and journal peer-reviewed summary. Scientific research note only, no experimental protocol instructions. MQR 5.4 OPEN.

## 1. Primary published evidence
Cao et al. (2018), 'Joint profiling of chromatin accessibility and gene expression in thousands of single cells', *Science* 361(6409):1380–1385, DOI [10.1126/science.aau0730](https://doi.org/10.1126/science.aau0730), publicly indexed [NIH full article](https://pmc.ncbi.nlm.nih.gov/articles/6571013/). The study introduced **sci-CAR**, permitting joint profiling of chromatin accessibility and transcriptomes from the **same single cells**. The original abstract reports reconstructing chromatin profiles by RNA-defined cell types, comparing pseudotemporal dynamics and linking candidate cis-regulatory sites to target genes **by covariance** across cells. **Important: covariance alone does not establish a direct causal regulatory arrow.**

A separate 2019 study, Chen et al., 'High-throughput sequencing of the transcriptome and chromatin accessibility in the same cell', *Nature Biotechnology* 37:1452–1457, [PubMed 31611697](https://pubmed.ncbi.nlm.nih.gov/31611697/), describes **SNARE-seq** with paired transcriptomic and accessibility measurements and an inter-assay identity agreement check. It reinforces that scientifically meaningful joint profiles require validated *pairing*, not mere semantic labels.

A 2022 [multiomics review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9191639/) explicitly observes that simultaneous same-cell measurements help avoid the problem of matching different cells from individually profiled modalities. This is existing strong methodological **prior art** to MQR's R44 toy formalization.

**Source-grade limits:** original 2018 abstract/indexing and source snippets inspected, rather than verifying every figure/table from the primary PDF in this turn. 2019 PubMed abstract inspected. PMC open returned a recaptcha in this session, so **full HTML/PDF article close reading and independent participant/cell count reproduction HOLD**. We do not claim single-cell data were downloaded.

## 2. A real operational change beyond better isolated measurements
Two separate laboratories might each perfectly classify RNA or accessible chromatin **distributions across populations**, but without same-cell linkage they cannot identify cell-level covariance directly without assumptions about population matching or conditional independence.

Joint same-cell measurement changes the estimand from disconnected distributions to `P(RNA, chromatin | same measured cell and preparation)`. The physical operation identifies a joint structure that is not reducible to having more precise marginal population estimates. On the other hand, the procedure has its own sampling, capture, dropout, barcode collision, cell-state and preparation disturbances: **paired** does not mean *error-free* or *causally identified*.

The article's documented improvements and cell-level covariance analysis are the proper evidence for new **empirical answerability**, not a philosophically invented 'first time anyone could express genes and chromatin jointly' claim.

## 3. Rival causal interpretations of same-cell covariance
- **R_regulate:** accessibility causes or permits a transcription change at the proposed regulator.
- **R_common:** a shared upstream cell state influences both accessibility and transcription, producing covariance with no direct arrow.
- **R_selection:** cell-type selection, cell viability, barcode linkage or read-depth effects induce an apparent association.
- **R_feedback:** transcriptional activity itself can correlate with or affect chromatin state; association does not uniquely determine direction.

All four can produce same observational joint distributions under some model parameters. Appropriate interventions and replicated target binding matter to distinguish them.

## 4. Comparative negative control
GW170817 pairs independent astrophysical *event* detections by cross-instrument spacetime localization and chance coincidence. sci-CAR pairs different molecular readouts from a **single biological cell**, relying on specimen identity and assay readout validation. These are **not literally the same mechanism**, and there is no guarantee a universal scalar 'bridge confidence' applies. Both provide empirical evidence for an integration obligation: alignment must be grounded in physical event/cell identity and uncertainty.

Where R44 idealized a single Boolean A,B record, this original 2018 example supplies the real need for joint data; however it is a standard, well-known reason for multiomics assay development. A novel MQR claim would require historical circumstances where this source pairing created a class of answerable questions not fully explainable by generic joint-distribution identifiability or scientific integration theory.

## 5. Custody status
Authenticated Drive targeted title searches for 'sci-CAR' and 'Joint profiling of chromatin accessibility' returned no exact 2018 standalone primary PDF; 'SNARE-seq' returned no exact 2019 standalone title. **Not proof of all-drive absence**. Both publicly accessible original bibliographic texts are logged as source radar only, **canonical missing 17 groups unchanged**, no bytes transferred.
