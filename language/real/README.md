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
   - T: declared-scope transport
   - D: defeat exposure / corrigibility

3. Residue
   - rivals
   - generator provenance
   - adverse observations
   - mystery / ontic reserve
   - successor vulnerability

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
