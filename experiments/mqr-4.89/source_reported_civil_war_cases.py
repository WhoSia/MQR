"""MQR-4.89 source-grounded civil-war leakage receipt court.
Reported evidence, NOT independent ML replication.
Source: Kapoor & Narayanan (2023), Patterns 4:100804, Figure 3.
"""
from dataclasses import dataclass
DOI = "10.1016/j.patter.2023.100804"
SOURCE_REPORTED = "SOURCE_REPORTED"
REOPEN = "REOPEN_ORIGINAL_EVALUATION"
HOLD = "HOLD_INDEPENDENT_VALIDATION"
@dataclass(frozen=True)
class Study:
    key: str
    leakage: tuple[str, ...]
    mechanism: str
    corrected_report: str
    origin: str = SOURCE_REPORTED
    original_data_replicated_by_mqr: bool = False
STUDIES = (
    Study("Muchlinski", ("L1.2",), "joint train-test imputation", "RF no better than LR"),
    Study("Colaresi-Mahmood", ("L1.2",), "reused improperly imputed data", "RF no better than LR"),
    Study("Wang", ("L1.2","L3.1"), "imputed-data reuse and temporal k-fold leakage", "AUC margin 0.14 to 0.01"),
    Study("Kaufman", ("L2","L3.1"), "target proxy and temporal k-fold leakage", "AdaBoost superiority disappears"),
)
def adjudicate(study):
    if not study.leakage: return ("NOT_AUDITED", "NOT_AUDITED", False)
    return (REOPEN, HOLD, True)
def test():
    expected = {"Muchlinski": ("L1.2",), "Colaresi-Mahmood": ("L1.2",),
                "Wang": ("L1.2","L3.1"), "Kaufman": ("L2","L3.1")}
    for study in STUDIES:
        assert study.leakage == expected[study.key]
        assert study.origin == SOURCE_REPORTED
        assert study.original_data_replicated_by_mqr is False
        assert adjudicate(study) == (REOPEN, HOLD, True)
    assert adjudicate(Study("unreviewed", (), "", "")) == ("NOT_AUDITED","NOT_AUDITED",False)
    print("MQR489_REPORTED_STUDIES=4")
    print("MQR489_CASES_PASS=4")
    print("MQR489_NEGATIVE_CONTROL=PASS")
    print("MQR489_INDEPENDENT_REPLICATION=NOT_PERFORMED")
if __name__ == "__main__":
    test()
