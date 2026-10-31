# MQR-5.3 — Bounded calibration and cross-environment intervention

**Status:** standalone Python analysis candidate; **NOT** Real Lang syntax promotion or experimental certification.

## Run
```bash
cd language/real/experiments
python -m unittest -v test_mqr53_calibration.py
```

## Model
An unobserved binary variable B has prevalence b. Binary calibration test C has
false-positive f=P(C=1|B=0) and false-negative n=P(C=0|B=1).
The observed test-positive rate q satisfies q=f+(1-f-n)b.
When sensitivity exceeds false-positive rate (1-f-n>0), b=(q-f)/(1-f-n).
The causal effect for the **assumed** XOR mechanism Y=A XOR B under do(A=1)
is 1-b; an alternative Y=1 XOR A XOR B has effect b despite identical Y
marginals when A is independent and fair.

**Crucial identification boundary:** independent intervals for f and n cannot
be replaced by a single symmetric error parameter eta. At q=.42, with
f,n separately in [.08,.12], sharp b bounds are [.375,.425].
Under the more restrictive f=n=eta in [.08,.12], b bounds narrow to
[.3947368421,.4047619048]. These are *structural identified sets*, not
confidence intervals.

**Finite samples:** Hoeffding half-width is
sqrt(log(2/alpha)/(2*N))/(1-f-n), conditioned on exact known f,n and iid
test results. For alpha=.05, f=n=.1, N=289 is sufficient for <=.1.
Errors in the estimated calibration rates are not included.

## Literature and custody
- [MQR-5.3 Notion master](https://app.notion.com/p/40aef561cf928165977af8e05ffc1b4f)
- [MQR-5.3 Google Drive master](https://docs.google.com/document/d/1rSArpBZ9GvYLkJrI5j3oEu6o-cdGobpi0xzmVj7SiH8/edit)
- Rubenstein et al. (2017), exact SEM transformations.
- Rischel & Weichwald (2021), compositional causal abstraction error.
- Pearl & Bareinboim (2011), causal transportability.

These functions are a finite synthetic illustration and do not measure
Galison's particle detector or Rheinberger's historical biochemical
preparations. No new data, empirical validation, CI receipt or formal language
promotion is claimed.
