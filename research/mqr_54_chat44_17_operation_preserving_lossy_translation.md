# MQR 5.4 · MQR 44 · Record 17 — Interventions that cannot descend through a lossy translation

**2026-11-22 KST; exact finite mathematical result locally executed PASS.** This is standard quotient-dynamics mathematics constructed for MQR, not a new theorem of category theory, causal inference or science. 5.4 OPEN.

## 1. The actual criterion for preserving an operation
Record15's lossy observational correspondence is f:A={0,1,2}->B={L,R}, f(0)=f(1)=L and f(2)=R. Consider any deterministic source operation T:A->A. Does there exist a well-defined target operation G:B->B such that:
```
f(T(a)) = G(f(a))  for EVERY a in A ?
```
This commutativity means that performing the operation then interpreting the result via f is indistinguishable, at target scope, from translating and then performing a target operation. It is the elementary criterion of a dynamics respecting an equivalence relation, **not** evidence of full historical theory translation.

**Necessary and sufficient condition:** whenever f(a)=f(a'), the transformed states must remain target-indistinguishable: f(T(a))=f(T(a')). Necessity follows by applying G to the equal target categories; sufficiency constructs G(b) by choosing any representative a of the fiber f^{-1}(b), well-defined exactly because results agree. This is valid because f is surjective onto the declared target B.

## 2. Exact full enumeration
There are 3^3=27 deterministic source transformations T. The fiber {0,1} must map either entirely to {0,1} (2²=4 choices) or entirely to {2} (1 choice): 5 possibilities. The singleton source fiber {2} can map to any of the 3 source states. Therefore **15** T admit a target G, and **12** do not.

Controls:
- swap 0 and 1, fix 2: **compatible**; G=identity on B. It changes source labels but preserves all coarse outcomes.
- swap 1 and 2, fix 0: **incompatible**. The two original states 0 and 1 both have target label L, but after the operation one remains L and one becomes R; there is no single G(L) capable of matching both.
- map all source states to 2: **compatible** with target G(L)=G(R)=R.

Exact executed implementation `language/real/experiments/mqr_dynamic_quotient_bridge_v54.py`, result `PASS: 27 source actions; 15 quotient-compatible, 12 incompatible`. This is stronger than the prior observational coarsening analysis because it explicitly identifies which interventions break the bridge.

## 3. New research principle: contract-relative adequacy, not binary commensurability
A lossy scientific translation may perfectly preserve passive target observations while failing for specific physically accessible interventions. Its authority must therefore carry an **operation-specific domain**:
```
BRIDGE(f; permitted_actions A*) is ADEQUATE
iff for every T in A* there exists a declared G_T
such that f∘T = G_T∘f on the specified states.
```
If A* only contains compatible operations, the bridge is sufficient for those questions even though noninvertible. If A* includes incompatible actions, the bridge fails for that action. The availability of the action is a historical/material question, not established by abstract mathematical possibility.

A practice may enlarge its repertoire I_t, making a previously adequate bridge inadequate without changing the observed passive output vocabulary at all. Conversely a new target sensor can refine B enough to recover adequate cross-operation comparison. Thus question-genesis and translation can interact dynamically; this is MQR's *integrative research hypothesis*, not a discovered physical law.

## 4. Two hard caveats
- A mathematical source T may fail to represent any physically permissible intervention. Never infer scientific noncommensurability simply by enumerating arbitrary functions on a state set. Real chemistry/physics has conservation, symmetries, controllability and instrument constraints.
- An instrument's coarse categories may be probabilistic, context-conditioned or operationally reconstructed, not a deterministic function of a small state set. Extending the condition to stochastic kernels requires a different commutation equation and identifiability gates.

## 5. Historical test against Faraday/Ampère
Faraday 12 Sep 1821 explicitly distinguishes common rotation observations from theoretical claims about hidden electric currents within a magnet. Hachette 12 Dec 1821 attests Paris experimental repetition; Faraday's letter editorially dated 2 Feb 1822 disputes what a rotation test is competent to decide. These are strong witnesses of **experimentally shared but inferentially contested** access, not a demonstrated failure of the formal f∘T=G∘f criterion. Applying our finite criterion requires reconstructing actual co-observables, operations and predictions from dated Faraday and Ampère sources and specifying bridge assumptions before judging.

## 6. Next adversarial probe
Formalize a minimal stochastic-kernel analogue and a context-dependent bridge; compare against Blackwell statistical sufficiency, Markov lumpability and category-theoretic functorial preservation. Do not collapse those established concepts into a claimed novel MQR theorem. Investigate whether any historical case displays an intervention-induced *loss of formerly adequate cross-theory translation* with genuinely independently documented operational change.

**Status:** standard theorem rederived and 27/27 transformations exhaustively categorized. Historical generalization HOLD. MQR 5.4 OPEN.
