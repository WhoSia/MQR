"""Action-language enlargement under EXTERNALLY warranted executability.

Finite deterministic analyst-oracle model; the common state space and readout
semantics are GIVEN, not inferred from alien or independent laboratories.
This is an operational possibility witness, not actual contact/invention.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class NamedAction:
    name: str
    mapping: tuple[int, ...]


@dataclass(frozen=True)
class ActionLanguage:
    observation: tuple[str, ...]
    actions: tuple[NamedAction, ...] = ()

    def __post_init__(self):
        n=len(self.observation)
        if not 2 <= n <= 5 or any(not s for s in self.observation):
            raise ValueError("Requires 2..5 states and nonempty outcomes")
        names=[a.name for a in self.actions]
        if len(set(names)) != len(names):
            raise ValueError("Primitive action names must be distinct")
        for a in self.actions:
            if not a.name or len(a.mapping)!=n or any(
                not isinstance(v,int) or isinstance(v,bool) or v<0 or v>=n
                for v in a.mapping
            ):
                raise ValueError("Invalid deterministic action map")

    @staticmethod
    def compose(f,g):
        """f after g, with indices naming states in analyst world."""
        return tuple(f[g[i]] for i in range(len(f)))

    def closure_with_words(self) -> dict[tuple[int,...],tuple[str,...]]:
        n=len(self.observation)
        identity=tuple(range(n))
        words={identity:()}
        queue=deque([identity])
        while queue:
            before=queue.popleft()
            for primitive in self.actions:
                successor=self.compose(primitive.mapping,before)
                if successor not in words:
                    words[successor]=words[before]+(primitive.name,)
                    queue.append(successor)
        return words

    def equivalence_classes(self) -> tuple[tuple[int,...],...]:
        """s~t iff all words in the existing action monoid yield same readout."""
        maps=tuple(sorted(self.closure_with_words()))
        groups={}
        for state in range(len(self.observation)):
            signature=tuple(self.observation[action[state]] for action in maps)
            groups.setdefault(signature,[]).append(state)
        return tuple(sorted(tuple(block) for block in groups.values()))


@dataclass(frozen=True)
class GeneratorTrial:
    base: ActionLanguage
    proposed: NamedAction
    externally_certified_executable: bool

    def analyze(self):
        augmented=ActionLanguage(self.base.observation,
                                 self.base.actions+(self.proposed,))
        old_words=self.base.closure_with_words()
        old_blocks=self.base.equivalence_classes()
        if not self.externally_certified_executable:
            return dict(certified=False,novel=False,strict_refinement=False,
                        old_blocks=old_blocks,new_blocks=old_blocks,
                        old_operations=len(old_words),new_operations=len(old_words),
                        witness=None)
        new_words=augmented.closure_with_words()
        new_blocks=augmented.equivalence_classes()
        witness=None
        for block in old_blocks:
            for j,first in enumerate(block):
                for second in block[j+1:]:
                    candidates=[
                        (len(word),word,first,second,
                         self.base.observation[mapping[first]],
                         self.base.observation[mapping[second]])
                        for mapping,word in new_words.items()
                        if self.base.observation[mapping[first]] !=
                           self.base.observation[mapping[second]]
                    ]
                    if candidates:
                        _,word,s,t,ys,yt=min(candidates)
                        witness=dict(states=(s,t),word=word,outputs=(ys,yt))
                        break
                if witness is not None:
                    break
            if witness is not None:
                break
        return dict(certified=True,
                    novel=self.proposed.mapping not in old_words,
                    strict_refinement=witness is not None,
                    old_blocks=old_blocks,new_blocks=new_blocks,
                    old_operations=len(old_words),new_operations=len(new_words),
                    witness=witness)
