#!/usr/bin/env python3
"""MQR-4.112 P1-E: provenance/edition boundary only, no retrospective claims.

The 2021 BayLum 0.2.1.9000-5 and current upstream BayLum both have the
EXACT SAME Git blob for data/Model_AgeS.rda (the JAGS model DATA file).
R/AgeS_Computation.R differs. A shared packaged model-asset blob alone
does NOT prove unchanged likelihood invocation or source tutorial cohort.
"""
import json
import urllib.request
from pathlib import Path

OWNER = "crp2a/BayLum"
OLD = "2c267b63c2b7017cae1e141d0969eb0765ad2500"
# Pin a real upstream main-tree SHA observed 2026-10-11, not dynamic HEAD
NEW = "42e551f951b2a24c8062849b6ecbeeb661c99b83"
REQUIRED = {
    "data/Model_AgeS.rda": ("a84f3c7160f9fc3bbb59245b54bb5cebe6d66ede",
                            "a84f3c7160f9fc3bbb59245b54bb5cebe6d66ede"),
    "R/AgeS_Computation.R": ("8f269dc7d417aaf677b9ab7fba0ba42c71fd45f7",
                              "f018d5489789cebebea203f93a6162a0999ab729"),
    "R/Generate_DataFile.R": ("5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8",
                               "804550b215e4132177f51ff7563bf1b778842313"),
    "DESCRIPTION": ("859cf2e68bd251641dd23f0e67212e024322525c",
                    "ff15ba45d3422cbf41174bed4155a49834fe23c6"),
}
def tree(sha):
    url = f"https://api.github.com/repos/{OWNER}/git/trees/{sha}?recursive=1"
    req = urllib.request.Request(url, headers={"User-Agent":"MQR-4112-read-only-source-court"})
    with urllib.request.urlopen(req,timeout=30) as f:
        payload=json.load(f)
    assert payload["sha"]==sha and not payload.get("truncated"),"tree provenance incomplete"
    return {x["path"]:x["sha"] for x in payload["tree"] if x["type"]=="blob"}
def main():
    old,new=tree(OLD),tree(NEW)
    out={"source":"crp2a/BayLum","historical_commit":OLD,"comparison_commit":NEW,
         "conclusions":{},"files":{}}
    for name,(expected_old,expected_new) in REQUIRED.items():
        a,b=old.get(name),new.get(name)
        if (a,b)!=(expected_old,expected_new):
            raise RuntimeError(f"{name}: unexpected source blob {a} / {b}")
        out["files"][name]={"old_blob":a,"new_blob":b,"identical":a==b}
    assert out["files"]["data/Model_AgeS.rda"]["identical"]
    assert not out["files"]["R/AgeS_Computation.R"]["identical"]
    out["conclusions"]={
        "JAGS_MODEL_RDA_BINARY_BLOB_IDENTITY":"PASS_EXACT_GIT_BLOB",
        "AGE_WRAPPER_SOURCE_IDENTITY":"FAIL_EXACT_GIT_BLOB",
        "OLD_AUTHOR_EXACT_RUNTIME_REVISION":"HOLD",
        "FUNCTION_LEVEL_LIKELIHOOD_EQUIVALENCE":"HOLD",
        "FER3_PUBLISHED_POSTERIOR_REPRODUCTION":"HOLD"}
    Path("out").mkdir(exist_ok=True)
    Path("out/source_vintage_blob_manifest.json").write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out["conclusions"],indent=2))
if __name__=="__main__":
    main()
