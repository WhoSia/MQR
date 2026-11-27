:- module(reusable_inquiry_v55, [choice/4, interval_decision/6]).
:- use_module(library(plunit)).
natural(X) :- integer(X), X>=0.

% Common costs cancel. P is the acquisition premium, S the saving per task.
choice(P,S,N,Result) :-
    ground(P-S-N), maplist(natural,[P,S,N]),
    D is N*S-P,
    ( D>0 -> Result=reuse ; D<0 -> Result=direct ; Result=tie ).

% Worst-case regret over all integer horizons L..H.
% This is a conditional cost criterion, not a general research priority score.
interval_decision(P,S,L,H,DRegret,RRegret) :-
    ground(P-S-L-H), maplist(natural,[P,S,L,H]), L=<H,
    DRegret is max(0,H*S-P), RRegret is max(0,P-L*S).

:- begin_tests(reusable_inquiry).
test(immediate) :- choice(5,2,0,direct).
test(reuse) :- choice(5,2,3,reuse).
test(tie) :- choice(6,2,3,tie).
test(zero_saving) :- choice(1,0,100,direct).
test(zero_premium) :- choice(0,1,1,reuse).
test(interval_crosses) :- interval_decision(5,2,0,4,3,5).
test(interval_reuse) :- interval_decision(5,2,3,4,3,0).
test(interval_direct) :- interval_decision(5,2,0,2,0,5).
test(single_horizon) :- interval_decision(5,2,2,2,0,1).
test(invalid_interval,[fail]) :- interval_decision(1,1,3,2,_,_).
test(negative,[fail]) :- choice(-1,2,3,_).
test(unbound,[fail]) :- interval_decision(_,2,0,1,_,_).
:- end_tests(reusable_inquiry).
