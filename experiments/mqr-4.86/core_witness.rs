use std::{env,fs,process};
fn two(s:&str)->Vec<&str>{s.split(',').collect()}
fn main(){
 let path=env::args().nth(1).unwrap_or_else(||"experiments/mqr-4.86/COURT-FREEZE.tsv".to_string());
 let body=fs::read_to_string(path).expect("freeze missing");
 let mut n=0usize;let mut pass=0usize;let mut rel_only=0usize;let mut positive=0usize;
 for (index,line) in body.lines().enumerate().skip(1){
   if line.trim().is_empty(){continue}
   let a:Vec<&str>=line.split('\t').collect();
   assert_eq!(a.len(),11,"line {} must have 11 columns",index+1);
   let present=two(a[3]);assert_eq!(present.len(),2);
   let r=present.iter().all(|&x|x=="1");
   let mut consistent=true;
   for i in 4..=8 {let x=two(a[i]);assert_eq!(x.len(),2,"invalid pair {}",a[0]);consistent &= x[0]==x[1];}
   let authority=r && consistent;
   let er=a[9]=="1";let ea=a[10]=="1";
   if r==er && authority==ea{pass+=1;}else{
      eprintln!("FAIL {}: rel={} expected {}, auth={} expected {}",a[0],r,er,authority,ea);
   }
   if r && !authority {rel_only+=1;}
   if authority {positive+=1;}
   n+=1;
 }
 println!("MQR486_CASES={n}");
 println!("MQR486_PASS={pass}");
 println!("MQR486_RELATION_NONLIFT={rel_only}");
 println!("MQR486_POSITIVE={positive}");
 if n!=10 || n!=pass || rel_only<1 || positive<1 {process::exit(1);}
 println!("MQR486_PROTOTYPE=PASS");
 println!("MQR486_SCIENTIFIC_VERDICT=UNADJUDICATED");
}