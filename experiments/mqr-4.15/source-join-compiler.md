# MQR-4.15 — Source/Join Compiler Packet

Role: SOURCE/JOIN COMPILER ONLY
Forbidden knowledge: rival labels, thresholds, winner semantics.

Source class:
Fingrid Open Data datasets 177, 192, 193.

Selection:
1. After this packet is sealed, take the first newly visible dataset-192 power interval whose endTime is later than 2026-09-23T06:51:00Z and for which dataset 193 has the exact same [startTime,endTime).
2. Compute midpoint t_mid.
3. From dataset 177 choose the unique frequency interval [u0,u1) with u0 <= t_mid < u1.
4. Any missing/malformed value, non-unique join, or absent match => INCONCLUSIVE.

Output ONLY:
- power_start
- power_end
- production
- consumption
- frequency_start
- frequency_end
- frequency
- local_balance = production-consumption
- frequency_deviation = frequency-50.00
- admission_status

No rival or scoring interpretation is allowed.
