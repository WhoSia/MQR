"""MQR-5.3 R46: finite typed rival-verdict discriminability witness.

Analyst-supplied toy rivals are NOT historical philosophers' positions.
No universal score, empirical result, or new language syntax is claimed.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Callable, Mapping


class Judgment(str, Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


class Question(str, Enum):
    PURSUIT = "pursuit"  # Legacy probe: permissibility, not comparative priority.
    PURSUIT_PRIORITY = "pursuit_priority"
    ACCEPTANCE = "acceptance"
    PROGRESS = "progress"


@dataclass(frozen=True)
class Verdict:
    question: Question
    judgment: Judgment


@dataclass(frozen=True)
class Rival:
    name: str
    decide: Callable[[Mapping[str, bool]], Verdict]


@dataclass(frozen=True)
class Witness:
    conditions: tuple[tuple[str, bool], ...]
    left: Verdict
    right: Verdict


def competing_witnesses(
    left: Rival, right: Rival, condition_names: tuple[str, ...], question: Question,
) -> tuple[Witness, ...]:
    """Locate determinate verdict disagreements over a finite case space.

    UNKNOWN never counts as disagreement. All verdicts must address
    the same question: pursuit-permissibility, pursuit-priority, acceptance\n    and progress are not synonyms.
    """
    if len(set(condition_names)) != len(condition_names):
        raise ValueError("Condition names must be unique")
    if not condition_names:
        raise ValueError("Provide at least one case condition")
    if len(condition_names) > 16:
        raise ValueError("Finite enumeration limited to 16 Boolean conditions")
    result = []
    for values in product((False, True), repeat=len(condition_names)):
        assignment = dict(zip(condition_names, values))
        a, b = left.decide(assignment), right.decide(assignment)
        if a.question != question or b.question != question:
            raise ValueError("Rival verdicts must answer the same requested question")
        if a.judgment is Judgment.UNKNOWN or b.judgment is Judgment.UNKNOWN:
            continue
        if a.judgment != b.judgment:
            result.append(Witness(tuple(assignment.items()), a, b))
    return tuple(result)


def recorded_outcome(verdict: Verdict, verified_evidence: bool | None) -> str:
    """Historical evidential support and modeled verdict remain distinct."""
    if verified_evidence is None:
        return "historical-evidence-hold"
    if verdict.judgment is Judgment.UNKNOWN:
        return "verdict-underdetermined"
    return "evidence-available-for-independent-review"


def example_rivals() -> tuple[Rival, Rival]:
    """Invented toy rules; NOT models of Dewey, Kuhn, Chang, etc."""
    def exploratory(c: Mapping[str, bool]) -> Verdict:
        return Verdict(Question.PURSUIT, Judgment.YES if c["feasible"] and c["new_question"] else Judgment.NO)

    def confirmation_first(c: Mapping[str, bool]) -> Verdict:
        return Verdict(Question.PURSUIT, Judgment.YES if c["feasible"] and c["independent_support"] else Judgment.NO)

    return Rival("toy-exploratory", exploratory), Rival("toy-confirmation-first", confirmation_first)
