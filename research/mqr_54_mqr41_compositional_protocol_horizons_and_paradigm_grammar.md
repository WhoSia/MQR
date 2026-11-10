# MQR 5.4 / Chat MQR 41 — Compositional Experiments, Sensor Reachability, and Changing Inquiry Grammars

Date: 2026-11-11 KST. **CHAT NUMBER MQR 41 IS FIXED**; this is a research continuation inside MQR 5.4.

## 1. Origin and research question

MQR 40 closing directive: restore several ambitious origins (UV–Vis / logic circuits, possible alternative sciences, paradigm of paradigms, genesis of conceptual questions), alternate DFS and BFS, do not let narrow thermometry history or repetitive novelty-kill audits become the entire project.

This continuation attacks a precise methodological weakness in the previous MQR 41 finite-menu experiment: **greedy immediate information gain can discard an apparently useless experimental primitive that becomes indispensable in a multi-operation protocol**.

## 2. Exact negative control: myopic experiment choice fails

Let X={0,1}^3 and observe O(x,y,z)=x. The available physical-action grammar has adjacent bit swaps S_xy and S_yz, and F_x (toggle x). These are supplied as hypothetical, perfectly controlled operations, not inferred chemistry.

- O(s) resolves x only: 2 observational classes.
- O(S_yz(s))=x, so S_yz **alone** creates 0 new classes.
- O(S_xy(s))=y, so the single useful immediate action resolves (x,y), yielding 4 classes.
- However O(S_xy(S_yz(s)))=z. The composition of a myopically 'useless' operation followed by a useful one unlocks the third variable.
- With 0,1,2 action steps the observable classes become **2,4,8**, with respective finite Boolean observable-predicate algebras of cardinalities **4,16,256**.
- A greedy policy that only adds one standalone primitive action if it *immediately increases* equivalence-class count chooses S_xy and stops at **4** classes, while breadth-first compositional-word exploration up to length 2 reaches **8**.

The exact assertions were executed locally on all 8 truth-table states and recorded in code [compositional protocol search](https://github.com/WhoSia/MQR/blob/main/experiments/mqr-5.4/mqr41_compositional_protocol_search.py). A second program [sensor reachability horizon](https://github.com/WhoSia/MQR/blob/main/experiments/mqr-5.4/mqr41_sensor_reachability_horizon.py) enumerates n=2..6 and confirms the more general structural bound below.

### Graph-distance observation horizon

Let n independent binary coordinates be arranged on a path graph 0--1--...--n-1. A sensor reads only coordinate 0. Each allowed primitive swaps neighboring coordinates. At protocol depth at most h, the set of coordinates that can be routed to the sensor is **exactly** {0,...,min(n-1,h)}.

Reason: One adjacent swap moves a coordinate at most one graph edge; conversely moving coordinate j to position 0 takes j sequential swaps. Thus there are r=min(n,h+1) independently accessible bits. The finite observational equivalence relation has 2^r distinct classes (each observed r-bit assignment), and the algebra of unions of classes has 2^(2^r) elements. This is a trivial finite reachability lemma, NOT an original mathematical theorem, and not a claim that each abstract predicate describes a natural kind. For n=6 and h=4: 32 observable classes, but 2^32 possible Boolean unions; enumerating possible predicates is not an empirical scientific discovery.

This exposes a general rule of a **fixed operator grammar**: a useful scientific intervention may have zero one-step gain yet provide structural access at a longer horizon. Far from claiming novelty, this is related to classical observability, graph reachability, nonmyopic experimental design and automated planning.

## 3. Epistemic defects that survive the toy success

(A) **Coherent repeated state preparation**: Joint observation signatures from separate interventions assume repeated trials begin in the *same state*, which may be scientifically difficult or impossible for a unique specimen.
(B) **Given physical action grammar**: The scientist already has adjacent swaps and knows their operational meaning; the program does not *invent* a new instrument from arbitrary physics.
(C) **Given ontology**: x,y,z labels come from the modeler. Hidden coordinate access is not automatic ontological justification.
(D) **Observational nuisance**: Previous MQR41 session artifact experiment showed a confounded 'new' readout can raise both training and retest class counts while disagreeing for state-matched observations. This is distinct from the present protocol-depth effect and must not be conflated.
(E) **Finite horizon**: The first h steps may not suffice. Increasing horizon may require energy, resources, preparation cost, irreversible disturbance and supervision.
(F) **Science beyond formal learning**: Enlarging a language of experiments is not necessarily the same as changing the norms for what counts as an explanation, or why an investigator considers a question important.

## 4. Strong 2025–2026 prior-art collisions found by external search

1. **Léo Henry, Thomas Neele, Mohammad Reza Mousavi, Matteo Sammartino, CONCUR 2025**: [Compositional Active Learning of Synchronizing Systems Through Automated Alphabet Refinement](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CONCUR.2025.20), DOI **10.4230/LIPIcs.CONCUR.2025.20**. Already studies *automatic alphabet refinement*, including component alphabets and behavior-based counterexamples. Thus 'refine an operation alphabet while learning' is **not MQR novelty**. The paper is formally about synchronous systems, not unconditionally about all scientific paradigms.
2. **JiongHan Wang and WenChao Huang (2026)**: [An Automated Framework for Input Alphabet Construction in Stateful Protocol Implementation Learning](https://arxiv.org/abs/2606.23464), arXiv **2606.23464**, posted June 22, 2026. Already proposes constructing input alphabets from protocol structure and mutations. Do not claim that our model is first automatic protocol-alphabet invention. This paper is an arXiv research preprint, not verified peer-reviewed.
3. **Hasib et al. (2026)**: [Unifying AI-assisted scientific discovery around exploration, hypothesis generation, and testing](https://doi.org/10.1016/j.patter.2026.101660), *Patterns*, published October 9, 2026, DOI **10.1016/j.patter.2026.101660**. This review identifies weak connections between generating hypotheses and executable, revisable experimental tests. It is a recent competing macro-workflow account; literature-survey synthesis, NOT empirical proof that all AI discovery fails.
4. **Active learning of symbolic Mealy automata (2026)**: journal research on refining essential input characters; exact final publisher bibliographic details should be checked before ledger promotion. Scope: active learning, no inherent ontology discovery.
5. Earlier full text available locally in Drive: Angluin (1987), Steinle (1997 & 2016), Nersessian (2008), Haueis (2023), Schmidhuber (2013). Their originality ceilings remain valid.

**Custody:** Targeted Google Drive title searches for exact new 2025/2026 works returned no exact-title confirmed hits. This proves **NOT YET VERIFIED HELD**, not universal absence. Log them as *provisional acquisition radar*, not as newly certified missing primary sources. Publisher/abstract reading is not full-text deep reading.

## 5. Return to the big questions — DFS/BFS

- Q1 UV–Vis: a numerical reading at an ADC can encode the endpoint of an instrument, not all physically conceivable manipulations. A new optical excitation or chemical intervention may change the observable question grammar. **No claim** UV–Vis can 'swap hidden bits' literally.
- Q2 possible sciences: two independently discovered experimental grammars may appear incomparable when only atomic operations are compared, but become partially matchable after constructing composite operations. Conversely, a long matching history can conceal a difference in an as-yet-unexplored action.
- Q3 paradigm of paradigms: What institutional/material constraints license new operators and certify referents? A grammar-expansion count itself cannot decide scientific validity.
- Q4 genesis of scientific concepts: A primitive may become useful as part of an unforeseen arrangement; Faraday-style exploratory apparatus variation and Maxwell-style model modification serve historical conceptual comparators, not evidence that this toy model describes their discovery algorithm.
- Q5 mathematics and engineering: mathematical compositionality can become valuable because it affords new experimental routes and engineering interventions, but the availability of physical couplings and experimental resources filters the possible useful mathematics.
- Next DFS: seek a genuine interface with unknown or non-reproducible initial state, or a physical measurement model with specific noise and intervention costs; do not simply proliferate variants of Boolean toy models.
- Next BFS: compare the historical *social and material* norm changes (what problems/experiments are considered admissible) without reducing Kuhn or the entire history of science to an information-gain optimizer.

## 6. Repository/Harvest provenance

Existing MQR Harvest [LR-20260916-B](https://app.notion.com/p/3ddef561cf9281f1975bd07b6883ab8f) and [LR-20260916-C](https://app.notion.com/p/3ddef561cf9281ed8085cca1290f447f) already cover exploratory concept formation and the rule **operational split ≠ natural kind**. Reuse rather than clone. The MQR missing-source registry remains the canonical record. No raw Drive files acquired, renamed or moved in this unit.

**Gate:** exhaustive synthetic enumeration PASS; classical theorem novelty HOLD; cross-instrument observation HOLD; general scientific discovery claim HOLD. Direct WhoSia connector commits only, no GitHub-Actions[bot] contributor.
