//! MQR 4.95 P3b: full historical 2024 original GBIF TSV to Serov CSV
//! row-ordinal comparison, validated label transform and ambiguity diagnostics.
//! No Python, pandas, third-party Rust crates or guessed source IDs.
use std::{
 collections::{BTreeMap,BTreeSet},
 env,error::Error,fs::{self,File},
 io::{BufRead,BufReader,Write},path::Path
};
fn die(s:impl Into<String>)->Box<dyn Error>{
 std::io::Error::new(std::io::ErrorKind::InvalidData,s.into()).into()
}
fn csv(s:&str)->Vec<String>{
 s.trim_start_matches('\u{feff}').trim_end_matches('\r')
  .split(',').map(|t|t.trim().trim_matches('"').to_owned()).collect()
}
fn tsv(s:&str)->Vec<String>{
 s.trim_start_matches('\u{feff}').trim_end_matches('\r')
  .split('\t').map(ToOwned::to_owned).collect()
}
fn idx(h:&[String],key:&str)->Result<usize,Box<dyn Error>>{
 h.iter().position(|s|s==key).ok_or_else(||die(format!("missing input column {key}")))
}
fn norm(s:&str)->&str{if s==""||s=="NA"||s=="N/A" {"<MISSING>"}else{s}}
fn status(s:&str)->Result<u8,Box<dyn Error>>{
 match s{"ABSENT"=>Ok(0),"PRESENT"=>Ok(1),_=>Err(die(format!("unexpected original GBIF occurrenceStatus {s}")))}
}
#[derive(Default,Clone,Copy)]struct Stat{positive:usize,negative:usize}
impl Stat{
 fn add(&mut self,y:u8){if y==1{self.positive+=1;}else{self.negative+=1;}}
 fn total(&self)->usize{self.positive+self.negative}
}
fn run(csv_path:&str,gbif_path:&str,out:&str)->Result<(),Box<dyn Error>>{
 fs::create_dir_all(out)?;
 let mut source=BufReader::new(File::open(csv_path)?).lines();
 let mut gbif=BufReader::new(File::open(gbif_path)?).lines();
 let source_header=csv(&source.next().ok_or_else(||die("empty source CSV"))??);
 let gbif_header=tsv(&gbif.next().ok_or_else(||die("empty original GBIF TSV"))??);
 let (si_lat,si_lon,si_year,si_presence)=
   (idx(&source_header,"lat")?,idx(&source_header,"long")?,idx(&source_header,"year")?,idx(&source_header,"presence")?);
 let (gi_lat,gi_lon,gi_year,gi_status,gi_gbif,gi_dataset,gi_occ)=(
   idx(&gbif_header,"decimalLatitude")?,idx(&gbif_header,"decimalLongitude")?,
   idx(&gbif_header,"year")?,idx(&gbif_header,"occurrenceStatus")?,
   idx(&gbif_header,"gbifID")?,idx(&gbif_header,"datasetKey")?,
   idx(&gbif_header,"occurrenceID")?);
 let source_has_ids=["gbifID","occurrenceID","datasetKey","eventID"].iter()
   .any(|z|source_header.iter().any(|h|h==z));
 if source_has_ids{return Err(die("original source unexpectedly changed to include IDs; re-audit needed"));}
 let mut counts=BTreeMap::<String,Stat>::new();
 let mut same_key=BTreeMap::<String,usize>::new();
 let mut unique_ids=BTreeSet::<String>::new();
 let mut rows=0usize;
 let mut class_mismatches=0usize;
 let mut latlon_mismatches=0usize;
 let mut year_mismatches=0usize;
 let mut pair_missing=0usize;
 let mut totals=Stat::default();
 let mut mapping=File::create(Path::new(out).join("mqr495-GBIF-Original-2024-Ordinal-ID-to-Presence.tsv"))?;
 writeln!(mapping,"original_row_index\tgbifID\tdatasetKey\toccurrenceID\toriginalStatus\tserovPresence\tlat\tlon\tyear")?;
 loop{
   let (s,g)=match (source.next(),gbif.next()){
      (None,None)=>break,
      (Some(s),Some(g))=>(s?,g?),
      _=>return Err(die("Serov/GBIF row cardinality mismatch")),
   };
   rows+=1;
   let sf=csv(&s);
   let gf=tsv(&g);
   if sf.len()!=source_header.len() || gf.len()!=gbif_header.len(){
      return Err(die(format!("truncated source or GBIF row at ordinal {rows}: {} vs {}",sf.len(),gf.len())));
   }
   let y=sf[si_presence].parse::<u8>()?;
   if y>1{return Err(die("Serov nonbinary presence"));}
   let gbif_y=status(&gf[gi_status])?;
   if y!=gbif_y{class_mismatches+=1;}
   if norm(&sf[si_year])!=norm(&gf[gi_year]){year_mismatches+=1;}
   let (al,gl)=(norm(&sf[si_lat]),norm(&gf[gi_lat]));
   let (ao,go)=(norm(&sf[si_lon]),norm(&gf[gi_lon]));
   if al!=gl||ao!=go{latlon_mismatches+=1;}
   if al=="<MISSING>"||ao=="<MISSING>"{
      if al=="<MISSING>"&&gl=="<MISSING>"&&ao=="<MISSING>"&&go=="<MISSING>"{pair_missing+=1;}
   }
   if gf[gi_gbif].is_empty()||gf[gi_dataset].is_empty()||gf[gi_occ].is_empty() {
      return Err(die("missing GBIF stable source columns on original row"));
   }
   if !unique_ids.insert(gf[gi_gbif].clone()){return Err(die("duplicate 2024 original gbifID"));}
   totals.add(gbif_y);
   counts.entry(gf[gi_dataset].clone()).or_default().add(gbif_y);
   let collision_key=format!("{}|{}|{}|{}",
      norm(&sf[si_lat]),norm(&sf[si_lon]),norm(&sf[si_year]),y);
   *same_key.entry(collision_key).or_default()+=1;
   writeln!(mapping,"{rows}\t{}\t{}\t{}\t{}\t{y}\t{}\t{}\t{}",
      gf[gi_gbif],gf[gi_dataset],gf[gi_occ],gf[gi_status],
      sf[si_lat],sf[si_lon],sf[si_year])?;
 }
 if rows!=29543||totals.positive!=18377||totals.negative!=11166||counts.len()!=27 {
    return Err(die(format!("original data cardinality, source count or classes incorrect rows={rows}, pos={}, neg={}, sets={}",totals.positive,totals.negative,counts.len())));
 }
 if class_mismatches!=0||year_mismatches!=0||latlon_mismatches!=0 {
   return Err(die(format!("full original GBIF→Serov 1:1 ordinal mapping FAILED: class={class_mismatches},year={year_mismatches},coordinates={latlon_mismatches}")));
 }
 let ambiguous_groups=same_key.values().filter(|&&c|c>1).count();
 let ambiguous_rows:usize=same_key.values().filter(|&&c|c>1).sum();
 let max_key_collision=same_key.values().copied().max().unwrap_or(0);
 let top_spring="acf9b46d-e71a-4ccb-91d2-a021ffda4dd4";
 let top_kastikka="f2e389da-39c3-4f21-8d72-b7d574d924a9";
 if counts.get(top_spring).map(Stat::total)!=Some(14651)||
    counts.get(top_kastikka).map(Stat::total)!=Some(9686){
     return Err(die("original 2024 GBIF source-contributor populations do not match frozen metadata"));
 }
 let mut report=String::new();
 report.push_str("MQR495_P3B_SOURCE_ROOT=ORIGINAL_2024_GBIF_DOWNLOAD_0031144-240626123714530\n");
 report.push_str(&format!("MQR495_P3B_ORIGINAL_ROWS={rows} UNIQUE_GBIF_IDS={} SOURCE_DATASETS={}\n",unique_ids.len(),counts.len()));
 report.push_str(&format!("MQR495_P3B_ALL_ROW_ORDINAL_STATUS_LABEL_MISMATCHES={class_mismatches}\n"));
 report.push_str(&format!("MQR495_P3B_ALL_ROW_ORDINAL_YEAR_MISMATCHES={year_mismatches}\n"));
 report.push_str(&format!("MQR495_P3B_ALL_ROW_ORDINAL_NORMALIZED_COORDINATE_MISMATCHES={latlon_mismatches}\n"));
 report.push_str(&format!("MQR495_P3B_MISSING_COORD_PAIR_BOTH_SIDES={pair_missing}\n"));
 report.push_str(&format!("MQR495_P3B_ORIGINAL_2024_PRESENCE_ABSENT={} PRESENT={}\n",totals.negative,totals.positive));
 report.push_str(&format!("MQR495_P3B_NONIDENTIFIED_COORD_YEAR_LABEL_TIED_GROUPS={ambiguous_groups} ROWS={ambiguous_rows} MAX_GROUP={max_key_collision}\n"));
 report.push_str("MQR495_P3B_LABEL_RULE_VERIFIED_ON_FROZEN_ORDER=ABSENT_TO_0_PRESENT_TO_1\n");
 report.push_str("MQR495_P3B_GBIF_ROW_IDS_RESTORED_WITH_POSITIONAL_EVIDENCE=PASS\n");
 report.push_str("MQR495_P3B_AUTHOR_ORIGINAL_ETL_GENERATION_SCRIPT=NOT_PUBLISHED_IN_PINNED_REPO\n");
 report.push_str("MQR495_P3B_UNAMBIGUOUS_KEYED_LINEAGE_ORIGINAL_CSV=HOLD_NO_ID_COLUMN\n");
 let mut breakdown=File::create(Path::new(out).join("mqr495-GBIF-Original-2024-Presence-by-Dataset.tsv"))?;
 writeln!(breakdown,"datasetKey\tABSENT\tPRESENT\tTOTAL")?;
 for(k,v)in &counts{
   writeln!(breakdown,"{k}\t{}\t{}\t{}",v.negative,v.positive,v.total())?;
   if k==top_spring||k==top_kastikka {
      report.push_str(&format!("MQR495_P3B_DATASET_{k}_ORIGINAL_ABSENT={} PRESENT={} TOTAL={}\n",v.negative,v.positive,v.total()));
   }
 }
 report.push_str("MQR495_P3B_ORIGINAL_RAW_TO_SEROV_LABEL_AUDIT=PASS_BOUNDED\n");
 File::create(Path::new(out).join("mqr495-P3B-Original-2024-Ordinal-Lineage-Verdict.txt"))?
  .write_all(report.as_bytes())?;
 print!("{report}");
 Ok(())
}
fn main()->Result<(),Box<dyn Error>>{
 let v=env::args().collect::<Vec<_>>();
 if v.len()!=4 {return Err(die("usage gbif_p3b PINNED_SEROV_CSV ORIGINAL_2024_GBIF_TSV OUTPUT_DIR"));}
 run(&v[1],&v[2],&v[3])
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn status_map_is_explicit(){assert_eq!(status("ABSENT").unwrap(),0);assert_eq!(status("PRESENT").unwrap(),1);assert!(status("").is_err());}
 #[test]fn missing_coordinate_is_not_false_conflict(){assert_eq!(norm("NA"),norm(""));assert_ne!(norm("NA"),norm("60.4"));}
 #[test]fn csv_and_gbif_headers(){assert_eq!(csv(r#""lat","long","presence""#),vec!["lat","long","presence"]); assert_eq!(tsv("gbifID\tdatasetKey"),vec!["gbifID","datasetKey"]);}
}
