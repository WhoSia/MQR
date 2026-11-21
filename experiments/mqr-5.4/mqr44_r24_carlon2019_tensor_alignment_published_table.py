"""MQR44 R24: exact arithmetic on published Carlon et al. Table 1 (2019 journal).
No fitting, structural coordinate reads, or independently replayed NMR acquisition.
"""
from dataclasses import dataclass
from decimal import Decimal as D

@dataclass(frozen=True)
class PublishedFit:
    name: str
    r_free: D
    q_rdc: D | None
    geometry_bond_length: D

BASE=PublishedFit("deposited 4QQB structure",D("0.2360"),D("0.440"),D("0.006"))
NO_NMR=PublishedFit("new refit no NMR",D("0.2352"),None,D("0.0064"))
EMPIRICAL=PublishedFit("single tensor with 0.8 domain scale",D("0.2362"),D("0.131"),D("0.0101"))
ORIENTED=PublishedFit("joint tensor orientation constraint",D("0.2360"),D("0.121"),D("0.0100"))

def improvements(ref,alt):
    """Raw differences; lower is preferable for these particular published metrics."""
    if ref.q_rdc is None or alt.q_rdc is None:
        raise ValueError("A model without NMR Q is not evidence of an NMR change")
    return {"q_rdc_improvement":ref.q_rdc-alt.q_rdc,
            "r_free_improvement":ref.r_free-alt.r_free,
            "bond_rmsd_improvement":ref.geometry_bond_length-alt.geometry_bond_length}

def test():
    assert improvements(EMPIRICAL,ORIENTED)=={
        "q_rdc_improvement":D("0.010"),"r_free_improvement":D("0.0002"),
        "bond_rmsd_improvement":D("0.0001")}
    assert ORIENTED.r_free == BASE.r_free
    assert ORIENTED.q_rdc < EMPIRICAL.q_rdc < BASE.q_rdc
    assert NO_NMR.r_free < ORIENTED.r_free
    assert ORIENTED.geometry_bond_length > BASE.geometry_bond_length
    assert all(v>=0 for v in improvements(EMPIRICAL,ORIENTED).values())
    try:
        improvements(NO_NMR,ORIENTED)
    except ValueError:
        pass
    else:
        raise AssertionError("Missing NMR comparison must be rejected")
    return True

if __name__=="__main__":
    test()
    for model in (BASE,NO_NMR,EMPIRICAL,ORIENTED):
        print(model)
    print(improvements(EMPIRICAL,ORIENTED))
    print("PASS: 7 scoped exact Decimal checks on rounded author-published Table 1")
