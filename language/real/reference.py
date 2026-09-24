#!/usr/bin/env python3
from __future__ import annotations
import math,shlex,sys
from pathlib import Path

GATES=("C","E","P","R")
V2_AXES=("W","N","I","T","D")
V3_AXES=("W","N","I","D")

class PacketError(ValueError): pass

def esc(s:str)->str:
    return s.replace("\\","\\\\").replace("\n","\\n").replace("=","\\=")

def transport_authority(e:str,s:str)->str:
    pairs={
        ("TESTED","SURVIVED"):"TRANSPORT_PASS",
        ("TESTED","FAILED"):"TRANSPORT_FAIL",
        ("TESTED","MIXED_OR_NONATOMIC"):"SPLIT_REQUIRED",
        ("UNTESTED_AVAILABLE","NA"):"HOLD_UNTESTED",
        ("TARGET_UNAVAILABLE","NA"):"HOLD_TARGET_UNAVAILABLE",
        ("OUT_OF_SCOPE","NA"):"OUT_OF_SCOPE",
    }
    if (e,s) not in pairs: raise PacketError(f"invalid evaluability/survival pair: {e}/{s}")
    return pairs[(e,s)]

def parse(path:Path):
    p={"version":"","id":"","epoch":"","claim_type":"","claim_text":"","scope":"","gates":{},"axes":{},
       "transports":[],"generators":[],"rivals":[],"residue":[],"mystery":[],"ontic":[],
       "successor":"VULNERABLE","shocks":[],"sources":[]}
    started=ended=False
    for n,raw in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        line=raw.strip()
        if not line or line.startswith("#"): continue
        try:t=shlex.split(line)
        except ValueError as e: raise PacketError(f"{path}:{n}: {e}") from e
        if not t: continue
        cmd=t[0]
        if cmd.upper()=="REALPACKET":
            if len(t)!=2 or t[1] not in {"0.2","0.3"}: raise PacketError(f"{path}:{n}: expected REALPACKET 0.2 or 0.3")
            p["version"]=t[1];started=True;continue
        if not started: raise PacketError(f"{path}:{n}: packet must begin with REALPACKET")
        if cmd.upper()=="END": ended=True;break

        if cmd=="id" and len(t)==2:p["id"]=t[1]
        elif cmd=="epoch" and len(t)==2:p["epoch"]=t[1]
        elif cmd=="claim" and len(t)>=3:p["claim_type"]=t[1].upper();p["claim_text"]=" ".join(t[2:])
        elif cmd=="scope" and len(t)>=2:p["scope"]=" ".join(t[1:])
        elif cmd=="gate" and len(t)==3:
            g,s=t[1].upper(),t[2].upper()
            if g not in GATES or s not in {"PASS","HOLD","FAIL"}:raise PacketError(f"{path}:{n}: invalid gate")
            p["gates"][g]=s
        elif cmd=="axis" and len(t)>=3:
            a=t[1].upper()
            allowed=V2_AXES if p["version"]=="0.2" else V3_AXES
            if a not in allowed:raise PacketError(f"{path}:{n}: invalid axis {a} for v{p['version']}")
            v=float(t[2])
            if not 0<=v<=1:raise PacketError(f"{path}:{n}: axis outside [0,1]")
            p["axes"][a]=(v," ".join(t[3:]))
        elif cmd=="transport" and p["version"]=="0.3" and len(t)>=8:
            e,s=t[5].upper(),t[6].upper()
            transport_authority(e,s)
            p["transports"].append({
                "component":t[1],"source":t[2],"target":t[3],"dimension":t[4].upper(),
                "evaluability":e,"survival":s,"note":" ".join(t[7:])
            })
        elif cmd=="generator" and len(t)>=3:p["generators"].append((t[1].upper()," ".join(t[2:])))
        elif cmd=="rival" and len(t)>=3:p["rivals"].append((t[1].upper()," ".join(t[2:])))
        elif cmd=="residue" and len(t)>=3:p["residue"].append((t[1].upper()," ".join(t[2:])))
        elif cmd=="mystery" and len(t)>=3:p["mystery"].append((t[1].upper()," ".join(t[2:])))
        elif cmd=="ontic" and len(t)>=3:p["ontic"].append((t[1].upper()," ".join(t[2:])))
        elif cmd=="successor" and len(t)==2:p["successor"]=t[1].upper()
        elif cmd=="shock" and len(t)>=4:p["shocks"].append((t[1],t[2].upper()," ".join(t[3:])))
        elif cmd=="source" and len(t)>=2:p["sources"].append(" ".join(t[1:]))
        else:raise PacketError(f"{path}:{n}: malformed command: {line}")
    if not ended:raise PacketError(f"{path}: missing END")
    if not all(p[k] for k in ("version","id","epoch","claim_type","claim_text","scope")):raise PacketError(f"{path}: missing required field")
    for g in GATES:
        if g not in p["gates"]:raise PacketError(f"{path}: missing gate {g}")
    required=V2_AXES if p["version"]=="0.2" else V3_AXES
    for a in required:
        if a not in p["axes"]:raise PacketError(f"{path}: missing axis {a}")
    if p["version"]=="0.3" and "T" in p["axes"]:raise PacketError(f"{path}: v0.3 forbids legacy axis T")
    return p

def claim_state(p):
    if not p["transports"]:return "NO_EVALUABLE_TARGET"
    any_required=any_fail=any_hold=any_split=False
    for t in p["transports"]:
        a=transport_authority(t["evaluability"],t["survival"])
        if a=="OUT_OF_SCOPE":continue
        any_required=True
        any_fail |= a=="TRANSPORT_FAIL"
        any_hold |= a in {"HOLD_UNTESTED","HOLD_TARGET_UNAVAILABLE"}
        any_split |= a=="SPLIT_REQUIRED"
    if not any_required:return "NO_EVALUABLE_TARGET"
    if any_split:return "SPLIT_REQUIRED"
    if any_fail:return "SOME_REQUIRED_CELLS_FAIL"
    if any_hold:return "PARTIAL_WITH_HOLDS"
    return "ALL_REQUIRED_CELLS_PASS"

def canonical(p,scalar=False):
    o=[f"REAL-LANGUAGE={p['version']}",f"id={esc(p['id'])}",f"epoch={esc(p['epoch'])}",
       f"claim.type={esc(p['claim_type'])}",f"claim.text={esc(p['claim_text'])}",f"scope={esc(p['scope'])}"]
    for g in GATES:o.append(f"gate.{g}={p['gates'][g]}")
    axes=V2_AXES if p["version"]=="0.2" else V3_AXES
    for a in axes:
        v,n=p["axes"][a]
        o += [f"profile.{a}={v:.6f}",f"profile.{a}.note={esc(n)}"]
    passed=all(p["gates"][g]=="PASS" for g in GATES)
    o += [f"authority={'SCOPED_REALIST_AUTHORITY' if passed else 'HOLD'}",
          "profile.order=PARETO_PARTIAL","profile.scalar.default=OFF"]

    if p["version"]=="0.2":
        o.append("legacy.profile.T=ACTIVE_V0_2")
        if scalar:
            g=math.prod(p["axes"][a][0] for a in V2_AXES)**(1/5)
            o += [f"display.scalar.geometric_mean={g:.6f}","display.scalar.status=UNCALIBRATED_DISPLAY_ONLY"]
    else:
        o += ["legacy.profile.T=DEPRECATED","transport.mode=TYPED_RELATION_MAP",f"transport.count={len(p['transports'])}"]
        for i,t in enumerate(p["transports"]):
            a=transport_authority(t["evaluability"],t["survival"])
            o += [
                f"transport.{i}.component={esc(t['component'])}",
                f"transport.{i}.source={esc(t['source'])}",
                f"transport.{i}.target={esc(t['target'])}",
                f"transport.{i}.dimension={esc(t['dimension'])}",
                f"transport.{i}.evaluability={t['evaluability']}",
                f"transport.{i}.survival={t['survival']}",
                f"transport.{i}.authority={a}",
                f"transport.{i}.note={esc(t['note'])}",
            ]
        o.append(f"transport.claim_state={claim_state(p)}")
        if scalar:o.append("display.scalar.status=UNAVAILABLE_V0_3_TYPED_TRANSPORT")

    o += ["open_world_residue=true","final_truth_distance=UNIDENTIFIED",f"successor={p['successor']}"]
    for key,name in (("generators","generator"),("rivals","rival"),("residue","residue"),("mystery","mystery"),("ontic","ontic")):
        label={"generator":"kind","rival":"state","residue":"level","mystery":"level","ontic":"state"}[name]
        for i,(k,d) in enumerate(p[key]):o += [f"{name}.{i}.{label}={k}",f"{name}.{i}.text={esc(d)}"]
    for i,(e,k,d) in enumerate(p["shocks"]):o += [f"shock.{i}.epoch={esc(e)}",f"shock.{i}.type={k}",f"shock.{i}.text={esc(d)}"]
    for i,s in enumerate(p["sources"]):o.append(f"source.{i}={esc(s)}")
    return "\n".join(o)+"\n"

def main(argv):
    scalar="--diagnostic-scalar" in argv
    args=[x for x in argv[1:] if x!="--diagnostic-scalar"]
    if not args:
        print("usage: reference.py [--diagnostic-scalar] PACKET [PACKET ...]",file=sys.stderr);return 2
    outs=[canonical(parse(Path(x)),scalar) for x in args]
    sys.stdout.write("---\n".join(outs));return 0

if __name__=="__main__":raise SystemExit(main(sys.argv))
