:- module(disciplinary_genesis_v55, [compatible/2, withdrawal_status/3]).
:- use_module(library(plunit)).
model(method_mediated).
model(common_context).
bit(0).
bit(1).
outcome(method_mediated,_,R,M,F) :- F is R*M.
outcome(common_context,U,R,_,F) :- F is U*R.
valid_row(row(U,R,M,F)) :- maplist(bit,[U,R,M,F]).
matches(E,row(U,R,M,F)) :- outcome(E,U,R,M,F).
compatible(Rows,E) :-
    ground(Rows), is_list(Rows), maplist(valid_row,Rows),
    model(E), maplist(matches(E),Rows).
withdrawal_status(Rows,context(U,R),Status) :-
    ground(U-R), bit(U), bit(R),
    findall(F,(compatible(Rows,E),outcome(E,U,R,0,F)),Fs),
    sort(Fs,Values),
    ( Values=[] -> Status=inconsistent
    ; Values=[V] -> Status=identified(V)
    ; Status=ambiguous(Values)
    ).
observational_rows([row(0,0,0,0),row(0,1,0,0),
                    row(1,0,1,0),row(1,1,1,1)]).
:- begin_tests(disciplinary_genesis).
test(complete_factual_support) :-
    observational_rows(Rows),
    findall(E,compatible(Rows,E),[method_mediated,common_context]).
test(necessity_ambiguous) :-
    observational_rows(Rows),
    withdrawal_status(Rows,context(1,1),ambiguous([0,1])).
test(withdrawal_failure) :-
    observational_rows(Rows),
    withdrawal_status([row(1,1,0,0)|Rows],context(1,1),identified(0)).
test(withdrawal_success) :-
    observational_rows(Rows),
    withdrawal_status([row(1,1,0,1)|Rows],context(1,1),identified(1)).
test(inconsistent) :-
    withdrawal_status([row(1,1,1,0)],context(1,1),inconsistent).
test(readiness_absent) :-
    withdrawal_status([],context(1,0),identified(0)).
test(invalid_row,[fail]) :- compatible([row(1,1,1,2)],_).
test(unbound_row,[fail]) :- compatible([row(1,1,1,_)],_).
:- end_tests(disciplinary_genesis).
