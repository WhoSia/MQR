//! MQR 4.114: finite graph census, not a census of experimental reality.
use std::collections::{BTreeMap,BTreeSet};
#[derive(Clone,Debug)]
struct Template { id:String, domain:String, roles:BTreeSet<String> }
fn parse(s:&str)->Result<Vec<Template>,String>{
 let mut out=Vec::new();let mut seen=BTreeSet::new();
 for (i,line) in s.lines().enumerate(){
  let l=line.trim();if l.is_empty()||l.starts_with('#'){continue}
  let f:Vec<_>=l.split('\t').collect();if f.len()!=3 {return Err(format!("bad_columns:{i}"))}
  if !seen.insert(f[0].to_string()){return Err(format!("duplicate_template:{i}"))}
  let mut roles=BTreeSet::new();for x in f[2].split(','){
   if !matches!(x,"observe"|"boundary"|"normalize"|"encode"|"compare"|"infer"|"decide"|"partition"|"snapshot"|"calibrate"|"iterate"){return Err(format!("unknown_role:{i}"))}
   if !roles.insert(x.to_string()){return Err(format!("duplicate_role:{i}"))}
  }
  if roles.is_empty()||f[1].is_empty(){return Err(format!("missing_metadata:{i}"))}
  out.push(Template{id:f[0].into(),domain:f[1].into(),roles});
 }
 if out.is_empty(){return Err("empty_graph".into())}Ok(out)
}
fn degrees(xs:&[Template])->BTreeMap<String,usize>{let mut deg=BTreeMap::new();for t in xs{for op in &t.roles{*deg.entry(op.clone()).or_insert(0)+=1}}deg}
fn split_normalize(xs:&[Template])->Vec<Template>{xs.iter().map(|x|{let mut t=x.clone();if t.roles.remove("normalize"){t.roles.insert(format!("normalize__{}",t.domain));}t}).collect()}
fn edge_total(xs:&[Template])->usize{xs.iter().map(|x|x.roles.len()).sum()}
fn report(s:&str)->Result<String,String>{
 let xs=parse(s)?;let degrees=degrees(&xs);let edge_count=edge_total(&xs);
 let sum:usize=degrees.values().sum();if sum!=edge_count{return Err("edge_conservation_failure".into())}
 let mut ranking:Vec<_>=degrees.iter().map(|(k,v)|(k.clone(),*v)).collect();ranking.sort_by(|a,b|b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
 let universals=ranking.iter().filter(|(_,n)|*n==xs.len()).count();
 let split=split_normalize(&xs);let after=degrees(&split);
 let after_universals=after.values().filter(|&&n|n==xs.len()).count();
 let domains=xs.iter().map(|x|x.domain.as_str()).collect::<BTreeSet<_>>().len();
 let top5:usize=ranking.iter().take(5).map(|(_,n)|n).sum();
 let ranked=ranking.into_iter().map(|(a,b)|format!("{a}:{b}")).collect::<Vec<_>>().join(",");
 Ok(format!("corpus=ILLUSTRATIVE_NOT_EMPIRICAL\ntemplates={}\ndomains={}\noperators={}\narrows={}\ncolumn_sums={}\ntop5_arrows={}\ntop5_share={}/{}\nuniversal_nodes_before={}\nuniversal_nodes_after_normalize_split={}\narrows_after_split={}\nranked={}\nphysical_instrument_warrant=HOLD\nindependent_evidence_count=NOT_IDENTIFIED\npower_law_claim=NOT_TESTABLE_WITH_THIS_CORPUS\n",xs.len(),domains,degrees.len(),edge_count,sum,top5,top5,edge_count,universals,after_universals,edge_total(&split),ranked))
}
fn main(){print!("{}",report(include_str!("fixtures/p1_abstract_graph.tsv")).expect("frozen corpus must parse"))}
#[cfg(test)]mod tests{use super::*;
 const EXAMPLE:&str=include_str!("fixtures/p1_abstract_graph.tsv");
 #[test]fn source_census(){let x=parse(EXAMPLE).unwrap();assert_eq!(x.len(),7);assert_eq!(edge_total(&x),51);assert_eq!(degrees(&x).values().sum::<usize>(),51);}
 #[test]fn top5_is_not_evidence(){let s=report(EXAMPLE).unwrap();assert!(s.contains("top5_share=35/51"));assert!(s.contains("physical_instrument_warrant=HOLD"));}
 #[test]fn operators_degrees(){let x=parse(EXAMPLE).unwrap();let d=degrees(&x);assert_eq!(d.len(),11);for k in ["observe","boundary","normalize","encode","decide"]{assert_eq!(d[k],7)}assert_eq!(d["infer"],6);assert_eq!(d["compare"],5);assert_eq!(d["calibrate"],2);}
 #[test]fn ontology_refinement_changes_universal_count_but_preserves_edges(){let x=parse(EXAMPLE).unwrap();let y=split_normalize(&x);assert_eq!(edge_total(&y),edge_total(&x));assert_eq!(degrees(&y).len(),17);assert_eq!(degrees(&x).values().filter(|&&n|n==7).count(),5);assert_eq!(degrees(&y).values().filter(|&&n|n==7).count(),4);}
 #[test]fn duplicate_template_is_not_new_evidence(){let x=parse(EXAMPLE).unwrap();let mut y=x.clone();let mut z=x[0].clone();z.id="A_COPY".to_string();y.push(z);assert_eq!(edge_total(&y),58);}
 #[test]fn reject_missing_metadata(){assert!(parse("A\ta\t\n").is_err());}
 #[test]fn reject_duplicate_role(){assert!(parse("A\ta\tobserve,observe\n").is_err());}
 #[test]fn reject_duplicate_template(){assert!(parse("A\ta\tobserve\nA\tb\tboundary\n").is_err());}
 #[test]fn reject_unknown_operator(){assert!(parse("A\ta\tnonexistent\n").is_err());}
 #[test]fn deterministic_output(){assert_eq!(report(EXAMPLE).unwrap(),report(EXAMPLE).unwrap());}
}