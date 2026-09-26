:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic packet_id/1, claim_scope/1, source_ontology/1, target_ontology/1.
:- dynamic candidate_relation/1, proposer/2, adjudicator/3, standard/3.
:- dynamic witness/5, challenge/3, meta_dep/2, meta_anchor/2, force_singleton/1.
:- dynamic expected_authority/1, expected_singleton/1, expected_self/1.
:- dynamic expected_capture/1, expected_meta_cycle/1, expected_world_separator/1.
:- dynamic seen_header/0, seen_end/0.

relations(['DISJOINT','EXACT','MERGE','OVERLAP','REFINE','UNMAPPED']).

reset_db :-
    retractall(packet_id(_)), retractall(claim_scope(_)), retractall(source_ontology(_)),
    retractall(target_ontology(_)), retractall(candidate_relation(_)), retractall(proposer(_,_)),
    retractall(adjudicator(_,_,_)), retractall(standard(_,_,_)), retractall(witness(_,_,_,_,_)),
    retractall(challenge(_,_,_)), retractall(meta_dep(_,_)), retractall(meta_anchor(_,_)),
    retractall(force_singleton(_)), retractall(expected_authority(_)), retractall(expected_singleton(_)),
    retractall(expected_self(_)), retractall(expected_capture(_)), retractall(expected_meta_cycle(_)),
    retractall(expected_world_separator(_)), retractall(seen_header), retractall(seen_end).

atomize(S,A):-atom_string(A,S).
plus_relations(S,R):-split_string(S,"+","",Ps),Ps\=[],maplist(atomize,Ps,A0),maplist(upcase_atom,A0,A1),sort(A1,R),relations(All),ord_subset(R,All).

parse_line(Line):-
    normalize_space(string(N),Line),
    (N=""->true
    ;sub_string(N,0,1,_,"#")->true
    ;seen_end->true
    ;split_string(N," \t"," \t",T),
      (T=["REALMAPAUTH","0.13"]->parse_tokens(T)
      ;seen_header->parse_tokens(T)
      ;format(user_error,'PROLOG_HEADER_REQUIRED ~s~n',[Line]),fail)).

parse_tokens(["REALMAPAUTH","0.13"]):- \+ seen_header,assertz(seen_header).
parse_tokens(["id",S]):-atomize(S,A),assertz(packet_id(A)).
parse_tokens(["claim_scope",S]):-atomize(S,A),assertz(claim_scope(A)).
parse_tokens(["source_ontology",S]):-atomize(S,A),assertz(source_ontology(A)).
parse_tokens(["target_ontology",S]):-atomize(S,A),assertz(target_ontology(A)).
parse_tokens(["candidate_relation",S]):-atomize(S,A0),upcase_atom(A0,A),relations(All),member(A,All),assertz(candidate_relation(A)).
parse_tokens(["proposer",I,A]):-atomize(I,AI),atomize(A,AA),assertz(proposer(AI,AA)).
parse_tokens(["adjudicator",I,A,P]):-atomize(I,AI),atomize(A,AA),atomize(P,P0),upcase_atom(P0,AP),member(AP,['INTERNAL','EXTERNAL','MIXED']),\+adjudicator(AI,_,_),assertz(adjudicator(AI,AA,AP)).
parse_tokens(["standard",I,A,T]):-atomize(I,AI),atomize(A,AA),atomize(T,T0),upcase_atom(T0,AT),member(AT,['PRESEALED','POST_OUTCOME','INHERITED']),\+standard(AI,_,_),assertz(standard(AI,AA,AT)).
parse_tokens(["witness",I,S,A,L,R]):-atomize(I,AI),atomize(S,AS),atomize(A,AA),atomize(L,L0),upcase_atom(L0,AL),member(AL,['DIRECT','META']),plus_relations(R,Rs),assertz(witness(AI,AS,AA,AL,Rs)).
parse_tokens(["challenge",I,M,R]):-atomize(I,AI),atomize(M,M0),upcase_atom(M0,AM),member(AM,['INTERNAL','WORLD_FACING']),plus_relations(R,Rs),assertz(challenge(AI,AM,Rs)).
parse_tokens(["meta_dep",A,B]):-atomize(A,AA),atomize(B,AB),assertz(meta_dep(AA,AB)).
parse_tokens(["meta_anchor",N,K]):-atomize(N,AN),atomize(K,K0),upcase_atom(K0,AK),member(AK,['WORLD_FACING','DECLARED']),assertz(meta_anchor(AN,AK)).
parse_tokens(["force_singleton",S]):-atomize(S,A0),upcase_atom(A0,A),member(A,['YES','NO']),assertz(force_singleton(A)).
parse_tokens(["authorize_mapping_authority",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_authority(A)).
parse_tokens(["authorize_correspondence_singleton",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_singleton(A)).
parse_tokens(["authorize_self_certified",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_self(A)).
parse_tokens(["authorize_capture_risk",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_capture(A)).
parse_tokens(["authorize_meta_cycle",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_meta_cycle(A)).
parse_tokens(["authorize_world_separator",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_world_separator(A)).
parse_tokens(["END"]):-assertz(seen_end).

load_packet(File):-
    reset_db,read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls),maplist(parse_line,Ls),
    seen_header,seen_end,packet_id(_),claim_scope(_),source_ontology(_),target_ontology(_),
    candidate_relation(_),proposer(_,_),adjudicator(_,_,_),standard(_,_,_),witness(_,_,_,_,_),force_singleton(_),
    \+ (witness(_,S0,_,_,_),\+standard(S0,_,_)),
    \+ (witness(_,_,A0,_,_),\+adjudicator(A0,_,_)).

evidence_support(R):-witness(_,_,_,_,R).
evidence_support(R):-challenge(_,_,R).
preworld_support(R):-witness(_,_,_,_,R).
preworld_support(R):-challenge(_,'INTERNAL',R).
direct_support(R):-witness(_,_,_,'DIRECT',R).
meta_support(R):-witness(_,_,_,'META',R).

intersect_all([H|T],R):-foldl(ord_intersection,T,H,R).
support_intersection(Pred,R):-findall(S,call(Pred,S),Ss),(Ss=[]->relations(R);intersect_all(Ss,R)).

self_certified:-proposer(I,A),(adjudicator(I,_,_);adjudicator(_,A,_)),!.
common_ancestry:-findall(I,adjudicator(I,_,_),Is0),sort(Is0,Is),length(Is,N),findall(A,adjudicator(_,A,_),As0),sort(As0,As),length(As,M),N>M.
capture_risk:-proposer(_,A),standard(_,A,_),!.
capture_risk:-standard(_,_, 'POST_OUTCOME'),!.

support_disagreement:-
    findall(S,evidence_support(S),[H|T]),member(X,T),X\=H,!.

path(X,Y,Visited):-meta_dep(X,Y),\+member(Y,Visited).
path(X,Y,Visited):-meta_dep(X,Z),\+member(Z,Visited),path(Z,Y,[Z|Visited]).
meta_cycle:-meta_dep(A,B),path(B,A,[B]),!.

terminal_node(N):- (meta_dep(N,_);meta_dep(_,N)), \+meta_dep(N,_).
unanchored_terminal(N):-terminal_node(N),\+meta_anchor(N,_).

direct_meta_conflict:-
    findall(S,direct_support(S),Ds),Ds\=[],
    findall(S,meta_support(S),Ms),Ms\=[],
    intersect_all(Ds,D),intersect_all(Ms,M),ord_intersection(D,M,[]),!.

yes(true,'YES'):-!.
yes(_,'NO').

authority_state(CAS,Singleton,Forced,MetaCycle,DM,Capture,Self,Common,MetaDebt,Candidate,Authority):-
    (CAS=[]->Authority='CONTESTED_NO_COMMON_RELATION'
    ;Forced=true,Singleton=false->Authority='REOPEN_FORCED_SINGLETON'
    ;MetaCycle=true->Authority='REOPEN_META_CYCLE'
    ;DM=true->Authority='REOPEN_DIRECT_META_CONFLICT'
    ;Capture=true->Authority='HOLD_STANDARD_CAPTURE'
    ;Self=true->Authority='HOLD_SELF_CERTIFIED'
    ;Common=true->Authority='HOLD_COMMON_ANCESTRY'
    ;MetaDebt>0->Authority='HOLD_META_DEBT'
    ;\+member(Candidate,CAS)->Authority='HOLD_CANDIDATE_UNSUPPORTED'
    ;Singleton=false->Authority='SET_VALUED_PROVISIONAL'
    ;Authority='EARNED_PROVISIONAL').

check_expected(A,S,Self,Capture,Cycle,WS):-
    (expected_authority(X)->X=A;true),
    (expected_singleton(X)->X=S;true),
    (expected_self(X)->X=Self;true),
    (expected_capture(X)->X=Capture;true),
    (expected_meta_cycle(X)->X=Cycle;true),
    (expected_world_separator(X)->X=WS;true).

run(File):-
    load_packet(File),
    findall(I,adjudicator(I,_,_),Is0),sort(Is0,Is),length(Is,AdjCount),
    findall(A,adjudicator(_,A,_),As0),sort(As0,As),length(As,AncCount),
    (self_certified->SelfB=true;SelfB=false),yes(SelfB,Self),
    (common_ancestry->CommonB=true;CommonB=false),yes(CommonB,Common),
    (capture_risk->CaptureB=true;CaptureB=false),yes(CaptureB,Capture),
    findall(S,standard(S,_,_),Ss0),sort(Ss0,Ss),length(Ss,StdCount),
    support_intersection(preworld_support,Pre),
    support_intersection(evidence_support,CAS),
    length(CAS,CASSize),(CASSize=:=1->SingletonB=true;SingletonB=false),yes(SingletonB,Singleton),
    force_singleton(FS),(FS='YES',SingletonB=false->ForcedB=true;ForcedB=false),yes(ForcedB,Forced),
    (support_disagreement->ConflictCount=1;ConflictCount=0),
    (direct_meta_conflict->DMB=true;DMB=false),yes(DMB,DM),
    (challenge(_,'WORLD_FACING',_),length(Pre,PN),length(CAS,CN),CN>0,CN<PN->WSB=true;WSB=false),yes(WSB,WS),
    (meta_cycle->CycleB=true;CycleB=false),yes(CycleB,Cycle),
    findall(N,unanchored_terminal(N),Ns0),sort(Ns0,Ns),length(Ns,MetaDebt),
    candidate_relation(Candidate),
    authority_state(CAS,SingletonB,ForcedB,CycleB,DMB,CaptureB,SelfB,CommonB,MetaDebt,Candidate,Authority),
    (SelfB=true->Independence='SELF_CERTIFIED';CommonB=true->Independence='COMMON_ANCESTRY';AncCount>=2->Independence='ANCESTRY_SEPARATED';Independence='UNRESOLVED'),
    atomic_list_concat(CAS,'+',CASAtom0),(CAS=[]->CASAtom='NONE';CASAtom=CASAtom0),
    format('authority.candidate_relation=~w~n',[Candidate]),
    format('authority.adjudicator_count=~w~n',[AdjCount]),
    format('authority.adjudicator_ancestry_count=~w~n',[AncCount]),
    format('authority.independence_state=~w~n',[Independence]),
    format('authority.self_certified=~w~n',[Self]),
    format('authority.common_ancestry=~w~n',[Common]),
    format('authority.standard_count=~w~n',[StdCount]),
    format('authority.capture_risk=~w~n',[Capture]),
    format('authority.correspondence_set=~w~n',[CASAtom]),
    format('authority.correspondence_set_size=~w~n',[CASSize]),
    format('authority.correspondence_singleton=~w~n',[Singleton]),
    format('authority.forced_singleton_overclaim=~w~n',[Forced]),
    format('authority.conflict_count=~w~n',[ConflictCount]),
    format('authority.direct_meta_conflict=~w~n',[DM]),
    format('authority.world_facing_separator_present=~w~n',[WS]),
    format('authority.meta_cycle=~w~n',[Cycle]),
    format('authority.meta_debt_count=~w~n',[MetaDebt]),
    format('authority.mapping_authority=~w~n',[Authority]),
    writeln('authority.unique_world_correspondence_inferred=NO'),
    writeln('authority.future_translation_closed=NO'),
    writeln('authority.consensus_truth_oracle=NO'),
    writeln('authority.standard_truth_oracle=NO'),
    writeln('authority.externality_truth_oracle=NO'),
    writeln('authority.meta_cycle_authority=NO'),
    writeln('authority.guidance_mode=CONTESTABLE_SET_VALUED_TRANSLATION_AUTHORITY'),
    check_expected(Authority,Singleton,Self,Capture,Cycle,WS).
