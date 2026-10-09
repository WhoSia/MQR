//! Independent Rust source-count verification; no ecological likelihood inference.
use std::{collections::{HashMap,HashSet},env,fs,path::Path};
fn load(p:&Path)->(Vec<String>,Vec<Vec<String>>){
 let s=fs::read_to_string(p).expect("Missing CSV");
 let mut lines=s.lines();
 let h=lines.next().unwrap().split(';').map(str::to_owned).collect::<Vec<_>>();
 let r=lines.filter(|l|!l.trim().is_empty()).map(|l|l.split(';').map(str::to_owned).collect::<Vec<_>>()).collect::<Vec<_>>();
 assert!(r.iter().all(|a|a.len()==h.len()),"Unexpected delimiter or schema");
 (h,r)
}
fn val<'a>(r:&'a [String],h:&[String],k:&str)->&'a str {
 &r[h.iter().position(|v|v==k).expect("Missing column")]
}
fn main(){
 let a=env::args().nth(1).expect("Usage: source_audit EXTRACT_DIR");
 let p=Path::new(&a);
 let (dh,ds)=load(&p.join("amro_obsdetection.csv"));
 let (sh,sites)=load(&p.join("amro_sitecovs_simplified.csv"));
 let (eh,ebird)=load(&p.join("amro_ebird_simplified.csv"));
 let ids:HashSet<_>=sites.iter().map(|r|val(r,&sh,"Checklist_ID")).collect();
 let mut counts:HashMap<&str,usize>=HashMap::new();
 let mut within=0;let mut orphan=0;
 for r in &ds{
  let id=val(r,&dh,"Checklist_ID");*counts.entry(id).or_default()+=1;
  let d:f64=val(r,&dh,"Distance").parse().expect("Invalid distance");
  if d<=300.0{within+=1;}
  if !ids.contains(id){orphan+=1;assert_eq!(val(r,&dh,"Year"),"11");}
 }
 let sumsite:usize=sites.iter().map(|r|{
  let n:usize=val(r,&sh,"Count").parse().unwrap();
  assert_eq!(n,*counts.get(val(r,&sh,"Checklist_ID")).unwrap_or(&0));
  n
 }).sum();
 let sumeb:usize=ebird.iter().map(|r|val(r,&eh,"count").parse::<usize>().unwrap()).sum();
 assert_eq!((ds.len(),within,sites.len(),sumsite,orphan,ebird.len(),sumeb),
 (2090,2020,2912,2076,14,1059,819));
 println!("RUST_ORIGINAL_PASS {} {} {} {} {} {} {}",ds.len(),within,sites.len(),sumsite,orphan,ebird.len(),sumeb);
}
