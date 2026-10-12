//! MQR 4.114: cross-domain rival identifiability test.
//! All values are INTENTIONALLY CONSTRUCTED; no physical or behavioral rows.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct PhysicalWorld { quantity: i32, shared_bias: i32 }
fn instrument_pair(w: PhysicalWorld) -> (i32,i32) {
    (w.quantity+w.shared_bias,w.quantity+w.shared_bias)
}
fn reference_readout(w: PhysicalWorld, shares_bias: bool) -> i32 {
    w.quantity+if shares_bias {w.shared_bias} else {0}
}
fn physical_rivals() -> (PhysicalWorld, PhysicalWorld) {
    (PhysicalWorld{quantity:1,shared_bias:0},
     PhysicalWorld{quantity:0,shared_bias:1})
}
#[derive(Debug, Clone, Copy)]
enum GoalModel { PerceivedHorizon, DirectAge }
fn reported_goal(model:GoalModel, age:u8, horizon:u8) -> u8 {
    match model {GoalModel::PerceivedHorizon=>horizon,GoalModel::DirectAge=>age}
}
fn baseline(age:u8)->u8 {age}
fn reversed_horizon(age:u8)->u8 {1-age}
fn check()->Result<String,String>{
 let (a,b)=physical_rivals();
 if instrument_pair(a)!=instrument_pair(b){return Err("physical_pair_not_equivalent".into())}
 if reference_readout(a,true)!=reference_readout(b,true){return Err("shared_reference_unexpectedly_independent".into())}
 if reference_readout(a,false)==reference_readout(b,false){return Err("independent_anchor_no_discrimination".into())}
 for age in 0..=1 {
  if reported_goal(GoalModel::PerceivedHorizon,age,baseline(age))!=reported_goal(GoalModel::DirectAge,age,baseline(age)){return Err("behavior_observation_not_equivalent".into())}
  if reported_goal(GoalModel::PerceivedHorizon,age,reversed_horizon(age))==reported_goal(GoalModel::DirectAge,age,reversed_horizon(age)){return Err("behavior_intervention_not_discriminative".into())}
 }
 Ok("mode=EXACT_FINITE_CONSTRUCTED_RIVALS\nphysical_observational_equivalence=TRUE\nthird_device_same_calibration_root=NO_NEW_IDENTIFICATION\nindependent_anchor_if_proven=DISCRIMINATES_CONSTRUCTED_RIVALS\nbehavior_age_horizon_observation=NONIDENTIFYING\nbehavior_do_horizon_if_valid=DISCRIMINATES_CONSTRUCTED_RIVALS\nempirical_intervention=NOT_PERFORMED\nbehavioral_construct_validity=HOLD\nphysical_calibration_ancestry=HOLD\nSST_REVIEW_NOT_RAW_TRIAL=TRUE\nBENDIX_METHOD_BOOK_NOT_SST_PAPER=TRUE\nREAL_LANG_PROMOTION=HOLD\n".into())
}
fn main(){print!("{}",check().expect("contract"))}
#[cfg(test)]mod tests{use super::*;
 #[test]fn pair_same(){let(a,b)=physical_rivals();assert_eq!(instrument_pair(a),instrument_pair(b))}
 #[test]fn true_quantity_distinct(){let(a,b)=physical_rivals();assert_ne!(a.quantity,b.quantity)}
 #[test]fn shared_reference_stays_ambiguous(){let(a,b)=physical_rivals();assert_eq!(reference_readout(a,true),reference_readout(b,true))}
 #[test]fn independent_reference_separates(){let(a,b)=physical_rivals();assert_ne!(reference_readout(a,false),reference_readout(b,false))}
 #[test]fn reference_has_correct_ideal_value(){let(a,_)=physical_rivals();assert_eq!(reference_readout(a,false),a.quantity)}
 #[test]fn behavior_baseline_identical_at_both_ages(){for age in 0..=1{let h=baseline(age);assert_eq!(reported_goal(GoalModel::PerceivedHorizon,age,h),reported_goal(GoalModel::DirectAge,age,h))}}
 #[test]fn behavior_intervention_separates_both_ages(){for age in 0..=1{let h=reversed_horizon(age);assert_ne!(reported_goal(GoalModel::PerceivedHorizon,age,h),reported_goal(GoalModel::DirectAge,age,h))}}
 #[test]fn intervention_does_not_change_age(){for age in 0..=1{assert_eq!(age,1-reversed_horizon(age))}}
 #[test]fn full_receipt_has_holds(){let s=check().unwrap();assert!(s.contains("empirical_intervention=NOT_PERFORMED"));assert!(s.contains("physical_calibration_ancestry=HOLD"))}
 #[test]fn no_false_book_equivalence(){assert!(check().unwrap().contains("BENDIX_METHOD_BOOK_NOT_SST_PAPER=TRUE"))}
 #[test]fn no_v044_promotion(){assert!(check().unwrap().contains("REAL_LANG_PROMOTION=HOLD"))}
}
