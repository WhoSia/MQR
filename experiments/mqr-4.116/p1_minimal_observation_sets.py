from itertools import combinations

# Constructed possible worlds, not empirical states in Greenberg's network.
worlds = [
    {"id":"w1","independent":1,"defeated":0,"selection":"A","citations":"same","cert":"distinct"},
    {"id":"w2","independent":0,"defeated":0,"selection":"A","citations":"same","cert":"shared"},
    {"id":"w3","independent":1,"defeated":1,"selection":"A","citations":"same","cert":"distinct"},
    {"id":"w4","independent":0,"defeated":1,"selection":"B","citations":"same","cert":"shared"},
]
def verdict(w):
    return (w["independent"]==1 and w["defeated"]==0)

def identifies(keys):
    groups={}
    for w in worlds:
        o=tuple(w[k] for k in ("citations",)+tuple(keys))
        groups.setdefault(o,set()).add(verdict(w))
    return all(len(s)==1 for s in groups.values())

candidates=("selection","cert","defeated")
assert not identifies(())
assert not identifies(("selection",))
assert not identifies(("cert",))
assert not identifies(("defeated",))
assert identifies(("cert","defeated"))
minimal=[tuple(c) for k in range(1,len(candidates)+1) for c in combinations(candidates,k)
         if identifies(c) and not any(identifies(sub) for n in range(1,k) for sub in combinations(c,n))]
assert minimal==[("cert","defeated")]
print("PASS: unique minimal extra observation set =",minimal)
