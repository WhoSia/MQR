"""MQR 4.119 P2 constructed-case contract sanity; no model evaluation."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Case:
    ident: str
    split: str
    family: str
    observation: str
    challenge: str

CASES = (
    Case("T01","train","blank_drift","baseline moved","Is the blank valid?"),
    Case("T02","train","range_violation","signal above range","May one extrapolate?"),
    Case("H01","holdout","spectral_overlap","extra absorption band","Is analyte attribution valid?"),
    Case("H02","holdout","matrix_nonlinearity","dilution slope changes","Is linearity justified?"),
    Case("H03","holdout","custody_inconsistency","standard records conflict","Is custody authenticated?"),
)

def sanity():
    ids=[c.ident for c in CASES]
    train={c.family for c in CASES if c.split=="train"}
    hold={c.family for c in CASES if c.split=="holdout"}
    assert len(set(ids))==len(CASES)==5
    assert len(train)==2 and len(hold)==3 and train.isdisjoint(hold)
    assert hold=={"spectral_overlap","matrix_nonlinearity","custody_inconsistency"}
    return "CONTRACT_SANITY_PASS (not epistemic performance)"

if __name__=="__main__":
    print(sanity())
