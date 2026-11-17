# MQR 5.4 — A paired order test with drift and a preparation reversal

2026-11-17 KST

## What this test adds

[The readout study](mqr_54_readout_identifiability_results.md) assumed a stable detector. This design allows time-dependent additive offset and multiplicative gain on a stable response curve within a block. It also makes a directional prediction for each of two independently prepared input polarizations. A rescheduling artifact can reverse an apparent order effect, so time balance is part of the empirical test of a translation claim.

Let A place a lossless retarder before a horizontal polarizer, and B place the same elements in the opposite order, with polarization-insensitive total transmitted power readout. Use one wavelength appropriate to the retarder. Write p and s for the polarizer's parallel and orthogonal intensity transmissions and q for the fraction of an input basis polarization rotated into the orthogonal component. With retarder axis theta and retardance delta, the Jones result is q = sin²(2 theta) sin²(delta/2). This yields, for unit incident intensity:

| Preparation | A | B | A − B |
|---|---:|---:|---:|
| Horizontal | p(1 − q) + sq | p | −q(p − s) |
| Vertical | s(1 − q) + pq | s | +q(p − s) |

Finite polarizer leakage and incomplete rotation shrink the contrast while keeping the sign reversal for p > s and q > 0. A lossless retarder whose axis is aligned to H/V gives q = 0 and is the zero-effect control. Fixed detector gain, unrelated throughput and physical shifts introduced by moving optics are separate considerations. If the swap changes the illuminated detector area or optical throughput independently of the Jones operators, this derivation alone cannot assign the observed difference to the operators.

## Time balance and an exact adverse case

Use Y(t) = a(t) + g(t) f(I) + e(t), with the same stable basic response f for both conditions, positive g, and a(t) and g(t) depending on time and not on the condition. For each condition, compute the mean of its measurements and subtract mean B from mean A. If the A and B timestamps have equal averages of powers 0 through d, all offset terms up to degree d cancel and the gain terms yield the same positive mean gain multiplying f(I_A) − f(I_B). A monotone detector may still hide a genuine difference when its response is flat.

- With evenly spaced readings, ABBA balances moments through degree 1.
- ABBABAAB balances moments through degree 2. Its A indices are 0, 3, 5, 6 and B indices are 1, 2, 4, 7. Both sums are 14 and both sums of squares are 70. Cubic moment imbalance is −12 in sample-index units.
- For A = 0 and B = 1 with additive offset t² and unit gain, the true contrast −1 appears as +1 under ABBA and returns to −1 under ABBABAAB. Uneven timestamps can leave a nonzero drift term even in the intended block, so record actual acquisition times. The code checks all balanced equal-weight designs of lengths 2, 4, 6 and 8. Only the eight-reading pattern and its complement satisfy the quadratic constraints in this family.

Offset-drift cancellation is standard in metrology; the eight-reading sequence is the order-three Prouhet–Thue–Morse split. Sutton and Clarkson explicitly discuss gain drift and higher polynomial orders in comparisons. [NIST drift guidance](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc3312.htm) · [Sutton and Clarkson, temporal drift](https://doi.org/10.1088/0026-1394/30/5/004) · [Prouhet–Thue–Morse construction](https://arxiv.org/abs/1411.6168). The implementation computes the balance from recorded times instead of assuming every planned delay was respected.

## Acquisition and decision

1. Establish horizontal and vertical input preparations using a separate analyzer. Check blocked, unblocked and one stable intermediate optical reference independently of A/B. Use a detector with fixed settings and check for saturation at the chosen wavelength. Keep beam geometry and module positions fixed, and control source output across preparations.
2. Record each preparation in an independent eight-reading block, balancing the complement and preparation order across blocks where practical. Reserve evenly spaced acquisition slots even if the reconfiguration takes different amounts of time. Place reference checks before and after the block, or interleave them only if the actual A/B timestamps still meet the balance or the imbalance is included in the error budget. Save block, preparation, physical order, timestamp, raw reading, detector setting and any overload or rejected reading.
3. Predeclare a minimum meaningful separation and a residual uncertainty budget. If every reading's remaining deviation is bounded by epsilon, the unweighted difference of condition means has worst-case residual at most 2 epsilon. The budget must include imperfect time balance, scatter and effects seen in the references. To support the operator-order account, seek a negative H contrast and positive V contrast with margins outside that budget, plus a small contrast under the zero-mixing control. If the calibrated range or accessible separation cannot establish a sign, record the result as unresolved.

The physical near-neighbor Procopio et al. (2015) did control polarization-gate order using a single-photon interferometer. That paper reports both time drift and phase changes when waveplates were physically rotated. Its main text and supplement describe photon-pair counts, interference and waveplate settings, and give no verified independent dark/full/intermediate reference record for the same two-order intensity test defined here. The previous Rivera-Ortega data give single-configuration intensity readings. A public paired reference-and-order intensity log for these predictions was not located. [Procopio et al.](https://doi.org/10.1038/ncomms8913) · [Supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fncomms8913/MediaObjects/41467_2015_BFncomms8913_MOESM716_ESM.pdf).

[Real-Lang exploratory implementation](../language/real/experiments/polarization_order_v54.py) · [Regression tests](../language/real/experiments/test_polarization_order_v54.py). Eight new tests passed and the full local Python experiment suite passed 99 tests. The finite results include a separate complex Jones-matrix calculation and an exhaustive search over the stated time-grid family. No new optical measurements were made.
