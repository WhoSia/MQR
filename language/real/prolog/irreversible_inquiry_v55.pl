:- module(irreversible_inquiry_v55, [strategy/3]).
:- use_module(library(pairs)).
:- use_module(library(plunit)).

hypothesis(three,0).
hypothesis(three,1).
hypothesis(three,2).
hypothesis(four,w(G,B)) :- member(G,[0,1]), member(B,[0,1]).
action(three,0).
action(three,1).
action(four,split).
action(four,left).
action(four,right).

signature(0,_,0).
signature(1,P,P).
signature(2,P,Y) :- Y is 1-P.

step(three,W,start,P,dead,Y) :- signature(W,P,Y).
step(three,_,dead,_,dead,0).
step(four,w(G,_),start,split,ready,G).
step(four,_,start,A,dead,0) :- memberchk(A,[left,right]).
step(four,w(G,B),ready,A,dead,Y) :-
    ( (A=left,G=0 ; A=right,G=1) -> Y=B ; Y=0 ).
step(four,_,dead,_,dead,0).

% Beliefs retain hypothesis identity even when current physical states coincide.
branches(E,B,A,Groups) :-
    findall(Y-case(W,T),(member(case(W,S),B),step(E,W,S,A,T,Y)),Raw),
    keysort(Raw,Sorted), group_pairs_by_key(Sorted,Groups).

wins(_,B,_,leaf(W)) :-
    findall(H,member(case(H,_),B),Hs), sort(Hs,[W]), !.
wins(E,B,Seen,node(A,Subtrees)) :-
    \+ memberchk(B,Seen), action(E,A),
    branches(E,B,A,Groups), Groups \= [],
    maplist(win_branch(E,[B|Seen]),Groups,Subtrees).

win_branch(E,Seen,Y-B,Y-T) :- sort(B,Canonical), wins(E,Canonical,Seen,T).

% Exact for these finite, deterministic, complete tables. A winning finite
% tree can remove a repeated belief along a branch, so cycle pruning is sound.
strategy(E,Ws,Result) :-
    ground(E-Ws), memberchk(E,[three,four]), is_list(Ws), Ws \= [],
    maplist(hypothesis(E),Ws), sort(Ws,Unique),
    findall(case(W,start),member(W,Unique),B),
    ( once(wins(E,B,[],T)) -> Result=identified_by(T) ; Result=no_strategy ).

:- begin_tests(irreversible_inquiry).
test(all_pairs) :-
    forall(member(P,[[0,1],[0,2],[1,2]]),strategy(three,P,identified_by(_))).
test(no_global) :- strategy(three,[0,1,2],no_strategy).
test(already_known) :- strategy(three,[1],identified_by(leaf(1))).
test(adaptive_four) :-
    strategy(four,[w(0,0),w(0,1),w(1,0),w(1,1)],
      identified_by(node(split,[0-node(left,[0-leaf(w(0,0)),1-leaf(w(0,1))]),
                                1-node(right,[0-leaf(w(1,0)),1-leaf(w(1,1))])])).
test(invalid_world,[fail]) :- strategy(three,[3],_).
test(empty,[fail]) :- strategy(four,[],_).
test(unbound,[fail]) :- strategy(three,[_],_).
:- end_tests(irreversible_inquiry).
