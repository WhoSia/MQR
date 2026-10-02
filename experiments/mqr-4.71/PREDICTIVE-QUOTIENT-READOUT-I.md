# MQR-4.71 — Predictive Quotient Readout I

Status: **ORIGINAL-EXPECTATION-FAILED / MINIMAL-FEATURE-COUNT-4 / PROXY-ALIASING-DETECTED / ORIGINAL-FREEZE-PRESERVED**

## Frozen result

The first generative-state quotient attack expected a unique minimal feature set:

`generators + tech_state + budget_state + ethics_state`

The exact run falsified uniqueness.

Observed:

```text
RAW_STATES = 6
PREDICTIVE_CLASSES = 5
MINIMAL_FEATURE_COUNT = 4

MINIMAL FEATURE SETS:
1. generators,tech_state,budget_state,ethics_state
2. tech_state,budget_state,ethics_state,ancestry_label
```

Therefore:

```text
CURRENT_ENVELOPE_DROPPED = YES
REVISION_STATE_DROPPED = YES
ANCESTRY_DROPPED = NO ON THE ORIGINAL FROZEN SAMPLE
```

## Interpretation

This does **not** establish ancestry as causally necessary.

In the original six-state sample:
- the THEORY-only state uniquely carries `PATH_A`;
- plural-generator states carry `PATH_B` or `PATH_C`.

Therefore ancestry label can act as a predictive proxy for generator capability.

The original sample is insufficient to identify which of the two minimal representations is structurally transportable.

## Scientific consequence

The previous statement:

`FULL ANCESTRY IS UNNECESSARY`

remains supported by the explicit ancestry-null pair S_PLURAL / S_PLURAL_ALT, but the stronger statement:

`ANCESTRY CAN BE DROPPED FROM EVERY MINIMAL PREDICTIVE REPRESENTATION`

is **not earned on the original freeze**.

## Ruling

**FROZEN-SAMPLE-PROXY-ALIASING / UNIQUE-MINIMAL-STATE-HOLD**

The failed expectation is retained as a scientific result.

A second prospective Court may break the generator↔ancestry correlation, but it must use a new freeze and must not rewrite the original table.
