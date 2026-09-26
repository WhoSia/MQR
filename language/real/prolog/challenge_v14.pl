:- use_module(library(readutil)).
:- use_module(library(ordsets)).

:- dynamic packet_id/1, claim_scope/1, candidate_relations/1.
:- dynamic selector/2, selection_timing/1, selection_rule/3.
:- dynamic route/1, probe/5, covers/2, score_source/2, relevance_source/2, expansion/2.
:- dynamic expected_authority/1, expected_narrowed/1, expected_coverage/1.
:- dynamic expected_common/1, expected_capture/1, expected_expansion_reopen/1.
:- dynamic seen_header/0, seen_end/0.

relations(['DISJOINT','EXACT','MERGE','OVERLAP','REFINE','UNMAPPED']).

reset_db :-
  retractall(packet_id(_)),retractall(claim_scope(_)),retractall(candidate_relations(_)),
  retractall(selector(_,_)),retractall(selection_timing(_)),retractall(selection_rule(_,_,_)),
  retractall(route(_)),retractall(probe(_,_,_,_,_)),retractall(covers(_,_)),
  retractall(score_source(_,_)),retractall(relevance_source(_,_)),retractall(expansion(_,_)),
  retractall(expected_authority(_)),retractall(expected_narrowed(_)),retractall(expected_coverage(_)),
  retractall(expected_common(_)),retractall(expected_capture(_)),retractall(expected_expansion_reopen(_)),
  retractall(seen_header),retractall(seen_end).

atomize(S,A):-atom_string(A,S).
plus_relations(S,R):-split_string(S,"+","",Ps),Ps\=[],maplist(atomize,Ps,A0),maplist(upcase_atom,A0,A1),sort(A1,R),relations(All),ord_subset(R,All).

parse_line(Line):-
  normalize_space(string(N),Line),
  (N=""->true
  ;sub_string(N,0,1,_,"#")->true
  ;seen_end->true
  ;split_string(N," \t"," \t",T),
    (T=["REALCHALLENGE","0.14"]->parse_tokens(T)
    ;seen_header->parse_tokens(T)
    ;format(user_error,'PROLOG_HEADER_REQUIRED ~s~n',[Line]),fail)).

parse_tokens(["REALCHALLENGE","0.14"]):- \+seen_header,assertz(seen_header).
parse_tokens(["id",S]):-atomize(S,A),assertz(packet_id(A)).
parse_tokens(["claim_scope",S]):-atomize(S,A),assertz(claim_scope(A)).
parse_tokens(["candidate_relations",S]):-plus_relations(S,R),assertz(candidate_relations(R)).
parse_tokens(["selector",I,A]):-atomize(I,AI),atomize(A,AA),assertz(selector(AI,AA)).
parse_tokens(["selection_timing",S]):-atomize(S,A0),upcase_atom(A0,A),member(A,['PRESEALED','POST_OUTCOME']),assertz(selection_timing(A)).
parse_tokens(["selection_rule",I,A,M]):-atomize(I,AI),atomize(A,AA),atomize(M,M0),upcase_atom(M0,AM),member(AM,['INDEPENDENT','INCUMBENT_DEFINED','UNRESOLVED']),assertz(selection_rule(AI,AA,AM)).
parse_tokens(["route",I]):-atomize(I,A),\+route(A),assertz(route(A)).
parse_tokens(["probe",I,A,S,M,R]):-atomize(I,AI),atomize(A,AA),atomize(S,S0),upcase_atom(S0,AS),member(AS,['SELECTED','UNSELECTED']),atomize(M,M0),upcase_atom(M0,AM),member(AM,['WORLD_FACING','INTERNAL']),plus_relations(R,Rs),\+probe(AI,_,_,_,_),assertz(probe(AI,AA,AS,AM,Rs)).
parse_tokens(["covers",P,R]):-atomize(P,AP),atomize(R,AR),assertz(covers(AP,AR)).
parse_tokens(["score_source",P,S]):-atomize(P,AP),atomize(S,S0),upcase_atom(S0,AS),member(AS,['INDEPENDENT','CANDIDATE_DERIVED','STANDARD_DERIVED']),assertz(score_source(AP,AS)).
parse_tokens(["relevance_source",P,S]):-atomize(P,AP),atomize(S,S0),upcase_atom(S0,AS),member(AS,['INDEPENDENT','CANDIDATE_DERIVED','STANDARD_DERIVED']),assertz(relevance_source(AP,AS)).
parse_tokens(["expansion",I,R]):-atomize(I,AI),plus_relations(R,Rs),assertz(expansion(AI,Rs)).
parse_tokens(["authorize_selection_authority",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_authority(A)).
parse_tokens(["authorize_narrowed",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_narrowed(A)).
parse_tokens(["authorize_declared_route_coverage_complete",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_coverage(A)).
parse_tokens(["authorize_common_ancestry",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_common(A)).
parse_tokens(["authorize_discriminator_capture",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_capture(A)).
parse_tokens(["authorize_expansion_reopen",S]):-atomize(S,A0),upcase_atom(A0,A),assertz(expected_expansion_reopen(A)).
parse_tokens(["END"]):-assertz(seen_end).

load_packet(File):-
  reset_db,read_file_to_string(File,S,[]),split_string(S,"\n","\r",Ls),maplist(parse_line,Ls),
  seen_header,seen_end,packet_id(_),claim_scope(_),candidate_relations(_),selector(_,_),
  selection_timing(_),selection_rule(_,_,_),route(_),probe(_,_,_,_,_),
  \+(covers(P,_),\+probe(P,_,_,_,_)),
  \+(covers(_,R),\+route(R)),
  \+(probe(P,_,_,_,_),\+score_source(P,_)),
  \+(probe(P,_,_,_,_),\+relevance_source(P,_)).

selected_world(P,A,R):-probe(P,A,'SELECTED','WORLD_FACING',R).
selected_any(P):-probe(P,_,'SELECTED',_,_).

intersect_all([H|T],R):-foldl(ord_intersection,T,H,R).
after_set(A):-
  candidate_relations(B),
  findall(S,selected_world(_,_,S),Ss),
  (Ss=[]->A=B;intersect_all([B|Ss],A)).

covered_selected_route(R):-covers(P,R),selected_world(P,_,_).

common_ancestry:-
  findall(P,selected_world(P,_,_),Ps0),sort(Ps0,Ps),length(Ps,N),
  findall(A,selected_world(_,A,_),As0),sort(As0,As),length(As,M),
  N>1,N>M.

incumbent_relevance:-selection_rule(_,_, 'INCUMBENT_DEFINED'),!.
incumbent_relevance:-selected_world(P,_,_),relevance_source(P,'CANDIDATE_DERIVED'),!.

candidate_score:-selected_world(P,_,_),score_source(P,'CANDIDATE_DERIVED'),!.
discriminator_capture:-incumbent_relevance,!.
discriminator_capture:-candidate_score,!.

omitted_counterprobe:-
  after_set(A),A\=[],
  probe(P,_, 'UNSELECTED','WORLD_FACING',S),
  candidate_relations(B),ord_intersection(B,S,X),X\=[],
  ord_intersection(A,S,[]),!.

expansion_result(S,X):-after_set(A),expansion(_,S),ord_intersection(A,S,X).
expansion_instability:-after_set(A),expansion_result(_,X),X\=A,!.
expansion_reopen:-after_set(A),A\=[],expansion_result(_,[]),!.
expansion_narrow:-after_set(A),expansion_result(_,X),X\=[],length(X,NX),length(A,NA),NX<NA,!.

yes(true,'YES'):-!.
yes(_,'NO').

authority_state(Post,Capture,Omitted,WorldN,Coverage,Common,ExpansionReopen,After,Narrow,Authority):-
  (Post=true->Authority='HOLD_POST_OUTCOME_SELECTION'
  ;Capture=true->Authority='HOLD_DISCRIMINATOR_CAPTURE'
  ;Omitted=true->Authority='REOPEN_OMITTED_COUNTERPROBE'
  ;WorldN=:=0->Authority='HOLD_NO_WORLD_FACING'
  ;Coverage=false->Authority='HOLD_ROUTE_COVERAGE'
  ;Common=true->Authority='HOLD_COMMON_ANCESTRY'
  ;ExpansionReopen=true->Authority='REOPEN_EXPANSION_CONFLICT'
  ;After=[]->Authority='REOPEN_SELECTED_CONFLICT'
  ;Narrow=true->Authority='AUTHORIZED_PROVISIONAL_NARROWING'
  ;Authority='ADMISSIBLE_NO_NARROWING').

check_expected(A,N,C,Com,Cap,ER):-
  (expected_authority(X)->X=A;true),
  (expected_narrowed(X)->X=N;true),
  (expected_coverage(X)->X=C;true),
  (expected_common(X)->X=Com;true),
  (expected_capture(X)->X=Cap;true),
  (expected_expansion_reopen(X)->X=ER;true).

run(File):-
  load_packet(File),
  findall(P,probe(P,_,_,_,_),Reg0),sort(Reg0,Reg),length(Reg,RegN),
  findall(P,selected_any(P),Sel0),sort(Sel0,Sel),length(Sel,SelN),
  findall(P,selected_world(P,_,_),W0),sort(W0,W),length(W,WorldN),
  findall(A,selected_world(_,A,_),As0),sort(As0,As),length(As,AncN),
  findall(R,route(R),Rs0),sort(Rs0,Rs),length(Rs,RouteN),
  findall(R,covered_selected_route(R),CR0),sort(CR0,CR),length(CR,CoverN),
  UncoverN is RouteN-CoverN,(UncoverN=:=0->CoverageB=true;CoverageB=false),yes(CoverageB,Coverage),
  (WorldN>1,WorldN>CoverN->MultB=true;MultB=false),yes(MultB,Mult),
  (common_ancestry->CommonB=true;CommonB=false),yes(CommonB,Common),
  (selection_timing('POST_OUTCOME')->PostB=true;PostB=false),yes(PostB,Post),
  (incumbent_relevance->IncB=true;IncB=false),yes(IncB,Inc),
  (discriminator_capture->CapB=true;CapB=false),yes(CapB,Capture),
  (omitted_counterprobe->OmitB=true;OmitB=false),yes(OmitB,Omitted),
  candidate_relations(Before),after_set(After),
  length(Before,NB),length(After,NA),(After\=[],NA<NB->NarrowB=true;NarrowB=false),yes(NarrowB,Narrow),
  findall(I,expansion(I,_),Es0),sort(Es0,Es),length(Es,ExpN),
  (expansion_instability->EIB=true;EIB=false),yes(EIB,EI),
  (expansion_reopen->ERB=true;ERB=false),yes(ERB,ER),
  (expansion_narrow->ENB=true;ENB=false),
  (ExpN=:=0->EState='NONE';ERB=true->EState='REOPENED';ENB=true->EState='NARROWED';EIB=true->EState='CHANGED';EState='STABLE'),
  authority_state(PostB,CapB,OmitB,WorldN,CoverageB,CommonB,ERB,After,NarrowB,Authority),
  atomic_list_concat(Before,'+',BeforeA),
  (After=[]->AfterA='NONE';atomic_list_concat(After,'+',AfterA)),
  format('challenge.registered_probe_count=~w~n',[RegN]),
  format('challenge.selected_probe_count=~w~n',[SelN]),
  format('challenge.selected_world_probe_count=~w~n',[WorldN]),
  format('challenge.selected_ancestry_count=~w~n',[AncN]),
  format('challenge.route_count=~w~n',[RouteN]),
  format('challenge.covered_route_count=~w~n',[CoverN]),
  format('challenge.uncovered_route_count=~w~n',[UncoverN]),
  format('challenge.declared_route_coverage_complete=~w~n',[Coverage]),
  format('challenge.probe_route_multiplicity=~w~n',[Mult]),
  format('challenge.common_ancestry=~w~n',[Common]),
  format('challenge.post_outcome_selection=~w~n',[Post]),
  format('challenge.incumbent_relevance=~w~n',[Inc]),
  format('challenge.discriminator_capture=~w~n',[Capture]),
  format('challenge.omitted_counterprobe=~w~n',[Omitted]),
  format('challenge.correspondence_before=~w~n',[BeforeA]),
  format('challenge.correspondence_after=~w~n',[AfterA]),
  format('challenge.narrowed=~w~n',[Narrow]),
  format('challenge.expansion_count=~w~n',[ExpN]),
  format('challenge.expansion_instability=~w~n',[EI]),
  format('challenge.expansion_reopen_required=~w~n',[ER]),
  format('challenge.expansion_state=~w~n',[EState]),
  writeln('challenge.current_family_complete=NO'),
  writeln('challenge.future_challenge_space_closed=NO'),
  writeln('challenge.probe_count_truth_oracle=NO'),
  writeln('challenge.externality_truth_oracle=NO'),
  writeln('challenge.cost_truth_oracle=NO'),
  writeln('challenge.selection_rule_truth_oracle=NO'),
  format('challenge.selection_authority=~w~n',[Authority]),
  writeln('challenge.guidance_mode=CONSTITUTED_REOPENABLE_SEPARATOR_AUTHORITY'),
  check_expected(Authority,Narrow,Coverage,Common,Capture,ER).
