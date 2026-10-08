"""MQR-4.89: causal nonidentifiability despite formally independent receipts.

Exact two-model counterexample inspired by Bareinboim & Pearl (2016),
Definition 2. This is PRIOR ART, not a new MQR theorem.
Uses the real restricted MQR-4.87 source-family interpreter.
"""
from collections import defaultdict
from fractions import Fraction
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import sys

HALF = Fraction(1, 2)

def observational(orientation):
    # Both structures produce X=Y=U, U ~ Bernoulli(1/2).
    assert orientation in ("X_TO_Y", "Y_TO_X")
    return {(0, 0): HALF, (1, 1): HALF}

def interventional(orientation, x):
    # First structure: X=U and Y=X. Second: Y=U and X=Y.
    # After do(X=x), Y=x in first, Y=U in second.
    if orientation == "X_TO_Y":
        return Fraction(x, 1)
    if orientation == "Y_TO_X":
        return HALF
    raise ValueError(orientation)

def original_487():
    path = Path(__file__).resolve().parent.parent / "mqr-4.87" / "real_lang_p1.py"
    spec = spec_from_file_location("mqr487_original_policy", path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError(path)
    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def source_family_verdict(families=("F1", "F2"), permission=True):
    p = original_487()
    scope = "hypothetical-causal-use"
    sources = {name: p.Source(family, frozenset({component}), frozenset({scope}))
               for name, family, component in
               zip(("a", "b"), families, ("survey_1", "survey_2"))}
    return p.adjudicate([(("a",),1),(("b",),1)],
                        sources, scope, permission, threshold=2)

def adjudicate_causal_transport(families=("F1","F2"), permission=True):
    src = source_family_verdict(families, permission)
    if src["verdict"] != "AUTHORIZED_FOR_USE":
        return "SOURCE_POLICY_" + src["verdict"]
    # This countermodel pair has identical observational distributions but
    # materially different causal queries, so no general causal warrant
    # follows merely from 4.87 family count.
    worlds = ("X_TO_Y", "Y_TO_X")
    assert observational(worlds[0]) == observational(worlds[1])
    if len({interventional(model, 1) for model in worlds}) > 1:
        return "HOLD_CAUSAL_WARRANT_NONIDENTIFIABLE"
    return "NO_IDENTIFIABILITY_OBJECTION_WITHIN_TESTED_MODELS_ONLY"

def tests():
    w1,w2 = "X_TO_Y","Y_TO_X"
    checks = [
        observational(w1)==observational(w2),
        observational(w1)=={(0,0):HALF,(1,1):HALF},
        interventional(w1,1)==1,
        interventional(w2,1)==HALF,
        interventional(w1,0)==0,
        interventional(w2,0)==HALF,
        source_family_verdict()["verdict"]=="AUTHORIZED_FOR_USE",
        source_family_verdict(("F1","F1"))["verdict"]=="HOLD_INSUFFICIENT",
        source_family_verdict(permission=False)["verdict"]=="DENIED_SCOPE",
        adjudicate_causal_transport()=="HOLD_CAUSAL_WARRANT_NONIDENTIFIABLE",
        adjudicate_causal_transport(("F1","F1"))=="SOURCE_POLICY_HOLD_INSUFFICIENT",
        adjudicate_causal_transport(permission=False)=="SOURCE_POLICY_DENIED_SCOPE",
    ]
    assert all(checks), list(enumerate(checks,1))
    print("MQR489_CAUSAL_COUNTERMODEL_CHECKS=12 PASS")
    print("MQR489_POLICY_RESULT=AUTHORIZED_FOR_USE")
    print("MQR489_CAUSAL_WARRANT=HOLD_CAUSAL_WARRANT_NONIDENTIFIABLE")
    print("MQR489_ORIGINAL_EMPIRICAL_REPLAY=NOT_PERFORMED")
    print("MQR489_NOVELTY=PRIOR_ART_NOT_NEW_THEOREM")
if __name__=="__main__":
    tests()
