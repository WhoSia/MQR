# MQR-4.63 — Cross-Domain Calibration Result

Status: **FIRST-REVEAL RESULT FROZEN / QUALIFIED NEGATIVE RESULT**

First executable reveal:
- head: `34a22befcb30e8328c19d29b0964ab3ebe84f248`
- run: `36963803586`

All four first-reveal jobs succeeded without scientific or plumbing repair:
- `MQR-4.63/Calibration`
- `MQR-4.63/Independent-Audit`
- `MQR-4.63/Analysis`
- `MQR-4.63/Deterministic-Replay`

Calibration size:
- 5 structurally distinct worlds
- 3,392 paired policy runs
- deterministic replay PASS
- independent metric recomputation PASS
- negative-control invariants PASS
- scalar MQR score forbidden

## Frozen classification matrix

| Coordinate | Frozen classification | Own-ablation worlds |
|---|---|---|
| OPR / BOD | **COLLAPSES_TO_BASELINE** | SCOUT-PARK, SAMPLE-RESERVE |
| ARR / RCR | **COLLAPSES_TO_BASELINE** | SCOUT-PARK, THEORY-ECOLOGY, SAMPLE-RESERVE |
| EAI | **COLLAPSES_TO_BASELINE** | THEORY-ECOLOGY |
| Exterior reserve / ERR | **COLLAPSES_TO_BASELINE** | SCOUT-PARK, THEORY-ECOLOGY |
| NEDL / NED | **SURVIVES_LOCAL** | SCOUT-PARK only |

No coordinate satisfies the frozen `SURVIVES_CROSS_DOMAIN` gate.

## Paired own-ablation effects

Benefit delta is signed so positive favors `mqr_full`.

### OPR — primary BOD

SCOUT-PARK:
- mean benefit delta: **0.0023**
- bootstrap 95% CI: **[-0.0076, 0.0130]**
- nontrivial: **NO**

SAMPLE-RESERVE:
- mean: **0.0000**
- CI: **[0, 0]**
- nontrivial: **NO**

Verdict: OPR does not earn independent policy incrementality in this pack.

### ARR — primary RCR

SCOUT-PARK:
- mean: **0.0052**
- CI: **[-0.0156, 0.0313]**
- nontrivial: **NO**

THEORY-ECOLOGY:
- mean: **0.0000**
- CI: **[0, 0]**

SAMPLE-RESERVE:
- mean: **0.0000**
- CI: **[0, 0]**

Verdict: reopening capacity is diagnostically meaningful in some policy comparisons, but the explicit ARR guard does not add independent action-guiding value here.

### EAI

THEORY-ECOLOGY:
- full vs `-EAI`: **0.0000 [0, 0]**

Verdict: EAI does not earn independent policy incrementality in this pack.

### Exterior reserve — primary ERR

SCOUT-PARK:
- mean: **0.0093**
- CI: **[-0.0058, 0.0246]**
- nontrivial: **NO**

THEORY-ECOLOGY:
- mean: **0.0000**
- CI: **[0, 0]**

Verdict: exterior recovery is a useful diagnostic but the dedicated MQR exterior guard is absorbed by strong baseline behavior here.

### NEDL — primary NED

SCOUT-PARK:
- mean benefit delta: **0.1539**
- bootstrap 95% CI: **[0.1337, 0.1760]**
- positive sign fraction: **0.917**
- nontrivial: **YES**

THEORY-ECOLOGY:
- **0.0000 [0, 0]**

SAMPLE-RESERVE:
- **0.0000 [0, 0]**

Verdict: **SURVIVES_LOCAL**, not cross-domain.

NEDL is therefore retained as a local candidate for resource-bounded retention/search regimes, not promoted to a general cross-domain acquisition primitive.

## Negative controls

CAUSAL-SEP:
- `mqr_full` vs strong causal-identifiability baseline: conventional-success delta **0**
- BOD = 0, CSD = 0, NED = 0 as presealed.

SENSING-GRID:
- `mqr_full` vs entropy-greedy baseline: conventional-success delta **0**
- BOD = 0, CSD = 0, NED = 0 as presealed.

This is a substantive calibration success: MQR did **not** manufacture gains in worlds where the extra coordinates were predeclared inactive.

## Diagnostic separability survives more strongly than policy incrementality

THEORY-ECOLOGY contains a key descriptive witness.

Confirmation vs falsification have the same mean conventional success (**0.4762**) while differing sharply in:
- ERR: **0.0 vs 0.5**
- RCR: **0.0 vs 0.5**
- NED: **0.5167 vs 0.0**
- BSI: **1.0 vs 0.5556**

Therefore the typed coordinates can diagnose scientifically material acquisition differences not visible in the chosen conventional success metric.

But this does **not** imply that an MQR-specific guard is required to obtain the better policy. Strong disagreement, representative, random and robust-multifactor baselines already recover the exterior structure in the frozen world.

Hence:

~~~text
DIAGNOSTIC SEPARABILITY
!=
POLICY INCREMENTALITY
~~~

and:

~~~text
A TYPED FAILURE COORDINATE CAN BE REAL
WITHOUT
A NEW MQR-SPECIFIC CONTROL RULE
BEING INDEPENDENTLY EARNED.
~~~

## Strong-baseline absorption

In THEORY-ECOLOGY:
- disagreement, random, and representative policies reach conventional success **1.0** and ERR/RCR **1.0**;
- representative acquisition reaches mean reopening latency **0.0559**;
- `mqr_full` reaches success **1.0**, ERR/RCR **1.0**, latency **0.0618**.

The MQR layer therefore does not establish superiority over strong existing acquisition ideas.

In SAMPLE-RESERVE:
- immediate-information, fixed-preserve, and `mqr_full` all reach current success **1.0**, ERR/FSR/RCR **1.0**, and BOD/NED **0**;
- the frozen sample inventory and budget make the option constraint non-binding for competent policies.

The correct result is collapse, not post-reveal redesign.

## SCOUT-PARK local result

SCOUT-PARK is the only world in which NEDL's own ablation is materially active.

Selected policy means:

| Policy | Current success | ERR | RCR | BOD | NED | BSI |
|---|---:|---:|---:|---:|---:|---:|
| current_information | 1.000 | 0.000 | 0.000 | 0.990 | 0.523 | 1.000 |
| fixed_park | 0.807 | 0.052 | 0.932 | 0.938 | 0.231 | 0.736 |
| random_mix | 0.473 | 0.090 | 0.995 | 0.899 | 0.064 | 0.350 |
| mqr_full | 0.721 | 0.055 | 0.990 | 0.934 | 0.092 | 0.578 |
| mqr_minus_nedl | 0.848 | 0.011 | 0.969 | 0.978 | 0.246 | 0.750 |

NEDL lowers exploration debt and improves reopening/exterior behavior relative to its own ablation, while sacrificing some current-target success.

But random mixing is still better on several exterior/option coordinates and worse on current-target success.

Therefore 4.63 does not identify a global winner or a uniquely MQR-optimal policy.

## Scientific verdict

The broad 4.62 action-guidance interpretation is **narrowed**.

What survives:
- typed acquisition diagnostics can reveal distinctions hidden by a single conventional success metric;
- negative-control collapse is well behaved;
- NEDL has one local action-guiding effect in a resource-bounded retention world.

What does not survive:
- cross-domain policy incrementality for OPR, ARR, EAI, exterior reserve, or NEDL;
- a new universal or broadly superior MQR acquisition policy;
- promotion of a new Real-Language acquisition version from this study.

## Real-Language promotion decision

**NO REAL-LANGUAGE v0.30 PROMOTION.**

Reason:

~~~text
NEW CALIBRATION EVIDENCE
+ STRONG-BASELINE ABSORPTION
+ NO CROSS-DOMAIN OWN-ABLATION SURVIVOR
---------------------------------------
=> DOCTRINE NARROWING / BENCHMARK RETENTION
=> NO SEMANTIC VERSION INFLATION
~~~

REALACQUIRE 0.29 remains the typed diagnostic/constitutional surface, but 4.63 limits what may be inferred from the existence of those receipts.

## Publication consequence

The broad computational-paper thesis:

> MQR supplies a generally independent cross-domain evidence-acquisition policy layer

is **not supported** by 4.63.

A narrower empirical/formal thesis remains plausible:

> scientific acquisition policies can be diagnostically distinguished by reopening, ancestry, separator and debt coordinates even when conventional terminal performance is matched; however, whether those coordinates require new control rules depends on binding conditions and may often be absorbed by strong existing acquisition policies.

This shifts the research frontier from **inventing another selector** to **characterizing when a diagnostic coordinate becomes action-guiding and nonredundant**.

## Claim ceiling

Earned:
- deterministic five-world calibration harness;
- strong-baseline matched negative result;
- diagnostic-separability / policy-incrementality distinction;
- local NEDL effect in SCOUT-PARK;
- explicit non-promotion of redundant acquisition objects.

Not earned:
- natural-science external validation;
- exact replication of donor studies;
- general superiority of MQR;
- cross-domain independence of OPR/ARR/EAI/NEDL/exterior reserve;
- universal acquisition rule;
- publication-level novelty for the remaining local NEDL effect.
