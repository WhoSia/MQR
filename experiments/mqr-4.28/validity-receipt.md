# MQR-4.28 — Truth-Proximity without a Truth Oracle Receipt

Status: TPX TRUTH-METRIC REJECTED / REAL-LANGUAGE v0.2 PROFILE-FIRST PASS

## Stage
MQR-4.28 — Truth-Proximity without a Truth Oracle, Verisimilitude Rivalry, Historical Rank-Reversal Attack, Axis-Weight Underdetermination, Scalar-Ablation Test & Whether TPX Measures Earned Realist Proximity rather than Merely Re-encoding the MQR Constitution

## Preseal
Initial preseal commit:
82eacedb2c067bda2a8efb4e875c7dcc9cb20041

Implementation-choice note:
9844d7e9decf1d25c5c948067cb859e3b3a32457

## Naming result
R-Language / R-Packet is retired.

New canonical name:
Real-Language / Real-Packet v0.2.

Reason:
avoid collision with the statistical programming language R and better express the language's role.

## Implementation result
Canonical implementation:
Rust.

Independent reference implementation:
Python.

Rust package:
language/real/Cargo.toml
commit 4c11627a07d204cb75e5d46c278091fcaf8c380b

Rust compiler:
language/real/src/main.rs
commit cc68ced6706e6870b7096df43428b2316439a117

Python reference:
language/real/reference.py
commit fc764aeddcfbd347221b96e18116cc30cb32595c

Language constitution:
language/real/README.md
commit ff7a5b129110fdca732e7e23edca875b5ba63f66

Six historical packets were migrated to REALPACKET 0.2.

An initial migration run failed because the first header replacement was over-escaped and some files remained RPACKET 0.1.
This was treated as an implementation bug, not hidden or ignored.
All six headers were corrected before the canonical run.

## Canonical execution
Workflow:
.github/workflows/real-language-ci.yml

Workflow commit:
794d90c9c321733e7d5d15fe830a609fff9bb085

Canonical successful run:
36006070617

Canonical run head:
5e64eaae770079db5e6116f0ced0d765b1d43874

Rust:
1.98.1

Build:
PASS.

Rust/Python receipt concordance over all six historical packets:
PASS.

Rust/Python concordance with optional diagnostic scalar enabled:
PASS.

Machine receipt:
REAL_LANGUAGE_CROSS_IMPLEMENTATION_CONCORDANCE=PASS

Thus compiler semantics are not dependent on Python or Rust implementation choice.

## Language-choice judgment
Python was not rejected because packet execution is too slow.
For the current packet scale, Python speed is not the scientific bottleneck.

Rust is canonical because:
- the packet language benefits from explicit static types and enums;
- parser/runtime semantics can be frozen into a standalone compiled binary;
- implementation errors can be caught earlier;
- performance leaves room for larger packet corpora without changing architecture.

Python is retained because:
- it is compact and auditable;
- it provides a structurally independent implementation;
- exact cross-language concordance is a stronger implementation check than one compiler testing itself.

Implementation language remains epistemically irrelevant to scientific authority.

## Verisimilitude audit
The stage actively compared TPX to the truthlikeness/verisimilitude research programme.

Key pressure:
- Popper's original true/false-content definition of verisimilitude fails under the Tichy-Miller result;
- later theories of truthlikeness introduce substantive choices about similarity, possible-world distance, relevant content, structure, or approximation;
- Niiniluoto separates verisimilitude from mere corroboration and does not treat a truthlikeness formula as a self-sufficient solution to induction/theory preference;
- Laudan's historical criticism blocks a simple success -> approximate truth inference.

Therefore no ready-made philosophical theorem licenses:
geometric_mean(W,N,I,T,D) = distance to truth.

## Composite-indicator audit
OECD/JRC composite-indicator methodology treats:
- weighting,
- aggregation,
- normalization,
- uncertainty,
- sensitivity analysis
as load-bearing methodological choices.

Thus a geometric mean is not self-justifying merely because it is non-additive.

## A1 — Historical hindsight rank-reversal attack
Frozen historical packets:
Newton/Mercury 1859 TPX > GR/Mercury 1915 TPX.

Yet later successor judgment contracts Newtonian final-law authority in favor of GR.

Machine:
HISTORICAL_HINDSIGHT_MONOTONICITY=REJECT.

Interpretation:
TPX tracks contemporaneous evidence-process maturity more closely than retrospective truthlikeness.

Therefore:
TPX != direct historical truth distance.

PASS against overclaim.

## A2 — Aggregator rank-reversal attack
Adversarial crossing profiles:

A=(1,1,.25,.25,.25)
B=(.5,.5,.5,.5,.5)

They are Pareto-incomparable.

Arithmetic mean selects A.
Geometric mean selects B.
Harmonic mean selects B.
Minimum selects B.

Machine:
AGGREGATOR_RANK_REVERSAL=PASS.

Therefore:
unique scalar ordering is not identified by the profile alone.

## A3 — Positive-weight underdetermination
Weighted geometric means were evaluated over a broad positive weight grid.

Different admissible positive weights yield:
A winner,
B winner,
and ties.

An additional Dirichlet(1,1,1,1,1) diagnostic with 200,000 random weight vectors gave approximately:
A winner 31.5%.
B winner 68.5%.

This Monte Carlo result is diagnostic, not itself a calibration distribution.

Machine:
WEIGHT_SENSITIVITY_REVERSAL=PASS.
PARETO_PARTIAL_ORDER=PASS.

Therefore:
without independent weight calibration, crossing profiles permit only partial ordering.

## A4 — Scalar ablation
C/E/P/R_open authority decisions were recomputed with TPX absent.

No authority promotion/HOLD decision changed.

Rivals, residue, scope, and successor shocks also remain independently represented.

Machine:
SCALAR_ABLATION_AUTHORITY_INVARIANCE=PASS.

Therefore:
TPX is not constitutive of MQR scientific authority.

## A5 — Re-encoding / profile separability
All six historical packets have C/E/P/R=PASS while W/N/I/T/D vary.

Machine:
PROFILE_SEPARABILITY_WITH_FIXED_GATES=PASS.

Thus the profile is not literal duplication of the four authority gates.

However:
current historical corpus N=6 is not adequate for independent axis calibration.

Profile-validity audit:
- D=0.75 for all six packets, so D variance=0;
- corr(W,N) ~= .894;
- corr(W,T) ~= .914;
- corr(N,T) ~= .928;
- other correlations are also non-negligible.

These are small-N diagnostics only.

Therefore:
PROFILE_FACE_VALIDITY=PASS-NARROW.
PROFILE_DISCRIMINANT_VALIDITY=HOLD.
PROFILE_EXTERNAL_CALIBRATION=HOLD.

## A6 — Synthetic truth-oracle sandbox
A toy world with known generating truth was constructed.

One claim was exactly true but evidentially young.
A second claim was false outside the observed region but assigned a mature evidence-process profile.

Oracle truth error:
true-young < false-mature.

Old TPX:
true-young < false-mature.

Machine:
SYNTHETIC_TRUTH_ORACLE_RANK_REVERSAL=PASS.
TPX_DIRECT_TRUTH_DISTANCE=REJECT.

This is sufficient to refute TPX as a general direct truth-distance metric.

It does NOT show that mature evidence processes are useless.
It shows that epistemic maturity and ontic truth distance are different variables.

## Scientific-validity judgment

### Compiler / implementation validity
PASS.
Rust and Python produce byte-identical canonical receipts.

### Authority semantics
PASS.
C/E/P/R_open remain noncompensatory gates.

### Profile face validity
PASS-NARROW.
W/N/I/T/D have explicit operational interpretations.

### Profile discriminant validity
HOLD.
Current corpus does not establish independence/nonredundancy of all axes.

### External/criterion validity to truth
NOT ESTABLISHED.

### TPX direct truth-distance validity
REJECT.

### TPX unique scalar identification
REJECT.

### TPX necessity for scientific authority
REJECT.

## Real-Language v0.2 successor semantics

Default output:

PROFILE_ORDER = PARETO_PARTIAL
SCALAR_PROJECTION_DEFAULT = OFF
FINAL_TRUTH_DISTANCE = UNIDENTIFIED

An optional geometric mean may still be requested for display/debugging, but it is labeled:

UNCALIBRATED_DISPLAY_ONLY

and cannot change authority.

The active scientific object is now:
WORLD-CONSTRAINED EVIDENTIAL PROFILE + GATES + RIVALS + RESIDUE + SCOPE + SUCCESSOR STATE.

It is not a truth percentage.

## Philosophical result
MQR can rationally say:
"This claim has stronger current world-constrained authority than that claim in these explicit respects"

without pretending to know:
"this claim is 79.4% of the way to final Truth."

This preserves fallibilist realism while refusing a fabricated oracle.

## Literature / methodology files
Verisimilitude audit:
experiments/mqr-4.28/verisimilitude-audit.md
commit f5fde65cd8702d2905ee5811789754257c9077fe

Profile discriminant-validity audit:
experiments/mqr-4.28/profile-validity-audit.md
commit 6065110d8b087571442abfa9386b5e34d5fafe5a

TPX machine tests:
experiments/mqr-4.28/tpx_validity.py
commit 184ed2d072d69a342865f0c830321e561ac8b7e0

Root live-surface promotion:
974e0d4be417f7b3096b58a2075717b967e51af4

Current doctrine finalization:
af4c9e74f2477abc8faf8dbabb029f9841e164fb

## Verdict
TRUTH-ORACLE-ABSENT /
VERISIMILITUDE-RIVALRY-AUDITED /
POPPER-STYLE-NAIVE-TRUTHLIKENESS-WARNING-RETAINED /
HISTORICAL-HINDSIGHT-MONOTONICITY-REJECT /
AGGREGATOR-RANK-REVERSAL-PASS /
POSITIVE-WEIGHT-RANK-REVERSAL-PASS /
PARETO-PARTIAL-ORDER-PASS /
SCALAR-ABLATION-AUTHORITY-INVARIANCE-PASS /
SYNTHETIC-TRUTH-ORACLE-RANK-REVERSAL-PASS /
TPX-DIRECT-TRUTH-DISTANCE-REJECT /
TPX-UNIQUE-SCALAR-IDENTIFICATION-REJECT /
TPX-SCIENTIFIC-AUTHORITY-NECESSITY-REJECT /
PROFILE-FACE-VALIDITY-PASS-NARROW /
PROFILE-DISCRIMINANT-VALIDITY-HOLD /
PROFILE-EXTERNAL-CALIBRATION-HOLD /
REAL-LANGUAGE-V0.2-PROFILE-FIRST-PASS /
RUST-CANONICAL-COMPILER-PASS /
PYTHON-INDEPENDENT-REFERENCE-PASS /
CROSS-IMPLEMENTATION-CONCORDANCE-PASS /
SCALAR-PROJECTION-DEFAULT-OFF /
FINAL-TRUTH-DISTANCE-UNIDENTIFIED /
NO-NEW-METAPHYSICAL-PRIMITIVE /
GENERATION-IV-CONTINUES.
