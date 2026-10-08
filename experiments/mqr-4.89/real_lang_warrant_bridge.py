"""MQR-4.89 scoped warrant bridge to the ACTUAL MQR-4.87 Real Lang policy.

Methodological hypothetical, not independent scientific validation.
A source-reported paper and MQR synthetic study cannot jointly license a
claim about original civil-war forecasting performance.
"""
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

@dataclass(frozen=True)
class Receipt:
    receipt_id:str
    claim_id:str
    target_scope:str
    origin:str
    family:str
    raw_component:str
    audited_bytes:bool
    protocol_audited:bool
    valid_credential:bool=True

def predecessor():
    path=Path(__file__).resolve().parent.parent/'mqr-4.87'/'real_lang_p1.py'
    if not path.is_file(): raise FileNotFoundError('Canonical MQR-4.87 interpreter unavailable: '+str(path))
    spec=spec_from_file_location('mqr_487_for_489',path)
    m=module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def evaluate(receipts,target_claim,target_scope,permission=True,threshold=2,compromised=()):
    reasons=[];eligible=[];seen=set()
    for r in receipts:
        if r.claim_id!=target_claim or r.target_scope!=target_scope:
            reasons.append((r.receipt_id,'CLAIM_OR_SCOPE_MISMATCH'));continue
        if r.origin!='AUDITED_EXTERNAL_REPLICATION':
            reasons.append((r.receipt_id,'ORIGIN_NOT_EXTERNAL_REPLICATION'));continue
        if not r.audited_bytes or not r.protocol_audited:
            reasons.append((r.receipt_id,'REPLICATION_AUDIT_INCOMPLETE'));continue
        if not r.valid_credential:
            reasons.append((r.receipt_id,'CREDENTIAL_REVOKED'));continue
        if r.raw_component in compromised:
            reasons.append((r.receipt_id,'KNOWN_COMPROMISED_COMPONENT'));continue
        if r.family in seen:
            reasons.append((r.receipt_id,'DUPLICATE_UPSTREAM_FAMILY'));continue
        seen.add(r.family);eligible.append(r)
    p=predecessor()
    terms=[((r.receipt_id,),1) for r in eligible]
    sources={r.receipt_id:p.Source(r.family,frozenset({r.raw_component}),frozenset({target_scope})) for r in eligible}
    result=p.adjudicate(terms,sources,target_scope,permission,threshold)
    assert result['families']==sorted(seen) or not permission
    method=('DENIED_SCOPE' if not permission else
            'HYPOTHETICAL_FAMILY_RULE_SATISFIED' if len(seen)>=threshold else
            'HOLD_INSUFFICIENT_AUDITED_FAMILIES')
    assert (result['verdict']=='AUTHORIZED_FOR_USE')==(method=='HYPOTHETICAL_FAMILY_RULE_SATISFIED')
    return dict(method_verdict=method,legacy_verdict=result['verdict'],
                scientific_authority='NOT_DETERMINED',
                independent_families_counted=sorted(seen),excluded=reasons)

def test():
    base=dict(claim_id='synthetic-method',target_scope='synthetic-only',
              origin='AUDITED_EXTERNAL_REPLICATION',audited_bytes=True,protocol_audited=True)
    def r(id,fam,**patch):return Receipt(receipt_id=id,family=fam,raw_component=id,**(base|patch))
    a,b=r('a','F1'),r('b','F2')
    cases=[
      ([],False),
      ([r('original','paper',origin='SOURCE_REPORTED'),r('mqr','lab',origin='SYNTHETIC')],False),
      ([r('a','F1',origin='SYNTHETIC'),r('b','F2',origin='SYNTHETIC')],False),
      ([a,r('b','F2',claim_id='different')],False),
      ([a,r('b','F2',target_scope='different')],False),
      ([a,r('b','F2',audited_bytes=False)],False),
      ([a,r('b','F2',protocol_audited=False)],False),
      ([a,r('b','F1')],False),
      ([a,b],True),
    ]
    for receipts,expected in cases:
        outcome=evaluate(receipts,'synthetic-method','synthetic-only')
        assert (outcome['method_verdict']=='HYPOTHETICAL_FAMILY_RULE_SATISFIED')==expected,outcome
        assert outcome['scientific_authority']=='NOT_DETERMINED'
    assert evaluate([a,b],'synthetic-method','synthetic-only',False)['method_verdict']=='DENIED_SCOPE'
    assert evaluate([a,b],'synthetic-method','synthetic-only',compromised=('a',))['method_verdict']=='HOLD_INSUFFICIENT_AUDITED_FAMILIES'
    assert evaluate([a,b],'synthetic-method','synthetic-only',threshold=3)['method_verdict']=='HOLD_INSUFFICIENT_AUDITED_FAMILIES'
    print('MQR489_BRIDGE_CHECKS=12 PASS')
    print('MQR489_SCIENTIFIC_AUTHORITY=NOT_DETERMINED')
if __name__=='__main__':test()
