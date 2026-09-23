# MQR-4.18 — KEY A Mechanical Execution Receipt

Status: KEY A PASS

Externally selected rule:
MIDPOINT-NEAREST SAMPLE
sealed at commit:
c44c6446dd865bb50453390981075123dbc74d76

Fresh matched power interval:
2026-09-23T15:54:00Z -> 15:57:00Z

Production:
6858.44 MW

Consumption:
8626.18 MW

Power midpoint:
2026-09-23T15:55:30Z

Frequency candidates within same interval:
1. 15:54:56Z -> 15:55:56Z, value 49.975 Hz, representative midpoint 15:55:26Z, distance 4 s
2. 15:55:56Z -> 15:56:56Z, value 49.994 Hz, representative midpoint 15:56:26Z, distance 56 s

Externally selected rule therefore chooses candidate 1.

Selected frequency:
49.975 Hz

Derived:
local_balance = 6858.44 - 8626.18 = -1767.74 MW
frequency_deviation = 49.975 - 50.00 = -0.025 Hz

Frozen strong-B separator:
abs(local_balance) >= 100 MW: PASS
abs(frequency_deviation) <= 0.01 Hz: FAIL

Mechanical verdict:
STRONG_B_WITNESS_NOT_PRESENT

This is not an A-win.

No averaging, endpoint substitution, interpolation, alternate source, or post-outcome repair was used.

KEY A = PASS.
