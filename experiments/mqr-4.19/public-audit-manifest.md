# MQR-4.19 — Public Audit Manifest

Status: PUBLICLY AUDITABLE PROVENANCE CHAIN

## Immutable public anchors
Rule seal commit:
https://github.com/WhoSia/MQR/commit/c44c6446dd865bb50453390981075123dbc74d76
Timestamp: 2026-09-23T15:51:19Z

Pinned rule content:
https://raw.githubusercontent.com/WhoSia/MQR/c44c6446dd865bb50453390981075123dbc74d76/experiments/mqr-4.17/external-rule-seal.md

Fresh execution receipt commit:
https://github.com/WhoSia/MQR/commit/7317e7ec57deccd2cfb6ada286b2d589eef17fad
Timestamp: 2026-09-23T16:13:01Z

Pinned execution content:
https://raw.githubusercontent.com/WhoSia/MQR/7317e7ec57deccd2cfb6ada286b2d589eef17fad/experiments/mqr-4.18/key-a-execution.md

Rule-path public history:
https://api.github.com/repos/WhoSia/MQR/commits?path=experiments/mqr-4.17/external-rule-seal.md&per_page=20

## Auditable chronology
1. External midpoint-nearest rule sealed at 15:51:19Z.
2. Fresh replay interval begins at 15:54:00Z and ends at 15:57:00Z.
3. Execution receipt committed at 16:13:01Z.
4. Rule-path history contains creation at c44c644 and later retirement at e465a26 after execution; no intervening modification commit exists before 7317e7e.

## Auditable rule identity
The pinned rule:
- requires midpoint-nearest selection;
- defines each frequency interval by its midpoint;
- tie -> earlier timestamp;
- no averaging, endpoint substitution, interpolation, or outcome-dependent fallback.

The pinned execution:
- cites the same rule-seal commit;
- uses midpoint 15:55:30Z;
- compares candidate representative midpoints 15:55:26Z and 15:56:26Z;
- selects the 4-second candidate, 49.975 Hz;
- records no post-outcome repair.

## Frozen MQR-4.19 audit criteria
A1 chronology verified.
A2 rule content verified.
A3 execution-rule identity verified.
A4 fresh interval later than seal verified.
A5 candidate selection mechanically verified.
A6 no pre-execution rule modification verified.

If A1-A6 are all externally verifiable from public GitHub resources:
KEY B = PASS.
Otherwise:
KEY B = HOLD.
