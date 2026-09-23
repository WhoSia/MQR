# MQR-4.15 — Governance-Independent Source/Join Compilation, Sealed Rival Packet Separation, Fresh Blind Replay & Whether Executable Transport Can Cross the Final Independence Boundary

Status: ACTIVE / EXECUTED
Date: 2026-09-24

## Sealed architecture
- source/join compiler packet cannot see rival thresholds;
- rival/scorer packet cannot see source identity;
- fresh outcome was retrieved only after sealing;
- compiler and scorer executed on different external compute surfaces;
- governance independence was adjudicated separately from runtime/provider separation.

Packet commits:
- source/join compiler: 9fade8720efe90c02c48d7ffabc099be707cb93e
- rival/scorer: 33b643164916ba07ece7d0a117cc2932dfbfaadc
- separation manifest: 652cb0c0a991aed7720e13791d67c350caab98e6

## Provider attempt
Hugging Face external compute was attempted first and failed with HTTP 402 Payment Required.
No independent-runtime claim was made from that failed lane.

## Fresh blind replay
Fresh Fingrid records after sealing:
- power interval: 2026-09-23T15:27:00Z -> 15:30:00Z
- production: 6674.65 MW
- consumption: 8601.77 MW

The source/join compiler saw no rival thresholds.
External compiler: Wolfram stateless kernel.
Frozen J_mid selected:
- midpoint: 15:28:30Z
- frequency interval: 15:27:56Z -> 15:28:56Z
- frequency: 49.9597 Hz

Masked compiler output:
- local_balance = -1927.12 MW
- frequency_deviation = -0.0403 Hz
- admission_status = PASS

The scorer saw only the masked tuple and frozen threshold contract.
External scorer: separate Firecrawl Python execution surface.

Scorer output:
STRONG_B_WITNESS_NOT_PRESENT

This is not an A-win.

## Independence adjudication
SEQUENCE-HELD-OUT:
PASS.

IDENTITY-MASKED:
PASS-NARROW for scorer.

COMPILER–SCORER CONTEXT SEPARATION:
PASS.

EXTERNAL PROVIDER SEPARATION:
PASS for Wolfram compiler vs Firecrawl scorer.

TRAINING-INDEPENDENT FRESH OUTCOME:
PASS.

RUNTIME-CONTEXT-INDEPENDENT:
PASS-NARROW.

GOVERNANCE-INDEPENDENT:
FAIL / NOT ESTABLISHED.

Reason:
the source family, admissible field ontology, J_mid join constitution, rival family, thresholds and promotion semantics were all still authorized by the same MQR research-governance process. Moving execution to different external providers changes execution dependence, not the authorship/selection dependence of the experiment constitution.

Therefore:
EXTERNAL EXECUTION INDEPENDENCE != GOVERNANCE INDEPENDENCE.

ALL-FOUR JOINT SATISFACTION:
HOLD.

## Strongest result
Executable transport can cross source, clock and provider boundaries while still failing the final governance-independence boundary.

A genuinely governance-independent test requires at minimum an independently constituted source/join/rival contract or an external adjudicating authority that can reject or alter the experiment constitution before outcome reveal.

## Verdict
SEALED-COMPILER-PACKET-PASS /
SEALED-RIVAL-PACKET-PASS /
FRESH-BLIND-REPLAY-PASS /
COMPILER-SCORER-CONTEXT-SEPARATION-PASS /
EXTERNAL-PROVIDER-SEPARATION-PASS /
HF-402-NOT-LAUNDERED /
STRONG-B-WITNESS-NOT-PRESENT /
NO-A-WIN-INFERENCE /
TRAINING-INDEPENDENT-OUTCOME-PASS /
RUNTIME-INDEPENDENCE-PASS-NARROW /
GOVERNANCE-INDEPENDENCE-NOT-ESTABLISHED /
EXTERNAL-EXECUTION-INDEPENDENCE-NOT-GOVERNANCE-INDEPENDENCE /
ALL-FOUR-JOINT-SATISFACTION-HOLD /
NO-NEW-EPISTEMIC-PRIMITIVE /
GENERATION-IV-CONTINUES.

Historical research records are canonical in Notion. GitHub experiments/ retains only the current active stage.
