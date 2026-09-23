# MQR-4.7 — Outcome-Blind Representation Separator — PRESEAL

## Status
This file is frozen **before opening the selected held-out UIUC wind-tunnel polar values**.

The present run claims procedural outcome-blindness with respect to the specific held-out numeric record in this execution sequence. It does **not** claim pristine ignorance of all background aerodynamic knowledge, because the adjudicating model has prior training.

## Target
Low-Reynolds-number airfoil, UIUC Low-Speed Airfoil Tests.

Selected target family:
**Eppler 387 (E387)** — a classic low-Re airfoil for which UIUC experimental polar data are publicly available.

## Evidence partition
### Baseline envelope Ω0
Low-to-moderate angle of attack, below obvious stall, where both rivals can accommodate approximately linear lift growth.

No held-out high-angle numerical polar values may be inspected before this preseal is committed.

### Held-out separator Ω1
Higher angle-of-attack region approaching/passing stall at low Reynolds number.

Primary held-out observables:
- lift coefficient \(C_L\);
- drag coefficient \(C_D\);
- whether incremental lift continues approximately linearly or saturates/declines;
- whether drag rises sharply.

## Rival A — linear attached-flow representation
A deliberately reduced representation:

\[
C_L(\alpha)=a(\alpha-\alpha_0)
\]

with approximately constant slope over the extrapolated held-out range.

Qualitative frozen prediction:
- lift continues increasing approximately linearly with angle of attack over Ω1;
- no sharp stall-induced lift saturation/drop is represented;
- no mechanism-specific sharp drag escalation is predicted.

This rival is not intended as a globally realistic aerodynamic model. It is a baseline-equivalent reduced rival.

## Rival B — viscous/separation-sensitive representation
A richer qualitative representation including:
- Reynolds-sensitive boundary layer;
- transition/separation;
- finite stall onset;
- strong nonlinear drag growth near/post stall.

Frozen prediction:
- baseline low-angle lift may look approximately linear and thus mimic Rival A;
- in Ω1, \(C_L\) should depart materially from indefinite linear extrapolation, typically saturating or declining;
- \(C_D\) should increase disproportionately as separation grows.

## Separating criterion
The held-out record separates the rivals if, relative to the low-angle trend:
1. lift ceases to follow an approximately linear continuation in the high-angle region; and
2. drag rises strongly in the same regime.

Strong B win:
both conditions clearly occur.

Weak B win:
one occurs strongly and the other is ambiguous.

A survives:
lift continues approximately linearly with no strong separation-linked drag increase across the held-out range.

Inconclusive:
held-out range does not reach a genuinely separating regime or data quality is insufficient.

## Convenience control
Both rivals are evaluated against:
- the same airfoil;
- the same experimental program;
- the same type of aerodynamic coefficients;
- the same held-out measured polar.

No institutional-popularity or software-adoption criterion enters the verdict.

## Authority-update rule
Before reveal:
**SCOPED AUTHORITY — SHARED LOW-ANGLE LIFT TREND ONLY.**

If B wins:
authority may expand to the claim that viscous/separation structure is load-bearing for high-angle behavior in the tested low-Re regime.

If A survives:
no such expansion is licensed.

The full ontology of any particular viscous model is not promoted.

## Frozen limitation
Because the evaluator is a pretrained model and E387 is a known airfoil, this is a **tool-sequence held-out test**, not proof that no latent memory of the result exists.

The stronger standard of externally blinded evaluation remains separate.
