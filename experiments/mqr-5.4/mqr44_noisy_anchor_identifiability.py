"""MQR 5.4: exact two-bridge inference under independently warranted anchor data.

Synthetic only. The reliability and independence of anchor matches are assumptions,
NOT conclusions that can be derived from two scientists' native transcripts.
"""
from fractions import Fraction as F
from math import prod

EPSILON = F(1, 5)


def likelihood(bits, hypothesis, epsilon=EPSILON):
    """hypothesis=0: agreed polarity; hypothesis=1: complementary polarity.
    A bit 1 means an externally MATCHED physical calibration event supports
    'same native readout' after declared local encoding.
    """
    assert hypothesis in (0, 1)
    assert F(0) < epsilon < F(1, 2)
    assert all(bit in (0, 1) for bit in bits)
    matching_bit = 1 - hypothesis
    return prod((1-epsilon if bit == matching_bit else epsilon for bit in bits), start=F(1))


def posterior(bits, epsilon=EPSILON):
    """Equal prior; only valid for genuinely conditionally independent anchors."""
    L0 = likelihood(bits, 0, epsilon)
    L1 = likelihood(bits, 1, epsilon)
    return (L0 / (L0 + L1), L1 / (L0 + L1))


def exact_cases():
    assert posterior(()) == (F(1, 2), F(1, 2))
    assert posterior((1,)) == (F(4, 5), F(1, 5))
    assert posterior((1, 1, 1)) == (F(64, 65), F(1, 65))
    assert posterior((0, 0, 0)) == (F(1, 65), F(64, 65))
    assert posterior((1, 1, 1, 1, 1)) == (F(1024, 1025), F(1, 1025))
    # Five copies of one physical event are ONE lineage, not five independent anchors.
    assert posterior((1,)) != posterior((1, 1, 1, 1, 1))
    # An adversarial systematic flip of one lineage would make the naive
    # independent model confident in the wrong bridge; arithmetic demonstrates
    # the model-misspecification trap, not the probability of such failures.
    assert posterior((0,)*5)[1] == F(1024, 1025)
    return True


if __name__ == '__main__':
    assert exact_cases()
    print('PASS 7 exact model-internal assertions; 0 physical anchor events verified')
    for label, bits in [('no externally anchored event', ()),
                        ('one matched event', (1,)),
                        ('three independent matched events (assumed)', (1,1,1)),
                        ('five duplicated events wrongly treated independent', (1,)*5)]:
        print(label, posterior(bits))
