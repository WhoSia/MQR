"""MQR 4.108 P5. Exact graph-table compression and rival sufficiency.
This is synthetic, NOT digitized Regnault historical readings.

A graph-producing pipeline reports the 2-point arithmetic mean
at one abscissa, then a regularly sampled table. Its raw inputs
might have different residual spread. Under Gaussian known-variance
location family, the mean is sufficient for mu, but NOT for
unknown variance / heterogeneous or mixture models.
"""
from fractions import Fraction as Q
from math import prod
A=(Q(0),Q(2))
B=(Q(1),Q(1))
def table(raw):
    return sum(raw,Q(0))/len(raw)
def scatter(raw):
    m=table(raw)
    return sum((x-m)**2 for x in raw)
assert table(A)==table(B)==Q(1)
assert scatter(A)==Q(2)
assert scatter(B)==Q(0)
# For Gaussian N(mu, sigma^2), unknown sigma, likelihood ratio
# at any common mu depends on scatter. At mu=1:
# ratio L(A;1,sigma)/L(B;1,sigma)=exp(-1/sigma^2).
# Hence it is not constant as sigma changes and mean is not
# sufficient for the joint parameter (mu,sigma).
# For known variance, ratio across these datasets at fixed
# mu is exp(-1/sigma_fixed^2), independent of mu.
assert sum((x-Q(1))**2 for x in A)==2
assert sum((x-Q(1))**2 for x in B)==0
# A covariance row can be retained as extra diagnostic.
assert (table(A),scatter(A))!=(table(B),scatter(B))
print("PASS: identical graph table, different raw scatter")
print("Known-variance Gaussian mean-sufficiency survives (mu only)")
print("Unknown-variance Gaussian mean-only sufficiency fails")
print("Warrant for process identity, provenance and model-class choice still separate")
