# MQR-3.187 — Real-Domain Authority-Envelope Selection, Externally Justified State-Bound Search, Reset–Homing–Replica Feasibility & First Non-Self-Referential Exact-Learning World-Contact Authorization

## 0. Gate
MQR-3.186 permits exact identification only inside a prospectively presealed bounded challenge envelope.

MQR-3.187 searches for a **real, non-self-referential scientific domain** satisfying all of:

1. externally defined scientific authority output;
2. finite or externally bounded decision/update alphabet;
3. externally defensible state/fault bound;
4. reset, homing, or qualified-replica access;
5. observable input/output behavior;
6. feasible complete conformance campaign;
7. real world-contact rather than an MQR-authored toy;
8. a clear separation between adaptive learning and final certification;
9. a later out-of-envelope challenge capable of testing boundary honesty.

No candidate is promoted merely because it has a finite workflow graph.

## 1. Candidate A — GEMS adaptive laboratory automation

### Source status
**READ DEPTH: FULL-TEXT-SUBSTANTIVE-READ via the complete RSC HTML article.**

Tahara-Arai et al. (2026), *GEMS: a deterministic finite automaton framework for adaptive laboratory automation*, DOI 10.1039/D5DD00409H.

The paper states that:
- experimental protocols are represented as POMDPs;
- when the protocol policy is deterministic over a finite observation alphabet, its execution logic is representable as a Mealy-style DFA;
- the DFA represents protocol control logic rather than laboratory physics;
- raw observations are quantized through a map (b:Omega	oSigma);
- physical wet-lab case studies include RGB liquid-mixture optimisation and long-running mammalian-cell culture;
- code, raw data, figure scripts, and exact software snapshots are publicly archived.

The RGB study has explicit GEMS states for mixing, imaging, and evaluation and actual robot/camera measurements.

### Passes
- external source and external state semantics;
- genuine physical experimental execution;
- open code/data/versioned snapshots;
- finite control graph;
- replayable archived traces;
- independent replicas exist at the sample/well level.

### Fatal failure
The paper explicitly limits the DFA sufficiency claim to **protocol control logic**.

The physical/sample state remains latent in the POMDP, and finiteness is obtained only after observation quantisation:

[
b:Omega	oSigma.
]

Therefore the number of GEMS controller states does not independently bound the number of scientifically relevant physical or epistemic states.

Using the protocol-state count as the authority-state bound would conflate:

[
	ext{finite control representation}
]

with

[
	ext{finite world/authority state}.
]

That violates the MQR-3.186 Envelope Boundary Principle.

### Verdict
**NEAR-SURVIVOR / CONTROL-LAYER-EXACTNESS-POSSIBLE / SCIENTIFIC-AUTHORITY-BOUND-NOT-JUSTIFIED.**

## 2. Candidate B — regulated qPCR result interpretation

### Source status
**READ DEPTH: PARTIAL-FULL-TEXT of FDA/CDC control and interpretation sections.**

Regulated molecular assays provide an unusually explicit scientific authority layer:
- positive/negative controls gate run validity;
- thresholded Ct categories determine positive, negative, inconclusive, or invalid outputs;
- invalid or inconclusive outcomes trigger specified retest/re-extraction/reporting actions;
- guidance requires interpretation/retest algorithms to be prospectively defined rather than improvised after the pivotal study.

Representative FDA/CDC documents contain finite interpretation tables and explicit run-invalidity conditions.

### Passes
- real scientific/reporting authority output;
- externally specified finite decision categories;
- explicit control failures and retest transitions;
- repeated runs/specimens can provide replica structure;
- interpretation rules are prospectively documented.

### Fatal failure 1 — learning collapses into rediscovery
The decision algorithm is already explicitly published.

If MQR constructs the finite automaton directly from the regulatory table, no unknown scientific authority automaton has been learned from world contact.

It has been **compiled from a specification**.

### Fatal failure 2 — physical fault domain is not bounded by the decision table
Continuous amplification curves, Ct uncertainty, contamination, inhibition, extraction quality, specimen quality, instrument drift, and other failure mechanisms are mapped into discrete categories.

The finite table bounds the **decision layer**, not the full scientific world/fault layer.

Thus exact recovery of the table would not certify that its threshold/quantizer is scientifically adequate.

### Verdict
**NEAR-SURVIVOR / REAL-AUTHORITY-SEMANTICS / DECISION-RULE-ALREADY-SPECIFIED / PHYSICAL-FAULT-BOUND-NOT-JUSTIFIED.**

## 3. Candidate C — FDA-regulated automated diagnostic software / FilmArray-style result state

Regulatory records expose finite run-control outputs such as Passed, Failed, Invalid and finite reported-result categories such as Detected, Not Detected, Equivocal, Invalid.

### Strength
This is a genuine machine-mediated scientific authority decision rather than a research toy.

### Failure
- proprietary implementation;
- no public membership-query endpoint;
- no justified upper bound on hidden implementation states;
- no controlled reset/homing contract for an external learner;
- output-category finiteness does not bound internal or physical fault states.

### Verdict
**AUTHORITY-RICH / BLACK-BOX-ACCESS-FAIL / STATE-BOUND-FAIL.**

## 4. Candidate D — calibrated DAQ / measurement-device authority

NI calibration documentation supplies a real example where external calibration rewrites EEPROM calibration constants and invalidates the original calibration certificate; traceable recalibration can create a new certificate.

### Strength
This is genuine measurement authority with explicit state-changing intervention.

### Failure
- calibration error/drift is continuous;
- hardware fault state is not externally finite-bounded;
- recalibration itself changes the instrument state and authority object;
- exact finite-state learning would require an unjustified abstraction of the physical metrology layer.

### Verdict
**REAL-MEASUREMENT-AUTHORITY / DESTRUCTIVE-UPDATE-WITNESS / FINITE-FAULT-BOUND-FAIL.**

## 5. Candidate E — LAP / PRISM / protocol-state infrastructures

LAP specifies task and safety state machines for agent-to-instrument control; PRISM validates generated laboratory protocols in simulation and then executes selected protocols on robotic hardware.

### Strength
Typed actions, safety states, instrument constraints, and explicit protocol lifecycle are useful envelope ingredients.

### Failure
They currently provide protocol/infrastructure state machines, not an independently justified finite state space for scientific epistemic authority.

Simulation validity and protocol safety cannot be promoted directly into scientific-world equivalence.

### Verdict
**USEFUL-ENVELOPE-INFRASTRUCTURE / AUTHORITY-STATE-BOUND-FAIL.**

## 6. Candidate F — open-source SCPI multimeter state machine

Open-source SCPI implementations expose explicit measurement state machines for MEASure, INIT, FETCh, triggers, modes, and asynchronous measurement.

### Strength
- queryable software;
- finite command surface;
- resettable digital implementation;
- naturally compatible with automata learning.

### Failure
Its finite control state is instrument-operation state, not scientific measurement authority.
Without independently validated calibration/uncertainty/measurement-validity semantics, exact control-model learning earns no realist measurement authority.

### Verdict
**LEARNABILITY-RICH / AUTHORITY-SEMANTICS-FAIL.**

## 7. Tournament result
No single candidate satisfies the full conjunction.

The two strongest near-survivors are complementary:

### GEMS
[
	ext{physical world contact + open finite control}
]

but lacks an externally justified finite **authority/world** state bound.

### Regulated qPCR interpretation
[
	ext{real authority semantics + finite decision rule}
]

but the rule is already specified and does not bound the physical assay fault space.

Therefore the missing object is not simply another domain.

It is a justified bridge between:
1. continuous/open physical world state;
2. observation/quantisation layer;
3. finite decision/authority automaton.

## 8. Layer-Split Barrier
Let:
- (X) be physical/world states;
- (q:X	oSigma) be an observation/quantisation map;
- (M) be a finite authority automaton over (Sigma);
- (A_M) be its authority output.

Even if (M) is learned or verified exactly,

[
widehat M equiv M,
]

this does not imply that the composite scientific authority map

[
A_Mcirc q
]

is world-adequate.

There may exist (x_1,x_2in X) such that

[
q(x_1)=q(x_2)
]

while the scientifically warranted authority verdict differs.

Then no exactness theorem over (M) can recover the lost distinction.

### Layer-Split Non-Transfer Principle
[
oxed{
	ext{Exact finite decision logic}

otRightarrow
	ext{exact scientific authority}
}
]

unless the observation/quantisation map and its domain of validity are independently justified.

This is an application of MQR's earlier observation-aliasing and authority-firewall doctrines, not a new primitive.

## 9. External State-Bound Search result
The candidate search produced three kinds of bounds:

1. **Code/protocol bound** — number of states written in a controller.
2. **Decision-table bound** — number of reportable interpretation categories.
3. **Physical/fault bound** — number of scientifically relevant world/failure states.

Only (3) can support the strong interpretation of a finite scientific authority automaton.

No candidate produced an independently justified finite bound of type (3).

Therefore:

[
oxed{
	ext{EXTERNALLY JUSTIFIED SCIENTIFIC-AUTHORITY STATE BOUND = NOT FOUND}.
}
]

## 10. Reset–Homing–Replica feasibility
### GEMS
Digital controller reset and archived replay are available; physical experiments have sample replication.
But these do not reset the latent physical world to an authority-equivalent state in the strong sense required for exact world-state learning.

### qPCR
Independent controls/runs/specimens support replication at the assay level.
But repeated assays do not enumerate or bound the full failure ontology.

### calibrated instrument
Recalibration changes the authority-bearing calibration state; reset is not epistemically neutral.

### protocol software
Digital reset is easy, but the scientific authority semantics are too weak.

Thus no candidate simultaneously satisfies:
- strong authority semantics;
- justified state bound;
- valid reset/homing/replica semantics.

## 11. World-contact authorization
### Not authorized
No candidate currently warrants:

**FIRST NON-SELF-REFERENTIAL EXACT SCIENTIFIC-AUTHORITY AUTOMATON WORLD CONTACT — GO.**

### Narrow preparation allowed
Two lanes are scientifically useful without overclaiming:

#### Lane G — GEMS control-layer exactness
Use the published code/data snapshots to test whether the externally authored protocol-control automaton can be exactly reconstructed or conformance-checked.

Allowed claim:
**CONTROL-LAYER CLASS-IDENTIFIED.**

Forbidden promotion:
**SCIENTIFIC-AUTHORITY GLOBALLY IDENTIFIED.**

#### Lane Q — regulated assay decision-layer authority
Compile the published interpretation/retest rules into a finite authority decision graph and audit completeness against the published specification.

Allowed claim:
**DECISION-LAYER SPECIFICATION-COMPLETE.**

Forbidden promotion:
**PHYSICAL ASSAY FAULT SPACE EXHAUSTED.**

These lanes are diagnostic controls for the Layer-Split Barrier, not substitutes for the missing world-contact witness.

## 12. Literature custody update
The three pending MQR-3.186 sources arrived in Drive intake during this stage.

Canonicalised:
- Pferscher & Aichernig (2023), *Fingerprinting and Analysis of Bluetooth Devices with Automata Learning* — moved to canonical paper commons.
- Aichernig & Tappler (2019), *Efficient Active Automata Learning via Mutation Testing* — moved to canonical paper commons.
- The uploaded TACAS 2024 object is the full Proceedings Part II rather than a standalone Kruger–Junges–Rot paper; it was moved to the non-paper/proceedings collection and renamed to record that it contains the chapter *Small Test Suites for Active Automata Learning*.

Thus the previous three-item byte-custody wait is closed, with the Kruger paper held as chapter-in-proceedings custody rather than falsely relabeled as a standalone paper PDF.

## 13. Generation-IV gate
- G4-A prospective differential: OPEN
- G4-B non-isomorphic replication: NOT REACHED
- G4-C side-by-side reduction defeat: FAIL
- G4-D constitutional compression: PASS-INTERNAL / novelty FAIL
- finite quotient existence: HOLD
- exact learning inside bounded class: PASS-CONDITIONAL
- real-domain externally justified authority-state bound: FAIL
- first exact-learning world contact: NOT AUTHORIZED

MQR-4.0 remains unauthorized.

## 14. Next frontier
The next useful question is not "find another finite-state domain" indiscriminately.

It is:

> Can the observation/quantisation bridge itself earn authority strongly enough that exact decision-layer learning transports to a scoped scientific-authority claim?

This requires a domain where:
1. the finite decision layer is externally specified or learnable;
2. the observation map (q) has independently validated calibration/error bounds;
3. within a presealed scope, observation aliasing is prospectively tested;
4. a finite out-of-envelope adversarial set can attack the bridge rather than only the automaton.

Without this bridge, exact automata learning remains a control/decision result.

## 15. Verdict
**PASS-REAL-DOMAIN-TOURNAMENT / NO-QUALIFYING-EXACT-AUTHORITY-DOMAIN / GEMS-CONTROL-LAYER-NEAR-SURVIVOR / REGULATED-QPCR-AUTHORITY-LAYER-NEAR-SURVIVOR / EXTERNAL-PHYSICAL-STATE-BOUND-NOT-FOUND / LAYER-SPLIT-NON-TRANSFER / CONTROL-AND-DECISION-PREPARATION-ALLOWED / FIRST-EXACT-LEARNING-WORLD-CONTACT-HOLD / MQR-3.186-BYTE-CUSTODY-CLOSED / GENERATION-III-STABLE / NO-MQR-4.0.**
