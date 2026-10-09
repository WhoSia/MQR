"""MQR-3.154 adversarial minimal models. Python standard library only."""
from math import comb

def bernoulli_sequence_likelihood(theta, outcomes):
    p = 1.0
    for x in outcomes:
        p *= theta if x else 1.0-theta
    return p

def stopped_success_likelihood(theta, stopping_time):
    """Observe every attempt: first success on trial t."""
    return theta*(1.0-theta)**(stopping_time-1)

def final_success_only_likelihood(theta):
    """Observe only 'eventually succeeded', ignoring trial count, no upper bound."""
    return 1.0 if 0.0 < theta <= 1.0 else 0.0

def posterior_beta(successes,failures,a=1.0,b=1.0):
    return (a+successes,b+failures)

def likelihood_ratio(theta, reference, outcomes):
    return bernoulli_sequence_likelihood(theta,outcomes)/bernoulli_sequence_likelihood(reference,outcomes)

def main():
    theta=0.3
    # Same full observations in different order: identical likelihood/posterior
    h1=(1,0,1,0)
    h2=(0,1,0,1)
    assert bernoulli_sequence_likelihood(theta,h1)==bernoulli_sequence_likelihood(theta,h2)
    assert posterior_beta(sum(h1),len(h1)-sum(h1))==posterior_beta(sum(h2),len(h2)-sum(h2))
    print("ORDER INVARIANCE: likelihood",bernoulli_sequence_likelihood(theta,h1),"posterior",posterior_beta(2,2))
    # Two superficially identical headlines 'success': fixed first trial vs stop-on-success.
    # Complete records or observation mechanisms, not bare headline, determine likelihood.
    fixed=bernoulli_sequence_likelihood(theta,(1,))
    selective=final_success_only_likelihood(theta)
    t3=stopped_success_likelihood(theta,3)
    assert abs(fixed-0.3)<1e-12
    assert selective==1.0
    assert abs(t3-0.147)<1e-12
    print("REPORTING PATH: fixed n=1 P(success)=",fixed,
          "stop-on-success eventual P(success)=",selective,
          "stop time 3 P(first success on t=3)=",round(t3,3))
    print("INTERPRETATION: stopping + disclosure differences are already captured by statistical likelihood and selection theory; no MQR novelty established.")
if __name__=="__main__":
    main()
