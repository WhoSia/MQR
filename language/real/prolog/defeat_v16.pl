:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic packet_id/1, claim_scope/1, source_representation/1, target_representation/1, challenge/1.
:- dynamic source_content/5, target_content/5, content_map/3, role_witness/3.
:- dynamic hidden_content/3, expansion/4, path_state/2.
:- dynamic expected_authority/1, expected_local_equivalence/1, expected_split_duplication/1.
:- dynamic expected_manifestation_multiplication/1, expected_mechanism_aliasing/1, expected_common_cause/1.
:- dynamic expected_expansion_break/1, expected_hidden_novel/1, expected_path_conflict/1.
:- dynamic seen_header/0, seen_end/0.

reset_db :-
  retractall(packet_id(_)),retractall(claim_scope(_)),retractall(source_representation(_)),retractall(target_representation(_)),
  retractall(challenge(_)),retractall(source_content(_,_,_,_,_)),retractall(target_content(_,_,_,_,_)),
  retractall(content_map(_,_,_)),retractall(role_witness(_,_,_)),retractall(hidden_content(_,_,_)),
  retractall(expansion(_,_,_,_)),retractall(path_state(_,_)),
  retractall(expected_authority(_)),retractall(expected_local_equivalence(_)),retractall(expected_split_duplication(_)),
  retractall(expected_manifestation_multiplication(_)),retractall(expected_mechanism_aliasing(_)),retractall(expected_common_cause(_)),
  retractall(expected_expansion_break(_)),retractall(expected_hidden_novel(_)),retractall(expected_path_conflict(_)),
  retractall(seen_header),retractall(seen_end).

atomize(S,A):-atom_string(A,S).
plus_atoms(S,R):-split_string(S,"+","",Ps),Ps\=[],maplist(atomize,Ps,A0),sort(A0,R).

parse_line(Line):-
  normalize_space(string(N),Line),
  (N=""->true
  ;sub_string(N,0,1,_,"#")->true
  ;seen_end->true
  ;split_string(N," \t"," \t",T),
    (T=["REALDEFEAT","0.16"]->parse_tokens(T)
    ;seen_header->parse_tokens(T)
    ;format(user_error,'PROLOG_HEADER_REQUIRED ~s~n',[Line]),fail)).

parse_tokens(["REALDEFEAT","0.16"]):- \+seen_header,assertz(seen_header).
parse_tokens(["id",S]):-atomize(S,A),assertz(packet_id(A)).
parse_tokens(["claim_scope",S]):-atomize(S,A),assertz(claim_scope(A)).
parse_tokens(["source_representation",S]):-atomize(S,A),assertz(source_representation(A)).
parse_tokens(["target_representation",S]):-atomize(S,A),assertz(target_representation(A)).
parse_tokens(["challenge",S]):-atomize(S,A),\+challenge(A),assertz(challenge(A)).
parse_tokens(["source_content",I,M,V,A,Q]):-
  atomize(I,AI),atomize(M,AM),atomize(V,AV),atomize(A,AA),plus_atoms(Q,Qs),
  \+source_content(AI,_,_,_,_),assertz(source_content(AI,AM,AV,AA,Qs)).
parse_tokens(["target_content",I,M,V,A,Q]):-
  atomize(I,AI),atomize(M,AM),atomize(V,AV),atomize(A,AA),plus_atoms(Q,Qs),
  \+target_content(AI,_,_,_,_),assertz(target_content(AI,AM,AV,AA,Qs)).
parse_tokens(["map",S,K,T]):-
  plus_atoms(S,Ss),atomize(K,K0),upcase_atom(K0,AK),
  member(AK,['EXACT','REFINE','MERGE','OVERLAP','DISJOINT','UNMAPPED']),
  plus_atoms(T,Ts),assertz(content_map(Ss,AK,Ts)).
parse_tokens(["role_witness",S,T,Q]):-
  atomize(S,AS),atomize(T,AT),plus_atoms(Q,Qs),assertz(role_witness(AS,AT,Qs)).
parse_tokens(["hidden_content",I,K,Q]):-
  atomize(I,AI),atomize(K,K0),upcase_atom(K0,AK),
  member(AK,['NOVEL_COUNTERFACTUAL_DISTINCTION','REFINEMENT_OF_EXISTING','MECHANISM_REASSIGNMENT','MANIFESTATION_REASSIGNMENT','COMMON_CAUSE_REVEAL','REPRESENTATION_ESCAPE','PREVIOUSLY_UNMAPPED','UNRESOLVED']),
  plus_atoms(Q,Qs),assertz(hidden_content(AI,AK,Qs)).
parse_tokens(["expansion",I,S,T,R]):-
  atomize(I,AI),atomize(S,AS),atomize(T,AT),atomize(R,R0),upcase_atom(R0,AR),
  member(AR,['SAME','DISTINGUISHES']),assertz(expansion(AI,AS,AT,AR)).
parse_tokens(["path",I,S]):-
  atomize(I,AI),atomize(S,S0),upcase_atom(S0,AS),member(AS,['PASS','HOLD','REOPEN']),assertz(path_state(AI,AS)).
parse_tokens(["authorize_identity_authority",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_authority(A)).
parse_tokens(["authorize_local_equivalence",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_local_equivalence(A)).
parse_tokens(["authorize_split_duplication",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_split_duplication(A)).
parse_tokens(["authorize_manifestation_multiplication",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_manifestation_multiplication(A)).
parse_tokens(["authorize_mechanism_aliasing",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_mechanism_aliasing(A)).
parse_tokens(["authorize_common_cause",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_common_cause(A)).
parse_tokens(["authorize_expansion_break",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_expansion_break(A)).
parse_tokens(["authorize_hidden_novel",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_hidden_novel(A)).
parse_tokens(["authorize_path_conflict",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_path_conflict(A)).
parse_tokens(["END"]):-assertz(seen_end).

all_challenges(Qs):-findall(Q,challenge(Q),Q0),sort(Q0,Qs).
valid_profiles:-all_challenges(All),forall(source_content(_,_,_,_,Qs),ord_subset(Qs,All)),forall(target_content(_,_,_,_,Qs),ord_subset(Qs,All)).
valid_map_refs:-forall(content_map(Ss,_,Ts),(forall(member(S,Ss),source_content(S,_,_,_,_)),forall(member(T,Ts),target_content(T,_,_,_,_)))).
valid_witness_refs:-forall(role_witness(S,T,Qs),(source_content(S,_,_,_,SQ),target_content(T,_,_,_,TQ),ord_subset(Qs,SQ),ord_subset(Qs,TQ))).
valid_hidden_profiles:-all_challenges(All),forall(hidden_content(_,_,Qs),ord_subset(Qs,All)).
valid_expansion_refs:-forall(expansion(_,S,T,_),(source_content(S,_,_,_,_),target_content(T,_,_,_,_))).

load_packet(File):-
  reset_db,read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls),maplist(parse_line,Ls),
  seen_header,seen_end,packet_id(_),claim_scope(_),source_representation(_),target_representation(_),challenge(_),
  source_content(_,_,_,_,_),target_content(_,_,_,_,_),
  valid_profiles,valid_map_refs,valid_witness_refs,valid_hidden_profiles,valid_expansion_refs.

ord_union_all([],[]).
ord_union_all([H|T],R):-foldl(ord_union,T,H,R).

distinct_count(List,N):-sort(List,S),length(S,N).
source_count(N):-findall(I,source_content(I,_,_,_,_),Xs),distinct_count(Xs,N).
target_count(N):-findall(I,target_content(I,_,_,_,_),Xs),distinct_count(Xs,N).
source_mechanism_count(N):-findall(M,source_content(_,M,_,_,_),Xs),distinct_count(Xs,N).
target_mechanism_count(N):-findall(M,target_content(_,M,_,_,_),Xs),distinct_count(Xs,N).
source_manifestation_count(N):-findall(V,source_content(_,_,V,_,_),Xs),distinct_count(Xs,N).
target_manifestation_count(N):-findall(V,target_content(_,_,V,_,_),Xs),distinct_count(Xs,N).
source_ancestry_count(N):-findall(A,source_content(_,_,_,A,_),Xs),distinct_count(Xs,N).
target_ancestry_count(N):-findall(A,target_content(_,_,_,A,_),Xs),distinct_count(Xs,N).

profile_sig(Qs,S):-atomic_list_concat(Qs,'+',S).
source_profile_count(N):-findall(S,(source_content(_,_,_,_,Qs),profile_sig(Qs,S)),Xs),distinct_count(Xs,N).
target_profile_count(N):-findall(S,(target_content(_,_,_,_,Qs),profile_sig(Qs,S)),Xs),distinct_count(Xs,N).

split_count(N):-findall(1,(content_map(Ss,'REFINE',Ts),length(Ss,1),length(Ts,TN),TN>1),Xs),length(Xs,N).
merge_count(N):-findall(1,(content_map(Ss,'MERGE',Ts),length(Ss,SN),SN>1,length(Ts,1)),Xs),length(Xs,N).

manifestation_multiplication:-
  (source_content(_,M,V1,_,_),source_content(_,M,V2,_,_);target_content(_,M,V1,_,_),target_content(_,M,V2,_,_);source_content(_,M,V1,_,_),target_content(_,M,V2,_,_)),
  V1\=V2,!.
mechanism_aliasing:-
  (source_content(_,M1,V,_,_),source_content(_,M2,V,_,_);target_content(_,M1,V,_,_),target_content(_,M2,V,_,_);source_content(_,M1,V,_,_),target_content(_,M2,V,_,_)),
  M1\=M2,!.

common_cause_compression:-
  source_count(C),source_ancestry_count(A),C>1,C>A,!.
common_cause_compression:-
  target_count(C),target_ancestry_count(A),C>1,C>A,!.

mapped_targets(S,Ts):-
  findall(T,(content_map(Ss,_,MTs),member(S,Ss),member(T,MTs)),T0),sort(T0,Ts).

witnessed_for_source(S,Targets,W):-
  findall(Qs,(role_witness(S,T,Qs),member(T,Targets)),All),ord_union_all(All,W).

role_transport_complete:-
  forall(source_content(S,_,_,_,Profile),
    (mapped_targets(S,Ts),Ts\=[],witnessed_for_source(S,Ts,W),ord_subset(Profile,W))).

local_counterfactual_equivalence:-
  content_map([S],_,[T]),source_content(S,_,_,_,P),target_content(T,_,_,_,P),!.

source_union(U):-findall(P,source_content(_,_,_,_,P),Ps),ord_union_all(Ps,U).
target_union(U):-findall(P,target_content(_,_,_,_,P),Ps),ord_union_all(Ps,U).

hidden_novel:-hidden_content(_,K,_),member(K,['NOVEL_COUNTERFACTUAL_DISTINCTION','PREVIOUSLY_UNMAPPED']),!.
hidden_revision:-hidden_content(_,_,_),!.
expansion_break:-expansion(_,_,_,'DISTINGUISHES'),!.
path_conflict:-findall(S,path_state(_,S),Xs),sort(Xs,Ys),length(Ys,N),N>1.
role_drift:-content_map([S],'EXACT',[T]),source_content(S,_,_,_,SP),target_content(T,_,_,_,TP),SP\=TP,!.

yes(true,'YES'):-!.
yes(_,'NO').

authority(HN,EB,PC,HR,RoleDrift,SplitDup,MergeN,Transport,Collapse,Refine,MergeAuth,LocalEq,A):-
  (HN=true->A='REOPEN_HIDDEN_NOVEL_DISTINCTION'
  ;EB=true->A='REOPEN_EXPANSION_BREAK'
  ;PC=true->A='REOPEN_REVISION_PATH_CONFLICT'
  ;HR=true->A='REOPEN_HIDDEN_CONTENT_REVISION'
  ;RoleDrift=true->A='HOLD_ROLE_DRIFT'
  ;SplitDup=true->A='HOLD_SPLIT_WITHOUT_NEW_DISTINCTION'
  ;MergeN>0,Transport=false->A='HOLD_MERGE_DISTINCTION_LAUNDERING'
  ;Collapse=true->A='HOLD_REPRESENTATION_COLLAPSE'
  ;Transport=false->A='HOLD_ROLE_TRANSPORT'
  ;Refine=true->A='AUTHORIZED_COUNTERFACTUAL_REFINEMENT'
  ;MergeAuth=true->A='AUTHORIZED_SCOPE_QUOTIENT_MERGE'
  ;LocalEq=true->A='AUTHORIZED_LOCAL_COUNTERFACTUAL_QUOTIENT'
  ;A='AUTHORIZED_LOCAL_DEFEAT_ROLE_TRANSPORT').

check_expected(A,LE,SD,MM,MA,CC,EB,HN,PC):-
  (expected_authority(X)->X=A;true),
  (expected_local_equivalence(X)->X=LE;true),
  (expected_split_duplication(X)->X=SD;true),
  (expected_manifestation_multiplication(X)->X=MM;true),
  (expected_mechanism_aliasing(X)->X=MA;true),
  (expected_common_cause(X)->X=CC;true),
  (expected_expansion_break(X)->X=EB;true),
  (expected_hidden_novel(X)->X=HN;true),
  (expected_path_conflict(X)->X=PC;true).

run(File):-
  load_packet(File),
  source_count(SC),target_count(TC),
  source_mechanism_count(SMC),target_mechanism_count(TMC),
  source_manifestation_count(SVC),target_manifestation_count(TVC),
  source_ancestry_count(SAC),target_ancestry_count(TAC),
  source_profile_count(SPC),target_profile_count(TPC),
  split_count(SplitN),merge_count(MergeN),
  (manifestation_multiplication->MMB=true;MMB=false),yes(MMB,MM),
  (mechanism_aliasing->MAB=true;MAB=false),yes(MAB,MA),
  (common_cause_compression->CCB=true;CCB=false),yes(CCB,CC),
  (role_transport_complete->TB=true;TB=false),yes(TB,Transport),
  (local_counterfactual_equivalence->LEB=true;LEB=false),yes(LEB,LE),
  (role_drift->RDB=true;RDB=false),yes(RDB,RD),
  (SplitN>0,TC>SC,TPC=<SPC->SDB=true;SDB=false),yes(SDB,SD),
  source_union(SU),target_union(TU),(ord_subset(SU,TU)->CollapseB=false;CollapseB=true),yes(CollapseB,Collapse),
  (expansion_break->EBB=true;EBB=false),yes(EBB,EB),
  findall(H,hidden_content(H,_,_),Hs),sort(Hs,HU),length(HU,HC),
  (hidden_novel->HNB=true;HNB=false),yes(HNB,HN),
  (hidden_revision->HRB=true;HRB=false),
  (path_conflict->PCB=true;PCB=false),yes(PCB,PC),
  ((EBB=true;HRB=true;PCB=true)->ReopenB=true;ReopenB=false),yes(ReopenB,Reopen),
  (SplitN>0,TB=true,TPC>SPC->RefineB=true;RefineB=false),
  (MergeN>0,TB=true,CollapseB=false->MergeAuthB=true;MergeAuthB=false),
  authority(HNB,EBB,PCB,HRB,RDB,SDB,MergeN,TB,CollapseB,RefineB,MergeAuthB,LEB,Authority),
  format('defeat.source_content_count=~w~n',[SC]),
  format('defeat.target_content_count=~w~n',[TC]),
  format('defeat.source_mechanism_count=~w~n',[SMC]),
  format('defeat.target_mechanism_count=~w~n',[TMC]),
  format('defeat.source_manifestation_count=~w~n',[SVC]),
  format('defeat.target_manifestation_count=~w~n',[TVC]),
  format('defeat.source_ancestry_count=~w~n',[SAC]),
  format('defeat.target_ancestry_count=~w~n',[TAC]),
  format('defeat.counterfactual_profile_count_source=~w~n',[SPC]),
  format('defeat.counterfactual_profile_count_target=~w~n',[TPC]),
  format('defeat.split_count=~w~n',[SplitN]),
  format('defeat.merge_count=~w~n',[MergeN]),
  format('defeat.manifestation_multiplication=~w~n',[MM]),
  format('defeat.mechanism_aliasing=~w~n',[MA]),
  format('defeat.common_cause_compression=~w~n',[CC]),
  format('defeat.role_transport_complete=~w~n',[Transport]),
  format('defeat.local_counterfactual_equivalence=~w~n',[LE]),
  format('defeat.role_drift=~w~n',[RD]),
  format('defeat.split_without_new_distinction=~w~n',[SD]),
  format('defeat.representation_collapse=~w~n',[Collapse]),
  format('defeat.expansion_breaks_equivalence=~w~n',[EB]),
  format('defeat.hidden_content_count=~w~n',[HC]),
  format('defeat.hidden_novel_distinction=~w~n',[HN]),
  format('defeat.path_conflict=~w~n',[PC]),
  format('defeat.reopen_required=~w~n',[Reopen]),
  format('defeat.identity_authority=~w~n',[Authority]),
  writeln('defeat.current_defeat_atoms_complete=NO'),
  writeln('defeat.future_defeat_space_closed=NO'),
  writeln('defeat.label_identity_oracle=NO'),
  writeln('defeat.mechanism_identity_oracle=NO'),
  writeln('defeat.manifestation_identity_oracle=NO'),
  writeln('defeat.counterfactual_equivalence_truth_oracle=NO'),
  writeln('defeat.representation_truth_oracle=NO'),
  writeln('defeat.guidance_mode=REOPENABLE_COUNTERFACTUAL_DEFEAT_QUOTIENT'),
  check_expected(Authority,LE,SD,MM,MA,CC,EB,HN,PC).
