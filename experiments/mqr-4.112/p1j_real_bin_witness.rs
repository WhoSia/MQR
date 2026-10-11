//! MQR-4.112 P1-J: independently pair original author's public grain IDs
//! with *all* Risoe BIN v4 raw records. No full-cohort data is presumed.
//! 2021 tutorial originals only. No synthetic data admitted as empirical.
#![forbid(unsafe_code)]
use std::collections::{BTreeMap,BTreeSet};
use std::{env,fs,path::Path};

type Key=(u16,i16);
#[derive(Clone,Debug)]
struct Record{key:Key,dtype:u8,channels:usize}
fn decode(bytes:&[u8])->Result<Vec<Record>,String>{
    let mut ans=Vec::new();let mut off=0;
    while off<bytes.len(){
        let h=bytes.get(off..off+272).ok_or("truncated header")?;
        if h[0]!=4{return Err("not Risoe v4".into())}
        let size=usize::from(u16::from_le_bytes([h[2],h[3]]));
        let channels=usize::from(u16::from_le_bytes([h[6],h[7]]));
        if channels!=100 || size!=272+channels*4 {return Err(format!("invalid record size {size} / {channels}"));}
        if bytes.get(off..off+size).is_none(){return Err("truncated data".into());}
        let grain=i16::from_le_bytes([h[210],h[211]]);
        let position=u16::from(h[33]);
        if grain<=0||position==0{return Err("invalid physical key".into());}
        ans.push(Record{key:(position,grain),dtype:h[67],channels});
        off+=size;
    }
    if ans.is_empty(){return Err("empty BIN".into())}
    Ok(ans)
}
fn csv_keys(raw:&str)->Result<Vec<Key>,String>{
    let mut iter=raw.lines();if iter.next()!=Some("position,grain"){return Err("unexpected DiscPos header".into());}
    let mut out=Vec::new();let mut unique=BTreeSet::new();
    for (idx,line) in iter.enumerate(){
        if line.trim().is_empty(){continue;}
        let parts:Vec<_>=line.split(',').map(str::trim).collect();
        if parts.len()!=2 {return Err(format!("bad DiscPos row {}",idx+2));}
        let x=parts[0].parse::<u16>().map_err(|_|"bad disc".to_string())?;
        let y=parts[1].parse::<i16>().map_err(|_|"bad grain".to_string())?;
        if x==0||y<=0||!unique.insert((x,y)){return Err(format!("duplicate/invalid key row {}",idx+2));}
        out.push((x,y));
    }
    Ok(out)
}
fn witness(sample:&str,dir:&Path)->Result<String,String>{
    let csv=fs::read_to_string(dir.join("DiscPos.csv")).map_err(|e|e.to_string())?;
    let bin=fs::read(dir.join("bin.BIN")).map_err(|e|e.to_string())?;
    let keys=csv_keys(&csv)?;
    let recs=decode(&bin)?;
    let want=match sample {"FER1"=>(49,882,18,[392,441,49]),"FER3"=>(49,784,16,[343,392,49]),_=>return Err("unknown sample".into())};
    if keys.len()!=want.0||recs.len()!=want.1{return Err("original sample size or record mismatch".into());}
    let all:BTreeSet<_>=keys.iter().copied().collect();
    let mut counts=BTreeMap::<Key,usize>::new();
    let mut dtype=BTreeMap::<u8,usize>::new();
    for record in &recs{
        if !all.contains(&record.key){return Err("orphan raw BIN grain outside DiscPos".into());}
        *counts.entry(record.key).or_insert(0)+=1;
        *dtype.entry(record.dtype).or_insert(0)+=1;
        if record.channels!=100{return Err("unexpected channel count".into());}
    }
    if counts.len()!=want.0 || counts.values().any(|&n|n!=want.2)
        || [0u8,6,3].iter().zip(want.3).any(|(&d,n)|dtype.get(&d)!=Some(&n))
        || dtype.len()!=3 {return Err("unexpected grain cycles/DTYPE census".into());}
    Ok(format!("{sample},PASS_PUBLIC_SUBSET,{}, {}, {},{}",keys.len(),
        recs.len(),recs.len()*100,bin.len()).replace(", ",","))
}
fn main(){
    let arg:Vec<_>=env::args().collect();
    if arg.len()!=2 {eprintln!("usage: p1j_real_bin_witness <unpacked_2021_supplement_data_dir>");std::process::exit(2);}
    let dir=Path::new(&arg[1]);
    println!("sample,source_scope,selected_grain_keys,raw_BIN_records,raw_channels,bin_bytes");
    for sample in ["FER1","FER3"]{
        match witness(sample,&dir.join(sample)){
            Ok(s)=>println!("{s}"),
            Err(e)=>{eprintln!("{sample}: {e}");std::process::exit(1);}
        }
    }
    println!("FULL_2015_OR_2021_AUTHOR_COHORT_NOT_PRESENT");
}
#[cfg(test)]mod tests{
    use super::*;
    fn one_record()->Vec<u8>{
        let mut b=vec![0u8;672];b[0]=4;b[2..4].copy_from_slice(&672u16.to_le_bytes());
        b[6..8].copy_from_slice(&100u16.to_le_bytes());
        b[33]=1;b[67]=0;b[210..212].copy_from_slice(&1i16.to_le_bytes());b
    }
    #[test]fn frame_roundtrip(){let a=decode(&one_record()).unwrap();assert_eq!(a.len(),1);assert_eq!(a[0].key,(1,1));}
    #[test]fn fail_on_truncated_frame(){let mut v=one_record();v.pop();assert!(decode(&v).is_err());}
    #[test]fn reject_source_duplicates(){assert!(csv_keys("position,grain\n1,1\n1,1\n").is_err());}
    #[test]fn skip_author_blank_rows(){assert_eq!(csv_keys("position,grain\n\n1,1\n\n2,3\n").unwrap().len(),2);}
    #[test]fn reject_missing_headers(){assert!(csv_keys("grain,position\n1,1").is_err());}
    #[test]fn reject_impossible_grain(){assert!(csv_keys("position,grain\n1,0").is_err());}
}
