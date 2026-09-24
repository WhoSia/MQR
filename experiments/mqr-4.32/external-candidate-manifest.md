# MQR-4.32 — External Candidate Manifest

Status: PRE-REVEAL / CANDIDATE AND EXCLUSION SET FROZEN

## Confirmatory selected

### TKN-001 — Hugging Face tokenizers version composition
Lineage: ENGINEERING_DEVELOPMENT
Regimes: 0.21.4 -> 0.22.2 -> 0.23.2
Direct surface: HELDOUT_WORLD
Bridge fixtures: B01..B06
Direct fixtures: H01..H06
Preseal blob: 7ab9c167a113e3f8412f98b00127a4d61ead5379
Vocabulary blob: f4a9ad55dc41607eb84f002525ed9cf536f7c515
Probe source blob: 3b03212ad52689187805b7955054689daf344eb6

Admission:
SELECTED.

Reason:
the direct A->C fixture set is disjoint from the adjacent-edge bridge fixture set and direct execution is prohibited until a mediated seal is written.

## Diagnostic / non-confirmatory

### EPI-P35
Lineage: RESEARCH_LAB
Canonical candidate run: 36032390165
Noncanonical duplicate run: 36032383918

Admission:
DIAGNOSTIC_ONLY under current design.

Reason:
the existing P35 analysis->sample adjacent comparison and anchor->sample direct comparison consume the same sample endpoint. Under MQR-4.32 Amendment A this does not provide an independent direct surface. A selective field reveal is insufficient if the adjacent verdict logically reuses/determines the direct endpoint.

No P35 native result may change this admission status.

### HWPX-P316
Lineage: ENGINEERING_DEVELOPMENT
Source surface:
p316_version_indexed.py / p316_stability_builder.py
Structural fact:
at least three fresh repetitions are supported.

Admission:
DIAGNOSTIC_ONLY.

Reason:
three repetitions provide an A/B/C regime sequence, but pairwise A->B, B->C and A->C comparisons over the same repetition records do not by themselves provide a held-out/noncommon direct surface. Native artifact custody needed for a stronger design is not present on the current repository surface.

ChatGPT-Web-HWPX-MCP remains ENGINEERING_DEVELOPMENT, not RESEARCH_LAB.

### C3X-P19
Lineage: RESEARCH_LAB

Admission:
EXCLUDED_FROM_FRESH_CONFIRMATION.

Reason:
candidate discovery exposed outcome-bearing commit-message text before an MQR-4.32 mediated seal. It may be used only as later diagnostic/stress material.

## Cross-lineage consequence

At this pre-reveal point:
- admissible ENGINEERING_DEVELOPMENT confirmatory lane: available (TKN-001);
- admissible RESEARCH_LAB confirmatory lane: none.

Therefore FULL MQR-4.32 external cross-lineage promotion cannot PASS on the currently admitted corpus.

This ceiling is frozen before TKN-001 bridge/direct reveal and before P35 native completion.

A future stage may create a genuinely held-out/noncommon research triangle. MQR-4.32 will not weaken direct-surface independence to obtain a PASS.

## Frozen status

CURRENT_EXTERNAL_PROMOTION_CEILING=HOLD /
TKN-001=SELECTED /
EPI-P35=DIAGNOSTIC-ONLY /
HWPX-P316=DIAGNOSTIC-ONLY /
C3X-P19=EXCLUDED-LEAKAGE /
RESEARCH-LAB-CONFIRMATORY-SURFACE=ABSENT.
