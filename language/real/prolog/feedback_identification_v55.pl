:- module(feedback_identification_v55, [worlds_for/2, response_status/2]).
:- use_module(library(plunit)).

% Finite binary-coefficient restriction of the Lean Nat model.
world(w(D,R,B,I)) :-
    between(0,1,D), between(0,1,R), between(0,1,B), between(0,1,I).

valid_observation(cell(P,M,Y)) :-
    memberchk(P,[0,1]), memberchk(M,[0,1]), integer(Y), Y >= 0.

matches(w(D,R,B,I), cell(P,M,Y)) :-
    Y =:= D + P*R + M*B + P*M*I.

% Ground inputs only; malformed inputs fail, contradictory observations yield [].
worlds_for(Obs, Worlds) :-
    ground(Obs), is_list(Obs), maplist(valid_observation, Obs),
    findall(W, (world(W), maplist(matches(W), Obs)), Worlds).

% These verdicts are relative to the declared finite model family.
response_status(Obs, Status) :-
    worlds_for(Obs, Worlds),
    findall(R, member(w(_,R,_,_), Worlds), Raw),
    sort(Raw, Values),
    ( Values = [] -> Status = inconsistent
    ; Values = [V] -> Status = identified(V)
    ; Status = ambiguous(Values)
    ).

:- begin_tests(feedback_identification).
test(before_after_confounded) :-
    worlds_for([cell(0,0,0),cell(1,1,1)], Ws),
    assertion(Ws == [w(0,0,0,1),w(0,0,1,0),w(0,1,0,0)]),
    response_status([cell(0,0,0),cell(1,1,1)], ambiguous([0,1])).
test(three_cells_response_not_interaction) :-
    Obs = [cell(0,0,0),cell(1,0,1),cell(0,1,0)],
    worlds_for(Obs, Ws),
    assertion(Ws == [w(0,1,0,0),w(0,1,0,1)]),
    response_status(Obs, identified(1)).
test(four_cells) :-
    worlds_for([cell(0,0,0),cell(1,0,1),cell(0,1,0),cell(1,1,2)], Ws),
    assertion(Ws == [w(0,1,0,1)]).
test(no_observations) :-
    worlds_for([], Ws), length(Ws,16),
    response_status([], ambiguous([0,1])).
test(contradiction) :-
    response_status([cell(0,0,0),cell(0,0,1)], inconsistent).
test(duplicate_agreement) :-
    worlds_for([cell(0,0,0)], A),
    worlds_for([cell(0,0,0),cell(0,0,0)], B),
    assertion(A == B).
test(invalid_policy,[fail]) :- worlds_for([cell(2,0,1)], _).
test(unbound_observation,[fail]) :- worlds_for([cell(_,0,1)], _).
:- end_tests(feedback_identification).
