"""SNO 2002 published-flux illustrative linear sensitivity; not a refit.
Run: python sno_sensitivity.py. Standard library only. No SNO event likelihood.
"""
from math import sqrt

CC, NC = 1.76, 5.09
cc_stat, cc_sys = 0.05, 0.09
nc_stat_plus, nc_sys_plus = 0.44, 0.46
reported_other = 3.41  # Joint CC+NC+ES inference, NOT NC-CC

def simple_flux_difference(cc=CC, nc=NC):
    return nc - cc

def inferred_flavors(cc_rate, nc_rate, cc_eff=1.0, nc_eff=1.0):
    if cc_eff <= 0 or nc_eff <= 0:
        raise ValueError("responses must be positive")
    electron = cc_rate / cc_eff
    return electron, nc_rate / nc_eff - electron

def diff_sigma(cc_sigma, nc_sigma, rho):
    if not (-1 <= rho <= 1):
        raise ValueError("invalid correlation")
    return sqrt(max(0, cc_sigma**2 + nc_sigma**2 - 2*rho*cc_sigma*nc_sigma))

def main():
    print("Units: 10^6 cm^-2 s^-1")
    print("Simple NC-CC:", round(simple_flux_difference(),3))
    print("Published joint-fit non-electron:",reported_other)
    print("Difference:",round(reported_other-simple_flux_difference(),3))
    for ec,en in [(1,1),(.95,1),(1.05,1),(1,.95),(1,1.05),(.95,1.05),(1.05,.95)]:
        e,x=inferred_flavors(CC,NC,ec,en)
        print(f"cc_eff={ec:.2f} nc_eff={en:.2f} electron={e:.3f} other={x:.3f}")
    nc_unc=sqrt(nc_stat_plus**2 + nc_sys_plus**2)
    cc_unc=sqrt(cc_stat**2 + cc_sys**2)
    for rho in [-.75,0,.75]:
        sig=diff_sigma(cc_unc,nc_unc,rho)
        print(f"illustrative corr={rho:+.2f} sigma_delta={sig:.3f} z={(NC-CC)/sig:.3f}")
    assert abs(simple_flux_difference()-3.33)<1e-12
    assert diff_sigma(1,1,1)==0
    assert abs(diff_sigma(1,1,-1)-2)<1e-12

if __name__ == "__main__":
    main()
