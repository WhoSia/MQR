use std::collections::BTreeSet;
#[derive(Clone,Debug)]
struct State { live:BTreeSet<&'static str>, discharged:BTreeSet<&'static str>, receipts:BTreeSet<&'static str>, history:Vec<&'static str> }
fn initial()->State {State{live:["a"].into_iter().collect(),discharged:BTreeSet::new(),receipts:BTreeSet::new(),history:vec![]}}
fn keep(s:&mut State){s.history.push("keep");}
fn discharge(s:&mut State, receipt:bool){if receipt && s.live.remove("a"){s.discharged.insert("a");s.receipts.insert("a");s.history.push("verified_discharge");}}
fn erase(s:&mut State){s.live.remove("a");s.history.push("unwarranted_erasure");}
fn reopen(s:&mut State){if s.discharged.remove("a"){s.live.insert("a");s.receipts.remove("a");s.history.push("reopening");}}
fn valid(s:&State)->bool{
  let original:BTreeSet<&str>=["a"].into_iter().collect();
  s.live.is_disjoint(&s.discharged)
  && s.live.union(&s.discharged).copied().collect::<BTreeSet<&str>>()==original
  && s.discharged.is_subset(&s.receipts)
}
fn main(){
 let mut legal=initial();keep(&mut legal);discharge(&mut legal,true);
 let mut illegal=initial();erase(&mut illegal);keep(&mut illegal);
 let mut reopened=legal.clone();reopen(&mut reopened);
 let mut no_receipt=initial();discharge(&mut no_receipt,false);
 let tests=[
  ("legal",valid(&legal),true),
  ("erasure_rejected",valid(&illegal),false),
  ("reopening",valid(&reopened),true),
  ("unwarranted_discharge_blocked",valid(&no_receipt),true),
  ("same_visible_projection",legal.live==illegal.live,true),
  ("different_authority_certificate",legal.discharged!=illegal.discharged,true),
  ("reopening_restores_live",reopened.live.contains("a"),true),
  ("reopening_retains_history",reopened.history.contains(&"verified_discharge"),true),
 ];
 let mut passed=0;
 for (name,actual,expect) in tests{if actual==expect{passed+=1;} else{eprintln!("FAIL {name}");}}
 println!("MQR486_DEBT_CASES=8");
 println!("MQR486_DEBT_PASS={passed}");
 println!("MQR486_DEBT_SCIENTIFIC_NOVELTY=UNADJUDICATED");
 if passed!=8{std::process::exit(1);}
}