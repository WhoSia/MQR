# MQR-4.15 — Sealed Rival/Scorer Packet

Role: SCORER ONLY
Forbidden knowledge: source identity, dataset IDs, descriptive engineering context.

Input:
- local_balance [MW]
- frequency_deviation [Hz]
- admission_status

If admission_status != PASS => INCONCLUSIVE.

Frozen strong-B witness:
- abs(local_balance) >= 100
- AND abs(frequency_deviation) <= 0.01

Output exactly one of:
- STRONG_B_WITNESS_PRESENT
- STRONG_B_WITNESS_NOT_PRESENT
- INCONCLUSIVE

STRONG_B_WITNESS_NOT_PRESENT is NOT an A-win.
