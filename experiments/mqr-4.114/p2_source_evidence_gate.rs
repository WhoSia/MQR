//! MQR 4.114 P2 literature provenance gate: case labels are not world receipts.
use std::collections::{BTreeMap,BTreeSet};
const CORPUS: &str=include_str!("fixtures/p2_source_vignettes.psv");
#[derive(Clone,Debug,Eq,PartialEq)]
struct Case {id:String,source:String,kind:String,acquisition:String,raw:bool,independent:bool,roles:BTreeSet<String>}
fn decode(s:&str)->Result<Vec<Case>,String>{
 let mut out=Vec::new();let mut ids=BTreeSet::new();
 for (ln,l) in s.lines().enumerate(){
  let t=l.trim();if t.is_empty()||t.starts_with('#'){continue}
  let f:Vec<_>=t.split('|').collect();
  if f.len()!=7{return Err(format!("column_count_line_{}",ln+1))}
  if !ids.insert(f[0].to_string()){return Err(format!("repeated_id_line_{}",ln+1))}
  if !matches!(f[2],"SECONDARY_ANNOTATION"|"ONTOLOGY_SCHEMATIC"|"PUBLISHED_PRIMARY_REPORT"|"LITERATURE_REVIEW"){return Err(format!("unknown_source_kind_line_{}",ln+1))}
  if !matches!(f[3],"REANALYSIS_ONLY"|"ORIGINAL_OBSERVATION_DESCRIBED"|"ILLUSTRATION_NOT_OBSERVATION"|"LITERATURE_SYNTHESIS_NOT_OBSERVATION"){return Err(format!("unknown_acquisition_line_{}",ln+1))}
  if !f[1].starts_with("10."){return Err(format!("missing_source_doi_line_{}",ln+1))}
  let yesno=|x:&str|match x{"YES"=>Ok(true),"NO"=>Ok(false),_=>Err(format!("invalid_boolean_line_{}",ln+1))};
  let raw=yesno(f[4])?;let independent=yesno(f[5])?;
  if independent && (!raw||f[3]!="ORIGINAL_OBSERVATION_DESCRIBED"||f[2]!="PUBLISHED_PRIMARY_REPORT"){return Err(format!("independence_claim_not_grounded_line_{}",ln+1))}
  if raw && f[2]!="PUBLISHED_PRIMARY_REPORT"{return Err(format!("raw_evidence_source_kind_conflict_line_{}",ln+1))}
  if (f[2]=="LITERATURE_REVIEW")!=(f[3]=="LITERATURE_SYNTHESIS_NOT_OBSERVATION"){return Err(format!("review_type_mismatch_line_{}",ln+1))}
  let roles=f[6].split(',').map(str::to_string).collect::<BTreeSet<_>>();
  if roles.is_empty()||roles.contains(""){return Err(format!("empty_role_line_{}",ln+1))}
  out.push(Case{id:f[0].into(),source:f[1].into(),kind:f[2].into(),acquisition:f[3].into(),raw,independent,roles});
 }
 if out.is_empty(){return Err("no_cases".into())}Ok(out)
}
fn summary(xs:&[Case])->String{
 let unique_sources=xs.iter().map(|x|x.source.as_str()).collect::<BTreeSet<_>>().len();
 let new_observation_described=xs.iter().filter(|x|x.acquisition=="ORIGINAL_OBSERVATION_DESCRIBED").count();
 let reanalysis=xs.iter().filter(|x|x.acquisition=="REANALYSIS_ONLY").count();
 let illustration=xs.iter().filter(|x|x.acquisition=="ILLUSTRATION_NOT_OBSERVATION").count();
 let reviews=xs.iter().filter(|x|x.kind=="LITERATURE_REVIEW" && x.acquisition=="LITERATURE_SYNTHESIS_NOT_OBSERVATION").count();
 let raw=xs.iter().filter(|x|x.raw).count();
 let independent=xs.iter().filter(|x|x.independent).count();
 let mut roles:BTreeMap<&str,usize>=BTreeMap::new();
 for x in xs{for r in &x.roles{*roles.entry(r.as_str()).or_default()+=1;}}
 format!("corpus=SOURCE_ANNOTATED_LITERATURE_NOT_RAW_MEASUREMENTS\ncases={}\nunique_source_documents={}\nsource_reused_across_cases={}\noriginal_observations_described={}\nreanalysis_only_cases={}\nontology_schematic_cases={}\nliterature_review_cases={}\nraw_measurement_rows_verified={}\nindependent_physical_reference_verified={}\noperation_roles={}\nrole_edges={}\nreal_experiment_population_hub_distribution=HOLD\nontic_universality=HOLD\n",xs.len(),unique_sources,xs.len()-unique_sources,new_observation_described,reanalysis,illustration,reviews,raw,independent,roles.len(),xs.iter().map(|x|x.roles.len()).sum::<usize>())
}
fn main(){let xs=decode(CORPUS).expect("case annotations must parse");print!("{}",summary(&xs))}
#[cfg(test)]mod tests{use super::*;
 #[test]fn fixed_original_source_counts(){let xs=decode(CORPUS).unwrap();let s=summary(&xs);for x in ["cases=5","unique_source_documents=4","source_reused_across_cases=1","original_observations_described=2","reanalysis_only_cases=1","ontology_schematic_cases=1","literature_review_cases=1","raw_measurement_rows_verified=0","independent_physical_reference_verified=0","operation_roles=16","role_edges=16"]{assert!(s.contains(x),"missing {x}")}}
 #[test]fn no_actual_independence_from_doi(){let xs=decode(CORPUS).unwrap();assert!(xs.iter().all(|x|!x.independent));}
 #[test]fn reused_source_is_not_new_paper(){let xs=decode(CORPUS).unwrap();assert_eq!(xs.iter().filter(|x|x.source=="10.1098/rsif.2006.0134").count(),2);}
 #[test]fn cannot_assert_independence_without_raw(){let t="X|10.111/x|PUBLISHED_PRIMARY_REPORT|ORIGINAL_OBSERVATION_DESCRIBED|NO|YES|readout";assert!(decode(t).is_err());}
 #[test]fn no_schematic_independence(){let t="X|10.111/x|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|YES|YES|readout";assert!(decode(t).is_err());}
 #[test]fn source_not_missing(){let t="X|source|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|NO|NO|readout";assert!(decode(t).is_err());}
 #[test]fn duplicate_case_rejected(){let t="X|10.111/x|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|NO|NO|readout\nX|10.111/y|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|NO|NO|readout";assert!(decode(t).is_err());}
 #[test]fn strict_boolean(){let t="X|10.111/x|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|MAYBE|NO|readout";assert!(decode(t).is_err());}
 #[test]fn empty_role_rejected(){let t="X|10.111/x|ONTOLOGY_SCHEMATIC|ILLUSTRATION_NOT_OBSERVATION|NO|NO|";assert!(decode(t).is_err());}
 #[test]fn review_can_never_claim_raw(){let t="R|10.1146/review|LITERATURE_REVIEW|LITERATURE_SYNTHESIS_NOT_OBSERVATION|YES|NO|summary";assert!(decode(t).is_err());}
 #[test]fn review_can_never_claim_independent_reference(){let t="R|10.1146/review|LITERATURE_REVIEW|LITERATURE_SYNTHESIS_NOT_OBSERVATION|NO|YES|summary";assert!(decode(t).is_err());}
 #[test]fn review_must_not_be_called_primary_observation(){let t="R|10.1146/review|LITERATURE_REVIEW|ORIGINAL_OBSERVATION_DESCRIBED|NO|NO|summary";assert!(decode(t).is_err());}
 #[test]fn parser_deterministic(){let x=decode(CORPUS).unwrap();assert_eq!(summary(&x),summary(&decode(CORPUS).unwrap()));}
}