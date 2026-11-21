"""MQR 5.4 chat43: anomaly custody outside a frozen native-action learner.

All evidence flags and lineage labels are user-supplied claims, NOT authenticated
world contact. No procedure creates a scientific concept from an exception.
"""
from dataclasses import dataclass
from itertools import permutations

A_SENSOR = ('low', 'low', 'high')
A_TURN = (1, 0, 2)
B_SWAP = (0, 2, 1)
B_CYCLE = (1, 2, 0)
ALPHABET = ('A:turn', 'B:shift')


def native_predict(word, b_operation=B_SWAP, alignment=(0, 1, 2), sensor=A_SENSOR):
    if tuple(sorted(alignment)) != (0, 1, 2):
        raise ValueError('Must specify a bijective three-state alignment')
    if len(b_operation) != 3 or tuple(sorted(b_operation)) != (0, 1, 2):
        raise ValueError('B operation must be a three-state permutation')
    if len(sensor) != 3:
        raise ValueError('A sensor must report each analyst state')
    reverse = tuple(alignment.index(i) for i in range(3))
    state = 0
    for name in word:
        if name == 'A:turn':
            state = A_TURN[state]
        elif name == 'B:shift':
            state = alignment[b_operation[reverse[state]]]
        else:
            raise ValueError('Unknown native action')
    return sensor[state]


def frozen_predictions(word):
    return frozenset(native_predict(word, B_SWAP, p)
                     for p in permutations(range(3)))


@dataclass(frozen=True)
class ClaimedReceipt:
    token_checked: bool
    preparation_stable: bool
    reset_checked: bool
    sensor_calibrated: bool

    def __post_init__(self):
        if any(type(x) is not bool for x in (self.token_checked,
               self.preparation_stable, self.reset_checked,
               self.sensor_calibrated)):
            raise ValueError('Receipt flags must be explicit Booleans')

    @property
    def declared_admissible(self):
        return all((self.token_checked, self.preparation_stable,
                    self.reset_checked, self.sensor_calibrated))


@dataclass(frozen=True)
class ReportedTrial:
    trial_id: str
    lineage_id: str
    word: tuple[str, ...]
    observed: str
    negative_control_observed: str
    receipt: ClaimedReceipt

    def __post_init__(self):
        if (not self.trial_id or not self.lineage_id or
            not isinstance(self.word, tuple) or
            any(x not in ALPHABET for x in self.word) or
            self.observed not in ('low', 'high') or
            self.negative_control_observed not in ('low', 'high') or
            not isinstance(self.receipt, ClaimedReceipt)):
            raise ValueError('Malformed native observation/receipt')


class AnomalyRegister:
    """Keep raw reports; an inadmissible report cannot update model authority.

    No method edits the sealed six-permutation model. A label saying that two
    runs have distinct lineages is NOT proof of noncommon error ancestors.
    """
    def __init__(self):
        self._reports = []
        self._trial_ids = set()

    @property
    def reports(self):
        return tuple(self._reports)

    def add(self, report):
        if not isinstance(report, ReportedTrial):
            raise ValueError('Typed trial required')
        if report.trial_id in self._trial_ids:
            raise ValueError('Duplicate trial_id; append rejected')
        self._trial_ids.add(report.trial_id)
        self._reports.append(report)
        if not report.receipt.declared_admissible:
            return 'QUARANTINED_DECLARED_GATE_FAILED'
        if report.negative_control_observed != 'low':
            return 'QUARANTINED_NEGATIVE_CONTROL_FAILED'
        if report.observed not in frozen_predictions(report.word):
            return 'MODEL_CLASS_MISMATCH_RECORDED'
        return 'FROZEN_MODEL_COMPATIBLE'

    def assess(self, word):
        relevant = [r for r in self._reports if r.word == tuple(word) and
                    r.receipt.declared_admissible and
                    r.negative_control_observed == 'low']
        if not relevant:
            return 'HOLD_NO_QUALIFYING_REPORTS'
        by_lineage = {}
        for r in relevant:
            by_lineage.setdefault(r.lineage_id, set()).add(r.observed)
        if any(len(v) > 1 for v in by_lineage.values()) or len({x for v in
               by_lineage.values() for x in v}) > 1:
            return 'HOLD_INCONSISTENT_RESULTS'
        observed = next(iter(next(iter(by_lineage.values()))))
        if observed in frozen_predictions(word):
            return 'HOLD_COMPATIBLE_WITH_FROZEN_MODEL'
        if len(by_lineage) < 2:
            return 'HOLD_SINGLE_DECLARED_LINEAGE'
        return 'HOLD_CONDITIONAL_FROZEN_CLASS_REFUTATION'


def rival_outputs(word):
    """Analyst-postulated alternatives, no autonomous concept generation."""
    return {
        'old_involution': native_predict(word),
        'three_cycle': native_predict(word, B_CYCLE),
        'global_sensor_inversion': native_predict(word, B_SWAP,
                                                  sensor=('high','high','low')),
        'query_dependent_sensor_artifact': native_predict(word, B_CYCLE),
    }


def prospective_discriminant(word):
    interpretations = rival_outputs(word)
    # Mechanisms with identical predicted outputs are never distinguishable
    # with this word, irrespective of number of repeated experiments.
    return tuple(sorted((a, b) for a in interpretations for b in interpretations
                        if a < b and interpretations[a] != interpretations[b]))
