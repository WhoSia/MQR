# MQR-4.65 — Literature and Prior-Art Pressure

Status: **POST-PRESEAL / PRE-EXECUTABLE-REVEAL / NOVELTY-KILL ONLY**

Canonical PRESEAL:
`bf579654ec22e91686968932417f145f717f8a84`

No compiler class, verdict definition, anti-vacuity guard, claim ceiling, or nonrepresentability criterion is changed by this pass.

## 1. History dependence is not by itself non-Markovian irreducibility

### Bacchus, Boutilier & Grove (1996), *Rewarding Behaviors*

The core prior-art pressure is direct: temporally extended / history-dependent reward can be encoded in an MDP by enriching the state with enough history-relevant information.

4.65 consequence:

```text
HISTORY DEPENDENCE
!=
SEMANTIC NONREPRESENTABILITY
```

A C0/C1 failure is scientifically interesting only as a state-sufficiency failure unless stronger compiler classes also fail.

### Thiébaux, Gretton, Slaney, Price & Kabanza (2006), *Decision-Theoretic Planning with non-Markovian Rewards*

DOI: `10.1613/jair.1676`.

This work systematically translates temporal-logic-specified non-Markovian reward decision processes into equivalent MDPs and compares construction/solution methods.

4.65 novelty kill:
- product/state augmentation for history dependence is not new;
- equivalence to a Markovian planner after adding suitable state is not new;
- compact/minimal augmented-state construction is already a separate algorithmic question.

## 2. Partial observability already motivates informational state augmentation

### Kaelbling, Littman & Cassandra (1998), *Planning and Acting in Partially Observable Stochastic Domains*

Canonical Drive source:
`13lNQIQF4duF31tGa9VGldEMWXxrtz6Sh`.

The POMDP framework uses history of actions/observations through an information state/belief representation, and the paper studies finite-memory controllers as compact policy representations.

4.65 consequence:

```text
OBSERVATION HISTORY
CAN BE COMPILED INTO
AN INFORMATION STATE
WHEN THE MODEL CONSTITUTION
SUPPORTS THAT UPDATE
```

Scientific provenance/history variables therefore need an independent reason to resist ordinary information-state augmentation.

## 3. Sequential scientific experiment choice is already a dynamic-programming / POMDP problem

### Huan & Marzouk (2016), *Sequential Bayesian optimal experimental design via approximate dynamic programming*

Canonical Drive source:
`13fWsLQ-kymrZqDFH0BXUk_5OWXJd8a7r`.

The paper formulates general sequential optimal experimental design as a dynamic program; batch and greedy designs appear as special cases.

Novelty killed:
- lookahead scientific experiment choice;
- feedback from previous observations;
- future-value-aware experiment selection;
- scientific design as sequential control.

### Shen & Huan (2023), *Bayesian Sequential Optimal Experimental Design for Nonlinear Models Using Policy Gradient Reinforcement Learning*

DOI: `10.1016/j.cma.2023.116304`.
Canonical Drive source:
`1gjlLxsPTU5_mH_pvxs59Qb4H4cMFn14r`.

The paper formulates sOED explicitly as a finite-horizon POMDP with information-theoretic utilities.

4.65 consequence:
MQR cannot claim that a scientific information-acquisition policy escapes ordinary sequential planning merely because the latent scientific state is partially observed or posterior-valued.

## 4. Dynamic experiment constraints are already first-class in BED

### Guo, Huang, Zhang, Katt, Kaski & Bharti (2026), *Constrained Bayesian Experimental Design via Online Planning*

ICML 2026, PMLR 306:37961–37984; arXiv `2605.26990`.
Canonical Drive source:
`1bW0dI9MPo23tkQcTtxMjrhbhVOrUoKSX`.

The method combines offline policy/posterior amortization with online multi-step scenario-tree planning under dynamic budget, cost and physical/design-transition constraints.

Novelty killed:
- dynamic feasibility constraints in scientific experimental design;
- online replanning when constraints change during deployment;
- multi-step lookahead under such constraints.

4.65 surviving question is therefore not whether scientific constraints can matter, but whether the MQR constraint semantics require a state/constraint language that ordinary constrained planning cannot represent.

## 5. Relational/object state weakens fixed-vector nonclosure claims

### Diuk, Cohen & Littman (2008), *An Object-Oriented Representation for Efficient Reinforcement Learning*

DOI: `10.1145/1390156.1390187`.

### Wang, Joshi & Khardon (2008), *First Order Decision Diagrams for Relational MDPs*

DOI: `10.1613/JAIR.2489`.

### Sanner & Boutilier (2009), *Practical Solution Techniques for First-Order MDPs*

DOI: `10.1016/j.artint.2008.11.003`.

These lines of work treat MDP states as structured collections of objects/relations and derive policies at a relational level rather than requiring one fixed propositional slot for every possible object.

4.65 consequence:

```text
NEW RIVAL / ROUTE / PROVENANCE OBJECT
EXCEEDS FIXED FEATURE VECTOR
```

does **not** imply:

```text
ORDINARY SEQUENTIAL PLANNING
CANNOT REPRESENT THE STATE
```

It motivates C3 generic finite-set/graph state.

## 6. Pre-stage Harvest pressure

The pre-4.65 close-reading audit also matters:

- Blackwell: decision-universal experiment comparison can exist inside a fixed experiment/state constitution.
- Lindley: expected-information dominance is weaker than Blackwell decision dominance.
- Bernardo: an epistemically described information objective can become ordinary Bayesian expected utility after the decision space is constituted appropriately.
- Ay–Jost–Lê–Schwachhöfer: sufficient-statistic invariance can characterize Fisher geometry rather than merely preserve an arbitrary metric.
- Yamaguchi–Nozawa: approximate sufficiency gives a quantitative bounded-distortion neighborhood under explicit regularity assumptions.

The Ay et al. result is particularly important: the Fisher quadratic form is uniquely characterized up to a constant among the relevant weakly continuous quadratic-form fields invariant under sufficient statistics, and sufficient statistics preserve the Amari–Chentsov structure. This demonstrates a general methodological lesson for 4.65: representation change can support positive structure theorems once the admissible transformation category is explicit.

## 7. Strong novelty kill

MQR-4.65 cannot claim invention of:

- history-to-state Markovization;
- temporal-logic/product-state compilation;
- POMDP information-state representation;
- finite-memory policy/controller representation;
- dynamic programming for sequential experimental design;
- POMDP formulations of Bayesian experimental design;
- dynamic constraints in BED;
- generic object/relational state representations;
- scientific epistemic objectives merely being representable within decision theory.

## 8. Surviving MQR target

The strongest remaining target is narrower:

> Given a source MQR acquisition authority and frozen information-admissibility rules, what is the **least ordinary state augmentation** required for exact feasible-set, policy, release, transition and scientific-reachability equivalence?

This turns 4.65 from a vocabulary novelty claim into a **compilation/minimal-state court**.

## 9. Critical theorem pressure

The PRESEAL's C4 class exposes a likely theorem:

If:
1. the source authority is a contemporaneously decidable predicate `C(h,a)` of finite history `h`,
2. source release and scientific labels are also functions of that finite history,
3. the target planner may use `h` itself as state,

then the identity state compiler `φ(h)=h` and target feasibility predicate `G(h,a)=C(h,a)` give an immediate lossless representation.

Therefore a genuine `NONREPRESENTABLE_C4` witness would require violating at least one of those premises. If the violation is hidden-future information, it is already rejected as `ORACLE_DEPENDENT_SOURCE`.

This theorem is not yet the executable verdict; it will be formalized and independently stress-tested before 4.65 closes.

## 10. Claim ceiling after literature pressure

Even if C0–C3 expose failures, MQR-specific control semantics is not earned unless the failure survives the C4 theorem boundary without violating information admissibility.

A likely scientifically meaningful negative result is:

```text
MQR MAY CONTRIBUTE
WHAT SCIENTIFIC STATE /
CONSTRAINT SHOULD BE CONSTITUTED

WITHOUT CONTRIBUTING
A NEW SEQUENTIAL-CONTROL
EXPRESSIVITY CLASS
```

That outcome is admissible and will not be treated as a failure of the project.
