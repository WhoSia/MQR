# MQR-4.64 — Literature Boundary and Novelty Kill

Status: **POST-PRESEAL / PRE-EXECUTABLE-REVEAL**

Frozen parents:
- PRESEAL `517da250c97c84770be3fae543ba2b6b9a3c0407`
- BINDING-MANIFEST `3365c6ce4b87c7a9e7281246b3aac1de73c6209a`

## Strong prior-art pressure

### Constrained Bayesian experimental design
Guo, Huang, Zhang, Katt, Kaski & Bharti (2026), *Constrained Bayesian Experimental Design via Online Planning*.

This directly covers sequential Bayesian design under dynamic budget, cost and physical constraints with online multi-step lookahead planning.

MQR novelty kill:
- dynamic experimental constraints are not new;
- feasible-set restriction is not new;
- online replanning is not new;
- multi-step constraint-aware experiment choice is not new.

### Sequential optimal experimental design
Huan & Marzouk, *Sequential Bayesian Optimal Experimental Design via Approximate Dynamic Programming*.
Shen & Huan (2023), *Bayesian Sequential Optimal Experimental Design for Nonlinear Models Using Policy Gradient Reinforcement Learning*, DOI `10.1016/j.cma.2023.116304`.

sOED already treats experiment selection as a finite-horizon dynamic program / POMDP with feedback and lookahead.

MQR novelty kill:
- myopic != sequence-optimal is prior art;
- future consequences of current experiments are already legitimate planning state;
- policy-level rather than one-step experiment optimization is prior art.

### Safe / constrained exploration
Wachi, Sui, Yue & Ono (2018), *Safe Exploration and Optimization of Constrained MDPs Using Gaussian Processes*, DOI `10.1609/aaai.v32i1.12103`.
Ni & Kamgarpour (2025), *A Safe Exploration Approach to Constrained Markov Decision Processes*.

MQR novelty kill:
- restricting policies to preserve safety/feasibility during learning is prior art;
- an action can be rejected because of reachable-future constraints without MQR.

### Real options / irreversibility
Arrow & Fisher (1974), *Environmental Preservation, Uncertainty, and Irreversibility*, DOI `10.2307/1883074`.
Henry (1974), *Investment Decisions under Uncertainty: The Irreversibility Effect*.

MQR novelty kill:
- preserving future choices under irreversibility and uncertainty is not new;
- future information can create an irreversibility/option premium without an MQR ontology.

### Robust design under misspecification
Callahan & Catanach (2026), *On the Misinformation in a Statistical Experiment*.
Tang, Sloman & Kaski (2026), *Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification*.

MQR novelty kill:
- more expected information can be harmful under misspecification;
- representativeness and error-deamplification are modern explicit acquisition criteria.

## 4.63 backflow

MQR-4.63 already showed:
- OPR / ARR / EAI / exterior control were absorbed by strong baselines in the frozen cross-domain pack;
- NEDL had a local own-ablation effect only in SCOUT-PARK;
- diagnostic separability does not imply policy incrementality.

Therefore 4.64 may not rescue these objects by making worlds more favorable after seeing 4.63.

## Surviving target

The only candidate excess under study is a **promotion boundary**, not a new planner:

> characterize when a scientific diagnostic changes a declared future scientific-capability reachability set in a way that is (a) contemporaneously observable, (b) not already represented by the strong baseline's constraints/state/reward, and (c) released when substitutes or reversibility remove the capability scarcity.

This may still collapse into constrained planning / real-option / safe-exploration semantics. Such collapse is a valid result.

## Claim ceiling

No claim of novelty for:
- constraint-aware experiment choice;
- future-value planning;
- irreversibility premiums;
- safe exploration;
- POMDP experiment design;
- robust active learning;
- feasibility preservation.

A surviving MQR contribution would need either:
1. a nonredundant scientific-capability reachability semantics not behaviorally equivalent to the matched planning baseline; or
2. a useful negative theorem/characterization showing when typed MQR diagnostics are guaranteed redundant and should be released.
