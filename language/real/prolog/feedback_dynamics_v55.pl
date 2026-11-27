:- module(feedback_dynamics_v55, [worlds_for_trials/2, separator/3]).
:- use_module(library(plunit)).

bit(0).
bit(1).
world(w(A,B,C,D)) :- bit(A), bit(B), bit(C), bit(D).

step(w(A,_,_,_),0,0,A).
step(w(_,B,_,_),0,1,B).
step(w(_,_,C,_),1,0,C).
step(w(_,_,_,D),1,1,D).

trace(_,_,[],[]).
trace(W,S,[P|Ps],[T|Ts]) :-
    step(W,S,P,T), trace(W,T,Ps,Ts).

valid_trial(trial(Ps,Ts)) :-
    is_list(Ps), is_list(Ts), same_length(Ps,Ts),
    maplist(bit,Ps), maplist(bit,Ts).
matches(W,trial(Ps,Ts)) :- trace(W,0,Ps,Ts).

worlds_for_trials(Trials,Worlds) :-
    ground(Trials), is_list(Trials), maplist(valid_trial,Trials),
    findall(W,(world(W),maplist(matches(W),Trials)),Worlds).

% Complete only for known reset 0, fully observed Boolean state, deterministic
% time-invariant transitions and unrestricted Boolean interventions.
separator(A,B,Result) :-
    ground(A-B), world(A), world(B),
    ( once((between(1,2,N),length(Ps,N),maplist(bit,Ps),
            trace(A,0,Ps,Ts),trace(B,0,Ps,Us),Ts \= Us))
      -> Result = separates(Ps)
      ; Result = equivalent_from_reset
    ).

:- begin_tests(feedback_dynamics).
test(constant_policy_ambiguity) :-
    worlds_for_trials([trial([0,0],[0,0]),trial([1,1],[1,1])],Ws),
    assertion(Ws == [w(0,1,0,1),w(0,1,1,1)]).
test(withdrawal) :-
    separator(w(0,1,0,1),w(0,1,1,1),separates([1,0])).
test(withdrawal_identifies) :-
    worlds_for_trials([trial([0,0],[0,0]),trial([1,1],[1,1]),
                       trial([1,0],[1,1])],Ws),
    assertion(Ws == [w(0,1,1,1)]).
test(unreachable_rows) :-
    separator(w(0,0,0,0),w(0,0,1,1),equivalent_from_reset).
test(pair_census) :-
    findall(R,(world(A),world(B),A @< B,separator(A,B,R)),Rs),
    findall(1,member(separates([_]),Rs),Ones), length(Ones,96),
    findall(1,member(separates([_,_]),Rs),Twos), length(Twos,18),
    findall(1,member(equivalent_from_reset,Rs),Eq), length(Eq,6).
test(no_data) :- worlds_for_trials([],Ws), length(Ws,16).
test(contradictory_trials) :-
    worlds_for_trials([trial([1],[0]),trial([1],[1])],[]).
test(invalid_length,[fail]) :- worlds_for_trials([trial([0,1],[0])],_).
test(invalid_action,[fail]) :- worlds_for_trials([trial([2],[0])],_).
test(unbound_world,[fail]) :- separator(_,w(0,0,0,0),_).
:- end_tests(feedback_dynamics).
