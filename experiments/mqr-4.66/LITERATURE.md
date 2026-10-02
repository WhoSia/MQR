# MQR-4.66 — Literature and Prior-Art Collision Map

Status: **POST-PRESEAL / PRE-EXECUTABLE-REVEAL / NOVELTY-KILL / EVIDENCE-LAYERED**

Canonical PRESEAL:
`54b24be19c7bd9b4e36bd07dfa178066830c6bfc`

The entries below use the 4.66 evidence ledger:
**OBSERVED / PROVED / ENUMERATED / INFERRED / OPEN**.

No source below is allowed to mutate the PRESEAL's preservation obligations or verdict definitions.

## 1. MDP bisimulation and minimal models

### Givan, Dean & Greig (2003)
*Equivalence Notions and Model Minimization in Markov Decision Processes*
Artificial Intelligence 147(1–2):163–223.
DOI: `10.1016/S0004-3702(02)00376-4`.

Drive canonical source:
`1nb1_v9pKOvJMtkwmYfXtowzfYUo3fmg4`.

**OBSERVED.**
The paper explicitly frames MDP reduction as grouping equivalent states into a reduced MDP, makes the chosen equivalence notion fundamental, seeks the smallest reduced MDP for the chosen notion, and develops a stochastic bisimulation-based equivalence for which an optimal policy on the reduced model induces an optimal policy on the original model.

**OBSERVED.**
The paper emphasizes that compact/factored representation does not guarantee equally compact solution structure; states grouped by the representation may still need to be separated by solution-relevant behavior.

**Novelty kill.**
4.66 does not invent:
- exact state aggregation by bisimulation;
- partition refinement toward a minimal model under a fixed equivalence notion;
- policy-preserving MDP quotienting;
- the distinction between representational grouping and solution-relevant grouping.

**INFERRED pressure on MQR.**
If 4.66's preservation relation is merely ordinary reward/transition bisimulation with renamed labels, there is no MQR-specific formal novelty.

## 2. State-abstraction hierarchies and preservation targets

### Li, Walsh & Littman (2006)
*Towards a Unified Theory of State Abstraction for MDPs*.

Drive canonical source:
`1P1HjH1S47t8d3Vq8Npd09eb3hxhYmfSC`.

**OBSERVED.**
The paper explicitly asks what information is lost under abstraction, when optimal policy is preserved, and how multiple abstraction schemes relate. It studies five abstraction schemes and distinguishes stricter model-preserving abstractions from weaker value/policy-related abstractions.

**OBSERVED.**
The paper notes negative behavior when abstraction is improperly constrained and treats preservation guarantees as dependent on the abstraction scheme.

**Novelty kill.**
4.66 does not invent:
- a hierarchy of abstractions with different guarantees;
- preservation-target-dependent state compression;
- the question “what information is lost?” as such;
- policy preservation as distinct from full model preservation.

**INFERRED pressure on MQR.**
4.66 must specify why preserving authority/reopening/provenance is a scientifically different target relation, not merely another policy/value abstraction chosen ad hoc.

## 3. Predictive state representations

### Littman, Sutton & Singh (2001)
*Predictive Representations of State*.

Drive canonical source:
`1WmtgdpM0e-yuHeacvtSFk9y6XN3-jNjH`.

**OBSERVED.**
The paper represents dynamical state using predictions of action-conditional future observation sequences (“tests”). It explicitly states that a sufficient set of tests can determine predictions for all tests and presents predictive state representations as recursively updateable alternatives to latent-state POMDP representations.

**OBSERVED.**
The paper states that any system has a linear predictive-state representation with no more predictions than the number of states in its minimal POMDP model.

**Novelty kill.**
4.66 does not invent:
- future-behavior-based state representations;
- replacing history by a sufficient predictive state;
- recursive predictive-state updating;
- using future tests to decide which history distinctions matter.

**INFERRED pressure on MQR.**
A “future world-contact language” quotient is close in spirit to PSR unless the preserved outputs and admissible interventions are materially different and explicitly justified.

## 4. Bisimulation metrics and approximate compression

### Ferns, Panangaden & Precup (2004)
*Metrics for Finite Markov Decision Processes*.

Drive canonical source:
`1Hu3BKEsHRBXgxVNo0pIqruzNnQmYUKOf`.

**OBSERVED.**
The paper starts from exact bisimulation and develops quantitative semimetrics intended to measure how similar states are, including links between metric distance and optimal value differences.

**OBSERVED.**
The motivation explicitly includes state compression when exact equality is too brittle.

**Novelty kill.**
4.66 does not invent:
- approximate state equivalence;
- a compression–accuracy tradeoff;
- bisimulation-distance-guided aggregation.

**INFERRED pressure on MQR.**
If exact quotienting is too strict, an approximate MQR quotient would need an explicit error semantics for lost authority/reachability—not merely a heuristic compression ratio.

## 5. Computational mechanics / causal states

### Shalizi & Crutchfield (2001)
*Computational Mechanics: Pattern and Prediction, Structure and Simplicity*.

Drive canonical source:
`1T0T2lXQs5VuD9ytU86O6KnV6B_JIlZ-k`.

**OBSERVED.**
The paper defines causal states from equivalence classes of histories/pasts with the same predictive distribution over futures and presents the resulting representation as maximally predictive, sufficient, minimal among prescient rivals, and unique in the paper's stated sense.

**OBSERVED.**
The paper's own section structure includes explicit results titled “Causal States Are Maximally Prescient”, “Causal States Are Sufficient Statistics”, “Causal States Are Minimal”, and “Causal States Are Unique”.

**Novelty kill.**
4.66 does not invent:
- grouping histories by future predictive equivalence;
- a minimal sufficient predictive state derived from histories;
- uniqueness/minimality claims under a fixed predictive target.

**Strongest prior-art collision.**
This source is a direct warning against describing a 4.66 coarsest future-behavior quotient as a new general concept.

## 6. Automata-minimization / continuation equivalence

### Myhill–Nerode family

**OBSERVED from standard theorem structure / external verification.**
Deterministic automaton states can be quotiented by equality of future acceptance behavior; the induced right-congruence supports a minimal deterministic automaton under the declared language semantics.

**Novelty kill.**
4.66 does not invent:
- continuation-based distinguishability;
- minimal distinguishing continuations;
- stable quotienting under future event strings;
- partition refinement as an algorithmic pattern.

**OPEN bibliographic note.**
No single historical source has yet been ingested into Drive for this item in the 4.66 pass. It remains a theorem-family comparator, not a harvested citation packet.

## 7. What may still be distinct

**INFERRED, not yet earned.**

The surviving 4.66 target is not “minimal state” generically. It is the possibility that a scientific-methodological constitution requires preserving a richer typed output than ordinary reward/value/prediction:

- current action authority;
- rival-separation reachability;
- ancestry/common-mode distinctions;
- reopening activation/release;
- exterior-route availability;
- schema-reopening obligations when novel rival objects are admitted.

A candidate MQR contribution would be:

> an explicit preservation contract for **scientific authority under open-frontier schema revision**, plus executable evidence that weaker abstractions alias histories that are equivalent for a narrower planner objective but not equivalent for the scientific-authority contract.

This is **OPEN** until the Court produces prospective witnesses and literature comparison survives.

## 8. Hard novelty-kill summary

MQR-4.66 may not claim novelty for:
- bisimulation;
- MDP model minimization;
- policy/value-preserving state abstraction;
- predictive state representations;
- causal-state minimality;
- continuation-based automata equivalence;
- partition refinement;
- approximate bisimulation metrics.

## 9. Surviving question after collision

The narrowed question is:

> If the preservation target is expanded from ordinary reward/value/prediction to a typed scientific-authority contract containing reopening, provenance and open-frontier schema obligations, what is the coarsest finite quotient on a frozen scientific-history system, and which apparently reasonable weaker abstractions become unsound?

This is a characterization question, not yet a novelty claim.

## 10. Publication discipline

**OPEN.**
The 4.66 line becomes paper-relevant only if at least one of the following survives:
1. a naturalistic scientific case where a conventional compact state aliases authority-relevant histories;
2. a formal difference between the MQR preservation contract and established abstraction targets that is not terminological;
3. a dynamic schema-reopening result not already subsumed by known adaptive abstraction / predictive-state machinery.

Until then, publication language remains provisional.
