# MQR-4.111 — When Measurement Changes the World It Tests: Irreversible Experimental Histories, Pre-Intervention State Identifiability, Reset Witnesses & the Limits of Scientific Retrodiction

**Formal version:** OPEN (user-fixed title, 2026-10-10). **P1:** mathematically bounded synthetic fixtures PASS; natural-science source comparison PASS_BOUNDED; original empirical retrodiction and MQR-specific novelty HOLD. Previous MQR-4.110 remains OPEN / DISTINCTNESS HOLD. Not a claim of a new theorem.

**Notion current version:** https://app.notion.com/p/3f5ef561cf92815c9263c9d8bcb535dc

## Explanandum and original continuity

An assay is not merely a mapping from a fixed world state to an output. An intervention may alter the state carrying the evidence. What observations and independently validated models justify reconstruction of a *pre-intervention state*, especially if the pre-state is not repeatably accessible?

MQR-4.106 already distinguished readout from state transition. MQR-4.110 distinguished source-authenticated historical measurements, transformed tables and calibration warrant. Neither originated the claim that measurements change the system or that state transitions may be unobservable. This stage asks for rival-divergent claims concerning **physical historical-state retrodiction**, not a renamed behavioral equivalence fact.

## P1 finite two-world countermodels — exact and entirely synthetic

Let pre-intervention feature Q and binary outcome Y be defined in two alternative data-generating models. Each of the eight enumerated elementary atoms has probability 1/8, composed of two equally likely seeds and four equally likely noise slots.

- A (preexisting state): Q=seed, Y=Q, with seed 0/1 equally likely.
- B (probe-created response): Q=0 always at the pre-intervention time; a probe creates Z=seed, then Y=Z.

For both A and B, P(Y=0)=P(Y=1)=1/2. However P_A(Q=1)=1/2 and P_B(Q=1)=0. A protocol that only records Y cannot distinguish A from B; the two models have **different measurement kernels or intervention mechanisms**. This does not prove nonidentifiability when the true kernel has already been externally certified.

### Visible reset is not recovery of an original hidden feature

For each atom, add an operational reset readout R=0 after Y is acquired. Both models then have identical (Y,R) cell counts (4,0,4,0) under the fixed table order (Y=0,R=0),(Y=0,R=1),(Y=1,R=0),(Y=1,R=1); the original Q distributions remain different. An operational response reset can be a many-to-one map and has no general inverse. This is a basic identification result, not an original MQR theorem or a description of any specific OSL reset instrument.

### A certified independent pre-probe marker can separate the worlds

Suppose an *independent pre-probe marker* M reports Q with known symmetric error rate e, and its measurement does not disturb the pre-state or the subsequent probe process. With e=1/4, the empirical joint cell counts over eight equiprobable atoms, rows M=0/1 and columns Y=0/1, are:

A = [[3,1],[1,3]]
B = [[3,3],[1,1]]

Therefore A and B are distinguishable under the **known-marker-kernel assumption**; this is a population-level distinction. With e=1/2, both joint tables become [[2,2],[2,2]], and the marker cannot discriminate.

In general, p=P(Q=1), alpha=P(M=1|Q=0) and beta=P(M=1|Q=1) yield P(M=1)=alpha+(beta-alpha)p. Thus if alpha,beta are **known, invariant, and beta != alpha**, p=(P(M=1)-alpha)/(beta-alpha). This is textbook binary-mixture identification, not MQR novelty. Even then, an individual Q is not necessarily known: for e=1/4 and p=1/2, P(Q=1|M=1)=3/4. The source and non-perturbation status of the marker kernel are scientific claims to validate, not consequences of marker availability.

**Noninvertibility distinction:** a deterministic physical reset cannot generally reconstruct a particular lost microstate, yet statistical inference about an original *population* may remain possible from a known full-column-rank response kernel. Claims about recovering one destroyed object's realized counterfactual must not borrow that population authority.

### Implementation receipt

[Dependency-free Rust exact fixture](../experiments/mqr-4.111/src/main.rs): four tests for identical post-probe distributions with different prior truth, operational reset ambiguity, separation with known marker error 1/4, and failure with marker error 1/2.

[Read-only path-scoped workflow](../.github/workflows/mqr-4.111-irrev-probe-rust.yml), explicitly permissions contents:read, no commit/push/writeback. Actual first run [#38038957460](https://github.com/WhoSia/MQR/actions/runs/38038957460), source+workflow HEAD 560653be2c8c660ec361bae04d3f9f15e51b25d8, GitHub Actions SUCCESS, compile/test execution step SUCCESS; 4 unit tests. Prior model counts independently checked with Python in the analysis environment, also synthetic. **This evidence certifies only this small finite implementation.**

## P1 natural-science rival: optically stimulated luminescence in quartz

Quartz OSL measures stored signals that can be depleted by optical stimulation. The SAR approach regenerates known signal responses and uses test-dose normalization, recycling and dose-recovery reasoning; signal-resetting in the laboratory is **part of an actual inference procedure**, not evidence that historical-state inference is impossible.

- Murray, Arnold, Buylaert, Guérin, Qin, Singhvi, Smedley & Thomsen (2021), *Optically stimulated luminescence dating using quartz*, Nature Reviews Methods Primers 1, 72, DOI 10.1038/s43586-021-00068-5, publisher https://www.nature.com/articles/s43586-021-00068-5. **Author version direct PDF** https://orbit.dtu.dk/files/337668770/MurrayEtAl-2021-AuthorVersion_1_.pdf ; do not conflate author version and publisher Version of Record. **Drive 미확보(색인 검색 기준)** after title/author topic search.
- Murray & Wintle (2003), *The single aliquot regenerative dose protocol: potential for improvements in reliability*, Radiation Measurements 37, 377–381, DOI 10.1016/S1350-4487(03)00053-2; publisher https://www.sciencedirect.com/science/article/pii/S1350448703000532. Publisher text distinguishes dose-recovery tests, slow/fast signal components and recuperation; canonical Drive title searches did not find source; **직접 PDF 미확인**.
- Murray & Roberts (1998), *Measurement of the equivalent dose in quartz using a regenerative-dose single-aliquot protocol*, DOI 10.1016/S1350-4487(98)00044-4, https://www.sciencedirect.com/science/article/pii/S1350448798000444, publisher text identifies cycle-dependent sensitivity change and independent correction logic; **Drive 미확보(색인 검색 기준), 직접 PDF 미확인**.
- Earlier Regnault/Chang glass history remains a qualitative rival example; **the 4.110 DjVu six-page set does not supply a within-specimen pre/post thermal-treatment sequence**, and no such experiment has been newly attributed to Regnault.

**Positive conclusion:** destructive or signal-depleting assays are not automatically epistemically futile. The question is the experimentally warranted **transport** of a response/calibration model from controlled known inputs to the particular natural history whose record is read.

## Adversarial rival court

1. **Known-kernel statistical inference:** if response kernel K(Y|Q) is externally established and injective over the relevant mixture class, pre-state population inference is possible despite destruction; fixed-kernel retrodiction needs no new metaphysical rule.
2. **Unknown-kernel ambiguity:** if both original p(Q) and K vary unconstrained, the two-world example exhibits the ordinary latent model nonidentifiability problem. Existing causal inference and measurement theory suffice to explain it.
3. **Behavioral states and causal abstractions:** Barnett & Crutchfield (2015), *Computational Mechanics of Input–Output Processes*, Drive https://drive.google.com/file/d/1enuIYvv7dF4B1r59nCcGQmdO8mthCCwO/view ; Geiger et al. (2025), *Causal Abstraction*, JMLR original in Drive https://drive.google.com/file/d/1dkkczKfLgmHL8YPwKWrKunEdCbAel6hK/view. Distinguishing all permitted future behavior and intervention fidelity is already developed in these theories.
4. **Measurement philosophy:** Tal (2017), *Calibration: Modelling the measurement process*, Drive https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view ; Tal (2019), *Individuating quantities*, Drive https://drive.google.com/file/d/1dm4Oea-l6BVMEuZGTwe-OeUp05gYTzrA/view ; Chang (2004), *Inventing Temperature*, Drive https://drive.google.com/file/d/1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV/view. Model-mediated accuracy, sensitivity, quantity identity, and the history of thermometric comparison are strong rivals; no distinct philosophical MQR prediction so far.
5. **Retrodiction versus reset:** a successful known-dose recovery control tests the stated control conditions; it does not, without transport assumptions, prove that every historical signal was acquired in an identical state regime. Conversely, lack of literal microstate restoration does not invalidate calibrated dose inference.

## Prospective falsification (not performed)

Using **existing published OSL datasets and protocols**, search for paired reported natural-versus-controlled recovery outcomes and variation in sensitivity/recycling/recuperation. Define the original historical quantity and claimed uncertainty first. Compare (H0) a calibrated known-input response law that transports to natural archives against (H1) a prehistory-dependent response law. Hold source/aliquot/processing choices constant or model documented differences. Pre-register a divergence observable from published records; if ordinary validated correction models already explain it, reject distinct MQR explanatory gain. No irradiation, optical or thermal treatment, laboratory intervention, subject exposure, new experimental data or physical replication performed here.

## P1 verdict and next

- **FORMAL_VERSION:** MQR-4.111 OPEN (authorized by user).
- **P1_SYNTHETIC:** finite counterexample and known-marker identification PASS_BOUNDED; exact Rust CI successful.
- **P1_REAL_CASE:** OSL established literature contact; new independent primary experimental data not yet reanalyzed.
- **RETRODICTION_CLAIM:** unknown-kernel original-state identification HOLD; model-conditional population inference possible.
- **ORIGINALITY:** HOLD. Any forthcoming result must defeat a named existing theory on the same empirically measurable target.
- **NEXT P2:** source-specific OSL paper/data acquisition and concrete discriminating observable; meanwhile preserve all 4.110 source errata and other preexisting HOLDs. No automatic successor version or new Court required.

## P2 — Source-linked OSL validation contrast (literature-level only)

**Purpose:** identify an actual measurable rival-sensitive contrast, *not* a new MQR discovery. Primary empirical observations are drawn from published author/publisher abstracts and publisher-visible sections; underlying numeric tables, archived individual grain curves and full original PDFs for the following two works were not obtained. The cases are independent and **must not be pooled as if they were one cohort**.

1. Choi, Murray, Cheong & Hong (2009), *The dependence of dose recovery experiments on the bleaching of natural quartz OSL using different light sources*, Radiation Measurements 44, 600–605, DOI 10.1016/j.radmeas.2009.02.018. [Publisher article](https://www.sciencedirect.com/science/article/pii/S1350448709000407). The authors report that the apparent recovery of a known laboratory dose depends on signal-resetting conditions and can underestimate the reference by about 20% in studied circumstances; other tested conditions recovered known doses. They investigated changes in luminescence sensitivity as a physical explanation. **This finding is theirs; it is not our experiment or new inference.** Drive title/DOI search: **미확보(색인 기준)**; direct full PDF: **미확인**.
2. Costas et al. (2012), *Comparison of OSL ages from young dune sediments with a high-resolution independent age model*, Quaternary Geochronology 10, 16–23, DOI 10.1016/j.quageo.2012.03.007. [Publisher](https://www.sciencedirect.com/science/article/pii/S187110141200060X); [MPI metadata abstract](https://pure.mpg.de/pubman/item/item_2129408). Independent aerial-image and radar-based dune history permits comparison to OSL-based dates; the authors report overestimation by 10–40 years in six of seven younger samples, associated with incomplete signal bleaching and an experimental signal transfer mechanism. These are source-abstract figures only, **not a new row-level reanalysis**. Drive title/author search: **미확보(색인 기준)**; direct original PDF: **미확인**.

**Different source roles:** Choi tests protocol-sensitive *controlled recovery*. Costas supplies an external independent *historical-time reference*. A difference within Choi does not establish the mechanism in Costas, and Costas did not give MQR a new dose-recovery effect. These cases instead define two independent validation axes (same-protocol controlled input / world-facing independent time) that an adequate historical measurement model should explain.

### Targeted mathematical research design

Let h represent the material's prior physical history, pi an observational protocol, D the historical quantity, and K_{h,pi}(y|D) the measurement response kernel. A controlled recovery test at (h_cal,pi_cal) constrains K_{h_cal,pi_cal}. Transport to naturally archived material (h_nat,pi_nat) requires a justified relation between the kernels, NOT just successful recovery in the calibration regime.

A prospective falsifier would pair available published cross-regime histories with external age constraints, specify two rival kernels with competing predictions for a *shared material and measurand*, and check pre-specified residuals under ordinary SAR corrections. If established correction models already predict the discrepancy, label the result a conventional positive validation / negative MQR distinctness. No such paired archival raw dataset was identified or analyzed in this stage.

**P2 status:** SOURCE-ABSTRACT-REVIEW PASS; EXACT ORIGINAL ARTICLE PDF and per-sample recorded DATA HOLD; new empirical result HOLD; MQR theoretical novelty HOLD. Keep MQR-4.111 formally OPEN.

## P3–P4 — Recovered originals and real published-summary dose rival audit (2026-10-10)

**Priority of latest status: the P2 statements “Drive unavailable/PDF unverified” are historically accurate *only at P2*. Five full-text PDFs were subsequently found in \`00_INTAKE\` and normalized to \`10_PAPERS\` with unchanged file IDs and verified byte sizes. Source acquisition **PASS**; standalone raw aliquot-level files and supplementary Fig. S1 (recovery-distribution observations) remain **HOLD**.**

### Original paper identity and Drive custody readback

| Paper | Canonical Google Drive PDF ID | Checked byte size | Version |
|---|---|---:|---|
| Choi, Murray, Cheong & Hong (2009), *The dependence of dose recovery experiments on the bleaching of natural quartz OSL using different light sources*, DOI 10.1016/j.radmeas.2009.02.018 | [1TZzW1U1w4qqJMtav54AlXJ_Ix41V9fqA](https://drive.google.com/file/d/1TZzW1U1w4qqJMtav54AlXJ_Ix41V9fqA/view) | 450,951 | publisher article PDF |
| Costas et al. (2012), *Comparison of OSL ages from young dune sediments with a high-resolution independent age model*, DOI 10.1016/j.quageo.2012.03.007 | [1x1hlqsoszLVHzh1-aC1VGlNcj2MhX6du](https://drive.google.com/file/d/1x1hlqsoszLVHzh1-aC1VGlNcj2MhX6du/view) | 1,258,106 | publisher article PDF |
| Murray & Wintle (2003), *The single aliquot regenerative dose protocol: potential for improvements in reliability*, DOI 10.1016/S1350-4487(03)00053-2 | [1NKsPryjVZsswUcQxzt56P9P3-BUbYwgN](https://drive.google.com/file/d/1NKsPryjVZsswUcQxzt56P9P3-BUbYwgN/view) | 123,848 | publisher article PDF |
| Murray & Roberts (1998), *Measurement of the equivalent dose in quartz using a regenerative-dose single-aliquot protocol*, DOI 10.1016/S1350-4487(98)00044-4 | [14NDmYiEblFBI6lp-mo0mzbFqzb-jrEYt](https://drive.google.com/file/d/14NDmYiEblFBI6lp-mo0mzbFqzb-jrEYt/view) | 523,279 | publisher article PDF |
| Murray et al. (2021), *Optically stimulated luminescence dating using quartz*, DOI 10.1038/s43586-021-00068-5 | [1PechsfyJwe4zJ6wA7khYBLbjXrsNDYwx](https://drive.google.com/file/d/1PechsfyJwe4zJ6wA7khYBLbjXrsNDYwx/view) | 5,950,814 | DTU Orbit **author version / early preprint**, not publisher VoR |

The five were moved by Drive metadata-only \`update_file\` from \`00_INTAKE\` (folder ID \`1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16\`) to \`10_PAPERS\` (folder ID \`1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP\`), with canonical author/year/title names. Readback confirmed all five final parents and original byte sizes. No PDF edits or copies were made; no full source SHA256 was independently computed. Intake JCGM 200:2012 file \`1JARbDk01J3xluNFIpWUPyAs7CsQqK9RB\` **PRESERVED** because a canonical VIM document already exists in \`10_PAPERS\` \`1qg5-xP0puqjay3Rd9VXq9yHX44JIk-YM\`; byte-level equality of these separate files was **not** verified.

### Five-paper conceptual triangulation, no novelty claimed

- **Murray & Roberts 1998:** same-aliquot regenerative measurements require within-cycle sensitivity correction; 13 sample comparisons were documented. The DS3 protocols differ (printed text gives e.g. 4.33 ± 0.09 Gy versus 5.17 ± 0.06 Gy from the two techniques); not all methods are universally interchangeable.
- **Murray & Wintle 2003:** fast-vs-medium/slow OSL contributions and recuperation bias are already recognised; isolating a fast component and testing known-dose recovery is standard. A test-dose-normalized L/T curve is model-mediated.
- **Choi et al. 2009:** long solar-simulator bleaching led to ~20% under-recovery in tested samples, while alternative lights/short exposures often recovered known inputs. Figure 2 uses *different laboratory reference doses* for PK03=10 Gy, T9=30 Gy, 0011KS-1=150 Gy. Their modern-dune sample D-1 recovered laboratory doses 20/60/120 Gy (Fig.7). Their Figure 5 varies dose, duration, light intensity and prior history. The original authors propose sensitivity changes, not a new MQR back-action discovery.
- **Costas et al. 2012:** 13 sites along a Sylt dune transect with independent aerial/GPR relative chronology, natural OSL dose and SAR recovery. Oldest boundary sample GWD-0 is excluded by the authors due to geological context: the external “age reference” is itself conditional on which depositional unit the sample belongs to.
- **Murray et al. 2021:** full author-manuscript review describes L/T sensitivity correction, cycling, recuperation, component saturation, independent-age comparisons. Its Figure 11 discusses hundreds of independently dated examples; one adverse seven-sample subgroup must not be used to indict OSL dating globally.

### Costas 2012 published Table 2 — checked transcription and exact Rust recomputation

[Source transcription and exact Rust code](../experiments/mqr-4.111/costas_2012_table2.rs), original table in the linked Drive PDF p.19. 13 table rows and all age columns are from published *sample summary rows*, **not** individual aliquot raw files. Contributing 2012 paper data: 13 site samples, n≈23–24 aliquots per sample. They reported recovery checks with n=78, mean (measured/given) LBG 1.019 ± 0.004 and EBG 1.011 ± 0.007. These recovery values are separate laboratory tests, not observations of true OSL ages.

Published history-based age and laboratory luminescence age are different validation targets. For youngest 7 (GWD-100, 140, 160, 180, 200, 220, 245):
- expected chronological ages [59,43,35,28,20,12,2] years;
- EBG OSL ages [94,65,97,77,60,40,34] years;
- signed age differences [35,22,62,49,40,28,32] years; mean **38.2857 years** (unweighted, cross-sample descriptive).
- Table 2 history-model expected equivalent doses [41,31,26,19,13,8,1] mGy;
- EBG observed equivalent doses [66,46,71,51,41,28,23] mGy;
- dose differences [25,15,45,32,28,20,22] mGy; unweighted mean **26.7143 mGy**, median **25 mGy**.
- five older same-depositional-unit rows GWD-10 through GWD-80 (GWD-0 excluded): dose differences [-4,10,2,17,5] mGy; unweighted mean **6 mGy**.
- For young seven, there are **six nonoverlapping pairs of separately drawn expected/observed ±2σ intervals**, GWD-140 being the overlap case; this interval criterion is **NOT** equivalent to a standard 2σ test on their difference under independence, and no independence of age reference and OSL errors or between samples is certified. The source authors' 6/7 age-overestimation characterization should be read as their declared criterion, not a newly computed p-value.

**Miniature physical rival models on dose scale**, descriptive only, selected *after* reading the paper:
- additive-offset model \`y=x+c\`, one parameter \`c\`, reflecting e.g. residual stored component and/or thermal transfer;
- pure proportional model \`y=a*x\`, one parameter \`a\`, reflecting e.g. a simple multiplicative sensitivity calibration mismatch.
- Unweighted leave-one-out RMSE on seven young rows: **10.5409 mGy** for additive offset vs **19.7591 mGy** for pure proportion. Whole-sample best-fit additive offset c=26.7143mGy. No attenuation, measurement-error, source-sharing, uncertainty, background or full covariance model fitted, and N=7; model comparison is exploratory and *is not* a causal adjudication.
- Costas et al. already measured thermal transfer **4–12 mGy** and identified about **15 mGy** extra residual attributable to incomplete bleaching of a medium OSL component (under their tested procedure). These already-known mechanisms and source differences compete directly with an alleged novel MQR causal account.
- **Important physical limitation:** the fitted 26.7mGy *group mean difference* is not an independent estimate of the paper's mechanism-specific ~15mGy component; they are different quantities.

Actual scoped CI:
1. Initial dual-source [#38040038036](https://github.com/WhoSia/MQR/actions/runs/38040038036) FAILED solely on \`rustc -D warnings\` release build: \`lbg_bias\` only used in tests, dead-code warning; 4+4 unit tests had already passed.
2. Human-authored source patch \`7539ab3\`; [#38040095767](https://github.com/WhoSia/MQR/actions/runs/38040095767) SUCCESS: 4 synthetic + 4 real-table tests.
3. Dose-scale summary and competing one-parameter LOOCV added in human-authored \`05913877dcc3c70ed36681afc07e3da10459585f\`; [#38040322286](https://github.com/WhoSia/MQR/actions/runs/38040322286) **SUCCESS**, verified log **4 synthetic + 6 table and model tests**, and printed numeric outputs match the transcription. All source code and workflows are on \`main\`; Actions permissions \`contents: read\`; no automated writebacks.

### RAVEL: falsifier scope and source-boundary issues

**Strong conventional explanation currently survives**: imperfect natural bleaching + protocol-specific thermal transfer + known source-component mixture. The observed “dose-recovery pass but age mismatch” was already diagnosed in the Costas paper. The proposed measurement-history kernel \`K_{history,protocol}(y|D)\` acts as explicit *bookkeeping*, not a new MQR physical law.

A stronger future study needs a **same-sample linked data source** with original SAR \`Lx/Tx\` cycles, controlled dose-recovery/recuperation, natural dose and independent age + stratigraphic assignment. Figures or captions are not such raw trajectories. Search reproducible raw OSL datasets; for example, the independent R-Lum \`Luminescence\` package includes a real quartz sample \`ExampleData.LxTxData\` and example SAR raw files, but those sample examples do **not** inherently come with the Costas 2012 independent historical reference dates. Combining different paper cohorts would be pseudoreplication and is prohibited.

**Reopen trigger:** before claiming distinctive MQR contribution, name (A) a standard SAR/physical-history/covariance model and (B) a materially different prediction about *the same named aliquot or sample*, then obtain genuine source data where they conflict. Otherwise classify work as a reproducibility and science-history case study.

**P3 status:** original PDFs PASS / source identity readback PASS / independent byte-level SHA-256 unverified / raw aliquot and 2012 supplementary figure file HOLD.
**P4 status:** published-summary exact arithmetic + post-hoc one-parameter model comparison **PASS_BOUNDED** / causal mechanism discrimination and original theory **HOLD**. MQR-4.111 remains **OPEN**.

## P5 — Archive-identity witnesses, missing S1 and stronger standard competitors (2026-10-10)

**Source-coverage result:** Retrieved/read canonical original full Costas 2012 source on Drive; source paper itself *states* `Appendix A. Supplementary material` and points to DOI `10.1016/j.quageo.2012.03.007`. Fig. S1 is cited twice as the 78-recovery-observation graph, but is not part of the eight printed pages and a matching standalone PDF, plot data or original `BIN/BINX` readings was NOT found in Drive searches (`Costas`, `GWD`, `aliquot`, `Reimann`, `supplementary`, and direct intake folder). Publisher, AWI EPIC, MPG PuRe, dissertation archive and indexed supplemental searches yielded bibliographic descriptions but no separately fetched Fig S1 or individual Costas aliquot bytes. Guessed static publisher paths did not open; **do not convert speculative paths into source links or an assertion that the supplement does not exist**. Exact Fig S1 original **HOLD**; 78 per-aliquot recovery measures **HOLD**.

### P5 real sample material witness: GWD-245 (published author results; NOT our experiment)

The actual source's **Table 2** and **discussion** link three distinct evidence streams for the sediment sample (NOT the same physical grain):

| Independent or experimental evidence | Published source summary | Role / limitation |
|---|---:|---|
| Aerial-photo+GPR stratigraphic age model | **2 ± 1 years** and *expected* equivalent dose **1 ± 1 mGy** for GWD-245 | External age estimate is model-derived from mapped dune history, not directly observed burial time |
| Natural source OSL EBG measurement | **23 ± 5 mGy** | Same geological sample code; main experimental 2012 Table 2, not raw photons |
| Subsequent daylight-cleared separate aliquots of GWD-245 | **8 ± 1 mGy** residual, 24 aliquots, per source §5 | Separate subsamples; includes signal-transfer/residual influences rather than demonstrated microstate reset |

Arithmetic checks: observed minus independent-chronology expectation = **22 mGy**; natural minus separately cleared residual = **15 mGy**, as described by the authors; formal subtraction of the latter operational 8 mGy reference from the *age discrepancy* gives **14 mGy**, but this is **conditional arithmetic**, not a point-identification of a specific source compartment because aliquots and measurement kernels differ. Do **not** count the 8mGy residual and its possible thermal-transfer part twice. Original authors also report 4–12mGy transfer effects in tested regimes and a natural-versus-regenerated **component-shape difference** for another sample GWD-140 (natural initial curve more medium-component influenced, regenerated curve more fast-component influenced). All these phenomena and interpretations were already published by Costas et al.

**Bounded physical verdict:** a *pure residual from the common post-reset measurement step* cannot alone explain all of the natural-versus-daylight-cleared difference **if** the two subsample response laws are stable and comparable; natural-history signal not fully absent is a good source-consistent explanation. Nonetheless imperfect pre-burial bleaching, protocol-induced component redistribution, subsample heterogeneity, response-kernel drift, and dependence in uncertainties are not separable from the published aggregates. Thus the **evidence of signal-history sensitivity is stronger than a simple age-table correlation**, but a unique causal mechanism or an MQR-specific new law is not established.

### Independent geological age-model source audit

The Costas article explicitly says a **1925 map** and **seven aerial images** are available, yet immediately enumerates **eight** aerial-image years (**1936, 1944, 1958, 1965, 1988, 1998, 2003, 2009**) and then refers to **eight isochrones**. Whether one image was left out of the actual age-line fitting cannot be settled from those sentences or Table 2 alone. This is a narrow documentary count ambiguity, NOT proof that the age model is invalid. The published **4.1 m/yr dune migration rate** is not automatically the inverse gradient of the 245m-transect age series: dune-front travel and stratigraphic depositional-age position are distinct geometries and GPR transfers control across units. Required external witness: the original georeferenced photo/map index, which images/isochrones entered the fit, GPR transect alignment and uncertainty/covariance. Parent 2013 dissertation *Climate Archive Dune* by Iria Costas Vázquez, Hamburg thesis entry https://ediss.sub.uni-hamburg.de/handle/ediss/5374, identifies a 17.59 MB attached dissertation PDF; not byte-fetched or read here and cannot be treated as having the missing raw records.

### Truly published raw grain/aliquot dataset competitor found — Guérin et al. 2021

Guérin et al. 2021, *Towards an improvement of optically stimulated luminescence (OSL) age uncertainties: modelling OSL ages with systematic errors, stratigraphic constraints and radiocarbon ages using the R package BayLum*, [official peer-reviewed article](https://gchron.copernicus.org/articles/3/229/2021/) DOI 10.5194/gchron-3-229-2021, [official 665KB supplement ZIP](https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip). Publisher article confirms that its **FER1/FER3 site-specific data folders** provide raw BIN/BINX OSL signals for a **subset** of measured grains and CSV `DiscPos`, `Rule`, `DoseSource`, `DoseEnv`, alongside an R Markdown reproduction tutorial. This is unusually well-connected provenance for a demonstrable published source-replay court. However the ZIP download through available Web and container pathways did not return actual bytes in this session, so **source presence CONFIRMED BY PUBLISHER but local/Drive ingestion NOT VERIFIED and no computations on raw FER grains were run**.

**Critical independent-age split in Guérin:** §3 compares FER3 OSL to **three real 14C ages published for the same archaeological layer** in Guérin et al. 2015, and §4 constrains layer order. But its later §6 demonstration **explicitly assigns arbitrary illustrative radiocarbon ages** of 38,000 ± 400 BP and 44,000 ± 400 BP to explore Bayesian behavior. These are not newly measured independent dates; do not treat them as observed historical ground truth. FER1 and FER3 are different strata and are not Costas GWD samples. Established BayLum already models covariance, strata and radiocarbon; MQR cannot rebrand that facility.

**Alternative truly archived raw repository:** Mauz, Kreutzer & Lawless (2026), [Zenodo dataset DOI 10.5281/zenodo.21226350](https://zenodo.org/records/21226350), 31.5MB project ZIP containing original BINX, published-source CSV LxTx and reproducibility scripts. Source affiliation/sample identity is **different** from Costas or Guérin; cannot attach Costas' independent-age labels to this corpus. A second Fuchs et al. 2013 [78.9MB BIN/dose-recovery dataset](https://zenodo.org/records/8246533) likewise cannot be silently joined with Costas 2012.

### Three competing mechanisms and what is still unidentified

1. **Natural pre-burial retained signal:** predicts age bias even with a good laboratory known-dose recovery; also predicts natural vs extensively cleared curve-content difference if observation kernels are comparable. Source report is consistent, but no original grain-level paired repeated signals are available.
2. **Measurement-induced carryover / thermal component transfer / component-specific sensitivity:** predicts differences by laboratory observation protocol, signal component, and history. Source demonstrates such effects in controlled subsamples, so it cannot simply be excluded. Full raw Lx/Tx and exact per-aliquot labels needed for quantitative competition.
3. **External chronology/stratigraphic alignment or shared dose-rate model error:** predicts site- or regime-correlated residuals. The GWD0 original exclusion and shared age-reference construction show this must remain a competing contributor; requiring independent photo/GPR fit data and uncertainty correlations.

Already-adjudicated observations: controlled EBG dose recovery 1.011±0.007 (n78, mean; manuscript) alongside GWD245 23mGy natural versus 1mGy expected; authors' natural-vs-cleared contrast 15mGy; older-five vs young-seven mean dose residuals 6.0 vs 26.714mGy; GWD140 natural/regenerated curve composition difference. An across-cohort point estimate of contribution shares is **not** identifiable from these published summaries. MQR distinctness **HOLD** against original authors, SAR physics, BayLum, and standard inverse-problem identification.

**Formal data-ingestion gate (metadata only; no real-world experimental instructions):** Every new digital record must carry exact publication DOI, archive identifier, source file checksum/byte count, sample ID, aliquot/grain ID, whether natural or regenerated, observation order, signal curve/channel data, pre-processing decision, response-normalization record, age-anchor georeferencing/stratigraphic unit, shared calibration ancestry and uncertainty covariance. Do not pool rows lacking cross-record join keys or use a published figure as raw individual-level data.

**P5 executable receipt:** [source-witness Rust assertions](../experiments/mqr-4.111/costas_2012_table2.rs), [read-only CI #38041208652 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38041208652), source head `506165f09cb55b9001184ea702786d981f6e6992`, **4 synthetic + 8 published-summary/source-consistency tests** (12 total), actual log verified. No new physical trials or material manipulations were conducted.

**P5 final:** SAME-SAMPLE PUBLISHED SUMMARY TRIANGULATION PASS_BOUNDED; REAL COSTAS INDIVIDUAL ALIQUOT BYTES HOLD; COSTAS S1 HOLD; COMPLETE INDEPENDENT AIRPHOTO/GPR AGE CONSTRUCTION HOLD; DIFFERENT-SOURCE FER RAW PUBLISHED UPSTREAM BUT INGESTION HOLD; POINT-CAUSAL MECHANISM and ORIGINAL MQR LAW HOLD. Do not open 4.112 or claim closure.

## P6 — 2026-10-10 00_INTAKE original-byte ingestion, upstream supplement rescue and shared-error tests

**SCOPE:** User approved a literature/raw-data intake audit and continued **inside** MQR-4.111, no new formal version. This phase removes archival blockers but DOES NOT alone decide irreversible-retrodiction theory or identify a unique physical mechanism.

### Entire accession and source custody (Google Drive, 32 items, metadata-only moves)

Full source-by-source audit with exact Drive file IDs/links and per-item status: conversation artifact \`MQR_00_INTAKE_FULL_AUDIT_20261010.md\` (2026-10-10; users can retrieve in the current conversation). The intake changed while auditing (new GUM-5:2026 and two Heawood volumes arrived). A verified 32-item accounting: **16 journal/preprint/accepted-manuscript PDFs** to central \`10_PAPERS\` (folder ID \`1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP\`); **four** journal-volume/thesis/JCGM authority sources to \`11_SOURCES\` (folder ID \`1Ee2UDLahRj4ozlnNUXZcQk6Xsbr1Bqfv\`); **eight** research ZIP/derived/strict SHA-duplicate assets to MQR \`01_SOURCE_ACCRUAL_RAW\` (ID \`1rJiWzqG88bfK0tDf4C5Ta2IzYCq0AiBc\`); **four** historical MQR/KSGT/EvoNOMOS handoff or KSGT paper ZIP in \`00_INTAKE\` (ID \`1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16\`) not moved without cross-lab ownership resolution. No PDFs or ZIP bytes were edited, no deletions or overwrites. Verified new parent IDs and file names on each move. Duplicate original PDFs were held with explicit DUPLICATE names rather than trashed.

**Original OSL competitor court now expanded:**
- [Murray & Wintle (2000)](https://drive.google.com/file/d/168eb8qJLiIsFHLjeeVCRFTtWu-ihhXmj/view), [Wintle & Murray (2006)](https://drive.google.com/file/d/1Y34eZF_2XA92QXC4CLxQI31Don3gs2Dh/view), [Cunningham & Wallinga (2010)](https://drive.google.com/file/d/1btO7sq5qbzQe7OpKki1G66qzeqHd1RKc/view) directly establish test-dose sensitivity correction, SAR protocol prehistory/recycling/recuperation tests, and signal-selection EBG versus LBG. Cunningham's fast-dominant net signal from an early background immediately following the initial integral is an **explicit existing approach**, and its physical explanations strongly compete with 4.111.
- [Combès et al. (2015)](https://drive.google.com/file/d/10RBHB4BIqqFr5KM_VK_RfztykPYb7bbZ/view), [Combès & Philippe (2017)](https://drive.google.com/file/d/1suuf6C_25a6hzzx3MA4LOQE2uq47z69x/view), [Philippe et al., BayLum introduction](https://drive.google.com/file/d/1bz_9qHLnHLRuIgpgnjHQptxyFR9qOIaP/view), and [Guérin et al. (2021)](https://drive.google.com/file/d/1hgzZlM8HbVyq5l_auJyS36mQo2u3nAZb/view) already provide Bayesian inverse modelling, shared covariance and stratigraphic chronology. The 2015/2017/2018 BayLum-era PDFs include **publisher accepted-manuscript variants**, not final version of record; 2019 label is metadata bibliographic, not proof of final text version.
- [Reimann et al. (2012)](https://drive.google.com/file/d/1WKR2cz5wFOsX9orise2lavkaN-PPQD2S/view) is a DIFFERENT Sylt mixed coastal sediment study with finite mixture model and small/single-grain methods; no direct GWD sample ID union. [Ballarini et al. (2003)](https://drive.google.com/file/d/103PjbEZmDyIy3DEffSJ54bm1f-28ijgb/view) report 17/20 independently controlled samples in good agreement; [Madsen et al. (2007)](https://drive.google.com/file/d/1XLkySMB6vAH5QK3L100inVI7WQgyP_za/view) report acceptable \`210Pb\` age comparisons. These constrain any sweeping source-invasiveness theory: calibrated OSL can work in young, well-bleached environments.
- [Taylor & Noyes (1944)](https://drive.google.com/file/d/1PpY7wF9xxtErRVKz4d9rK_CtPL3XOWj8/view) reports conventional time-dependent thermometer bulb drift, including non-monotonic/multi-rate cases. Source PDF begins with unrelated preceding journal content, so it is marked journal excerpt rather than a standalone original. [Brown, Hod & Kalemaj (2022)](https://drive.google.com/file/d/1690w4PxcI0lHBFgNmTulv_CkFS36r79p/view) and [Zhang et al. (2023)](https://drive.google.com/file/d/1KRbWsoKUy3OcBoV4q5yY05QPZyxC5njt/view) add well-developed conventional models of stateful performativity/intervention design; not new MQR laws.

### Original 2012 Fig S1 is materially recovered in same-author 2013 thesis

[Costas Vázquez (2013), *Climate Archive Dune*, PhD thesis, first-party original](https://drive.google.com/file/d/1Y-jl7Thu3__5shXZ2zH0VLifvIOVqNPP/view), **PDF page 23 = printed page 20, Fig. 2.4** directly reproduces the two dose-recovery histograms that the 2012 publisher article referred to as online Fig S1. It reports LBG \`n=78\`, mean \`1.019±0.004\`, observed SD \`0.036\`; EBG \`n=78\`, mean \`1.011±0.007\`, SD \`0.062\`. Histogram visualization and aggregate statistics can now be viewed in the first-party thesis; separate exact publisher supplement PDF/image byte identity is **NOT** known and individual 78×2 response values and Lx/Tx are still **HOLD**. No fake extraction of individual histogram observations has been performed. The thesis includes mapped dune/geophysical figures, but **does not provide raw georeferenced aerial rasters, GPR traces or estimated across-site age covariance matrices**.

The thesis confirms the existing count ambiguity: prose “seven aerial images and one historical map (1925)” but explicitly lists **eight** photo years 1936, 1944, 1958, 1965, 1988, 1998, 2003, 2009, while claiming eight fitted isochrones. Exact inclusion in the fit **HOLD**; model error is **NOT** thereby proven. This new original source improves geographic/document provenance, not same-aliquot inverse identification.

### Public original ZIPs: CRC, SHA-256, provenance and duplication

\`Guérin_2021\` original supplement ZIP: [Google Drive](https://drive.google.com/file/d/1BCujdWongKH2nA2RJjnBRao1dsJHGzJg/view), \`681776\` bytes, 229 ZIP entries, **CRC PASS**, SHA-256 \`25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228\`. Original two \`.BIN\` files from FER1/FER3 have 592704 and 526848 bytes, respectively; in each \`DiscPos.csv\` there are **49 unique selected (disc,grain) pairs**; FER1 11 discs, FER3 21 discs. They represent **subsets** of the actual measured grains, not the whole historical experiment. Source \`DoseSource.csv\` provides common \`obs=0.0445,var=0.000000792\` for both; \`DoseEnv.csv\` reports FER1 \`obs=1.93,var=0.007706\`, FER3 \`obs=1.58,var=0.006992\`; units and normalization must be read in original Rmd/article before combination. This receipt verifies byte custody, archive integrity, and metadata parsing, NOT a posterior BayLum/MCMC inference. \`.Rproj.user\` cache files are not observations.

[Guérin's two authored illustrative covariance CSVs](https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip):
\`\`\`
Matrix A ("SimplisticExample")     [[0.009191746,0.007616071],[0.007616071,0.007991537]]
Matrix B ("RealisticExample")      [[0.009191746,0.002152365],[0.002152365,0.007991537]]
\`\`\`
The same marginal variances \`0.009191746,0.007991537\` with two alternative **assumed covariance terms** imply correlation \`0.88862150555\` vs \`0.25113182726\`. Let \`Z=X_1-X_2\`; \`Var(Z)=V11+V22-2 V12\`. Exact source-decimal arithmetic yields \`0.001951141\` vs \`0.012878553\`; SD \`0.04417172\` vs \`0.11348371\`, variance ratio \`6.600524\`. This is a comparison of TWO AUTHOR-SUPPLIED MODELLING SCENARIOS, NOT two freshly measured physical environments. Existing standard GUM/BayLum covariance treatment already entails the difference. Independently executable minimal Rust source: [fer covariance fixture](../experiments/mqr-4.111/guerin_2021_fer_covariance.rs), read-only CI extended in \`.github/workflows/mqr-4.111-irrev-probe-rust.yml\`; software receipt and final log must be verified separately from source claims.

\`Mauz/Fuchs\`:
- [Mauz V1 ZIP](https://drive.google.com/file/d/1lDMDTBt18gxycqi629EV2R45QBaNTt9t/view), \`31456514\` bytes, 505 ZIP entries CRC PASS, SHA256 \`a3388aa51adb357a1a61b3aeac3ca03fcfcbacfa05846b789eb1af116d6f99c3\`.
- [Fuchs dataset ZIP](https://drive.google.com/file/d/1dDhIgn7WItrpR6vQyzJU8EcfBRgZuU_N/view), \`78925285\` bytes, 430 ZIP entries CRC PASS, SHA256 \`05ca8d57446b5c09c986d54b6fc8d7afda9391fa6d692575c6960855f6daa1dc\`.
- At least **four** files are identical across datasets by SHA-256: \`20120718_HighDoseExperiment_BT754_FGQ.BIN\`, its \`.SEQ\`, \`20120720_HighDoseExperiment_BT754_753_755_FGQ.BIN\` and its \`.SEQ\`. Two ZIPs therefore share some PRIMARY EXPERIMENTAL SOURCE and cannot count as independent confirming trials for overlapping runs. The [Otor workbook](https://drive.google.com/file/d/1U4BhFuIMzJU0pkiXjUWudl5YndQSAsbW/view) gives parameter results and should be treated as a derived table until the same sample/UID/aliquot lineage is tracked. The small \`data_for_figures_1,2,9.zip\` has 3 CSV/3 Python but **source-article attribution is still HOLD**, despite plausible relation.
- Existing redundant Costas article, VIM and Heawood source files were confirmed byte-**SHA256 identical** to canonical original file ID counterparts and explicitly flagged, not deleted.

### Correct source location for 1890 original Heawood

[Quarterly Journal vol. 24, 1890 original 83,170,297-byte Göttingen scan](https://drive.google.com/file/d/12S2u1WeI5B-VF9Ukrkco16HCQ6k-PFj3/view): P.J. Heawood, *Map-Colour Theorem*, original **printed pp.332–337**, PDF **pages 351–356** (1-based). Next printed p338 is a different author; earlier bibliographic p332–338 inference must not be perpetuated. Original source-view **PASS**, exact old diagram graph adjacency and interpretation **HOLD**, no new mathematical theorem claimed. Duplicate same-SHA scan is archived in MQR raw folder, not deleted.

### Further source gaps / science judgment

1. **Costas lab raw original**: GWD0–245 individual aliquot \`Lx/Tx\`, BIN/BINX, per-aliquot dose recovery n=78, recycling/recuperation, order, exclusion flags. Available article/table/histogram does NOT identify those individual histories. Publisher Fig S1 original artifact desired for custody, though histogram functionally recovered in thesis. Contact authors/institution with explicit raw row/sample ID request; no invented file link.
2. **Independent original history**: 1925 map/8 listed aerial years, original georeferenced imagery+reprojection controls, GPR raw traces, physical sample-layer alignment, fitted isochrone membership and covariance. Need reconstruct independent dates under physically distinct units rather than treating 4.1m/yr dune-front speed as a direct cross-transect age gradient.
3. **Guérin FER1/FER3 independent ages**: exact original dating layer, source \`Guérin et al 2015b\`, measured true \`14C\` sample-level linkage and provenance; [Talamo 2020 La Ferrassie chronology](https://drive.google.com/file/d/1nr-YRaOk8whVmREwj9FaqheLT9OgKwtm/view) is NOT automatically a same-sample calibration. Guérin §6 has arbitrarily specified 38ka/44ka radiocarbon examples; do not label them measured. Complete R/BayLum package/seed-locked MCMC replay **HOLD** pending execution.
4. **Primary independent models**: better data allow a same-sample physically discriminating comparison between prior retained signal, lab component sensitivity/carryover, and independent depositional chronology/shared dose-rate errors. The source papers already explain all broad categories. A new MQR causal law remains unsupported.
5. **Heawood 1890**, **Regnault 1847** point-level graphical reconstruction and independent SNO raw likelihood are historical work streams; primary source copies now present but neither point trace nor SNO event likelihood has been reconstituted.

**P6 status:** \`INTAKE 32 FILES AUDITED\`; 28 moved; \`RAW ZIP ORIGINAL CRC/SHA PASS\`; \`COSTAS-S1 SAME-AUTHOR-HISTOGRAM FOUND\`; \`FER 49+49 SELECTED-KEY AUDIT PASS\`; \`SCENARIO COVARIANCE BOUNDED_ARITHMETIC PASS\` conditional on CI; \`PHYSICAL RAW COSTAS AND CAUSAL DISTINCTNESS HOLD\`. Existing version **MQR-4.111 OPEN**. This work is archival, sample-identity and **existing-theory** science, not a new physical experiment. No 4.112 opened.

## P7 — Source-typed rival tests: low-preheat persistence, publication arithmetic and non-pseudojoin witness (2026-10-10)

**Formal scientific stage MQR-4.111 remains OPEN** (P7 is an internal paragraph/stage within it). No new raw Costas aliquot stream, independently reconstructed georeferencing, or R/JAGS Bayesian posterior run. Three source-specific gains and two original-source reporting tensions were established without pooling nonidentical cohorts.

### A. Direct measured-protocol rival, original Costas 2012 published evidence

I. Costas et al., *Quaternary Geochronology* 10, pp. 16–23 (2012), DOI [10.1016/j.quageo.2012.03.007](https://doi.org/10.1016/j.quageo.2012.03.007), Table 2 and Discussion pp.20–22: for **the same source sites**, but not necessarily the same physical aliquots, published EBG equivalent doses are:

| sample | independently expected mGy ±1σ | earlier natural EBG mGy ±1σ | natural EBG after lower-preheat protocol mGy ±1σ | alternate – earlier mGy |
|---|---:|---:|---:|---:|
| GWD-80 | 50±5 | 55±5 | 56±2 | +1 |
| GWD-140 | 31±3 | 46±3 | 50±2 | +4 |
| GWD-245 | 1±1 | 23±5 | 18±2 | −5 |

Using just **individually reported 2× marginal SD intervals** (neither a correlated Gaussian significance test nor Bayesian inference), GWD-140 expected [25,37] vs new natural [46,54] are disjoint; GWD-245 expected [-1,3] vs new natural [14,22] are disjoint; GWD-80 expected [40,60] vs new natural [52,60] overlap. **Bounded discrimination:** the proposition that this protocol change alone resolves the entire discrepancy is contradicted by the original published data for 2 of 3 sites; it does **not** identify incomplete bleaching as unique cause, nor establish any new MQR law. Natural 23±5 vs one-week-cleared 8±1 mGy at GWD-245 remains source-site contrast across **different aliquots**, not same-aliquot pre/post observation. The physical paper itself already discusses thermal transfer, incomplete bleaching of medium/slow components, low signal-to-noise ratio and independently expected-age/dose rate model error. The lowered-preheat assay is not a direct controlled observation of depositional history.

### B. Published source internal numeric and chronology-language audits

Source Table 2 younger-seven (GWD-100,140,160,180,200,220,245) EBG ages minus independent expected ages = `35,22,62,49,40,28,32` years, which includes two differences >40 years, while abstract and Discussion describe *approximately 10–40 years* in the six of seven younger significantly over-aged sites. Mark `SOURCE_TEXT_TABLE_RANGE_UNRESOLVED`; do **not** substitute the prose interval into Table 2, fabricate raw numbers, or assert the geological study invalid. Similarly narrative calls source chronology “seven aerial photographs and one map”, then lists photograph years 1936, 1944, 1958, 1965, 1988, 1998, 2003, 2009 (eight distinct photograph dates) plus 1925 map and calls the fit eight isochrones. Mark `HISTORICAL_IMAGE_FIT_MEMBERSHIP_UNRESOLVED` pending the authors' georeferenced raw image map/GPR fitting inputs. Neither count mismatch by itself proves systematic error in independently expected ages.

### C. FER original bytes, documented processing choices and anti-pseudojoin audit

Original [Guérin et al. (2021) archive](https://drive.google.com/file/d/1BCujdWongKH2nA2RJjnBRao1dsJHGzJg/view) contains author `PracticalGuideToBayLum.Rmd`, FER1 and FER3 BIN bytes, each sample's `DiscPos.csv`, `rule.csv`, `DoseEnv.csv`, `DoseSource.csv`, and two example covariance CSVs. Full custody: ZIP SHA256 `25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228`, 681776 bytes, 229 entries CRC PASS. FER1 `bin.BIN`: **592704 bytes**, SHA256 `8328723705b6cdf3` prefix; FER3 `bin.BIN`: **526848 bytes**, SHA256 `510c0af01b4eaf6b` prefix. FER1 49 selected distinct `(position,grain)` keys across 11 positions; FER3 49 across 21 positions. These are published **selected** records, not every originally measured single grain. `rule.csv` for both defines channel-selection, background and removed final SAR cycles. Byte presence ≠ decoded decay curves ≠ original whole-experiment population.

Original authored `PracticalGuideToBayLum.Rmd`, **Example 5**, explicitly sets `C14age <- c(43400)`, `C14ageEr <- c(400)`, `SampleNames <- c("FER1", "C14", "FER3")`, and an IntCal20 curve. Neither packaged `data/` tree nor original `C14` example declaration supplies an independent linked carbon-dated specimen ID or raw calibrated-lab record. Source-paper §6 also uses illustrative, arbitrarily assigned comparison ages. Therefore the tutorial `43400±400` is *not* promoted to a verified independent historical witness for FER. Distinguish the available **real raw quartz readings** from the **unvalidated independent 14C anchoring**; BayLum posterior cannot be claimed from a moment/covariance check. The local compute environment has no Rscript/JAGS; no version-pinned JAGS inference was executed. [Documented standard Risø BIN import](https://r-lum.github.io/Luminescence/reference/read_BIN2R.html) handles versions 03–08; byte format marker is no replacement for parser record verification. The associated local source manifest `MQR_4111_P7_ORIGINAL_FER_MANIFEST_20261010.json` (conversation artifact) includes exact checksums and program line declarations.

### D. Executable source authority gate

[Source-typed Rust fixture](../experiments/mqr-4.111/source_rival_and_join_gate.rs) captures (a) original low-preheat rival evidence, (b) mathematical marginal interval logic, (c) Table 2 text-versus-arithmetic conflict, (d) reject cross-aliquot pseudo-pairing, (e) admit **only** same-study/same-site **published summary** reference contrast, and (f) reject a source-unlinked example 14C as an empirically verified anchor. These are **finite local evidence gates** not a proof that no experimental identification is possible, not a causal discovery.

**Actual CI evidence:** first [#38050496022 failed](https://github.com/WhoSia/MQR/actions/runs/38050496022) at non-test executable `-D warnings` on 7 unused source helpers while all 6 new unit tests passed; corrected by main-only [human WhoSia commit `aea192e`](https://github.com/WhoSia/MQR/commit/aea192e1f9a8a6dc7bfcce9a26f0af2f2b598e80) exercising both tests and runtime diagnostic. [Read-only CI #38050547118](https://github.com/WhoSia/MQR/actions/runs/38050547118): **SUCCESS**, 22 tests = 4 synthetic + 8 Costas source + 4 Guérin matrix + 6 P7; both test and main executables built with `-D warnings`. Exact executed CI commit `aea192e1f9a8a6dc7bfcce9a26f0af2f2b598e80`, **not** later README/ledger-only commits. No bot GitHub authorship claimed, no CI writes. Full local P7 source audit: conversation-generated artifact named `MQR_4111_P7_SOURCE_RIVAL_AND_JOIN_AUDIT_20261010.md` (not a public repository URL). is a conversation artifact, not a public GitHub URL.

**P7 judgment:** `PROTOCOL_CHANGE_ALONE_EXPLAINS_ALL = FAIL_BOUNDED`; `SAME_SITE_SUMMARY_TEST = PASS_BOUNDED`; `FER_SOURCE_BYTES_AND_SELECTED_KEYS = PASS_BOUNDED`; `COSTAS_INDIVIDUAL_ALIQUOT_PREPOST = HOLD`; `FER_INDEPENDENT_C14_ANCHOR = HOLD`; `CAUSE_SHARE_IDENTIFIABILITY = HOLD`; `NOVEL_MQR_PHYSICAL_LAW = HOLD`. Remain **4.111 OPEN**, no 4.112.

## P8 — Original FER BIN v4 record decoding, real independent-layer anchors and Costas fit-frame disambiguation (2026-10-10)

**Version:** 4.111 formally OPEN; 4.112 remains a proposal only. Local original-data audit file \`MQR_4111_P8_PRIMARY_DECODE_AND_HISTORY_LINK_AUDIT.md\` and reproducibility bundle \`MQR_4111_P8_FER_REAL_CURVES_ANALYSIS_PACKAGE.zip\` are preserved as current-chat artifacts, not fake public GitHub paths. **All empirical receipt numbers below derived from user-custodied original FER ZIP**; GitHub CI contains synthetic record boundary tests only.

### Same original FER1/FER3 measured curves — source-level actually decoded

- The original [Guérin et al. (2021) official supplement](https://drive.google.com/file/d/1BCujdWongKH2nA2RJjnBRao1dsJHGzJg/view), DOI [10.5194/gchron-3-229-2021](https://doi.org/10.5194/gchron-3-229-2021), SHA256 \`25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228\` (681776 bytes), was re-opened and parsed in a fresh read-only independent Python BIN-v4 decoder using documented [R-Lum read_BIN2R format](https://raw.githubusercontent.com/R-Lum/Luminescence/master/R/read_BIN2R.R); not just listed or hash checked.
- FER1 original \`bin.BIN\`: **592704 bytes, 882 complete version-4 records of 672 bytes each, 100 integer count channels/record, 88,200 genuine stored integer counts**, all \`LTYPE=1\` OSL; \`DTYPE 0/6/3\` counts 392/441/49. Raw \`DiscPos.csv\` 49 distinct selected (position,grain) keys **49/49** match decoded header pairs; **18 records per selected pair**. Full BIN hash \`8328723705b6cdf33d65ab9c946fb7a1461b51f0861b4bbc3bf531f2d4460786\`.
- FER3 original \`bin.BIN\`: **526848 bytes, 784 complete v4 records, same 672 bytes and 100 channels each, 78,400 count values**, \`LTYPE=1\`; \`DTYPE 0/6/3\` counts 343/392/49. **49/49** selected keys match, **16 records per pair**, hash \`510c0af01b4eaf6b8283aac857b093682e158f2a900da39db1dabdd3780e56d4\`. Both record parses reach the exact terminal byte with zero missing/trailing frames; metadata and count channels exported as CSV (reproducibility archive).
- Both author \`rule.csv\` files require 1-based signal channels **6–10** and background channels **76–95**. To inspect channel intensities only, \`S_net=sum(counts[6..10])-5/20*sum(counts[76..95])\`. Among first-run \`DTYPE=0\` curve (one per selected grain), descriptive median \`S_net\` = **288.25 raw count units** FER1 vs **107.5** FER3. NOT a cross-sample comparative age, dose, radiocarbon, physical clock time, \`Lx/Tx\` or Bayesian posterior. First-run intensity outliers exist and must not be trimmed by an invented rule. BIN v4 decoded \`TIMETICK\` may contain suspect numbers (e.g. FER1 \`5.922894843832526e-39\`), so original figures x-axis stays **channel index**, never guessed seconds.
- **Claim upgrade earned**: \`FER_ORIGINAL_CURVE_BYTES = PASS_BOUNDED\`, \`SELECTED_GRAIN_ID_49x2_RAW_JOIN = PASS_BOUNDED\`. Official \`Luminescence::read_BIN2R()\` versus Python/Rust channel-by-channel cross-implementation parity **HOLD** (no R installed), original complete screened population **HOLD**, **BayLum JAGS posterior NOT RUN**. Do not call a 49-grain selection the whole experimental cohort.

### Independent reference chronology/source ontology is now stronger, but NOT grain-paired

- **Primary published FER 3 layer-linked ^14C witness**: [Guérin et al. (2015) *J. Archaeol. Sci.* 58, 147–166](https://doi.org/10.1016/j.jas.2015.01.019) reports **three measured radiocarbon specimens** in Layer 5b with combined **44.4–47.3 ka cal BP outer limits across their 95% calibrated intervals** (full paper version indexed at \`https://files01.core.ac.uk/download/pdf/43249736.pdf\`; exact available bytes NOT checked). The later [Guérin et al. (2021)](https://gchron.copernicus.org/articles/3/229/2021/) explicitly states FER3 is Layer 5B, FER1 is superposed Layer7, and three **real** radiocarbon ages from the *same layer* compare favorably to FER3 BayLum. Therefore \`FER3_SAME_LAYER_INDEPENDENT_14C_PUBLISHED = PASS_BOUNDED\`; the earlier generic \`all independent 14C missing\` is now overly pessimistic. What remains unverified is **exact individual carbon-specimen accession / coordinates / lab age pairing to the 49 OSL grain measurements**, and independent recalibration execution. Crucially the *different* R Markdown **Example 5** value \`C14age <- c(43400)\` is a constructed tutorial control and **not** the recovered three actual lab dates.
- The already held [Talamo et al. (2020)](https://drive.google.com/file/d/1nr-YRaOk8whVmREwj9FaqheLT9OgKwtm/view) is an independent later 14C study, not a drop-in same-sample substitute. Direct stratigraphic joins must explicitly bind edition/date/layer boundary and specimen provenance.

### Costas eight-isocrone map labels: stronger proposed explanation

[Costas Vázquez 2013 dissertation](https://drive.google.com/file/d/1Y-jl7Thu3__5shXZ2zH0VLifvIOVqNPP/view), **PDF page 17 / original printed 14**, original *Figure 2.2B*: labels **1925,1936,1944,1958,1965,1988,1998,2003** appear on buried GPR isochrone overlays. The 2009 aerial photograph appears in Fig 2.2A as a current-state image **but no 2009 GPR buried isochrone label** is shown. This **plausibly reconciles** reported 'seven aerial images + one map' with eight fitted isochrones; seven photo dates through 2003 + 1925 historical map, with 2009 a baseline/current comparison. **Scope: visual-source hypothesis; numeric regression input membership and weighting/HISTORICAL_AGE_COVARIANCE remain HOLD**. Earlier 7-v-8 issue no longer warrants assuming the chronology paper is substantively wrong. Thesis chapter 3/4 mentions GIS georeferencing, GPR acquisition and a GWD-08 profile but not original radar trace bytes/GWD BIN data.
- Traced a potential **archive discovery, not a source match**: Schleswig-Holstein [LKN 1988 aerial photo centroid SHP archive](https://umweltportal.schleswig-holstein.de/trefferanzeige?docuuid=2048fb86-b449-4023-8780-9cb0c61df2c8). Photo centroid does not equal source georeferenced imagery and lacks verified connection to Costas sites; no substitute sample match was made. Need author/institution custodian for original aerial images + GIS georeference control, GPR trace survey profile/GWD-08 and source original OSL reader BIN/aliquot rows; DOI/PANGAEA/Zenodo raw same-GWD accession **still not located**.

### Reproducible finite validation and epistemic classification

Original-byte decoder output, sample-raw curves and a signed manifest were generated locally; [standalone Rust v4 reader](../experiments/mqr-4.111/fer_bin_v4_record_gate.rs) commits **NO original BIN bytes** and tests the format's boundaries with only synthetic constructed byte frames. Real cross-language FER decoded-byte parity remains untested until raw files run through that binary outside CI. [Read-only CI #38052022040 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38052022040), 28 tests = 4 synthetic prior-state + 8 Costas summary + 4 Guérin covariance + 6 P7 + 6 P8 raw-format *synthetic*. Executed CI at source \`feac155e1e7094d5efa692c80874491198636ae1\`; subsequent README/ledger commits are documentation-only.

**P8 verdict**: \`GENUINE_FER_ORIGINAL_CURVES_DECODED = PASS_BOUNDED\`; \`FER3_SAME_LAYER_ACTUAL_C14_REFERENCE = PASS_PUBLISHED_LAYER\`; \`COSTAS_8_HISTORIC_ISOCHRONE_LABELS = PASS_VISUAL\`; \`COSTAS_RAW_SAME_ALIQUOT_AND_ORIGINAL_AERIAL_GPR_FIT = HOLD\`; \`OFFICIAL_R_DECODER_PARITY / COMPLETE_SAR_LXTX_BAYLUM_MCMC = HOLD\`; \`UNIQUE_MQR_RETRODICTION_LAW = HOLD\`. **4.111 OPEN**.

### P8-generated **formal name proposal only** — user approval required to open 4.112

**MQR-4.112 — Source-Indexed Calibration Transport & the Boundary of Retrodictive Identifiability: Grain-Level Response Reconstruction, Independent Chronology Ancestry & Cross-Regime Rival Falsification**

Prospective question: under what **observable, source-indexed** conditions is a known-dose control transferable to naturally history-dependent source-state retrodiction, and when is a published independent reference genuinely independent of the measured cohort? Must compare ordinary SAR, incomplete bleaching, thermal transfer, BayLum/GUM shared covariance, sample selection and chronology-mapping error against a declared claim of new inferential restriction. Demands independently source-locked data, predeclared holdouts, genuine original grain/same-layer join permissions, exact rival likelihoods/calibration, negative controls and real-outcome checks. **If raw Costas GWD/GPR cannot be acquired, remain 4.111 OPEN or mark 4.112 conceptual-only; no new physical law may be promoted from case narrative or synthetic replay.**
