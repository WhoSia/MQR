"""MQR 4.120 P6: synthetic, scope-sensitive causal-consequence claim validator."""
def assess(r):
    if not r.get('scope_covered', False): return 'OUT_OF_SCOPE'
    if not r.get('remedy_ordered', False): return 'NO_ORDER'
    if not r.get('implementation_receipt', False): return 'ORDER_ONLY'
    if not r.get('post_observation', False): return 'IMPLEMENTED_OUTCOME_UNKNOWN'
    if not r.get('independent_observation', False): return 'OUTCOME_SOURCE_DEPENDENT'
    if not r.get('baseline_comparable', False): return 'OBSERVED_NONCOMPARABLE'
    if not r.get('confounding_addressed', False): return 'CHANGE_OBSERVED_CAUSE_HOLD'
    return 'CONDITIONAL_CAUSAL_SUPPORT_IN_FIXTURE'
BASE = dict(scope_covered=True, remedy_ordered=True, implementation_receipt=True,
            post_observation=True, independent_observation=True,
            baseline_comparable=True, confounding_addressed=True)
def run():
    cases=[
      ({},'CONDITIONAL_CAUSAL_SUPPORT_IN_FIXTURE'),
      ({'scope_covered':False},'OUT_OF_SCOPE'),
      ({'remedy_ordered':False},'NO_ORDER'),
      ({'implementation_receipt':False},'ORDER_ONLY'),
      ({'post_observation':False},'IMPLEMENTED_OUTCOME_UNKNOWN'),
      ({'independent_observation':False},'OUTCOME_SOURCE_DEPENDENT'),
      ({'baseline_comparable':False},'OBSERVED_NONCOMPARABLE'),
      ({'confounding_addressed':False},'CHANGE_OBSERVED_CAUSE_HOLD')]
    for k,(mod,expected) in enumerate(cases,1):
        got=assess(BASE | mod)
        assert got==expected,(k,got,expected)
        print(k,got)
    print('PASS: 8 synthetic gates; no independent or causal empirical validation')
if __name__=='__main__':run()
