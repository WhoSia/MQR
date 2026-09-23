# MQR-4.9 — Sealed-Source Representation Test — PRESEAL

## Source class
Live electricity-grid telemetry generated at/near evaluation time from Estonia's transmission-system operator Elering, accessed through a public API/dashboard relay.

The exact current frequency / production / consumption / system-balance values must not be opened before this preseal commit.

Because the telemetry timestamp is generated after model training, the specific held-out numeric outcome cannot have been memorized during pretraining.

## Engineering target
Short-timescale relation between active-power imbalance and synchronous-grid frequency deviation.

## Rival A — balance-sensitive electromechanical representation
Qualitative claim:
- if instantaneous generation exceeds load/export-adjusted demand, frequency pressure is upward;
- if load exceeds generation, frequency pressure is downward;
- control reserves and interconnection may attenuate or reverse simple one-step correspondence, so only directionally consistent deviations within a tolerance are expected.

Frozen prediction:
sign(system imbalance) should have the same sign as frequency deviation from 50 Hz more often than not in the same telemetry snapshot, unless balancing/interchange terms or control action dominate.

## Rival B — frequency-decoupled snapshot representation
Qualitative claim:
the contemporaneous system-balance sign carries no directional information about frequency deviation once the grid is synchronized; current frequency may be above or below 50 Hz independently of the local balance sign.

Frozen prediction:
no sign-consistency requirement between local system balance and f-50 Hz.

## Separator
Reveal one current Elering telemetry snapshot containing at least:
- grid frequency f;
- production;
- consumption;
- system balance or equivalent net-balance quantity.

Strong A-consistent outcome:
sign(balance) = sign(f-50 Hz), with both values non-negligibly away from zero/50 within published precision.

Weak / inconclusive:
- either quantity is effectively zero within display precision;
- sign conventions are ambiguous;
- system balance includes cross-border/interchange terms not aligned with the frozen interpretation;
- timestamp mismatch exceeds the source update interval.

B-compatible outcome:
clear opposite signs under unambiguous conventions.

## Authority rule
A single snapshot cannot establish the full swing equation, inertia, droop constants, or causality.

If A-consistent:
authority may expand only to SCOPED SUPPORT that current balance and frequency deviation are directionally coupled in this live operating state.

If B-compatible:
the simple snapshot-coupling claim is defeated or requires missing state/interchange/control variables.

## Blindness labels frozen before reveal
- SEQUENCE-HELD-OUT: required.
- IDENTITY-MASKED: NO; source family is known.
- CONTEXT-INDEPENDENT: NO; same conversation/compiler.
- TRAINING-INDEPENDENT OUTCOME: candidate YES because the exact live telemetry is generated post-training, but source plumbing itself is public.

## Fatal honesty constraint
No claim of compiler-adjudicator context separation will be made in this run.
4.9 tests whether source freshness can solve latent outcome-memory leakage even when context independence remains absent.