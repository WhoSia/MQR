//! P3: transcription and conditional set identification, not an estimator of biological truth.
//! Source: Diefenbach et al. 2007, Auk 124(1), Table 1, DOI 10.1093/auk/124.1.96.
//! The CSV is *transcribed published aggregate data*, NOT the authors' individual behavior log.
use mqr499_identifiability::sharp_detection_bounds;
const TABLE: &str = include_str!("../../sources/p3_diefenbach_published_table1.csv");
#[derive(Debug)]
struct Record { species:String, protocol:String, minutes:f64, availability:f64, lo:f64, hi:f64, periods:usize }
fn close(x:f64,y:f64) { assert!((x-y).abs()<1e-10,"{x} != {y}"); }
fn parse() -> Vec<Record> {
 let mut lines=TABLE.lines();
 assert_eq!(lines.next().unwrap(),"species,protocol,minutes,availability,ci_lower,ci_upper,monitoring_periods");
 let mut v=Vec::new();
 for line in lines.filter(|s|!s.trim().is_empty()) {
  let c=line.split(',').collect::<Vec<_>>();assert_eq!(c.len(),7);
  let r=Record{species:c[0].to_string(),protocol:c[1].to_string(),minutes:c[2].parse().unwrap(),
   availability:c[3].parse().unwrap(),lo:c[4].parse().unwrap(),hi:c[5].parse().unwrap(),periods:c[6].parse().unwrap()};
  assert!(r.lo>0.0 && r.lo<=r.availability && r.availability<=r.hi && r.hi<=1.0);
  v.push(r);
 }
 assert_eq!(v.len(),10);
 v
}
fn entry<'a>(v:&'a [Record],s:&str,p:&str,t:f64)->&'a Record{
 v.iter().find(|x|x.species==s&&x.protocol==p&&(x.minutes-t).abs()<1e-9).unwrap()
}
fn probe(v:&[Record]){
 for (s,n) in [("HenslowSparrow",54),("GrasshopperSparrow",80)]{
  for &p in &["song_only","song_and_visible"]{
   let a=entry(v,s,p,5.0);let b=entry(v,s,p,10.0);
   assert_eq!(a.periods,n);assert_eq!(b.periods,n);
   assert!(a.availability<=b.availability); // nested time-window event at fixed source
  }
  for &t in &[5.0,10.0]{
   let sing=entry(v,s,"song_only",t);let both=entry(v,s,"song_and_visible",t);
   assert!(both.availability<=sing.availability); // inclusion of source-defined events
  }
  let a5=entry(v,s,"song_only",5.0).availability;
  let a10=entry(v,s,"song_only",10.0).availability;
  let poisson_10=1.0-(1.0-a5).powi(2);
  println!("SOURCE_AGGREGATE {} 5min_song={:.3} 10min_song={:.3} hypothetical_stationary_poisson_10={:.6} point_difference={:.6} (DESCRIPTIVE; NO REJECTION)",s,a5,a10,poisson_10,a10-poisson_10);
 }
 // Hypothetical q=0.2, NOT a measured fraction for Henslow or Oregon robins.
 // Conditional on transfer of Henslow 5min singing+visible availability interval [.34,.49]:
 let (lo,hi)=sharp_detection_bounds(0.2,0.34,0.49).unwrap();
 close(lo,20.0/49.0);close(hi,10.0/17.0);
 // Attainability witnesses: a=U and a=L yield same q=ap.
 close(0.49*lo,0.2);close(0.34*hi,0.2);
 // Without defensible species/protocol transfer, target a free in [0,1], so p in [q,1].
 let (no_bridge_lo,no_bridge_hi)=sharp_detection_bounds(0.2,0.0,1.0).unwrap();
 close(no_bridge_lo,0.2);close(no_bridge_hi,1.0);
 assert_eq!(sharp_detection_bounds(0.6,0.34,0.49),None);
 // Averages cannot be combined naively in heterogeneous populations:
 let mean_ap=(0.2*0.8+0.8*0.2)/2.0;
 let product_mean=((0.2+0.8)/2.0)*((0.8+0.2)/2.0);
 close(mean_ap,0.16);close(product_mean,0.25);
 println!("CONDITIONAL_SHARP_BOUND q_hypothetical=0.200 a_source=[0.34,0.49] p_if_valid_same_protocol_transport=[{lo:.9},{hi:.9}] p_no_bridge=[{no_bridge_lo:.9},{no_bridge_hi:.9}]");
 println!("HETEROGENEITY_COUNTEREXAMPLE mean(a*p)={mean_ap:.3} mean(a)*mean(p)={product_mean:.3}");
 println!("P3_SCOPE_PASS: transcribed aggregates + conditional sharp-set witness; no new field truth, no population transport.");
}
fn main(){probe(&parse());}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn published_values_and_event_inclusion(){let rows=parse();probe(&rows);}
 #[test]fn no_valid_target_denominator_in_existing_ds_count(){assert_eq!(sharp_detection_bounds(0.6,0.34,0.49),None);}
}
