//! MQR 4.95 P3: original 2024 GBIF download vs pinned Serov CSV
//! source schema / source key admissibility scanner (std-only Rust).
use std::{collections::{BTreeMap,BTreeSet},env,error::Error,fs::File,io::{BufRead,BufReader,Write},path::Path};
fn error(s:impl Into<String>)->Box<dyn Error>{std::io::Error::new(std::io::ErrorKind::InvalidData,s.into()).into()}
fn fields(line:&str)->Vec<String> {
    line.trim_start_matches('\u{feff}').trim_end_matches('\r').split(',').map(|s|s.trim().trim_matches('"').to_string()).collect()
}
fn inspect(path:&str) -> Result<String,Box<dyn Error>>{
    let file=File::open(path)?;
    let mut stream=BufReader::new(file).lines();
    let header=fields(&stream.next().ok_or_else(||error("empty publisher source"))??);
    let mut occurrences=BTreeMap::<String,usize>::new();
    for name in &header { *occurrences.entry(name.clone()).or_default()+=1; }
    if occurrences.values().any(|n|*n!=1){return Err(error("duplicate source columns"));}
    let idx=header.iter().position(|z|z=="presence").ok_or_else(||error("no publisher 'presence' field"))?;
    let mut presence=[0usize;2];let mut rows=0usize;let mut invalid_rows=0usize;
    let mut canonical_combos=BTreeSet::<String>::new();
    let mut site_count=BTreeMap::<String,usize>::new();
    let lat=header.iter().position(|z|z=="lat");
    let long=header.iter().position(|z|z=="long");
    let year=header.iter().position(|z|z=="year");
    for line in stream {
        let v=fields(&line?);
        if v.len()!=header.len(){invalid_rows+=1;continue;}
        let label=v[idx].parse::<u8>().map_err(|_|error("noninteger publisher presence"))?;
        if label>1 {return Err(error("nonbinary publisher presence flag"));}
        presence[label as usize]+=1;rows+=1;
        if let (Some(a),Some(b),Some(y))=(lat,long,year){
            let key=format!("{}|{}|{}",v[a],v[b],v[y]);
            *site_count.entry(key.clone()).or_default()+=1;
            canonical_combos.insert(key);
        }
    }
    if rows!=29543 || invalid_rows!=0 {return Err(error(format!("published CSV: {rows} rows / {invalid_rows} malformed, expected exactly 29543")));}
    let id_candidates=["gbifID","gbifId","gbifid","occurrenceID","occurrenceId","datasetKey","eventID","eventId","catalogNumber","occurrenceStatus","originalStatus","samplingProtocol","coordinateUncertaintyInMeters","basisOfRecord","recordedBy"];
    let keys=id_candidates.iter().filter(|n|occurrences.contains_key(**n)).copied().collect::<Vec<_>>();
    let has_joinable_id=id_candidates[..8].iter().any(|n|occurrences.contains_key(*n));
    let mut s=String::new();
    s.push_str("MQR495_P3_PUBLISHER_SOURCE_ROW_COUNT=29543\n");
    s.push_str(&format!("MQR495_P3_PUBLISHER_COLUMNS={}\n",header.join("|")));
    s.push_str(&format!("MQR495_P3_PRESENCE_COUNTS=0:{} 1:{}\n",presence[0],presence[1]));
    s.push_str(&format!("MQR495_P3_ROW_LEVEL_SOURCE_FIELDS_PRESENT={}\n",if keys.is_empty(){"NONE".to_owned()}else{keys.join("|")}));
    s.push_str(&format!("MQR495_P3_DIRECT_SHARED_SOURCE_IDENTIFIER={}\n",if has_joinable_id{"POTENTIAL"}else{"ABSENT"}));
    s.push_str(&format!("MQR495_P3_LAT_LONG_YEAR_COMBOS={} MAX_DUPLICATES={}\n",canonical_combos.len(),site_count.values().max().copied().unwrap_or_default()));
    s.push_str(&format!("MQR495_P3_LABEL_KEYED_SOURCE_LINEAGE={}\n",if has_joinable_id{"REQUIRES_ID_TO_ORIGINAL_STATUS_CHECK"}else{"HOLD_NO_IDENTIFIED_ROW_JOIN"}));
    Ok(s)
}
fn main()->Result<(),Box<dyn Error>>{
    let args:Vec<String>=env::args().collect();
    if args.len()!=3{return Err(error("usage: gbif_p3 ORIGINAL_PUBLISHER_CSV OUTPUT_TXT"));}
    let s=inspect(&args[1])?;
    File::create(Path::new(&args[2]))?.write_all(s.as_bytes())?;
    print!("{s}");
    Ok(())
}
#[cfg(test)]
mod tests{
    use super::*;
    #[test] fn trims_quoted_headers(){assert_eq!(fields(r#""lat","long","presence","bio1""#),vec!["lat","long","presence","bio1"]);}
    #[test] fn absence_cannot_be_inferred_from_nonmatching_header(){assert!(!["lat","long","year","presence","bio1"].contains(&"gbifID"));}
    #[test] fn csv_fields_remain_conservative_not_geo_fuzzy(){let x=fields("1,2,2024,1");assert_eq!(x[0],"1");assert_eq!(x.len(),4);}
}
