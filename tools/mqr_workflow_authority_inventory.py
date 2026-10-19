"""Static authority inventory for checked-out .github/workflows (no API calls)."""
import json
import re
import sys
from pathlib import Path

PERM = re.compile(r'^\s*([a-z-]+)\s*:\s*write\b', re.M)
DIRECT_PUSH = re.compile(r'\bgit\s+(?:-C\s+\S+\s+)?(?:push|commit)\b', re.I)
POST_STATUS = re.compile(r'\bgh\s+api\b[\s\S]{0,250}statuses/|createCommitStatus|/statuses/', re.I)

def examine(text):
    # Remove whole-line comments. Inline shell and external actions still
    # require separate review; this is a static screening aid, not a proof.
    active='\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('#'))
    return {
        'write_permissions': sorted(set(PERM.findall(active))),
        'direct_git_mutation': bool(DIRECT_PUSH.search(active)),
        'explicit_status_post_pattern': bool(POST_STATUS.search(active)),
        'has_top_level_permissions': bool(re.search(r'^permissions\\s*:',active,re.M)),
        'listens_to_workflow_run': bool(re.search(r'^\\s{2}workflow_run\\s*:',active,re.M)),
    }

def scan(root):
    results={}
    for path in sorted((root/'.github'/'workflows').glob('*.yml')):
        results[path.name]=examine(path.read_text(encoding='utf-8'))
    return {
        'count': len(results),
        'statuses_write': sorted(k for k,v in results.items() if 'statuses' in v['write_permissions']),
        'contents_write': sorted(k for k,v in results.items() if 'contents' in v['write_permissions']),
        'missing_top_level_permissions': sorted(k for k,v in results.items() if not v['has_top_level_permissions']),
        'workflow_run_listeners': sorted(k for k,v in results.items() if v['listens_to_workflow_run']),
        'other_write': {k:v['write_permissions'] for k,v in results.items() if set(v['write_permissions'])-{'statuses','contents'}},
        'direct_git_mutation': sorted(k for k,v in results.items() if v['direct_git_mutation']),
        'explicit_status_post_pattern': sorted(k for k,v in results.items() if v['explicit_status_post_pattern']),
    }

def test():
    assert examine('permissions:\n  contents: read\n  statuses: write')['write_permissions']==['statuses']
    assert examine('permissions:\n  contents: write')['write_permissions']==['contents']
    assert examine('run: git push origin main')['direct_git_mutation']
    assert not examine('run: git fetch origin main')['direct_git_mutation']
    assert examine('run: gh api --method POST "repos/x/y/statuses/abc"')['explicit_status_post_pattern']
    assert not examine('# contents: write\npermissions:\n  contents: read')['write_permissions']
    assert not examine('on: push\njobs:\n  foo: {}')['has_top_level_permissions']
    assert examine('on:\n  workflow_run:\n    types: [completed]')['listens_to_workflow_run']
    print('MQR_WORKFLOW_AUDIT_FIXTURE=PASS')

if __name__=='__main__':
    test()
    if len(sys.argv)>1:
        print(json.dumps(scan(Path(sys.argv[1])),ensure_ascii=False,indent=2))
