//! REALREPRESENT 0.43-CANDIDATE: physically keyed representation permutation audit.
//! Reads P1-J independently attested historical CSV from a source-pinned prior CI.
//! No raw OSL luminescence bytes are added to the repository.
//! A bijection of observed public physical grain IDs is NOT the full author cohort.
#![forbid(unsafe_code)]
use std::{collections::BTreeSet,env,fs};
#[derive(Debug,Clone)]
struct Row{sample:String,pos:u16,grain:u16,source:usize,jags:usize,modern:usize,signature:String}
fn cells(line:&str)->Vec<String>{
 line.splitn(7,',').map(|s|s.trim().trim_matches('"').to_string()).collect()
}
fn read(text:&str)->Result<Vec<Row>,String>{
 let mut it=text.lines();
 if cells(it.next().ok_or("empty")?)!=["sample","position","grain","csv_row",
             "jags_global_row","modern_matched_row","signal_sig"]{
  return Err("not actual P1-J crosswalk schema".into());
 }
 let mut rows=Vec::new();
 for (i,line) in it.enumerate(){
  if line.trim().is_empty(){return Err(format!("empty CSV row {}",i+2));}
  let v=cells(line);
  if v.len()!=7{return Err(format!("wrong width row {}",i+2));}
  let parse=|j:usize|v[j].parse::<usize>().map_err(|_|format!("bad integer row {}",i+2));
  let pos=parse(1)?;let grain=parse(2)?;
  if pos==0||grain==0||pos>u16::MAX as usize||grain>u16::MAX as usize{
     return Err("invalid physical disc/grain ID".into());
  }
  if v[6].len()<20||!v[6].contains('|'){return Err("source signal row signature missing".into());}
  rows.push(Row{
    sample:v[0].clone(),pos:pos as u16,grain:grain as u16,
    source:parse(3)?,jags:parse(4)?,modern:parse(5)?,signature:v[6].clone()
  });
 }
 Ok(rows)
}
fn permutation(s:&[Row],sample:&str,offset:usize)->Result<usize,String>{
 if s.len()!=49||s.iter().any(|r|r.sample!=sample){return Err(format!("{sample}: not exactly 49 original public keys"));}
 let mut key=BTreeSet::new();let mut old=BTreeSet::new();
 let mut modern=BTreeSet::new();let mut sig=BTreeSet::new();let mut displaced=0;
 for r in s {
   if !key.insert((r.pos,r.grain))||!old.insert(r.source)||!modern.insert(r.modern)
      ||!sig.insert(r.signature.clone()){return Err(format!("{sample}: non-injective physical/source/modern/signature"));}
   if r.jags!=r.source+offset {return Err(format!("{sample}: source→JAGS position is not proven"));}
   if r.modern!=r.source{displaced+=1;}
 }
 if old!=BTreeSet::from_iter(1..=49)||modern!=BTreeSet::from_iter(1..=49){
    return Err(format!("{sample}: missing/duplicate rows in representation permutation"));
 }
 Ok(displaced)
}
fn verify(rows:&[Row])->Result<(usize,usize),String>{
 if rows.len()!=98{return Err("source does not have exactly 49+49 public selected grains".into());}
 let a=permutation(&rows[..49],"FER1",0)?;
 let b=permutation(&rows[49..],"FER3",49)?;
 if a!=21||b!=49 {return Err("unexpected original-source→modern row displacement; possible source drift".into());}
 Ok((a,b))
}
fn main(){
 let f=env::args().nth(1).unwrap_or_else(||{
  eprintln!("usage: real-v43-crosswalk <P1J original crosswalk CSV>");std::process::exit(2);
 });
 let t=fs::read_to_string(f).unwrap_or_else(|e|{eprintln!("READ_ERROR: {e}");std::process::exit(2)});
 let res=read(&t).and_then(|r|verify(&r));
 match res{
  Ok((a,b))=>print!("representation.source=P1J_2021_OFFICIAL_PUBLIC_49_EACH\n\
   representation.physical_grain_key_bijection=PASS_FINITE_98\n\
   representation.FER1_observed_keys=49\nrepresentation.FER3_observed_keys=49\n\
   representation.FER1_row_displacement={a}\nrepresentation.FER3_row_displacement={b}\n\
   representation.JAGS_SOURCE_ROW_MAPPING=PASS\n\
   representation.INDEX_EQUALS_PHYSICAL_ID=FALSE\n\
   representation.SOURCE_SIGNAL_VALUE_MATCH_REQUIRES_UPSTREAM_P1J_RECEIPT=YES\n\
   representation.FULL_AUTHOR_COHORT=HOLD\nrepresentation.WORLD_AUTHORITY=HOLD\n"),
  Err(e)=>{eprintln!("REJECTED_REAL_CROSSWALK: {e}");std::process::exit(2);}
 }
}
#[cfg(test)]
mod tests{
 use super::*;
 fn stub(s:&str,r:usize,m:usize)->Row{Row{sample:s.into(),pos:r as u16,grain:(r+10)as u16,
 source:r,jags:r+if s=="FER3"{49}else{0},modern:m,signature:format!("{r}|{}|source",r+1)}}
 fn identity()->Vec<Row>{let mut r=Vec::new();for s in ["FER1","FER3"]{for i in 1..=49{r.push(stub(s,i,i));}}r}
 #[test]fn full_public_crosswalk_does_not_justify_default_identity(){
    let r=identity();assert!(verify(&r).is_err());
 }
 #[test]fn expected_permutation_recovers_pair_keys(){
  let mut r=identity();for (i,j) in (0..21).zip((0..21).rev()){r[i].modern=j+1;} // creates permutation in a prefix
  for i in 49..98{r[i].modern=(i-49+1)%49+1;}
  assert_eq!(permutation(&r[..49],"FER1",0).unwrap(),20);
  assert_eq!(permutation(&r[49..],"FER3",49).unwrap(),49);
 }
 #[test]fn duplicate_physical_key_rejected(){let mut r=identity();r[1].grain=r[0].grain;r[1].pos=r[0].pos;assert!(permutation(&r[..49],"FER1",0).is_err());}
 #[test]fn duplicate_modern_row_rejected(){let mut r=identity();r[1].modern=r[0].modern;assert!(permutation(&r[..49],"FER1",0).is_err());}
 #[test]fn jags_source_mismatch_rejected(){let mut r=identity();r[1].jags=0;assert!(permutation(&r[..49],"FER1",0).is_err());}
 #[test]fn source_row_drift_rejected(){let mut r=identity();r[1].source=3;assert!(permutation(&r[..49],"FER1",0).is_err());}
 #[test]fn wrong_total_must_fail(){let r=identity();assert!(verify(&r[..97]).is_err());}
 #[test]fn real_schema_csv_parses(){let h="\"sample\",\"position\",\"grain\",\"csv_row\",\"jags_global_row\",\"modern_matched_row\",\"signal_sig\"\n\"FER1\",1,19,1,1,1,\"1|2|abcdeabcdefabcde\"\n";let r=read(h).unwrap();assert_eq!(r[0].sample,"FER1");assert_eq!(r[0].grain,19);}
}
