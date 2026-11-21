"""Toy query-generating instrument policy: actions can create new observables.

Four equal-prior worlds (x,y), two time slots. Script uses enumerated
worlds and Shannon entropy. No empirical or historical claim.
"""
from collections import Counter
from itertools import product
from math import log2

WORLDS = tuple(product((0,1), repeat=2))

def observe(world, plan):
    x,y = world
    built=False
    output=[]
    for action in plan:
        if action=="inspect_x":
            output.append(("x",x))
        elif action=="build":
            built=True
            output.append(("none",None))
        elif action=="measure_xy":
            if not built:
                raise ValueError("measurement not available until built")
            output.append(("xy",(x,y)))
        else:
            raise ValueError(action)
    return tuple(output)

def information_bits(plan):
    observed=Counter(observe(w,plan) for w in WORLDS)
    return sum(count/4 * log2(4/count) for count in observed.values())

def accessible_plans():
    for a in ("inspect_x","build"):
        for b in ("inspect_x","build","measure_xy"):
            if b=="measure_xy" and a!="build":
                continue
            yield (a,b)

def verify():
    assert information_bits(("inspect_x",))==1
    assert information_bits(("build",))==0
    assert information_bits(("inspect_x","inspect_x"))==1
    assert information_bits(("inspect_x","build"))==1
    assert information_bits(("build","measure_xy"))==2
    assert max((information_bits(p),p) for p in accessible_plans())[0]==2
    assert all(information_bits(p)<=2 for p in accessible_plans())
    try:
        observe((0,0),("measure_xy",))
    except ValueError:
        pass
    else:
        raise AssertionError("premature measurement should fail")
    return "PASS: immediate-info greedy=1 bit, capability-first plan=2 bits"

if __name__=="__main__":
    print(verify())
