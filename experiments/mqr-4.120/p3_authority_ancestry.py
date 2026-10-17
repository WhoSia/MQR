"""Finite graph-contract tests; no claim of institutional independence."""
from collections import deque

def ancestors(graph, start):
    visited=set(); pending=deque(graph.get(start, ()))
    while pending:
        x=pending.popleft()
        if x in visited: continue
        visited.add(x); pending.extend(graph.get(x, ()))
    return visited

def audit(graph, origin, appeal, independent_origins):
    if origin not in graph or appeal not in graph:
        return 'HOLD_UNDOCUMENTED'
    a=ancestors(graph,origin)|{origin}; b=ancestors(graph,appeal)|{appeal}
    if origin in ancestors(graph,origin) or appeal in ancestors(graph,appeal):
        return 'HOLD_CYCLIC_AUTHORITY'
    if a & b:
        return 'SHARED_ANCESTRY'
    if not (b & set(independent_origins)):
        return 'HOLD_UNVERIFIED_MANDATE'
    return 'STRUCTURALLY_SEPARATE_CONDITIONAL'

def test():
    scenarios=[
      ({'court':['ministry'],'appeal':['ministry'],'ministry':[]},'court','appeal',[], 'SHARED_ANCESTRY'),
      ({'court':['panel_a'],'appeal':['panel_b'],'panel_a':['office'],'panel_b':['office'],'office':[]},'court','appeal',[], 'SHARED_ANCESTRY'),
      ({'court':['office'],'appeal':['external'],'office':[],'external':[]},'court','appeal',[], 'HOLD_UNVERIFIED_MANDATE'),
      ({'court':['office'],'appeal':['external'],'office':[],'external':[]},'court','appeal',['external'], 'STRUCTURALLY_SEPARATE_CONDITIONAL'),
      ({'court':['appeal'],'appeal':['court']},'court','appeal',[], 'HOLD_CYCLIC_AUTHORITY'),
      ({'court':[]},'court','absent',[], 'HOLD_UNDOCUMENTED'),
    ]
    for idx,(g,o,a,roots,expected) in enumerate(scenarios):
        result=audit(g,o,a,roots)
        assert result==expected,(idx,result,expected)
    print('PASS: 6 constructed ancestry graph checks. No real-world authority certified.')
if __name__=='__main__':test()
