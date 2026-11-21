# MQR 5.4 · MQR 44 · Record 09 — Inquiry may require inventing its own observables

**2026-11-22 KST.** SYNTHETIC FINITE CONSTRUCTION + SOURCE-GROUNDED COMPARATIVE THEORY. MQR 5.4 OPEN. No claim of new information-theoretic theorem or new physics.

## 1. Deep primary/secondary original-book re-reading and provenance
- **Steinle (2016)**, *Exploratory Experiments: Ampère, Faraday, and the Origins of Electrodynamics*, University of Pittsburgh Press English translation by Alex Levine of the **2005 German work**. Held and freshly fetched Drive PDF `1-kviuErWDAEJMRlcbACBX7FbLR55hV1G` (extracted text ~1.23 million characters). The table of contents explicitly distinguishes Chapter 3 Ampère's early studies, Chapter 6 Faraday's initial **electromagnetic rotation** investigations, and later conceptual and experimental reconstruction. The introduction explicitly addresses how exploratory experimental activity and provisional concepts mutually stabilize and destabilize, and that short periods of branching can fix long-term research trajectories. **Do not conflate the 1821 electromagnetic rotation episode with Faraday's later 1852 papers on physical lines of force**. Historical argument is Steinle's interpretation of archival episodes, not a direct 1821 original notebook transcription.
- **Nersessian (2008)**, *Creating Scientific Concepts*, held original book, Drive PDF `168Yv277pBhy--iQrNjhMWbYcFhVx3_KR` freshly fetched (~645k characters extracted). The preface and contents explicitly describe model-based reasoning, analogy, thought experiments and constructed hybrid representations, with historical attention to Faraday–Einstein field concepts. Direct prior art to conceptual generativity and bridging representations.
- **Steinle (1997)** exploratory experiment journal article, held `1rl444ab9HV-Q285EwbPq1QBR2z5g3JcR`; and **Secord (2004)** 'Knowledge in Transit' held `1Y0N6ke4RCf6iDw7pl9S34jgwcI9VjBYt`, read in preceding research unit. Theoretical originality cannot rest on asserting that explorations produce concepts: these scholars already made the argument.

## 2. New conceptual correction: a question need not be currently executable to motivate its own apparatus
Earlier MQR expression `P_t=(L_t,Q_t,I_t,G_t,S_t,E_t)` is a *snapshot*. It omits actions that transform the future set I_(t+1) of admissible instruments and therefore change the questions that can be meaningfully tested. A local change in beliefs on a fixed finite state space is not enough.

One candidate representation is a **generative inquiry transition system**
```
state_t = (model alternatives, instruments, admissible actions, evidence, goals)
action_t in admissible_actions(state_t)
(observation_t, state_(t+1)) = transition(state_t, action_t)
```
An action can (a) produce data, (b) modify the observation interface and action repertoire, or (c) revise the problem's vocabulary and validation standards. A mathematical machine specifying all future transitions is an **external analyst's reconstruction**, not evidence that the historical agent already possessed the future concepts.

## 3. Exactly solvable two-step construction
Four equiprobable worlds W={(0,0),(0,1),(1,0),(1,1)}, hidden bits X,Y independent uniform.
Initial admissible operations:
- inspect_x: immediately outputs X (1 bit).
- build: yields no new data (0 bit) but installs a future instrument.
In the second slot, only after build, measure_xy becomes available and reports both (X,Y) (2 bits). If inspect_x is done first, the second slot offers inspect_x or build only; the novel measurement is unavailable until after the two-slot horizon.

Thus a **greedy immediate information policy** selects inspect_x (1>0) and learns at most 1 bit over two slots. A **capability-building policy** chooses build then measure_xy and resolves all four worlds (2 bits). The gain is not metaphysical; it comes from explicitly modeled costs, instrument affordances and a two-step horizon.

The exact enumeration executable `language/real/experiments/mqr_question_invention_capabilities_v54.py` was run locally and returned:
`PASS: immediate-info greedy=1 bit, capability-first plan=2 bits`.
This construction is a familiar idea related to sequential optimal experiment design, value of information and technology investment. It is **not** a novel mathematical result and does NOT prove investment should universally win. If building costs exceed the available horizon, or the new device does not discriminate the desired questions, the advantage reverses.

## 4. Why this is philosophically more than immediate posterior gain
The physical analog is not merely 'new sensor measures another already known bit'. Actual emerging science may not have `Y` as a named variable in its pre-experimental vocabulary. Then a retrospective analyst may model Y while the researcher discovers a novel response class through systematic parameter variation. To move from the finite analogy to an authentic historical thesis we must source:
1. the investigator's *then-current* classified observables and questions;
2. the exploratory operations actually attempted and the practical instrument constraints;
3. a dated anomaly or new stable distinction recorded before retrospective theoretical cleanup;
4. evidence that the new distinction changed what experiments were then conceived and executed;
5. a serious rival explanation of mere re-labeling or instrument refinement.

The actual 1821 Ampère/Faraday papers/notebooks require edition-verified direct historical reading, not an assertion from Steinle's 2016 retrospective text. MQR 5.4's earliest founder precursor from 2026-02-05 explicitly asks about structural generation rather than only accurate description; this problem directly answers its ambition.

## 5. A severe adversarial objection
All of the two-step construction might be described by ordinary POMDP / Bayes-adaptive planning, because an omniscient external model pre-encodes every future device and response. A theory of 'concept creation' that does not explain where this state/action ontology comes from is just a change of optimization horizon.

Therefore the first genuine philosophical gap is **model-space revision with history-grounded constraints**, not a renamed Bellman equation. We must prevent the analyst from seeding an inaccessible future concept and later claiming the scientific agent invented it. Nersessian and Steinle are essential to investigate how material models, analogies, exploratory manipulations and social learning produce the subsequent representation.

## 6. Boundary and next tests
- PASS: 2-stage information value contrast in synthetic finite system.
- PASS: original-book introduction and chapter map checks, correct 2005-vs-2016 edition label.
- HOLD: actual historical chronological causal attribution of Faraday's field and apparatus inventions.
- HOLD: model of genuinely unanticipatable conceptual primitives, if 'unanticipatable' cannot be operationally specified without contradiction.
- Next: stage-constrained negative controls, genuine two-instrument observational access, historical timeline; then tie to epistemic communication where method circulation changes another agent's available action repertoire.

**Research judgment:** Treat constructing a new observable and discovering a new scientific question as distinct but interacting operations. Novel source-based synthesis is worthwhile under doctrine even when no unprecedented theorem emerges.
