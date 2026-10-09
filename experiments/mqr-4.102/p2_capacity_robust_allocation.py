#!/usr/bin/env python3
"""4.102 P2 finite multi-target allocation with explicit capacity restrictions.
All reviews are hypothetical: no third-party truth is observed.
"""
import collections,csv,hashlib,itertools,json,sys
from fractions import Fraction
from pathlib import Path
SHA="d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842"
def source(path):
 b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==SHA
 rows=list(csv.DictReader(b.decode().splitlines()))
 assert len(rows)==487
 by=collections.defaultdict(lambda:[0,0,0])
 for r in rows:
  x=by[r["record"]];x[0]+=1
  if r["paired_complete"]=="1":
   x[1]+=1
   if (float(r["q1_QT_ms"])>=440)!=(float(r["q2_QT_ms"])>=440):x[2]+=1
 assert len(by)==11 and sum(q[1] for q in by.values())==402 and sum(q[2] for q in by.values())==76
 return dict(sorted(by.items()))
def width(by,alloc,target):
 den=402 if target=="pooled" else None
 return sum(Fraction(2*(v[2]-alloc.get(r,0)),den if den else 11*v[1]) for r,v in by.items())
def optimum(by,budget,caps,target):
 # separable integer linear maximization under individual caps
 if target not in ("pooled","equal"):raise ValueError(target)
 assert 0<=budget<=sum(min(caps.get(r,0),v[2]) for r,v in by.items())
 order=sorted(by,key=lambda r:(-Fraction(2,402 if target=="pooled" else 11*by[r][1]),r))
 remaining=budget;result={}
 for r in order:
  n=min(remaining,by[r][2],caps.get(r,0))
  result[r]=n;remaining-=n
 assert remaining==0
 return {r:x for r,x in result.items() if x}
def exhaustive():
 cases=0
 for counts in itertools.product(range(3),repeat=3):
  by={f"r{i}":[v,v,d] for i,(v,d) in enumerate(zip((2,3,4),counts))}
  for caps_t in itertools.product(range(3),repeat=3):
   caps=dict(zip(by,caps_t));feasible=sum(min(caps[r],by[r][2]) for r in by)
   for budget in range(feasible+1):
    for target in ("pooled","equal"):
     out=optimum(by,budget,caps,target); val=width(by,out,target)
     vals=[]
     for x in itertools.product(*(range(min(caps[r],by[r][2])+1) for r in by)):
      if sum(x)==budget:vals.append(width(by,dict(zip(by,x)),target))
     assert vals and val==min(vals),(by,caps,budget,target,val,min(vals))
     cases+=1
 return cases
def main(input,output):
 by=source(input); caps={r:min(3,x[2]) for r,x in by.items()}
 budget=10
 # Some records cannot supply 3 adjudications; no review is presumed to succeed.
 rows={}
 for target in ("pooled","equal"):
  unconstrained=optimum(by,budget,{r:x[2] for r,x in by.items()},target)
  constrained=optimum(by,budget,caps,target)
  rows[target]={"current_width":str(width(by,{},target)),
    "unconstrained_10_allocation":unconstrained,
    "unconstrained_residual_width":str(width(by,unconstrained,target)),
    "cap3_10_allocation":constrained,
    "cap3_residual_width":str(width(by,constrained,target))}
 # Robust unknown objective mixture: lambda*pooled+(1-lambda)*equal,
 # max over lambda in [0,1] equals max(endpoint widths). Enumerate feasible 
 # per-record integer allocations and minimize that worst-case width.
 feasible={r:min(by[r][2],caps[r]) for r in by}
 keys=[r for r,n in feasible.items() if n]
 def search(i,remaining,out):
  if i==len(keys):
   if remaining==0:yield dict(out)
   return
  r=keys[i]
  for v in range(min(remaining,feasible[r])+1):
   out[r]=v
   yield from search(i+1,remaining-v,out)
  out.pop(r,None)
 best=None;bestallocation=None;ties=0
 for a in search(0,budget,{}):
  score=max(width(by,a,"pooled"),width(by,a,"equal"))
  if best is None or score<best:
   best=score;bestallocation=dict(a);ties=1
  elif score==best:ties+=1
 assert best is not None
 actual=exhaustive()
 receipt={"source_sha256":SHA,"records":by,"budget":budget,"max_reviews_per_record":3,
          "allocation_is_hypothetical":True,"review_truth_observations":0,
          "targets":rows,"minimax_over_all_unknown_mixture_weights":{
             "max_residual_identification_width":str(best),
             "selected_reviews":{r:v for r,v in bestallocation.items() if v},
             "number_of_optimal_integer_allocations":ties},
          "small_world_exact_optimizer_tests":actual,
          "risk_status":"FINITE_IDENTIFICATION_WIDTH_ONLY;UNKNOWN_THIRD_PARTY_REFERENCE=HOLD;POPULATION_RISK=HOLD"}
 Path(output).parent.mkdir(parents=True,exist_ok=True)
 Path(output).write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
 print("MQR4102_P2_CAPACITY_SELECTION_EXACT_SMALL_WORLDS=PASS;REAL_TRUTH_HOLD",actual)
 print(json.dumps(rows,sort_keys=True));print("MINIMAX",str(best),bestallocation)
if __name__=="__main__":
 main(sys.argv[1],sys.argv[2])
