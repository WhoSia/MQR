:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic packet_id/1, claim_scope/1, source_ontology/1, target_ontology/1, content/1.
:- dynamic source_route/4, target_route/3, route_map/3, coverage_witness/3.
:- dynamic hidden_route/3, path_state/2.
:- dynamic expected_authority/1, expected_equivalence/1, expected_duplication/1.
:- dynamic expected_collapse/1, expected_hidden_novel/1, expected_entanglement/1, expected_path_conflict/1.
:- dynamic seen_header/0, seen_end/0.

reset_db :-
  retractall(packet_id(_)),retractall(claim_scope(_)),retractall(source_ontology(_)),retractall(target_ontology(_)),
  retractall(content(_)),retractall(source_route(_,_,_,_)),retractall(target_route(_,_,_)),
  retractall(route_map(_,_,_)),retractall(coverage_witness(_,_,_)),retractall(hidden_route(_,_,_)),
  retractall(path_state(_,_)),retractall(expected_authority(_)),retractall(expected_equivalence(_)),
  retractall(expected_duplication(_)),retractall(expected_collapse(_)),retractall(expected_hidden_novel(_)),
  retractall(expected_entanglement(_)),retractall(expected_path_conflict(_)),
  retractall(seen_header),retractall(seen_end).

atomize(S,A):-atom_string(A,S).
plus_atoms(S,R):-split_string(S,"+","",Ps),Ps\=[],maplist(atomize,Ps,A0),sort(A0,R).

parse_line(Line):-
  normalize_space(string(N),Line),
  (N=""->true
  ;sub_string(N,0,1,_,"#")->true
  ;seen_end->true
  ;split_string(N," \t"," \t",T),
    (T=["REALROUTE","0.15"]->parse_tokens(T)
    ;seen_header->parse_tokens(T)
    ;format(user_error,'PROLOG_HEADER_REQUIRED ~s~n',[Line]),fail)).

parse_tokens(["REALROUTE","0.15"]):- \+seen_header,assertz(seen_header).
parse_tokens(["id",S]):-atomize(S,A),assertz(packet_id(A)).
parse_tokens(["claim_scope",S]):-atomize(S,A),assertz(claim_scope(A)).
parse_tokens(["source_ontology",S]):-atomize(S,A),assertz(source_ontology(A)).
parse_tokens(["target_ontology",S]):-atomize(S,A),assertz(target_ontology(A)).
parse_tokens(["content",S]):-atomize(S,A),\+content(A),assertz(content(A)).
parse_tokens(["source_route",I,A,C,S]):-
  atomize(I,AI),atomize(A,AA),plus_atoms(C,Cs),atomize(S,S0),upcase_atom(S0,AS),
  member(AS,['COVERED','UNCOVERED']),\+source_route(AI,_,_,_),assertz(source_route(AI,AA,Cs,AS)).
parse_tokens(["target_route",I,A,C]):-
  atomize(I,AI),atomize(A,AA),plus_atoms(C,Cs),\+target_route(AI,_,_),assertz(target_route(AI,AA,Cs)).
parse_tokens(["map",S,K,T]):-
  plus_atoms(S,Ss),atomize(K,K0),upcase_atom(K0,AK),
  member(AK,['EXACT','REFINE','MERGE','OVERLAP','DISJOINT','UNMAPPED']),
  plus_atoms(T,Ts),assertz(route_map(Ss,AK,Ts)).
parse_tokens(["coverage_witness",S,T,C]):-
  atomize(S,AS),atomize(T,AT),plus_atoms(C,Cs),assertz(coverage_witness(AS,AT,Cs)).
parse_tokens(["hidden_route",I,K,C]):-
  atomize(I,AI),atomize(K,K0),upcase_atom(K0,AK),
  member(AK,['NOVEL_ROUTE','REFINEMENT_OF_EXISTING','MERGE_CORRECTION','PREVIOUSLY_UNMAPPED_CONTENT','ANCESTRY_REVELATION','UNRESOLVED']),
  plus_atoms(C,Cs),assertz(hidden_route(AI,AK,Cs)).
parse_tokens(["path",I,S]):-
  atomize(I,AI),atomize(S,S0),upcase_atom(S0,AS),member(AS,['PASS','HOLD','REOPEN']),assertz(path_state(AI,AS)).
parse_tokens(["authorize_coverage_authority",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_authority(A)).
parse_tokens(["authorize_coverage_equivalence",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_equivalence(A)).
parse_tokens(["authorize_duplication",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_duplication(A)).
parse_tokens(["authorize_collapse",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_collapse(A)).
parse_tokens(["authorize_hidden_novel",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_hidden_novel(A)).
parse_tokens(["authorize_ancestry_entanglement",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_entanglement(A)).
parse_tokens(["authorize_path_conflict",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_path_conflict(A)).
parse_tokens(["END"]):-assertz(seen_end).

all_declared_contents(Cs):-findall(C,content(C),C0),sort(C0,Cs).
valid_route_contents:-all_declared_contents(All),forall(source_route(_,_,Cs,_),ord_subset(Cs,All)),forall(target_route(_,_,Cs),ord_subset(Cs,All)).
valid_map_refs:-forall(route_map(Ss,_,Ts),(forall(member(S,Ss),source_route(S,_,_,_)),forall(member(T,Ts),target_route(T,_,_)))).
valid_witness_refs:-forall(coverage_witness(S,T,Cs),(source_route(S,_,SC,_),target_route(T,_,TC),ord_subset(Cs,SC),ord_subset(Cs,TC))).
valid_hidden_contents:-all_declared_contents(All),forall(hidden_route(_,_,Cs),ord_subset(Cs,All)).

load_packet(File):-
  reset_db,read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls),maplist(parse_line,Ls),
  seen_header,seen_end,packet_id(_),claim_scope(_),source_ontology(_),target_ontology(_),content(_),
  source_route(_,_,_,_),target_route(_,_,_),
  valid_route_contents,valid_map_refs,valid_witness_refs,valid_hidden_contents.

ord_union_all([],[]).
ord_union_all([H|T],R):-foldl(ord_union,T,H,R).

source_total(Cs):-findall(X,source_route(_,_,X,_),Xs),ord_union_all(Xs,Cs).
target_total(Cs):-findall(X,target_route(_,_,X),Xs),ord_union_all(Xs,Cs).
source_covered(Cs):-findall(X,source_route(_,_,X,'COVERED'),Xs),ord_union_all(Xs,Cs).
witnessed(Cs):-findall(X,coverage_witness(_,_,X),Xs),ord_union_all(Xs,Cs).

source_ancestry_count(N):-findall(A,source_route(_,A,_,_),As0),sort(As0,As),length(As,N).
target_ancestry_count(N):-findall(A,target_route(_,A,_),As0),sort(As0,As),length(As,N).
ancestry_entanglement:-
  findall(R,source_route(R,_,_,_),SR0),sort(SR0,SR),length(SR,SN),source_ancestry_count(SA),SN>1,SN>SA,!.
ancestry_entanglement:-
  findall(R,target_route(R,_,_),TR0),sort(TR0,TR),length(TR,TN),target_ancestry_count(TA),TN>1,TN>TA,!.

duplicate_target_content:-
  target_route(A,_,Cs),target_route(B,_,Cs),A@<B,!.

split_count(N):-findall(1,(route_map(Ss,'REFINE',Ts),length(Ss,1),length(Ts,TN),TN>1),Xs),length(Xs,N).
merge_count(N):-findall(1,(route_map(Ss,'MERGE',Ts),length(Ss,SN),SN>1,length(Ts,1)),Xs),length(Xs,N).

route_contents_source_ids([],[]).
route_contents_source_ids([S|Ss],R):-source_route(S,_,C,_),route_contents_source_ids(Ss,R0),ord_union(C,R0,R).
route_contents_target_ids([],[]).
route_contents_target_ids([T|Ts],R):-target_route(T,_,C),route_contents_target_ids(Ts,R0),ord_union(C,R0,R).
covered_source_contents_ids([],[]).
covered_source_contents_ids([S|Ss],R):-
  source_route(S,_,C,State),covered_source_contents_ids(Ss,R0),
  (State='COVERED'->ord_union(C,R0,R);R=R0).

map_witness_contents(Ss,Ts,R):-
  findall(Cs,(coverage_witness(S,T,Cs),member(S,Ss),member(T,Ts)),Xs),
  ord_union_all(Xs,R).

coverage_collapse:-
  route_map(Ss,'MERGE',Ts),
  route_contents_source_ids(Ss,SC),route_contents_target_ids(Ts,TC),
  \+ord_subset(SC,TC),!.
coverage_collapse:-
  route_map(Ss,'MERGE',Ts),
  covered_source_contents_ids(Ss,SC),map_witness_contents(Ss,Ts,W),
  \+ord_subset(SC,W),!.

existing_surface(E):-source_total(S),target_total(T),ord_union(S,T,E).
hidden_novel:-
  hidden_route(_,K,Cs),member(K,['NOVEL_ROUTE','PREVIOUSLY_UNMAPPED_CONTENT']),!.
hidden_novel:-
  existing_surface(E),hidden_route(_,_,Cs),\+ord_subset(Cs,E),!.

hidden_revision:-hidden_route(_,_,_),!.

path_conflict:-
  findall(S,path_state(_,S),Ss0),sort(Ss0,Ss),length(Ss,N),N>1.

yes(true,'YES'):-!.
yes(_,'NO').

authority_state(HN,PC,HR,Collapse,SourceComplete,TransportComplete,SurfaceEq,TargetComplete,Entangled,Eq,Authority):-
  (HN=true->Authority='REOPEN_HIDDEN_NOVEL_CONTENT'
  ;PC=true->Authority='REOPEN_REVISION_PATH_CONFLICT'
  ;HR=true->Authority='REOPEN_HIDDEN_ROUTE_REVISION'
  ;Collapse=true->Authority='HOLD_COVERAGE_COLLAPSE'
  ;SourceComplete=false->Authority='HOLD_SOURCE_COVERAGE_INCOMPLETE'
  ;TransportComplete=false->Authority='HOLD_COVERAGE_TRANSPORT'
  ;SurfaceEq=false->Authority='HOLD_CONTENT_SURFACE_CHANGE'
  ;TargetComplete=false->Authority='HOLD_TARGET_COVERAGE_INCOMPLETE'
  ;Entangled=true->Authority='HOLD_ROUTE_ANCESTRY_ENTANGLEMENT'
  ;Eq=true->Authority='AUTHORIZED_CONTENT_PRESERVING_TRANSPORT'
  ;Authority='HOLD_COVERAGE_INEQUIVALENT').

check_expected(A,Eq,Dup,Col,HN,Ent,PC):-
  (expected_authority(X)->X=A;true),
  (expected_equivalence(X)->X=Eq;true),
  (expected_duplication(X)->X=Dup;true),
  (expected_collapse(X)->X=Col;true),
  (expected_hidden_novel(X)->X=HN;true),
  (expected_entanglement(X)->X=Ent;true),
  (expected_path_conflict(X)->X=PC;true).

run(File):-
  load_packet(File),
  findall(R,source_route(R,_,_,_),SR0),sort(SR0,SR),length(SR,SRN),
  findall(R,target_route(R,_,_),TR0),sort(TR0,TR),length(TR,TRN),
  source_total(ST),target_total(TT),source_covered(SC),witnessed(W),
  length(ST,SCN),length(TT,TCN),length(SC,SCCN),length(W,TWCN),
  source_ancestry_count(SAN),target_ancestry_count(TAN),
  split_count(SplitN),merge_count(MergeN),
  (SC=ST->SourceCompleteB=true;SourceCompleteB=false),yes(SourceCompleteB,SourceComplete),
  (ord_subset(TT,W)->TargetCompleteB=true;TargetCompleteB=false),yes(TargetCompleteB,TargetComplete),
  (ord_subset(SC,W)->TransportCompleteB=true;TransportCompleteB=false),yes(TransportCompleteB,TransportComplete),
  (ST=TT->SurfaceEqB=true;SurfaceEqB=false),yes(SurfaceEqB,SurfaceEq),
  (duplicate_target_content->DupB=true;DupB=false),yes(DupB,Dup),
  (coverage_collapse->CollapseB=true;CollapseB=false),yes(CollapseB,Collapse),
  (SourceCompleteB=true,TargetCompleteB=true,TransportCompleteB=true,SurfaceEqB=true,CollapseB=false->EqB=true;EqB=false),yes(EqB,Eq),
  findall(H,hidden_route(H,_,_),Hs0),sort(Hs0,Hs),length(Hs,HNCount),
  (hidden_novel->HNB=true;HNB=false),yes(HNB,HN),
  (ancestry_entanglement->EntB=true;EntB=false),yes(EntB,Ent),
  (path_conflict->PCB=true;PCB=false),yes(PCB,PC),
  (hidden_revision->HRB=true;HRB=false),
  ((HRB=true;PCB=true)->ReopenB=true;ReopenB=false),yes(ReopenB,Reopen),
  authority_state(HNB,PCB,HRB,CollapseB,SourceCompleteB,TransportCompleteB,SurfaceEqB,TargetCompleteB,EntB,EqB,Authority),
  format('route.source_route_count=~w~n',[SRN]),
  format('route.target_route_count=~w~n',[TRN]),
  format('route.source_content_count=~w~n',[SCN]),
  format('route.target_content_count=~w~n',[TCN]),
  format('route.source_covered_content_count=~w~n',[SCCN]),
  format('route.target_witnessed_content_count=~w~n',[TWCN]),
  format('route.source_ancestry_count=~w~n',[SAN]),
  format('route.target_ancestry_count=~w~n',[TAN]),
  format('route.split_count=~w~n',[SplitN]),
  format('route.merge_count=~w~n',[MergeN]),
  format('route.source_coverage_complete=~w~n',[SourceComplete]),
  format('route.target_coverage_complete=~w~n',[TargetComplete]),
  format('route.coverage_transport_complete=~w~n',[TransportComplete]),
  format('route.content_surface_equivalent=~w~n',[SurfaceEq]),
  format('route.coverage_duplication_detected=~w~n',[Dup]),
  format('route.coverage_collapse_detected=~w~n',[Collapse]),
  format('route.coverage_equivalence=~w~n',[Eq]),
  format('route.hidden_route_count=~w~n',[HNCount]),
  format('route.hidden_novel_content=~w~n',[HN]),
  format('route.ancestry_entanglement=~w~n',[Ent]),
  format('route.path_conflict=~w~n',[PC]),
  format('route.reopen_required=~w~n',[Reopen]),
  format('route.coverage_authority=~w~n',[Authority]),
  writeln('route.current_route_ontology_complete=NO'),
  writeln('route.future_defeat_space_closed=NO'),
  writeln('route.route_count_truth_oracle=NO'),
  writeln('route.route_label_identity_oracle=NO'),
  writeln('route.coverage_fraction_truth_oracle=NO'),
  writeln('route.revision_path_truth_oracle=NO'),
  writeln('route.guidance_mode=VERSIONED_DEFEAT_CONTENT_COVERAGE'),
  check_expected(Authority,Eq,Dup,Collapse,HN,Ent,PC).
