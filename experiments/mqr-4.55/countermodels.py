def attacks():
    many={"probe_count":10,"ancestry_count":1,"incumbent_agree":True,"exterior_separates":True}
    probe_intervention={"probes_agree":True,"intervention_splits":True}
    intervention_morphism={"interventions_agree":True,"morphism_splits":True}
    target_defeat={"registered_share_target_grammar":True,"external_anomaly_outside_grammar":True}
    serialization={"labels_before":1,"labels_after":12,"material_classes_before":1,"material_classes_after":1}
    grammar_escape={"grammar_closed":True,"off_grammar_material_escape":True}
    experts={"expert_count":6,"training_ancestry_count":1,"same_family":True,"outsider_adds_escape":True}
    productive_intuition={"outside_formal_generator":True,"prospective_separator":True,"self_authorized":False}
    seductive_intuition={"felt_salience_high":True,"world_contact_rejects":True}
    primitive_omission={"complete_in_language":True,"material_primitive_unexpressible":True}
    competence={"protocol_complete":True,"initial_capability":False,"reconstructed":True,"held_out_after":True}
    futures={"same_current_family":True,"different_expansion":True,"different_reopening":True}
    return {
      "many_probes_one_ancestry": all((many["probe_count"]>many["ancestry_count"],many["incumbent_agree"],many["exterior_separates"])),
      "probe_saturation_intervention_escape": all(probe_intervention.values()),
      "intervention_saturation_morphism_escape": all(intervention_morphism.values()),
      "target_generated_defeat_blindness": all(target_defeat.values()),
      "serialization_inflation": serialization["labels_after"]>serialization["labels_before"] and serialization["material_classes_after"]==serialization["material_classes_before"],
      "generator_closure_world_escape": all(grammar_escape.values()),
      "expert_headcount_common_mode": experts["expert_count"]>1 and experts["training_ancestry_count"]==1 and experts["same_family"] and experts["outsider_adds_escape"],
      "productive_intuition_generator": productive_intuition["outside_formal_generator"] and productive_intuition["prospective_separator"] and not productive_intuition["self_authorized"],
      "seductive_intuition_not_oracle": all(seductive_intuition.values()),
      "formal_completeness_primitive_omission": all(primitive_omission.values()),
      "protocol_not_competence": competence["protocol_complete"] and not competence["initial_capability"] and competence["reconstructed"] and competence["held_out_after"],
      "same_family_different_expansion_capacity": all(futures.values()),
    }

def positives():
    rigor={"useful_target":True,"gap_existed":True,"formal_detected_gap":True,"repair_preserved_target":True}
    intuition={"generated":True,"self_authorized":False,"prospective_test":True,"survives":True}
    cross_channel={"channels_converge":True,"independent_ancestries":True}
    tacit={"initial_transfer":False,"reconstructed":True,"held_out_after":True}
    open_family={"ancestry_audited":True,"off_grammar_route":True,"adversarial_expansion":True,
                 "serialization_invariant":True,"reopening_active":True,"world_complete_claim":False}
    return {
      "rigor_repairs_intuition": all(rigor.values()),
      "intuition_generate_world_adjudicate": intuition["generated"] and not intuition["self_authorized"] and intuition["prospective_test"] and intuition["survives"],
      "cross_channel_convergence": all(cross_channel.values()),
      "tacit_competence_reconstructible": not tacit["initial_transfer"] and tacit["reconstructed"] and tacit["held_out_after"],
      "open_family_local_adequacy": all(open_family[k] for k in ("ancestry_audited","off_grammar_route","adversarial_expansion","serialization_invariant","reopening_active")) and not open_family["world_complete_claim"],
    }
