"""MQR 5.4 Chat45 R68: reproduce reported *rounded* 1972 Bell-test contrasts.

Only published rounded normalized coincidence-rate summaries are inputs.
NOT raw-count reanalysis; no uncertainty propagation from shared denominator.
Based on January 1972 LBL-392 preprint, preserved at UC eScholarship.
"""
from fractions import Fraction as Q

R22 = Q(400, 1000)
R67 = Q(100, 1000)
R1 = Q(497, 1000)
R2 = Q(499, 1000)

def calculate():
    # Two-sided CHSH-style instrument rate constraint: -1 <= D(phi) <= 0
    # At phi=22.5°, 3phi=67.5°; at phi=67.5°, 3phi=202.5°,
    # whose R is same as R(22.5°) by angular periodicity.
    d22 = 3*R22-R67-R1-R2
    d67 = 3*R67-R22-R1-R2
    delta = abs(R22-R67)-Q(1,4)
    assert d22 == Q(104,1000)
    assert d67 == Q(-1096,1000)
    assert delta == Q(50,1000)
    assert d22 > 0 and d67 < -1 and delta > 0

    # If R22 and R67 were individually rounded to the nearest 0.001,
    # their extrema alone imply delta in [0.049,0.051].
    half_round = Q(1,2000)
    delta_min=(R22-half_round)-(R67+half_round)-Q(1,4)
    delta_max=(R22+half_round)-(R67-half_round)-Q(1,4)
    assert (delta_min,delta_max)==(Q(49,1000),Q(51,1000))

    # A 6.25 ratio uses authors' *reported* +/-0.008 uncertainty,
    # not a recomputed sampling variance.
    reported_sigma=Q(8,1000)
    assert delta/reported_sigma==Q(25,4)
    return {"D22_from_rounded":str(d22), "D67_from_rounded":str(d67),
            "delta_from_rounded":str(delta),
            "delta_rounding_interval":[str(delta_min),str(delta_max)],
            "reported_sigma":str(reported_sigma),
            "ratio_to_reported_sigma":str(delta/reported_sigma),
            "raw_count_statistical_reanalysis":False}

if __name__ == "__main__":
    print(calculate())
