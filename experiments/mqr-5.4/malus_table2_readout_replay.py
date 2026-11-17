"""Recalculate descriptive diagnostics from Rivera-Ortega et al. (2025), Table 2.

Source: https://doi.org/10.3390/physics7040067
The rows transcribe the measurements printed in the article. They are not
instrument log files or a two-device validation set.
"""

from fractions import Fraction
from math import cos, radians
from statistics import pstdev, stdev

ROWS = (
    (0, (60, 60, 60, 60, 60), 0),
    (15, (54, 53, 53, 56, 56), 1.24),
    (30, (44, 41, 43, 43, 44), 1),
    (45, (28, 26, 28, 28, 28), 0.73),
    (60, (16, 15, 16, 19, 19), 1.53),
    (75, (6, 6, 6, 9, 9), 1.34),
    (90, (3, 2, 2, 2, 3), 0.45),
)


if __name__ == "__main__":
    means = [Fraction(sum(row), len(row)) for _, row, _ in ROWS]
    low, high = means[-1], means[0]
    print("angle,min,max,mean,endpoint_scaled,residual,population_sd,sample_sd,printed_sd")
    for (angle, row, printed_sd), mean in zip(ROWS, means, strict=True):
        scaled = (mean - low) / (high - low)
        residual = float(scaled) - cos(radians(angle)) ** 2
        print(f"{angle},{min(row)},{max(row)},{float(mean):.3f},{float(scaled):.6f},"
              f"{residual:.6f},{pstdev(row):.6f},{stdev(row):.6f},{printed_sd}")
    print("All adjacent observed ranges disjoint in predicted order:",
          all(min(a) > max(b) for (_, a, _), (_, b, _) in zip(ROWS, ROWS[1:])))
