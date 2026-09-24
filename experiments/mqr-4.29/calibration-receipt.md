# MQR-4.29 — Prospective Profile Calibration Receipt

Status: LEVEL-2 INTERNAL CALIBRATION PASS / EXTERNAL CALIBRATION HOLD

## Stage
MQR-4.29 — Prospective Profile Calibration, Axis-Separating World Construction, Known-Outcome Blind Benchmark, Inter-Axis Redundancy/Monotonicity Stress & Whether W–N–I–T–D Can Earn Measurement Status without Reintroducing a Truth Oracle

## Preseal
Commit:
d5de267800745a2dd3cae3e43954b3f4ee9ff707

Frozen ladder:
LEVEL 0 — label.
LEVEL 1 — operational index.
LEVEL 2 — internal calibration.
LEVEL 3 — external calibration.
LEVEL 4 — truth-distance metric.

Maximum possible promotion in this stage:
LEVEL 2.

## Benchmark construction
Generator:
experiments/mqr-4.29/generate_calibration.py

Commit:
bef732230c8087f8649ed303a5c9cf2403d61429

Design:
3^5 = 243 full-factorial base worlds.

Two lanes:
- exact structural lane;
- noisy blind lane.

Total public rows:
486.

Separate decoy-twin rows:
486.

Hidden key is generated to a separate file and is not supplied to the canonical scorer.

Exact target levels:
0.25, 0.50, 1.00.

Noisy hidden target levels:
0.20, 0.50, 0.80.

## Frozen benchmark hashes
public.tsv:
40cdf79b4f2b41f0772f396c4b019bc2048d03ed8e64981bb15c5ca06a01b1fd

public_decoy.tsv:
5f4695c5b5f1375e395a9a2e72a746ab5b27a37d14611f18bfc71fa0f57a1a5d

hidden_key.tsv:
594efbf28249a1ddb3f568a5f94a72fa00d65f0118b57f09a5b6d25b47e64421

## Operational indices
W:
survived adverse perturbation probes / total authorized adverse probes.

N:
independent evidence lineages / normalized available lineage capacity.
Replicate count within one lineage is explicitly nonconstitutive.

I:
claim-relevant invariant consequences / total claim-relevant consequences.
Raw rival count is explicitly nonconstitutive when invariance is unchanged.

T:
successful held-out regimes / total predeclared held-out regimes.
Training/in-scope regime count is explicitly nonconstitutive.

D:
covered distinct defeat families / total declared defeat families.
Challenge multiplicity inside an already-covered family is explicitly nonconstitutive.

These are normalized construct-relative indices, not truth probabilities.

## Canonical scorer implementations
Rust canonical scorer:
language/real/src/calibrate.rs
commit 251bea78b320a77b2889d85419cb260f9e820848

Cargo registration:
c70b31d7f359e892732e5915f57df0795786c75c

Python independent reference:
language/real/calibration_reference.py
commit 3d7a41c80d53367c44f217ea0447462482bef364

## Evaluator
Initial evaluator:
a5640c17499520ca5c3d4ece0618acf9cecc22a4

Final repaired evaluator:
f9ece7212bb7ddd533c9b06676e52be42d94afd1

The evaluator sees the hidden key only after scoring output has already been produced.

## Workflow
.github/workflows/mqr-4.29-calibration.yml

Commit:
73921f45ed92952d0fa649a92e9b54331e3de41d

## Transparent implementation failures
### Failed run 1
Run:
36007577131

Cause:
Rust source contained a literal tab character inside a character literal after connector serialization.

Scientific scoring:
not reached.

Fix:
delimiter escaping only.

Fix commit:
7a55f168583e7ead276f986b7d296eeed4c80df9

No benchmark, key, threshold or construct definition changed.

### Failed run 2
Run:
36007694387

Status before failure:
- benchmark generation PASS;
- Rust build PASS;
- Rust/Python scoring concordance PASS.

Cause:
evaluator CLI still expected the pre-decoy argument count while workflow passed the strengthened public-decoy file.

Hidden-key scientific criteria:
not evaluated.

Fix:
evaluator interface only.

Final evaluator commit:
f9ece7212bb7ddd533c9b06676e52be42d94afd1

No benchmark, key, threshold or construct definition changed.

## Canonical successful run
Run:
36007841159

Head:
f9ece7212bb7ddd533c9b06676e52be42d94afd1

Conclusion:
SUCCESS.

## S1 — Exact recovery
243 / 243 exact worlds recovered exactly on all five coordinates.

Machine:
S1_EXACT_RECOVERY=PASS rows=243

## S2 — Axis intervention separation
Matched exact worlds differing in one latent axis were compared.

Cross-axis leakage:
0.

Machine:
S2_AXIS_INTERVENTION_SEPARATION=PASS leakage=0

## S3 — Monotonicity
Exact matched monotonic checks:
405 / 405 PASS.

Machine:
S3_EXACT_MONOTONICITY=PASS checks=405

Noisy level means:

W:
0.212770 < 0.497685 < 0.800347

N:
0.206211 < 0.500772 < 0.791088

I:
0.211806 < 0.496914 < 0.805748

T:
0.198688 < 0.498264 < 0.795910

D:
0.195988 < 0.493827 < 0.793596

Machine:
S3_NOISY_MEAN_MONOTONICITY=PASS

## S4 — Noisy criterion recovery
Self-axis Pearson correlations:

W:
0.973079

N:
0.975841

I:
0.974238

T:
0.974044

D:
0.976977

Presealed threshold:
r >= 0.90.

Minimum observed:
0.973079.

Machine:
S4_NOISY_CRITERION_RECOVERY=PASS min_r=0.973079

## S5 — Cross-axis discriminant stress
Presealed threshold for measured axis A versus nonmatching hidden axis B:
abs(r) <= 0.10.

Observed maximum:
0.022682.

Machine:
S5_CROSS_AXIS_DISCRIMINANT_STRESS=PASS max_abs_r=0.022682

Measured-axis maximum absolute correlation under the orthogonal noisy factorial design:
0.038496.

This is diagnostic support for internal separation, not evidence of real-world orthogonality.

## Noisy absolute error diagnostics
W MAE:
0.044985

N MAE:
0.042670

I MAE:
0.044972

T MAE:
0.044895

D MAE:
0.041821

These were not presealed promotion thresholds.

## S6 — Decoy invariance
Decoy fields changed:
2430 cells.

Profile cells changed:
0.

Machine:
S6_DECOY_INVARIANCE=PASS changed_profile_cells=0
DECOY_FIELDS_MUTATED=PASS cells=2430
DECOY_FIELDS_NONCONSTITUTIVE=PASS

Thus:
replicate count,
raw rival count,
training-regime count,
challenge multiplicity,
and repeated non-adversarial measurement count
do not mechanically inflate their corresponding coordinates.

## S7 — Cross-implementation reproducibility
Rust and Python produced byte-identical profile outputs for:
- original public benchmark;
- decoy-mutated benchmark.

Machine:
S7_CROSS_IMPLEMENTATION_REPRODUCIBILITY=PASS

## Measurement-validity audit
File:
experiments/mqr-4.29/measurement-validity-audit.md

Commit:
64a77d46b2a016fe4060e75dd990383f460b5fa3

The interpretation uses:
- construct-validation logic;
- convergent/discriminant separation;
- causal-measurement caution;
- interpretation/use validity;
- measurement-invariance and evidential-diversity warnings.

Relevant canonical Drive sources already present:
- Alexandrova & Haybron (2016), Is Construct Validation Valid?
- Vandenberg & Lance (2000), measurement invariance review
- Kuorikoski & Marchionni (2016), Evidential Diversity and the Triangulation of Phenomena
- Tal (2019), Individuating Quantities

## Scientific adjudication
All presealed S1-S7 criteria:
PASS.

Therefore:

W/N/I/T/D
=
LEVEL-2 INTERNALLY CALIBRATED OPERATIONAL INDICES.

This means:
- prospectively defined;
- mechanically computable from auditable receipts;
- monotone in their own synthetic construct;
- separable under matched interventions;
- robust to frozen decoys;
- recoverable under finite noise;
- implementation-reproducible.

It does NOT mean:
- externally calibrated across scientific domains;
- psychometric/physical interval scales;
- equally spaced epistemic quantities;
- universally orthogonal dimensions;
- probabilities of truth;
- distance to final Truth.

## Anti-circularity boundary
The synthetic generator and scorer share the same construct constitution.

Therefore successful recovery is partly constitutive by design.

The noisy blind lane, decoy attacks and implementation separation strengthen internal calibration, but cannot establish an external causal measurement relation in real historical science.

Hence:

LEVEL-3 EXTERNAL CALIBRATION = HOLD.

The next scientifically meaningful promotion requires:
real or externally adjudicated cases,
prospectively predicted axis changes,
and cross-domain invariance/transport tests not generated from the scoring definitions themselves.

## Doctrine promotion
Root README:
0edfb8cea6eccb926f08e2cbb17bfba3eda5ba0f

Current doctrine:
93d4e19e89ad331834d64c713cb2c880e5ed9472

Real-Language README:
1c45b365aee4176bbf9f6f23bf8d9e34090de2fa

## Verdict
PROSPECTIVE-FULL-FACTORIAL-BENCHMARK-PASS /
KNOWN-OUTCOME-BLIND-SCORING-PASS /
EXACT-RECOVERY-243-OF-243 /
AXIS-INTERVENTION-LEAKAGE-ZERO /
EXACT-MONOTONICITY-405-OF-405 /
NOISY-SELF-AXIS-CORRELATION-MIN-0.973079 /
CROSS-AXIS-LEAKAGE-MAX-0.022682 /
DECOY-MUTATIONS-2430 /
DECOY-PROFILE-CHANGES-ZERO /
RUST-PYTHON-CALIBRATION-CONCORDANCE-PASS /
WNITD-LEVEL2-INTERNALLY-CALIBRATED-OPERATIONAL-INDICES /
PROFILE-FACE-VALIDITY-PASS /
PROFILE-INTERNAL-DISCRIMINANT-VALIDITY-PASS /
PROFILE-EXTERNAL-CALIBRATION-HOLD /
INTERVAL-SCALE-STATUS-HOLD /
TRUTH-DISTANCE-SEMANTICS-NOT-REINTRODUCED /
SCALAR-PROJECTION-REMAINS-OFF /
FINAL-TRUTH-DISTANCE-UNIDENTIFIED /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
