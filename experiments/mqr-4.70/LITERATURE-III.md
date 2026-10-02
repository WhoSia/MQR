# MQR-4.70 — Literature Readout III: Newly Normalized Core Baselines

Status: **READ / DRIVE-NORMALIZED / BASELINE-ABSORPTION-STRENGTHENED / GOVERNANCE-RESIDUE-NARROWED**

## Drive normalization completed

Moved from `00_INTAKE — Literature Radar` into canonical libraries:

### 10_PAPERS
- Barnett & Crutchfield (2015) — *Computational Mechanics of Input–Output Processes: Structured Transformations and the ε-Transducer*.
- Elahi et al. (2024) — *Adaptive Online Experimental Design for Causal Discovery* — ICML 2024.
- Tigas et al. (2022) — *Interventions, Where and How? Experimental Design for Causal Models at Scale* — NeurIPS 2022.
- Gevertz & Kareva (2024) — *Minimally Sufficient Experimental Design Using Identifiability Analysis*.

### 11_BOOKS
- Torgersen (1991) — *Comparison of Statistical Experiments*.

No duplicate canonical copy was found for these five objects.

## 1. Barnett & Crutchfield 2015

The paper extends computational mechanics from autonomous stochastic processes to input–output processes.

The key object is an input-conditioned causal-state construction yielding an ε-transducer, described as a minimal/optimal predictor of the stochastic mapping from input process to output process.

### MQR collision

This sharply strengthens baseline F3:

```text
INPUT-CONDITIONED PREDICTIVE STATE
IS PRIOR ART
```

Therefore MQR-4.70 cannot claim novelty merely because predictive equivalence depends on a family of admissible interventions/inputs.

### Surviving residue

The ε-transducer takes the input process/family as part of the modeling situation.

MQR-4.70's narrower question remains:

> What scientific warrant permits treating a declared intervention/input envelope as the relevant or closed family for authority claims about state minimality?

This is a governance question, not a predictive-state construction question.

## 2. Elahi et al. 2024

Elahi et al. explicitly use a **graph separating system**: a family of interventions sufficient to cut every graph edge at least once under the stated assumptions.

They then add:
- adaptive allocation among interventions;
- sample-history-dependent selection;
- a confidence-indexed termination condition;
- finite-sample efficiency analysis.

### MQR collision

This absorbs several naive 4.70 claims:

```text
SEPARATING INTERVENTION FAMILY
+ ADAPTIVE SELECTION
+ STOPPING RULE
!=
MQR NOVELTY
```

It also shows that a family can be justified relative to a declared identifiability target and structural assumptions.

### Surviving residue

The relevant question becomes conditional:

> When may the structural assumptions and declared target be treated as adequate to close the intervention universe?

If the closure is assumption-relative, MQR must represent that authority ceiling explicitly rather than pretend to universal minimality.

## 3. Tigas et al. 2022

The paper embeds causal discovery in Bayesian optimal experimental design.

It selects both:
- the intervention target;
- the intervention value/strength.

The acquisition objective is expected information gain over uncertainty in the causal model.

### MQR collision

This strongly activates the utility-reconstruction baseline:

```text
TEST-FAMILY SELECTION
CAN BE A STANDARD EXPECTED-INFORMATION-GAIN PROBLEM
```

MQR does not get credit for proposing a new selector unless a concrete scientific constraint survives this reconstruction.

### Surviving residue

The BOED optimizer presupposes:
- a model/hypothesis space;
- a prior/posterior representation;
- a design space;
- an admissible intervention-value range;
- a utility/acquisition objective.

MQR-4.70's remaining pressure is upstream of optimization: who licenses the design space and its closure conditions?

## 4. Gevertz & Kareva 2024

The paper explicitly defines a minimally sufficient experimental design through practical identifiability.

It seeks data-collection timing/amount sufficient to uniquely parameterize a model while minimizing experimental time/cost.

### MQR collision

This is a direct novelty kill:

```text
MINIMALLY SUFFICIENT EXPERIMENTAL DESIGN
IS ESTABLISHED SCIENTIFIC PRACTICE
```

MQR-4.70 cannot sell “minimal sufficient test family” as a new primitive.

### Surviving residue

Minimal sufficiency is always relative to:
- a model class;
- parameters of interest;
- a noise/data regime;
- a declared identifiability criterion.

Therefore a scientific authority claim should expose those relativizing conditions.

## 5. Torgersen 1991

The monograph provides a self-contained theory of statistical experiment comparison.

Relevant structure includes:
- derived experiments;
- decision problems;
- deficiencies;
- equivalent conditions for deficiency;
- randomization criterion;
- equivalence and representation of experiments;
- sufficient algebras;
- local/fixed-sample comparison.

### MQR collision

This makes the experiment-comparison baseline substantially stronger than Blackwell alone.

```text
EXPERIMENT EQUIVALENCE
EXPERIMENT DEFICIENCY
APPROXIMATE COMPARISON
RANDOMIZATION
SUFFICIENCY
```

are all mature mathematical objects.

### Surviving residue

Even a complete comparison theory over a specified experiment class does not by itself answer whether that class exhausts scientifically admissible future contact.

This is the clearest remaining 4.70 boundary.

## Consolidated baseline verdict

After reading the newly normalized sources:

```text
PREDICTIVE-STATE CONSTRUCTION: BASELINE ABSORBED
SEPARATING TEST FAMILIES: BASELINE ABSORBED
ADAPTIVE TEST SELECTION: BASELINE ABSORBED
MINIMAL SUFFICIENT EXPERIMENT DESIGN: BASELINE ABSORBED
EXPERIMENT COMPARISON / DEFICIENCY: BASELINE ABSORBED
UNIQUE MINIMAL FAMILY: FALSE EVEN SYNTHETICALLY
```

The surviving MQR question is now narrower:

```text
WHO WARRANTS THE CLOSURE
OF THE ADMISSIBLE SCIENTIFIC INTERVENTION ENVELOPE?
```

Equivalent formulation:

> A state may be minimal relative to a declared family U. What licenses treating U as the family against which scientific minimality or stopping authority should be assessed, especially when future admissible probes may expand U?

## Current candidate contribution

Not a new experiment optimizer.

Not a new predictive-state construction.

Not a new informativeness order.

Candidate contribution:

1. explicit authority typing for family-relative sufficiency;
2. closure certificates for declared intervention envelopes;
3. exterior-probe debt when closure is not warranted;
4. transport conditions for admissibility envelopes across domains;
5. a prohibition on promoting finite-family minimality into open-world scientific minimality.

This candidate remains OPEN pending naturalistic calibration.
