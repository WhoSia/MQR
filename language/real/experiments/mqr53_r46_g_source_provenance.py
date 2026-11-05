"""MQR R46-G: source origin and transmission must not be conflated.

A translated primary writing remains evidence of an actor's stated
position, subject to edition and translation fidelity. It is not
automatically a contemporary *physical edition*.
"""
from dataclasses import dataclass
from enum import Enum


class Origin(str, Enum):
    ACTOR = "actor"
    HISTORIAN = "historian"


class Transmission(str, Enum):
    ORIGINAL_EDITION = "original_edition"
    LATER_TRANSLATION = "later_translation"
    EDITED_ESTATE = "edited_estate"
    SECONDARY_QUOTATION = "secondary_quotation"


@dataclass(frozen=True)
class Evidence:
    title: str
    authored_year: int | None
    accessed_edition_year: int
    origin: Origin
    transmission: Transmission
    independently_collated: bool = False


def is_actor_position(evidence: Evidence) -> bool:
    """A primary-in-origin passage may survive in later translation."""
    return evidence.origin is Origin.ACTOR and evidence.transmission is not Transmission.SECONDARY_QUOTATION


def original_wording_verified(evidence: Evidence) -> bool:
    """Original word-for-word parity requires independent original collation."""
    return (is_actor_position(evidence)
            and evidence.independently_collated
            and evidence.transmission is Transmission.ORIGINAL_EDITION)


def available_at(evidence: Evidence, decision_year: int) -> bool:
    """Minimal publication-era gate; not evidence of actor's actual access."""
    return evidence.authored_year is not None and evidence.authored_year <= decision_year


def can_attest_direct_original_letter(evidence: Evidence) -> bool:
    """A historian's quotation is not independent possession of the letter."""
    return (evidence.origin is Origin.ACTOR
            and evidence.transmission is Transmission.ORIGINAL_EDITION
            and evidence.independently_collated)


WEYL_1921_VIA_1998 = Evidence(
    "Weyl 1921, translated in Mancosu 1998", 1921, 1998,
    Origin.ACTOR, Transmission.LATER_TRANSLATION,
)
BROUWER_ESTATE_VIA_1998 = Evidence(
    "Brouwer comments on Weyl, edited in Mancosu 1998", 1921, 1998,
    Origin.ACTOR, Transmission.EDITED_ESTATE,
)
FRAENKEL_1923_VIA_KISH_2022 = Evidence(
    "Fraenkel letter 18 Apr 1923 quoted via Kish Bar-On 2022", 1923, 2022,
    Origin.ACTOR, Transmission.SECONDARY_QUOTATION,
)
