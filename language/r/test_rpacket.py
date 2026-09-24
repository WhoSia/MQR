#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import math

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("rpacket", HERE/"rpacket.py")
rpacket=importlib.util.module_from_spec(spec)
spec.loader.exec_module(rpacket)

EXAMPLES=sorted((HERE/"examples").glob("*.rpacket"))
assert len(EXAMPLES) >= 6

compiled=[rpacket.parse(p) for p in EXAMPLES]

for p in compiled:
    assert p["open_world_residue"] is True
    assert p["compiler_invariants"]["hindsight_firewall"] is True
    assert p["authority"]["state"] == "SCOPED_REALIST_AUTHORITY"
    assert p["truth_proximity"]["TPX"] is not None
    assert 0 <= p["truth_proximity"]["TPX"] <= 1
    assert p["truth_proximity"]["is_probability"] is False
    assert p["truth_proximity"]["is_metaphysical_truth_distance"] is False
    assert p["residue"], p["id"]
    assert p["ontic_reserve"], p["id"]

by_id={p["id"]:p for p in compiled}

# Historical packets keep successor shock separate from contemporaneous TPX.
assert by_id["newton-mercury-1859"]["successor_shocks"]
assert by_id["ozone-1985-halley"]["successor_shocks"]
assert by_id["hpylori-1983-association"]["successor_shocks"]

# The compiler must be non-compensatory at the authority-gate level.
probe=by_id["ozone-1986-regional"].copy()
probe["gates"]=dict(probe["gates"])
probe["gates"]["R"]="HOLD"
blocked=rpacket.compile_packet(probe, Path("<synthetic-gate-test>"))
assert blocked["truth_proximity"]["TPX"] is None
assert blocked["authority"]["state"] == "HOLD"

print("R_LANGUAGE_EXAMPLES", len(compiled))
for p in compiled:
    print(p["id"], p["truth_proximity"]["TPX"], p["truth_proximity"]["band"])
print("GATE_NONCOMPENSATION=PASS")
print("HINDSIGHT_FIREWALL=PASS")
print("OPEN_WORLD_RESIDUE=PASS")
print("R_LANGUAGE_V0_1=PASS")
