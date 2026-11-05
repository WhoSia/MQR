"""MQR R46-E: defend historical case comparisons against category errors.

Research-only Python prototype, NOT production Real Lang syntax.
It does not turn historians' interpretations into computational verdicts.
"""
from dataclasses import dataclass
from enum import Enum


class Question(str, Enum):
    PURSUIT = 'pursuit'
    PRIORITY = 'priority'
    ACCEPTANCE = 'acceptance'
    UPTAKE = 'uptake'
    CONTRIBUTION = 'contribution'


class Status(str, Enum):
    SUPPORTED = 'supported'
    REJECTED = 'rejected'
    UNDETERMINED = 'undetermined'


@dataclass(frozen=True)
class HistoricalJudgment:
    case: str
    domain: str
    question: Question
    status: Status
    cutoff_year: int
    source_kind: str  # contemporaneous, later_translation, historiography


def comparable(a: HistoricalJudgment, b: HistoricalJudgment) -> bool:
    """Strict gate for competing judgments about the *same* case/question.

    A comparison does not imply that either judgment is historically sound.
    """
    return (a.case == b.case and a.domain == b.domain
            and a.question == b.question and a.cutoff_year == b.cutoff_year)


def grounded_conflict(a: HistoricalJudgment, b: HistoricalJudgment) -> bool:
    """No conflict inferred from unknown judgments or unmatched questions.

    Later historical writing can describe a past decision, but by itself it
    is not treated as a contemporaneous actor's decision record.
    """
    if not comparable(a, b):
        return False
    if a.status is Status.UNDETERMINED or b.status is Status.UNDETERMINED:
        return False
    if 'contemporaneous' not in (a.source_kind, b.source_kind):
        return False
    return a.status != b.status


def later_uptake_cannot_decide_pursuit(uptake: HistoricalJudgment) -> bool:
    """No bridge from later community adoption to earlier rational pursuit."""
    if uptake.question is not Question.UPTAKE:
        raise ValueError('Expected a later uptake judgment')
    return True
