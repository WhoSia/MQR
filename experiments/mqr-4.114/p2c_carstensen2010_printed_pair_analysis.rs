//! MQR-4.114 P2-C: source-published decimal pair sufficient moments.
//! This program verifies formulae from tabulated published values, not calibration history.
//! Source: Bendix Carstensen, Statistics in Medicine 29 (2010) 401-410,
//! doi:10.1002/sim.3769; original Drive ID 1G4kq_UOCs5F_BgdyWringOXg8WKtAUt6.
use std::collections::BTreeSet;
const FIXTURE: &str=include_str!("fixtures/p2c_carstensen2010_printed_pair_moments.psv");
#[derive(Debug,Clone,Copy,PartialEq,Eq)]
enum Orientation { AMinusB, BMinusA }
impl Orientation { fn sign(self)->f64{if self==Self::AMinusB {1.0}else{-1.0}} }
#[derive(Debug,Clone)]
struct PrintedMoments {
 id:String, n:usize, scale:f64, sum_a:f64,sum_b:f64,
 sum_a2:f64,sum_b2:f64,sum_ab:f64,orientation:Orientation,
 previous_source:String, source_doi:String, ancestry:String,
}
#[derive(Debug,Clone)]
struct Fit {
 intercept:f64,slope:f64,residual_sd:f64, mean_difference:f64,
 naive_intercept:f64,naive_slope:f64,
 b_given_a_intercept:f64,b_given_a_slope:f64,b_given_a_sd:f64,
 a_given_b_intercept:f64,a_given_b_slope:f64,a_given_b_sd:f64,
}
fn parse(src:&str)->Result<Vec<PrintedMoments>,String>{
 let mut found=BTreeSet::new();let mut out=Vec::new();
 for (i,line) in src.lines().enumerate(){
  let s=line.trim();if s.is_empty()||s.starts_with('#'){continue}
  let f:Vec<_>=s.split('|').collect();if f.len()!=12{return Err(format!("wrong_columns_line_{}",i+1))}
  if !found.insert(f[0].to_string()){return Err("duplicate_dataset".into())}
  let parse_usize=|x:&str|->Result<usize,String>{x.parse::<usize>().map_err(|_|"bad_count".into())};
  let parse_u=|x:&str|->Result<f64,String>{x.parse::<u64>().map(|v|v as f64).map_err(|_|"bad_nonnegative_integer_moment".into())};
  let n=parse_usize(f[1])?;if n<4{return Err("too_few_pairs".into())}
  let scale=parse_u(f[2])?;if scale<1.0{return Err("bad_scale".into())}
  let v:Vec<_>=f[3..8].iter().map(|s|parse_u(s)).collect::<Result<_,_>>()?;
  let orientation=match f[8]{"A_MINUS_B"=>Orientation::AMinusB,"B_MINUS_A"=>Orientation::BMinusA,_=>return Err("bad_orientation".into())};
  if f[9]!="10.1002/sim.3769"{return Err("wrong_paper_doi".into())}
  if f[10].is_empty(){return Err("missing_prior_origin".into())}
  if f[11]!="UNVERIFIED"{return Err("self_certified_ancestry_rejected".into())}
  out.push(PrintedMoments{
   id:f[0].into(),n,scale,sum_a:v[0],sum_b:v[1],sum_a2:v[2],sum_b2:v[3],sum_ab:v[4],
   orientation,source_doi:f[9].into(),previous_source:f[10].into(),ancestry:f[11].into(),
  });
 }
 if out.is_empty(){return Err("no_source_moments".into())}Ok(out)
}
fn fit(m:&PrintedMoments)->Result<Fit,String>{
 let n=m.n as f64;let k=m.scale;let sign=m.orientation.sign();
 // For x=(method A+method B)/2, y=sign*(method A-method B):
 let sx=(m.sum_a+m.sum_b)/(2.0*k);
 let sy=sign*(m.sum_a-m.sum_b)/k;
 let sxx=(m.sum_a2+2.0*m.sum_ab+m.sum_b2)/(4.0*k*k)-sx*sx/n;
 let syy=(m.sum_a2-2.0*m.sum_ab+m.sum_b2)/(k*k)-sy*sy/n;
 let sxy=sign*(m.sum_a2-m.sum_b2)/(2.0*k*k)-sx*sy/n;
 if !sxx.is_finite()||!syy.is_finite()||!sxy.is_finite()||sxx<=0.0||syy<=0.0{return Err("invalid_source_variances".into())}
 let slope=sxy/sxx;
 let intercept=sy/n-slope*sx/n;
 let rss=syy-sxy*sxy/sxx;
 if !rss.is_finite()||rss<=0.0{return Err("invalid_regression_residual".into())}
 let residual_sd=(rss/(n-2.0)).sqrt();
 // Canonical A-B parameter orientation, regardless of printed regression sign.
 let a=sign*intercept;let b=sign*slope;
 let p=1.0+b/2.0;let q=1.0-b/2.0;
 if p.abs()<1e-12||q.abs()<1e-12{return Err("noninvertible_comparison_mapping".into())}
 Ok(Fit{
  intercept,slope,residual_sd,mean_difference:sy/n,
  naive_intercept:-a,naive_slope:1.0-b,
  b_given_a_intercept:-a/p,b_given_a_slope:q/p,b_given_a_sd:residual_sd/p.abs(),
  a_given_b_intercept:a/q,a_given_b_slope:p/q,a_given_b_sd:residual_sd/q.abs(),
 })
}
fn report(src:&str)->Result<String,String>{
 let list=parse(src)?;let mut out=String::new();
 out.push_str("evidence_type=PUBLISHED_PRINTED_PAIRS_DERIVED_MOMENTS\npublisher_source_pdf_id=1G4kq_UOCs5F_BgdyWringOXg8WKtAUt6\n");
 let mut total=0;
 for m in &list{
  let f=fit(m)?;total+=m.n;
  out.push_str(&format!(
   "{}.n={}\n{}.source_parent={}\n{}.intercept={:.6}\n{}.slope={:.6}\n{}.residual_sd={:.6}\n{}.B_given_A_intercept={:.6}\n{}.B_given_A_slope={:.6}\n{}.A_given_B_intercept={:.6}\n{}.A_given_B_slope={:.6}\n",
   m.id,m.n,m.id,m.previous_source,m.id,f.intercept,m.id,f.slope,m.id,f.residual_sd,
   m.id,f.b_given_a_intercept,m.id,f.b_given_a_slope,m.id,f.a_given_b_intercept,m.id,f.a_given_b_slope,
  ));
 }
 out.push_str(&format!("source_printed_paired_rows={}\nunique_published_tables={}\noriginal_lab_trace_independently_inspected=NO\nplasma_normal_reference_schemes_are_independent_instruments=NO\nmethod_specific_error_variances_from_single_pairs=NOT_IDENTIFIED\nprediction_interval_is_independent_physical_calibration=NO\nexternal_reference_ancestry=HOLD\nreal_language_promotion=HOLD\n",total,list.len()));
 Ok(out)
}
fn main(){print!("{}",report(FIXTURE).expect("frozen published summary"))}
#[cfg(test)]mod tests{
 use super::*;
 fn get(id:&str)->(PrintedMoments,Fit){let m=parse(FIXTURE).unwrap().into_iter().find(|m|m.id==id).unwrap();let f=fit(&m).unwrap();(m,f)}
 fn near(a:f64,b:f64,tol:f64){assert!((a-b).abs()<tol,"{a} not within {tol} of {b}")}
 #[test]fn distinct_published_tables(){let x=parse(FIXTURE).unwrap();assert_eq!(x.len(),2);assert_eq!(x[0].n,46);assert_eq!(x[1].n,99);assert_eq!(x.iter().map(|m|m.n).sum::<usize>(),145);}
 #[test]fn original_glucose_coefficients(){let(m,f)=get("GLUCOSE_TABLE_I");assert_eq!(m.source_doi,"10.1002/sim.3769");near(f.intercept,-2.2438346111,1e-6);near(f.slope,0.3346317885,1e-7);near(f.residual_sd,1.0837457786,1e-6);}
 #[test]fn original_plasma_normal_coefficients(){let(_,f)=get("PLASMA_NORMAL_TABLE_II");near(f.intercept,-0.9084134296,1e-6);near(f.slope,-0.0889979738,1e-7);near(f.residual_sd,2.0373923643,1e-6);}
 #[test]fn glucose_directional_conversion(){let(_,f)=get("GLUCOSE_TABLE_I");near(f.b_given_a_intercept,1.9222171326,1e-6);near(f.b_given_a_slope,0.7133322778,1e-7);near(2.0*f.b_given_a_sd,1.8568166234,1e-5);near(f.a_given_b_intercept,-2.6947009023,1e-6);near(f.a_given_b_slope,1.4018712333,1e-7);near(2.0*f.a_given_b_sd,2.6030178098,1e-5);}
 #[test]fn plasma_normal_directional_conversion(){let(_,f)=get("PLASMA_NORMAL_TABLE_II");near(f.b_given_a_intercept,-0.8697121212,1e-6);near(f.b_given_a_slope,0.9147936236,1e-7);near(1.96*f.b_given_a_sd,3.8231621897,2e-5);near(f.a_given_b_intercept,0.9507194834,1e-6);near(f.a_given_b_slope,1.0931427310,1e-7);near(1.96*f.a_given_b_sd,4.1780569570,2e-5);}
 #[test]fn model_conversion_reciprocal(){for m in parse(FIXTURE).unwrap(){let f=fit(&m).unwrap();near(f.a_given_b_slope*f.b_given_a_slope,1.0,1e-12);near(f.a_given_b_intercept+f.a_given_b_slope*f.b_given_a_intercept,0.0,1e-12);}}
 #[test]fn naive_plug_in_mean_is_not_inverse(){let(_,f)=get("GLUCOSE_TABLE_I");assert!((f.naive_slope-f.b_given_a_slope).abs()>0.04);}
 #[test]fn normalized_volume_is_not_second_lab_instrument(){let(m,_)=get("PLASMA_NORMAL_TABLE_II");assert_eq!(m.previous_source,"BLAND_ALTMAN_1999_REUSED_ALTERNATE_NORMAL_REFERENCES");assert_eq!(m.ancestry,"UNVERIFIED");}
 #[test]fn no_ancestry_self_assertion(){let s=FIXTURE.replace("|UNVERIFIED","|INDEPENDENT_VERIFIED");assert!(parse(&s).is_err());}
 #[test]fn reject_wrong_source_doi(){let s=FIXTURE.replace("10.1002/sim.3769|CARSTENSEN","10.1002/NOT_THE_PAPER|CARSTENSEN");assert!(parse(&s).is_err());}
 #[test]fn reject_negative_moment(){let s=FIXTURE.replace("|36768|","|-36768|");assert!(parse(&s).is_err());}
 #[test]fn reject_bad_orientation(){let s=FIXTURE.replace("A_MINUS_B","MAYBE");assert!(parse(&s).is_err());}
 #[test]fn reject_duplicated_source_table(){let x=FIXTURE.lines().find(|x|x.starts_with("GLUCOSE_TABLE_I|")).unwrap();let s=format!("{FIXTURE}\n{x}");assert!(parse(&s).is_err());}
 #[test]fn zero_raw_lab_evidence_claim(){let s=report(FIXTURE).unwrap();assert!(s.contains("original_lab_trace_independently_inspected=NO"));assert!(s.contains("external_reference_ancestry=HOLD"));}
 #[test]fn source_table_status_counts(){let s=report(FIXTURE).unwrap();assert!(s.contains("source_printed_paired_rows=145"));assert!(s.contains("unique_published_tables=2"));}
}
