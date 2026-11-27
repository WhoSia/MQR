:- module(measurement_reactivity_v55, [contrast_bounds/5, calibrated_bounds/6, mismatch_bounds/5]).
:- use_module(library(plunit)).

% g(Negative,Positive,Missing) describes one known baseline group.
valid_group(g(A,B,M),N) :-
    maplist(nonnegative,[A,B,M]), N is A+B+M, N>0.
nonnegative(X) :- integer(X), X>=0.

cost(g(_,P,M),C,K) :- K is max(0,max(P-C,C-P-M)).

contrast_bounds(G0,G1,K,Lo,Hi) :-
    ground(G0-G1-K), valid_group(G0,N0), valid_group(G1,N1),
    nonnegative(K),
    findall(D,(between(0,N0,C0),between(0,N1,C1),
        cost(G0,C0,K0),cost(G1,C1,K1), K0+K1=<K,
        D is N0*C1-N1*C0), Ds),
    min_list(Ds,Lo),max_list(Ds,Hi).

% Exact same-cohort untreated total B; inconsistent observations return no solution.
calibrated_bounds(G0,G1,K,B,Lo,Hi) :-
    ground(G0-G1-K-B), valid_group(G0,N0), valid_group(G1,N1),
    nonnegative(K), nonnegative(B), B=<N0+N1,
    findall(D,(between(0,N1,C1), C0 is B-C1, C0>=0,C0=<N0,
        cost(G0,C0,K0),cost(G1,C1,K1), K0+K1=<K,
        D is N0*C1-N1*C0), Ds),
    Ds \= [], min_list(Ds,Lo),max_list(Ds,Hi).

% Marginal counts alone imply endpoints, with possible mismatch counts spaced by two.
mismatch_bounds(N,A,B,Lo,Hi) :-
    ground(N-A-B), maplist(nonnegative,[N,A,B]), A=<N,B=<N,
    Lo is abs(A-B), Hi is min(A+B,2*N-A-B).

:- begin_tests(measurement_reactivity).
test(no_reactivity) :-
    contrast_bounds(g(4,0,1),g(0,4,1),0,15,25).
test(budget_two) :-
    contrast_bounds(g(4,0,1),g(0,4,1),2,5,25).
test(budget_three) :-
    contrast_bounds(g(4,0,1),g(0,4,1),3,0,25).
test(budget_four) :-
    contrast_bounds(g(4,0,1),g(0,4,1),4,-5,25).
test(all_missing) :-
    contrast_bounds(g(0,0,2),g(0,0,3),0,-6,6).
test(unequal_groups) :-
    contrast_bounds(g(1,0,0),g(0,3,0),1,0,3).
test(negative_budget,[fail]) :-
    contrast_bounds(g(4,0,1),g(0,4,1),-1,_,_).
test(empty_group,[fail]) :-
    contrast_bounds(g(0,0,0),g(0,4,1),0,_,_).
test(unbound,[fail]) :-
    contrast_bounds(g(_,0,1),g(0,4,1),0,_,_).
test(calibrated_two) :-
    calibrated_bounds(g(4,0,1),g(0,4,1),2,5,5,25).
test(calibrated_three) :-
    calibrated_bounds(g(4,0,1),g(0,4,1),3,5,5,25).
test(calibration_inconsistent,[fail]) :-
    calibrated_bounds(g(4,0,1),g(0,4,1),0,0,_,_).
test(marginal_equality_can_hide_full_change) :- mismatch_bounds(8,4,4,0,8).
test(unequal_margins) :- mismatch_bounds(8,2,5,3,7).
test(mismatch_invalid,[fail]) :- mismatch_bounds(8,9,5,_,_).
test(nested_fixed_budget) :-
    contrast_bounds(g(3,0,1),g(0,3,1),1,4,16),
    contrast_bounds(g(3,1,0),g(1,3,0),1,4,12).
test(coverage_with_replacement_budget_loses_sign) :-
    contrast_bounds(g(3,1,0),g(1,3,0),2,0,16).
:- end_tests(measurement_reactivity).
