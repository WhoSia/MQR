from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class Checkpoint:
    date: str
    label: str
    eligible: Optional[bool]
    mapping: str
    mode: str
    historical_action: str
    source_key: str

@dataclass(frozen=True)
class NaturalisticCase:
    case_id: str
    domain: str
    target: str
    projection: str
    window_kind: str
    stop_window: Optional[Tuple[int, int]]
    checkpoints: Tuple[Checkpoint, ...]
    note: str

CASES = (
    NaturalisticCase(
        "C01","PARTICLE_TIMING",
        "superluminal-neutrino anomaly as an authoritative measurement claim",
        "UNIQUE","IDENTIFIED_WINDOW",(3,4),
        (
            Checkpoint("2011-09-23","initial OPERA anomaly",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","OPERA_2011"),
            Checkpoint("2011-11-18","short-bunch confirmation but independent checks still live",False,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","CERN_2011_UPDATE"),
            Checkpoint("2012-02-23","two possible timing-system effects identified",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","CERN_2012_TIMING"),
            Checkpoint("2012-06-08","Gran Sasso experiments consistent with c; timing fault identified",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","CERN_2012_GRAN_SASSO"),
            Checkpoint("2012-12-06","dedicated OPERA beam confirms revised result",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","OPERA_2012_DEDICATED"),
        ),
        "Instrument-debt exhaustion supports a bounded claim-freeze window."
    ),
    NaturalisticCase(
        "C02","CMB_POLARIMETRY",
        "primordial-tensor interpretation of the BICEP2 B-mode excess",
        "MULTI_MODE","IDENTIFIED_WINDOW",(3,4),
        (
            Checkpoint("2014-03-17","BICEP2 excess; dust explicitly not excluded",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","BICEP2_2014"),
            Checkpoint("2014-05-22","foreground-sensitive reanalysis keeps dust live",False,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","MORTONSON_SELJAK_2014"),
            Checkpoint("2014-09-22","Planck polarized-dust evidence increases foreground pressure",False,"BOUNDED","CLAIM_FREEZE","CONTINUE_PROBING","PLANCK_DUST_2014"),
            Checkpoint("2015-01-30","joint public result: no conclusive primordial-wave evidence",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","ESA_JOINT_2015"),
            Checkpoint("2015-02-02","joint BICEP2/Keck/Planck analysis posted",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","JOINT_BKP_2015"),
        ),
        "Claim closure and continued CMB observation are different authority modes."
    ),
    NaturalisticCase(
        "C03","MICROBIAL_BIOCHEMISTRY",
        "arsenate substitution for phosphate in GFAJ-1 biomolecules",
        "MULTI_MODE","IDENTIFIED_WINDOW",(2,3),
        (
            Checkpoint("2010-12-02","arsenic-life claim announced; replication and contamination issues live",False,"BOUNDED","HANDOFF","HANDOFF","GFAJ1_2010"),
            Checkpoint("2011-05-27","technical criticism targets phosphate contamination and DNA purification",False,"BOUNDED","HANDOFF","CONTINUE_PROBING","GFAJ1_COMMENTS_2011"),
            Checkpoint("2012-07-08","independent studies show phosphate dependence and no detectable DNA arsenate",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","ERB_REAVES_2012"),
            Checkpoint("2012-07-27","independent studies appear in Science",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","SCIENCE_2012_PUBLICATION"),
        ),
        "Independent-lab handoff resolves a claim while the organism remains scientifically interesting."
    ),
    NaturalisticCase(
        "C04","COLLIDER_PHYSICS",
        "existence of a new boson near 125 GeV",
        "MULTI_MODE","IDENTIFIED_WINDOW",(1,2),
        (
            Checkpoint("2011-12-13","ATLAS/CMS hints explicitly below discovery authority",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","CERN_HIGGS_2011"),
            Checkpoint("2012-07-04","independent ATLAS/CMS five-sigma new-particle observations",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","CERN_HIGGS_2012"),
            Checkpoint("2012-07-31","discovery analyses enter publication record",True,"EXACT","CLAIM_FREEZE","CONTINUE_PROBING","ATLAS_CMS_2012_PAPERS"),
            Checkpoint("2013-03-14","more data support Higgs-boson identity; SM identity still open",True,"EXACT","CLAIM_FREEZE","CONTINUE_PROBING","CERN_HIGGS_2013"),
        ),
        "Positive convergence freezes the existence claim while identity/property inquiry continues."
    ),
    NaturalisticCase(
        "C05","GW_INTERFEROMETRY",
        "GW150914 as an astrophysical gravitational-wave detection",
        "MULTI_MODE","IDENTIFIED_WINDOW",(2,3),
        (
            Checkpoint("2015-09-14","low-latency candidate triggers validation programme",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","LIGO_EVENT_2015"),
            Checkpoint("2015-10-16","detection case strong but review, calibration and detchar work remain",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","LIGO_DETECTION_CASE"),
            Checkpoint("2016-01-28","review feedback accepts analyses and conclusions",True,"BOUNDED","CLAIM_FREEZE","CLAIM_FREEZE","LIGO_REVIEW_2016"),
            Checkpoint("2016-02-11","public discovery paper and announcement",True,"EXACT","CLAIM_FREEZE","CLAIM_FREEZE","LIGO_PUBLIC_2016"),
            Checkpoint("2016-11-30","observatory resumes search after upgrades",True,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","LIGO_O2_2016"),
        ),
        "A discovery claim can close while an observatory keeps searching and improving calibration."
    ),
    NaturalisticCase(
        "C06","CLINICAL_MICROBIOLOGY",
        "H. pylori causal/action authority for peptic-ulcer disease",
        "MULTI_MODE","CONTRACT_DEPENDENT",None,
        (
            Checkpoint("1983-06-04","curved bacilli reported in active chronic gastritis",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","WARREN_MARSHALL_1983"),
            Checkpoint("1984-06-16","100-patient association and culture study",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","MARSHALL_WARREN_1984"),
            Checkpoint("1985-04-15","human inoculation establishes induced gastritis",False,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","MARSHALL_1985"),
            Checkpoint("1988-12-01","double-blind eradication trial links eradication to relapse prevention",True,"PROXY","PROVISIONAL_USE","PROVISIONAL_USE","MARSHALL_1988_RCT"),
            Checkpoint("1993-12-01","systematic causal overview separates disease-specific authority",True,"PROXY","PROVISIONAL_USE","PROVISIONAL_USE","H_PYLORI_OVERVIEW_1993"),
        ),
        "Treatment-use authority and broad causal/mechanistic closure have different stop windows."
    ),
    NaturalisticCase(
        "C07","PLANETARY_SPECTROSCOPY",
        "phosphine detection in the atmosphere of Venus",
        "MULTI_MODE","RIGHT_CENSORED",None,
        (
            Checkpoint("2020-09-14","reported spectral phosphine detection",False,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","VENUS_PH3_2020"),
            Checkpoint("2020-11-20","ALMA processing error and recalibration warning",False,"EXACT","CLAIM_FREEZE","CONTINUE_PROBING","VENUS_EDITOR_NOTE_2020"),
            Checkpoint("2021-07-16","independent analysis reports no evidence / discrepant upper limits",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","VENUS_REANALYSIS_2021"),
            Checkpoint("2022-10-24","SOFIA analysis reports strict upper limit",False,"EXACT","CONTINUE_PROBING","CONTINUE_PROBING","SOFIA_UPPER_2022"),
            Checkpoint("2022-11-17","counter-reanalysis recovers candidate signal and calls for further work",False,"BOUNDED","CONTINUE_PROBING","CONTINUE_PROBING","SOFIA_RECOVERY_2022"),
        ),
        "Discordant calibration/reanalysis leaves the episode right-censored rather than cleanly stopped."
    ),
)

PRIMARY_COUNT = len(CASES)
SENSITIVITY_CASES = ("C08_ANTARCTIC_OZONE",)
REJECTED_CASES = ("C09_HUBBLE_TENSION",)
