# MQR-4.67 — Approximation Prior-Art and Baseline Collision

Status: **POST-PRESEAL / PRE-EXECUTABLE-REVEAL / NOVELTY-KILL / ANTI-SELF-CONFIRMATION**

PRESEAL:
`2be9ea7c9aa94cd36ca3540e3306a193234af84a`

## Evidence tags

All statements use:
**OBSERVED / PROVED / ENUMERATED / SIMULATED / INFERRED / OPEN**.

## 1. Ferns, Panangaden & Precup — bisimulation metrics

### Source
Norm Ferns, Prakash Panangaden, Doina Precup.
*Metrics for Finite Markov Decision Processes* (2004).

Drive canonical source:
`1Hu3BKEsHRBXgxVNo0pIqruzNnQmYUKOf`.

Later continuous-state treatment:
*Bisimulation Metrics for Continuous Markov Decision Processes*,
SIAM Journal on Computing, DOI `10.1137/10080484X`.

### OBSERVED
The finite-MDP paper explicitly motivates approximate state compression because exact stochastic equivalence is brittle when model probabilities are themselves estimated or approximate.

It constructs smooth bisimulation semimetrics from:
- immediate reward difference;
- a probability metric over successor distributions;
- positive weights combining these terms.

For the Kantorovich-based metric, the state distance is defined as a fixed point of a weighted reward-difference plus transition-distribution distance operator.

### OBSERVED
The paper establishes a relation between bisimulation metric distance and optimal value-function difference under its assumptions. Thus a quantitative state-similarity metric with downstream value-error control is established prior art.

### Novelty kill
MQR-4.67 does not invent:
- approximate behavioral equivalence;
- weighted reward/transition state distance;
- fixed-point state-similarity metrics;
- value-error bounds from abstraction distance;
- metric-guided aggregation.

### INFERRED pressure
If MQR's typed loss vector is immediately mapped to one weighted distance and judged only by a downstream scalar value error, the construction is baseline-absorbed.

## 2. Li, Walsh & Littman — abstraction hierarchy and dynamic disaggregation

### Source
Lihong Li, Thomas J. Walsh, Michael L. Littman.
*Towards a Unified Theory of State Abstraction for MDPs* (2006).

Drive canonical source:
`1P1HjH1S47t8d3Vq8Npd09eb3hxhYmfSC`.

### OBSERVED
The paper treats abstraction as a mapping from a ground representation to a more compact representation while preserving selected properties required for decision making.

It reviews multiple abstraction families, including:
- exact bisimulation;
- homomorphisms;
- approximate bisimulation;
- bisimulation metrics;
- policy irrelevance;
- utile distinction;
- adaptive aggregation.

### OBSERVED
Its prior-work review explicitly notes dynamic aggregation/disaggregation strategies and the tradeoff that coarser abstractions provide greater computational compression/generalization but looser performance-loss bounds.

### Novelty kill
MQR-4.67 does not invent:
- preservation-contract-dependent abstraction;
- bounded approximate abstraction;
- online aggregation/disaggregation;
- the compression-versus-error tradeoff.

### INFERRED pressure
"Re-expansion when approximation becomes unsafe" is not novel merely because it is called scientific reopening. MQR must show a materially different trigger/authority semantics.

## 3. Modern state-abstraction surveys

### OBSERVED
Recent model-based RL surveys continue to treat state abstraction as compacting the state space while preserving task-relevant behavior, and discuss ε-bisimulation / bounded-loss abstractions as established methods.

A 2024 JMLR paper by Panangaden, Rezaei-Shoshtari, Zhao, Meger & Precup extends homomorphism/abstraction machinery to continuous state/action settings and uses approximate/lax bisimulation ideas for learned abstraction.

### Novelty kill
Modern representation learning and continuous-control work already moves far beyond finite tabular exact partitions. MQR cannot claim novelty from applying approximate abstraction outside a tiny finite machine.

## 4. Multi-objective / Pareto baseline

### OBSERVED
Multi-objective reinforcement learning already represents multiple conflicting objectives using vector rewards, Pareto fronts/coverage sets, and a variety of linear and nonlinear scalarizations.

Recent literature explicitly distinguishes:
- vector-valued objective retention;
- Pareto/non-dominated solution sets;
- scalarization by preference weights;
- nonlinear scalarization.

### Novelty kill
MQR-4.67 does not invent:
- a vector objective;
- refusal to use one linear weight vector;
- Pareto incomparability;
- preference-sensitive scalarization.

### Strong pressure
A typed scientific-loss vector is not novel simply because coordinates are noncommensurable or because linear weights can reverse preferences.

Any surviving MQR-specific object must concern the **authority semantics attached to particular lost distinctions**:
- a lost rival separator;
- a hidden provenance/common-mode distinction;
- a disabled reopening trigger;
- an exterior discovery-route loss;
- a release/commit authority error.

Whether that semantics is formally distinct from constrained multi-objective control remains **OPEN**.

## 5. Baseline absorption tests required by 4.67

Before any Real-Lang promotion, the Court must test:

1. **Bisimulation-metric absorption** — can conventional behavioral distance + value-error bounds already justify the tested merge?
2. **Multiobjective absorption** — can typed losses be represented as an ordinary vector objective with a Pareto/coverage-set treatment?
3. **Constraint absorption** — are hard vetoes merely ordinary safety constraints?
4. **Adaptive-abstraction absorption** — is re-expansion just known dynamic disaggregation?
5. **Provenance/reopening residue** — does anything remain that changes scientific authority but is not captured by the chosen planning/value objective?

## 6. Simulation epistemic boundary

### PRESEALED
A simulation result has authority only over the declared simulator semantics.

Even perfect robustness over:
- seeds;
- implementations;
- parameter grids;
- repeated synthetic worlds

does not validate:
- the ontology of loss coordinates;
- the completeness of event grammar;
- naturalistic prevalence;
- scientific importance of a coordinate;
- publication-level transport.

Simulation can:
- falsify an implementation expectation;
- expose internal counterexamples;
- characterize a frozen formal machine;
- compare baselines under declared assumptions.

Simulation cannot certify that those assumptions are true of science.

## 7. Surviving 4.67 target

### OPEN
The only plausible MQR-specific surface is:

> a typed **scientific-authority-loss receipt** in which approximation is allowed only under explicit coordinate-level authority ceilings, with provenance-preserving ancestry and mandatory reopen/re-expand behavior when later world contact activates a previously silent distinction.

This remains OPEN until:
- baseline absorption tests;
- executable court;
- Real-Lang candidate validation;
- and naturalistic transport.

## 8. Real-Lang consequence

The software-development question is legitimate even if the scientific novelty collapses.

An executable typed receipt can still be useful as infrastructure if it:
- prevents accidental scalarization;
- records evidence provenance;
- makes loss budgets machine-checkable;
- forces explicit reopen/re-expand decisions;
- exposes when a result is SIMULATED rather than OBSERVED.

Utility as infrastructure does not imply novelty as scientific theory.
