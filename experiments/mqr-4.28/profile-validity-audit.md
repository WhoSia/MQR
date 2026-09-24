# MQR-4.28 — Profile Discriminant-Validity Audit

Frozen historical corpus:
- H. pylori early
- H. pylori causal consolidation
- GR 1915
- Newton/Mercury 1859
- Ozone 1985
- Ozone 1986

Axes:
W, N, I, T, D.

## Variance result

D is 0.75 in all six packets.

Therefore:
D variance = 0 in the current historical corpus.

The corpus cannot empirically discriminate or calibrate D.

## Pairwise correlation diagnostic

Using the six frozen profiles:

- corr(W,N) ~= 0.894
- corr(W,I) ~= 0.800
- corr(W,T) ~= 0.914
- corr(N,I) ~= 0.447
- corr(N,T) ~= 0.928
- corr(I,T) ~= 0.581
- correlations with D are undefined because D has zero variance.

These values are diagnostics only.
N=6 is far too small and deliberately selected for historical replay, so they are not population estimates.

## Interpretation

The profile is not literal duplication of the C/E/P/R gates:
the gates are fixed PASS while profile coordinates vary.

However the current corpus does NOT establish:
- orthogonality of W/N/I/T/D;
- discriminant validity of all five coordinates;
- stable weights;
- interval-scale measurement;
- calibrated distance to an external truth state.

Therefore:

PROFILE_FACE_VALIDITY = PASS-NARROW.
PROFILE_DISCRIMINANT_VALIDITY = HOLD.
PROFILE_EXTERNAL_CALIBRATION = HOLD.

W/N/I/T/D remain useful typed diagnostics, not a validated psychometric-style scale.

## Successor requirement

A future calibration stage should use a larger prospective packet set deliberately crossing the axes:
- high W / low N,
- low W / high N,
- high I / low T,
- high T / low I,
- high D / low W,
- low D / otherwise mature,
and include known synthetic or externally adjudicated outcomes where a domain-specific target metric is available.

No scalar promotion is permitted before that calibration.
