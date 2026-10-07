use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let dir=c[2]; let scope=b(c[3]); let rel=b(c[4]); let basis_content=b(c[5]);
 let basis_auth=b(c[6]); let refine=b(c[7]); let debt=b(c[8]); let depth=b(c[9]); let escape=b(c[10]);
 if escape{return "REOPEN_CROSS_LEVEL_ESCAPE";}
 if depth{return "DEPTH_LAUNDERING";}
 if dir=="NONE" || !scope || !rel{return "AUTHORITY_INCOMPARABLE";}
 if refine && !basis_content{return "REFINEMENT_WITHOUT_AUTHORITY_TRANSPORT";}
 if basis_content && !basis_auth{return "BASIS_AUTHORITY_NONINHERITANCE";}
 if !debt{return "RESIDUAL_DEBT_MIGRATION_FAILURE";}
 if dir=="BOTH"{return "AUTHORITY_EQUIVALENT_AT_SHARED_SCOPE";}
 if dir=="A2B"{return "A_AUTHORITY_DOMINATES_B";}
 if dir=="B2A"{return "B_AUTHORITY_DOMINATES_A";}
 "AUTHORITY_INCOMPARABLE"
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0; let mut ok=0;
 for(i,l) in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect(); assert_eq!(c.len(),12);
  let got=classify(&c); n+=1;
  if got==c[11]{ok+=1}else{eprintln!("{} expected={} got={}",c[0],c[11],got);}
 }
 println!("MQR483_CASES={n}");
 println!("MQR483_PASS={ok}");
 println!("MQR483_DEPTH_IMPLIES_AUTHORITY=REJECT");
 println!("MQR483_REFINEMENT_IMPLIES_AUTHORITY=REJECT");
 println!("MQR483_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}