"""MQR-4.107 source-transcribed Regnault comparative readings and identifiability test.
Historical readings from Chang (2004), Inventing Temperature, tables 2.4/2.5,
adapted from Regnault (1847). Toy common-bias demonstration is NOT 1847 data.
"""
from math import isclose

MERCURY = [
  # air reading, Choisy-le-Roi crystal, ordinary, green, Swedish glass
  (100., 100.,100.,100.,100.),
  (150.,150.40,149.80,150.30,150.15),
  (200.,201.25,199.70,200.80,200.50),
  (250.,253.00,250.05,251.85,251.44),
  (300.,305.72,301.08,None,None),
  (350.,360.50,354.00,None,None)
]
AIR = [
 # ambient A degree, A-prime degree, original reported difference
 (95.57,95.57,0.00),
 (155.99,155.82,0.17),
 (212.25,212.27,-0.02),
 (239.17,239.21,-0.04),
 (281.07,280.85,0.22),
 (339.68,339.39,0.29),
]
def calibration_model(t,delta):
    """Synthetic shared-nonlinearity term zero at 0 and 100 Celsius."""
    return t + delta*t*(t-100)/10000
def main():
    print("Regnault mercury at air 250:",MERCURY[3])
    print("At 350 two available glass readings differ:",MERCURY[-1][1]-MERCURY[-1][2])
    assert isclose(MERCURY[-1][1]-MERCURY[-1][2],6.5)
    assert all(isclose(a-b,d,abs_tol=1e-8) for a,b,d in AIR)
    assert max(abs(d) for a,b,d in AIR)==.29
    # Two perfectly agreeing independent readout paths with shared scale bias.
    for delta in [0., 1., 3.]:
        assert calibration_model(0,delta)==0
        assert calibration_model(100,delta)==100
        a=calibration_model(250,delta)
        b=calibration_model(250,delta)
        print(f"SYNTHETIC shared bias={delta:g}: instrument A={a:.3f}; B={b:.3f}; nominal 250; bias={a-250:.3f}")
        assert a==b
    print("Inter-device agreement and two fixed points do not identify common calibration nonlinearity.")
if __name__=="__main__": main()
