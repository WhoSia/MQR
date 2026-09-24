#!/usr/bin/env python3
from __future__ import annotations
import math,shlex,sys
from pathlib import Path

VERSION="0.2"
GATES=("C","E","P","R")
AXES=("W","N","I","T","D")

class PacketError(ValueError): pass

def esc(s:str)->str:
    return s.replace("\\","\\\\").replace("\n","\\n").replace("=","\\=")

def parse(path:Path):
    p={"id":"","epoch":"","claim_type":"","claim_text":"","scope":"","gates":{},"axes":{},
       "generators":[],"rivals":[],"residue":[],"mystery":[],"ontic":[],
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
            if len(t)!=2 or t[1]!=VERSION: raise PacketError(f"{path}:{n}: expected REALPACKET {VERSION}")
            started=True; continue
        if not started: raise PacketError(f"{path}:{n}: packet must begin with REALPACKET {VERSION}")
        if cmd.upper()=="END": ended=True; break
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
            if a not in AXES:raise PacketError(f"{path}:{n}: invalid axis")
            v=float(t[2])
            if not 0<=v<=1:raise PacketError(f"{path}:{n}: axis outside [0,1]")
            p["axes"][a]=(v," ".join(t[3:]))
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
    if not all(p[k] for k in ("id","epoch","claim_type","claim_text","scope")):raise PacketError(f"{path}: missing required field")
    for g in GATES:
        if g not in p["gates"]:raise PacketError(f"{path}: missing gate {g}")
    for a in AXES:
        if a not in p["axes"]:raise PacketError(f"{path}: missing axis {a}")
    return p

def canonical(p,scalar=False):
    o=["REAL-LANGUAGE=0.2",f"id={esc(p['id'])}",f"epoch={esc(p['epoch'])}",
       f"claim.type={esc(p['claim_type'])}",f"claim.text={esc(p['claim_text'])}",f"scope={esc(p['scope'])}"]
    for g in GATES:o.append(f"gate.{g}={p['gates'][g]}")
    for a in AXES:
        v,n=p["axes"][a]
        o+= [f"profile.{a}={v:.6f}",f"profile.{a}.note={esc(n)}"]
    passed=all(p["gates"][g]=="PASS" for g in GATES)
    o += [f"authority={'SCOPED_REALIST_AUTHORITY' if passed else 'HOLD'}",
          "profile.order=PARETO_PARTIAL","profile.scalar.default=OFF"]
    if scalar:
        g=math.prod(p["axes"][a][0] for a in AXES)**(1/5)
        o += [f"display.scalar.geometric_mean={g:.6f}","display.scalar.status=UNCALIBRATED_DISPLAY_ONLY"]
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
