//! 4.97: real 2001 Delaware NAAMP Pseudacris field visits.
//! Source packages pinned at cran/unmarked git fc0c7119d86c53c9e48a4db10ff2170819cd245f.
//! Calling index 0 = not detected in that survey; 1–3 = heard.
//! Occupancy fit is a traditional conditional independent/detection model,
//! NOT established ecological truth, spatial population confidence or innovation.
use std::collections::{BTreeMap,BTreeSet};
use std::error::Error;
use std::fs::{self,File};
use std::io::{BufRead,BufReader,Write};
use std::path::Path;
type R<T>=Result<T,Box<dyn Error>>;
fn err(x:impl Into<String>)->Box<dyn Error>{std::io::Error::new(std::io::ErrorKind::InvalidData,x.into()).into()}
#[derive(Clone,Debug)]
struct Visit{site:String,day:u16,heard:bool,call:u8,after_sunset:f64,temperature:f64}
#[derive(Clone)]
struct Site{key:String,visits:Vec<Visit>}
fn parse(path:&str,species:&str)->R<(Vec<Site>,usize)>{
 let file=File::open(path)?;
 let mut lines=BufReader::new(file).lines();
 let head=lines.next().ok_or_else(||err("empty NAAMP data"))??;
 let h:Vec<&str>=head.trim_end_matches('\r').split(',').collect();
 let expected=["RouteNumStopNum","JulianDate",species,"MinAfterSunset","Wind","Sky","Temperature"];
 if h!=expected{return Err(err(format!("NAAMP real source wrong header: {h:?}")));}
 let mut bysite:BTreeMap<String,Vec<Visit>>=BTreeMap::new();
 let mut seen=BTreeSet::new();let mut nr=0;
 for l in lines{
  let l=l?;if l.trim().is_empty(){continue;}
  let f:Vec<&str>=l.trim_end_matches('\r').split(',').collect();
  if f.len()!=7{return Err(err("NAAMP malformed CSV field count"));}
  let site=f[0].to_owned();
  if site.is_empty(){return Err(err("missing original NAAMP site key"));}
  let day=f[1].parse::<u16>()?;
  if !(1..=366).contains(&day){return Err(err("Julian day out of range"));}
  let call=f[2].parse::<u8>()?;
  if call>3{return Err(err("auditory calling index outside documented 0..3"));}
  let after_sunset=f[3].parse::<f64>()?;
  let temperature=f[6].parse::<f64>()?;
  if !after_sunset.is_finite()||!temperature.is_finite(){return Err(err("nonfinite survey-level data"));}
  let key=(site.clone(),day);
  if !seen.insert(key){return Err(err("duplicate visit for one site/day, no independent extra replicate"));}
  bysite.entry(site.clone()).or_default().push(Visit{site,day,heard:call>0,call,after_sunset,temperature});nr+=1;
 }
 if nr<100||bysite.len()<10{return Err(err("NAAMP field source insufficient site-visits"));}
 let mut sites=Vec::new();
 for(key,mut visits)in bysite{
   visits.sort_by_key(|x|x.day);
   sites.push(Site{key,visits});
 }
 Ok((sites,nr))
}
fn log_prob(psi:f64,p:f64,site:&Site)->f64{
 let n=site.visits.len() as i32;
 let k=site.visits.iter().filter(|x|x.heard).count() as i32;
 if k>0 {psi.ln()+f64::from(k)*p.ln()+f64::from(n-k)*(1.0-p).ln()}
 else {(1.0-psi+psi*(1.0-p).powi(n)).ln()}
}
fn log_likelihood(x:&[Site],psi:f64,p:f64)->f64{
 x.iter().map(|r|log_prob(psi,p,r)).sum()
}
fn fit(x:&[Site])->R<(f64,f64,f64)>{
 if x.len()<4{return Err(err("not enough source sites"));}
 if x.iter().all(|s|s.visits.iter().all(|v|!v.heard)) {return Err(err("no detection support"));}
 let mut best=(0.5,0.5,f64::NEG_INFINITY);
 for a in 1..100{
  for b in 1..100{
   let psi=a as f64/100.0;let p=b as f64/100.0;
   let ll=log_likelihood(x,psi,p);
   if ll>best.2 {best=(psi,p,ll);}
  }
 }
 let mut step=0.005;
 for _ in 0..4{
   let center=best;
   for di in -5..=5{
    for dj in -5..=5{
      let psi=(center.0+f64::from(di)*step).clamp(1e-8,1.0-1e-8);
      let p=(center.1+f64::from(dj)*step).clamp(1e-8,1.0-1e-8);
      let ll=log_likelihood(x,psi,p);
      if ll>best.2{best=(psi,p,ll);}
    }
   }
   step/=5.0;
 }
 Ok(best)
}
fn fnv(bytes:&[u8])->u64{
 let mut h=14695981039346656037u64;
 for b in bytes {h^=u64::from(*b);h=h.wrapping_mul(1099511628211);}
 h
}
fn split(sites:&[Site])->(Vec<Site>,Vec<Site>){
 let mut train=Vec::new();let mut test=Vec::new();
 for x in sites{
   if fnv(format!("MQR-4.97-NAAMP-2001-SEALED-75-25|{}",x.key).as_bytes())%4==0{test.push(x.clone());}
   else{train.push(x.clone());}
 }
 (train,test)
}
fn naive_ever(x:&[Site])->f64{
 x.iter().filter(|s|s.visits.iter().any(|v|v.heard)).count() as f64/x.len() as f64
}
fn observed_visit_rate(x:&[Site])->f64{
 let (mut n,mut y)=(0usize,0usize);
 for site in x{for v in &site.visits{n+=1;y+=v.heard as usize;}}
 y as f64/n as f64
}
fn first_visit_rate(x:&[Site])->f64{
 x.iter().filter(|s|s.visits[0].heard).count() as f64/x.len() as f64
}
fn iid_loglik(x:&[Site],q:f64)->f64{
 let q=q.clamp(1e-8,1.0-1e-8);
 x.iter().map(|s|s.visits.iter().map(|v|if v.heard {q.ln()} else {(1.0-q).ln()}).sum::<f64>()).sum()
}
fn between_visit_switches(sites:&[Site])->(u64,u64,u64){
 let(mut absent_present,mut present_absent,mut visit_pairs)=(0,0,0);
 for site in sites{for vs in site.visits.windows(2){
  visit_pairs+=1;
  if !vs[0].heard&&vs[1].heard {absent_present+=1;}
  if vs[0].heard&&!vs[1].heard {present_absent+=1;}
 }}
 (absent_present,present_absent,visit_pairs)
}
fn run(species:&str,path:&str,out:&str)->R<String>{
 let(sites,rows)=parse(path,species)?;
 let (train,test)=split(&sites);
 if train.len()<8||test.len()<3{return Err(err("sealed train/test split lacks site support"));}
 let (psi,p,ll)=fit(&train)?;
 let (psi_full,p_full,ll_full)=fit(&sites)?;
 let naive_full=naive_ever(&sites);
 let first_rate=first_visit_rate(&train);
 let train_visit_rate=observed_visit_rate(&train);
 let n_test_visits:usize=test.iter().map(|s|s.visits.len()).sum();
 let model_test=log_likelihood(&test,psi,p);
 let iid_first=iid_loglik(&test,first_rate);
 let iid_all=iid_loglik(&test,train_visit_rate);
 let detected_sites=sites.iter().filter(|s|s.visits.iter().any(|v|v.heard)).count();
 let sites_ge2=sites.iter().filter(|s|s.visits.len()>=2).count();
 let (ap,pa,pairs)=between_visit_switches(&sites);
 let(mut min_visit,mut max_visit)=(usize::MAX,0);
 let(mut day_min,mut day_max)=(u16::MAX,0);
 let mut visit_hist=BTreeMap::<usize,usize>::new();
 let(mut total_heard,mut high_call,mut call_zero)=(0,0,0);
 let(mut avg_temp,sum_after,mut visit_count)=(0.0,0.0,0.0);
 let mut time_total=0.0;
 for s in &sites{
  min_visit=min_visit.min(s.visits.len());max_visit=max_visit.max(s.visits.len());
  *visit_hist.entry(s.visits.len()).or_default()+=1;
  for v in &s.visits {
    day_min=day_min.min(v.day);day_max=day_max.max(v.day);
    total_heard+=v.heard as usize;
    high_call+=(v.call>=2) as usize;
    call_zero+=(v.call==0) as usize;
    avg_temp+=v.temperature;time_total+=v.after_sunset;visit_count+=1.0;
    if v.site!=s.key{return Err(err("original site key corruption"));}
  }
 }
 let first_day_nonzero=sites.iter().filter(|s|s.visits[0].heard).count();
 let mut info=String::new();
 info.push_str(&format!("MQR497_SPECIES={species}\nMQR497_FROZEN_EXTERNAL_ORIGINAL_USGS_NAAMP_2001=TRUE\n"));
 info.push_str(&format!("MQR497_ORIGINAL_RECORDS={rows} SITES={} SITES_GE2_VISITS={sites_ge2} VISIT_MIN={min_visit} VISIT_MAX={max_visit} JULIAN_DAY_MIN={day_min} JULIAN_DAY_MAX={day_max}\n",sites.len()));
 info.push_str(&format!("MQR497_REVISIT_COUNTS={visit_hist:?}\n"));
 info.push_str(&format!("MQR497_EVER_HEARD_SITES={detected_sites} NAIVE_RATE={naive_full:.9} FIRST_DAY_HEARD_SITES={first_day_nonzero}\n"));
 info.push_str(&format!("MQR497_RECORDER_SURVEYS_POSITIVE={total_heard} NEGATIVE={call_zero} CALL_2_OR_3={high_call} MEAN_TEMPERATURE={:.5} MEAN_MINUTES_AFTER_SUNSET={:.5}\n",avg_temp/visit_count,time_total/visit_count));
 info.push_str(&format!("MQR497_WITHIN_SITE_TRANSITIONS_0_TO_1={ap} 1_TO_0={pa} ADJACENT_VISIT_PAIRS={pairs}\n"));
 info.push_str(&format!("MQR497_CONDITIONAL_HOMOGENEOUS_OCCUPANCY_FULL_PSI={psi_full:.9} P_DETECTION={p_full:.9} LOGLIK={ll_full:.8}\n"));
 info.push_str(&format!("MQR497_SOURCE_SPLIT_TRAIN_SITES={} TEST_SITES={} TEST_VISITS={n_test_visits} TRAIN_PSI={psi:.9} TRAIN_DETECTION_P={p:.9} TRAIN_LOGLIK={ll:.8}\n",train.len(),test.len()));
 info.push_str(&format!("MQR497_TEST_WHOLE_SITE_LOGLOSS_OCCUPANCY={:.8} TEST_IID_FIRST_VISIT={:.8} TEST_IID_TRAIN_VISIT_RATE={:.8} TRAIN_FIRST_VISIT_Q={:.8} TRAIN_ALL_VISIT_Q={:.8}\n",
    -model_test,-iid_first,-iid_all,first_rate,train_visit_rate));
 info.push_str("MQR497_ASSUMPTIONS=STABLE_SITE_OCCUPANCY|HOMOGENEOUS_DETECTION|NO_FALSE_POSITIVES|CONDITIONAL_VISIT_INDEPENDENCE\n");
 info.push_str("MQR497_NAAMP_REAL_SOURCE_REPEATED_DETECTION=PASS\nMQR497_ECOLOGICAL_OCCUPANCY_IDENTIFIED_UNCONDITIONALLY=HOLD\n");
 info.push_str("MQR497_NFI_SWEDEN_10YEAR_REVISITS_NOT_WITHIN_SEASON_REPLICATES=TRUE\nMQR497_SEROV_FINLAND_INDEPENDENT_TARGET_RISK=HOLD\n");
 fs::create_dir_all(out)?;
 let mut file=File::create(Path::new(out).join(format!("mqr497-{species}-field-verdict.txt")))?;
 file.write_all(info.as_bytes())?;
 let mut rec=File::create(Path::new(out).join(format!("mqr497-{species}-original-site-visit-contract.tsv")))?;
 writeln!(rec,"site_original\tjulian_day\tcall_index_original\trecorded_detection\tminutes_after_sunset\ttemperature\ttrain_or_test")?;
 for s in &sites{
  let role=if fnv(format!("MQR-4.97-NAAMP-2001-SEALED-75-25|{}",s.key).as_bytes())%4==0{"TEST"}else{"TRAIN"};
  for v in &s.visits{
   writeln!(rec,"{}\t{}\t{}\t{}\t{}\t{}\t{role}",s.key,v.day,v.call,v.heard as u8,v.after_sunset,v.temperature)?;
  }
 }
 Ok(info)
}
fn main()->R<()>{
 let args=std::env::args().collect::<Vec<_>>();
 if args.len()!=4{return Err(err("usage: mqr497-naamp ORIGINAL_pcru.csv ORIGINAL_pfer.csv OUT_DIR"));}
 let a=run("Pcru",&args[1],&args[3])?;
 let b=run("Pfer",&args[2],&args[3])?;
 print!("{a}\n{b}");
 Ok(())
}
#[cfg(test)]
mod tests{
 use super::*;
 fn s(bits:&[bool])->Site{
  Site{key:"test".into(),visits:bits.iter().enumerate().map(|(i,&b)|Visit{site:"test".into(),day:100+i as u16,heard:b,call:b as u8,after_sunset:32.0,temperature:13.0}).collect()}
 }
 #[test]fn zero_event_mixture_does_not_equal_known_absence(){
  let x=s(&[false,false,false]);
  let v=log_prob(.5,.5,&x).exp();
  assert!((v-(.5+.5*.125)).abs()<1e-12);
 }
 #[test]fn heard_event_requires_occupancy(){
  assert!(log_prob(1e-5,.8,&s(&[true,false])) < log_prob(.5,.8,&s(&[true,false])));
 }
 #[test]fn zero_and_detected_site_produce_nontrivial_fit(){
  let x=vec![s(&[false,false,false]),s(&[true,false,true]),s(&[true,true,true]),s(&[false,false,false])];
  let (psi,p,ll)=fit(&x).unwrap();
  assert!(psi>0.3&&p>0.3&&ll.is_finite());
 }
 #[test]fn stable_site_split_deterministic(){
  let x=vec![s(&[true]),Site{key:"abc".into(),visits:s(&[false]).visits}];
  let (a,b)=split(&x);assert_eq!(a.len()+b.len(),2);
 }
 #[test]fn repeat_transitions_are_observed_label_not_true_occupancy(){
  let x=vec![s(&[false,true,false])];
  assert_eq!(between_visit_switches(&x),(1,1,2));
 }
}
