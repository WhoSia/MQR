# MQR-4.80 — Independent Oracle

Status: **INDEPENDENT EXPECTATION ORACLE / NO CANONICAL LOGIC IMPORT**

The frozen 16 cases are independently mapped by case identity to expected authority state.

| Case | State |
|---|---|
| N1 | PROVENANCE_PRESERVING_PARTIAL_GLUE |
| N2 | INTERSECTION_LAUNDERING |
| N3 | UNION_LAUNDERING |
| N4 | TRANSLATION_LAUNDERING |
| N5 | OBLIGATION_LOSS |
| N6 | NO_JOINT_AUTHORITY |
| N7 | OVERLAP_ONLY_AUTHORITY |
| N8 | REOPEN_HIDDEN_NONOVERLAP |
| M1 | PROVENANCE_PRESERVING_PARTIAL_GLUE |
| M2 | OBLIGATION_LOSS |
| M3 | OBLIGATION_INVENTION |
| M4 | TRANSLATION_LAUNDERING |
| M5 | CONFLICT_PRESERVED |
| C1 | INTERSECTION_LAUNDERING |
| C2 | OVERLAP_ONLY_AUTHORITY |
| C3 | OBLIGATION_LOSS |

This oracle is deliberately implementation-independent from the canonical classifier. It checks the frozen case identities and states rather than reusing the Rust decision tree.

Required agreement: 16 / 16.
