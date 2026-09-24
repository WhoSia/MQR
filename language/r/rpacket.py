#!/usr/bin/env python3
"""R-Language / R-Packet v0.1 compiler.

This compiler deliberately does NOT estimate P(claim=true).
It compiles a scoped MQR authority receipt and an optional
Truth-Proximity Proxy (TPX) from explicit auditable coordinates.
"""

from __future__ import annotations

import json
import math
import pathlib
import shlex
import sys
from typing import Any

VERSION = "0.1"
GATES = ("C", "E", "P", "R")
AXES = ("W", "N", "I", "T", "D")
GATE_STATES = {"PASS", "HOLD", "FAIL"}
SUCCESSOR_STATES = {"VULNERABLE", "STABLE", "RETIRED"}
RIVAL_STATES = {"SURVIVING", "DEFEATED", "LIVE", "HISTORICAL"}
SHOCK_TYPES = {"PRESERVE", "CONTRACT", "REINTERPRET", "EXPAND_RIVAL_SPACE", "RETIRE"}
ONTIC_STATES = {"PASS", "HOLD", "FAIL"}
RESIDUE_LEVELS = {"LOW", "MODERATE", "HIGH", "CRITICAL"}
MYSTERY_LEVELS = {"LOW", "MODERATE", "HIGH", "OPEN"}


class RPacketError(ValueError):
    pass


def band(tpx: float) -> str:
    if tpx < 0.40:
        return "FRAGILE_SCOPED"
    if tpx < 0.60:
        return "LIMITED_SCOPED"
    if tpx < 0.80:
        return "SCOPED_REALIST"
    return "STRONG_SCOPED_REALIST"


def blank() -> dict[str, Any]:
    return {
        "language": "R-Packet",
        "version": VERSION,
        "id": None,
        "epoch": None,
        "claim": {"type": None, "text": None},
        "scope": None,
        "gates": {},
        "axes": {},
        "generators": [],
        "rivals": [],
        "residue": [],
        "mystery": [],
        "ontic_reserve": [],
        "successor_state": "VULNERABLE",
        "successor_shocks": [],
        "sources": [],
    }


def parse(path: pathlib.Path) -> dict[str, Any]:
    p = blank()
    started = False
    ended = False

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            parts = shlex.split(line)
        except ValueError as e:
            raise RPacketError(f"{path}:{lineno}: quoting error: {e}") from e
        if not parts:
            continue

        cmd = parts[0]
        ucmd = cmd.upper()

        if ucmd == "RPACKET":
            if len(parts) != 2 or parts[1] != VERSION:
                raise RPacketError(f"{path}:{lineno}: expected RPACKET {VERSION}")
            started = True
            continue

        if not started:
            raise RPacketError(f"{path}:{lineno}: packet must begin with RPACKET {VERSION}")

        if ucmd == "END":
            ended = True
            break

        if cmd == "id" and len(parts) == 2:
            p["id"] = parts[1]
        elif cmd == "epoch" and len(parts) == 2:
            p["epoch"] = parts[1]
        elif cmd == "claim" and len(parts) >= 3:
            p["claim"] = {"type": parts[1].upper(), "text": " ".join(parts[2:])}
        elif cmd == "scope" and len(parts) >= 2:
            p["scope"] = " ".join(parts[1:])
        elif cmd == "gate" and len(parts) == 3:
            g, state = parts[1].upper(), parts[2].upper()
            if g not in GATES or state not in GATE_STATES:
                raise RPacketError(f"{path}:{lineno}: invalid gate")
            p["gates"][g] = state
        elif cmd == "axis" and len(parts) >= 3:
            a = parts[1].upper()
            if a not in AXES:
                raise RPacketError(f"{path}:{lineno}: invalid axis {a}")
            try:
                value = float(parts[2])
            except ValueError as e:
                raise RPacketError(f"{path}:{lineno}: axis must be numeric") from e
            if not 0.0 <= value <= 1.0:
                raise RPacketError(f"{path}:{lineno}: axis must be in [0,1]")
            p["axes"][a] = {
                "value": value,
                "note": " ".join(parts[3:]) if len(parts) > 3 else "",
            }
        elif cmd == "generator" and len(parts) >= 3:
            p["generators"].append({"kind": parts[1].upper(), "description": " ".join(parts[2:])})
        elif cmd == "rival" and len(parts) >= 3:
            state = parts[1].upper()
            if state not in RIVAL_STATES:
                raise RPacketError(f"{path}:{lineno}: invalid rival state {state}")
            p["rivals"].append({"state": state, "description": " ".join(parts[2:])})
        elif cmd == "residue" and len(parts) >= 3:
            level = parts[1].upper()
            if level not in RESIDUE_LEVELS:
                raise RPacketError(f"{path}:{lineno}: invalid residue level {level}")
            p["residue"].append({"level": level, "description": " ".join(parts[2:])})
        elif cmd == "mystery" and len(parts) >= 3:
            level = parts[1].upper()
            if level not in MYSTERY_LEVELS:
                raise RPacketError(f"{path}:{lineno}: invalid mystery level {level}")
            p["mystery"].append({"level": level, "description": " ".join(parts[2:])})
        elif cmd == "ontic" and len(parts) >= 3:
            state = parts[1].upper()
            if state not in ONTIC_STATES:
                raise RPacketError(f"{path}:{lineno}: invalid ontic state {state}")
            p["ontic_reserve"].append({"state": state, "description": " ".join(parts[2:])})
        elif cmd == "successor" and len(parts) == 2:
            state = parts[1].upper()
            if state not in SUCCESSOR_STATES:
                raise RPacketError(f"{path}:{lineno}: invalid successor state {state}")
            p["successor_state"] = state
        elif cmd == "shock" and len(parts) >= 4:
            kind = parts[2].upper()
            if kind not in SHOCK_TYPES:
                raise RPacketError(f"{path}:{lineno}: invalid shock type {kind}")
            p["successor_shocks"].append({
                "epoch": parts[1],
                "type": kind,
                "description": " ".join(parts[3:]),
            })
        elif cmd == "source" and len(parts) >= 2:
            p["sources"].append(" ".join(parts[1:]))
        else:
            raise RPacketError(f"{path}:{lineno}: unknown or malformed command: {line}")

    if not ended:
        raise RPacketError(f"{path}: packet missing END")
    return compile_packet(p, path)


def compile_packet(p: dict[str, Any], path: pathlib.Path) -> dict[str, Any]:
    for key in ("id", "epoch", "scope"):
        if not p[key]:
            raise RPacketError(f"{path}: missing required field {key}")
    if not p["claim"]["type"] or not p["claim"]["text"]:
        raise RPacketError(f"{path}: missing claim")

    missing_gates = [g for g in GATES if g not in p["gates"]]
    missing_axes = [a for a in AXES if a not in p["axes"]]
    if missing_gates:
        raise RPacketError(f"{path}: missing gates {missing_gates}")
    if missing_axes:
        raise RPacketError(f"{path}: missing axes {missing_axes}")

    gates_pass = all(p["gates"][g] == "PASS" for g in GATES)
    values = [p["axes"][a]["value"] for a in AXES]

    if gates_pass:
        # Any zero coordinate forces TPX to zero. This prevents additive compensation.
        tpx = math.prod(values) ** (1.0 / len(values))
        p["truth_proximity"] = {
            "TPP": {a: p["axes"][a]["value"] for a in AXES},
            "TPX": round(tpx, 6),
            "band": band(tpx),
            "semantics": "CURRENT_WORLD_CONSTRAINED_PROXIMITY_PROXY",
            "is_probability": False,
            "is_metaphysical_truth_distance": False,
        }
        p["authority"] = {
            "state": "SCOPED_REALIST_AUTHORITY",
            "band": band(tpx),
        }
    else:
        p["truth_proximity"] = {
            "TPP": {a: p["axes"][a]["value"] for a in AXES},
            "TPX": None,
            "band": None,
            "semantics": "GATE_BLOCKED",
            "is_probability": False,
            "is_metaphysical_truth_distance": False,
        }
        p["authority"] = {
            "state": "HOLD",
            "band": None,
            "blocking_gates": [g for g in GATES if p["gates"][g] != "PASS"],
        }

    p["open_world_residue"] = True
    p["final_ontology"] = "HOLD" if any(x["state"] == "HOLD" for x in p["ontic_reserve"]) else "UNSPECIFIED"
    p["compiler_invariants"] = {
        "hindsight_firewall": True,
        "successor_vulnerable": p["successor_state"] == "VULNERABLE",
        "scalar_requires_all_gates": True,
        "residue_visible": True,
        "open_world_closure_forbidden": True,
    }
    return p


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: rpacket.py PACKET [PACKET ...]", file=sys.stderr)
        return 2
    out = [parse(pathlib.Path(x)) for x in argv[1:]]
    payload: Any = out[0] if len(out) == 1 else out
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
