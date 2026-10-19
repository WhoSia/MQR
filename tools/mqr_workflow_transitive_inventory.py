"""MQR workflows: source-only external action / local command inventory.

This is NOT a supply-chain security verdict: dynamic strings, reusable workflows,
nested scripts and external actions require further independent source inspection.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

USES = re.compile(r"^\s*(?:-\s*)?uses\s*:\s*['\"]?([^\s#'\"]+)", re.M)
ROOT_SCRIPTS = re.compile(
    r"\b(?:python(?:3(?:\.\d+)?)?|bash|sh)\s+((?:\./)?(?:experiments|tools|language)/[\w./-]+\.(?:py|sh))"
)
PIN = re.compile(r"^[0-9a-fA-F]{40}$")

def analyze(text, root):
    active = "\n".join(line for line in text.splitlines()
                       if not line.lstrip().startswith("#"))
    used = sorted(set(USES.findall(active)))
    external = [u for u in used if not u.startswith("./")]
    scripts = sorted(set(ROOT_SCRIPTS.findall(active)))
    return {
        "external": external,
        "local_actions": [u for u in used if u.startswith("./")],
        "floating_refs": [u for u in external
                          if "@" not in u or not PIN.fullmatch(u.rsplit("@", 1)[-1])],
        "repo_root_scripts": scripts,
        "missing_repo_root_scripts": [p for p in scripts if not (root/p.removeprefix("./")).is_file()],
        "post_status": bool(re.search(r"\bgh\s+api\b[\s\S]{0,180}/statuses/|createCommitStatus", active)),
        "checkout_persist_false": "persist-credentials: false" in active,
        "workflow_call": bool(re.search(r"^\s{2}workflow_call\s*:",active,re.M)),
    }

def scan(root):
    wf = root/".github"/"workflows"
    if not wf.is_dir(): raise ValueError("Expected checked-out repository root")
    analyzed={}
    for f in sorted(wf.glob("*.yml")):
        analyzed[f.name]=analyze(f.read_text(encoding="utf-8"),root)
    action_counts=Counter(u for v in analyzed.values() for u in v["external"])
    return {
        "workflow_count":len(analyzed),
        "external_action_refs":dict(sorted(action_counts.items())),
        "floating_action_uses":{k:v["floating_refs"] for k,v in analyzed.items() if v["floating_refs"]},
        "repo_root_scripts":sorted(set(x for v in analyzed.values() for x in v["repo_root_scripts"])),
        "missing_explicit_repo_root_scripts":{k:v["missing_repo_root_scripts"] for k,v in analyzed.items() if v["missing_repo_root_scripts"]},
        "status_post_explicit_yaml":sorted(k for k,v in analyzed.items() if v["post_status"]),
        "workflow_call_receivers":sorted(k for k,v in analyzed.items() if v["workflow_call"]),
    }

def tests():
    root=Path(".")
    z=analyze("""jobs:
      a:
        steps:
        - uses: actions/checkout@v4
        - uses: leanprover/lean-action@38fbc41a8c28c4cbaec22d7f7de508ec2e7c0dd9
        - run: python3 tools/mqr_workflow_transitive_inventory.py
        - run: gh api --method POST repos/x/y/statuses/abc
""",root)
    assert "actions/checkout@v4" in z["floating_refs"]
    assert not any("leanprover/" in q for q in z["floating_refs"])
    assert z["post_status"]
    assert "tools/mqr_workflow_transitive_inventory.py" in z["repo_root_scripts"]
    assert not analyze("jobs:\n  a:\n    steps:\n    - run: python -c 'print(1)'",root)["repo_root_scripts"]
    print("MQR_TRANSITIVE_AUDIT_FIXTURE=PASS")

if __name__=="__main__":
    tests()
    if len(sys.argv)>1:
        print(json.dumps(scan(Path(sys.argv[1])),indent=2,ensure_ascii=False))
