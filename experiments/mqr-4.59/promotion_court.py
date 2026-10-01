from pathlib import Path
import json
from admission_core import Case, prior_rule, revised_relation

CASES = {
    "c01": (Case("c01", deletion=True), "PROMOTE"),
    "c02": (Case("c02", executable="FORMAL_ONLY"), "COMPRESS"),
    "c03": (Case("c03", contact="DUPLICATE"), "COMPRESS"),
    "c04": (Case("c04", repair="ENGINEERING"), "COMPRESS"),
    "c05": (Case("c05", compression=True), "PROMOTE"),
    "c06": (Case("c06", claim_reduction=True), "PROMOTE"),
    "c07": (Case("c07", executable="FORMAL_ONLY"), "COMPRESS"),
    "c08": (Case("c08", authority_correction=True), "PROMOTE"),
    "c09": (Case("c09", contact="DUPLICATE"), "COMPRESS"),
    "c10": (Case("c10", executable="FORMAL_ONLY", criterion_audit=False), "HOLD"),
    "c11": (Case("c11", executable="FORMAL_ONLY"), "COMPRESS"),
    "c12": (Case("c12", repair="ENGINEERING"), "COMPRESS"),
    "c13": (Case("c13", executable="MATERIAL", presealed=False), "HOLD"),
    "c14": (Case("c14", criterion_audit=False), "HOLD"),
    "c15": (Case("c15", live_consequence=False), "REJECT"),
    "c16": (Case("c16", option_value=True), "PROMOTE"),
    "c17": (Case("c17", localization=True), "PROMOTE"),
    "c18": (Case("c18", authority_correction=True), "PROMOTE"),
    "c19": (Case("c19", repair="ENGINEERING"), "COMPRESS"),
    "c20": (Case("c20", criterion_audit=False), "HOLD"),
}

POSITIVE = {
    "p01": (Case("p01", executable="MATERIAL"), "PROMOTE"),
    "p02": (Case("p02", contact="INDEPENDENT"), "PROMOTE"),
    "p03": (Case("p03", repair="ENGINEERING"), "COMPRESS"),
    "p04": (Case("p04", deletion=True), "PROMOTE"),
    "p05": (Case("p05", claim_reduction=True), "PROMOTE"),
    "p06": (Case("p06", executable="FORMAL_ONLY"), "COMPRESS"),
    "p07": (Case("p07", localization=True), "PROMOTE"),
    "p08": (Case("p08", authority_correction=True), "PROMOTE"),
    "p09": (Case("p09", live_consequence=False, archive_value=True), "ARCHIVE"),
    "p10": (Case("p10", criterion_audit=False), "HOLD"),
}

def evaluate(bank):
    out={}
    for key,(case,expected) in bank.items():
        got=revised_relation(case)
        out[key]={"expected":expected,"got":got,"pass":got==expected}
    return out

def main():
    cases=evaluate(CASES)
    positive=evaluate(POSITIVE)
    old_false_negative = prior_rule(Case("old_a", compression=True)) == "COMPRESS_NO_PROMOTION"
    old_false_positive = prior_rule(Case("old_b", executable="FORMAL_ONLY")) == "PROMOTION_CANDIDATE"
    report={
        "stage":"MQR-4.59",
        "preseal_commit":"7d76672b81e9f4c6bba1da975f58305f6c684737",
        "stress_manifest_commit":"9974e8731cfd2f61e7e6bc2ee187d944e688943d",
        "cases":cases,
        "positive":positive,
        "old_rule_false_negative_witness":old_false_negative,
        "old_rule_false_positive_witness":old_false_positive,
        "prior_rule_necessary":"REJECT",
        "execution_universal_gate":"REJECT",
        "novelty_default_value":"REJECT",
        "recursive_artifact_count_progress":"REJECT",
        "criterion_authority_default":"REJECT",
        "universal_meta_objective":"NOT_EARNED",
        "rpar":"CANDIDATE",
        "mcl":"CANDIDATE",
        "cdr":"CANDIDATE",
    }
    out=Path(__file__).parent/"results"/"promotion_court.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for key,row in cases.items():
        print(f"mqr459.{key}={'PASS' if row['pass'] else 'FAIL'}")
    for key,row in positive.items():
        print(f"mqr459.{key}={'ADMIT' if row['pass'] else 'HOLD'}")
    print(f"mqr459.old_rule_false_negative={'PASS' if old_false_negative else 'FAIL'}")
    print(f"mqr459.old_rule_false_positive={'PASS' if old_false_positive else 'FAIL'}")
    for key in (
        "prior_rule_necessary","execution_universal_gate","novelty_default_value",
        "recursive_artifact_count_progress","criterion_authority_default",
        "universal_meta_objective","rpar","mcl","cdr"
    ):
        print(f"mqr459.{key}={report[key]}")

if __name__=="__main__":
    main()
