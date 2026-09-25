# MQR-4.36 — Finite Residue, Decision Sufficiency, and Open-World Boundary

Status: THEORY RECEIPT AFTER FRESH WORLD CONTACT

## 1. The question

Can MQR prove a finite bound on residue for an explicitly declared intervention/probe class without pretending to close the world?

MQR-4.36 answers:

```text
YES for internal, declared, decision-relative residue.
NO for unrestricted open-world residue from that fact alone.
```

## 2. Three quantifiers that must not be exchanged

Let:
- W be the target-world family;
- P be a preregistered finite probe algebra;
- D be a preregistered decision family;
- T be the executed subset of P;
- Relevant_D(p) indicate whether probe p can affect D.

### Internal execution residue

```text
R_int(P,D,T) = { p in P : Relevant_D(p) and p notin T }
```

If P is finite and completely enumerated, Relevant_D is explicit, and every relevant p has a typed execution/discharge receipt, then:

```text
R_int(P,D,T) = empty
```

is a legitimate finite claim.

### Representational residue

Even if R_int is empty, the representation q may identify worlds that produce different probe outcomes:

```text
q(x)=q(y), E_P(x)!=E_P(y)
```

MQR-4.36 supplies exactly such a fresh naturalistic NU3 collision.

Therefore complete execution of P does not imply that q is sufficient even for P.

### Open-world residue

Define conceptually:

```text
R_open = possible world-separating interventions/observables not captured by the declared P and current representation.
```

MQR does not require this set to be enumerable or even expressible in the current language.

A proof that R_int=empty does not imply R_open=empty.

## 3. Fresh 4.36 witness

The preregistered F-R1 NU3 fiber contains both:

```text
JSCHEMA-001 -> E1_QUOTIENT_ONLY
OASV-001    -> E0_FULL
```

with identical NU3 receipt.

Meanwhile:

```text
EXECUTED_ATOMIC_ROWS=132
UNRESOLVED_ATOMIC_ROWS=0
INTERNAL_RESIDUE_WITHIN_DECLARED_PROBE_CLASS=ZERO
```

Thus internal closure and representational insufficiency coexist in the same experiment.

This is an exact witness against the inference:

```text
EXHAUSTIVE_DECLARED_TESTING
therefore
REPRESENTATION_SUFFICIENT
```

and against the stronger inference:

```text
EXHAUSTIVE_DECLARED_TESTING
therefore
WORLD_CLOSED
```

## 4. Decision-relative sufficiency

Let a decision family D induce action map a_D over empirical reach.

Representation q is D,P-sufficient on admitted corpus W iff:

```text
q(x)=q(y)
implies
a_D(E_P(x)) = a_D(E_P(y))
```

for all admitted x,y.

MQR-4.36 freezes two decisions.

### D36 — fine reuse decision

```text
E0 -> FULL_REUSE
E1 -> CORE_ONLY
E2 -> REJECT
E3 -> HOLD
```

F-R1 contains E0 and E1, so NU3 fails D36 sufficiency.

### D36_CORE — coarse core-reuse decision

```text
E0 or E1 -> ALLOW_CORE_REUSE
E2 -> REJECT_CORE_REUSE
E3 -> HOLD
```

Both F-R1 cases map to ALLOW_CORE_REUSE.

Therefore on this fresh corpus:

```text
EXACT_REACH_SUFFICIENCY = FAIL
FINE_DECISION_SUFFICIENCY = FAIL
CORE_REUSE_DECISION_SUFFICIENCY = NOT_DEFEATED
```

This is not universal D36_CORE validation.

It establishes the logical possibility that a representation can be scientifically insufficient for one explanandum while operationally sufficient for a narrower declared decision.

## 5. Finite residue theorem

The formal theorem belongs to the internal quantifier only.

For an explicitly bounded probe index Fin n:

```text
(∀ p, Relevant(p) -> Tested(p))
->
InternalResidueEmpty(Relevant, Tested)
```

This is nearly definitional, and that is a virtue.

The hard scientific work is not proving the implication.

The hard work is earning:
- the probe class;
- its enumeration;
- relevance to D;
- execution receipts;
- and the right not to confuse the class with the world.

## 6. Why a theorem prover cannot prove world completeness from the certificate

A proof assistant can prove a theorem about every element of Fin n.

It cannot infer that every future world-separating intervention is represented by some element of Fin n unless that world-adequacy premise is separately supplied.

If world adequacy is imported as an axiom, kernel verification only certifies consequences conditional on that axiom.

This is the Axiom-Laundering boundary.

## 7. Syntactic-extension countertheorem

The Lean bridge also constructs an extended probe language containing a fresh constructor outside the lifted old tested predicate.

Its meaning is deliberately modest:

```text
a declared formal probe language can be strictly extended
```

not:

```text
nature necessarily realizes the fresh constructor.
```

The point is to block a logical inference from internal exhaustiveness to language-finality.

## 8. UV–Vis return

Suppose a UV–Vis compiler has a finite registered test suite that exhaustively verifies:
- ADC arithmetic;
- baseline transform;
- wavelength calibration equations;
- absorbance computation;
- a bounded inference rule.

A proof assistant can certify zero residue inside that declared software/mathematical class.

It still cannot certify that:
- the optical coupling captured every chemically relevant distinction;
- no unmodeled interferent exists;
- another measurement modality cannot split an apparent equivalence class;
- future instrumentation will not expose a new variable.

Thus early MQR's physical-oracle/logical-processor distinction survives formalization intact.

## 9. The bounded-residue principle

MQR-4.36 proposes the following doctrine:

> Residue may be finitely eliminated only relative to an explicitly declared probe algebra, relevance/decision family, and execution semantics. The boundary of that quantification must remain visible in the claim.

Symbolically:

```text
ZERO_INTERNAL_RESIDUE(P,D)
does not entail
ZERO_OPEN_WORLD_RESIDUE.
```

This is compatible with strong local proof and open-world realism simultaneously.

## 10. Successor hypotheses only

The F-R1 naturalistic collision suggests that NU3 still conflates distinctions such as:
- specification adoption/enforcement topology;
- unknown-keyword or extension semantics;
- how a nominal domain extension becomes behaviorally active.

These are post-result hypotheses only.

MQR-4.36 does not add them to NU3.

Any successor representation must predeclare them before new world contact.

## Verdict

```text
FINITE_INTERNAL_RESIDUE_THEOREM = EARNED_IN_PRINCIPLE_AND_EXECUTED_IN_4.36
DECLARED_PROBE_CLASS_4.36 = EXHAUSTED
OPEN_WORLD_RESIDUE = NOT_ELIMINATED
NU3_NATURALISTIC_SUFFICIENCY = FAIL
D36_FINE_SUFFICIENCY = FAIL
D36_CORE_SUFFICIENCY = NOT_DEFEATED_ON_FRESH_CORPUS
QUANTIFIER_BOUNDARY = LOAD_BEARING
```
