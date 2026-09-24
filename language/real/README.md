# Real-Language / Real-Packet v0.2

Real-Language is MQR's active event-to-realist-authority language.

It compiles a scientific event, claim, anomaly, historical receipt, or successor shock into a scoped authority packet.

## Why "Real-Language"

The former name "R-Language" was retired to avoid confusion with the statistical programming language R.

## Profile-first semantics

Real-Language v0.2 does **not** output a default scalar "truth score".

It outputs:

1. Authority gates
   - C: constitutional/adjudication legitimacy
   - E: admissible world-contact
   - P: provenance/time/auditability
   - R: open-world rival invariance

2. Evidence profile
   - W: world resistance
   - N: noncommon evidence-route strength
   - I: rival invariance / identification
   - T: declared-scope transport **(legacy v0.2 field; MQR-4.30 shows this construct requires successor decomposition into transport target/evaluability/survival)**
   - D: defeat exposure / corrigibility

3. Residue
   - rivals
   - generator provenance
   - adverse observations
   - mystery / ontic reserve
   - successor vulnerability

## Calibration status

MQR-4.29 promotes W/N/I/T/D to **LEVEL-2 internally calibrated operational indices**.

Prospective calibration:
- 243 exact full-factorial worlds;
- 243 noisy blind worlds;
- hidden-key reveal only after scoring;
- matched single-axis interventions;
- decoy attacks;
- Rust/Python scorer concordance.

Canonical results:
- exact recovery: PASS;
- cross-axis leakage in exact lane: 0;
- noisy self-axis r: 0.973079–0.976977;
- max nonmatching hidden-axis |r|: 0.022682;
- max measured-axis |r|: 0.038496;
- decoy mutations: 2430 cells;
- decoy-induced profile changes: 0.

Interpretation ceiling after MQR-4.30:

```text
W = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL INDEX
I = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL INDEX
N = LEVEL-2 RETAINED / LEVEL-3 EXTERNAL HOLD
T = LEVEL-2 RETAINED-WITH-WARNING / LEVEL-3 EXTERNAL HOLD
D = LEVEL-2 RETAINED / EXTERNAL POLARITY PASS / LEVEL-3 RANGE HOLD
INTERVAL SCALE = HOLD
TRUTH-DISTANCE METRIC = NOT ESTABLISHED
```

MQR-4.30 used label-blind scoring against independent non-MQR research constitutions and obtained 29/32 exact directional agreements. W matched 8/8 and I 7/7 across four external domains. T matched only 5/8 and is now known to conflate at least transport target, transport evaluability, and transport survival. D matched 9/9 but the external sample contained only HIGH-D cases, so discriminant calibration is range-restricted. N passes the anti-counting test but lacks cross-domain external criterion coverage.

The profile values remain construct-relative indices. Only W and I currently possess external ordinal calibration; numeric differences are not licensed as equal epistemic intervals across domains.

## Scalar policy

The v0.1 TPX geometric mean is demoted.

Reason:
- historical rank reversal shows contemporaneous epistemic maturity is not retrospective truthlikeness;
- crossing profiles can reverse rank under arithmetic, geometric, harmonic, minimum, or different positive weights;
- authority decisions are invariant when TPX is removed;
- a controlled truth-oracle toy world can contain a true but young claim with lower TPX than a mature false claim.

Therefore:

```text
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
SCALAR_PROJECTION_DEFAULT = OFF
ORDERING = PARETO_PARTIAL + EXPLICIT_PROFILE
```

A scalar may be requested only as an explicitly uncalibrated display projection. It never changes authority.

## Canonical implementation

- Rust: canonical compiler
- Python: independent reference compiler

CI requires byte-identical canonical receipts on the frozen packet corpus.

Implementation language is not an epistemic primitive.

## Packet grammar

```text
REALPACKET 0.2
id "packet-id"
epoch "epoch"
claim CONSTRAINT "claim text"
scope "licensed scope"

gate C PASS
gate E PASS
gate P PASS
gate R PASS

axis W 0.75 "why"
axis N 0.50 "why"
axis I 0.75 "why"
axis T 0.50 "why"
axis D 0.75 "why"

generator STRUCTURAL "description"
rival SURVIVING "description"
residue MODERATE "description"
mystery OPEN "description"
ontic HOLD "description"
successor VULNERABLE
shock "later epoch" CONTRACT "description"
source "source pointer"
END
```

## Interpretation rule

If any C/E/P/R gate is not PASS:
authority = HOLD.

If all gates PASS:
authority = SCOPED_REALIST_AUTHORITY.

No scalar can compensate for a failed gate.

Even when authority passes:
OPEN_WORLD_RESIDUE = true
FINAL_TRUTH_DISTANCE = UNIDENTIFIED

Real-Language is allowed to compress bookkeeping.
It is not allowed to manufacture a truth oracle.
