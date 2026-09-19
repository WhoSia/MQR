# MQR-3.186 — Bounded Challenge-Envelope Preseal, Authority Fault-Domain Constitution, Destructive-Probe Budgeting & Whether a Finite Scientific Authority Automaton Can Be Learned Exactly within a Prospectively Closed Test Regime

## 0. Aim
MQR-3.185 established that finite index alone does not make an unknown authority process finitely certifiable.

MQR-3.186 asks whether exact identification becomes legitimate after replacing the open future challenge space with a **prospectively closed bounded challenge envelope** whose assumptions are frozen before testing.

The target is explicitly relative exactness:

[
	ext{EXACT WITHIN PRESEALED CLASS}
]

not:

[
	ext{EXACT OVER ALL FUTURE SCIENCE}.
]

## 1. Bounded Challenge Envelope
Define a bounded challenge envelope

[
mathcal E=
langle
U_E,Lambda_E,mathcal C_E,N_E,R_E,D_E,S_E,A_E,B_E,Pi_E
angle
]

where:

- (U_E): finite typed update/input alphabet;
- (Lambda_E): observable authority/output alphabet;
- (mathcal C_E): presealed fault/hypothesis class;
- (N_E): structural/state-count bound;
- (R_E): reset/homing/re-entry contract;
- (D_E): determinism/noise contract;
- (S_E): stationarity/version interval;
- (A_E): update admissibility rules;
- (B_E): probe/resource budget;
- (Pi_E): abstraction/mapper and observation semantics.

Every term must be frozen before the decisive conformance campaign.

Changing one after observing failures defines a successor envelope rather than repairing the original one.

## 2. Prospectively Closed Regime
An envelope is prospectively closed for a campaign iff before execution it fixes:

1. the alphabet and abstraction map;
2. the output/verdict semantics;
3. the implementation/fault class;
4. the state-count/structural bound;
5. reset or homing access;
6. determinism/noise tolerance;
7. version/stationarity window;
8. admissible probes;
9. completeness construction;
10. probe-cost and destructive-resource accounting.

Closure does **not** assert that no future scientific challenge exists.
It only freezes what the current exactness claim ranges over.

Thus:

[
	ext{CLOSED ENVELOPE}
eq	ext{CLOSED SCIENCE}.
]

## 3. Classical bounded exactness
Let the current hypothesis (mathcal H) be a minimal Mealy machine.

Define the fault domain

[
mathcal C_{mathcal H}^{k}
=
{mathcal S: |mathcal S|-|mathcal H|le k}.
]

Let (P) be a state cover and (W) a characterization set.

Then the classical W-method suite is

[
T_W=Pcdot I^{le k+1}cdot W.
]

Under the standard deterministic finite-state assumptions, the W-method is (k)-complete:

[
orall mathcal Sinmathcal C_{mathcal H}^{k},
quad
mathcal Hsim_{T_W}mathcal S
Rightarrow
mathcal Hsimmathcal S.
]

Therefore a finite exact equivalence claim **is possible relative to a presealed bounded fault domain**.

This is established conformance-testing theory, not MQR novelty.

## 4. What the exactness claim actually says
If an authority process is encoded as a deterministic Mealy-style system and all envelope assumptions hold, then passing a complete suite licenses:

[
oxed{
	ext{CLASS-IDENTIFIED}(mathcal E)
}
]

meaning:

> no behaviorally distinct implementation inside the presealed class (mathcal C_E) survives the complete suite.

It does **not** license:

> no out-of-class state, update, failure predicate, abstraction, or future scientific challenge can distinguish the process.

Hence:

[
	ext{CLASS-EXACT}

otRightarrow
	ext{GLOBAL-EXACT}.
]

## 5. Full-text literature audit — evidence-depth labels
MQR-3.186 introduces explicit source-reading depth tags for novelty attacks and harvests.

Allowed labels:

- **FULL-TEXT-READ** — substantive methods/results/limitations sections inspected;
- **PARTIAL-FULL-TEXT** — accessible substantive sections inspected but not the entire paper;
- **ABSTRACT-ONLY** — only abstract/metadata safely inspected;
- **CITATION-ONLY** — bibliographic use only; no substantive inference permitted.

No source may be harvested as if FULL-TEXT-READ when only its abstract was inspected.

### 5.1 Pferscher & Aichernig — Bluetooth automata learning
**READ DEPTH: FULL-TEXT-READ via open full-text HTML.**

Substantive body findings:
- the MAT equivalence oracle is replaced by conformance testing;
- because the final state count of the physical SUL is unknown, conformance is only approximated by a finite set of input/output sequences;
- the physical peripheral is assumed resettable;
- response/listening parameters depend on environmental conditions;
- the implementation adds mechanisms for connection errors and nondeterministic outputs;
- fingerprinting sequences are explicitly only valid for the investigated SoCs;
- learning itself revealed a crashing input sequence.

### Harvest
1. **Unknown-state-count blocks exactness even when active learning succeeds operationally.**
2. **Reset is an epistemic resource, not a mere engineering convenience.**
3. **Physical interaction parameters belong in the challenge envelope.**
4. **Nondeterminism handling can silently alter the observational quotient and therefore must be frozen.**
5. **A successful discriminating sequence is population-relative; extending the population requires reopening the model.**
6. **A challenge can destroy/crash the SUL, so probe cost can include irreversible state loss.**

These are imported as constraints, not as novelty claims.

### 5.2 Vaandrager et al. — Small Test Suites for Active Automata Learning
**READ DEPTH: FULL-TEXT-READ for definitions, completeness results, randomisation discussion and assumptions via full-text HTML.**

Substantive body findings:
- (k)-completeness is explicitly relative to implementations at most (k) states larger than the hypothesis;
- the W-method uses state cover (P), bounded infix (I^{le k+1}), and characterization set (W);
- the paper proves the W-method (k)-complete;
- test suites grow as (|I|^k);
- smaller suites are obtained only by adding structural assumptions about the SUL/subalphabets;
- randomized ASI methods prioritize an effectively infinite suite and achieve guaranteed (k)-completeness only in the limit unless sufficient bookkeeping establishes completion.

### Harvest
1. **Fault-domain assumptions are part of the theorem, not optional implementation notes.**
2. **A smaller challenge envelope buys tractability by spending assumption strength.**
3. **Completeness metadata must name the exact fault class.**
4. **Randomized counterexample search is not finite exact certification merely because it performs well empirically.**
5. **Challenge-envelope compression and authority compression must not be conflated.**

### 5.3 Smetsers et al. — Efficient Active Automata Learning via Mutation Testing
**READ DEPTH: PARTIAL-FULL-TEXT, including introduction, conformance assumptions, test selection, and reported evaluation/discussion.**

Substantive body findings:
- classical W/partial-W style methods need a fixed upper state bound that is usually unknown;
- their suites are exponential in that bound;
- practical equivalence testing is the main learning bottleneck;
- mutation-guided/randomized methods greatly reduce cost but trade exhaustive completeness for targeted fault detection;
- in one reported setting, even one million random tests did not reliably learn the correct model across runs.

### Harvest
1. **Exactness has an explicit combinatorial price.**
2. **Probe-budget pressure creates a temptation to replace complete fault-domain coverage with empirical confidence.**
3. **Mutation/fault models can make search economical, but authority must remain typed to the injected fault family.**
4. **Failure to find a counterexample under a large random campaign is not a completeness certificate.**

### 5.4 Angluin 1987
**READ DEPTH: FULL-TEXT-SUBSTANTIVE-READ from canonical Drive PDF.**

Verified in the body:
- a minimally adequate teacher answers membership queries and conjecture/equivalence queries;
- incorrect conjectures must be accompanied by a counterexample;
- L* maintains a closed/consistent observation table;
- observation-table rows serve as candidate states and suffix columns as distinguishing experiments;
- once the table is closed and consistent, the induced DFA is the uniquely smallest acceptor consistent with the finite table;
- counterexamples and their prefixes are added back into the table and trigger another refinement cycle;
- Angluin explicitly flags equivalence-query feasibility as the problematic teacher assumption and discusses stochastic approximate substitution separately.

### Harvest
1. **Exact identification is teacher/oracle-relative, not evidence-free induction.**
2. **Distinguishing experiments are constitutive of state discovery rather than an after-the-fact test.**
3. **The exactness guarantee depends on the semantics of MEMBER/EQUIV access; replacing EQUIV changes the authority class.**
4. **Approximate stochastic substitution must not inherit the word exact from the MAT result.**

### 5.5 Rivest & Schapire 1993
**READ DEPTH: PARTIAL-FULL-TEXT / accessible extended-paper material and bibliographic full-article record.**

Safe finding:
lack of reset does not automatically make finite learning impossible; homing-sequence methods can recover learnability under stronger interaction/teacher assumptions, including counterexample support.

### Harvest
1. Replace “no reset ⇒ impossible” with:
   **no reset ⇒ require a justified alternative state-localization contract.**
2. (R_E) therefore permits reset, homing, synchronization, or another prevalidated re-entry mechanism.

Further detailed harvest remains pending full canonical-paper reread.

## 6. Fault-Domain Constitution
An exact authority-learning claim must bind itself to a named fault domain.

A valid fault-domain certificate must state:

- reference hypothesis (H_0);
- maximum state excess (k) or another explicit structural bound;
- allowed transition/output deviations;
- abstraction map;
- nondeterminism/noise exclusions or model;
- version interval;
- reset/homing semantics.

The certificate is invalid if the state bound is chosen after observing how deep a counterexample occurs.

### Prospective Bound Rule
[
oxed{
N_E	ext{ must be justified independently of pass/fail results from the decisive suite.}
}
]

Otherwise the test campaign selects the fault domain it later claims to certify.

## 7. Destructive-Probe Budget
Each probe (q) has a resource effect

[
c(q)=
langle
t,
m,
r,
d,
v
angle
]

where:
- (t): time cost;
- (m): material/monetary cost;
- (r): certification/reserve consumption;
- (d): destructive or irreversible effect;
- (v): version/state disturbance.

For suite (T),

[
C(T)=sum_{qin T}c(q)
]

only when effects are additive; otherwise the budget must track path-dependent resource state.

The complete suite is executable only if every required test remains admissible under the evolving resource state.

## 8. Learning–Certification separation
Exact model learning and authority certification must not silently share a consumable challenge resource.

Define:
- (B_L): learning/debugging/probe budget;
- (B_C): independent certification budget.

If learning consumes information that makes later certification adaptively dependent, then:

[
B_Lcap B_C
eqarnothing
]

requires explicit dependence accounting.

Preferred design:

[
B_Lperp B_C
]

through independent replicas, fresh holdouts, independent specimens, or another justified separation mechanism.

### No-Free-Reuse Rule
A challenge used to discover/refine the automaton does not automatically remain fresh certification evidence for the final automaton.

This is inherited from MQR's selection–certification firewall.

## 9. Destructive scientific systems
If a probe irreversibly modifies a unique scientific object, classical membership-query repetition can fail.

There are three admissible responses:

### R1 — True reset
Demonstrate restoration to an authority-equivalent starting state.

### R2 — Valid homing/synchronization
Use an independently justified state-localization sequence without pretending the system was reset.

### R3 — Independent replicas
Perform destructive probes on exchangeable/independently qualified replicas and model replica variation explicitly.

If none is available, an exact active-learning claim for the unique object is not authorized.

## 10. Exactness-cost frontier
Classical (k)-complete suites may grow approximately with

[
|I|^k.
]

Therefore exactness can become physically or epistemically unaffordable even when it exists mathematically.

Define:

[
mathrm{FeasibleExact}(mathcal E)
iff
T_{mathcal E}	ext{ is complete}
land
C(T_{mathcal E})le B_E
land
	ext{all tests remain admissible}.
]

If completeness holds mathematically but the required suite cannot be executed under the budget, the correct verdict is:

[
	ext{EXACT-IN-PRINCIPLE / EXECUTION-HOLD}.
]

Do not downsample the suite and keep the word exact.

## 11. Can a finite scientific authority automaton be learned exactly?
### Conditional answer: YES
Within a genuinely prospectively closed envelope, if:
1. the authority process satisfies the finite deterministic model class;
2. the fault-domain/state bound is independently justified;
3. observation and abstraction are fixed;
4. reset/homing/replica access satisfies the learning theorem;
5. transitions remain stationary;
6. a complete suite is executed;
7. destructive/resource effects do not invalidate the query semantics;
8. the final certification role is kept distinct from adaptive learning,

then exact identification within (mathcal C_E) is legitimate.

Formally:

[
oxed{
mathcal E	ext{-assumptions}
+
	ext{complete suite pass}
Rightarrow
	ext{CLASS-IDENTIFIED}(mathcal E).
}
]

### Unconditional answer: NO
The result cannot be exported beyond (mathcal E).

## 12. Scientific authority ceiling
Even perfect exact learning inside (mathcal E) licenses only:

[
A(Cmidmathcal E).
]

It does not establish:

[
A(Cmid U_{mathrm{future}})
]

for unknown future instruments, challenge types, ontologies, or fault classes.

Thus bounded exactness is compatible with MQR corrigibility.

### Envelope Boundary Principle
[
oxed{
	ext{exactness strength cannot exceed envelope closure strength}.
}
]

## 13. Current world-contact status
No real scientific authority domain has yet been materialized in this stage with:
- independently justified finite state bound;
- closed update alphabet;
- exact reset/homing/replica semantics;
- executable complete suite;
- separated learning and certification resources.

Therefore:

**BOUNDed exactness theorem = PASS.**

**REAL SCIENTIFIC AUTHORITY AUTOMATON EXECUTION = HOLD.**

This stage must not substitute a hand-designed MQR automaton as evidence for its own empirical adequacy.

## 14. Novelty status
The positive theorem is prior-art conformance testing instantiated with MQR semantics.

The source-level harvest further weakens any claim that:
- reset-free learning is categorically impossible;
- practical physical learning implies equivalence;
- large randomized testing implies completeness;
- a finite alphabet alone constitutes a closed fault domain.

MQR's contribution remains governance:
- preseal the fault domain;
- type exactness to that class;
- include resource/destructive effects in admissibility;
- separate discovery from certification;
- forbid export from bounded exactness to global realist authority.

No irreducible formal novelty is established.

## 15. Next world-contact gate
A substantive successor must select one real domain where the envelope can be made non-vacuous.

Selection criteria:
1. naturally finite/finite-bounded update alphabet;
2. externally defensible state/fault bound;
3. reset, homing, or qualified replicas;
4. observable outputs tied to a real scientific authority decision;
5. a complete suite feasible within budget;
6. an out-of-envelope successor challenge can later test whether the boundary was honestly typed.

Do not choose a domain merely because MQR itself defines the states.

## 16. Verdict
**PASS-BOUNDED-EXACTNESS-CONSTITUTION / PROSPECTIVE-ENVELOPE-PRESEAL / FAULT-DOMAIN-CERTIFICATE / K-COMPLETE-CLASS-IDENTIFICATION / DESTRUCTIVE-PROBE-BUDGET / LEARNING-CERTIFICATION-SEPARATION / RESET-HOMING-REPLICA-TRICHOTOMY / ENVELOPE-BOUNDARY-PRINCIPLE / FULL-TEXT-HARVEST-PROTOCOL-ACTIVE / REAL-AUTHORITY-AUTOMATON-EXECUTION-HOLD / GENERATION-III-STABLE / NO-MQR-4.0.**


## 17. Post-custody full-text correction — Lee & Yannakakis 1994
**READ DEPTH: FULL-TEXT-SUBSTANTIVE-READ from canonical Drive PDF.**

Verified in the body:
- adaptive distinguishing sequences are decision-tree experiments for state identification;
- if an adaptive distinguishing sequence exists, one of length at most n(n-1)/2 can be constructed, and this bound is tight;
- intermediate-subset state-identification can become PSPACE-complete;
- checking sequences distinguish a specification from non-isomorphic implementations in the stated bounded setting;
- preset distinguishing sequences/UIO sequences can be exponentially long or hard to decide, while adaptive distinguishing sequences yield stronger constructive results.

### Harvest
1. **Probe adaptivity can turn an otherwise prohibitive fixed experiment into a tractable state-identification procedure.**
2. **Existence of a finite state space does not imply cheap preset certification.**
3. **Adaptive identification cost and checking-sequence completeness are distinct resources and must be recorded separately.**
4. **The MQR destructive-probe budget must distinguish preset, adaptive, homing and checking-sequence costs rather than collapsing them to test count.**

Drive custody:
- Angluin (1987) canonical PDF confirmed.
- Lee & Yannakakis (1994) canonical PDF confirmed.
- Rivest & Schapire (1993) previously unidentified PII file canonically renamed.
