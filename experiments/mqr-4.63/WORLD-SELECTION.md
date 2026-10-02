# MQR-4.63 — Harvest-Grounded World Selection

Status: **SELECTED UNDER FROZEN ELIGIBILITY RULE / PRE-EXECUTABLE-REVEAL**

Frozen before Harvest contact:
- PRESEAL: `a0dcb1605dbc691cca414d5b27b4fcdf8dc5e910`
- WORLD-CALIBRATION-MANIFEST: `d114f87ba2e295a6a838c74989f12173f213d312`

World inclusion below was based on structural eligibility, heterogeneity and source quality, not pilot outcome.

## W1 — CAUSAL-SEP

Family: **causal intervention / structure discovery**

Source donor:
- Hyttinen, Eberhardt & Hoyer (2013), *Experiment Selection for Causal Discovery*, JMLR 14:3041–3071.
- The paper treats causal experiment selection through separating/completely-separating systems and gives constructive experiment-set results under explicit causal assumptions.

Reconstruction:
- finite family of candidate directed causal structures;
- actions are interventions on declared variable subsets;
- observations eliminate structures incompatible with the intervention response;
- action availability is reversible;
- no hidden rival enters unless a dedicated open-frontier variant is switched on.

Strong baseline:
- greedy unresolved-edge/separating-system coverage;
- expected hypothesis elimination;
- random intervention.

Expected MQR exposure:
- **IDR active**;
- OPR/ARR/NEDL should largely collapse in the closed reversible variant;
- this is a positive control against gratuitous MQR complexity.

Primary metrics:
- identification success;
- actions to identification;
- FSR;
- EAI;
- NED should remain ~0 when alternative separators remain.

## W2 — SENSING-GRID

Family: **active sensing / sequential measurement**

Source donor:
- Veiga & Renoux (2023), *From Reactive to Active Sensing: A Survey on Information Gathering in Decision-Theoretic Planning*.
- Their survey formulates information gathering through POMDP/belief-state planning and uses target tracking as an illustrative setting.

Reconstruction:
- moving hidden target on a small graph;
- actions choose one sensor/node to query;
- observations update a belief distribution;
- target transition and sensor model are known;
- sensing is reversible and non-destructive.

Strong baseline:
- one-step entropy reduction / expected information gain;
- short-horizon lookahead;
- random sensing.

Expected MQR exposure:
- mostly **IDR only**;
- OPR, BOD, CSD and NED should remain inactive;
- if MQR adds large gains here, that is evidence of metric or implementation inflation.

Primary metrics:
- target-state entropy;
- localization accuracy;
- information gain per query;
- FSR/NED/BOD as negative controls.

## W3 — SCOUT-PARK

Family: **resource-bounded scientific data acquisition / irreversible retention**

Natural source donor:
- CMS Collaboration (2025), *Enriching the Physics Program of the CMS Experiment via Data Scouting and Data Parking*, Physics Reports 1115:678–772.
- Data scouting trades complete event information for much higher event rates within bandwidth constraints.
- Data parking stores raw detector data collected with lower trigger thresholds for later processing when compute becomes available.

Important boundary:
This is **not** a counterfactual claim about what CMS should have done. It is a transparent stylized acquisition world inspired by the real architectural tradeoff.

Reconstruction:
- event stream contains known high-value classes plus low-threshold/exterior classes;
- actions allocate a finite per-step data budget among:
  - FULL: rich event content, low rate;
  - SCOUT: reduced content, high rate;
  - PARK: raw retention with future compute/debt;
  - DROP: irreversible loss;
- a later analysis capability or hidden signal family can appear after acquisition;
- some future separators require raw fields absent from scouted events.

Strong baselines:
- current-target expected information per bandwidth;
- cost-normalized acquisition;
- high-rate scouting;
- fixed parking fraction;
- random budget mix.

MQR layer:
- OPR tracks preservation of unique future separators;
- ARR protects raw/exterior reopening capacity;
- NEDL records skipped unique retention routes;
- BOD records irreversible branchwise loss.

Primary metrics:
- current-target detection;
- retained event rate;
- future hidden-family recovery;
- FSR;
- RCR/RL;
- BOD;
- NED;
- cost/bandwidth.

## W4 — THEORY-ECOLOGY

Family: **theory-guided scientific experiment choice / policy-induced evidence ecology**

Source donor:
- Dubova, Moskvichev & Zollman (2026), *Against Theory-Motivated Experimentation: Can Random Experimental Choice Lead to Better Theories?*
- Their multi-agent simulations compare confirmation-, falsification-, disagreement-oriented and random experiment choice and report regimes where theory-motivated selection produces apparently successful theories on less representative evidence.
- Public code/data availability is declared by the paper.

Important boundary:
MQR-4.63 does **not** claim exact replication of their implementation. The world is a separately auditable reduced reconstruction designed to test the same acquisition-feedback failure family plus MQR-specific ancestry/reopening metrics.

Reconstruction:
- finite experimental context grid;
- current theory family models only part of the true relation surface;
- acquisition policy chooses contexts;
- under-sampled exterior region can contain a hidden rival/failure pattern;
- repeated theory-guided querying can concentrate samples where the current family is easiest to fit;
- evidence can share policy/generator ancestry even when nominal sample count grows.

Strong baselines:
- confirmation-seeking;
- falsification-seeking;
- disagreement;
- random exterior;
- representativeness-aware acquisition;
- robust R-IDeA-inspired proxy combining informativeness + representativeness + local error-deamplification.

MQR layer:
- ERR/BSI measure exterior-rival recovery and self-created blind spots;
- EAI penalizes common acquisition ancestry;
- ARR forces bounded reopening capacity;
- NEDL tracks repeated skipping of unique exterior separators.

Primary metrics:
- in-sample fit;
- global predictive error;
- hidden-rival recovery;
- BSI;
- ERR;
- EAI;
- RCR/RL;
- NED.

## Heterogeneity check

| Dimension | CAUSAL-SEP | SENSING-GRID | SCOUT-PARK | THEORY-ECOLOGY |
|---|---|---|---|---|
| action reversible | yes | yes | mixed/no | yes |
| action alters future evidence availability | weak | weak | strong | strong via sampling ecology |
| model/rival set open | optional control | no | yes via later analysis/hidden family | yes |
| common-mode ancestry | low | low | medium | high |
| intervention semantics | yes | sensing | acquisition/retention | experiment selection |
| primary MQR objects expected active | IDR | IDR | OPR/ARR/NEDL | ARR/EAI/NEDL |

The pack therefore satisfies the frozen heterogeneity requirement without selecting worlds on observed MQR performance.
