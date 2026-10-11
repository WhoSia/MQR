#!/usr/bin/env python3
"""REALCHANNEL 0.44-CANDIDATE experimental Real-Language surface.

Parses a *typed* stochastic binary experiment packet. Dispatches only
finite mathematics to the independently tested 4.113 P1 exact rational
Blackwell/Le Cam engine. Structural 'PASS' never confers empirical authority.
No external data fetch and no promotion of the established Real-Language API.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
ENGINE=ROOT / "experiments" / "mqr-4.113" / "p1_exact_binary_experiments.py"

def load_engine():
    spec=importlib.util.spec_from_file_location("mqr_4113_p1_exact_binary_engine",ENGINE)
    if spec is None or spec.loader is None:
        raise ValueError("PINNED_EXACT_BINARY_ENGINE_UNAVAILABLE")
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

ALLOWED={"id","basis","source_quantity","target_quantity",
         "source_operation","target_operation","calibration_ancestry",
         "source_sha256","source_0","source_1","target_0","target_1"}
REQUIRED=ALLOWED-{"source_sha256"}

def parse_packet(text):
    lines=[l.strip() for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if not lines or lines[0]!="REALCHANNEL 0.44-CANDIDATE" or lines[-1]!="END":
        raise ValueError("INVALID_REALCHANNEL_HEADER_OR_MISSING_END")
    if any(l=="END" for l in lines[1:-1]):
        raise ValueError("DUPLICATE_END_OR_TRAILING_STATEMENT")
    fields={}
    for line in lines[1:-1]:
        parts=line.split()
        if not parts or parts[0] not in ALLOWED:
            raise ValueError("UNKNOWN_REALCHANNEL_FIELD")
        key=parts[0]
        if key in fields:
            raise ValueError("DUPLICATE_REALCHANNEL_FIELD")
        if key in {"source_0","source_1","target_0","target_1"}:
            if len(parts)!=3:
                raise ValueError("BINARY_ROW_ARITY_MUST_BE_2")
            fields[key]=parts[1:]
        elif (len(parts)==2 and len(parts[1])<=256 and
              not any(x in parts[1] for x in "<>{};")):
            fields[key]=parts[1]
        else:
            raise ValueError("BAD_REALCHANNEL_ATTRIBUTE")
    if not REQUIRED.issubset(fields):
        raise ValueError("REQUIRED_STOCHASTIC_AND_MEASUREMENT_FIELDS_MISSING")
    if fields["basis"] not in ("FINITE_SYNTHETIC","SOURCE_REPORTED"):
        raise ValueError("UNRECOGNIZED_SOURCE_BASIS")
    has_hash="source_sha256" in fields
    if fields["basis"]=="FINITE_SYNTHETIC" and has_hash:
        raise ValueError("SYNTHETIC_CANNOT_LAUNDER_TO_EMPIRICAL_HASH")
    if fields["basis"]=="SOURCE_REPORTED" and not has_hash:
        raise ValueError("SOURCE_REPORTED_REQUIRES_HASH_POINTER")
    if has_hash:
        d=fields["source_sha256"]
        if len(d)!=64 or any(c not in "0123456789abcdefABCDEF" for c in d):
            raise ValueError("SOURCE_HASH_INVALID")
    e=load_engine()
    a=e.matrix([fields["source_0"],fields["source_1"]])
    b=e.matrix([fields["target_0"],fields["target_1"]])
    fields["_A"]=a
    fields["_B"]=b
    return fields

def evaluate(text):
    e=load_engine()
    p=parse_packet(text)
    ab,ba,math_relation=e.label(p["_A"],p["_B"])
    return {
      "real_language":"REALCHANNEL 0.44-CANDIDATE",
      "packet_id":p["id"],"source_basis":p["basis"],
      "mathematical_experiment_order":math_relation,
      "le_cam_directional_delta_source_to_target":str(ab["delta"]),
      "le_cam_directional_delta_target_to_source":str(ba["delta"]),
      "blackwell_source_to_target_witness_K":[[str(v) for v in row] for row in ab["kernel"]],
      "blackwell_target_to_source_witness_K":[[str(v) for v in row] for row in ba["kernel"]],
      "physical_measurand_declared_match":
          "SAME_DECLARATION_NOT_EMPIRICAL_PROOF" if p["source_quantity"]==p["target_quantity"]
          else "DECLARED_DIFFERENT_QUANTITIES",
      "operation_ancestry":
          "DIFFERENT_LABELS" if p["source_operation"]!=p["target_operation"]
          else "SAME_LABEL_NOT_EMPIRICALLY_VERIFIED",
      "calibration_ancestry_claim":p["calibration_ancestry"],
      "statistical_math_authority":"EXACT_DECLARED_FINITE_CHANNELS_ONLY",
      "empirical_source_warrant":"UNVERIFIED_EVEN_WITH_HASH",
      "measured_physical_equivalence":"HOLD",
      "mqr_4112_full_fer_original_source":"HOLD",
      "real_language_promotion":"UNPROMOTED_CANDIDATE",
    }

def main():
    if len(sys.argv)!=2:
        raise ValueError("usage: real_channel_v44.py packet.real")
    p=Path(sys.argv[1])
    result=evaluate(p.read_text(encoding="utf-8"))
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__":
    try:main()
    except (ValueError,OSError) as exc:
        sys.stderr.write(f"REALCHANNEL_REJECTED: {exc}\n")
        sys.exit(2)
