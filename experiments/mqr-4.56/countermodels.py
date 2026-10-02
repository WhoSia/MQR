def attacks():
    cheap={"cheap_yield":10,"expensive_load_bearing":True,"cheap_material":False}
    info={"a_info":9,"a_relevance":1,"b_info":4,"b_relevance":9}
    novelty={"novelty_up":True,"target_relevance_down":True}
    goodhart={"proxy_up":True,"world_relevance_down":True,"shared_target_representation":True}
    drift={"old_relevance_high":True,"target_changed":True,"old_order_still_used":True}
    decoy={"count":1000,"independent":True,"high_proxy":True,"touches_live_boundary":False}
    evaluator={"generator_ancestry_diverse":True,"single_value_model":True,"shared_blind_spot":True}
    units={"order_before":"A>B","order_after":"B>A","scientific_relation_unchanged":True}
    horizon={"short":"A","long":"B","option_opening_B":True}
    action={"a_separation":9,"a_action":0,"b_separation":5,"b_action":1}
    surprise={"surprise_high":True,"peripheral_only":True}
    sunk={"past_yield_A":10,"fresh_escape_B":True,"policy_stays_A":True}
    insulation={"criticizes_value_model":True,"value_model_scores_irrelevant":True}
    option={"equal_current":True,"only_B_unlocks_new_family":True}
    return {
      "cheap_challenge_trap": cheap["cheap_yield"]>1 and cheap["expensive_load_bearing"] and not cheap["cheap_material"],
      "information_relevance_divergence": info["a_info"]>info["b_info"] and info["a_relevance"]<info["b_relevance"],
      "novelty_drift": novelty["novelty_up"] and novelty["target_relevance_down"],
      "incumbent_proxy_goodhart": all(goodhart.values()),
      "target_relevance_drift": all(drift.values()),
      "adversarial_decoy_flood": decoy["count"]>100 and decoy["independent"] and decoy["high_proxy"] and not decoy["touches_live_boundary"],
      "common_evaluator_capture": all(evaluator.values()),
      "cost_unit_rank_reversal": units["order_before"]!=units["order_after"] and units["scientific_relation_unchanged"],
      "horizon_reversal": horizon["short"]!=horizon["long"] and horizon["option_opening_B"],
      "actionability_divergence": action["a_separation"]>action["b_separation"] and action["a_action"]<action["b_action"],
      "surprise_not_importance": all(surprise.values()),
      "sunk_yield_lockin": sunk["past_yield_A"]>0 and sunk["fresh_escape_B"] and sunk["policy_stays_A"],
      "value_model_self_insulation": all(insulation.values()),
      "equal_current_value_unequal_option": all(option.values()),
    }

def positives():
    local={"prior_declared":True,"utility_declared":True,"cost_declared":True,"unique_local_optimum":True,"world_optimum":False}
    partial={"A_dominates_B":True,"C_D_incomparable":True}
    drift={"contract_changed":True,"sentinel_fires":True,"old_order_reused":False,"reconstituted":True}
    decoy={"decoy_rejected":True,"material_challenge_retained":True,"universal_utility_used":False}
    option={"modest_immediate":True,"unlocks_family":True,"declared_horizon":True,"admitted":True}
    revise={"predicted_superiority":True,"prospective_failure":True,"value_model_revised":True}
    return {
      "declared_model_local_optimizer": local["prior_declared"] and local["utility_declared"] and local["cost_declared"] and local["unique_local_optimum"] and not local["world_optimum"],
      "partial_order_guidance": all(partial.values()),
      "target_drift_reopening": drift["contract_changed"] and drift["sentinel_fires"] and not drift["old_order_reused"] and drift["reconstituted"],
      "adversarial_decoy_rejection": decoy["decoy_rejected"] and decoy["material_challenge_retained"] and not decoy["universal_utility_used"],
      "option_opening_value": all(option.values()),
      "value_model_revision": all(revise.values()),
    }
