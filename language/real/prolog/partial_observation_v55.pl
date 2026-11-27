:- module(partial_observation_v55, [separator/4]).
:- use_module(library(plunit)).

state(0).
state(1).
state(2).
action(0).
action(1).
world(W) :- is_list(W), length(W,6), maplist(state,W).

step(W,S,P,T) :- I is 2*S+P, nth0(I,W,T).
observe(coarse,S,Y) :- (S=:=2 -> Y=1 ; Y=0).
observe(fine,S,S).

% Queue carries reversed action paths. Each equal-output pair expands at most once.
% Scope: known reset 0, common sensor, deterministic time-invariant tables.
separator(Mode,A,B,Result) :-
    ground(Mode-A-B), memberchk(Mode,[coarse,fine]), world(A), world(B),
    bfs(Mode,A,B,[node(0,0,[])],[],Result).

bfs(_,_,_,[],_,equivalent_from_reset).
bfs(Mode,A,B,[node(S,T,Rev)|Rest],Seen,Result) :-
    observe(Mode,S,Y), observe(Mode,T,Z),
    ( Y \= Z -> reverse(Rev,Word), Result=separates(Word)
    ; memberchk(S-T,Seen) -> bfs(Mode,A,B,Rest,Seen,Result)
    ; findall(node(X,U,[P|Rev]),
          (action(P),step(A,S,P,X),step(B,T,P,U)), Children),
      append(Rest,Children,Queue),
      bfs(Mode,A,B,Queue,[S-T|Seen],Result)
    ).

:- begin_tests(partial_observation).
test(coarse_four) :-
    separator(coarse,[0,1,0,2,0,0],[0,1,0,2,0,1],separates([1,1,1,1])).
test(fine_three) :-
    separator(fine,[0,1,0,2,0,0],[0,1,0,2,0,1],separates([1,1,1])).
test(same_world) :-
    separator(coarse,[0,1,0,2,0,0],[0,1,0,2,0,0],equivalent_from_reset).
test(unreachable_rows_even_fine) :-
    separator(fine,[0,0,0,0,0,0],[0,0,2,2,2,2],equivalent_from_reset).
test(refinement_can_break_equivalence) :-
    separator(coarse,[0,0,0,0,0,0],[1,1,1,1,1,1],equivalent_from_reset),
    separator(fine,[0,0,0,0,0,0],[1,1,1,1,1,1],separates([0])).
test(invalid_mode,[fail]) :-
    separator(unknown,[0,1,0,2,0,0],[0,1,0,2,0,1],_).
test(invalid_state,[fail]) :-
    separator(coarse,[0,1,0,3,0,0],[0,1,0,2,0,1],_).
test(unbound_world,[fail]) :-
    separator(coarse,_,[0,1,0,2,0,1],_).
:- end_tests(partial_observation).
