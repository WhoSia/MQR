"""MQR 5.4 / chat MQR 41: shortest observation path through adjacent swaps.

Proof-of-concept finite enumeration, not claim of original mathematics.
A state is n independent bits, only coordinate 0 is directly read.
One primitive action swaps adjacent coordinates i and i+1.
A protocol word of length <= h can expose exactly coordinates with
distance <= h from the sensor, subject to perfect preparation.
"""
from itertools import product

def observed_source_index(n, word):
    coordinates = list(range(n))
    for i in word:
        coordinates[i], coordinates[i+1] = coordinates[i+1], coordinates[i]
    return coordinates[0]

def accessible_coordinates(n, horizon):
    indices = {0}
    for depth in range(1, horizon+1):
        for word in product(range(n-1), repeat=depth):
            indices.add(observed_source_index(n, word))
    return indices

def check():
    for n in range(2, 7):
        for h in range(min(n-1,4)+1):
            observed = accessible_coordinates(n, h)
            expected = set(range(min(n, h+1)))
            assert observed == expected, (n, h, observed, expected)
        print('n=%d validated horizons 0..%d' % (n, min(n-1,4)))
    for h in range(4):
        k = 2 ** min(3,h+1)
        assert k in (2,4,8)
        print('n=3 h=%d distinguishable_states=%d Boolean_predicates=%d'
              % (h, k, 2**k))
    print('PASS: sensor horizon is bounded by swap-graph distance')

if __name__ == '__main__':
    check()
