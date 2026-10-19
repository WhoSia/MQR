"""MQR 4.121 P1F: synthetic signal-domain calibration stress.

Only model-generated data. No physical instrument or chemical identification validation.
Numpy required. Zong et al. Applied Optics 45 (2006), equations 1–10.
"""
import json
import numpy as np

def forward_matrix(D):
    D=np.asarray(D,float)
    assert D.ndim==2 and D.shape[0]==D.shape[1]
    assert np.allclose(np.diag(D),0.0) and np.all(D>=0)
    return np.eye(len(D))+D

def signal_correction(y,D_est):
    return np.linalg.solve(forward_matrix(D_est),y)

def absorbance(t):
    t=np.asarray(t,float)
    if np.any(t<=0):
        raise ValueError("nonpositive transmission")
    return -np.log10(t)

def main(seed=4121,n=20000):
    D=np.array([[0,.015,.002],[.012,0,.008],[.002,.014,0]])
    M=forward_matrix(D)
    true_t=np.array([.01,.10,.50])
    raw=M@true_t
    assert np.allclose(signal_correction(raw,D),true_t,atol=1e-14)
    q=np.array([.0008,.0004,.0002])
    bias_off=absorbance(signal_correction(raw+q,D))-absorbance(true_t)
    D_wrong=.8*D
    bias_matrix=absorbance(signal_correction(raw,D_wrong))-absorbance(true_t)
    t2=true_t-np.array([.0005,.0005,.0005])
    q2=M@(true_t-t2)
    assert np.all(q2>=0)
    assert np.allclose(M@true_t,M@t2+q2)
    sigma=1e-5
    rng=np.random.default_rng(seed)
    noise=rng.normal(0,sigma,(n,3))
    transmission=np.linalg.solve(M,(raw[None,:]+noise).T).T
    assert np.all(transmission>0)
    empirical_std=np.std(absorbance(transmission),axis=0,ddof=1)
    inverse=np.linalg.inv(M)
    j=np.diag(-1/(np.log(10)*true_t))
    cov_t=sigma*sigma*inverse@inverse.T
    linear_std=np.sqrt(np.diag(j@cov_t@j))
    assert np.allclose(empirical_std,linear_std,rtol=.07)
    return {
        "status":"SYNTHETIC_ONLY; PHYSICAL_DATA_HOLD",
        "condition_number":float(np.linalg.cond(M)),
        "reference_absorbance":absorbance(true_t).tolist(),
        "off_array_bias_AU":bias_off.tolist(),
        "20pct_underestimated_D_bias_AU":bias_matrix.tolist(),
        "observation_equivalent_state2":t2.tolist(),
        "equivalent_nonnegative_extra_light":q2.tolist(),
        "Monte_Carlo_n":n,
        "absolute_signal_noise_std":sigma,
        "absorbance_empirical_std_AU":empirical_std.tolist(),
        "absorbance_linearized_std_AU":linear_std.tolist()
    }

if __name__=="__main__":
    print(json.dumps(main(),indent=2))
