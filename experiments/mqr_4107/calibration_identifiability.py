"""MQR 4.107: bounded calibration identifiability audit, not a historical fit.
Regnault 1847 p181 corrected Wikisource transcription vs Chang 2004 Table 2.5:
one A-prime pressure discrepancy 785.21 versus 782.21 mmHg.
Historical p239 mercury-table facsimile not yet independently collated.
"""
from math import isclose
orig_p_at_95, chang_p_at_95 = 785.21, 782.21
assert orig_p_at_95 - chang_p_at_95 == 3.0

def reading(T, delta):
    return T + delta*T*(T-100)/10000

def derivative(T):
    return T*(T-100)/10000

for delta in [-4,0,2,4]:
    assert reading(0, delta)==0
    assert reading(100, delta)==100
assert derivative(0)==derivative(100)==0
assert derivative(250)==3.75
# A genuinely independent reference anchor with true temperature 250 and
# displayed readout 257.5 identifies the one-dimensional curvature delta.
recovered=(257.5-250)/derivative(250)
assert isclose(recovered,2)
print("Regnault-Chang transcription discrepancy: 3.00 mmHg (pending scan adjudication)")
print("Calibration derivative: [0,0,3.75] at T=[0,100,250]")
print("Conditionally identified curvature delta:",recovered)
print("PASS BOUNDED; no physical calibration or historical anomaly proven.")
