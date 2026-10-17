from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class Witness:
    name: str
    root: str
    strength: int
    defeated: bool = False

def verdict(ws):
    valid = [w for w in ws if not w.defeated]
    pairs = list(combinations(valid, 2))
    return (
        bool(valid),
        any(a.root != b.root for a,b in pairs),
        any(a.root != b.root and min(a.strength,b.strength) >= 2 for a,b in pairs)
    )

cases = {
    "original": [Witness("a","r1",2),Witness("b","r2",2)],
    "split_same_root": [Witness("a1","r1",2),Witness("a2","r1",2)],
    "independent_weak": [Witness("a","r1",1),Witness("b","r2",1)],
    "defeated": [Witness("a","r1",2),Witness("b","r2",2,True)],
    "syntax_duplicates": [Witness("a1","r1",2),Witness("a2","r1",2),Witness("b","r2",2)]
}
expected = [(True,True,True),(True,False,False),(True,True,False),(True,False,False),(True,True,True)]
for (name,ws), e in zip(cases.items(),expected):
    actual = verdict(ws)
    assert actual == e, (name,actual)
    print(name,actual)
print("PASS finite tests=5")
