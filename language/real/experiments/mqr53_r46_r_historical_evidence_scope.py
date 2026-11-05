"""R46-R: conservative evidence-scope checks for historical philosophy.

RESEARCH-ONLY Python fixture, NOT Real Lang production implementation.
Matches *questions* and claimed public access; it does not decide whether
a biological observation is causally valid or a philosopher was right.
"""
from dataclasses import dataclass
from enum import Enum


class Target(str, Enum):
    FRACTION_LABEL = "fraction_radioactivity"
    PEPTIDE_BOND = "alpha_peptide_bond"
    CHARACTERIZED_PROTEIN = "characterized_protein"
    VIRUS_PRODUCT = "specific_virus_protein"


@dataclass(frozen=True)
class HistoricalClaim:
    source: str
    organism: str
    preparation: str
    target: Target
    publication_year: int
    public_access_confirmed: bool
    status: str  # observed, not_observed, tentative, unknown


def same_inferential_question(a: HistoricalClaim, b: HistoricalClaim) -> bool:
    """Identity of a question requires matching biological and target scope."""
    return (a.organism == b.organism
            and a.preparation == b.preparation
            and a.target is b.target)


def actual_opposition(a: HistoricalClaim, b: HistoricalClaim) -> bool:
    """Opposed reports cannot be diagnosed from mismatched targets or samples.

    An opposition here is logical *report disagreement*, not a verdict
    about which report is experimentally better.
    """
    return (same_inferential_question(a, b)
            and {a.status, b.status} == {"observed", "not_observed"})


def accessible_by_year(item: HistoricalClaim, decision_year: int) -> bool:
    """Published-in-time is necessary but NOT enough to prove actual readership.

    Require affirmative public-access evidence, not just a manuscript
    'received' date or a retrospective citation.
    """
    return item.public_access_confirmed and item.publication_year <= decision_year


TOBACCO_FRACTION_1956 = HistoricalClaim(
    "Stephenson et al 1956 abstract", "tobacco", "cell_free_leaf_fraction",
    Target.FRACTION_LABEL, 1956, True, "observed"
)
TOBACCO_TMV_1956 = HistoricalClaim(
    "Stephenson et al 1956 abstract", "tobacco", "virus_infected_cell_free_leaf",
    Target.VIRUS_PRODUCT, 1956, True, "not_observed"
)
SPINACH_1964 = HistoricalClaim(
    "App and Jagendorf 1964", "spinach", "isolated_chloroplast_fraction",
    Target.FRACTION_LABEL, 1964, True, "tentative"
)
