"""Exact finite enumeration of the two-route reusable competence cost model."""
from itertools import product


def verify():
    cases = crossing = direct = reuse = tie = 0
    for premium, saving in product(range(9), repeat=2):
        for lo in range(11):
            for hi in range(lo, 11):
                losses = []
                signs = set()
                for n in range(lo, hi+1):
                    costs = (3+n*(2+saving), 3+premium+n*2)
                    best = min(costs)
                    losses.append(tuple(c-best for c in costs))
                    signs.add((costs[0]>costs[1])-(costs[0]<costs[1]))
                actual = tuple(map(max, zip(*losses)))
                assert actual == (max(0, hi*saving-premium), max(0, premium-lo*saving))
                crossing += {-1,1} <= signs
                direct += actual[0] < actual[1]
                reuse += actual[1] < actual[0]
                tie += actual[0] == actual[1]
                cases += 1
    assert (cases,crossing,direct,reuse,tie) == (5346,908,950,4243,153)
    print(cases,crossing,direct,reuse,tie)

if __name__ == '__main__':
    verify()
