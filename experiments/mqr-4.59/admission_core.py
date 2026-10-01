from dataclasses import dataclass

@dataclass(frozen=True)
class Case:
    name: str
    executable: str = "NONE"
    contact: str = "NONE"
    repair: str = "NONE"
    deletion: bool = False
    compression: bool = False
    claim_reduction: bool = False
    localization: bool = False
    authority_correction: bool = False
    option_value: bool = False
    criterion_audit: bool = True
    live_consequence: bool = True
    archive_value: bool = False
    provenance: bool = True
    presealed: bool = True

def prior_rule(c: Case) -> str:
    if c.executable != "NONE" or c.contact != "NONE" or c.repair != "NONE":
        return "PROMOTION_CANDIDATE"
    return "COMPRESS_NO_PROMOTION"

def revised_relation(c: Case) -> str:
    if not (c.provenance and c.presealed and c.criterion_audit):
        return "HOLD"
    material = any((
        c.executable == "MATERIAL",
        c.contact == "INDEPENDENT",
        c.repair == "SCIENTIFIC",
        c.deletion,
        c.compression,
        c.claim_reduction,
        c.localization,
        c.authority_correction,
        c.option_value,
    ))
    if c.live_consequence and material:
        return "PROMOTE"
    if c.archive_value and not c.live_consequence:
        return "ARCHIVE"
    if c.executable == "FORMAL_ONLY" or c.contact == "DUPLICATE" or c.repair == "ENGINEERING":
        return "COMPRESS"
    return "REJECT"
