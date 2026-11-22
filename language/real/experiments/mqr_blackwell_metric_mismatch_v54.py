"""Two-channel Blackwell checks on binary states, all probabilities rational.

Synthetic information model only: not a model of RNA chemistry or human memory.
"""
from fractions import Fraction as Q

STATES = (0, 1)
PRIOR = (Q(1, 2), Q(1, 2))

# Every channel maps state theta to a probability vector over outputs {0,1}.
PERFECT = ((Q(1), Q(0)), (Q(0), Q(1)))
OLD = ((Q(3, 4), Q(1, 4)), (Q(1, 4), Q(3, 4)))
BLIND = ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2)))


def compose(channel, kernel):
    return tuple(tuple(sum(channel[t][x] * kernel[x][y]
                           for x in STATES) for y in STATES)
                 for t in STATES)


def decision_value(channel, prior=PRIOR):
    """Optimal expected zero-one classification reward for binary state and output."""
    return sum(max(prior[t] * channel[t][y] for t in STATES)
               for y in STATES)


def compare_all_binary_priors(fine, coarse):
    for k in range(101):
        prior = (Q(k, 100), Q(100-k, 100))
        assert decision_value(fine, prior) >= decision_value(coarse, prior)


def verify():
    assert compose(PERFECT, OLD) == OLD
    assert compose(OLD, BLIND) == BLIND
    assert tuple(map(decision_value, (PERFECT, OLD, BLIND))) == (
        Q(1), Q(3, 4), Q(1, 2))
    compare_all_binary_priors(PERFECT, OLD)
    compare_all_binary_priors(OLD, BLIND)

    # 'Recovery yield' is a separate declared metric, not a channel order.
    yield_old, yield_replacement = Q(3, 5), Q(4, 5)
    assert yield_replacement > yield_old
    assert decision_value(BLIND) < decision_value(OLD)

    # Keeping the original signal plus the new auxiliary metric cannot hurt.
    joint_old_and_yield = OLD  # yield is a constant ancillary observation
    assert decision_value(joint_old_and_yield) == decision_value(OLD)
    return 'PASS Blackwell: V(perfect)=1, V(old)=3/4, V(blind)=1/2; yield reversal is different metric'


if __name__ == '__main__':
    print(verify())
