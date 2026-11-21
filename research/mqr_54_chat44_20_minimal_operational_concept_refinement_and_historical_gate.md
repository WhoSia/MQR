# MQR 5.4 · MQR 44 · Record 20 — The least conceptual refinement needed after a new operation

**2026-11-22 KST. Status: exact mathematical reconstruction and independent Python unittest PASS.** The following is classical deterministic-state partition refinement, closely related to automaton minimization, bisimulation/congruence and model checking; **no novel theorem** claimed. MQR 5.4 remains OPEN.

## 1. Research question more informative than 'bridge failed'
Previous R17–R18 showed a lossy bridge can cease to preserve newly available operations. This raises a stronger question: **when the old categories are inadequate, what is the minimum finer categorization that restores validity?** An intellectually generative scientific practice may invent a new observable or concept so that the bridge again accommodates the new operations. This is a constructive problem, not merely a failure label.

Let a finite world W have a coarse observation partition P0. For each available deterministic operation T:W→W require a refined partition P to be stable: whenever x and y belong to the same P-class, T(x) and T(y) must belong to the same P-class. In quotient terms this is the necessary and sufficient condition that an induced action G_T exists on the classes of P.

## 2. Explicit constructive algorithm
Given P_t and an action set I:
  signature_t(x) = (class_t(x), class_t(T_1(x)), ..., class_t(T_k(x))).
Define P_(t+1) as the partition into equal signatures. Repeat until no split occurs. Each step only refines, never merges, and strictly increases the number of classes if not at a fixed point. A finite W with n worlds therefore stabilizes after at most n-|P0| splitting rounds.

Minimality proof: suppose R is any action-stable partition refining P0. By induction R must refine every P_t. Base case follows from the premise. If R refines P_t and x,y are R-equivalent, then x,y are P_t-equivalent; stability of R makes T_i(x),T_i(y) R-equivalent and thus P_t-equivalent; so the computed signatures match. Hence every R-block lies within one P_(t+1)-block. The fixed-point partition is the **coarsest stable refinement** of P0. This proof is elementary and already well known in transition-system verification.

Source prior art: [Principles of Model Checking](https://is.ifmo.ru/books/_principles_of_model_checking.pdf), partition refinement algorithm; [CONCUR 2021 bisimulation partition refinement](https://drops.dagstuhl.de/opus/volltexte/2021/14408/pdf/LIPIcs-CONCUR-2021-31.pdf), distinct nondeterministic setting and complexity. Our case is deterministic and includes only finitely listed actions.

## 3. An illuminating two-round counterexample
Let W={0,1,2,3}, original observational classes P0={{0,1,2},{3}}. A new material operation T is:
   T(0)=1, T(1)=2, T(2)=3, T(3)=3.

At the first refinement, 2 is distinguished from 0 and 1 because its successor is in the formerly distinct {3} class:
   P1={{0,1},{2},{3}}.
At the next refinement, 1 is distinguished from 0 because T(1)=2 and T(0)=1 are now in different classes:
   P2={{0},{1},{2},{3}}.
A single intervention's consequences can induce a **cascade of newly necessary distinctions**. A material change need not yield just one added concept; because questions concern outcomes after operations, the resulting refinements can propagate backward into earlier categories.

Negative control: action S swapping 0 and 1 while fixing 2 and 3 preserves P0, so no refinement is needed. **More operations alone do not imply more categories**; their interaction with the current observational partition matters.

Exact code: [stable refinement](../language/real/experiments/mqr_stable_bridge_refinement_v54.py) and [six regression tests](../language/real/experiments/test_mqr_stable_bridge_refinement_v54.py). Local Python execution returned PASS: four-world refinement 2→3→4; harmless swap leaves 2 classes; all 27 three-state functions reach a stable refinement; all six independent tests passed.

## 4. What would make this a philosophical result rather than a renaming of known automata math?
A historical case must show *actual available actions, descriptions and data* in chronological order, and a conceptual refinement predicted under a previously frozen mapping rather than imposed by later notation.

- Historian must justify identifying state distinctions across pre/post practices without giving the earlier scientist unearned knowledge of future variables.
- Just because an analyst can calculate a partition does NOT imply that historical agents could measure each newly distinguished cell, invent the appropriate linguistic distinction, or execute the action successfully. An abstract stable refinement can be cognitively or physically inaccessible.
- The source-derived explanatory case must admit a rival where the apparent 'new concept' was already an available measurement category and merely received a new name.
- An independent empirical discriminator is required: did a new apparatus/discursive demonstration actually enable scientists to perform the newly specified tests?

This is a crisp connection between **material capability**, **conceptual classification**, and **inter-science translation**. Its exact math is old; its historical explanatory adequacy remains to be earned.

## 5. A formal negative prediction that can be falsified
For fixed finite W and pre-existing P0, any newly introduced deterministic operation that preserves every P0-class **does not require finer observational categories under this formal criterion**. Thus mere novelty of apparatus does not automatically constitute concept creation. If a dated historical case of a new apparatus is nevertheless claimed to exemplify conceptual revolution, the historian must show changes in permissible goals, representational inference, observation or action not encoded in this fixed-state toy model.

## 6. Decision
Mathematical proof PASS; exact code PASS; six tests PASS. Historical identification of Faraday's 1821 concepts as specific P0→P1→P2 classes: HOLD and likely too crude without additional research. This branch has now earned its constructive result and should backtrack to other 5.4 frontier areas rather than run indefinitely on finite toys.
