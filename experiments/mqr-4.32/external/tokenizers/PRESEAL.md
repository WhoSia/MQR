# MQR-4.32 External Engineering Lane — Hugging Face Tokenizers Preseal

Status: PRESEALED / NO VERSION BEHAVIOR MEASURED

## Selection rule
Target project: huggingface/tokenizers
Lineage kind: ENGINEERING_DEVELOPMENT

Version selection is outcome-independent:
take the latest stable patch release from each of the latest three completed stable minor lines visible at preseal time.

Frozen regimes:
- A = 0.21.4
- B = 0.22.2
- C = 0.23.2

## Claim component
For a fixed WordLevel vocabulary, fixed [UNK] token, fixed Whitespace pre-tokenizer and a declared input fixture,
the observable component is the ordered token-ID sequence plus ordered token string sequence.

This is an engineering behavior claim, not implementation identity or whole-library equivalence.

## Bridge surface
Bridge fixtures: B01..B06.
Adjacent edges: A->B and B->C.
Adjacent PASS requires byte-identical canonical output for all six bridge fixtures.

If PASS, bridge class is QUOTIENT_COMPATIBLE:
only the declared encoding-output quotient is licensed.

## Direct surface
Held-out fixtures: H01..H06.
They are disjoint input worlds and are not executed by the bridge workflow.

Direct A->C workflow MUST NOT be created or executed until:
1. bridge workflow completes;
2. adjacent states are recorded;
3. MQR seals COMPOSITION_CANDIDATE yes/no and any mediated A->C prediction.

direct_surface = HELDOUT_WORLD.

## Prediction rule
If and only if A->B and B->C are both TRANSPORT_PASS:
COMPOSITION_CANDIDATE = yes
predicted heldout direct A->C state = TRANSPORT_PASS.

Otherwise COMPOSITION_CANDIDATE = no.

## Limits
Adjacent PASS does not imply API-wide, serialization-wide, source-code, performance, or future-version equivalence.

## Engineering quality
Probe implementation is Rust.
Dependency versions are exact.
Cargo.lock hashes are captured per regime.
Bridge and direct workflows are separated.
The direct workflow is absent at preseal time.

## Verdict before execution
TOKENIZERS-THREE-REGIME-LANE=PRESEALED /
DIRECT-SURFACE=HELDOUT_WORLD /
DIRECT-EXECUTION=FORBIDDEN-UNTIL-MEDIATED-SEAL /
LINEAGE=ENGINEERING_DEVELOPMENT.
