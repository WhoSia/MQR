//! MQR-4.95 P2 — Live public GBIF parent data and external field-study witness.
//! Public API JSON is decoded to a documented TSV transport envelope by jq;
//! all scientific claim-admission checks are Rust std-only. No Python/serde.
//! The Swedish field observations establish a distinct binary survey source,
//! NOT a target label for the fixed Finnish 64-site study.
use std::{collections::{BTreeMap,BTreeSet},env,error::Error,fs::{self,File},io::{BufRead,BufReader,Write},path::Path};

const PARENT:&str="0031144-240626123714530";
const ORIGINAL_DOI:&str="10.15468/dl.7jsjca";
const FINBIF_PARENT_UUID:&str="df12ca07-f133-4550-ab3b-fde13f0e76ba";
const SWEDEN_MAIN:&str="d59ccafb-251e-46cf-9319-37b58d88e7c5";
const SWEDEN_DISCONTINUED:&str="e1a32bea-73df-4b9b-af2e-6e148ab2641b";

fn err(s:impl Into<String>)->Box<dyn Error> { std::io::Error::new(std::io::ErrorKind::InvalidData,s.into()).into() }
fn lines(path:&str)->Result<Vec<Vec<String>>,Box<dyn Error>>{
    let mut out=Vec::new();
    for line in BufReader::new(File::open(path)?).lines(){
        let line=line?;
        if line.trim().is_empty(){continue;}
        out.push(line.split('\t').map(ToString::to_string).collect());
    }
    Ok(out)
}
fn cells<'a>(xs:&'a [String],n:usize,table:&str)->Result<&'a [String],Box<dyn Error>>{
    if xs.len()!=n {return Err(err(format!("{table}: expected {n} fields, got {}",xs.len())));}
    Ok(xs)
}
#[derive(Debug,Clone,Copy,PartialEq,Eq)]
enum Admission { ReusedParent, DistinctBinaryFieldSurvey, SameTaxonDifferentTargetFrame, NoObservedBinary, Unattested }
#[derive(Debug)]
struct Survey<'a>{dataset:&'a str,region:&'a str,scientific_name:&'a str,observed_present:bool,observed_absent:bool}
fn source_admit(candidate:&Survey<'_>, parent_datasets:&BTreeSet<String>)->Admission{
    if parent_datasets.contains(candidate.dataset){return Admission::ReusedParent;}
    if candidate.scientific_name!="Anemone nemorosa L."{return Admission::Unattested;}
    if !(candidate.observed_present&&candidate.observed_absent){return Admission::NoObservedBinary;}
    if candidate.region!="FI" {return Admission::SameTaxonDifferentTargetFrame;}
    // Even a Finnish dataset absent from the exact 27-source parent still requires
    // underlying record IDs and matched site/effort; never grant direct labels here.
    Admission::DistinctBinaryFieldSurvey
}
#[derive(Debug)]
struct Evidence{
    group:String,dataset:String,status:String,count:usize,observation_id:String,event_id:String,
    scientific_name:String,country:String,coordinate_uncertainty_m:f64,sampling_effort:String
}
fn parse_evidence(xs:&[String])->Result<Evidence,Box<dyn Error>>{
    let r=cells(xs,10,"GBIF occurrence evidence")?;
    let uncertainty=r[8].parse::<f64>()?;
    if !uncertainty.is_finite() || uncertainty<=0.0{return Err(err("missing real coordinate uncertainty"));}
    let count=r[3].parse::<usize>()?;
    if count==0 || r[4].is_empty() || r[5].is_empty() || r[9].trim().is_empty() {
       return Err(err("absent live record or sampling protocol"));
    }
    if r[2]!="PRESENT"&&r[2]!="ABSENT"{return Err(err("unsupported occurrenceStatus"));}
    Ok(Evidence{group:r[0].clone(),dataset:r[1].clone(),status:r[2].clone(),count,
        observation_id:r[4].clone(),event_id:r[5].clone(),scientific_name:r[6].clone(),
        country:r[7].clone(),coordinate_uncertainty_m:uncertainty,sampling_effort:r[9].clone()})
}
fn main()->Result<(),Box<dyn Error>>{
    let argv:Vec<String>=env::args().collect();
    if argv.len()!=6{return Err(err("Usage: gbif_p2 PARENT_TSV DATASETS_TSV SWEDISH_ROWS_TSV OUTPUT_DIRECTORY LIVE_PARENT_SOURCE_STATUS_TSV"));}
    let root=cells(lines(&argv[1])?.first().ok_or_else(||err("missing parent metadata"))?,6,"GBIF parent")?.to_vec();
    if root[0]!=PARENT || root[1]!=ORIGINAL_DOI ||
       root[2]!="29543" || root[3]!="27" || root[4]!="FI" || root[5]!="3033263" {
        return Err(err("original GBIF parent snapshot mismatch"));
    }
    let d=lines(&argv[2])?;
    if d.len()!=27{return Err(err(format!("parent dataset count {} not 27",d.len())));}
    let mut keys=BTreeSet::new();
    let mut counts=BTreeMap::new();
    let mut sum=0usize;
    for row in &d {
        let r=cells(row,4,"GBIF dataset usage")?;
        let n=r[2].parse::<usize>()?;
        if n==0||r[0].is_empty()||r[1].is_empty()||r[3].is_empty(){return Err(err("missing source dataset metadata"));}
        if !keys.insert(r[0].clone()){return Err(err("duplicate datasetKey in GBIF 2024 parent"));}
        counts.insert(r[0].clone(),n);
        sum=sum.checked_add(n).ok_or_else(||err("record-count overflow"))?;
    }
    if sum!=29543 || !keys.contains(FINBIF_PARENT_UUID) || counts[FINBIF_PARENT_UUID]!=585 {
        return Err(err("original GBIF source-sum or FinBIF ancestry mismatch"));
    }
    if keys.contains(SWEDEN_MAIN)||keys.contains(SWEDEN_DISCONTINUED){
        return Err(err("Swedish dataset unexpectedly within original 2024 Finnish GBIF parent"));
    }
    let original_top=[
      ("acf9b46d-e71a-4ccb-91d2-a021ffda4dd4",14651usize),
      ("f2e389da-39c3-4f21-8d72-b7d574d924a9",9686usize),
      ("b84a3711-b4ca-4e4f-adac-80dfaea98d1c",2308usize),
      ("50c9509d-22c7-4a22-a47d-8c48425ef4a7",1560usize)];
    for (id,n) in original_top {
       if counts.get(id).copied()!=Some(n){return Err(err("original top publisher contributor drift"));}
    }
    let es=lines(&argv[3])?;
    if es.len()!=4{return Err(err("exact 4 real Swedish GBIF occurrence queries needed"));}
    let mut by_group:BTreeMap<String,BTreeMap<String,Evidence>>=BTreeMap::new();
    let mut observation_ids=BTreeSet::new();
    for row in &es {
       let x=parse_evidence(row)?;
       if x.country!="SE"||x.scientific_name!="Anemone nemorosa L."||
          (x.dataset!=SWEDEN_MAIN && x.dataset!=SWEDEN_DISCONTINUED) {
           return Err(err("Swedish record not exact species, country or source"));
       }
       if x.coordinate_uncertainty_m<200.0 || x.sampling_effort.trim().is_empty(){
          return Err(err("survey coordinates or original sampling effort unverified"));
       }
       if !observation_ids.insert(x.observation_id.clone()){return Err(err("sample receipt reuses observationID"));}
       if x.event_id.is_empty(){return Err(err("missing eventID: not a field-sampling witness"));}
       let g=by_group.entry(x.group.clone()).or_default();
       if g.insert(x.status.clone(),x).is_some(){return Err(err("repeated Swedish status evidence"));}
    }
    let mut output=String::new();
    output.push_str("MQR495_P2_PARENT_SNAPSHOT=ORIGINAL_GBIF_DOWNLOAD_PUBLIC_API\n");
    output.push_str(&format!("MQR495_P2_PARENT_ID={PARENT}\nMQR495_P2_PARENT_DOI={ORIGINAL_DOI}\n"));
    output.push_str(&format!("MQR495_P2_PARENT_DATASETS={} RECORDS={sum}\n",keys.len()));
    output.push_str(&format!("MQR495_P2_TOP2_ORIGINAL_RECORDS={}\n",14651+9686));
    output.push_str(&format!("MQR495_P2_FINBIF_ALREADY_IN_PARENT={}\n",counts[FINBIF_PARENT_UUID]));
    for (name,ds,n) in [("current",SWEDEN_MAIN,36435usize),("supplement",SWEDEN_DISCONTINUED,26102usize)]{
       let g=by_group.get(name).ok_or_else(||err("missing Swedish study group"))?;
       if g.len()!=2{return Err(err("both original present and absent records mandatory"));}
       let p=g.get("PRESENT").ok_or_else(||err("missing true present"))?;
       let a=g.get("ABSENT").ok_or_else(||err("missing true recorded absent"))?;
       if p.dataset!=ds || a.dataset!=ds || p.count+a.count!=n {
           return Err(err("Swedish GBIF selected taxon counts/source mismatch"));
       }
       let expected=if name=="current" {(3491,32944)} else {(2434,23668)};
       if (p.count,a.count)!=expected{return Err(err("Swedish GBIF count drift from source snapshot"));}
       let admit=source_admit(&Survey{dataset:ds,region:"SE",scientific_name:"Anemone nemorosa L.",
                            observed_present:true,observed_absent:true},&keys);
       if admit!=Admission::SameTaxonDifferentTargetFrame {
           return Err(err("accidentally granted Finnish target labels from Swedish evidence"));
       }
       output.push_str(&format!("MQR495_P2_SWEDISH_{}=DATASET:{} TAXON:3033263 PRESENT:{} ABSENT:{} TOTAL:{}\n",
           name.to_uppercase(),ds,p.count,a.count,n));
       output.push_str(&format!("MQR495_P2_SWEDISH_{}_RECORD_IDS={} / {}\n",
           name.to_uppercase(),p.observation_id,a.observation_id));
    }
    if source_admit(&Survey{dataset:FINBIF_PARENT_UUID,region:"FI",scientific_name:"Anemone nemorosa L.",
       observed_present:true,observed_absent:true},&keys)!=Admission::ReusedParent {
        return Err(err("reused parent root promoted"));
    }
    output.push_str("MQR495_P2_DISTINCT_SWEDISH_FIELD_OBSERVATION_BINARY_CONTACT=PASS\n");
    output.push_str("MQR495_P2_FINNISH_TARGET_DIRECT_CALIBRATION=HOLD\n");
    output.push_str("MQR495_P2_SPATIAL_DESIGN_BASED_CI=HOLD\n");
    // Postdiscovery 2026 current GBIF index, not archival 2024 occurrence-status proportions.
    let mut source_status:BTreeMap<String,BTreeMap<String,usize>>=BTreeMap::new();
    for row in lines(&argv[5])? {
        let r=cells(&row,4,"current GBIF contributor presence status")?;
        let (group,dataset,status)=(&r[0],&r[1],&r[2]);
        if !keys.contains(dataset) ||
            (group!="spring"&&group!="kastikka") ||
            (status!="PRESENT"&&status!="ABSENT") {
            return Err(err("source status not from frozen original GBIF contributor UUID"));
        }
        if (group=="spring"&&dataset!="acf9b46d-e71a-4ccb-91d2-a021ffda4dd4") ||
           (group=="kastikka"&&dataset!="f2e389da-39c3-4f21-8d72-b7d574d924a9") {
            return Err(err("original GBIF contributor group-to-dataset mismatch"));
        }
        let m=source_status.entry(group.clone()).or_default();
        if m.insert(status.clone(),r[3].parse()?).is_some(){
            return Err(err("repeated source-status cohort"));
        }
    }
    if source_status.len()!=2 || source_status.values().any(|m|m.len()!=2) {
        return Err(err("incomplete current source-status contrast"));
    }
    let spring=&source_status["spring"];
    let kastikka=&source_status["kastikka"];
    if spring["PRESENT"]!=3670 || spring["ABSENT"]!=11622 ||
       kastikka["PRESENT"]!=9862 || kastikka["ABSENT"]!=0 {
        return Err(err("current GBIF source cohort count drift; do not misreport as historical 2024 parent ratios"));
    }
    output.push_str(&format!("MQR495_P2B_SPRING_CURRENT_2000_2024=PRESENT:{} ABSENT:{} ORIGINAL_PARENT_2024:{}\\n",
        spring["PRESENT"],spring["ABSENT"],counts["acf9b46d-e71a-4ccb-91d2-a021ffda4dd4"]));
    output.push_str(&format!("MQR495_P2B_KASTIKKA_CURRENT_2000_2024=PRESENT:{} ABSENT:{} ORIGINAL_PARENT_2024:{}\\n",
        kastikka["PRESENT"],kastikka["ABSENT"],counts["f2e389da-39c3-4f21-8d72-b7d574d924a9"]));
    output.push_str("MQR495_P2B_SOURCE_LABEL_MECHANISM_HETEROGENEITY=PASS_OBSERVATIONAL\\n");
    let o=Path::new(&argv[4]);
    fs::create_dir_all(o)?;
    let mut f=File::create(o.join("mqr495-gbif-p2-rust-verdict.txt"))?;
    f.write_all(output.as_bytes())?;
    print!("{output}");
    Ok(())
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test] fn identical_gbif_parent_fails_authority(){
    let mut x=BTreeSet::new();x.insert(FINBIF_PARENT_UUID.to_owned());
    let v=Survey{dataset:FINBIF_PARENT_UUID,region:"FI",scientific_name:"Anemone nemorosa L.",observed_present:true,observed_absent:true};
    assert_eq!(source_admit(&v,&x),Admission::ReusedParent);
 }
 #[test] fn swedish_binary_record_is_not_finnish_target(){
    let x=BTreeSet::new();
    let v=Survey{dataset:SWEDEN_MAIN,region:"SE",scientific_name:"Anemone nemorosa L.",observed_present:true,observed_absent:true};
    assert_eq!(source_admit(&v,&x),Admission::SameTaxonDifferentTargetFrame);
 }
 #[test] fn absence_not_inferred_from_presence_only(){
    let x=BTreeSet::new();
    let v=Survey{dataset:SWEDEN_MAIN,region:"SE",scientific_name:"Anemone nemorosa L.",observed_present:true,observed_absent:false};
    assert_eq!(source_admit(&v,&x),Admission::NoObservedBinary);
 }
 #[test] fn wrong_taxon_never_granted(){
    let x=BTreeSet::new();
    let v=Survey{dataset:SWEDEN_MAIN,region:"SE",scientific_name:"Anemone spp.",observed_present:true,observed_absent:true};
    assert_eq!(source_admit(&v,&x),Admission::Unattested);
 }
 #[test] fn nonzero_coords_and_protocol_are_required(){
    let row=["current","d59ccafb-251e-46cf-9319-37b58d88e7c5","ABSENT","32944","uuid","event",
      "Anemone nemorosa L.","SE","1131","1 day survey of a 100 m^2 area"];
    let v=row.map(ToString::to_string).to_vec();
    let e=parse_evidence(&v).unwrap();
    assert_eq!(e.count,32944);
    assert_eq!(e.status,"ABSENT");
    assert!(e.coordinate_uncertainty_m>=200.0);
 }
}
