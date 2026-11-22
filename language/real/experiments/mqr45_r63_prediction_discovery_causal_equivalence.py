"""MQR Chat45 R63: two causal explanations of one identical research history.

This binary SCM is SYNTHETIC, not a quantitative reconstruction of
Dirac, Anderson, or any named scientist. Exact rational enumeration.
"""
from fractions import Fraction as Q


def observational_world(causal_prediction_to_action):
    distribution = {}
    for u in (0, 1):
        p = u
        a = p if causal_prediction_to_action else u
        d = a
        i = p*d
        record = (p, a, d, i)
        distribution[record] = distribution.get(record, Q(0)) + Q(1,2)
    return distribution


def interventional_action_probability(causal_prediction_to_action, fixed_prediction):
    assert fixed_prediction in (0,1)
    return sum(Q((fixed_prediction if causal_prediction_to_action else u),2)
               for u in (0,1))


def test():
    directed = observational_world(True)
    confounded = observational_world(False)
    expected = {(0,0,0,0):Q(1,2), (1,1,1,1):Q(1,2)}
    assert directed == confounded == expected
    assert interventional_action_probability(True,1) == 1
    assert interventional_action_probability(True,0) == 0
    assert interventional_action_probability(False,1) == Q(1,2)
    assert interventional_action_probability(False,0) == Q(1,2)
    effect_directed = interventional_action_probability(True,1)-interventional_action_probability(True,0)
    effect_confounded = interventional_action_probability(False,1)-interventional_action_probability(False,0)
    assert (effect_directed,effect_confounded) == (1,0)
    return {"observational_table_identical": True, "prediction_action_causal_effect": [1,0]}


if __name__ == "__main__":
    print(test())
