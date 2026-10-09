//! P1B postdiscovery diagnostic of visit-order detectability, using actual
//! USGS NAAMP 2001 original published field CSV. No simulated field data.
//! Model assumptions: stable site occupancy, no false detections, visit-order
//! homogeneous p_j among sites, conditional independence given occupancy.
//! Not a causal biological occupancy estimate nor a population CI.
use std::{collections::BTreeMap,env,error::Error,fs::File,io::{BufRead,BufReader,Write}};
type E=Box<dyn Error>;
fn bad(s:&str)->E{std::io::Error::new(std::io::ErrorKind::InvalidData,s).into()}
#[derive(Clone)]struct Site{key:String, y:Vec<bool>}
fn fnv(bytes:&[u8])->u64{let mut h=14695981039346656037u64;for b in bytes{h^=u64::from(*b);h=h.wrapping_mul(1099511628211)}h}
fn read(path:&str,label:&str)->Result<Vec<Site>,E>{
 let mut l=BufReader::new(File::open(path)?).lines();
 let h=l.next().ok_or_else(||bad("missing header"))??;
 let head=["RouteNumStopNum","JulianDate",label,"MinAfterSunset","Wind","Sky","Temperature"].join(",");
 if h.trim_end_matches('\r')!=head{return Err(bad("schema drift"));}
 let mut rows=BTreeMap::<String,Vec<(u16,bool)>>::new();
 let mut n=0;
 for line in l{
  let line=line?;
  if line.trim().is_empty(){continue;}
  let f:Vec<_>=line.trim_end_matches('\r').split(',').collect();
  if f.len()!=7{return Err(bad("7 columns required"));}
  let day=f[1].parse::<u16>()?;
  let call=f[2].parse::<u8>()?;
  if call>3{return Err(bad("call index >3"));}
  rows.entry(f[0].into()).or_default().push((day,call>0));n+=1;
 }
 if n!=337||rows.len()!=130{return Err(bad("original Delaware data count mismatch"));}
 let mut sites=Vec::new();
 for(key,mut visits)in rows{
  visits.sort_by_key(|v|v.0);
  for p in visits.windows(2){if p[0].0==p[1].0{return Err(bad("duplicate day"))}}
  if visits.len()>3||visits.is_empty(){return Err(bad("visit count out of bounds"));}
  sites.push(Site{key,y:visits.into_iter().map(|v|v.1).collect()});
 }
 Ok(sites)
}
fn stats(sites:&[Site])->([f64;3],[usize;3],[usize;3]){
 let(mut n,mut pos)=([0usize;3],[0usize;3]);
 for s in sites{for (j,&v)in s.y.iter().enumerate(){n[j]+=1;pos[j]+=v as usize;}}
 let mut q=[0.;3];for j in 0..3{q[j]=if n[j]==0{0.5}else{pos[j]as f64/n[j]as f64};}
 (q,n,pos)
}
fn site_ll(s:&Site,psi:f64,p:[f64;3])->f64{
 let mut pr=1.0;
 for (j,&v)in s.y.iter().enumerate(){pr*=if v{p[j]}else{1.0-p[j]};}
 if s.y.iter().any(|&v|v){(psi*pr).ln()}else{(1.0-psi+psi*pr).ln()}
}
fn ll(s:&[Site],psi:f64,p:[f64;3])->f64{s.iter().map(|v|site_ll(v,psi,p)).sum()}
fn occ_em(sites:&[Site])->Result<(f64,[f64;3],f64),E>{
 if sites.len()<10{return Err(bad("too few sites"))}
 let(q,n,_)=stats(sites);if n.contains(&0){return Err(bad("missing visit order"));}
 let mut best=(0.8,[0.5;3],f64::NEG_INFINITY);
 for start in [0.55f64,0.80,0.98]{
  let mut psi=start;let mut p=[0.;3];
  for j in 0..3{p[j]=(q[j]/psi).clamp(1e-8,1.0-1e-8);}
  for _ in 0..5000{
   let (mut wt,mut numer,mut denom)=(0.0,[0.0;3],[0.0;3]);
   for site in sites{
    let posterior=if site.y.iter().any(|&y|y){1.0}else{
     let zero=site.y.iter().enumerate().map(|(j,_)|1.0-p[j]).product::<f64>();
     let a=psi*zero;a/(1.0-psi+a)
    };
    wt+=posterior;
    for(j,&v)in site.y.iter().enumerate(){
      numer[j]+=v as usize as f64;
      denom[j]+=posterior;
    }
   }
   let next_psi=(wt/sites.len()as f64).clamp(1e-8,1.0-1e-8);
   let mut next_p=[0.;3];
   let mut delta=(next_psi-psi).abs();
   for j in 0..3{
     next_p[j]=(numer[j]/denom[j]).clamp(1e-8,1.0-1e-8);
     delta=delta.max((next_p[j]-p[j]).abs());
   }
   psi=next_psi;p=next_p;if delta<1e-12{break;}
  }
  let fit=ll(sites,psi,p);
  if fit>best.2{best=(psi,p,fit);}
 }
 Ok(best)
}
fn iid_occasion_ll(sites:&[Site],q:[f64;3])->f64{
 sites.iter().flat_map(|s|s.y.iter().enumerate()).map(|(j,&v)|{
  let p=q[j].clamp(1e-8,1.0-1e-8);if v{p.ln()}else{(1.0-p).ln()}
 }).sum()
}
fn run(label:&str,path:&str)->Result<String,E>{
 let sites=read(path,label)?;
 let mut train=Vec::new();let mut test=Vec::new();
 for s in sites.iter().cloned(){
  if fnv(format!("MQR-4.97-NAAMP-2001-SEALED-75-25|{}",s.key).as_bytes())%4==0{test.push(s)}
  else{train.push(s)}
 }
 if train.len()!=100||test.len()!=30{return Err(bad("split mismatch with frozen P1 original"));}
 let(q,n,pos)=stats(&sites);let(q_train,_,_)=stats(&train);
 let(psi,p,fit_ll)=occ_em(&train)?;
 let test_loss=-ll(&test,psi,p);
 let iid_loss=-iid_occasion_ll(&test,q_train);
 let mut x=String::new();
 x.push_str(&format!("MQR497_P1B_SPECIES={label} FULL_ORDER_COUNTS={n:?} DETECTED={pos:?} OBSERVED_Q={q:?}\n"));
 x.push_str(&format!("MQR497_P1B_TRAIN_OCCASION_Q={q_train:?} OCCASION_OCCUPANCY_PSI={psi:.10} P1={:.10} P2={:.10} P3={:.10} TRAIN_LOGLIK={fit_ll:.9}\n",p[0],p[1],p[2]));
 x.push_str(&format!("MQR497_P1B_SITE_HELDOUT=30 OCCASION_OCCUPANCY_NEGLOGLOSS={test_loss:.9} IID_OCCASION_Q_NEGLOGLOSS={iid_loss:.9}\n"));
 x.push_str("MQR497_P1B_POSTDISCOVERY_REAL_FIELD_OBSERVATION_HETEROGENEITY=PASS\n");
 x.push_str("MQR497_P1B_ECOLOGICAL_OCCUPANCY_AND_STATIONARITY=HOLD\n");
 Ok(x)
}
fn main()->Result<(),E>{
 let args=env::args().collect::<Vec<_>>();
 if args.len()!=4{return Err(bad("usage visit_order original-pcru original-pfer out.txt"))}
 let x=run("Pcru",&args[1])?+&run("Pfer",&args[2])?;
 File::create(&args[3])?.write_all(x.as_bytes())?;
 print!("{x}");Ok(())
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn allzero_is_mixture(){
  let s=Site{key:"z".into(),y:vec![false,false]};
  assert!((site_ll(&s,0.6,[0.5,0.25,0.9]).exp()-(0.4+0.6*0.5*0.75)).abs()<1e-12);
 }
 #[test]fn em_finite_on_toy(){
  let bits=[[true,false,false],[true,true,true],[false,false,false],[false,true,false],
   [true,false,true],[false,false,true],[false,false,false],[false,true,true],
   [true,false,false],[true,true,false]];
  let x=bits.iter().enumerate().map(|(i,b)|Site{key:i.to_string(),y:b.to_vec()}).collect::<Vec<_>>();
  let (psi,p,ll)=occ_em(&x).unwrap();
  assert!(psi>0.0&&psi<=1.0&&p.iter().all(|&v|v>0.0&&v<1.0)&&ll.is_finite());
 }
}
