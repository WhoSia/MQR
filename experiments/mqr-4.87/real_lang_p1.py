#!/usr/bin/env python3
"""MQR-4.87 P1 synthetic Real Lang court; no scientific authority oracle."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Source:
    family: str
    components: frozenset[str]
    scopes: frozenset[str]
    credential_valid: bool = True

def adjudicate(terms, sources, scope, permission, threshold=2, compromised=frozenset()):
    if not permission:
        return {"verdict":"DENIED_SCOPE","families":[],"affected":[],"unknown":[]}
    families, affected, unknown = set(), set(), set()
    for monomial, coefficient in terms:
        if coefficient <= 0:
            continue
        # Only singleton monomials have an independently interpreted source.
        if len(monomial) != 1:
            continue
        name = monomial[0]
        source = sources.get(name)
        if source is None:
            unknown.add(name)
            continue
        if not source.credential_valid or scope not in source.scopes:
            continue
        if source.components & compromised:
            affected.add(name)
            continue
        families.add(source.family)
    if len(families) >= threshold:
        verdict = "AUTHORIZED_FOR_USE"
    elif affected:
        verdict = "HOLD_SHARED_DEFECT"
    else:
        verdict = "HOLD_INSUFFICIENT"
    return dict(verdict=verdict, families=sorted(families),
                affected=sorted(affected), unknown=sorted(unknown))

def run_tests():
    a = Source("F1", frozenset({"inst1"}), frozenset({"s"}))
    b = Source("F2", frozenset({"inst2"}), frozenset({"s"}))
    shared = Source("F1", frozenset({"inst2"}), frozenset({"s"}))
    bad = Source("F2", frozenset({"inst2"}), frozenset({"s"}), False)
    pp = [(("p",),1),(("q",),1)]
    tests = [
       ("T1", adjudicate(pp,{"p":a,"q":b},"s",True), "AUTHORIZED_FOR_USE"),
       ("T2", adjudicate(pp,{"p":a,"q":shared},"s",True), "HOLD_INSUFFICIENT"),
       ("T3", adjudicate(pp,{"p":a,"q":b},"s",True,compromised=frozenset({"inst1","inst2"})), "HOLD_SHARED_DEFECT"),
       ("T4", adjudicate(pp,{"p":a,"q":b},"s",False), "DENIED_SCOPE"),
       ("T5", adjudicate([(("p","p"),2)],{"p":a},"s",True), "HOLD_INSUFFICIENT"),
       ("T6", adjudicate(pp,{"p":a,"q":bad},"s",True), "HOLD_INSUFFICIENT"),
       ("T7", adjudicate(pp,{"p":a,"q":shared},"s",True,threshold=1), "AUTHORIZED_FOR_USE"),
       ("T8", adjudicate(pp,{"p":a,"q":b},"s",True), "AUTHORIZED_FOR_USE"),
       ("T9", adjudicate([(("p",),2),(("p",),1)],{"p":a},"s",True), "HOLD_INSUFFICIENT"),
       ("T10", adjudicate(pp,{"p":a},"s",True), "HOLD_INSUFFICIENT"),
    ]
    for name, result, expected in tests:
        assert result['verdict'] == expected, (name,result,expected)
    assert tests[7][1]["verdict"] != tests[1][1]["verdict"]
    assert tests[9][1]["unknown"] == ["q"]
    assert tests[2][1]["affected"] == ["p","q"]
    print("MQR487_P1_CASES=10")
    print("MQR487_P1_PASS=10")
    print("MQR487_P1_NOVELTY=UNADJUDICATED")

if __name__ == "__main__":
    run_tests()