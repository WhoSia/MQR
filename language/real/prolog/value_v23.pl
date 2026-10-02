:- dynamic seen_header/0,seen_end/0,rid/1,target_contract/1,typed_value_profile/1,
 value_provenance/1,proxy_dependence/1,target_drift_sentinel/1,adversarial_decoy_test/1,
 opportunity_cost/1,unit_audit/1,horizon/1,option_value/1,exterior_value_challenge/1,
 reopening/1,optimizer_scope/1,scalar_default/1,world_optimum/1.

reset_all:-retractall(seen_header),retractall(seen_end),retractall(rid(_)),
 retractall(target_contract(_)),retractall(typed_value_profile(_)),retractall(value_provenance(_)),
 retractall(proxy_dependence(_)),retractall(target_drift_sentinel(_)),retractall(adversarial_decoy_test(_)),
 retractall(opportunity_cost(_)),retractall(unit_audit(_)),retractall(horizon(_)),retractall(option_value(_)),
 retractall(exterior_value_challenge(_)),retractall(reopening(_)),retractall(optimizer_scope(_)),
 retractall(scalar_default(_)),retractall(world_optimum(_)).

run(File):-reset_all,setup_call_cleanup(open(File,read,S),read_string(S,_,Text),close(S)),
 split_string(Text,"\n","\r",Lines),maplist(parse_line,Lines),validate,emit.

parse_line(Line):-normalize_space(string(N),Line),
 (N=""->true;sub_string(N,0,1,_,"#")->true;seen_end->fail;
  split_string(N," \t"," \t",T),
  (\+ seen_header->(T=["REALVALUE","0.23"]->assertz(seen_header);fail);parse_tokens(T))).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["target_contract",X]):- \+ target_contract(_),member(X,["DECLARED","HOLD"]),assertz(target_contract(X)),!.
parse_tokens(["typed_value_profile",X]):- \+ typed_value_profile(_),member(X,["PASS","FAIL"]),assertz(typed_value_profile(X)),!.
parse_tokens(["value_provenance",X]):- \+ value_provenance(_),member(X,["PASS","FAIL","UNKNOWN"]),assertz(value_provenance(X)),!.
parse_tokens(["proxy_dependence",X]):- \+ proxy_dependence(_),member(X,["DECLARED","HIDDEN"]),assertz(proxy_dependence(X)),!.
parse_tokens(["target_drift_sentinel",X]):- \+ target_drift_sentinel(_),member(X,["ACTIVE","ABSENT"]),assertz(target_drift_sentinel(X)),!.
parse_tokens(["adversarial_decoy_test",X]):- \+ adversarial_decoy_test(_),member(X,["PASS","HOLD","FAIL"]),assertz(adversarial_decoy_test(X)),!.
parse_tokens(["opportunity_cost",X]):- \+ opportunity_cost(_),member(X,["DECLARED","HOLD"]),assertz(opportunity_cost(X)),!.
parse_tokens(["unit_audit",X]):- \+ unit_audit(_),member(X,["PASS","FAIL"]),assertz(unit_audit(X)),!.
parse_tokens(["horizon",X]):- \+ horizon(_),member(X,["DECLARED","HOLD"]),assertz(horizon(X)),!.
parse_tokens(["option_value",X]):- \+ option_value(_),member(X,["TRACKED","UNTRACKED"]),assertz(option_value(X)),!.
parse_tokens(["exterior_value_challenge",X]):- \+ exterior_value_challenge(_),member(X,["ACTIVE","ABSENT"]),assertz(exterior_value_challenge(X)),!.
parse_tokens(["reopening",X]):- \+ reopening(_),member(X,["ACTIVE","INACTIVE"]),assertz(reopening(X)),!.
parse_tokens(["optimizer_scope",X]):- \+ optimizer_scope(_),member(X,["DECLARED_MODEL","NONE","WORLD"]),assertz(optimizer_scope(X)),!.
parse_tokens(["scalar_default",X]):- \+ scalar_default(_),member(X,["OFF","ON"]),assertz(scalar_default(X)),!.
parse_tokens(["world_optimum",X]):- \+ world_optimum(_),member(X,["NO_CLAIM","CLAIMED"]),assertz(world_optimum(X)),!.
parse_tokens(_):-fail.

validate:-seen_header,seen_end,rid(_),target_contract(_),typed_value_profile(_),value_provenance(_),
 proxy_dependence(_),target_drift_sentinel(_),adversarial_decoy_test(_),opportunity_cost(_),
 unit_audit(_),horizon(_),option_value(_),exterior_value_challenge(_),reopening(_),
 optimizer_scope(_),scalar_default(_),world_optimum(_).

local_guidance:-target_contract("DECLARED"),typed_value_profile("PASS"),value_provenance("PASS"),
 proxy_dependence("DECLARED"),target_drift_sentinel("ACTIVE"),adversarial_decoy_test("PASS"),
 opportunity_cost("DECLARED"),unit_audit("PASS"),horizon("DECLARED"),option_value("TRACKED"),
 exterior_value_challenge("ACTIVE"),reopening("ACTIVE"),optimizer_scope(OS),OS\="WORLD",
 scalar_default("OFF"),world_optimum("NO_CLAIM").

diagnosis("TARGET_CONTRACT_HOLD"):-target_contract("HOLD"),!.
diagnosis("VALUE_PROFILE_COLLAPSE"):-typed_value_profile("FAIL"),!.
diagnosis("VALUE_PROVENANCE_GAP"):-value_provenance(V),V\="PASS",!.
diagnosis("HIDDEN_PROXY_DEPENDENCE"):-proxy_dependence("HIDDEN"),!.
diagnosis("TARGET_DRIFT_BLIND"):-target_drift_sentinel("ABSENT"),!.
diagnosis("DECOY_RESISTANCE_GAP"):-adversarial_decoy_test(V),V\="PASS",!.
diagnosis("OPPORTUNITY_COST_HOLD"):-opportunity_cost("HOLD"),!.
diagnosis("UNIT_RANK_REVERSAL"):-unit_audit("FAIL"),!.
diagnosis("HORIZON_HOLD"):-horizon("HOLD"),!.
diagnosis("OPTION_VALUE_BLIND"):-option_value("UNTRACKED"),!.
diagnosis("VALUE_MODEL_SELF_INSULATION"):-exterior_value_challenge("ABSENT"),!.
diagnosis("VALUE_REOPENING_FAILURE"):-reopening("INACTIVE"),!.
diagnosis("WORLD_OPTIMIZER_OVERCLAIM"):-optimizer_scope("WORLD"),!.
diagnosis("SCALAR_DEFAULT_ON"):-scalar_default("ON"),!.
diagnosis("WORLD_OPTIMUM_OVERCLAIM"):-world_optimum("CLAIMED"),!.
diagnosis("LOCAL_EXPANSION_GUIDANCE_ADMISSIBLE").

yn(G,"YES"):-call(G),!. yn(_,"NO").
emit:-target_contract(T),typed_value_profile(TV),value_provenance(VP),proxy_dependence(PD),
 target_drift_sentinel(TD),adversarial_decoy_test(AD),opportunity_cost(OC),unit_audit(UA),
 horizon(H),option_value(OV),exterior_value_challenge(EV),reopening(R),optimizer_scope(OS),
 scalar_default(SD),world_optimum(WO),yn(local_guidance,LG),diagnosis(D),
 (local_guidance->W="EARNED_LOCAL_CANDIDATE";W="HOLD"),
 format("value.target_contract=~w~n",[T]),format("value.typed_value_profile=~w~n",[TV]),
 format("value.value_provenance=~w~n",[VP]),format("value.proxy_dependence=~w~n",[PD]),
 format("value.target_drift_sentinel=~w~n",[TD]),format("value.adversarial_decoy_test=~w~n",[AD]),
 format("value.opportunity_cost=~w~n",[OC]),format("value.unit_audit=~w~n",[UA]),
 format("value.horizon=~w~n",[H]),format("value.option_value=~w~n",[OV]),
 format("value.exterior_value_challenge=~w~n",[EV]),format("value.reopening=~w~n",[R]),
 format("value.optimizer_scope=~w~n",[OS]),format("value.scalar_default=~w~n",[SD]),
 format("value.world_optimum=~w~n",[WO]),format("value.local_guidance=~w~n",[LG]),
 format("value.diagnosis=~w~n",[D]),writeln("value.universal_scientific_utility=REJECT"),
 writeln("value.value_constitution_self_authorizes=REJECT"),
 writeln("value.world_optimal_policy=NOT_EARNED"),format("value.wcepr=~w~n",[W]).
