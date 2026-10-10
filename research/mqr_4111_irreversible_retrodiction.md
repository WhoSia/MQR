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
