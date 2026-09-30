:- dynamic seen_header/0,seen_end/0,rid/1,
 actor_genealogy/1,transition_provenance/1,obligation_transport/1,role_reauthorization/1,
 utility_reconstitution/1,mechanism_lineage/1,mechanism_replay/1,ontology_expansion/1,
 self_subjection/1,anti_inflation/1,closure_ceiling/1,scaffold_profile/1,
 world_claim_separation/1,drake_role_admission/1,toy_model_scope/1,
 scaffold_retirement/1,truth_distance_scalar/1,final_fixed_point/1.

reset_all:-
 retractall(seen_header),retractall(seen_end),retractall(rid(_)),
 retractall(actor_genealogy(_)),retractall(transition_provenance(_)),
 retractall(obligation_transport(_)),retractall(role_reauthorization(_)),
 retractall(utility_reconstitution(_)),retractall(mechanism_lineage(_)),
 retractall(mechanism_replay(_)),retractall(ontology_expansion(_)),
 retractall(self_subjection(_)),retractall(anti_inflation(_)),retractall(closure_ceiling(_)),
 retractall(scaffold_profile(_)),retractall(world_claim_separation(_)),
 retractall(drake_role_admission(_)),retractall(toy_model_scope(_)),
 retractall(scaffold_retirement(_)),retractall(truth_distance_scalar(_)),
 retractall(final_fixed_point(_)).

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
       (T=["REALREFLEX","0.25"] -> assertz(seen_header) ; fail)
   ; parse_tokens(T)
   )
 ).

parse_tokens(["END"]):-assertz(seen_end),!.
parse_tokens(["id",X]):- \+ rid(_),assertz(rid(X)),!.
parse_tokens(["actor_genealogy",X]):- \+ actor_genealogy(_),member(X,["PASS","FAIL"]),assertz(actor_genealogy(X)),!.
parse_tokens(["transition_provenance",X]):- \+ transition_provenance(_),member(X,["PASS","FAIL"]),assertz(transition_provenance(X)),!.
parse_tokens(["obligation_transport",X]):- \+ obligation_transport(_),member(X,["PASS","HOLD","FAIL"]),assertz(obligation_transport(X)),!.
parse_tokens(["role_reauthorization",X]):- \+ role_reauthorization(_),member(X,["PASS","HOLD","FAIL"]),assertz(role_reauthorization(X)),!.
parse_tokens(["utility_reconstitution",X]):- \+ utility_reconstitution(_),member(X,["PASS","HOLD","FAIL"]),assertz(utility_reconstitution(X)),!.
parse_tokens(["mechanism_lineage",X]):- \+ mechanism_lineage(_),member(X,["PASS","HOLD","FAIL"]),assertz(mechanism_lineage(X)),!.
parse_tokens(["mechanism_replay",X]):- \+ mechanism_replay(_),member(X,["PASS","HOLD","FAIL"]),assertz(mechanism_replay(X)),!.
parse_tokens(["ontology_expansion",X]):- \+ ontology_expansion(_),member(X,["PASS","HOLD","FAIL"]),assertz(ontology_expansion(X)),!.
parse_tokens(["self_subjection",X]):- \+ self_subjection(_),member(X,["ACTIVE","ABSENT"]),assertz(self_subjection(X)),!.
parse_tokens(["anti_inflation",X]):- \+ anti_inflation(_),member(X,["PASS","HOLD","FAIL"]),assertz(anti_inflation(X)),!.
parse_tokens(["closure_ceiling",X]):- \+ closure_ceiling(_),member(X,["ENFORCED","ABSENT"]),assertz(closure_ceiling(X)),!.
parse_tokens(["scaffold_profile",X]):- \+ scaffold_profile(_),member(X,["PASS","FAIL"]),assertz(scaffold_profile(X)),!.
parse_tokens(["world_claim_separation",X]):- \+ world_claim_separation(_),member(X,["PASS","FAIL"]),assertz(world_claim_separation(X)),!.
parse_tokens(["drake_role_admission",X]):- \+ drake_role_admission(_),member(X,["PASS","HOLD","FAIL"]),assertz(drake_role_admission(X)),!.
parse_tokens(["toy_model_scope",X]):- \+ toy_model_scope(_),member(X,["PASS","HOLD","FAIL"]),assertz(toy_model_scope(X)),!.
parse_tokens(["scaffold_retirement",X]):- \+ scaffold_retirement(_),member(X,["ACTIVE","ABSENT"]),assertz(scaffold_retirement(X)),!.
parse_tokens(["truth_distance_scalar",X]):- \+ truth_distance_scalar(_),member(X,["OFF","ON"]),assertz(truth_distance_scalar(X)),!.
parse_tokens(["final_fixed_point",X]):- \+ final_fixed_point(_),member(X,["NO_CLAIM","CLAIMED"]),assertz(final_fixed_point(X)),!.
parse_tokens(_):-fail.

validate:-
 seen_header,seen_end,rid(_),actor_genealogy(_),transition_provenance(_),
 obligation_transport(_),role_reauthorization(_),utility_reconstitution(_),
 mechanism_lineage(_),mechanism_replay(_),ontology_expansion(_),
 self_subjection(_),anti_inflation(_),closure_ceiling(_),scaffold_profile(_),
 world_claim_separation(_),drake_role_admission(_),toy_model_scope(_),
 scaffold_retirement(_),truth_distance_scalar(_),final_fixed_point(_).

local_reflex:-
 actor_genealogy("PASS"),transition_provenance("PASS"),obligation_transport("PASS"),
 role_reauthorization("PASS"),utility_reconstitution("PASS"),mechanism_lineage("PASS"),
 mechanism_replay("PASS"),ontology_expansion("PASS"),self_subjection("ACTIVE"),
 anti_inflation("PASS"),closure_ceiling("ENFORCED"),scaffold_profile("PASS"),
 world_claim_separation("PASS"),drake_role_admission("PASS"),toy_model_scope("PASS"),
 scaffold_retirement("ACTIVE"),truth_distance_scalar("OFF"),final_fixed_point("NO_CLAIM").

diagnosis("GENEALOGY_GAP"):-actor_genealogy("FAIL"),!.
diagnosis("TRANSITION_PROVENANCE_GAP"):-transition_provenance("FAIL"),!.
diagnosis("OBLIGATION_TRANSPORT_GAP"):-obligation_transport(V),V\="PASS",!.
diagnosis("ROLE_REAUTHORIZATION_GAP"):-role_reauthorization(V),V\="PASS",!.
diagnosis("UTILITY_RECONSTITUTION_GAP"):-utility_reconstitution(V),V\="PASS",!.
diagnosis("MECHANISM_LINEAGE_GAP"):-mechanism_lineage(V),V\="PASS",!.
diagnosis("MECHANISM_REPLAY_GAP"):-mechanism_replay(V),V\="PASS",!.
diagnosis("ONTOLOGY_EXPANSION_GAP"):-ontology_expansion(V),V\="PASS",!.
diagnosis("CONSTITUTION_SELF_EXEMPTION"):-self_subjection("ABSENT"),!.
diagnosis("RAVEL_NOOP_INFLATION"):-anti_inflation(V),V\="PASS",!.
diagnosis("CLOSURE_FINALITY_OVERCLAIM"):-closure_ceiling("ABSENT"),!.
diagnosis("SCAFFOLD_PROFILE_GAP"):-scaffold_profile("FAIL"),!.
diagnosis("SCAFFOLD_WORLD_AUTHORITY_CONFLATION"):-world_claim_separation("FAIL"),!.
diagnosis("DRAKE_ROLE_GAP"):-drake_role_admission(V),V\="PASS",!.
diagnosis("TOY_MODEL_SCOPE_GAP"):-toy_model_scope(V),V\="PASS",!.
diagnosis("SCAFFOLD_FOSSILIZATION"):-scaffold_retirement("ABSENT"),!.
diagnosis("TRUTH_DISTANCE_SCALAR_RESURRECTION"):-truth_distance_scalar("ON"),!.
diagnosis("FINAL_REFLECTIVE_FIXED_POINT_OVERCLAIM"):-final_fixed_point("CLAIMED"),!.
diagnosis("LOCAL_REFLEXIVE_ECOLOGY_ADMISSIBLE").

yn(G,"YES"):-call(G),!. yn(_,"NO").

emit:-
 actor_genealogy(G),transition_provenance(T),obligation_transport(O),
 role_reauthorization(RR),utility_reconstitution(U),mechanism_lineage(M),
 mechanism_replay(MR),ontology_expansion(OE),self_subjection(SS),
 anti_inflation(AI),closure_ceiling(CC),scaffold_profile(SP),
 world_claim_separation(WC),drake_role_admission(DR),toy_model_scope(TM),
 scaffold_retirement(SR),truth_distance_scalar(TD),final_fixed_point(FP),
 yn(local_reflex,LR),diagnosis(D),
 (local_reflex->W="EARNED_LOCAL_CANDIDATE";W="HOLD"),
 format("reflex.actor_genealogy=~w~n",[G]),
 format("reflex.transition_provenance=~w~n",[T]),
 format("reflex.obligation_transport=~w~n",[O]),
 format("reflex.role_reauthorization=~w~n",[RR]),
 format("reflex.utility_reconstitution=~w~n",[U]),
 format("reflex.mechanism_lineage=~w~n",[M]),
 format("reflex.mechanism_replay=~w~n",[MR]),
 format("reflex.ontology_expansion=~w~n",[OE]),
 format("reflex.self_subjection=~w~n",[SS]),
 format("reflex.anti_inflation=~w~n",[AI]),
 format("reflex.closure_ceiling=~w~n",[CC]),
 format("reflex.scaffold_profile=~w~n",[SP]),
 format("reflex.world_claim_separation=~w~n",[WC]),
 format("reflex.drake_role_admission=~w~n",[DR]),
 format("reflex.toy_model_scope=~w~n",[TM]),
 format("reflex.scaffold_retirement=~w~n",[SR]),
 format("reflex.truth_distance_scalar=~w~n",[TD]),
 format("reflex.final_fixed_point=~w~n",[FP]),
 format("reflex.local_reflexive_robustness=~w~n",[LR]),
 format("reflex.diagnosis=~w~n",[D]),
 writeln("reflex.fixed_actor_ontology=REJECT"),
 writeln("reflex.fixed_utility_transport=REJECT"),
 writeln("reflex.fixed_mechanism_ontology=REJECT"),
 writeln("reflex.constitution_self_immunity=REJECT"),
 writeln("reflex.stage_closure_finality=REJECT"),
 writeln("reflex.scaffold_value_equals_world_authority=REJECT"),
 writeln("reflex.world_authority_equals_scaffold_value=REJECT"),
 writeln("reflex.truth_distance_scalar_authority=NOT_EARNED"),
 writeln("reflex.universal_self_reduction_fixed_point=NOT_EARNED"),
 format("reflex.wcaer=~w~n",[W]),
 format("reflex.rcsr=~w~n",[W]),
 format("reflex.isp=~w~n",[W]).
