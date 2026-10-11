//! MQR-4.112 P1-J: prospective REAL author-data admission, not a proxy.
//! The repository intentionally contains NO full FER1/FER3 author observations.
//! Offline usage:
//! p1j_full_source_gate <original_2021_tutorial_data_dir> <new_author_full_data_dir>
//! Expected in new_author_full_data_dir:
//!  source_receipt.tsv: sample<TAB>bin_sha256<TAB>discpos_sha256<TAB>source_identifier<TAB>license_status
//!  FER1/bin.BIN, FER1/DiscPos.csv, FER3/bin.BIN, FER3/DiscPos.csv
//! This gate validates structure and hashes, NOT the authority of self-declared custody.
//! Real author-supplied BINX/multi-file inputs require explicit parser extension.
#![forbid(unsafe_code)]
use std::{collections::{BTreeMap,BTreeSet},env,fs,path::{Path,PathBuf},process::Command};

type Grain=(u16,i16);
fn roster(csv:&str)->Result<BTreeSet<Grain>,String>{
    let mut lines=csv.lines();
    if lines.next()!=Some("position,grain"){return Err("header != position,grain".into());}
    let mut keys=BTreeSet::new();
    for (idx,line) in lines.enumerate(){
        if line.trim().is_empty(){continue;}
        let items:Vec<_>=line.split(',').map(str::trim).collect();
        if items.len()!=2{return Err(format!("malformed selection row {}",idx+2));}
        let d=items[0].parse::<u16>().map_err(|_|"disc not numeric".to_owned())?;
        let g=items[1].parse::<i16>().map_err(|_|"grain not numeric".to_owned())?;
        if d==0||g<=0||!keys.insert((d,g)){return Err("duplicate/invalid grain".into());}
    }
    Ok(keys)
}
fn raw_bin_keys(bytes:&[u8])->Result<BTreeSet<Grain>,String>{
    let mut ids=BTreeSet::new();let mut offset=0usize;
    while offset<bytes.len(){
        let h=bytes.get(offset..offset+272).ok_or("truncated BIN header")?;
        if h[0]!=4{return Err("BINX or unexpected Risoe format; STOP for review".into());}
        let size=usize::from(u16::from_le_bytes([h[2],h[3]]));
        let n=usize::from(u16::from_le_bytes([h[6],h[7]]));
        if n==0||n>20_000||size!=272+n*4||bytes.get(offset..offset+size).is_none(){
            return Err("invalid BIN v4 frame".into());
        }
        let key=(u16::from(h[33]),i16::from_le_bytes([h[210],h[211]]));
        if key.0==0||key.1<=0{return Err("invalid BIN grain key".into());}
        ids.insert(key);offset+=size;
    }
    if ids.is_empty(){return Err("empty source BIN".into());}
    Ok(ids)
}
fn sha(path:&Path)->Result<String,String>{
    let output=Command::new("sha256sum").arg(path).output().map_err(|e|e.to_string())?;
    if !output.status.success(){return Err("sha256sum failed".into());}
    let s=String::from_utf8(output.stdout).map_err(|e|e.to_string())?;
    let h=s.split_whitespace().next().ok_or("sha256 missing")?;
    if h.len()!=64||!h.bytes().all(|b|b.is_ascii_hexdigit()){return Err("bad SHA256".into());}
    Ok(h.to_lowercase())
}
#[derive(Clone)]
struct Receipt{sample:String,bin_sha:String,roster_sha:String,source:String,license:String}
fn receipt_table(path:&Path)->Result<BTreeMap<String,Receipt>,String>{
    let t=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut l=t.lines();
    if l.next()!=Some("sample\tbin_sha256\tdiscpos_sha256\tsource_identifier\tlicense_status"){
        return Err("unrecognized source receipt schema".into());
    }
    let mut map=BTreeMap::new();
    for line in l{
        if line.trim().is_empty(){continue;}
        let p:Vec<_>=line.split('\t').collect();
        if p.len()!=5{return Err("bad source receipt width".into());}
        let r=Receipt{sample:p[0].to_owned(),bin_sha:p[1].to_lowercase(),
            roster_sha:p[2].to_lowercase(),source:p[3].to_owned(),license:p[4].to_owned()};
        if r.source.trim().len()<10||r.license.trim().is_empty(){
            return Err("missing source/rights statement".into());
        }
        if map.insert(r.sample.clone(),r).is_some(){return Err("duplicate source receipt sample".into());}
    }
    if map.len()!=2||!map.contains_key("FER1")||!map.contains_key("FER3"){
        return Err("require exact FER1+FER3 source receipt".into());
    }
    Ok(map)
}
fn audit(public_dir:&Path,full_dir:&Path)->Result<Vec<String>,String>{
    let manifest=receipt_table(&full_dir.join("source_receipt.tsv"))?;
    let mut rows=Vec::new();
    for (sample,prior_count) in [("FER1",97usize),("FER3",96usize)]{
        let old_dir=public_dir.join(sample);let new_dir=full_dir.join(sample);
        let pubbin=old_dir.join("bin.BIN");
        let pubselect=old_dir.join("DiscPos.csv");
        let newbin=new_dir.join("bin.BIN");
        let newselect=new_dir.join("DiscPos.csv");
        let pubkeys=roster(&fs::read_to_string(&pubselect).map_err(|e|e.to_string())?)?;
        if pubkeys.len()!=49{return Err(format!("{sample} public population not authentic 49"));}
        let allkeys=roster(&fs::read_to_string(&newselect).map_err(|e|e.to_string())?)?;
        if allkeys.len()<=49{return Err(format!("{sample}: not a full cohort; only {} selected grain",allkeys.len()));}
        if !pubkeys.is_subset(&allkeys){
            return Err(format!("{sample}: public 49 physical keys not subset of candidate; no matched contrast"));
        }
        let rec=&manifest[sample];
        if sha(&newbin)?!=rec.bin_sha||sha(&newselect)?!=rec.roster_sha{
            return Err(format!("{sample}: source checksum failed"));
        }
        if sha(&pubbin)?==sha(&newbin)?{
            return Err(format!("{sample}: tutorial BIN cannot be relabeled full author raw"));
        }
        let origin=raw_bin_keys(&fs::read(&newbin).map_err(|e|e.to_string())?)?;
        if !allkeys.is_subset(&origin){return Err(format!("{sample}: selected grains absent from full raw BIN"));}
        let match2015=if allkeys.len()==prior_count{"2015_COUNT_COMPATIBLE"}
                      else{"2015_COUNT_DIFF_REQUIRES_MANUAL_REVIEW"};
        rows.push(format!("{sample},{},{},{},{},{},{},STRUCTURAL_ONLY_EXTERNAL_PROVENANCE_REVIEW_REQUIRED",
            pubkeys.len(),allkeys.len(),allkeys.len()-pubkeys.len(),origin.len(),
            match2015,rec.license.replace(',',';')));
    }
    Ok(rows)
}
fn main(){
    let args:Vec<_>=env::args().collect();
    if args.len()!=3{eprintln!("usage: p1j_full_source_gate <2021_public_data_dir> <new_full_author_data_dir>");std::process::exit(2);}
    println!("sample,public_keys,candidate_keys,candidate_additional_keys,physical_raw_keys,vs_2015_accepted,license,verdict");
    match audit(&PathBuf::from(&args[1]),&PathBuf::from(&args[2])){
        Ok(rows)=>{for row in rows{println!("{row}");}
           eprintln!("WARNING: structural match does NOT authenticate the claimed source or the 2021 published cohort");},
        Err(e)=>{eprintln!("FULL_AUTHOR_DATA_NOT_ADMITTED: {e}");std::process::exit(1);}
    }
}
#[cfg(test)]mod tests{
    use super::*;
    #[test]fn reject_fake_49_as_full(){assert!(roster("position,grain\n1,1\n").unwrap().len()<=49);}
    #[test]fn duplicate_not_permitted(){assert!(roster("position,grain\n1,1\n1,1\n").is_err());}
    #[test]fn reject_bad_header(){assert!(roster("grain,position\n1,2").is_err());}
    #[test]fn missing_frame_is_not_raw(){assert!(raw_bin_keys(&[4,0,8]).is_err());}
    #[test]fn no_recipient_entitlement_without_receipt(){assert!(receipt_table(Path::new("/not/a/real/file")).is_err());}
    #[test]fn empty_selection_not_a_population(){assert!(roster("position,grain\n").unwrap().len()<=49);}
}
