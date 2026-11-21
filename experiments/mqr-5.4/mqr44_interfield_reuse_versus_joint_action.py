"""MQR 5.4: interfield evidence repurposing versus materially new joint action.
Exact synthetic four-state witness; not historical, physical or philosophical novelty.
"""
from itertools import product
S = tuple(product((0, 1), repeat=2))
def a(s): return s[0]
def b(s): return s[1]
def fa(s): return (1-s[0], s[1])
def fb(s): return (s[0], 1-s[1])
def port(s): return (s[0] ^ s[1], s[1])
def post(read, action): return lambda s: read(action(s))
def classes(fns):
    return len({tuple(f(s) for f in fns) for s in S})
def tests():
    # A cannot distinguish y by either local flip, regardless of repetitions.
    assert classes((a, post(a, fa), post(a, fb))) == 2
    # If the same preparation is reliably paired, exchanging B's pre-existing
    # sensor records extends A's answerable questions WITHOUT new material action.
    assert classes((a, b)) == 4
    # A cross-conditional physical port also exposes y to A, but changes state.
    assert classes((a, post(a, port))) == 4
    assert all((a(s), b(s)) == s for s in S)
    assert any(port(s) != s for s in S)
    assert classes((a, post(a, fb))) == 2
    # Reliable, nondisturbing report of B's y enables feedback simulation of c.
    feedback = lambda s: fa(s) if b(s) == 1 else s
    assert all(feedback(s) == port(s) for s in S)
    # Fixed local-action words cannot conditionally modify x based on y.
    for n in range(6):
        for word in product((fa, fb), repeat=n):
            def apply(s):
                for f in word: s = f(s)
                return s
            assert any(apply(s) != port(s) for s in S)
    # Same passive marginal histograms give NO evidence of event pairing.
    assert [sum(a(s) == bit for s in S) for bit in (0,1)] == [2,2]
    assert [sum(b(s) == bit for s in S) for bit in (0,1)] == [2,2]
    return True
if __name__ == '__main__':
    assert tests()
    print('PASS: scoped exact assertions (finite synthetic model; no real world contact)')
    print('A only:', classes((a, post(a, fa), post(a, fb))))
    print('A+B paired records:', classes((a, b)))
    print('A + joint operation:', classes((a, post(a, port))))
