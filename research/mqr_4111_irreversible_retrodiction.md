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

For each atom, add an operational reset readout R=0 after Y is acquired. Both models then have identical (Y,R) cell counts (4,0,0,4) under the fixed table order (Y=0,R=0),(Y=0,R=1),(Y=1,R=0),(Y=1,R=1); the original Q distributions remain different. An operational response reset can be a many-to-one map and has no general inverse. This is a basic identification result, not an original MQR theorem or a description of any specific OSL reset instrument.

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
