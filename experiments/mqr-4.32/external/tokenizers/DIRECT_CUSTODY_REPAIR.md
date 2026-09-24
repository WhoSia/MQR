# MQR-4.32 TKN-001 — Direct Receipt Custody Repair

Status: POST-ADJUDICATION CUSTODY REPAIR / SCIENTIFIC RESULT UNCHANGED

## Canonical direct execution

Workflow run:
36035751815

Trigger SHA:
56d8ba62471fbd1d62c541183ef91c90c2fa0462

Mediated prediction seal:
b03c31531d8eca42f5b567d6ffbe94164fad5371

The workflow preflight verified the mediated seal before running the held-out direct fixtures H01..H06.

Both version jobs completed successfully:
- A = tokenizers 0.21.4
- C = tokenizers 0.23.2

The direct adjudication step completed successfully and emitted:

- predicted_direct_A_TO_C = TRANSPORT_PASS
- observed_direct_A_TO_C = TRANSPORT_PASS
- path_class = COMMUTES_AT_CLAIM_QUOTIENT
- composition_state = COMPOSITION_PASS

The adjudication artifact is retained by GitHub Actions as:
- artifact name: tokenizers-direct-adjudication
- artifact id: 10825046164
- artifact digest: sha256:cad4723d76d527de033bc648ee26790d19bedb8e678bfd307d80512b8225de5b

Version artifacts:
- 0.21.4 artifact id 10825071154, digest sha256:f6e54f1424f78e64943e2887424eeb7eeac086d98a9257e9847dc4c47acf3ff9
- 0.23.2 artifact id 10824681316, digest sha256:82502cdb69de578e62b3179bd6bf73e450ea7718a3dadb9577671eb408c35ff0

## Why the workflow run is red

The scientific adjudication did not fail.

After adjudication, the workflow created a local commit:

843d89c — MQR-4.32: persist canonical tokenizers direct receipt [skip ci]

but the final `git push` was rejected because main had advanced concurrently when the research-engineering standard update was committed.

The failure was:

main -> main (fetch first)

Therefore the workflow-level conclusion is failure for an evidence-custody race after successful execution and adjudication.

## Recovery

The exact adjudication fields were recovered from the canonical workflow log and persisted without changing any scientific field at:

receipts/mqr-4.32/tokenizers-direct.tsv

Recovery commit:
8f48f9030126a88a397680788874da9455ea97b3

No direct result, prediction, path class, fixture, version or criterion was changed during recovery.

## Methodological consequence

A red CI run is not itself a scientific failure type.

MQR must distinguish at least:
- setup/build failure;
- world-contact execution failure;
- semantic/adjudication failure;
- evidence-persistence/custody failure.

This incident is a custody failure after successful world-contact and adjudication.

## Verdict

TKN-001-DIRECT-EXECUTION=PASS /
TKN-001-DIRECT-ADJUDICATION=PASS /
TKN-001-COMPOSITION=COMPOSITION_PASS /
WORKFLOW-FINAL-STATUS=FAIL-DUE-TO-CUSTODY-PUSH-RACE /
SCIENTIFIC-RESULT=UNCHANGED /
RECOVERED-RECEIPT=BOUND.
