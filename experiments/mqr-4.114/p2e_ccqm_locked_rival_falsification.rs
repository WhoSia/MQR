//! MQR 4.114 P2-E: FROZEN pre-row threshold, original published CCQM 2018
//! institute summaries; no detector raw traces, no independence certificate.
//! Prereg: research/mqr_4114_p2e_pre_result_falsification_contract.md
//! Original BIPM report DOI 10.1088/0026-1394/55/1A/08012, pp. 9,12,17-20,33.
use std::collections::BTreeSet;
const SOURCE:&str=include_str!("fixtures/p2e_ccqm_published_lab_summaries.psv");
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
enum Kind{K11,K12}
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
enum Role{Participant,Anchor,Solicited,Late}
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
enum Method{GC,LC,Mixed}
#[derive(Clone,Debug)]
struct Row {
 project:Kind,role:Role,name:String,x:f64,u:f64,
 vial1:Option<f64>,vial2:Option<f64>,family:Method,
 calibrant:String,source_table:String,
}
fn decode(text:&str)->Result<Vec<Row>,String>{
 let mut seen=BTreeSet::new();let mut out=Vec::new();
 for (line_no,s) in text.lines().enumerate(){
  let s=s.trim();if s.is_empty()||s.starts_with('#'){continue}
  let v:Vec<_>=s.split('|').collect();
  if v.len()!=10{return Err(format!("wrong_columns_line_{}",line_no+1))}
  let p=match v[0]{"K11_GLUCOSE"=>Kind::K11,"K12_CREATININE"=>Kind::K12,_=>return Err("unrecognized_measurand".into())};
  let role=match v[1]{"PARTICIPANT"=>Role::Participant,"REFERENCE_ORIGINAL_ANCHOR"=>Role::Anchor,"REFERENCE_SOLICITED_AFTER_DISCORDANCE"=>Role::Solicited,"LATE_EXCLUDED"=>Role::Late,_=>return Err("unrecognized_role".into())};
  let family=match v[7]{"GC"=>Method::GC,"LC"=>Method::LC,"MIXED"=>Method::Mixed,_=>return Err("unknown_chromatography_family".into())};
  if !seen.insert((v[0].to_string(),v[2].to_string())){return Err("duplicate_institute_same_material".into())}
  let num=|a:&str|->Result<f64,String>{let t=a.parse::<f64>().map_err(|_|"unparseable_number")?;if !t.is_finite()||t<=0.0{return Err("invalid_positive_number".into())}Ok(t)};
  let opt=|a:&str|->Result<Option<f64>,String>{if a=="NA"{Ok(None)}else{Ok(Some(num(a)?))}};
  let (x,u,vial1,vial2)=(num(v[3])?,num(v[4])?,opt(v[5])?,opt(v[6])?);
  if role==Role::Participant {
    let(a,b)=match(vial1,vial2){(Some(a),Some(b))=>(a,b),_=>return Err("missing_participant_two_vials".into())};
    let rounding=if p==Kind::K11{0.00051}else{0.00501};
    if ((a+b)/2.0-x).abs()>rounding{return Err("published_vial_mean_mismatch".into())}
  }else if role==Role::Late {
    if p!=Kind::K12 || vial1.is_none() || vial2.is_some() {return Err("late_result_handling_invalid".into())}
  }else if vial1.is_some()||vial2.is_some(){return Err("unreported_reference_vials_cannot_be_invented".into())}
  match (p,role,v[9]) {
    (Kind::K11,Role::Participant,"T5_A3"|"T5_A2_A3")=>{},
    (Kind::K11,Role::Anchor | Role::Solicited,"T6_A3")=>{},
    (Kind::K12,Role::Participant | Role::Late,"T10")=>{},
    (Kind::K12,Role::Anchor | Role::Solicited,"T11")=>{},
    _=>return Err("source_table_role_mismatch".into())
  }
  if p==Kind::K11 && v[2]=="VNIIM" && v[8]!="CONFLICT_A2_917a_A3_917c"{return Err("reported_calibrant_conflict_erased".into())}
  out.push(Row{project:p,role,name:v[2].into(),x,u,vial1,vial2,family,calibrant:v[8].into(),source_table:v[9].into()});
 }
 if out.is_empty(){return Err("empty_source".into())}Ok(out)
}
#[derive(Clone,Copy,Debug)]
struct Heterogeneity{n:usize,mean:f64,q:f64,critical99:f64}
fn critical(df:usize)->Result<f64,String>{
 // Values of chi-square distribution 0.99 quantiles, frozen at alpha=.01
 // Standard distributional constants; n is dictated by source inclusion policy.
 match df {
   2=>Ok(9.21034037197618),
   6=>Ok(16.811893829770927),
   7=>Ok(18.475306906582357),
   8=>Ok(20.090235029663233),
   11=>Ok(24.724970311318277),
   _=>Err(format!("unregistered_degrees_of_freedom_{}",df))
 }
}
fn q_stat<'a>(items:impl Iterator<Item=&'a Row>)->Result<Heterogeneity,String>{
 let v:Vec<&Row>=items.collect();if v.len()<3 {return Err("too_few_labs".into())}
 let sw:f64=v.iter().map(|r|1.0/(r.u*r.u)).sum();
 let mean=v.iter().map(|r|r.x/(r.u*r.u)).sum::<f64>()/sw;
 let q=v.iter().map(|r| ((r.x-mean)/r.u).powi(2)).sum::<f64>();
 let critical99=critical(v.len()-1)?;
 Ok(Heterogeneity{n:v.len(),mean,q,critical99})
}
fn q_with_uncertainty_increment(rows:&[&Row],delta:f64)->f64{
 let w:Vec<f64>=rows.iter().map(|r|1.0/(r.u+delta).powi(2)).collect();
 let mu=rows.iter().zip(w.iter()).map(|(r,w)|r.x*w).sum::<f64>()/w.iter().sum::<f64>();
 rows.iter().zip(w.iter()).map(|(r,w)|(r.x-mu).powi(2)*w).sum()
}
fn p_even_chi_square(df:usize,q:f64)->Result<f64,String>{
 if df%2!=0||df<2{return Err("only_exact_even_df_supported".into())}
 let x=q/2.0;
 let mut sum=1.0;let mut term=1.0;
 for k in 1..df/2 {term*=x/(k as f64);sum+=term;}
 Ok((-x).exp()*sum)
}
fn family_contrast(rows:&[Row])->Result<(usize,usize,f64,f64),String>{
 let p:Vec<_>=rows.iter().filter(|r|r.project==Kind::K11 && r.role==Role::Participant).collect();
 let gc:Vec<_>=p.iter().filter(|r|r.family==Method::GC).map(|r|*r).collect();
 let lc:Vec<_>=p.iter().filter(|r|r.family==Method::LC).map(|r|*r).collect();
 let mixed=p.iter().filter(|r|r.family==Method::Mixed).count();
 if gc.len()<2||lc.len()<2 || gc.len()+lc.len()+mixed!=p.len(){return Err("nonindependent_family_splits".into())}
 let wmean=|xs:&Vec<&Row>|{
  let sw=xs.iter().map(|r|1.0/(r.u*r.u)).sum::<f64>();
  (xs.iter().map(|r|r.x/(r.u*r.u)).sum::<f64>()/sw,1.0/sw)
 };
 let (gm,gv)=wmean(&gc);let (lm,lv)=wmean(&lc);
 let z=(gm-lm)/(gv+lv).sqrt();
 Ok((gc.len(),lc.len(),gm-lm,z))
}
fn adjudicate()->Result<String,String>{
 let rows=decode(SOURCE)?;
 let p11:Vec<_>=rows.iter().filter(|r|r.project==Kind::K11&&r.role==Role::Participant).collect();
 let p12:Vec<_>=rows.iter().filter(|r|r.project==Kind::K12&&r.role==Role::Participant).collect();
 let anchors:Vec<_>=rows.iter().filter(|r|r.project==Kind::K11&&r.role!=Role::Participant).collect();
 if p11.len()!=9||p12.len()!=7||anchors.len()!=3||rows.iter().filter(|r|r.role==Role::Late).count()!=1{return Err("cohort_contract_changed".into())}
 if rows.iter().filter(|r|r.project==Kind::K11 && r.calibrant=="NIST_SRM_917c").count()!=7{return Err("common_calibrant_catalog_count_mismatch".into())}
 if p11.iter().filter(|r|r.family==Method::Mixed && r.name=="HSA").count()!=1 {return Err("hybrid_method_lab_provenance_mismatch".into())}
 if rows.iter().any(|r|r.source_table.is_empty()){return Err("missing_per_row_source".into())}
 let reported_vial_summaries=p11.iter().flat_map(|r|[r.vial1,r.vial2]).filter(|o|o.is_some()).count();
 let r=q_stat(p11.iter().copied())?;
 let r12=q_stat(p12.iter().copied())?;
 let ranchor=q_stat(anchors.iter().copied())?;
 let full=q_stat(rows.iter().filter(|r|r.project==Kind::K11))?;
 let p=p_even_chi_square(8,r.q)?;
 let ref_p=p_even_chi_square(2,ranchor.q)?;
 let optimistic=q_with_uncertainty_increment(&p11,0.0005);
 let flips=(0..p11.len()).filter(|&i|{
    let g=q_stat(p11.iter().enumerate().filter(|(k,_)|*k!=i).map(|(_,r)|*r)).unwrap();
    g.q<=g.critical99
 }).count();
 let (ng,nl,diff,z)=family_contrast(&rows)?;
 Ok(format!(
"source_type=PUBLISHED_INSTITUTE_VIAL_SUMMARIES_NOT_RAW_DETECTOR_TRACES\nsource_doi=10.1088/0026-1394/55/1A/08012\npreregistered_analysis=research/mqr_4114_p2e_pre_result_falsification_contract.md\nk11_original_participant_institutes={}\nk11_participant_vial_summary_count={}\nk11_q={:.6}\nk11_weighted_location_mg_g={:.6}\nk11_q99_cutoff={:.6}\nk11_nominal_p={:.8}\nk11_R0_status={}\nk11_rounding_sensitivity_q_plus_0_0005={:.6}\nk11_rounding_sensitivity_crosses_1pct_gate={}\nk11_leave_one_lab_out_non_rejections={}\nk11_gc_only_institutes={}\nk11_lc_only_institutes={}\nk11_mixed_route_institutes=1\nk11_gc_minus_lc_weighted_mg_g={:.6}\nk11_gc_lc_diagnostic_z={:.6}\nk11_family_contrast_threshold_3sigma_pass={}\nk11_known_917c_catalog_entries_including_followup={}\nk11_917a_917c_source_table_conflict=VNIIM\nk11_reference_labs_excluded_primary={}\nk11_reference_only_q={:.6}\nk11_reference_only_p={:.10}\nk11_all12_posthoc_q={:.6}\nk12_distinct_material_institutes={}\nk12_q={:.6}\nk12_q99_cutoff={:.6}\nk12_secondary_R0_status={}\nk12_CENAM_late_result=EXCLUDED_FROM_TEST\ncommon_mode_bias_identified=NO\ncalibrant_catalog_sharing_proves_actual_error_correlation=NO\nphysical_calibration_source_independence=HOLD\nreference_KCRV_is_external_witness=NO_CONSENSUS_FROM_CONTRIBUTORS\nprospective_material_perturbation=NOT_PERFORMED\nreal_lang_promotion=HOLD\n",
 r.n,reported_vial_summaries,r.q,r.mean,r.critical99,p,
 if r.q>r.critical99{"REJECT_CONDITIONAL"}else{"NOT_REJECT_CONDITIONAL"},
 optimistic,if (optimistic>r.critical99)!=(r.q>r.critical99){"YES"}else{"NO"},
 flips,ng,nl,diff,z,if z.abs()>3.0{"YES"}else{"NO"},
 7,anchors.len(),ranchor.q,ref_p,full.q,r12.n,r12.q,r12.critical99,
 if r12.q>r12.critical99{"REJECT_CONDITIONAL"}else{"NOT_REJECT_CONDITIONAL"},
 ))
}
fn main(){print!("{}",adjudicate().expect("frozen prereg source contract must parse"))}
#[cfg(test)] mod tests {
 use super::*;
 fn near(a:f64,b:f64,e:f64){assert!((a-b).abs()<e,"left {a} right {b} tol {e}")}
 #[test]fn exactly_one_institute_per_measurand(){let r=decode(SOURCE).unwrap();assert_eq!(r.len(),23);assert_eq!(r.iter().filter(|z|z.project==Kind::K11).count(),12);assert_eq!(r.iter().filter(|z|z.project==Kind::K12).count(),11);}
 #[test]fn real_9_lab_primary_with_reported_uncertainties(){let r=decode(SOURCE).unwrap();let f=q_stat(r.iter().filter(|z|z.project==Kind::K11 && z.role==Role::Participant)).unwrap();assert_eq!(f.n,9);near(f.mean,1.1570068137044,1e-9);near(f.q,22.120695702673,1e-8);near(f.critical99,20.090235029663,1e-10);assert!(f.q>f.critical99);}
 #[test]fn pvalue_exact_even_degrees(){near(p_even_chi_square(8,22.120695702673).unwrap(),0.0046971176618784,1e-10);}
 #[test]fn uncertainty_rounding_breaks_gate(){let r=decode(SOURCE).unwrap();let p=r.iter().filter(|z|z.project==Kind::K11 && z.role==Role::Participant).collect::<Vec<_>>();let q=q_with_uncertainty_increment(&p,0.0005);near(q,19.1403529684147,1e-8);assert!(q<critical(8).unwrap());}
 #[test]fn leave_one_out_nonrejection_count_three(){let r=decode(SOURCE).unwrap();let p=r.iter().filter(|z|z.project==Kind::K11 && z.role==Role::Participant).collect::<Vec<_>>();let mut flip=BTreeSet::new();for (i,row) in p.iter().enumerate(){let q=q_stat(p.iter().enumerate().filter(|(k,_)|*k!=i).map(|(_,z)|*z)).unwrap();if q.q<=q.critical99{flip.insert(row.name.clone());}}assert_eq!(flip,BTreeSet::from(["CENAM".to_string(),"INMETRO".to_string(),"NMIJ".to_string()]));}
 #[test]fn gc_vs_lc_is_not_three_sigma(){let r=decode(SOURCE).unwrap();let(ng,nl,d,z)=family_contrast(&r).unwrap();assert_eq!((ng,nl),(4,4));near(d,-0.00513885120777,1e-9);near(z,-1.18982787168,1e-8);assert!(z.abs()<3.0);}
 #[test]fn additional_labs_are_not_blinded_holdout(){let r=decode(SOURCE).unwrap();assert_eq!(r.iter().filter(|x|x.project==Kind::K11 && x.role==Role::Solicited).count(),2);assert_eq!(r.iter().filter(|x|x.project==Kind::K11 && x.role==Role::Anchor).count(),1);}
 #[test]fn anchor_challenge_significant_diagnostic_only(){let r=decode(SOURCE).unwrap();let x=q_stat(r.iter().filter(|z|z.project==Kind::K11&&z.role!=Role::Participant)).unwrap();near(x.q,29.05607995558,1e-8);assert!(x.q>critical(2).unwrap());}
 #[test]fn secondary_distinct_creatinine_material(){let r=decode(SOURCE).unwrap();let x=q_stat(r.iter().filter(|z|z.project==Kind::K12&&z.role==Role::Participant)).unwrap();near(x.q,13.086794110955,1e-8);assert!(x.q<x.critical99);}
 #[test]fn post_deadline_institution_excluded(){let r=decode(SOURCE).unwrap();assert_eq!(r.iter().filter(|z|z.project==Kind::K12&&z.role==Role::Late).count(),1);assert!(adjudicate().unwrap().contains("k12_CENAM_late_result=EXCLUDED_FROM_TEST"));}
 #[test]fn catalog_repeat_is_not_independent_calibration(){let r=decode(SOURCE).unwrap();assert_eq!(r.iter().filter(|z|z.project==Kind::K11&&z.calibrant=="NIST_SRM_917c").count(),7);assert!(adjudicate().unwrap().contains("calibrant_catalog_sharing_proves_actual_error_correlation=NO"));}
 #[test]fn one_institute_two_methods_not_two_observations(){let r=decode(SOURCE).unwrap();let hsa=r.iter().filter(|z|z.project==Kind::K11 && z.name=="HSA").collect::<Vec<_>>();assert_eq!(hsa.len(),1);assert_eq!(hsa[0].family,Method::Mixed);}
 #[test]fn uncorrected_conflict_flag_required(){let s=SOURCE.replace("CONFLICT_A2_917a_A3_917c","NIST_SRM_917c");assert!(decode(&s).is_err());}
 #[test]fn reject_double_counted_institute(){let line=SOURCE.lines().find(|l|l.starts_with("K11_GLUCOSE|PARTICIPANT|HSA|")).unwrap();let s=format!("{SOURCE}\n{line}\n");assert!(decode(&s).is_err());}
 #[test]fn reject_vial_as_independent_source(){let s=SOURCE.replace("1.155|1.156|MIXED","NA|NA|MIXED");assert!(decode(&s).is_err());}
 #[test]fn refuse_self_certified_physical_authority(){let s=adjudicate().unwrap();assert!(s.contains("common_mode_bias_identified=NO"));assert!(s.contains("physical_calibration_source_independence=HOLD"));assert!(s.contains("prospective_material_perturbation=NOT_PERFORMED"));}
 #[test]fn reject_wrong_report_section(){let s=SOURCE.replace("|T6_A3","|T5_A3");assert!(decode(&s).is_err());}
 #[test]fn original_shared_material_but_no_independent_glucose_value(){let r=decode(SOURCE).unwrap();let p=r.iter().filter(|r|r.project==Kind::K11&&r.role==Role::Participant).collect::<Vec<_>>();assert_eq!(p.len(),9);assert!(adjudicate().unwrap().contains("reference_KCRV_is_external_witness=NO_CONSENSUS_FROM_CONTRIBUTORS"));}
 #[test]fn reproducibility(){assert_eq!(adjudicate().unwrap(),adjudicate().unwrap());}
}
