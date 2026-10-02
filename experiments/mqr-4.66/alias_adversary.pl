:- use_module(library(readutil)).
:- dynamic q3_block/2.

bit(S,B,V) :- V is (S >> B) /\ 1.

setbit(S,B,T) :- T is S \/ (1 << B).
clrbit(S,B,T) :- T is S /\ \(1 << B).

event(E) :- between(0,17,E).

step(S,0,T) :- setbit(S,0,T).
step(S,1,T) :- setbit(S,1,T).
step(S,2,T) :- setbit(S,2,T).
step(S,3,T) :- clrbit(S,0,T).
step(S,4,T) :- clrbit(S,1,T).
step(S,5,T) :- clrbit(S,2,T).
step(S,6,T) :- setbit(S,3,T).
step(S,7,T) :- setbit(S,4,T).
step(S,8,T) :- setbit(S,5,T).
step(S,9,T) :- clrbit(S,3,T).
step(S,10,T) :- clrbit(S,4,T).
step(S,11,T) :- clrbit(S,5,T).
step(S,12,T) :- setbit(S,7,T).
step(S,13,T) :- clrbit(S,7,T).
step(S,14,T) :- bit(S,7,P), (P=:=1 -> setbit(S,6,T) ; clrbit(S,6,T)).
step(S,15,T) :- setbit(S,8,T).
step(S,16,T) :- clrbit(S,8,T).
step(S,17,T) :-
    bit(S,8,X),
    ( X =:= 1 -> setbit(S,2,A), clrbit(A,5,T) ; T=S ).

unresolved(S,U) :-
    findall(I,
      (between(0,2,I), bit(S,I,R), J is I+3, bit(S,J,Sep), R=:=1, Sep=:=0),
      Xs),
    length(Xs,U).

label(S,L) :-
    unresolved(S,U),
    bit(S,6,C),
    ( U=:=0, C=:=1 -> Mask is 7, Rel=1 ; Mask is 11, Rel=0 ),
    L is U*64 + Mask*2 + Rel.

visible(S,V) :- V is S /\ 127.

same_visible_prov_pair(S,T) :-
    between(0,511,S), between(0,511,T), S<T,
    visible(S,V), visible(T,V),
    bit(S,8,X), bit(T,8,X),
    bit(S,7,P1), bit(T,7,P2), P1=\=P2.

same_visible_ext_pair(S,T) :-
    between(0,511,S), between(0,511,T), S<T,
    visible(S,V), visible(T,V),
    bit(S,7,P), bit(T,7,P),
    bit(S,8,X1), bit(T,8,X2), X1=\=X2.

same_q1_pair(S,T) :-
    between(0,511,S), between(0,511,T), S<T,
    label(S,L), label(T,L).

apply_word(S,[],S).
apply_word(S,[E|Es],T) :- step(S,E,U), apply_word(U,Es,T).

distinguishes(S,T,W) :-
    apply_word(S,W,S1), apply_word(T,W,T1),
    label(S1,L1), label(T1,L2), L1=\=L2.

word_of_length(0,[]).
word_of_length(N,[E|Es]) :-
    N>0, event(E), N1 is N-1, word_of_length(N1,Es).

shortest_for_pair(S,T,Max,D,W) :-
    between(0,Max,D),
    word_of_length(D,W),
    distinguishes(S,T,W), !.

shortest_q1(Max,S,T,D,W) :-
    between(0,Max,D),
    same_q1_pair(S,T),
    word_of_length(D,W),
    distinguishes(S,T,W), !.

load_q3(File) :-
    retractall(q3_block(_,_)),
    open(File,read,In),
    read_line_to_string(In,_Header),
    load_q3_lines(In),
    close(In).

load_q3_lines(In) :-
    read_line_to_string(In,Line),
    ( Line == end_of_file -> true
    ; split_string(Line,"\t","",Parts),
      Parts=[SS,BS],
      number_string(S,SS), number_string(B,Bs),
      assertz(q3_block(S,B)),
      load_q3_lines(In)
    ).

q3_violation(S,T,E) :-
    q3_block(S,B), q3_block(T,B), S<T,
    event(E),
    step(S,E,S1), step(T,E,T1),
    q3_block(S1,B1), q3_block(T1,B2),
    B1=\=B2.

main :-
    same_visible_prov_pair(PS,PT),
    step(PS,14,PS1), step(PT,14,PT1),
    label(PS1,PL1), label(PT1,PL2), PL1=\=PL2, !,
    format('MQR466_PROLOG_PROVENANCE_WITNESS=~w,~w,[14]~n',[PS,PT]),

    same_visible_ext_pair(XS,XT),
    step(XS,17,XS1), step(XT,17,XT1),
    label(XS1,XL1), label(XT1,XL2), XL1=\=XL2, !,
    format('MQR466_PROLOG_NOVELTY_WITNESS=~w,~w,[17]~n',[XS,XT]),

    shortest_q1(8,Q1S,Q1T,Q1D,Q1W),
    format('MQR466_PROLOG_Q1_SHORTEST=~w,~w,~w,~w~n',[Q1S,Q1T,Q1D,Q1W]),

    load_q3('experiments/mqr-4.66/results/haskell_q3_mapping.tsv'),
    ( q3_violation(S,T,E) ->
        ( shortest_for_pair(S,T,8,D,W) ->
            format('MQR466_PROLOG_Q3_SEPARATING=~w,~w,~w,~w,first_block_event_~w~n',[S,T,D,W,E])
        ; format('MQR466_PROLOG_Q3_BLOCK_VIOLATION_NO_LABEL_WITNESS_LE8=~w,~w,~w~n',[S,T,E]), fail )
    ; format('MQR466_PROLOG_Q3_STABLE=YES~n',[]) ),

    format('MQR466_PROLOG_ADVERSARY=PASS~n',[]).

:- initialization(main, main).
