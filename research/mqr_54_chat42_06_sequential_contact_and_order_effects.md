# MQR 5.4 — MQR 42 · 기록 06: Sequential native observations, contact and back-action

**Date:** 2026-11-21; **chat** MQR 42, **research version** MQR 5.4. Source-aware continuation of [chat42 record05 action grammar](mqr_54_chat42_05_action_grammar_genesis_and_negative_controls.md) and [record04 contact stabilizers](mqr_54_chat42_04_contact_stabilizer_conditional_proposition.md). Full runnable local [module](../language/real/experiments/sequential_contact_v54.py) and [8 unit tests](../language/real/experiments/test_sequential_contact_v54.py). Local execution: 8/8 passed, with exhaustive n=3 **46,656** combinations of native 2-valued readout functions and arbitrary deterministic after-state maps independently checking the criterion below. This is a **synthetic finite-state theorem**, not a measured PTB/QPSW effect, experimental calibration, or quantum compatibility claim.

## 1. The new question: when is a pair of two sciences' reports one and the same preparation?

The earlier formal model assumed that both laboratories' readouts apply to one stable initial world state. That is an *extra world-contact assumption*. In sequential real measurement, one instrument can transform the sample before the next instrument observes it, even if each output is internally repeatable and timestamps/labels appear aligned.

Take a finite analyst-specified state set S, native readout maps o_A:S→O_A and o_B:S→O_B with **unrelated native alphabets** O_A,O_B. Let measurement-induced after-state maps m_A,m_B:S→S (arbitrary total deterministic transformations). Define AB and BA records reordered to the same coordinate convention (A,B):

\[
R_{AB}(s)=(o_A(s),o_B(m_A(s))),\quad
R_{BA}(s)=(o_A(m_B(s)),o_B(s)).
\]

**Exact criterion:** R_AB(s)=R_BA(s) if and only if
\[
 o_B(m_A(s))=o_B(s),\qquad o_A(m_B(s))=o_A(s).
\]
This statement follows by comparing the corresponding components in the ordered pairs. Notice it requires **cross-observable non-disturbance**, not m_A(s)=s, m_B(s)=s, or the equation m_A∘m_B=m_B∘m_A. The two native output vocabularies need **not** use translated words, matched physical units or the same symbol strings. They merely need an operationally justified shared initial preparation and recorded native output equality *within* each lab's alphabet.

**Important conceptual correction:** Observational order invariance is neither *physical state non-change*, nor *thermodynamic irreversibility*, nor *state-map commutativity*. Do not use these terms interchangeably. Ordinary deterministic classical state machines suffice for counterexamples.

## 2. Two decisive counterexamples

- **Commuting maps but order disagreement:** On four states, let m_A=m_B swap 0↔1 and 2↔3. They are the same map and commute. Define o_A=(a,a,b,b), o_B=(x,y,x,y). Then A's first action changes B's future output, so R_AB≠R_BA on several states despite physical commutativity.
- **Noncommuting maps but order agreement:** On five states, o_A=(a,a,a,b,b), o_B=(u,u,u,v,v). Let m_A swap 0↔1 and m_B swap 1↔2. These maps do **not** commute; both, however, leave their counterpart's coarse dark/bright-like readout invariant. Hence R_AB=R_BA for all five states even though the latent dynamics are order-sensitive.

The second example is a key negative limit: **cross-lab measurement concordance can hide physically distinct unobserved trajectories**. It is therefore weaker than an ontological claim about the world's latent transitions.

## 3. Positive bridge: complementary native distinctions without translating a word

On four analyst-assumed stable states use
\[
o_A=(a_0,a_1,a_0,a_1),\qquad
o_B=(b_0,b_0,b_1,b_1).
\]
Each science alone distinguishes just two observational classes; neither has a dictionary identifying the other science's output values. In a *non-disturbing, independently anchored common-preparation* comparison, the pair (o_A(s),o_B(s)) distinguishes all four latent states. The new operational partition is the intersection/meet of the two native partitions. This yields **additional discriminating capacity** without translating native outcome semantics; physical co-reference + jointly repeatable testing, rather than a priori unit conversion, is the bridge.

Yet the model has S={0,1,2,3} **supplied by the analyst**. Neither independent agent can recover this common identity or an objective world ontology from a spreadsheet without a real common-prepare/transport mechanism. The meet-of-partitions is standard mathematics, **not original novelty**.

## 4. Counterexample to naive fusion: more apparent distinctions can arise *from the experiment itself*

Take baseline o_A=o_B=(0,0,1,1) but with distinct native symbol alphabets. Baseline nondemolition joint reporting gives only classes {0,1} and {2,3}. Now let A's measurement action transform initial state 1→2 but leave other states fixed, and let B observe *after* A. Then the **sequential intervention AB** yields three classes {0},{1},{2,3}, apparently a better discriminator than simultaneous/undisturbed reporting.

This is a *real conditional new distinguishing experiment* in the toy world, **not a false observation**. The error would be to claim that the two output coordinates simultaneously describe two undisturbed properties of the same initial state, or to infer an ontology from their numerical compatibility. A new action can create a new causal test even when non-disturbing measurement compatibility fails. It belongs to [record05's action novelty vs readout novelty](mqr_54_chat42_05_action_grammar_genesis_and_negative_controls.md) and demands its own operational interpretation.

## 5. Exactly what the tests cover

- 8 targeted unit tests passed on local Python; one parameterized exhaustive test sweeps **8×8×27×27=46,656** readout/back-action quadruples for n=3, checking the derived iff condition against independently computed native-label comparisons.
- Both noncommuting-but-agreeing and commuting-but-disagreeing counterexamples are explicitly covered.
- One clean preparation does **not** certify all states: a checked subset can pass while global order identity fails.
- Nonbijective and state-changing measurement maps are allowed; invalid states and duplicate/empty native identity records fail closed.

The exhaustive cases establish the program's consistency with a finite **definition**, not experimental power, robustness to noise, or general proof about stochastic quantum instruments. A sampling model must include error and disturbance distributions, randomized order, common specimen identity, reset protocol, uncertainty and independent replication.

## 6. Primary held source and prior-art restraint

- [Feest & Steinle (2012), *Scientific Concepts and Investigative Practice*](https://drive.google.com/file/d/1WJyJHhYFi3R27QNfNOu5Jr4pmsdq5Ua9/view) introduction and Feest's exploratory-experiment chapter describe how operational criteria and theoretical concepts change together; they do not claim this particular finite order-condition lemma.
- [Clement (1988), *Learning via Model Construction and Criticism*](https://drive.google.com/file/d/1X_EeNfK7g5ablkwQweNpyU_Jhy0uIxTk/view) documents generation/evaluation interplay in explanatory analogies, not proof of physical co-reference.
- Established sequential measurement theory explicitly studies **disturbance, compatibility, and order**: [*Contextuality, memory cost and non-classicality for sequential measurements* (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6754713/) and [*Formalizing contextuality in sequential scenarios* (2025)](https://arxiv.org/abs/2509.14125). The quantum-operator equivalences under sharpness assumed in some of that literature **must not** be silently applied to the arbitrary deterministic classical state maps here. Our formal criterion is elementary conditional logic, **not a claim of first discovery or quantum-contextuality certification**.
- Actual [PTB 2025 processed graph exports](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view) and [Šíra 2023 QWTB source archive](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view) do **not** contain the physically paired randomized AB/BA sequence required to evaluate this model on those instruments.

## 7. Preregistered next discrimination, not retrospective storytelling

1. Define a physical preparation and externally verifiable same-token custody; keep preparation identity distinct from material token identity.
2. Specify two native readout alphabets and a feasible repeatable reset/initial-state control. Prespecify experimental AB and BA orders and record actual time, lag, dark and reference readings, condition-dependent drift.
3. Compare **native conditional distributions**, not merely aligned English terms. Re-randomize measurement order across independent preparations; include one run with a deliberately known state-preserving control and one plausible disturbance control.
4. If AB and BA disagree, distinguish instrument-induced sample change, clock/run pairing, label conversion, and sensor transfer effects; do not leap to quantum contextuality or incompatible reality.
5. If AB and BA agree, infer only order-compatible **tested observable reports under the tested conditions**. Unobserved state changes and distinct ontologies remain live. An actual L2 action-generation claim additionally requires execution of an intervention unavailable to the previous apparatus grammar, not just this equality check.

**Research-director classification:** HELD SOURCE-ANCHORED FORMAL NEGATIVE/CONDITIONAL POSITIVE / NEW PROGRAM TESTS PASS / REAL PHYSICAL PAIRING AND LANGUAGE BOOTSTRAP UNRESOLVED. The goal remains new executable questions under world resistance, not more relabeling.
