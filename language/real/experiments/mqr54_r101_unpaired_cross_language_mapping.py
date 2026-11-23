"""MQR R101: unpaired marginals cannot determine a cross-language bit mapping.

Two hypothetical measurement communities A and B may each record fair
binary marginals from a physical process; unknown relabeling z=0 or z=1
is indistinguishable without authentic joint events. Pairing same event
identifies z in this toy setup IF matching is valid, readout maps are
stable and B's observation is nonperturbing. Without those premises, no
empirical science-to-science translation has been achieved.

Exact finite enumeration, NOT an actual alien-civilization experiment.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import permutations
import json

WORLD = (0, 0, 1, 1)


def observed_B(z: int) -> tuple[int, ...]:
    assert z in (0, 1)
    return tuple(s ^ z for s in WORLD)


def marginal(obs: tuple[int, ...]) -> tuple[F, F]:
    n=len(obs)
    return F(obs.count(0),n),F(obs.count(1),n)


def agreement(a: tuple[int, ...],b: tuple[int, ...]) -> F:
    if len(a)!=len(b):
        raise ValueError("pair length mismatch")
    return F(sum(x==y for x,y in zip(a,b)),len(a))


def test() -> dict:
    a=WORLD
    b0=observed_B(0)
    b1=observed_B(1)
    assert marginal(a)==marginal(b0)==marginal(b1)==(F(1,2),F(1,2))
    assert agreement(a,b0)==1
    assert agreement(a,b1)==0
    # A joint record of the very same four stable events distinguishes
    # z. An independent permutation of the B IDs is NOT valid pairing.
    all_perms = list(permutations(range(4)))
    shuffled=[agreement(a,tuple(b0[i] for i in p)) for p in all_perms]
    assert len(all_perms)==24
    assert sum(shuffled,F(0))/len(shuffled)==F(1,2)
    assert sorted(set(shuffled))==[F(0),F(1,2),F(1)]
    assert shuffled.count(F(0))==4
    assert shuffled.count(F(1,2))==16
    assert shuffled.count(F(1))==4
    # A strong false positive: every readout marginal unchanged,
    # yet individual cross-instrument mapping can be reversed.
    assert all(marginal(tuple(b0[i] for i in p))==marginal(b0)
               for p in all_perms)
    return {"result":"PASS_FINITE_UNPAIRED_MAPPING_COUNTERMODEL",
            "unpaired_mapping_identifiable":False,
            "correctly_paired_mapping_identifiable_under_assumptions":True,
            "pairings_enumerated":24,
            "permuted_agreement_mean":"1/2",
            "agreement_histogram":{"0":4,"1/2":16,"1":4},
            "actual_matched_experiment_performed":False,
            "universal_alien_translation_proved":False}


if __name__=="__main__":
    print(json.dumps(test(),sort_keys=True))
