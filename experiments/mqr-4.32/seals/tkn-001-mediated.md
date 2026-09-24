# MQR-4.32 TKN-001 — Mediated Composition Seal

Status: SEALED BEFORE DIRECT A->C EXECUTION

## Bound evidence

Canonical bridge execution:
- run: 36035350447
- trigger SHA: 81800ebcd46e7f8a4ea6eb5482de8401909b9cdd
- persisted receipt commit: 1fcc5477c251a6cbdcada348581e2d9d3fce1507
- receipt blob: f615315dc2072e7437d0eb41341834242c888982

Frozen regimes:
- A = tokenizers 0.21.4
- B = tokenizers 0.22.2
- C = tokenizers 0.23.2

Frozen component:
ordered token-ID sequence plus ordered token-string sequence for the declared WordLevel + [UNK] + Whitespace behavior.

## Adjacent states

A -> B:
TRANSPORT_PASS.

B -> C:
TRANSPORT_PASS.

Bridge class A -> B:
QUOTIENT_COMPATIBLE.

Bridge class B -> C:
QUOTIENT_COMPATIBLE.

The bridge classification licenses only the declared encoding-output quotient. It does not establish library, source, serialization, performance, API, or ontological equivalence.

Intermediate state compatibility:
PASS at the declared quotient.

Downstream required distinctions preserved:
YES at the declared quotient.

## Mediated adjudication before direct reveal

COMPOSITION_CANDIDATE:
YES.

Mediated target:
the same declared encoding-output quotient at C for held-out fixtures H01..H06.

Predicted direct A -> C state:
TRANSPORT_PASS.

Predicted path-congruence class:
COMMUTES_AT_CLAIM_QUOTIENT.

This is a prospective prediction, not a conclusion from A -> C evidence.

## Direct lock

At the time of this seal:
DIRECT_A_TO_C = NOT_EXECUTED.

The direct surface is the previously frozen, disjoint H01..H06 held-out fixture set.

No field above may be edited after direct execution. A failed direct test must remain a NONTRANSITIVITY_WITNESS; a passing direct test can earn only scoped COMPOSITION_PASS at the declared quotient.

## Promotion ceiling inherited from the external candidate manifest

Even if TKN-001 directly passes, full MQR-4.32 external promotion remains HOLD unless the already-presealed minimum corpus requirements are satisfied.

In particular, the current 4.32 confirmatory corpus lacks an admissible RESEARCH_LAB three-regime triangle and contains fewer than six confirmatory triangles.

## Seal verdict

TKN-001-COMPOSITION-CANDIDATE=YES /
MEDIATED-A-C-PREDICTION=TRANSPORT_PASS /
EXPECTED-PATH=COMMUTES_AT_CLAIM_QUOTIENT /
DIRECT-A-C=SEALED-UNOPENED /
NO-GLOBAL-EQUIVALENCE /
FULL-MQR432-PROMOTION-CEILING=HOLD.
