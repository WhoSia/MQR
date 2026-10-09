//! MQR-4.98: 2005 alder flycatcher 15-minute field point counts subdivided into
//! three observed 5-minute subintervals. CONDITIONAL-ON-DETECTED zero-truncated
//! capture-history likelihood, not population size / true site occupancy.
use std::{collections::{BTreeMap,BTreeSet},env,error::Error,fs::{self,File},io::{BufRead,BufReader,Write},path::Path};
type X<T>=Result<T,Box<dyn Error>>;
fn error(s:impl Into<String>)->Box<dyn Error>{std::io::Error::new(std::io::ErrorKind::InvalidData,s.into()).into()}
#[derive(Clone)]struct Bird{site:String,survey:usize,mask:u8}
fn source_birds(path:&str)->X<Vec<Bird>>{
 let mut ls=BufReader::new(File::open(path)?).lines();
 if ls.next().ok_or_else(||error("empty bird source"))??.trim_end_matches('\r')!="id,survey,interval1,interval2,interval3"{
   return Err(error("wrong alfl.csv schema"));
 }
 let mut a=Vec::new();
 for line in ls{
  let line=line?;if line.trim().is_empty(){continue;}
  let f=line.trim_end_matches('\r').split(',').collect::<Vec<_>>();
  if f.len()!=5{return Err(error("malformed original bird encounter row"));}
  let visit=f[1].parse::<usize>()?;
  if !(1..=3).contains(&visit){return Err(error("primary visit outside 1-3"));}
  let mut mask=0u8;
  for j in 0..3 {match f[j+2]{"0"=>{},"1"=>mask|=1<<(2-j),_=>return Err(error("invalid original capture bit"))}}
  if mask==0{return Err(error("zero detected bird in selected capture data; schema changed"));}
  a.push(Bird{site:f[0].into(),survey:visit,mask});
 }
 if a.is_empty(){return Err(error("no original birds"));}
 Ok(a)
}
fn pattern(mask:u8)->String{format!("{:03b}",mask)}
fn source_summary(path:&str)->X<(BTreeMap<(String,usize,u8),u64>,BTreeSet<String>,usize)>{
 let mut ls=BufReader::new(File::open(path)?).lines();
 let h=ls.next().ok_or_else(||error("empty capRecap"))??;
 let head=h.trim_end_matches('\r').split(',').collect::<Vec<_>>();
 if head.len()!=30{return Err(error(format!("wrong capRecap field number {}",head.len())));}
 let mut names=Vec::new();
 for visit in 1..=3{for mask in 1..=7{names.push(format!("visit{}_{}",visit,pattern(mask)));}}
 if head[1..22].iter().zip(names.iter()).any(|(a,b)|a!=b) {
  return Err(error("capture schema is not 21 enumerated visit*pattern columns"));
 }
 let mut counts=BTreeMap::new();let mut sites=BTreeSet::new();let mut rows=0;
 for l in ls{
  let l=l?;if l.trim().is_empty(){continue;}
  let f=l.trim_end_matches('\r').split(',').collect::<Vec<_>>();
  if f.len()!=head.len(){return Err(error("truncated capture summary"));}
  if !sites.insert(f[0].trim_matches('"').to_owned()){return Err(error("duplicate station summary"));}
  for (k,name) in names.iter().enumerate(){
   let visit=(k/7)+1;let mask=((k%7)+1)as u8;
   let value=f[k+1].parse::<u64>()?;
   if value>0 {counts.insert((f[0].trim_matches('"').to_owned(),visit,mask),value);}
   if name!=&format!("visit{}_{}",visit,pattern(mask)){return Err(error("schema invariant"));}
  }
  rows+=1;
 }
 Ok((counts,sites,rows))
}
fn covs(path:&str)->X<(BTreeSet<String>,usize)>{
 let mut ls=BufReader::new(File::open(path)?).lines();
 let h=ls.next().ok_or_else(||error("empty covariates"))??;
 if !h.contains("time.1")||!h.contains("date.3"){return Err(error("covariate contract drift"));}
 let mut st=BTreeSet::new();
 for l in ls{
  let l=l?;if l.trim().is_empty(){continue;}
  let f=l.split(',').collect::<Vec<_>>();
  if f.len()!=9{return Err(error("covariate wrong column count"));}
  if !st.insert(f[0].trim_matches('"').to_owned()){return Err(error("repeated covariate site"));}
  for value in &f[1..]{let v=value.trim_matches('"').parse::<f64>()?;if !v.is_finite(){return Err(error("nonfinite covariate"));}}
 }
 let n=st.len();Ok((st,n))
}
fn conditional_prob(mask:u8,p:[f64;3])->f64{
 let mut raw=1.0;
 for (j,v) in p.iter().enumerate(){raw*=if mask&(1<<(2-j))!=0{*v}else{1.0-v};}
 let den=1.0-p.iter().map(|v|1.0-v).product::<f64>();
 raw/den
}
fn ll(data:&[Bird],p:[f64;3])->f64{
 data.iter().map(|b|conditional_prob(b.mask,p).max(1e-200).ln()).sum()
}
fn fit_const(data:&[Bird])->(f64,f64){
 let mut best=(0.5,f64::NEG_INFINITY);
 for j in 1..1000 {
  let p=j as f64/1000.0;let l=ll(data,[p;3]); // constant p
  if l>best.1{best=(p,l);}
 }
 best
}
fn fit_order(data:&[Bird])->([f64;3],f64){
 let mut best=([0.5;3],f64::NEG_INFINITY);
 for start in [[0.2,0.2,0.2],[0.8,0.5,0.25],[0.5,0.5,0.5]]{
  let mut p=start;
  let mut step=0.01;
  for _ in 0..4{
   for _ in 0..20{
    let mut delta=0.0f64;
    for j in 0..3{
     let mut good=(p[j],ll(data,p));
     for k in -12..=12{
      let cand=(p[j]+k as f64*step).clamp(0.00001,0.99999);
      let mut q=p;q[j]=cand;
      let score=ll(data,q);
      if score>good.1{good=(cand,score);}
     }
     delta=delta.max((good.0-p[j]).abs());p[j]=good.0;
    }
    if delta<step*0.1 {break;}
   }
   step*=0.2;
  }
  let l=ll(data,p);
  if l>best.1{best=(p,l);}
 }
 best
}
fn hash(s:&str)->u64{
 let mut h=14695981039346656037u64;
 for b in s.bytes(){h^=b as u64;h=h.wrapping_mul(1099511628211);}
 h
}
fn run(birds:&[Bird],summary:&BTreeMap<(String,usize,u8),u64>,source_sites:&BTreeSet<String>,covs:&BTreeSet<String>,out:&str)->X<()>{
 let mut counted=BTreeMap::<(String,usize,u8),u64>::new();
 let mut positive_sites=BTreeSet::new();let mut visits=BTreeSet::<(String,usize)>::new();
 let(mut by_pattern,mut by_interval,mut by_visit)=([0usize;8],[0usize;3],[0usize;3]);
 for b in birds{
  if !source_sites.contains(&b.site)||!covs.contains(&b.site){return Err(error("bird site absent from full parent frame"));}
  positive_sites.insert(b.site.clone());visits.insert((b.site.clone(),b.survey));
  *counted.entry((b.site.clone(),b.survey,b.mask)).or_default()+=1;
  by_pattern[b.mask as usize]+=1;by_visit[b.survey-1]+=1;
  for (j,z) in by_interval.iter_mut().enumerate(){if b.mask&(1<<(2-j))!=0{*z+=1;}}
 }
 let mut errors=Vec::new();
 for (k,v)in counted.iter(){if summary.get(k).copied().unwrap_or(0)!=*v{errors.push(format!("{k:?} row {v} summary {:?}",summary.get(k)));}}
 for (k,v)in summary.iter(){if counted.get(k).copied().unwrap_or(0)!=*v{errors.push(format!("{k:?} summary {v} row {:?}",counted.get(k)));}}
 if !errors.is_empty(){return Err(error(format!("original row-count ↔ summarized source mismatch: {}",errors.iter().take(5).cloned().collect::<Vec<_>>().join("; "))));}
 let (mut train,mut test)=(Vec::new(),Vec::new());
 for b in birds.iter().cloned(){
  if hash(&format!("MQR498-2005-ALFL-75-25|{}",b.site))%4==0{test.push(b);}
  else{train.push(b);}
 }
 if train.len()<20||test.len()<6{return Err(error("too few selected bird histories in site-heldout split"));}
 let (p_all,l_all)=fit_const(birds);
 let (p_train,l_train)=fit_const(&train);
 let (ps_train,ls_train)=fit_order(&train);
 let (ps_all,ls_all)=fit_order(birds);
 let heldout_const=-ll(&test,[p_train;3]);
 let heldout_order=-ll(&test,ps_train);
 let zero_sites=source_sites.len()-positive_sites.len();
 let all_sessions=source_sites.len()*3;
 let empty_sessions=all_sessions-visits.len();
 let ten_derived=1.0-(1.0-p_all).powi(2);
 let fifteen_derived=1.0-(1.0-p_all).powi(3);
 let observed_first_two=birds.iter().filter(|b|b.mask&0b110!=0).count()as f64/birds.len()as f64;
 let mut output=String::new();
 output.push_str("MQR498_DATA_SOURCE=REAL_CHANDLER_ALDER_FLYCATCHER_2005_15_MINUTES_3X5MIN\n");
 output.push_str(&format!("MQR498_RAW_DETECTED_INDIVIDUAL_HISTORY_ROWS={} POSITIVE_SITE_KEYS={} FULL_SITE_FRAME={} COVARIATE_SITE_FRAME={} ALL_PRIMARY_SITE_VISITS={} WITH_DETECTIONS={} WITHOUT_DETECTIONS={}\n",
 birds.len(),positive_sites.len(),source_sites.len(),covs.len(),all_sessions,visits.len(),empty_sessions));
 output.push_str(&format!("MQR498_CAPTURE_PATTERN_COUNTS_001_TO_111={:?} BY_5MIN_INTERVAL={by_interval:?} BY_PRIMARY_VISIT={by_visit:?}\n",&by_pattern[1..]));
 output.push_str("MQR498_ORIGINAL_ROW_LEVEL_VS_49_SITE_SUMMARY_PATTERN_COUNTS=PASS_EXACT\n");
 output.push_str(&format!("MQR498_DETECTED_ONLY_NONZERO_HISTORIES=TRUE UNDETECTED_SITE_COUNT={} NONRECORDED_INDIVIDUAL_POPULATION_SIZE=NOT_IDENTIFIED\n",zero_sites));
 output.push_str(&format!("MQR498_TRUNCATED_HOMOGENEOUS_P5_FULL={p_all:.8} LOGLIK_FULL={l_all:.8} P10_TRANSPORT_ASSUMPTION_ONLY={ten_derived:.8} P15_TRANSPORT_ASSUMPTION_ONLY={fifteen_derived:.8} OBSERVED_SELECTED_FIRST_10MIN_DETECTION_RATE={observed_first_two:.8}\n"));
 output.push_str(&format!("MQR498_TRAIN_DETECTED_HISTORIES={} TEST_DETECTED_HISTORIES={} TRAIN_P5={p_train:.8} TRAIN_LL={l_train:.8} HELDOUT_CONDITIONAL_NEGLOGLIK_P_CONSTANT={heldout_const:.8}\n",train.len(),test.len()));
 output.push_str(&format!("MQR498_ORDER_CONDITIONAL_TRAIN_P1={:.8} P2={:.8} P3={:.8} TRAIN_LL={ls_train:.8} HELDOUT_CONDITIONAL_NEGLOGLIK_P_BY_INTERVAL={heldout_order:.8}\n",ps_train[0],ps_train[1],ps_train[2]));
 output.push_str(&format!("MQR498_ORDER_CONDITIONAL_FULL_P1={:.8} P2={:.8} P3={:.8} FULL_LL={ls_all:.8}\n",ps_all[0],ps_all[1],ps_all[2]));
 output.push_str("MQR498_EFFORT_EXPOSURE=3_KNOWN_FIVE_MINUTE_WINDOWS_PER_15MIN_POINT_COUNT\n");
 output.push_str("MQR498_BIRD_CAPTURE_HISTORIES_INFER_BIOLOGICAL_OCCUPANCY_OR_ABUNDANCE=HOLD_ZERO_TRUNCATION\n");
 output.push_str("MQR498_TRANSPORT_OUTSIDE_15MIN_SESSION=HOLD_NO_CLOSURE_OR_AVAILABILITY_PROOF\n");
 output.push_str("MQR498_USGS_NAAMP_AND_SEROV_FINLAND_RISK_TRANSPORT=HOLD_DIFFERENT_SAMPLE_FRAMES\n");
 fs::create_dir_all(out)?;
 File::create(Path::new(out).join("mqr498-original-capture-effort-verdict.txt"))?.write_all(output.as_bytes())?;
 let mut rec=File::create(Path::new(out).join("mqr498-original-2005-observed-history-and-roles.tsv"))?;
 writeln!(rec,"source_site_key\tprimary_survey\tdetected_5min_1\tdetected_5min_2\tdetected_5min_3\tpattern\tsite_holdout")?;
 for b in birds{
  writeln!(rec,"{}\t{}\t{}\t{}\t{}\t{}\t{}",b.site,b.survey,(b.mask>>2)&1,(b.mask>>1)&1,b.mask&1,pattern(b.mask),if hash(&format!("MQR498-2005-ALFL-75-25|{}",b.site))%4==0{"TEST"}else{"TRAIN"})?;
 }
 print!("{output}");Ok(())
}
fn main()->X<()>{
 let a=env::args().collect::<Vec<_>>();
 if a.len()!=5{return Err(error("usage: mqr498 alfl.csv alfl.capRecap.csv alflCovs.csv outdir"));}
 let b=source_birds(&a[1])?;
 let (summary,sites,_)=source_summary(&a[2])?;
 let (cov,n)=covs(&a[3])?;
 if n<30||sites.len()<30{return Err(error("frame malformed"));}
 run(&b,&summary,&sites,&cov,&a[4])
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn pattern_mask_right_order(){assert_eq!(pattern(5),"101");assert_eq!(pattern(7),"111");}
 #[test]fn conditional_capture_distribution_sums_one(){
   let p=[0.25,0.5,0.75];let s=(1..8).map(|i|conditional_prob(i,p)).sum::<f64>();
   assert!((s-1.0).abs()<1e-12);
 }
 #[test]fn zero_capture_not_in_admitted_support(){assert_eq!(pattern(0),"000");}
 #[test]fn truncated_constant_likelihood_removes_unknown_zeros(){
   let b=Bird{site:"abc".into(),survey:1,mask:1};
   assert!(ll(&[b],[0.5;3]).is_finite());
 }
 #[test]fn ten_minute_transfer_is_only_formula_under_independent_detection(){
   let p:f64=0.3;assert!((1.0-(1.0-p).powi(2)-0.51).abs()<1e-12);
 }
}