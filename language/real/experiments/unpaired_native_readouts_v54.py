"""Native reports do not determine cross-science joint observables without pairing.

All candidate correspondences are merely formal bijections of inventoried
physical tokens. Contact 'anchors' are EXTERNALLY certified, not inferred.
The model does not infer whether the shared specimen state survives transfer.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class LocalInventory:
    tokens: tuple[str, ...]
    outcomes: tuple[str, ...]

    def __post_init__(self):
        n=len(self.tokens)
        if not 1<=n<=8 or len(self.outcomes)!=n:
            raise ValueError('One to eight inventoried local tokens with readouts')
        if len(set(self.tokens))!=n or any(not s for s in self.tokens+self.outcomes):
            raise ValueError('Distinct nonempty token labels and outcomes required')


def _partition(sigs: tuple[tuple[str,str],...]) -> tuple[tuple[int,...],...]:
    groups={}
    for i,signature in enumerate(sigs):
        groups.setdefault(signature,[]).append(i)
    return tuple(sorted(tuple(g) for g in groups.values()))


@dataclass(frozen=True)
class UnpairedInventories:
    a: LocalInventory
    b: LocalInventory
    anchors: tuple[tuple[str,str],...]=()

    def __post_init__(self):
        if len(self.a.tokens)!=len(self.b.tokens):
            raise ValueError('Bijection model requires equal inventory sizes')
        da=set(self.a.tokens);db=set(self.b.tokens)
        if (len(set(x for x,_ in self.anchors))!=len(self.anchors) or
            len(set(y for _,y in self.anchors))!=len(self.anchors) or
            any(x not in da or y not in db for x,y in self.anchors)):
            raise ValueError('Only consistent unique externally certified anchors')

    def hypotheses(self) -> tuple[tuple[tuple[str,...],tuple[tuple[int,...],...]],...]:
        n=len(self.a.tokens)
        ai={name:i for i,name in enumerate(self.a.tokens)}
        out=[]
        for perm in permutations(range(n)):
            if any(self.b.tokens[perm[ai[x]]]!=y for x,y in self.anchors):
                continue
            signatures=tuple((self.a.outcomes[i],self.b.outcomes[perm[i]]) for i in range(n))
            out.append((tuple(self.b.tokens[j] for j in perm),_partition(signatures)))
        return tuple(out)

    def partition_histogram(self) -> dict[tuple[tuple[int,...],...],int]:
        return dict(Counter(partition for _,partition in self.hypotheses()))

    def possible_joint_class_counts(self) -> dict[int,int]:
        return dict(sorted(Counter(len(p) for _,p in self.hypotheses()).items()))
