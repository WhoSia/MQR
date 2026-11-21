# MQR 5.4 · MQR 44 · R24 — A scientifically stronger physical counterfactual: false mobility versus alignment-medium mismatch

**2026-11-21 KST.** R24 is a substantive follow-on to [R16–R23](mqr_54_chat44_23_iucr_supplement_primary_source_discovery_and_access_hold.md), focused on **measurement-induced apparent scientific disagreement** rather than another toy-state enumeration. `MQR 5.4 OPEN`; independent original-detector-record reproduction **HOLD**.

## Original primary experimental article and bibliographic parity

Azzurra Carlon, Enrico Ravera, Giacomo Parigi, Garib Murshudov and Claudio Luchinat, [*Joint X-ray/NMR structure refinement of multidomain/multisubunit systems*](https://link.springer.com/article/10.1007/s10858-018-0212-3), DOI [10.1007/s10858-018-0212-3](https://doi.org/10.1007/s10858-018-0212-3), *Journal of Biomolecular NMR* **73:265–278 (2019)**, first electronically **published 2018-10-11**. Publisher indicates a later [2019 correction notice](https://link.springer.com/article/10.1007/s10858-019-00238-4) **published 2019-05-08** (open access status was corrected). Do not conflate online-first 2018 and printed 2019 editions or pretend later corrections to bibliographic rights changed measured table numbers without evidence.

Primary original publisher HTML was read directly, with corresponding text-based 2019 PDF passages cross-checked. The PDF screenshot interface returned a *cache miss* so there is no independently established page-image parity; quote the publisher HTML and specific author table, not supposedly inspected PDF pixel rendering.

## The concrete scientific mechanism

A protein complex's two subunits are sometimes separately expressed, isotopically labelled, then reassembled for NMR. If RDC data are collected using samples with slightly different **alignment medium concentrations**, the absolute magnitude of the inferred RDC alignment tensors may change **without requiring physical flexibility between the subunits**. Earlier work on the Sxl–CSD1 complex applied an empirical **0.8 scaling factor** to RDC data for one subunit. Carlon et al. introduce a more structured protocol: allow separate tensor magnitudes but constrain their *orientation* to coincide in a presumed rigid assembly, which captures an alternative measurement condition rather than declaring new protein mobility.

This is **conditional**: presuming a common orientation is justified by an independent rigidity hypothesis or test and is not allowed in advance for every flexible multidomain protein. Alignment tensors can also differ because of true shape dynamics or changes in solution, so the new fit does not prove a unique cause. The physical question becomes: **What portion of the RDC conflict is attributable to different alignment-medium preparation, and what residual still requires a distinct molecular conformation?**

## Direct published experimental table (PDB 4QQB)

Author's Table 1; author-reported rounded metrics below (not MQR's measured NMR signals):

| Model | R_free | RDC Q factor | Bond-length RMSD |
|---|---:|---:|---:|
| Original deposited 4QQB | 0.2360 | 0.440 | 0.0060 |
| REFMAC refit, without NMR | 0.2352 | *not defined/reported* | 0.0064 |
| With NMR, no common-orientation constraint; empirical 0.8 domain scale | 0.2362 | 0.131 | 0.0101 |
| With NMR, imposed common tensor orientation but different magnitudes | 0.2360 | 0.121 | 0.0100 |

Measured **from the rounded published table only**, new constraint versus empirical scaling gives improvements of Q = 0.010, R_free = 0.0002, bond RMSD = 0.0001. These are small performance changes and **not statistical effect sizes with inferred standard errors**. Q reduction from .131 to .121 is 7.63% *of the former Q*, but a quantitative difference alone does not prove a correct physical rigidity model. The deposited original model's Q=.440 reflects its agreement with these RDC observations, not an independent baseline assay.

[Exact Decimal reproduction](../experiments/mqr-5.4/mqr44_r24_carlon2019_tensor_alignment_published_table.py) was committed; **7 independent exact Decimal checks on identical published constants were executed locally** using an equivalent short auditor in the container. The repository script itself was not pulled and re-run byte-for-byte locally; no claim of whole CI. Published numerical table values were verified in the Springer original.

## Important stronger rival constraints from the same paper

In the DAPk-peptide/calmodulin comparison, the authors considered *different molecules' arrangements* under different conditions. The study tests PDB **1YR5** (peptide bound), **2X0G** (whole DAPk bound), and **2BE6** (IQ peptide complex) under distinct domain tensor restrictions. For peptide-bound CaM 1YR5, NMR mismatch and crystallographic packing suggest differences relative to solution structure; whole protein-bound DAPk 2X0G has reduced crystal packing constraints and a better fit **when compared to peptide-bound NMR data**, but the authors themselves note this NMR dataset is not a fresh measurement of full-DAPk complex. Thus **cross-construct transfer remains conditional**. It would be false to assert 2X0G has newly measured same-target NMR evidence on the full complex from this paper.

This contrast rejects both shortcuts:
- 'An RDC mismatch always proves real conformation dynamics' **FALSE as general principle** (alignment media and model geometry can confound).
- 'An improved joint optimization proves no physical regime difference' **FALSE as general principle** (rigidity assumption and sampling condition changes can hide genuine distinctions).

## MQR founding-philosophy inference, carefully scoped

A new scientific question is not an automatic predicate invented whenever two methods disagree; it becomes investigable when specific rival mechanisms can be separated using feasible and calibrated additional measurements. Here the authors' mathematical choice to constrain tensor orientations while allowing magnitudes to vary is **physically interpretable** in terms of sample preparation. This is why mathematics may become productive in engineering and biomedicine: it encodes a conditional invariance anchored to physical operations, not merely an elegant coordinate transformation.

**Prior art:** Carlon et al. themselves designed and tested this method; MQR does NOT claim to invent the calibration/control method or discover the structural phenomenon. MQR contributes a source-typed comparison to our wider historical/philosophical research question. Real-Lang remains peripheral.

## Provenance/open-source gate

[2014 official 10.8MB source supplement and 27KB instructions](mqr_54_chat44_23_iucr_supplement_primary_source_discovery_and_access_hold.md) now LOCATED, but their byte retrieval and member check remain HOLD because of DNS/cache-miss blocks. Carlon (2018 online/2019 print) independent exact Research OS Drive PDF not established by targeted checks; public publisher full HTML suffices for direct reading, not raw-replay custody. Official 17 old heterogeneous missing groups unchanged. No new Global Harvest fragment; no Real-Lang canonical promotion.
