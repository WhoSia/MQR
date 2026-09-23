# MQR-4.19 — KEY B Independent Public-Provenance Verification

Status: KEY B PASS

External public-web verifier:
Exa web fetch.

The verifier independently retrieved public GitHub resources rather than relying on MQR prose alone.

## A1 — chronology
Rule-seal commit:
c44c6446dd865bb50453390981075123dbc74d76
GitHub timestamp:
2026-09-23T15:51:19Z

Fresh replay interval:
2026-09-23T15:54:00Z -> 15:57:00Z

Execution receipt commit:
7317e7ec57deccd2cfb6ada286b2d589eef17fad
GitHub timestamp:
2026-09-23T16:13:01Z

Result:
PASS.
seal < fresh interval < execution receipt.

## A2 — rule content
Pinned raw content at c44c644 independently retrieved.
It specifies:
- MIDPOINT-NEAREST SAMPLE;
- representative timestamp = frequency interval midpoint;
- tie -> earlier timestamp;
- no averaging, endpoint substitution, interpolation, or outcome-dependent fallback.

Result:
PASS.

## A3 — execution-rule identity
Pinned execution receipt at 7317e7e independently retrieved.
It cites c44c644 and executes the same midpoint-nearest rule.

Result:
PASS.

## A4 — post-seal freshness
Fresh interval begins 2 min 41 s after rule-seal commit timestamp.

Result:
PASS.

## A5 — mechanical candidate selection
Execution receipt records:
- candidate 1 midpoint 15:55:26Z, distance 4 s, 49.975 Hz
- candidate 2 midpoint 15:56:26Z, distance 56 s, 49.994 Hz

Midpoint-nearest selects candidate 1.

Result:
PASS.

## A6 — no pre-execution rule modification
Public GitHub path history for external-rule-seal.md contains:
- creation at c44c644, 15:51:19Z
- later retirement at e465a26, 16:14:18Z

There is no intervening modification commit before execution receipt 7317e7e at 16:13:01Z.

Result:
PASS.

## KEY B
A1-A6 all externally verified from public GitHub resources.

KEY B = PASS.

## Scope limit
GitHub reports the relevant commits as unsigned.
Therefore this stage establishes public chronology/content auditability but does not establish cryptographic author non-repudiation or third-party timestamp notarization.

That limitation does not violate the frozen MQR-4.19 audit contract, which required public retrievability and chronology, not signed commits.
