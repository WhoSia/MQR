# MQR-4.29 — Prospective Profile Calibration, Axis-Separating World Construction, Known-Outcome Blind Benchmark, Inter-Axis Redundancy/Monotonicity Stress & Whether W–N–I–T–D Can Earn Measurement Status without Reintroducing a Truth Oracle

Status: ACTIVE / PRESEAL

## Objective
Test whether the Real-Language W/N/I/T/D profile can earn a defensible measurement status.

The target is NOT:
distance to final Truth.

The target is narrower:
can each coordinate behave as a reproducible, prospectively operationalized measure of its declared evidential construct without collapsing into the other coordinates?

## Constructs
W = world resistance:
fraction/strength of authorized adverse perturbation probes under which the target constraint survives.

N = noncommon evidence-route strength:
independent evidence ancestry represented by genuinely distinct failure lineages, not replicate count.

I = inferential identification:
fraction of claim-relevant consequences invariant across the current surviving rival set.

T = transport:
fraction/strength of predeclared held-out regimes in which the scoped claim survives.

D = defeat exposure:
coverage of distinct live failure families by tests/routes capable of defeating the claim, not challenge count.

## Measurement-status ladder
LEVEL 0 — LABEL:
coordinate has only a verbal meaning.

LEVEL 1 — OPERATIONAL INDEX:
prospectively specified mapping from auditable receipts to a bounded coordinate exists.

LEVEL 2 — INTERNAL CALIBRATION:
known-outcome blind benchmark shows monotonicity, axis separation, decoy invariance and implementation reproducibility.

LEVEL 3 — EXTERNAL CALIBRATION:
independent real-world/adjudicated cases establish criterion/discriminant validity beyond the synthetic constitution.

LEVEL 4 — TRUTH-DISTANCE METRIC:
requires independently justified truth-state space and distance semantics.

MQR-4.29 may at most establish LEVEL 2.
LEVEL 3 requires genuinely external calibration.
LEVEL 4 is not targeted.

## Prospective benchmark constitution
Use a full factorial synthetic world family across three latent levels for each construct:

W,N,I,T,D in {LOW,MID,HIGH}.

Total base worlds:
3^5 = 243.

The latent key is held in a separate file from the observation file.

The canonical Rust calibration scorer receives ONLY public observations.
It does not receive latent labels.

A separate evaluator reveals the hidden key only after scoring.

## Exact structural lane
Construct public receipt fields such that each axis has a prospectively frozen mechanical estimator.

Target levels:
LOW = 0.25
MID = 0.50
HIGH = 1.00

Exact-lane estimators:
W = survived adverse probes / total adverse probes.
N = independent lineages / 4.
I = invariant consequences / total claim-relevant consequences.
T = successful held-out regimes / total held-out regimes.
D = covered distinct defeat families / total defeat families.

These are construct-relative indices, not probabilities of truth.

## Noisy blind lane
A second lane introduces finite-sample noise while preserving a hidden latent target for each construct.

Targets:
LOW = 0.20
MID = 0.50
HIGH = 0.80.

The scorer sees only realized counts/receipts.
The hidden evaluator sees latent levels.

Purpose:
test recovery, monotonicity and cross-axis leakage under realistic finite observation noise.

## Decoy attacks
Public packets also contain variables that should NOT change the corresponding construct:

- N decoy: replicate count within the same lineage.
- D decoy: number of challenges inside already-covered failure families.
- I decoy: raw rival count when claim-relevant invariance is unchanged.
- T decoy: training/in-scope regime count when held-out transport is unchanged.
- W decoy: repeated measurements without new adverse perturbation geometry.

A valid scorer must ignore these decoys.

## Presealed success criteria

### S1 — Exact recovery
Exact structural lane:
all five coordinates recovered exactly for all 243 worlds.

### S2 — Axis intervention separation
For matched worlds differing in only one latent axis:
only the corresponding measured axis may change in the exact lane.

Cross-axis leakage count must be zero.

### S3 — Monotonicity
LOW < MID < HIGH for every coordinate in the exact lane.

In the noisy lane, mean score by latent level must be strictly monotone for each coordinate.

### S4 — Noisy criterion recovery
For each coordinate in the noisy lane:
Pearson correlation(measured, hidden latent target) >= 0.90.

This threshold is frozen prospectively.

### S5 — Cross-axis discriminant stress
Because the latent factorial design is orthogonal:
for measured axis A and nonmatching hidden axis B,
absolute Pearson correlation <= 0.10.

### S6 — Decoy invariance
Mutating decoy variables while keeping construct-defining receipts fixed must not alter any measured profile coordinate.

### S7 — Cross-implementation reproducibility
Rust canonical scorer and independent Python reference scorer must emit byte-identical profile outputs.

## Anti-circularity rule
Passing this benchmark proves only:
the declared operational indices can recover synthetic constructs generated under a deliberately axis-separating constitution.

It does NOT prove:
- that the constructs are the uniquely correct epistemic dimensions;
- that historical science instantiates them cleanly;
- that equal numeric intervals have equal epistemic meaning;
- that the five dimensions are externally independent;
- that any scalar combination tracks truth.

Therefore a pass can promote W/N/I/T/D at most to:

INTERNALLY_CALIBRATED_OPERATIONAL_INDICES.

It cannot promote them to:
TRUTH METRIC
or
EXTERNALLY VALIDATED SCIENTIFIC SCALE.

## Literature pressure
The stage will actively use construct-validity and multi-trait/multi-method principles:
- Cronbach & Meehl style construct validation;
- Campbell & Fiske style convergent/discriminant separation;
- modern validity arguments emphasizing that validity concerns interpretation/use, not mere internal consistency;
- measurement-invariance/generalizability warnings;
- evidential-diversity literature where relevant.

## Failure rules
If any S1-S7 fails:
the affected coordinate remains LABEL or LEVEL-1 OPERATIONAL INDEX.

If S1-S7 pass:
W/N/I/T/D may be promoted jointly to LEVEL-2 INTERNALLY CALIBRATED OPERATIONAL INDICES.

External calibration remains HOLD regardless.
