//! MQR 4.111 P8: read-only Risø BIN v4 record structure gate.
//! Public reference: R-Lum/Luminescence R/read_BIN2R.R, v4 header/data layout.
//! Same user's Guérin FER original BINs are NOT committed to this repository.
//! This parser is a second, independent structural implementation, not
//! the official R parser, an OSL Lx/Tx likelihood, or BayLum posterior engine.
//! Invoke with an absolute BIN path to inspect the user's existing local file.
//! Without an input it runs a no-data smoke example; CI tests synthetic frames.
#![forbid(unsafe_code)]
use std::{collections::{BTreeMap,BTreeSet},env,fs};

#[derive(Debug,Clone,PartialEq,Eq)]
struct Record {
    position: u8, run: u8, set: u8, grain: i16,
    ltype: u8, dtype: u8, points: Vec<i32>,
}
fn read_le_u16(raw:&[u8],at:usize)->Result<usize,String>{
    let b=raw.get(at..at+2).ok_or("missing u16")?;
    Ok(usize::from(u16::from_le_bytes([b[0],b[1]])))
}
fn decode_v4(raw:&[u8])->Result<Vec<Record>,String>{
    let mut out=Vec::<Record>::new();
    let mut i=0usize;
    while i<raw.len(){
        let hdr=raw.get(i..i+8).ok_or("truncated v4 header")?;
        if hdr[0]!=4 {return Err(format!("unsupported version {} at {}",hdr[0],i))}
        let size=read_le_u16(raw,i+2)?;
        let n=read_le_u16(raw,i+6)?;
        if size<272 || n>20000 || size!=272+4*n {
            return Err(format!("invalid v4 length/point count: {size}/{n} at {i}"));
        }
        let frame=raw.get(i..i+size).ok_or("truncated v4 record payload")?;
        let grain=i16::from_le_bytes([frame[210],frame[211]]);
        let mut points=Vec::with_capacity(n);
        for p in 0..n {
            let at=272+4*p;
            points.push(i32::from_le_bytes(
                frame[at..at+4].try_into().map_err(|_|"broken sample data")?));
        }
        out.push(Record{ltype:frame[8],position:frame[33],run:frame[34],
            dtype:frame[67],set:frame[208],grain,points});
        i+=size;
    }
    Ok(out)
}
fn audit(records:&[Record])->(usize,usize,BTreeMap<u8,usize>){
    let keys:BTreeSet<(u8,i16)>=records.iter().map(|r|(r.position,r.grain)).collect();
    let mut dtype=BTreeMap::new();
    for r in records{*dtype.entry(r.dtype).or_insert(0)+=1;}
    (keys.len(),records.iter().map(|r|r.points.len()).sum(),dtype)
}
fn main(){
    let path=env::args().nth(1);
    match path{
        Some(p)=>{
            let raw=fs::read(&p).unwrap_or_else(|e|panic!("Cannot read input: {e}"));
            let rows=decode_v4(&raw).unwrap_or_else(|e|panic!("Invalid BIN v4 input: {e}"));
            let (keys,points,types)=audit(&rows);
            println!("BIN v4 record-level ONLY: {} records; {keys} (position,grain) keys; {points} raw counts",rows.len());
            println!("Record DTYPE distribution {:?}",types);
            println!("No sampling age, raw chronology join, official R cross-check or BayLum posterior inferred.");
        }
        None=>println!("MQR P8 reader: read-only v4 CLI (provide BIN path); no raw data embedded in CI."),
    }
}
#[cfg(test)]
mod tests{
    use super::*;
    fn frame(n:usize)->Vec<u8>{
        let mut x=vec![0u8;272+4*n];
        x[0]=4;x[2..4].copy_from_slice(&((272+4*n)as u16).to_le_bytes());
        x[6..8].copy_from_slice(&(n as u16).to_le_bytes());
        x[8]=1;x[33]=5;x[34]=3;x[67]=0;x[208]=4;
        x[210..212].copy_from_slice(&46i16.to_le_bytes());
        for t in 0..n {x[272+4*t..276+4*t].copy_from_slice(&(t as i32).to_le_bytes());}
        x
    }
    #[test] fn parse_one_synthetic_frame(){
        let b=frame(100);let r=decode_v4(&b).unwrap();
        assert_eq!(r.len(),1);assert_eq!(r[0].points.len(),100);
        assert_eq!(r[0].points[99],99);assert_eq!(r[0].position,5);
        assert_eq!(r[0].grain,46);assert_eq!(r[0].run,3);
        assert_eq!(r[0].set,4);assert_eq!(r[0].dtype,0);
    }
    #[test] fn parse_multiple_frames_and_source_key_counts(){
        let mut b=frame(100);b.extend(frame(100));let r=decode_v4(&b).unwrap();
        assert_eq!(r.len(),2);assert_eq!(audit(&r).0,1);
        assert_eq!(audit(&r).1,200);
    }
    #[test] fn reject_unsupported_version(){
        let mut b=frame(100);b[0]=8;assert!(decode_v4(&b).is_err());
    }
    #[test] fn reject_declared_payload_truncation(){
        let mut b=frame(100);b.pop();assert!(decode_v4(&b).is_err());
    }
    #[test] fn reject_declared_npoints_frame_mismatch(){
        let mut b=frame(100);b[6]=101;assert!(decode_v4(&b).is_err());
    }
    #[test] fn reject_partial_trailing_record(){
        let mut b=frame(100);b.extend_from_slice(&[4,0,1]);assert!(decode_v4(&b).is_err());
    }
}
