use std::{env,fs};
fn main(){
 let p=env::args().nth(1).expect("packet");
 let s=fs::read_to_string(p).expect("read");
 let mut relation="INCOMPARABLE";
 let mut veto="OFF"; let mut fatal="NO";
 let mut scope="LOCAL"; let mut veto_scope="LOCAL";
 let mut horizon="MEDIUM"; let mut veto_horizon="MEDIUM";
 let mut duplicate="NO"; let mut common="NO";
 let mut sealed="PASS"; let mut lineage="PASS"; let mut audit="PASS";
 for raw in s.lines(){
  let t:Vec<&str>=raw.split_whitespace().collect();
  if t.is_empty(){continue}
  match t[0]{
   "relation" if t.len()==2 => relation=t[1],
   "veto" if t.len()==2 => veto=t[1],
   "fatal" if t.len()==2 => fatal=t[1],
   "scope" if t.len()==2 => scope=t[1],
   "veto_scope" if t.len()==2 => veto_scope=t[1],
   "horizon" if t.len()==2 => horizon=t[1],
   "veto_horizon" if t.len()==2 => veto_horizon=t[1],
   "duplicate_ancestry" if t.len()==2 => duplicate=t[1],
   "common_mode" if t.len()==2 => common=t[1],
   "sealed" if t.len()==2 => sealed=t[1],
   "lineage" if t.len()==2 => lineage=t[1],
   "audit" if t.len()==2 => audit=t[1],
   _=>{}
  }
 }
 let governed=sealed=="PASS"&&lineage=="PASS"&&audit=="PASS";
 let local_veto=veto=="ACTIVE"&&fatal=="YES"&&scope==veto_scope&&horizon==veto_horizon;
 let (decision,reason)=if !governed {("HOLD","GOVERNANCE")}
  else if duplicate=="YES"||common=="YES" {("HOLD","ANCESTRY_COLLAPSE_REQUIRED")}
  else if local_veto {("HOLD","LOCAL_VETO_ACTIVE")}
  else if relation=="DOMINATES" {("PROMOTE","LOCAL_DOMINANCE")}
  else if relation=="DEFEATS_UNDER_SCOPE" {("HOLD","LOCAL_DEFEAT")}
  else {("HOLD","INCOMPARABLE")};
 println!("promotion.relation={relation}");
 println!("promotion.veto={}",if local_veto{"ACTIVE"}else{"INACTIVE"});
 println!("promotion.decision={decision}");
 println!("promotion.reason={reason}");
 println!("promotion.scalar_aggregation=OFF");
 println!("promotion.weighted_sum_universal=REJECT");
 println!("promotion.lexicographic_universal=REJECT");
 println!("promotion.pareto_selector=REJECT");
 println!("promotion.universal_meta_utility=NOT_EARNED");
 println!("promotion.prcr=CANDIDATE");
 println!("promotion.rag=CANDIDATE");
 println!("promotion.hrs=CANDIDATE");
}
