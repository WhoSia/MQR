:- dynamic seen_header/0,seen_end/0,rid/1,target/1,grammar/1,scope/1,
 probe_preservation/1,intervention_preservation/1,composition_status/1,
 defeat_preservation/1,embedding_status/1,morphism_integrity/1,
 preseal_provenance/1,reopening/1.

reset_all:-
 retractall(seen_header),retractall(seen_end),retractall(rid(_)),retractall(target(_)),
 retractall(grammar(_)),retractall(scope(_)),retractall(probe_preservation(_)),
 retractall(intervention_preservation(_)),retractall(composition_status(_)),
 retractall(defeat_preservation(_)),retractall(embedding_status(_)),
 retractall(morphism_integrity(_)),retractall(preseal_provenance(_)),retractall(reopening(_)).

run(File):-reset_all,setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),maplist(parse_line,Lines),validate,emit.

parse_line(Line):-normalize_space(string(N),Line),
 (N=""->true;sub_string(N,0,1,_,"#")->true;seen_end->fail;
  split_string(N," \t"," \t",T),
  (\+ seen_header->(T=["REALINVARIANCE","0.21"]->assertz(seen_header);fail);parse_tokens(T))).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["target",X]):- \+ target(_),member(X,["PROGRESS","MEASUREMENT","CAUSAL","REPRESENTATION","OTHER"]),assertz(target(X)),!.
parse_tokens(["grammar",X]):- \+ grammar(_),member(X,["GROUP","GROUPOID","PSEUDOGROUP","MONOID","PARTIAL_FAMILY"]),assertz(grammar(X)),!.
parse_tokens(["scope",X]):- \+ scope(_),member(X,["SUBSYSTEM","COMPOSITE","GLOBAL"]),assertz(scope(X)),!.
parse_tokens(["probe_preservation",X]):- \+ probe_preservation(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(probe_preservation(X)),!.
parse_tokens(["intervention_preservation",X]):- \+ intervention_preservation(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(intervention_preservation(X)),!.
parse_tokens(["composition_status",X]):- \+ composition_status(_),member(X,["PASS","FAIL","PARTIAL_VERIFIED","UNKNOWN"]),assertz(composition_status(X)),!.
parse_tokens(["defeat_preservation",X]):- \+ defeat_preservation(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(defeat_preservation(X)),!.
parse_tokens(["embedding_status",X]):- \+ embedding_status(_),member(X,["PASS","LOCAL_ONLY","FAIL","UNKNOWN"]),assertz(embedding_status(X)),!.
parse_tokens(["morphism_integrity",X]):- \+ morphism_integrity(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(morphism_integrity(X)),!.
parse_tokens(["preseal_provenance",X]):- \+ preseal_provenance(_),member(X,["SEALED","POSTHOC"]),assertz(preseal_provenance(X)),!.
parse_tokens(["reopening",X]):- \+ reopening(_),member(X,["ACTIVE","INACTIVE"]),assertz(reopening(X)),!.
parse_tokens(_):-fail.

validate:-seen_header,seen_end,rid(_),target(_),grammar(_),scope(_),probe_preservation(_),
 intervention_preservation(_),composition_status(_),defeat_preservation(_),embedding_status(_),
 morphism_integrity(_),preseal_provenance(_),reopening(_).

closure_ok:-grammar("PARTIAL_FAMILY"),!,composition_status(C),member(C,["PASS","PARTIAL_VERIFIED"]).
closure_ok:-composition_status("PASS").
embedding_ok:-embedding_status("PASS"),!.
embedding_ok:-embedding_status("LOCAL_ONLY"),scope(S),S\="GLOBAL".
preservation_ok:-probe_preservation("PASS"),intervention_preservation("PASS"),defeat_preservation("PASS").
constitution_admissible:-preservation_ok,closure_ok,embedding_ok,morphism_integrity("PASS"),preseal_provenance("SEALED"),reopening("ACTIVE").
global_transport:-constitution_admissible,scope("GLOBAL"),embedding_status("PASS").
yn(G,"YES"):-call(G),!. yn(_,"NO").

diagnosis("OVER_QUOTIENT"):-intervention_preservation("FAIL"),!.
diagnosis("PROBE_FAILURE"):-probe_preservation("FAIL"),!.
diagnosis("CLOSURE_FAILURE"):-composition_status(C),member(C,["FAIL","UNKNOWN"]),!.
diagnosis("DEFEAT_ERASURE"):-defeat_preservation("FAIL"),!.
diagnosis("SCOPE_EXPORT_FAILURE"):-embedding_status("FAIL"),!.
diagnosis("SCOPE_EXPORT_FAILURE"):-scope("GLOBAL"),embedding_status("LOCAL_ONLY"),!.
diagnosis("MORPHISM_CAPTURE"):-morphism_integrity("FAIL"),!.
diagnosis("CONSTITUTION_CAPTURE"):-preseal_provenance("POSTHOC"),!.
diagnosis("REOPENING_FAILURE"):-reopening("INACTIVE"),!.
diagnosis("ADMISSIBLE_LOCAL").

emit:-target(T),grammar(G),scope(S),probe_preservation(P),intervention_preservation(I),
 composition_status(C),defeat_preservation(D),embedding_status(E),morphism_integrity(M),
 preseal_provenance(PR),reopening(R),yn(closure_ok,CO),yn(embedding_ok,EO),yn(constitution_admissible,CA),
 diagnosis(DI),(global_transport->GT="YES_WITHIN_DECLARED_SCOPE";GT="NO"),
 (constitution_admissible->W="EARNED_LOCAL_CANDIDATE";W="HOLD"),
 format("invariance.target=~w~n",[T]),format("invariance.grammar=~w~n",[G]),format("invariance.scope=~w~n",[S]),
 format("invariance.probe_preservation=~w~n",[P]),format("invariance.intervention_preservation=~w~n",[I]),
 format("invariance.composition_status=~w~n",[C]),format("invariance.defeat_preservation=~w~n",[D]),
 format("invariance.embedding_status=~w~n",[E]),format("invariance.morphism_integrity=~w~n",[M]),
 format("invariance.preseal_provenance=~w~n",[PR]),format("invariance.reopening=~w~n",[R]),
 format("invariance.grammar_closure_adequate=~w~n",[CO]),format("invariance.embedding_claim_adequate=~w~n",[EO]),
 format("invariance.constitution_admissible=~w~n",[CA]),format("invariance.global_transport=~w~n",[GT]),
 format("invariance.diagnosis=~w~n",[DI]),writeln("invariance.self_authorizing=REJECT"),
 writeln("invariance.unique_global_constitution=NOT_EARNED"),
 writeln("invariance.actual_symmetry_equals_certified_inert=NO"),
 writeln("invariance.relation=CONTRACT_INDEXED"),format("invariance.wcicr=~w~n",[W]).
