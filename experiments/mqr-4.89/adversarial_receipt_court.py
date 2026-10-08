"""MQR-4.89 adversarial receipt court — synthetic input validation ONLY.
External attestation fields are supplied, NOT independently verified or signed.
"""
from dataclasses import dataclass
@dataclass(frozen=True)
class Audit:
    id:str
    evaluator:str
    claim:str
    scope:str
    protocol_ok:bool
    findings_ok:bool
    external_attestation:bool
@dataclass(frozen=True)
class Claim:
    id:str
    origin:str
    scope:str
    scope_allowed:bool|None
    leakage_reported:bool
    audit:Audit|None=None
def judge(c):
    if c.scope_allowed is False: return 'DENIED_SCOPE'
    if c.leakage_reported: return 'REOPEN_ORIGINAL_EVALUATION'
    if c.scope_allowed is None: return 'NEED_AUDIT'
    if c.origin != 'REVIEWED_REPLICATION_RECEIPT': return 'HOLD_INDEPENDENT_VALIDATION'
    a=c.audit
    if not a or not a.id or not a.evaluator or not a.external_attestation:
        return 'HOLD_INDEPENDENT_VALIDATION'
    if a.claim!=c.id or a.scope!=c.scope or not (a.protocol_ok and a.findings_ok):
        return 'HOLD_INDEPENDENT_VALIDATION'
    return 'SUPPORT_WITHIN_SCOPE'
def test():
    b=dict(id='c',origin='SOURCE_REPORTED',scope='study',scope_allowed=True,leakage_reported=False)
    good=Audit('a','external','c','study',True,True,True)
    bad=lambda **d: Audit(**(dict(id='a',evaluator='external',claim='c',scope='study',
                                  protocol_ok=True,findings_ok=True,external_attestation=True)|d))
    tests=[
      ({},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'EXTERNAL_CLAIMED_REPLICATION'},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT'},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':bad(external_attestation=False)},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':bad(claim='other')},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':bad(scope='other')},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':bad(protocol_ok=False)},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':bad(findings_ok=False)},'HOLD_INDEPENDENT_VALIDATION'),
      ({'origin':'REVIEWED_REPLICATION_RECEIPT','audit':good},'SUPPORT_WITHIN_SCOPE'),
      ({'scope_allowed':None,'origin':'REVIEWED_REPLICATION_RECEIPT','audit':good},'NEED_AUDIT'),
      ({'scope_allowed':False,'origin':'REVIEWED_REPLICATION_RECEIPT','audit':good},'DENIED_SCOPE'),
      ({'leakage_reported':True,'origin':'REVIEWED_REPLICATION_RECEIPT','audit':good},'REOPEN_ORIGINAL_EVALUATION'),
    ]
    for override, expected in tests:
        assert judge(Claim(**(b|override))) == expected
    print('MQR489_ADVERSARIAL_PASS=12')
    print('MQR489_EXTERNAL_VERIFICATION=NOT_PERFORMED')
if __name__=='__main__':test()
