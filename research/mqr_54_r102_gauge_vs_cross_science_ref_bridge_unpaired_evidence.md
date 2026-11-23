# MQR 5.4 · R102 — Two distinct nonidentifiabilities and the first physical bridge: gauge vs unpaired science readouts

**2026-11-23 KST.** The founding Q2/Q5/Q6/Q7 are independent of Faraday/Maxwell historical novelty claims. This is a *bounded synthetic thought experiment plus sourced methodology*, not a new physical discovery or universal solution to alien sciences.

## (A) Maxwell source-native content and what was checked

Original Maxwell **On Faraday's Lines of Force** read in [Niven collected *Scientific Papers* Vol I pp.204–207](https://strangebeautiful.com/other-texts/maxwell-scientific-papers-vol-1.pdf) (section *Summary of the Theory of the Electro-tonic State*, Laws I and VI). It explicitly specifies that a closed contour's integrated electro-tonic intensity corresponds to magnetic induction through the surface, and that changing electro-tonic intensity induces electromotive force. His earlier printed component formula at p.204/205 contains a unit-dependent factor **1/(4π)** and a time derivative. His wording calls the construction a **temporary instrument of research without a true physical account**; in particular do NOT read modern gauge equations as if Maxwell wrote them in SI vector calculus. Full PDF text read and web screenshot was attempted but **cache miss**; individual math glyphs and all printed original equations are NOT pixel-verified. [2014 *Physics Today* historical paper](https://physicstoday.aip.org/features/the-conceptual-origins-of-maxwells-equations-and-gauge-theory) distinguishes Thomson's earlier vector-potential mathematics and Maxwell's interpretive use. **Any source-native formula sign/equation-layout parity remains a HOLD.**

Modern illustration (separately labelled, flat simply-connected plane, smooth scalar gauge transform):
A1(x,y)=(0,Bx), A2(x,y)=(-By,0), χ(x,y)=-Bxy.
curl A1 = curl A2 = B, A2 = A1 + grad χ. For any grid path from p to q,
∫path A2·dl - ∫path A1·dl = χ(q) - χ(p).
On a closed path this difference vanishes. The circulation gives B times *signed area*, with orientation fixed. The **values of an open path integral** are not gauge invariant if the endpoint phase/reference is not fixed. **Non-identifiability of a representation does not establish multiplicity of independent physical magnetic fields.** For multiply connected domains a curl-free but not globally exact difference can have distinct holonomy: the simply connected hypothesis matters. The toy does not treat gauge-variant quantities as free-standing physically measured open-path quantities.

[Exact Fraction code R100](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r100_gauge_representation_exact.py). Independently implemented a finite 3x3 walk enumeration in a separate local Python instance: **2,364** valid walks of 1–5 steps, **168** closed, **1,384** with unequal A1/A2 open integrals; tested every path telescoping gradient and each loop signed area; output PASS for this independently reimplemented mathematical model. It is **not** source-byte-identical execution of the committed Git Python file, nor repository-wide CI, and no archival equation page pixels were verified.

## (B) How two successful sciences can fail to identify their shared referents

Let an unknown common 0/1 process s be sampled four times, two 0 and two 1. Practice A reports s. Practice B reports s XOR z, with unobserved binary relabeling z. With only A's marginal (1/2,1/2) and B's marginal (1/2,1/2), both z=0 and z=1 are observationally **indistinguishable even with arbitrarily many separately sampled observations under the stipulated symmetry**. If genuine same-event pairing is somehow established and B's sensor response stable/non-disturbing, agreement equals 1 at z=0 and 0 at z=1 for this noiseless toy. But shared physical-event IDs or interventions are an **outcome to engineer or negotiate**, not a pre-given universal dictionary.

A deliberately incorrect 4-record linkage gives 4!=24 indexed permutations. In exact enumeration of a=(0,0,1,1) and b=(0,0,1,1), agreement of a wrongly coupled with permuted b is 0 for 4 permutations, 1/2 for 16, and 1 for 4; mean 1/2. **An apparently perfect or perfectly opposite empirical pairing can be forged by record linkage alone without any altered marginal data.** Unlike gauge redundancy (two vector potentials representing the *same* B field in one known physical model), this is *cross-practice mapping underidentification* where physical sample correspondence was absent. The situations must NOT be equated.

[Exact Fraction and 24-permutation code R101](https://github.com/WhoSia/MQR/blob/main/language/real/experiments/mqr54_r101_unpaired_cross_language_mapping.py). Separate local Python enumeration confirmed exact histogram {0:4,1/2:16,1:4}, expectation 1/2. Again, not committed-byte execution/CI.

## (C) Existing strong rivals are not optional

- [**VIM JCGM 200:2012 §2.41**](https://jcgm.bipm.org/vim/en/2.41.html): **metrological traceability is a property of a measurement result**, related to a reference by a documented **unbroken** calibration chain with uncertainty. Common signal display or cross-lab agreement without traceability does not establish equal referents or adequate uncertainty. The VIM explicitly cautions that even traceability does not guarantee uncertainty fit for purpose or freedom from error.
- [**Galison, *Trading Zones*, in *Image and Logic* (1997)**](https://projects.iq.harvard.edu/files/andrewhsmith/files/galison_tradingzonesabridged.pdf), plus [SEP *Unity of Science*](https://plato.stanford.edu/entries/scientific-unity/): local coordination and evolving hybrid practices permit cooperation without universal pre-given reduction or total language translation. This substantive philosophical insight is well-established prior art, so MQR cannot claim to have originated the trading-zone strategy.
- [**Statistical matching partial identification**](https://pmc.ncbi.nlm.nih.gov/articles/PMC5423529/): formal methods for different variables that are never jointly observed already establish non-identifiability of many joint distributions. Our 4-bit case is a simple pedagogical construction, **not a new result**.
- [**NIST metrological traceability guidance**](https://www.nist.gov/metrology/metrological-traceability): documentation, uncertainty and fit of measured value, **not instrument-label alone**. A shared apparatus does not grant reference validity unconditionally.

## (D) Falsifiable MQR Q2 protocol: what is still missing?

The minimal viable **future** bridge study should register: physical stable target or jointly enacted intervention; true contemporaneous same-object/event IDs; each group's independent operational labels (not a gifted translation dictionary); measurable sensor disturbance, preparation changes and data selection; calibration traceability and independent blind negative controls; explicit intervention conditions under which the candidate learned bridge fails. Missing any of these cannot justify uniqueness of ontology. If the instrument is destructive, transfer only through a separately justified matched-preparation design, **never call two different aliquots repeated measurement of one identical physical object.**

Test cases before recruitment:
1. **Label-only control:** relabel both sensor outcomes, no real intervention added. Predict unchanged empirical distinguishability.
2. **Incorrect pairing control:** shuffle event IDs and show a proposed semantic mapping should lose its uniquely identifiable status.
3. **Instrument disturbance control:** B measurement alters s; now even correct matched ID may not preserve the same physical state, so the simple equivalence test fails.
4. **New reference intervention:** jointly prepared event with independent physical traceability; only here expect a new local reference bridge under stated assumptions.

This **does not** solve how entirely alien traditions construct the first shared operation from scratch. The protocol intentionally leaves that central problem open and explicitly lists it as the strongest blocker.

## LIRA declared judgments (not probabilities)

- Maxwell source **printed text supports contour/induction/instrumentality**: E=.90, C=.96, L=.90; **exact 1856 equation-image parity** remains C=.30 (pending screenshot), L=.95.
- Rational gauge example establishes **closed-loop invariance under exact gradient on stipulated domain**: E=.92, C=.99 for the specified math, G=.12 for the general Q2, L=.88.
- Four-bit unpaired counterexample establishes **non-identification with marginals alone**: E=.90, C=.99 for its math, G=.10 for the alien science problem, L=.94.
- 'True same-event pairing plus stable readout can learn a *local* binary mapping' has C=.92 under toy premises, but the actual world-facing cross-practice implementation is **HOLD**.
- 'Trading zones + traceability universally guarantee cross-ontology equivalence' is **REJECTED** (C=.07), because traceability and coordination are scoped, not metaphysical uniqueness conditions.

**Status** MQR5.4 OPEN; synthetic-only verified in independent reconstruction; no new independent physical data; Faraday and Bell historical dossiers remain protected; Q2 not closed.
