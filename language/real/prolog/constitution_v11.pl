:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic source/3, burden/2, obligation/4, predecessor/3.
:- dynamic successor/2, withdrawal/2, debt_transfer/2.
:- dynamic packet_id/1, claim_scope/1, challenge_route/1.
:- dynamic escape_burden/1, witness_omitted_burden/1.
:- dynamic expected_laundering/1, expected_successor_coverage/1.
:- dynamic expected_common_mode/1, expected_reopen/1, expected_admissible/1.
:- dynamic seen_header/0, seen_end/0.

reset_db :-
    retractall(source(_,_,_)), retractall(burden(_,_)),
    retractall(obligation(_,_,_,_)), retractall(predecessor(_,_,_)),
    retractall(successor(_,_)), retractall(withdrawal(_,_)),
    retractall(debt_transfer(_,_)), retractall(packet_id(_)),
    retractall(claim_scope(_)), retractall(challenge_route(_)),
    retractall(escape_burden(_)), retractall(witness_omitted_burden(_)),
    retractall(expected_laundering(_)),
    retractall(expected_successor_coverage(_)),
    retractall(expected_common_mode(_)), retractall(expected_reopen(_)),
    retractall(expected_admissible(_)),
    retractall(seen_header), retractall(seen_end).

atomize(S,A) :- atom_string(A,S).

plus_atoms(S,Atoms) :-
    split_string(S,"+","",Parts),
    Parts \= [],
    maplist(atomize,Parts,Atoms0),
    sort(Atoms0,Atoms).

parse_line(Line) :-
    normalize_space(string(N), Line),
    ( N="" -> true
    ; sub_string(N,0,1,_,"#") -> true
    ; seen_end -> true
    ; split_string(N," \t"," \t",T),
      ( T=["REALCONSTITUTE","0.11"] ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]), fail)
      ; seen_header ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL tokens=~q line=~s~n',[T,Line]), fail)
      ; format(user_error,'PROLOG_HEADER_REQUIRED line=~s~n',[Line]), fail
      )
    ).

parse_tokens(["REALCONSTITUTE","0.11"]) :- \+ seen_header, assertz(seen_header).
parse_tokens(["id",S]) :- atomize(S,A), assertz(packet_id(A)).
parse_tokens(["claim_scope",S]) :- atomize(S,A), assertz(claim_scope(A)).
parse_tokens(["agenda_source",I,A,K]) :-
    atomize(I,AI), atomize(A,AA), atomize(K,AK),
    member(AK,['ENDOGENOUS','EXTERNAL','MIXED']),
    \+ source(AI,_,_), assertz(source(AI,AA,AK)).
parse_tokens(["burden",I,K]) :-
    atomize(I,AI), atomize(K,AK),
    member(AK,['GENERATOR','QUERY','REPRESENTATION','INSTRUMENT','RESIDUAL','EXTERNAL_CASE']),
    \+ burden(AI,_), assertz(burden(AI,AK)).
parse_tokens(["obligation",I,S,M,Bs]) :-
    atomize(I,AI), atomize(S,AS), atomize(M,AM),
    member(AM,['MANDATORY','OPTIONAL']),
    plus_atoms(Bs,ABs),
    \+ obligation(AI,_,_,_), assertz(obligation(AI,AS,AM,ABs)).
parse_tokens(["predecessor",I,Bs,D]) :-
    atomize(I,AI), atomize(D,AD), member(AD,['DEBT','CLEAR']),
    plus_atoms(Bs,ABs),
    \+ predecessor(AI,_,_), assertz(predecessor(AI,ABs,AD)).
parse_tokens(["successor",O,Ns]) :-
    atomize(O,AO), plus_atoms(Ns,ANs),
    \+ successor(AO,_), assertz(successor(AO,ANs)).
parse_tokens(["withdraw",O,S]) :-
    atomize(O,AO), atomize(S,AS), member(AS,['DECLARED','NONE']),
    \+ withdrawal(AO,_), assertz(withdrawal(AO,AS)).
parse_tokens(["debt_transfer",O,Ns]) :-
    atomize(O,AO), plus_atoms(Ns,ANs),
    \+ debt_transfer(AO,_), assertz(debt_transfer(AO,ANs)).
parse_tokens(["challenge_route",S]) :-
    atomize(S,A), member(A,['LIVE','ABSENT']), assertz(challenge_route(A)).
parse_tokens(["escape_burden",S]) :- atomize(S,A), assertz(escape_burden(A)).
parse_tokens(["witness_omitted_burden",S]) :-
    atomize(S,A), assertz(witness_omitted_burden(A)).
parse_tokens(["authorize_laundering",S]) :-
    atomize(S,A), assertz(expected_laundering(A)).
parse_tokens(["authorize_successor_coverage",S]) :-
    atomize(S,A), assertz(expected_successor_coverage(A)).
parse_tokens(["authorize_common_mode",S]) :-
    atomize(S,A), assertz(expected_common_mode(A)).
parse_tokens(["authorize_reopen",S]) :-
    atomize(S,A), assertz(expected_reopen(A)).
parse_tokens(["authorize_admissible",S]) :-
    atomize(S,A), assertz(expected_admissible(A)).
parse_tokens(["END"]) :- assertz(seen_end).

load_packet(File) :-
    reset_db,
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    maplist(parse_line,Lines),
    seen_header, seen_end,
    packet_id(_), claim_scope(_), source(_,_,_), burden(_,_),
    obligation(_,_,_,_), challenge_route(_), escape_burden(E),
    witness_omitted_burden(_),
    \+ (obligation(_,S0,_,_), \+ source(S0,_,_)),
    \+ (obligation(_,_,_,Bs), member(B,Bs), \+ burden(B,_)),
    \+ (predecessor(_,Bs,_), member(B,Bs), \+ burden(B,_)),
    \+ (successor(O,_), \+ predecessor(O,_,_)),
    \+ (successor(_,Ns), member(N,Ns), \+ obligation(N,_,_,_)),
    \+ (withdrawal(O,_), \+ predecessor(O,_,_)),
    \+ (debt_transfer(O,_), \+ predecessor(O,_,_)),
    \+ (debt_transfer(_,Ns), member(N,Ns), \+ obligation(N,_,_,_)),
    (E='NONE';burden(E,_)).

yes(true,'YES') :- !.
yes(_,'NO').

join_or_none([], 'NONE').
join_or_none(Xs, A) :- Xs \= [], atomic_list_concat(Xs,'+',A).

obligation_union(Ids,Union) :-
    findall(B,(member(I,Ids),obligation(I,_,_,Bs),member(B,Bs)),Xs),
    sort(Xs,Union).

covered_burdens(Union) :-
    findall(B,(obligation(_,_,_,Bs),member(B,Bs)),Xs),
    sort(Xs,Union).

all_burdens(All) :-
    findall(B,burden(B,_),Xs), sort(Xs,All).

successor_full(Old) :-
    predecessor(Old,OldBs,_),
    successor(Old,News),
    obligation_union(News,Union),
    sort(OldBs,OldSet),
    ord_subset(OldSet,Union).

debt_transfer_full(Old) :-
    predecessor(Old,OldBs,_),
    successor(Old,Successors),
    debt_transfer(Old,Targets),
    forall(member(T,Targets),memberchk(T,Successors)),
    obligation_union(Targets,Union),
    sort(OldBs,OldSet),
    ord_subset(OldSet,Union).

common_mode(true) :-
    findall(S,source(S,_,_),Ss0), sort(Ss0,Ss), length(Ss,N), N>1,
    findall(A,source(_,A,_),As0), sort(As0,As), length(As,M), M<N, !.
common_mode(false).

endogenous_only(true) :-
    findall(S,obligation(_,S,'MANDATORY',_),Ss),
    Ss \= [],
    \+ (member(S,Ss), source(S,_,K), K \= 'ENDOGENOUS'), !.
endogenous_only(false).

external_present(true) :-
    source(_,_,K), member(K,['EXTERNAL','MIXED']), !.
external_present(false).

invalid_successor(Old) :- successor(Old,_), \+ successor_full(Old).

debt_transfer_required(Old) :-
    predecessor(Old,_,'DEBT'),
    \+ withdrawal(Old,'DECLARED').

debt_transfer_missing(Old) :-
    debt_transfer_required(Old),
    \+ (successor_full(Old), debt_transfer_full(Old)).

debt_transfer_item(Old) :-
    debt_transfer_required(Old),
    successor_full(Old),
    debt_transfer_full(Old).

count_solutions(Template,Goal,N) :-
    findall(Template,Goal,Xs), sort(Xs,Us), length(Us,N).

check_expected(Launder,Successor,Common,Reopen,Admissible) :-
    (expected_laundering(X)->X=Launder;true),
    (expected_successor_coverage(X)->X=Successor;true),
    (expected_common_mode(X)->X=Common;true),
    (expected_reopen(X)->X=Reopen;true),
    (expected_admissible(X)->X=Admissible;true).

run(File) :-
    load_packet(File),
    findall(O,obligation(O,_,_,_),Os0), sort(Os0,Os), length(Os,ObligationCount),
    findall(O,obligation(O,_,'MANDATORY',_),Ms0), sort(Ms0,Ms), length(Ms,MandatoryCount),
    all_burdens(AllBurden), length(AllBurden,BurdenCount),
    covered_burdens(Covered), length(Covered,CoveredCount),
    ord_subtract(AllBurden,Covered,Uncovered),
    join_or_none(Covered,BurdenUnion), join_or_none(Uncovered,UncoveredAtom),
    findall(S,source(S,_,_),Ss0), sort(Ss0,Ss), length(Ss,SourceCount),
    findall(A,source(_,A,_),As0), sort(As0,As), length(As,AncestryCount),
    common_mode(CMB), yes(CMB,Common),
    endogenous_only(EOB), yes(EOB,EndogenousOnly),
    external_present(EPB), yes(EPB,ExternalPresent),
    challenge_route(Challenge),
    count_solutions(O,successor(O,_),SuccessorClaimCount),
    count_solutions(O,invalid_successor(O),InvalidSuccessorCount),
    (InvalidSuccessorCount=:=0->SuccessorCoverage='YES';SuccessorCoverage='NO'),
    count_solutions(O,withdrawal(O,'DECLARED'),ExplicitWithdrawalCount),
    count_solutions(O,debt_transfer_required(O),DebtRequiredCount),
    count_solutions(O,debt_transfer_missing(O),DebtMissingCount),
    findall(O,debt_transfer_item(O),DT0), sort(DT0,DT), join_or_none(DT,DebtItems),
    (DebtMissingCount>0->Laundering='YES';Laundering='NO'),
    escape_burden(EscapeBurden),
    (EscapeBurden='NONE'->Escape='NO';Escape='YES'),
    Reopen=Escape,
    ( Challenge='LIVE',
      SuccessorCoverage='YES',
      Laundering='NO',
      Uncovered=[],
      Escape='NO'
      -> Admissible='YES', State='ADMISSIBLE'
      ; Escape='YES'
      -> Admissible='NO', State='REOPEN_REQUIRED'
      ; Admissible='NO', State='HOLD'
    ),
    format('constitution.obligation_count=~w~n',[ObligationCount]),
    format('constitution.mandatory_obligation_count=~w~n',[MandatoryCount]),
    format('constitution.burden_count=~w~n',[BurdenCount]),
    format('constitution.covered_burden_count=~w~n',[CoveredCount]),
    format('constitution.burden_union=~w~n',[BurdenUnion]),
    format('constitution.uncovered_declared_burdens=~w~n',[UncoveredAtom]),
    format('constitution.agenda_source_count=~w~n',[SourceCount]),
    format('constitution.agenda_ancestry_count=~w~n',[AncestryCount]),
    format('constitution.agenda_common_mode=~w~n',[Common]),
    format('constitution.endogenous_only=~w~n',[EndogenousOnly]),
    format('constitution.external_source_present=~w~n',[ExternalPresent]),
    format('constitution.challenge_route=~w~n',[Challenge]),
    format('constitution.successor_claim_count=~w~n',[SuccessorClaimCount]),
    format('constitution.invalid_successor_claim_count=~w~n',[InvalidSuccessorCount]),
    format('constitution.successor_coverage_complete=~w~n',[SuccessorCoverage]),
    format('constitution.explicit_withdrawal_count=~w~n',[ExplicitWithdrawalCount]),
    format('constitution.debt_transfer_required_count=~w~n',[DebtRequiredCount]),
    format('constitution.debt_transfer_missing_count=~w~n',[DebtMissingCount]),
    format('constitution.debt_transfer_items=~w~n',[DebtItems]),
    format('constitution.burden_laundering_detected=~w~n',[Laundering]),
    writeln('constitution.partition_count_authority=REJECT'),
    writeln('constitution.partition_audit_surface=DECLARED_BURDEN_UNION'),
    writeln('constitution.external_source_truth_oracle=NO'),
    writeln('constitution.endogenous_source_truth_oracle=NO'),
    format('constitution.escape_detected=~w~n',[Escape]),
    format('constitution.escape_reconstitution_required=~w~n',[Reopen]),
    writeln('constitution.reopen_on_escape=YES'),
    writeln('constitution.world_obligation_complete=NO'),
    writeln('constitution.omitted_burden_inferred=NO'),
    writeln('constitution.open_world_receipt=REQUIRED'),
    writeln('constitution.guidance_mode=CONTRACT_RELATIVE_CONSTITUTIONAL'),
    format('constitution.admissible_envelope=~w~n',[Admissible]),
    format('constitution.state=~w~n',[State]),
    check_expected(Laundering,SuccessorCoverage,Common,Reopen,Admissible).
