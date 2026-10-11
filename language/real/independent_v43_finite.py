#!/usr/bin/env python3
"""Independent finite oracle for REALREPRESENT v0.43; no physical-world claims.

Enumerate *all* triples (source observation O, postprocessor g, target Q) on
three possible histories, with three-valued source/codomain/target alphabet:
3^3 * 3^3 * 3^3 = 19,683 complete model cases. Tests the exact finite kernel
ordering property and target-relative sufficiency, NOT the completeness of H.
"""
from itertools import product

def factors(o, q):
    return all(o[i] != o[j] or q[i] == q[j]
               for i in range(len(o)) for j in range(i + 1, len(o)))

def same_partition(a, b):
    return all((a[i] == a[j]) == (b[i] == b[j])
               for i in range(len(a)) for j in range(i + 1, len(a)))

def run():
    values = tuple(product(range(3), repeat=3))
    checked = 0
    strict_loss = 0
    loss_keeps_target = 0
    loss_defeats_target = 0
    for src in values:
        for g in values:
            dst = tuple(g[x] for x in src)
            equivalent = same_partition(src, dst)
            for q in values:
                checked += 1
                s = factors(src, q)
                d = factors(dst, q)
                assert not d or s, ("impossible gain from deterministic garbling",
                                   src, g, q)
                if equivalent:
                    assert s == d, ("bijective-on-image representation changed truth",
                                    src, g, q)
                elif s:
                    strict_loss += 1
                    if d:
                        loss_keeps_target += 1
                    else:
                        loss_defeats_target += 1
    assert checked == 19683
    assert strict_loss > 0 and loss_keeps_target > 0 and loss_defeats_target > 0
    print("finite_source_postprocessor_target_cases=", checked)
    print("coarser_representation_source_identifiable_cases=", strict_loss)
    print("target_survived_loss_cases=", loss_keeps_target)
    print("target_defeated_by_loss_cases=", loss_defeats_target)
    print("FINITE_SCIENTIFIC_INFORMATION_ORDER_EXHAUSTIVE_19683_PASS")
    print("BLACKWELL_STOCHASTIC_EXPERIMENT_COMPARISON_NOT_TESTED")
    print("EMPIRICAL_MEASUREMENT_GROUNDING_NOT_TESTED")
if __name__ == "__main__":
    run()
