:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic source_burden/3, target_burden/2, map_edge/4.
:- dynamic target_cover/1, withdrawal/2, debt_trace/2, debt_count_mode/1.
:- dynamic conflict/4, path_edge/5.
:- dynamic packet_id/1, claim_scope/1, source_ontology/1, target_ontology/1.
:- dynamic witness_future_burden/1.
:- dynamic expected_debt_complete/1, expected_merge_preserved/1.
:- dynamic expected_path_conflict/1, expected_arbitration/1, expected_same_label_drift/1.
:- dynamic seen_header/0, seen_end/0.

reset_db :-
    retractall(source_burden(_,_,_)), retractall(target_burden(_,_)),
    retractall(map_edge(_,_,_,_)), retractall(target_cover(_)),
    retractall(withdrawal(_,_)), retractall(debt_trace(_,_)),
    retractall(debt_count_mode(_)), retractall(conflict(_,_,_,_)),
    retractall(path_edge(_,_,_,_,_)), retractall(packet_id(_)),
    retractall(claim_scope(_)), retractall(source_ontology(_)),
    retractall(target_ontology(_)), retractall(witness_future_burden(_)),
    retractall(expected_debt_complete(_)), retractall(expected_merge_preserved(_)),
    retractall(expected_path_conflict(_)), retractall(expected_arbitration(_)),
    retractall(expected_same_label_drift(_)),
    retractall(seen_header), retractall(seen_end).

atomize(S,A) :- atom_string(A,S).
plus_atoms(S,Atoms) :-
    split_string(S,"+","",Parts), Parts \= [],
    maplist(atomize,Parts,A0), sort(A0,Atoms).

parse_line(Line) :-
    normalize_space(string(N), Line),
    ( N="" -> true
    ; sub_string(N,0,1,_,"#") -> true
    ; seen_end -> true
    ; split_string(N," \t"," \t",T),
      ( T=["REALREVISE","0.12"] ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL ~q~n',[T]), fail)
      ; seen_header ->
          (parse_tokens(T) -> true ; format(user_error,'PROLOG_PARSE_FAIL ~q~n',[T]), fail)
      ; format(user_error,'PROLOG_HEADER_REQUIRED ~s~n',[Line]), fail
      )
    ).

parse_tokens(["REALREVISE","0.12"]) :- \+ seen_header, assertz(seen_header).
parse_tokens(["id",S]) :- atomize(S,A), assertz(packet_id(A)).
parse_tokens(["claim_scope",S]) :- atomize(S,A), assertz(claim_scope(A)).
parse_tokens(["source_ontology",S]) :- atomize(S,A), assertz(source_ontology(A)).
parse_tokens(["target_ontology",S]) :- atomize(S,A), assertz(target_ontology(A)).
parse_tokens(["source_burden",I,Cs,S]) :-
    atomize(I,AI), atomize(S,AS), member(AS,['DEBT','CLEAR']),
    plus_atoms(Cs,ACs), \+ source_burden(AI,_,_), assertz(source_burden(AI,ACs,AS)).
parse_tokens(["target_burden",I,Cs]) :-
    atomize(I,AI), plus_atoms(Cs,ACs),
    \+ target_burden(AI,_), assertz(target_burden(AI,ACs)).
parse_tokens(["map",Ss,K,Ts,P]) :-
    plus_atoms(Ss,ASs), atomize(K,AK),
    member(AK,['EXACT','REFINE','MERGE','OVERLAP','DISJOINT','UNMAPPED']),
    (Ts="" -> ATs=[] ; plus_atoms(Ts,ATs)),
    atomize(P,AP), member(AP,['INTERNAL','EXTERNAL','MIXED']),
    assertz(map_edge(ASs,AK,ATs,AP)).
parse_tokens(["target_cover",Ts]) :-
    plus_atoms(Ts,ATs), forall(member(T,ATs),assertz(target_cover(T))).
parse_tokens(["withdraw_source",S,V]) :-
    atomize(S,AS), atomize(V,AV), member(AV,['DECLARED','NONE']), assertz(withdrawal(AS,AV)).
parse_tokens(["debt_trace",S,T]) :- atomize(S,AS), atomize(T,AT), assertz(debt_trace(AS,AT)).
parse_tokens(["debt_count_mode",M]) :-
    atomize(M,AM), member(AM,['SOURCE_ANCESTRY','TARGET_CARRIER']), assertz(debt_count_mode(AM)).
parse_tokens(["conflict",I,S,T,K]) :-
    atomize(I,AI), atomize(S,AS), atomize(T,AT), atomize(K,AK),
    member(AK,['MANDATE','WITHDRAWAL','UNMAPPED','MERGE_COLLISION']),
    assertz(conflict(AI,AS,AT,AK)).
parse_tokens(["path",I,S,V,T,K]) :-
    atomize(I,AI), atomize(S,AS), atomize(V,AV), atomize(T,AT), atomize(K,AK),
    member(AK,['FULL','PARTIAL','NONE']), assertz(path_edge(AI,AS,AV,AT,AK)).
parse_tokens(["witness_future_burden",S]) :- atomize(S,A), assertz(witness_future_burden(A)).
parse_tokens(["authorize_debt_complete",S]) :- atomize(S,A), assertz(expected_debt_complete(A)).
parse_tokens(["authorize_merge_preserved",S]) :- atomize(S,A), assertz(expected_merge_preserved(A)).
parse_tokens(["authorize_path_conflict",S]) :- atomize(S,A), assertz(expected_path_conflict(A)).
parse_tokens(["authorize_arbitration",S]) :- atomize(S,A), assertz(expected_arbitration(A)).
parse_tokens(["authorize_same_label_drift",S]) :- atomize(S,A), assertz(expected_same_label_drift(A)).
parse_tokens(["END"]) :- assertz(seen_end).

load_packet(File) :-
    reset_db,
    read_file_to_string(File,S,[]),
    split_string(S,"\n","\r",Lines),
    maplist(parse_line,Lines),
    seen_header, seen_end, packet_id(_), claim_scope(_), source_ontology(_), target_ontology(_),
    source_burden(_,_,_), target_burden(_,_), debt_count_mode(_), witness_future_burden(_),
    \+ (map_edge(Ss,_,_,_), member(X,Ss), \+ source_burden(X,_,_)),
    \+ (map_edge(_,_,Ts,_), member(X,Ts), \+ target_burden(X,_)),
    \+ (target_cover(X), \+ target_burden(X,_)),
    \+ (withdrawal(X,_), \+ source_burden(X,_,_)),
    \+ (debt_trace(S0,T0), (\+ source_burden(S0,_,_); \+ target_burden(T0,_))).

semantic_kind('EXACT').
semantic_kind('REFINE').
semantic_kind('MERGE').
semantic_kind('OVERLAP').

mapped_source(S) :- map_edge(Ss,K,_,_), semantic_kind(K), member(S,Ss).
mapped_target(T) :- map_edge(_,K,Ts,_), semantic_kind(K), member(T,Ts).

target_union(Ts,U) :-
    findall(C,(member(T,Ts),target_burden(T,Cs),member(C,Cs)),X),
    sort(X,U).

targets_covered(Ts) :- forall(member(T,Ts),target_cover(T)).
traces_complete(S,Ts) :- forall(member(T,Ts),debt_trace(S,T)).

debt_ok(S) :- withdrawal(S,'DECLARED'), !.
debt_ok(S) :-
    source_burden(S,SCs,'DEBT'),
    map_edge(Ss,K,Ts,_), member(S,Ss),
    ( K='EXACT' ; K='REFINE' ),
    Ss=[S], targets_covered(Ts), target_union(Ts,U), sort(SCs,SU), SU=U,
    traces_complete(S,Ts), !.
debt_ok(S) :-
    source_burden(S,SCs,'DEBT'),
    map_edge(Ss,'MERGE',Ts,_), member(S,Ss),
    targets_covered(Ts), target_union(Ts,U), sort(SCs,SU), ord_subset(SU,U),
    traces_complete(S,Ts), !.

same_label_drift :-
    source_burden(I,SCs,_), target_burden(I,TCs), sort(SCs,S), sort(TCs,T), S \= T, !.

different_label_exact_alias :-
    map_edge([S],'EXACT',[T],_), S \= T,
    source_burden(S,SCs,_), target_burden(T,TCs),
    sort(SCs,X), sort(TCs,X), !.

refinement_multiplicity :-
    source_burden(S,_,'DEBT'), map_edge(Ss,'REFINE',Ts,_),
    member(S,Ss), length(Ts,N), N>1, !.

merge_collapse :-
    map_edge(Ss,'MERGE',Ts,_),
    member(S,Ss), source_burden(S,_,'DEBT'),
    member(T,Ts), \+ debt_trace(S,T), !.

direct_composed_conflict :-
    path_edge(_,S,'DIRECT',T,K1),
    path_edge(_,S,V,T,K2), V \= 'DIRECT', K1 \= K2, !.

count_distinct(X,G,N) :- findall(X,G,Xs), sort(Xs,U), length(U,N).
yes(true,'YES') :- !.
yes(_,'NO').
join_or_none([], 'NONE').
join_or_none(Xs,A) :- Xs \= [], atomic_list_concat(Xs,'+',A).

check_expected(DC,MP,PC,AR,SD) :-
    (expected_debt_complete(X)->X=DC;true),
    (expected_merge_preserved(X)->X=MP;true),
    (expected_path_conflict(X)->X=PC;true),
    (expected_arbitration(X)->X=AR;true),
    (expected_same_label_drift(X)->X=SD;true).

run(File) :-
    load_packet(File),
    count_distinct(S,source_burden(S,_,_),SourceCount),
    count_distinct(T,target_burden(T,_),TargetCount),
    count_distinct(I,map_edge(_,_,_,I),_), % harmless provenance enumeration
    findall(1,map_edge(_,_,_,_),Maps), length(Maps,MapCount),
    findall(1,map_edge(_,'EXACT',_,_),E0), length(E0,ExactCount),
    findall(1,map_edge(_,'REFINE',_,_),R0), length(R0,RefineCount),
    findall(1,map_edge(_,'MERGE',_,_),M0), length(M0,MergeCount),
    findall(1,map_edge(_,'OVERLAP',_,_),O0), length(O0,OverlapCount),
    findall(S,(source_burden(S,_,_),\+ mapped_source(S)),US0), sort(US0,US), length(US,UnmappedCount),
    join_or_none(US,UnmappedAtom),
    findall(T,(target_burden(T,_),\+ mapped_target(T)),NT0), sort(NT0,NT), length(NT,NovelCount),
    join_or_none(NT,NovelAtom),
    (same_label_drift->SDB=true;SDB=false), yes(SDB,SameDrift),
    (different_label_exact_alias->DAB=true;DAB=false), yes(DAB,Alias),
    findall(S,source_burden(S,_,'DEBT'),DS0), sort(DS0,DS), length(DS,DebtCount),
    (\+ (member(S,DS),\+ debt_ok(S))->DCB=true;DCB=false), yes(DCB,DebtComplete),
    debt_count_mode(Mode),
    (refinement_multiplicity->RMB=true;RMB=false), yes(RMB,RefMult),
    (Mode='TARGET_CARRIER',RMB=true->DDB=true;DDB=false), yes(DDB,DoubleCount),
    (merge_collapse->MCB=true;MCB=false), yes(MCB,Collapse),
    (MCB=true->MPB=false;MPB=true), yes(MPB,MergePreserved),
    count_distinct(S,mapped_source(S),ComparableCount),
    findall(1,conflict(_,_,_,_),Cs), length(Cs,ConflictCount),
    (ConflictCount>0->ARB=true;ARB=false), yes(ARB,Arbitration),
    (direct_composed_conflict->PCB=true;PCB=false), yes(PCB,PathConflict),
    ((DCB=false;DDB=true;MCB=true;PCB=true;ARB=true)->ROB=true;ROB=false), yes(ROB,Reopen),
    (ROB=true->State='REOPEN_REQUIRED';ComparableCount>0->State='ADMISSIBLE_MAPPED_SUBSPACE';State='HOLD'),
    format('revision.source_burden_count=~w~n',[SourceCount]),
    format('revision.target_burden_count=~w~n',[TargetCount]),
    format('revision.map_count=~w~n',[MapCount]),
    format('revision.exact_count=~w~n',[ExactCount]),
    format('revision.refine_count=~w~n',[RefineCount]),
    format('revision.merge_count=~w~n',[MergeCount]),
    format('revision.overlap_count=~w~n',[OverlapCount]),
    format('revision.unmapped_source_count=~w~n',[UnmappedCount]),
    format('revision.unmapped_sources=~w~n',[UnmappedAtom]),
    format('revision.target_novel_burden_count=~w~n',[NovelCount]),
    format('revision.target_novel_burdens=~w~n',[NovelAtom]),
    format('revision.same_label_drift=~w~n',[SameDrift]),
    format('revision.different_label_exact_alias=~w~n',[Alias]),
    format('revision.debt_source_count=~w~n',[DebtCount]),
    format('revision.debt_transport_complete=~w~n',[DebtComplete]),
    format('revision.debt_accounting_mode=~w~n',[Mode]),
    format('revision.refinement_multiplicity=~w~n',[RefMult]),
    format('revision.debt_double_count_detected=~w~n',[DoubleCount]),
    format('revision.debt_collapse_detected=~w~n',[Collapse]),
    format('revision.merge_provenance_preserved=~w~n',[MergePreserved]),
    format('revision.comparable_source_burden_count=~w~n',[ComparableCount]),
    writeln('revision.comparability_mode=MAPPED_SUBSPACE_ONLY'),
    format('revision.conflict_count=~w~n',[ConflictCount]),
    format('revision.arbitration_required=~w~n',[Arbitration]),
    writeln('revision.conflict_scalar_default=OFF'),
    format('revision.direct_composed_conflict=~w~n',[PathConflict]),
    format('revision.reopen_required=~w~n',[Reopen]),
    writeln('revision.reopen_on_path_conflict=YES'),
    writeln('revision.world_burden_identity_inferred=NO'),
    writeln('revision.future_revision_closed=NO'),
    writeln('revision.newer_ontology_truth_oracle=NO'),
    writeln('revision.provenance_truth_oracle=NO'),
    writeln('revision.guidance_mode=VERSIONED_LOSS_AWARE_TRANSPORT'),
    format('revision.state=~w~n',[State]),
    witness_future_burden(W),
    format('witness.future_burden=~w~n',[W]),
    check_expected(DebtComplete,MergePreserved,PathConflict,Arbitration,SameDrift).
