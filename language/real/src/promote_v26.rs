use std::{env,fs};
fn main(){
 let p=env::args().nth(1).expect("packet");
 let s=fs::read_to_string(p).expect("read");
 let mut add="NONE"; let mut contact="NONE"; let mut repair="NONE";
 let mut simplify="NO"; let mut narrow="NO"; let mut localize="NO"; let mut scope="NO"; let mut optionv="NO";
 let mut live="YES"; let mut archive="NO"; let mut sealed="PASS"; let mut lineage="PASS"; let mut audit="PASS";
 for raw in s.lines(){
  let t:Vec<&str>=raw.split_whitespace().collect();
  if t.len()!=2 {continue}
  match t[0]{
   "add"=>add=t[1],"contact"=>contact=t[1],"repair"=>repair=t[1],
   "simplify"=>simplify=t[1],"narrow"=>narrow=t[1],"localize"=>localize=t[1],
   "scope"=>scope=t[1],"option"=>optionv=t[1],"live"=>live=t[1],"archive"=>archive=t[1],
   "sealed"=>sealed=t[1],"lineage"=>lineage=t[1],"audit"=>audit=t[1],_=>{}
  }
 }
 let governed=sealed=="PASS"&&lineage=="PASS"&&audit=="PASS";
 let material=add=="MATERIAL"||contact=="INDEPENDENT"||repair=="SCIENTIFIC"||
  simplify=="YES"||narrow=="YES"||localize=="YES"||scope=="YES"||optionv=="YES";
 let d=if !governed{"HOLD"} else if live=="YES"&&material{"PROMOTE"}
 else if live=="NO"&&archive=="YES"{"ARCHIVE"}
 else if add=="FORMAL"||contact=="DUPLICATE"||repair=="ENGINEERING"{"COMPRESS"}
 else{"REJECT"};
 println!("promote.decision={d}");
 println!("promote.prior_rule_necessary=REJECT");
 println!("promote.execution_universal_gate=REJECT");
 println!("promote.universal_meta_objective=NOT_EARNED");
 println!("promote.rpar=CANDIDATE");
 println!("promote.mcl=CANDIDATE");
 println!("promote.cdr=CANDIDATE");
}
