# MQR-4.70 — Stochastic Closure Court Constitution

Status: **PRE-RESULT / STOCHASTIC-SEPARATION-TEST / BLACKWELL-BASELINE-PRIMARY**

## Purpose

The deterministic finite Court caused:
- C1 and C3 to coincide;
- C2 and C4 to coincide.

MQR-4.70 must not retain a multi-level closure hierarchy unless a non-artificial statistical setting separates the levels.

## Parameter space

Theta = {0,1}.

## Current experiment E

Binary outcome Y in {0,1}:

- P(Y=1 | theta=0) = 0.25
- P(Y=1 | theta=1) = 0.75

The two parameter values are observationally distinguishable under E.

Therefore the E-induced parameter partition is discrete.

## Exterior experiment F

Binary outcome Z in {0,1}:

- P(Z=1 | theta=0) = 0.10
- P(Z=1 | theta=1) = 0.90

F does not refine the exact parameter-equivalence partition because E already distinguishes theta=0 from theta=1.

But F may contain strictly more decision-relevant information.

## Frozen questions

Q1. Does parameter-partition closure hold for E relative to {E,F}?

Expected: YES, because E already yields distinct distributions for the two parameter values.

Q2. Is F a garbling of E?

Expected: NO.

For a binary channel K with:
- a = P(Z=1 | Y=0)
- b = P(Z=1 | Y=1),

garbling E into F would require:

0.75 a + 0.25 b = 0.10
0.25 a + 0.75 b = 0.90

whose unique solution is a=-0.30, b=1.30, outside [0,1].

Therefore exact Blackwell domination should fail.

Q3. Does this separate partition closure from Blackwell closure?

Expected: YES.

## Control experiment G

Binary outcome W:

- P(W=1 | theta=0) = 0.40
- P(W=1 | theta=1) = 0.60

Expected: G is a garbling of E.

Solving:

0.75 a + 0.25 b = 0.40
0.25 a + 0.75 b = 0.60

gives a=0.30, b=0.70, a valid stochastic kernel.

## Authority consequence

If the Court passes:

    PARAMETER PARTITION CLOSURE
    !=
    BLACKWELL EXPERIMENT CLOSURE

This justifies retaining a distinction between:
- C3: no new exact parameter/model distinctions under the declared exterior family;
- C4: no new decision-relevant information under the declared decision-theoretic comparison.

It does not justify C6 open-world closure.

## Novelty boundary

This is classical statistical-experiment theory.

A PASS earns zero new mathematical novelty.

Its role is calibration of MQR's authority typing.
