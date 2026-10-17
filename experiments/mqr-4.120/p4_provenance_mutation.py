"""Synthetic provenance-aware authority audit; never certifies real legitimacy."""
from collections import defaultdict

def audit(nodes, edges, origin, appeal, mandate_verified=False, appeal_can_hear_scope=False):
    if origin not in nodes or appeal not in nodes:
        return 'HOLD_MISSING_NODE'
    if any(not e.get('source_receipt') for e in edges):
        return 'HOLD_UNSOURCED_EDGE'
    graph = defaultdict(set)
    for e in edges:
        if e['child'] not in nodes or e['parent'] not in nodes:
            return 'HOLD_UNKNOWN_ENDPOINT'
        graph[e['child']].add(e['parent'])
    def ancestors(node):
        seen=set(); stack=list(graph[node])
        while stack:
            v=stack.pop()
            if v not in seen:
                seen.add(v); stack+=list(graph[v])
        return seen
    a,b=ancestors(origin),ancestors(appeal)
    if origin in a or appeal in b:
        return 'HOLD_CYCLIC'
    if not appeal_can_hear_scope:
        return 'HOLD_UNCONTESTABLE'
    if (a|{origin})&(b|{appeal}):
        return 'SHARED_ANCESTRY_REVIEW_REQUIRED'
    if not mandate_verified:
        return 'HOLD_MANDATE'
    return 'CONDITIONAL_STRUCTURAL_SEPARATION'

def audit_with_registry(nodes, observed_edges, registry, origin, appeal, **kwargs):
    # Registry must be independently supplied, not derived from observed edges.
    observed={(e['child'],e['parent']) for e in observed_edges}
    expected={(e['child'],e['parent']) for e in registry}
    if expected-observed:
        return 'HOLD_MISSING_REGISTERED_EDGE'
    if observed-expected:
        return 'HOLD_UNREGISTERED_EDGE'
    return audit(nodes,observed_edges,origin,appeal,**kwargs)

def test():
    nodes={'court','appeal','shared','external'}
    def edge(child,parent): return {'child':child,'parent':parent,'source_receipt':f'fixture:{child}:{parent}'}
    common=[edge('court','shared'),edge('appeal','shared')]
    separate=[edge('court','shared'),edge('appeal','external')]
    kw={'mandate_verified':True,'appeal_can_hear_scope':True}
    checks=[
      (audit_with_registry(nodes,common,common,'court','appeal',**kw),'SHARED_ANCESTRY_REVIEW_REQUIRED'),
      (audit_with_registry(nodes,common[:1],common,'court','appeal',**kw),'HOLD_MISSING_REGISTERED_EDGE'),
      (audit_with_registry(nodes,separate,separate,'court','appeal',**kw),'CONDITIONAL_STRUCTURAL_SEPARATION'),
      (audit_with_registry(nodes,separate,separate,'court','appeal',mandate_verified=False,appeal_can_hear_scope=True),'HOLD_MANDATE'),
      (audit_with_registry(nodes,separate,separate,'court','appeal',mandate_verified=True,appeal_can_hear_scope=False),'HOLD_UNCONTESTABLE'),
      (audit_with_registry(nodes,[{**separate[0], 'source_receipt':''},separate[1]],separate,'court','appeal',**kw),'HOLD_UNSOURCED_EDGE'),
      (audit_with_registry(nodes,common+[edge('court','external')],common,'court','appeal',**kw),'HOLD_UNREGISTERED_EDGE'),
      (audit_with_registry(nodes,[edge('court','appeal'),edge('appeal','court')],[edge('court','appeal'),edge('appeal','court')],'court','appeal',**kw),'HOLD_CYCLIC'),
    ]
    for i,(actual,expected) in enumerate(checks,1):
        assert actual==expected,(i,actual,expected)
        print(f'{i}: {actual}')
    print('PASS: 8 synthetic provenance and mutation checks; no world validation')
if __name__=='__main__': test()
