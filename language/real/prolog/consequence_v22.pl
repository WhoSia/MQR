:- dynamic seen_header/0,seen_end/0,rid/1,target/1,typed_channels/1,ancestry_audit/1,
 common_mode/1,generator_grammar/1,off_grammar_route/1,adversarial_expansion/1,
 serialization_quotient/1,tacit_competence/1,heuristic_role/1,holdout/1,reopening/1,world_complete/1.

reset_all:-retractall(seen_header),retractall(seen_end),retractall(rid(_)),retractall(target(_)),
 retractall(typed_channels(_)),retractall(ancestry_audit(_)),retractall(common_mode(_)),
 retractall(generator_grammar(_)),retractall(off_grammar_route(_)),retractall(adversarial_expansion(_)),
 retractall(serialization_quotient(_)),retractall(tacit_competence(_)),retractall(heuristic_role(_)),
 retractall(holdout(_)),retractall(reopening(_)),retractall(world_complete(_)).

run(File):-reset_all,setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),maplist(parse_line,Lines),validate,emit.

parse_line(Line):-normalize_space(string(N),Line),
 (N=""->true;sub_string(N,0,1,_,"#")->true;seen_end->fail;
  split_string(N," \t"," \t",T),
  (\+ seen_header->(T=["REALCONSEQUENCE","0.22"]->assertz(seen_header);fail);parse_tokens(T))).

one(Fact):- \+ call(Fact),assertz(Fact).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["target",X]):- \+ target(_),member(X,["PROGRESS","MEASUREMENT","CAUSAL","REPRESENTATION","OTHER"]),assertz(target(X)),!.
parse_tokens(["typed_channels",X]):- \+ typed_channels(_),member(X,["PASS","FAIL"]),assertz(typed_channels(X)),!.
parse_tokens(["ancestry_audit",X]):- \+ ancestry_audit(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(ancestry_audit(X)),!.
parse_tokens(["common_mode",X]):- \+ common_mode(_),member(X,["YES","NO","UNKNOWN"]),assertz(common_mode(X)),!.
parse_tokens(["generator_grammar",X]):- \+ generator_grammar(_),member(X,["DECLARED","HOLD"]),assertz(generator_grammar(X)),!.
parse_tokens(["off_grammar_route",X]):- \+ off_grammar_route(_),member(X,["ACTIVE","ABSENT"]),assertz(off_grammar_route(X)),!.
parse_tokens(["adversarial_expansion",X]):- \+ adversarial_expansion(_),member(X,["PASS","HOLD","FAIL"]),assertz(adversarial_expansion(X)),!.
parse_tokens(["serialization_quotient",X]):- \+ serialization_quotient(_),member(X,["PASS","FAIL"]),assertz(serialization_quotient(X)),!.
parse_tokens(["tacit_competence",X]):- \+ tacit_competence(_),member(X,["VERIFIED","RECONSTRUCTIBLE","MISSING","NA"]),assertz(tacit_competence(X)),!.
parse_tokens(["heuristic_role",X]):- \+ heuristic_role(_),member(X,["GENERATE_ONLY","SELF_AUTHORIZING","NONE"]),assertz(heuristic_role(X)),!.
parse_tokens(["holdout",X]):- \+ holdout(_),member(X,["AVAILABLE","UNAVAILABLE_JUSTIFIED","ABSENT"]),assertz(holdout(X)),!.
parse_tokens(["reopening",X]):- \+ reopening(_),member(X,["ACTIVE","INACTIVE"]),assertz(reopening(X)),!.
parse_tokens(["world_complete",X]):- \+ world_complete(_),member(X,["NO_CLAIM","CLAIMED"]),assertz(world_complete(X)),!.
parse_tokens(_):-fail.

validate:-seen_header,seen_end,rid(_),target(_),typed_channels(_),ancestry_audit(_),common_mode(_),
 generator_grammar(_),off_grammar_route(_),adversarial_expansion(_),serialization_quotient(_),
 tacit_competence(_),heuristic_role(_),holdout(_),reopening(_),world_complete(_).

local_adequacy:-typed_channels("PASS"),ancestry_audit("PASS"),common_mode("NO"),
 generator_grammar("DECLARED"),off_grammar_route("ACTIVE"),adversarial_expansion("PASS"),
 serialization_quotient("PASS"),tacit_competence(T),T\="MISSING",
 heuristic_role(H),H\="SELF_AUTHORIZING",holdout(O),O\="ABSENT",
 reopening("ACTIVE"),world_complete("NO_CLAIM").

diagnosis("CHANNEL_COLLAPSE"):-typed_channels("FAIL"),!.
diagnosis("ANCESTRY_AUDIT_GAP"):-ancestry_audit(A),A\="PASS",!.
diagnosis("COMMON_MODE_CAPTURE"):-common_mode("YES"),!.
diagnosis("GENERATOR_GRAMMAR_HOLD"):-generator_grammar("HOLD"),!.
diagnosis("GENERATOR_CLOSURE_MIRAGE"):-off_grammar_route("ABSENT"),!.
diagnosis("ADVERSARIAL_EXPANSION_GAP"):-adversarial_expansion(A),A\="PASS",!.
diagnosis("SERIALIZATION_INFLATION"):-serialization_quotient("FAIL"),!.
diagnosis("COMPETENCE_GAP"):-tacit_competence("MISSING"),!.
diagnosis("HEURISTIC_SELF_AUTHORITY"):-heuristic_role("SELF_AUTHORIZING"),!.
diagnosis("HOLDOUT_GAP"):-holdout("ABSENT"),!.
diagnosis("REOPENING_FAILURE"):-reopening("INACTIVE"),!.
diagnosis("WORLD_COMPLETENESS_OVERCLAIM"):-world_complete("CLAIMED"),!.
diagnosis("OPEN_LOCAL_ADMISSIBLE").

yn(G,"YES"):-call(G),!. yn(_,"NO").
emit:-target(T),typed_channels(TC),ancestry_audit(AA),common_mode(CM),generator_grammar(GG),
 off_grammar_route(OG),adversarial_expansion(AE),serialization_quotient(SQ),tacit_competence(TA),
 heuristic_role(HR),holdout(HO),reopening(R),world_complete(WC),yn(local_adequacy,LA),diagnosis(D),
 (local_adequacy->W="EARNED_LOCAL_CANDIDATE";W="HOLD"),
 format("consequence.target=~w~n",[T]),format("consequence.typed_channels=~w~n",[TC]),
 format("consequence.ancestry_audit=~w~n",[AA]),format("consequence.common_mode=~w~n",[CM]),
 format("consequence.generator_grammar=~w~n",[GG]),format("consequence.off_grammar_route=~w~n",[OG]),
 format("consequence.adversarial_expansion=~w~n",[AE]),format("consequence.serialization_quotient=~w~n",[SQ]),
 format("consequence.tacit_competence=~w~n",[TA]),format("consequence.heuristic_role=~w~n",[HR]),
 format("consequence.holdout=~w~n",[HO]),format("consequence.reopening=~w~n",[R]),
 format("consequence.world_complete=~w~n",[WC]),format("consequence.local_adequacy=~w~n",[LA]),
 format("consequence.diagnosis=~w~n",[D]),writeln("consequence.self_certifying_family=REJECT"),
 writeln("consequence.formal_rigor_implies_family_completeness=REJECT"),
 writeln("consequence.intuition_self_authorizes=REJECT"),
 writeln("consequence.more_tests_implies_more_authority=REJECT"),
 writeln("consequence.world_family_complete=NO"),format("consequence.wccfr=~w~n",[W]).
