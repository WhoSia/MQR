# MQR-3.185 — Finite-Index Authority Learnability, Distinguishing-Update Basis, Active State-Separation Complexity & Whether a Scientific Authority Quotient Can Be Empirically Identified without Exhausting the Space of Future Challenges

## 0. Origin
MQR-3.184 defined the canonical authority quotient

[
h_Aequiv_A h_B
iff
orall win U^*,;
B(h_A,w)=B(h_B,w),
]

with canonical state

[
sigma^*(h)=[h]_{equiv_A}.
]

MQR-3.185 asks a harder question:

> Even if the authority quotient has finite index, can its states and equivalence classes be empirically identified by finitely many scientific challenge/update probes without exhausting the whole future-update language?

The target must distinguish three different claims:

1. **finite-state existence**;
2. **state distinguishability given the correct finite machine**;
3. **exact learnability/certification of the unknown machine from finite interaction**.

These are not equivalent.

## 1. Formal learning problem
Assume a deterministic finite authority machine

[
M=(S,U,Lambda,delta,O),
]

where:
- (S) is the unknown authority-state set;
- (U) is the typed update alphabet;
- (Lambda) is the authority-output alphabet;
- (delta) is the update transition;
- (O) returns authority behavior.

A probe is an update word (win U^*).
A probe response is the observed authority behavior generated under (w).

The scientific learner does not initially know:
- (|S|);
- the transition graph;
- a complete characterizing set;
- whether the apparent finite model is complete;
- whether all updates are resettable/repeatable.

## 2. Distinguishing basis for a known finite quotient
If the quotient machine is already known, finite-state testing theory provides finite state-identification objects:

- preset distinguishing sequences;
- adaptive distinguishing sequences;
- unique input/output sequences;
- characterizing sets / W-sets;
- checking sequences.

An adaptive distinguishing sequence is a decision tree of inputs whose observed outputs identify the starting state when such a sequence exists.

Therefore:

[
	ext{FINITE INDEX + KNOWN MACHINE}
]

can support finite state separation under the usual determinism/completeness/reset assumptions.

This part is established prior art.

## 3. Cost is nontrivial
Even after finite distinguishability is granted, optimal probing need not be easy.

Minimum-cost adaptive distinguishing sequence construction is NP-hard, and hard to approximate under standard formulations.

Thus:

[
	ext{finite distinguishability}

otRightarrow
	ext{cheap distinguishability}.
]

MQR cannot treat existence of a finite witness basis as implying economical scientific identification.

## 4. Exact active learning and the equivalence-oracle burden
Angluin's (L^*) result learns a minimal DFA in polynomial time under a Minimally Adequate Teacher supplying:

1. membership queries;
2. equivalence queries;
3. counterexamples when a conjectured automaton is wrong.

The crucial second service is global:

> Is the current finite hypothesis behaviorally equivalent to the unknown target over the entire language?

If no, the teacher returns a distinguishing word.

This is much stronger than ordinary finite empirical probing.

In practical active automata learning, equivalence queries are usually replaced by conformance testing, random testing, model checking against a finite abstraction, or other counterexample-search procedures.

Therefore practical termination means:

[
	ext{no counterexample found by the current test regime}
]

rather than

[
	ext{global behavioral equivalence proved}.
]

## 5. Finite-Probe Non-Certifiability
Consider any finite set (Qsubset U^*) of tested update words.

If the authority-machine state bound is not known in advance, there exist two finite deterministic machines (M_1,M_2) such that:

[
orall qin Q,quad B_{M_1}(q)=B_{M_2}(q),
]

but for some untested word (w^*),

[
B_{M_1}(w^*)
eq B_{M_2}(w^*).
]

Construction:
take a machine matching every tested prefix and extend one machine with an additional finite chain reached only by a longer/unqueried word, ending in a different authority output.

Both machines remain finite-state.

Hence no fixed finite probe set can certify global authority equivalence over the class of all finite-index authority machines with unbounded unknown state count.

### Finite-Probe Non-Certifiability Theorem
Without an a priori structural bound, complete equivalence oracle, or equivalent completeness assumption:

[
oxed{
	ext{finite observed challenge agreement}

otRightarrow
	ext{global authority-state equivalence}.
}
]

This is a generic automata-identification consequence, not MQR-specific mathematics.

## 6. Why finite index alone is insufficient
MQR-3.184 left open:

[
|H/equiv_A|<infty.
]

Even granting that condition does not tell the learner the index (n).

The class

[
igcup_{n<infty}mathcal M_n
]

of all finite authority machines has no universal finite exhaustive probe basis independent of a state bound.

Thus:

[
	ext{FINITE INDEX}

otRightarrow
	ext{FINITE CERTIFIABILITY FROM UNKNOWN BLACK-BOX ACCESS}.
]

The missing ingredient is not merely computational power.
It is **epistemic closure over unseen future challenges**.

## 7. Bounded-state rescue
Suppose instead that all of the following are presealed:

1. deterministic finite authority dynamics;
2. finite update alphabet;
3. reliable reset to a known initial state or otherwise adequate homing/synchronization access;
4. an upper bound (N) on the number of authority states;
5. stable transitions during the learning campaign;
6. every required probe is admissible and observable.

Then finite complete conformance-testing methods can in principle search a bounded implementation class, and active learning can combine membership-style probing with systematic equivalence/conformance tests.

This gives a conditional positive result:

[
oxed{
	ext{bounded finite model class + strong query access}
Rightarrow
	ext{finite exact identifiability may be possible}.
}
]

But the scientific burden shifts to justifying the bound and oracle assumptions.

## 8. Scientific challenge-space problem
Scientific authority processes violate several classical active-learning conveniences.

### 8.1 No perfect reset
A scientific intervention may permanently alter:
- a specimen;
- an ecosystem;
- a deployed system;
- a dataset's selection status;
- a holdout's independence;
- a certification reserve.

Thus repeated membership queries may change the very epistemic state being queried.

### 8.2 No equivalence oracle
There is normally no agent that can certify:
"no future admissible scientific challenge distinguishes this authority model from reality."

### 8.3 Open or expanding alphabet
New instruments, new representations, new interventions, new failure predicates, and new rival theories can create future update types not present in the original alphabet (U).

### 8.4 Nonstationarity
The target world, institution, evaluator, or evidence infrastructure may change during learning.

Therefore exact authority-automaton identification is strictly harder than ordinary finite active automata learning.

## 9. Distinguishing-update basis
For a fixed finite authority machine, define a finite set (Wsubset U^*) to be a **state-distinguishing basis** if

[
orall s_i
eq s_j,;
exists win W:
B(s_i,w)
eq B(s_j,w).
]

Such a basis separates states of the known machine.

But a second object is required for scientific certification:

### Model-completeness basis
A probe family (C) is model-complete relative to hypothesis class (mathcal H) iff agreement on (C) implies full behavioral equivalence for every target in (mathcal H).

[
orall M_1,M_2inmathcal H,quad
B_{M_1}|_C=B_{M_2}|_C
Rightarrow
M_1equiv M_2.
]

State-distinguishing and model-completeness are different.

A W-set can distinguish known specification states without proving that an unknown implementation has no additional hidden states unless the fault domain/state bound assumptions are supplied.

This distinction is constitutionally important for MQR.

## 10. Active separation complexity
Let

[
D(s_i,s_j)
]

be the minimum cost of an admissible adaptive probe strategy that separates two authority states.

Let

[
D(M)
]

be the worst-case cost for identifying any state of machine (M).

Then MQR should track:
- existence of a separator;
- worst-case probe length;
- adaptive vs preset separation;
- reset/homing cost;
- destructive or reserve-consuming probe cost;
- whether the probe alters future admissibility.

This last term is especially important scientifically:
a challenge can reveal the state while consuming or changing the state.

Thus epistemic probing is not necessarily passive measurement.

## 11. Challenge-conservation constraint
Suppose probe (u) is informative but consumes the only remaining certification resource or irreversibly changes the authority state.

Then the act of identifying the state can change the state being identified.

Formally:

[
I(u;s_t)>0
]

but

[
delta(s_t,u)
eq s_t.
]

This is ordinary active-system identification structurally, but in MQR it creates a governance constraint:

> state-identification evidence cannot automatically be reused as if it were a non-consuming certification resource.

This follows from the existing selection/certification firewall and reserve doctrine; it is not a new primitive.

## 12. Learnability hierarchy
MQR-3.185 therefore establishes a strict hierarchy:

### L0 — Behavioral definition
The quotient is defined by all future update words.

### L1 — Finite index
There are finitely many exact authority states.

### L2 — Pairwise distinguishability
Every distinct state pair has some finite separating update word.

### L3 — Finite state-identification basis
A finite characterizing/distinguishing family separates the states of the known quotient.

### L4 — Exact model learnability
Finite interaction identifies the unknown quotient within a specified hypothesis class.

### L5 — Scientific certifiability
The assumptions making L4 exact are themselves justified by world-contact rather than stipulated.

The implications do not collapse:

[
L5Rightarrow L4Rightarrow L3Rightarrow L2,
]

while finite index alone does not grant L4 or L5.

## 13. Exact scientific verdict
At present MQR has not earned:
- a finite index for real scientific authority;
- an upper bound on that index;
- a closed update alphabet;
- resettable authority dynamics;
- a valid equivalence oracle;
- a finite model-complete challenge suite.

Therefore:

[
oxed{
	ext{EXACT EMPIRICAL IDENTIFICATION OF THE FULL MQR AUTHORITY QUOTIENT = HOLD}.
}
]

This is not pessimism about learning useful approximate models.
It is a rejection of silently upgrading finite challenge success into global quotient identification.

## 14. Relation to MQR realism
This result fits the anti-laundering constitution.

A finite challenge suite may earn authority for:

[
	ext{the tested challenge envelope},
]

not automatically for:

[
	ext{all future admissible challenges}.
]

Therefore MQR must type claims as:

- **ENVELOPE-IDENTIFIED** — separated over a specified finite/bounded update family;
- **CLASS-IDENTIFIED** — exact relative to a presealed bounded hypothesis/fault class;
- **GLOBALLY IDENTIFIED** — requires a genuine completeness proof/oracle and is generally unavailable.

No finite empirical test campaign should be relabeled GLOBAL merely because no counterexample was observed.

## 15. Prior-art reduction
The generic positive machinery is fully prior art:
- Angluin (L^*): exact active learning with membership/equivalence queries;
- distinguishing/characterizing sequences: finite state identification;
- checking/conformance sequences: implementation checking under fault-domain assumptions;
- adaptive distinguishing sequences: active state discrimination;
- practical automata learning: equivalence queries approximated by conformance testing.

The generic negative result is also inherited from the distinction between exact equivalence access and finite testing.

Thus no formal novelty is claimed for the learning theory.

The MQR-specific contribution remains semantic/governance:
**do not confuse finite challenge coverage with authority over an unbounded future challenge language.**

## 16. Generation-IV gate
- G4-A prospective differential: OPEN
- G4-B non-isomorphic replication: NOT REACHED
- G4-C side-by-side reduction defeat: FAIL
- G4-D constitutional compression: PASS-INTERNAL / novelty FAIL
- finite quotient: HOLD
- exact quotient learnability: HOLD
- global finite challenge completeness: NOT ESTABLISHED

MQR-4.0 remains unauthorized.

## 17. Next frontier
The next useful problem is no longer exact global learning.

It is to construct a **bounded challenge envelope** for a real scientific domain and ask whether:
1. the update alphabet can be presealed;
2. an authority-state upper bound can be justified;
3. a finite distinguishing/conformance basis can be generated;
4. the probe campaign leaves enough unconsumed certification capacity;
5. an out-of-envelope challenge falsifies the learned quotient.

That would return the formal machinery to world contact without pretending the open scientific future is exhausted.

## 18. Verdict
**PASS-LEARNABILITY-STRATIFICATION / FINITE-INDEX-NOT-SUFFICIENT / DISTINGUISHING-BASIS-CONDITIONAL / EXACT-LEARNING-REQUIRES-EQUIVALENCE-OR-FAULT-BOUND / FINITE-PROBE-NON-CERTIFIABILITY / CHALLENGE-CONSERVATION-CONSTRAINT / GLOBAL-QUOTIENT-IDENTIFICATION-HOLD / ENVELOPE-VS-CLASS-VS-GLOBAL-AUTHORITY-TYPING / GENERATION-III-STABLE / NO-MQR-4.0.**
