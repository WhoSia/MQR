:- dynamic seen_header/0,seen_end/0,rid/1,
 agent_map/1,private_information/1,incentive_map/1,supply_provenance/1,
 cost_reconciliation/1,target_provenance/1,proxy_choice_provenance/1,
 performative_feedback/1,strategic_ancestry/1,anti_sybil/1,
 mechanism_counterfactual/1,exterior_reserve/1,equilibrium_ceiling/1,
 capture_attribution/1,reopening/1,mechanism_scope/1,wcepr_dependency/1,
 universal_mechanism/1.

reset_all:-
 retractall(seen_header),retractall(seen_end),retractall(rid(_)),
 retractall(agent_map(_)),retractall(private_information(_)),retractall(incentive_map(_)),
 retractall(supply_provenance(_)),retractall(cost_reconciliation(_)),retractall(target_provenance(_)),
 retractall(proxy_choice_provenance(_)),retractall(performative_feedback(_)),
 retractall(strategic_ancestry(_)),retractall(anti_sybil(_)),retractall(mechanism_counterfactual(_)),
 retractall(exterior_reserve(_)),retractall(equilibrium_ceiling(_)),retractall(capture_attribution(_)),
 retractall(reopening(_)),retractall(mechanism_scope(_)),retractall(wcepr_dependency(_)),
 retractall(universal_mechanism(_)).

run(File):-
 reset_all,
 setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),
 maplist(parse_line,Lines),
 validate,
 emit.

parse_line(Line):-
 normalize_space(string(N),Line),
 ( N="" -> true
 ; sub_string(N,0,1,_,"#") -> true
 ; seen_end -> fail
 ; split_string(N," \t"," \t",T),
   ( \+ seen_header ->
       (T=["REALSTRATEGY","0.24"] -> assertz(seen_header) ; fail)
   ; parse_tokens(T)
   )
 ).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["agent_map",X]):- \+ agent_map(_),member(X,["PASS","FAIL"]),assertz(agent_map(X)),!.
parse_tokens(["private_information",X]):- \+ private_information(_),member(X,["PASS","FAIL"]),assertz(private_information(X)),!.
parse_tokens(["incentive_map",X]):- \+ incentive_map(_),member(X,["PASS","FAIL"]),assertz(incentive_map(X)),!.
parse_tokens(["supply_provenance",X]):- \+ supply_provenance(_),member(X,["PASS","FAIL"]),assertz(supply_provenance(X)),!.
parse_tokens(["cost_reconciliation",X]):- \+ cost_reconciliation(_),member(X,["PASS","HOLD","FAIL"]),assertz(cost_reconciliation(X)),!.
parse_tokens(["target_provenance",X]):- \+ target_provenance(_),member(X,["PASS","HOLD","FAIL"]),assertz(target_provenance(X)),!.
parse_tokens(["proxy_choice_provenance",X]):- \+ proxy_choice_provenance(_),member(X,["PASS","HOLD","FAIL"]),assertz(proxy_choice_provenance(X)),!.
parse_tokens(["performative_feedback",X]):- \+ performative_feedback(_),member(X,["PASS","HOLD","FAIL"]),assertz(performative_feedback(X)),!.
parse_tokens(["strategic_ancestry",X]):- \+ strategic_ancestry(_),member(X,["PASS","HOLD","FAIL"]),assertz(strategic_ancestry(X)),!.
parse_tokens(["anti_sybil",X]):- \+ anti_sybil(_),member(X,["PASS","HOLD","FAIL"]),assertz(anti_sybil(X)),!.
parse_tokens(["mechanism_counterfactual",X]):- \+ mechanism_counterfactual(_),member(X,["PASS","HOLD","FAIL"]),assertz(mechanism_counterfactual(X)),!.
parse_tokens(["exterior_reserve",X]):- \+ exterior_reserve(_),member(X,["ACTIVE","ABSENT"]),assertz(exterior_reserve(X)),!.
parse_tokens(["equilibrium_ceiling",X]):- \+ equilibrium_ceiling(_),member(X,["ENFORCED","ABSENT"]),assertz(equilibrium_ceiling(X)),!.
parse_tokens(["capture_attribution",X]):- \+ capture_attribution(_),member(X,["PASS","HOLD","FAIL"]),assertz(capture_attribution(X)),!.
parse_tokens(["reopening",X]):- \+ reopening(_),member(X,["ACTIVE","INACTIVE"]),assertz(reopening(X)),!.
parse_tokens(["mechanism_scope",X]):- \+ mechanism_scope(_),member(X,["DECLARED_LOCAL","WORLD"]),assertz(mechanism_scope(X)),!.
parse_tokens(["wcepr_dependency",X]):- \+ wcepr_dependency(_),member(X,["DECLARED","HIDDEN"]),assertz(wcepr_dependency(X)),!.
parse_tokens(["universal_mechanism",X]):- \+ universal_mechanism(_),member(X,["NO_CLAIM","CLAIMED"]),assertz(universal_mechanism(X)),!.
parse_tokens(_):-fail.

validate:-
 seen_header,seen_end,rid(_),agent_map(_),private_information(_),incentive_map(_),
 supply_provenance(_),cost_reconciliation(_),target_provenance(_),proxy_choice_provenance(_),
 performative_feedback(_),strategic_ancestry(_),anti_sybil(_),mechanism_counterfactual(_),
 exterior_reserve(_),equilibrium_ceiling(_),capture_attribution(_),reopening(_),
 mechanism_scope(_),wcepr_dependency(_),universal_mechanism(_).

local_robust:-
 agent_map("PASS"),private_information("PASS"),incentive_map("PASS"),supply_provenance("PASS"),
 cost_reconciliation("PASS"),target_provenance("PASS"),proxy_choice_provenance("PASS"),
 performative_feedback("PASS"),strategic_ancestry("PASS"),anti_sybil("PASS"),
 mechanism_counterfactual("PASS"),exterior_reserve("ACTIVE"),equilibrium_ceiling("ENFORCED"),
 capture_attribution("PASS"),reopening("ACTIVE"),mechanism_scope("DECLARED_LOCAL"),
 wcepr_dependency("DECLARED"),universal_mechanism("NO_CLAIM").

diagnosis("AGENT_MAP_GAP"):-agent_map("FAIL"),!.
diagnosis("PRIVATE_INFORMATION_BLIND"):-private_information("FAIL"),!.
diagnosis("INCENTIVE_MAP_GAP"):-incentive_map("FAIL"),!.
diagnosis("SUPPLY_ENDOGENEITY_BLIND"):-supply_provenance("FAIL"),!.
diagnosis("COST_REPORT_ORACLE"):-cost_reconciliation(V),V\="PASS",!.
diagnosis("TARGET_FRAMING_GAP"):-target_provenance(V),V\="PASS",!.
diagnosis("PROXY_ARBITRAGE_GAP"):-proxy_choice_provenance(V),V\="PASS",!.
diagnosis("PERFORMATIVE_FEEDBACK_BLIND"):-performative_feedback(V),V\="PASS",!.
diagnosis("STRATEGIC_ANCESTRY_GAP"):-strategic_ancestry(V),V\="PASS",!.
diagnosis("SYBIL_MULTIPLICITY"):-anti_sybil(V),V\="PASS",!.
diagnosis("MECHANISM_COUNTERFACTUAL_GAP"):-mechanism_counterfactual(V),V\="PASS",!.
diagnosis("EXTERIOR_RESERVE_ABSENT"):-exterior_reserve("ABSENT"),!.
diagnosis("EQUILIBRIUM_OVERCLAIM"):-equilibrium_ceiling("ABSENT"),!.
diagnosis("CAPTURE_ATTRIBUTION_GAP"):-capture_attribution(V),V\="PASS",!.
diagnosis("STRATEGIC_REOPENING_FAILURE"):-reopening("INACTIVE"),!.
diagnosis("WORLD_MECHANISM_OVERCLAIM"):-mechanism_scope("WORLD"),!.
diagnosis("HIDDEN_WCEPR_DEPENDENCY"):-wcepr_dependency("HIDDEN"),!.
diagnosis("UNIVERSAL_MECHANISM_OVERCLAIM"):-universal_mechanism("CLAIMED"),!.
diagnosis("LOCAL_STRATEGIC_ECOLOGY_ADMISSIBLE").

yn(G,"YES"):-call(G),!. yn(_,"NO").

emit:-
 agent_map(A),private_information(PI),incentive_map(I),supply_provenance(S),
 cost_reconciliation(C),target_provenance(T),proxy_choice_provenance(P),
 performative_feedback(PF),strategic_ancestry(SA),anti_sybil(AS),
 mechanism_counterfactual(MC),exterior_reserve(ER),equilibrium_ceiling(EQ),
 capture_attribution(CA),reopening(R),mechanism_scope(MS),wcepr_dependency(WD),
 universal_mechanism(UM),yn(local_robust,LR),diagnosis(D),
 (local_robust->W="EARNED_LOCAL_CANDIDATE";W="HOLD"),
 format("strategy.agent_map=~w~n",[A]),
 format("strategy.private_information=~w~n",[PI]),
 format("strategy.incentive_map=~w~n",[I]),
 format("strategy.supply_provenance=~w~n",[S]),
 format("strategy.cost_reconciliation=~w~n",[C]),
 format("strategy.target_provenance=~w~n",[T]),
 format("strategy.proxy_choice_provenance=~w~n",[P]),
 format("strategy.performative_feedback=~w~n",[PF]),
 format("strategy.strategic_ancestry=~w~n",[SA]),
 format("strategy.anti_sybil=~w~n",[AS]),
 format("strategy.mechanism_counterfactual=~w~n",[MC]),
 format("strategy.exterior_reserve=~w~n",[ER]),
 format("strategy.equilibrium_ceiling=~w~n",[EQ]),
 format("strategy.capture_attribution=~w~n",[CA]),
 format("strategy.reopening=~w~n",[R]),
 format("strategy.mechanism_scope=~w~n",[MS]),
 format("strategy.wcepr_dependency=~w~n",[WD]),
 format("strategy.universal_mechanism=~w~n",[UM]),
 format("strategy.local_strategic_robustness=~w~n",[LR]),
 format("strategy.diagnosis=~w~n",[D]),
 writeln("strategy.wcepr_incentive_robust_by_default=REJECT"),
 writeln("strategy.equilibrium_implies_epistemic_adequacy=REJECT"),
 writeln("strategy.nominal_agent_count_implies_independence=REJECT"),
 writeln("strategy.universal_scientific_mechanism=NOT_EARNED"),
 format("strategy.wcser=~w~n",[W]).
