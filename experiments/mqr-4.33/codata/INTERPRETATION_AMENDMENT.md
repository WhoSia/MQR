# MQR-4.33 CODATA Diagnostic — Exact-Uncertainty Interpretation Amendment

Status: FROZEN BEFORE CODATA Z COMPUTATION

The primary preseal already fixed:

z(i,j) = |x_i - x_j| / sqrt(u_i^2 + u_j^2)

TRANSPORT_PASS iff z <= 1.

This amendment completes the mathematical semantics for historical exact values before any 4.33 CODATA z-score is computed.

## Exact-value rule

A value reported as exact has:

u = 0.

If sqrt(u_i^2 + u_j^2) > 0, use the frozen formula directly.

If both uncertainties are zero:
- equal values => z = 0;
- unequal values => z = +infinity.

No continuity correction, covariance estimate, uncertainty inflation or retrospective rescaling is permitted.

## Dependence limitation

The diagnostic intentionally ignores cross-adjustment covariance.

Therefore CODATA-DIAG tests the transitivity of the frozen naive uncertainty-agreement relation, not independence of the underlying measurements and not the epistemic independence of CODATA adjustments.

## Claim ceiling

CODATA-DIAG cannot satisfy RESEARCH_LAB confirmation.

It may reveal:
- relation-level nontransitivity;
- sensitivity to changing uncertainty geometry;
- or a stable diagnostic composition pattern.

It cannot by itself establish a scientific transport law.

## Verdict

EXACT-U=0 /
ZERO-DENOMINATOR-RULE=FROZEN /
COVARIANCE=NOT-MODELED-BY-DESIGN /
NO-POSTHOC-UNCERTAINTY-INFLATION /
CODATA-COMPUTATION=MAY-PROCEED.
