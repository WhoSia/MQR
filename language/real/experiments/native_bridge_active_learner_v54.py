"""MQR 43: minimal active native-outcome queries over a FROZEN analyst hypothesis set.

An oracle contains a hidden simulated alignment; the learner only receives
native action-word outputs. This is NOT unsupervised concept invention or
independent physical validation. No latent state IDs appear in exported logs.
"""
from collections import Counter
from dataclasses import dataclass

from native_composition_bootstrap_v54 import (
    ProposedBridge, TransferReceipt, all_alignments,
)
from native_bridge_query_design_v54 import (
    Probe, candidate_probes, predict,
)


@dataclass(frozen=True)
class FrozenOracle:
    _bridge: ProposedBridge
    receipt: TransferReceipt
    b_sensor_visible: bool

    def ask(self, probe):
        if not self.receipt.admissible:
            raise RuntimeError('Physical-token, preparation and reset gates are not met')
        return predict(self._bridge, probe, self.b_sensor_visible)


class NativeLearner:
    def __init__(self, b_sensor_visible=False, max_word_length=3):
        self.b_sensor_visible = b_sensor_visible
        self.probes = candidate_probes(max_word_length, allow_a=True, allow_b=True)
        self._candidates = tuple(all_alignments())
        self.ledger = []  # native action words/results only; no guessed absolute labels

    @property
    def candidate_count(self):
        return len(self._candidates)

    def choose(self):
        best = None
        best_score = None
        used = {(tuple(record['word']), record['reader']) for record in self.ledger}
        for probe in self.probes:
            if (probe.word, probe.reader) in used:
                continue
            tally = Counter(predict(ProposedBridge(p), probe,
                                    self.b_sensor_visible) for p in self._candidates)
            if len(tally) < 2:
                continue
            score = (max(tally.values()), probe.primitive_cost, probe.reader, probe.word)
            if best_score is None or score < best_score:
                best, best_score = probe, score
        return best

    def record(self, probe, observed):
        if not isinstance(probe, Probe) or probe not in self.probes:
            raise ValueError('Probe is outside the frozen admitted query menu')
        if any(row['word'] == probe.word and row['reader'] == probe.reader for row in self.ledger):
            raise ValueError('Repeated query refused by this deterministic protocol')
        next_candidates = tuple(p for p in self._candidates if
            predict(ProposedBridge(p), probe, self.b_sensor_visible) == observed)
        if not next_candidates:
            raise ValueError('Observed output falsifies the entire frozen candidate set')
        before = len(self._candidates)
        self._candidates = next_candidates
        self.ledger.append(dict(word=probe.word, reader=probe.reader,
                                observed=observed, before=before,
                                remaining=len(next_candidates)))

    def learn(self, oracle, max_queries=8):
        if not isinstance(oracle, FrozenOracle) or not oracle.receipt.admissible:
            raise RuntimeError('External custody/reset assumptions not met')
        if self.b_sensor_visible != oracle.b_sensor_visible:
            raise ValueError('Native sensor exposure protocol mismatch')
        for _ in range(max_queries):
            probe = self.choose()  # DOES NOT accept oracle or the actual alignment
            if probe is None:
                break
            result = oracle.ask(probe)
            self.record(probe, result)
        return tuple(dict(row) for row in self.ledger)

    def heldout_prediction(self, probe):
        if not isinstance(probe, Probe) or probe not in self.probes:
            raise ValueError('Held-out probe must use the frozen query grammar')
        if any(row['word'] == probe.word and row['reader'] == probe.reader for row in self.ledger):
            raise ValueError('Held-out probe was used during selection')
        options = {predict(ProposedBridge(p), probe, self.b_sensor_visible)
                   for p in self._candidates}
        return next(iter(options)) if len(options) == 1 else None

    def simulated_heldout_check(self, oracle, probe):
        if not isinstance(oracle, FrozenOracle) or not oracle.receipt.admissible:
            raise RuntimeError('No certified query channel')
        expected = self.heldout_prediction(probe)
        if expected is None:
            return 'HOLD_UNIDENTIFIED'
        return 'PASS_SIMULATOR' if oracle.ask(probe) == expected else 'FAIL_SIMULATOR'
