use std::{collections::HashMap,fs,process};
fn yn(x:&str)->bool{match x{"YES"=>true,"NO"=>false,_=>{eprintln!("bad bool {x}");process::exit(2)}}}
fn verdict(r:&HashMap<String,String>)->&'static str{
 let sa=yn(&r["shared_authority_ancestry"]); let si=yn(&r["shared_infrastructure"]);
 let wc=yn(&r["independent_world_contact"]); let post=yn(&r["postoutcome_tuned"]);
 let nov=yn(&r["novel"]); let rel=yn(&r["claim_relevant"]); let bounded=yn(&r["bounded_search"]);
 let found=yn(&r["counterexample_found"]);
 if post && rel {return "NO_PROSPECTIVE_AUTHORITY"}
 if nov && !rel {return "NOVEL_BUT_IRRELEVANT"}
 if bounded && !found {return "NO_CLOSURE_FROM_SEARCH_FAILURE"}
 if sa {return "COMMON_MODE_HOLD"}
 if wc && found {return "AUTHORITY_UPGRADED"}
 if si && !sa && !wc && !nov && rel {return "BENIGN_SHARED_INFRASTRUCTURE"}
 if !sa && rel && found {
   if wc {return "INDEPENDENT_CHALLENGE"} else {return "ROUTE_DIVERSE_LOCAL"}
 }
 "HOLD"
}
fn main(){
 let src=fs::read_to_string("experiments/mqr-4.75/COURT-FREEZE.tsv").unwrap();
 let mut it=src.lines(); let h:Vec<&str>=it.next().unwrap().split('\t').collect();
 let mut n=0;let mut bad=0;
 let mut cm=false;let mut benign=false;let mut bounded=false;let mut up=false;let mut post=false;let mut irrelevant=false;
 for line in it{
  if line.trim().is_empty(){continue}
  let v:Vec<&str>=line.split('\t').collect(); if v.len()!=h.len(){eprintln!("bad row");process::exit(2)}
  let mut r=HashMap::new(); for(i,k)in h.iter().enumerate(){r.insert((*k).to_string(),v[i].to_string());}
  let got=verdict(&r);n+=1;if got!=r["expected"]{bad+=1;eprintln!("{}: {} != {}",r["case_id"],got,r["expected"])}
  match r["case_id"].as_str(){
   "N1"=>cm=got=="COMMON_MODE_HOLD",
   "C1"=>benign=got=="BENIGN_SHARED_INFRASTRUCTURE",
   "M1"=>bounded=got=="NO_CLOSURE_FROM_SEARCH_FAILURE",
   "N5"=>up=got=="AUTHORITY_UPGRADED",
   "N6"=>post=got=="NO_PROSPECTIVE_AUTHORITY",
   "N7"=>irrelevant=got=="NOVEL_BUT_IRRELEVANT",
   _=>{}
  }
 }
 let ok=bad==0&&n==13&&cm&&benign&&bounded&&up&&post&&irrelevant;
 println!("MQR475_CHALLENGE_COURT={}",if ok{"PASS"}else{"FAIL"});
 println!("MQR475_CASES={n}");
 println!("MQR475_COMMON_MODE_BLOCKS_INDEPENDENCE={}",if cm{"YES"}else{"NO"});
 println!("MQR475_SHARED_INFRASTRUCTURE_CAN_BE_BENIGN={}",if benign{"YES"}else{"NO"});
 println!("MQR475_BOUNDED_SEARCH_NO_CLOSURE={}",if bounded{"YES"}else{"NO"});
 println!("MQR475_EXTERNAL_CONTACT_CAN_UPGRADE={}",if up{"YES"}else{"NO"});
 println!("MQR475_POSTOUTCOME_NO_PROSPECTIVE_AUTHORITY={}",if post{"YES"}else{"NO"});
 println!("MQR475_NOVELTY_NOT_RELEVANCE={}",if irrelevant{"YES"}else{"NO"});
 if !ok{process::exit(1)}
}
