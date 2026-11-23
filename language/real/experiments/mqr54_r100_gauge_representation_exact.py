"""MQR 5.4 R100: exact gauge-representation countermodel.

Modern differential-form sanity check only, NOT verbatim Maxwell 1856 notation,
NOT evidence of an actual cross-civilization communication experiment.
For uniform B and integer-grid paths:
  A1=(0,B*x); A2=(-B*y,0);
  A2-A1=grad(-B*x*y); curl(A1)=curl(A2)=B.
Thus open path integrals differ by endpoint scalar difference; closed
integrals agree and equal B times signed area. Rational arithmetic throughout.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json

B = F(3, 2)
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def chi(p: tuple[int, int]) -> F:
    return -B * p[0] * p[1]


def edge_integrals(p: tuple[int, int], q: tuple[int, int]) -> tuple[F, F]:
    x, y = p
    xx, yy = q
    if abs(xx-x) + abs(yy-y) != 1:
        raise ValueError("must be an oriented unit horizontal or vertical edge")
    a1 = B * x * (yy-y)
    a2 = -B * y * (xx-x)
    assert a2 - a1 == chi(q) - chi(p)
    return (a1, a2)


def path_integrals(path: tuple[tuple[int, int], ...]) -> tuple[F, F]:
    if len(path) < 2:
        raise ValueError("two or more vertices required")
    vals = [edge_integrals(p, q) for p, q in zip(path, path[1:])]
    return (sum((a for a, _ in vals), F(0)),
            sum((b for _, b in vals), F(0)))


def signed_area(path: tuple[tuple[int, int], ...]) -> F:
    if path[0] != path[-1]:
        raise ValueError("polygonal closed path required")
    return F(sum(x*yy - xx*y for (x, y), (xx, yy) in zip(path, path[1:])), 2)


def test() -> dict:
    checked = 0
    closed = 0
    different_open = 0
    # Exhaustive grid walks of at most five steps in [-1,1]^2.
    for start in product(range(-1,2), repeat=2):
        for n in range(1,6):
            for dirs in product(DIRS, repeat=n):
                pts = [start]
                for dx,dy in dirs:
                    p = pts[-1]
                    q = (p[0]+dx, p[1]+dy)
                    if q[0] not in range(-1,2) or q[1] not in range(-1,2):
                        break
                    pts.append(q)
                else:
                    pth = tuple(pts)
                    p1,p2=path_integrals(pth)
                    assert p2-p1 == chi(pth[-1])-chi(pth[0])
                    checked += 1
                    if pth[0]==pth[-1]:
                        assert p1==p2==B*signed_area(pth)
                        closed += 1
                    if p1!=p2:
                        different_open += 1
    rectangle=((0,0),(1,0),(1,1),(0,1),(0,0))
    assert path_integrals(rectangle)==(B,B)
    assert signed_area(rectangle)==1
    assert path_integrals(tuple(reversed(rectangle)))==(-B,-B)
    # On an open path, A1 and A2 can disagree while curl agrees:
    open_path=((0,0),(1,0),(1,1))
    assert path_integrals(open_path)==(B, F(0))
    # Distinct physical B is NOT mere gauge: closed signal changes.
    assert B*signed_area(rectangle) != (B+F(1))*signed_area(rectangle)
    assert checked>0 and closed>0 and different_open>0
    return {"status":"PASS_EXACT_GAUGE_COUNTERMODEL",
            "rational_B":str(B),
            "valid_grid_walks":checked,
            "closed_walks":closed,
            "open_path_distinguishable_representations":different_open,
            "rectangle_loop_flux":str(B),
            "open_path_values":[str(v) for v in path_integrals(open_path)],
            "not_original_maxwell_1856_derivation":True,
            "not_an_empirical_result":True}


if __name__=="__main__":
    print(json.dumps(test(),ensure_ascii=False,sort_keys=True))
