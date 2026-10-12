//! MQR-4.114 P2-D: source-indexed certificate reference authority, NOT an experiment.
//! NIST SRM 965c Certificate of Analysis issued 2025-09-18:
//! https://tsapps.nist.gov/srmext/certificates/965c.pdf
//! Further metrology: NIST SP 260-253, doi 10.6028/NIST.SP.260-253.
//! User has NOT supplied a physical sample, matched apparatus, or lab readings.
#[derive(Debug,Clone,Copy)]
struct Level {n:u8, mg_dl:f64, mmol_l:f64, expanded_u_mmol:f64}
const CERTIFIED_LEVELS:[Level;4]=[
 Level{n:1,mg_dl:33.58,mmol_l:1.864,expanded_u_mmol:0.036},
 Level{n:2,mg_dl:95.94,mmol_l:5.325,expanded_u_mmol:0.068},
 Level{n:3,mg_dl:124.2,mmol_l:6.897,expanded_u_mmol:0.102},
 Level{n:4,mg_dl:299.1,mmol_l:16.61,expanded_u_mmol:0.22},
];
#[derive(Debug,Clone,Copy)]
struct Certificate {
 id:&'static str,issued:&'static str,expiry:&'static str,
 source:&'static str,traceable_to_si:bool,
 material_kind:&'static str, matched_to_2010_samples:bool,
}
const CURRENT:Certificate=Certificate{
 id:"NIST_SRM_965c",issued:"2025-09-18",expiry:"2035-01-31",
 source:"NIST_CERTIFICATE_2025_09_18",traceable_to_si:true,
 material_kind:"CERTIFIED_FROZEN_HUMAN_SERUM",matched_to_2010_samples:false,
};
const HISTORICAL:Certificate=Certificate{
 id:"NIST_SRM_965b",issued:"2019-08-01",expiry:"2024-12-31",
 source:"NIST_CERTIFICATE_2019_08_01",traceable_to_si:true,
 material_kind:"HISTORICAL_CERTIFIED_FROZEN_HUMAN_SERUM",matched_to_2010_samples:false,
};
fn date_shape(s:&str)->bool {
 let x=s.as_bytes();
 x.len()==10&&x[4]==b'-'&&x[7]==b'-'&&x.iter().enumerate().all(|(i,b)|i==4||i==7||b.is_ascii_digit())
}
fn certificate_period_contains(c:Certificate,date:&str)->Result<bool,String>{
 if !date_shape(c.issued)||!date_shape(c.expiry)||!date_shape(date)||c.issued>c.expiry{
  return Err("invalid_iso_date_metadata".into());
 }
 Ok(c.issued<=date&&date<=c.expiry)
}
fn verify_source_numbers(xs:&[Level])->Result<(),String>{
 if xs.len()!=4{return Err("four_certified_levels_required".into())}
 for (i,x) in xs.iter().enumerate(){
  if x.n!=i as u8+1 || !x.mg_dl.is_finite()||!x.mmol_l.is_finite()||!x.expanded_u_mmol.is_finite()
      ||x.mg_dl<=0.0||x.mmol_l<=0.0||x.expanded_u_mmol<=0.0 {return Err("invalid_level".into())}
  let converted=x.mg_dl*10.0/180.156;
  // Paper rounds concentrations independently from higher precision source values.
  if (converted-x.mmol_l).abs()>0.012{return Err("unit_derivation_conflict".into())}
  if i>0 && xs[i-1].mmol_l>=x.mmol_l{return Err("not_ordered".into())}
 }
 Ok(())
}
fn report()->Result<String,String>{
 verify_source_numbers(&CERTIFIED_LEVELS)?;
 let today="2026-10-12";
 let current=certificate_period_contains(CURRENT,today)?;
 let old=certificate_period_contains(HISTORICAL,today)?;
 if !current||old{return Err("certificate_period_contract_failure".into())}
 if CURRENT.matched_to_2010_samples||HISTORICAL.matched_to_2010_samples{return Err("false_matched_calibration".into())}
 Ok(format!(
  "source=NIST_SRM_965c_2025_09_18_CERTIFICATE\ncertified_material_levels={}\nreported_unit_views_per_level=3\nunit_conversion_creates_independent_measurements=NO\nmillimolar_values_derived_from_mass_concentration=YES\nSI_traceability_claim_source_certified={}\n965c_nominal_date_eligible_on_2026_10_12={}\n965b_nominal_date_eligible_on_2026_10_12={}\nmaterial_specific_certificate_condition=NOT_INSPECTED\ncarstensen_2010_pairs_referenced_to_965c=NO_MATCHED_MEASUREMENTS\nplasma_vs_capillary_matrix_commutability=HOLD\nCCQM_K11_2_anchor_consensus_difference_not_reproduced_in_code=TRUE\nexternal_intervention_by_MQR=NOT_PERFORMED\nreal_lang_promotion=HOLD\n",
  CERTIFIED_LEVELS.len(),CURRENT.traceable_to_si, current,old))
}
fn main(){print!("{}",report().expect("source typed certificate audit"))}
#[cfg(test)]mod tests{
 use super::*;
 #[test]fn four_original_certification_levels(){assert_eq!(CERTIFIED_LEVELS.len(),4);verify_source_numbers(&CERTIFIED_LEVELS).unwrap();}
 #[test]fn units_are_derived_not_replicates(){for l in CERTIFIED_LEVELS{assert!((l.mg_dl*10.0/180.156-l.mmol_l).abs()<0.012);}}
 #[test]fn every_reported_uncertainty_positive(){assert!(CERTIFIED_LEVELS.iter().all(|l|l.expanded_u_mmol>0.0));}
 #[test]fn reject_third_party_wrong_unit(){let mut a=CERTIFIED_LEVELS;a[0].mmol_l=3.2;assert!(verify_source_numbers(&a).is_err());}
 #[test]fn reject_negative_uncertainty(){let mut a=CERTIFIED_LEVELS;a[2].expanded_u_mmol=-0.1;assert!(verify_source_numbers(&a).is_err());}
 #[test]fn reject_duplicate_reference_level(){let mut a=CERTIFIED_LEVELS;a[3]=a[2];assert!(verify_source_numbers(&a).is_err());}
 #[test]fn certificate_965c_nominally_dated(){assert!(certificate_period_contains(CURRENT,"2026-10-12").unwrap());}
 #[test]fn historical_965b_expired(){assert!(!certificate_period_contains(HISTORICAL,"2026-10-12").unwrap());}
 #[test]fn current_future_period_end(){assert!(certificate_period_contains(CURRENT,"2035-01-31").unwrap());assert!(!certificate_period_contains(CURRENT,"2035-02-01").unwrap());}
 #[test]fn reject_malformed_dates(){assert!(certificate_period_contains(CURRENT,"2026/10/12").is_err());}
 #[test]fn source_has_no_matched_2010_experiment(){assert!(!CURRENT.matched_to_2010_samples);assert!(!HISTORICAL.matched_to_2010_samples);}
 #[test]fn material_authority_is_not_automatically_clinical_matrix_identity(){assert!(report().unwrap().contains("plasma_vs_capillary_matrix_commutability=HOLD"));}
 #[test]fn calendar_is_not_evidence_of_material_condition(){assert!(report().unwrap().contains("material_specific_certificate_condition=NOT_INSPECTED"));}
 #[test]fn actual_physical_intervention_has_not_occurred(){assert!(report().unwrap().contains("external_intervention_by_MQR=NOT_PERFORMED"));}
 #[test]fn source_doi_concepts_not_new_language(){assert!(report().unwrap().contains("real_lang_promotion=HOLD"));}
}
