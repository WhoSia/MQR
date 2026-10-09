//! MQR-4.100 internal P7 — separate Rust parser of original video-event / 9-column
//! sensor row contracts and Fréchet inequalities on independently generated receipt.
//! Not an independently reannotated video or an independent detector implementation.
use std::{collections::{BTreeMap,BTreeSet},env,fs::File,io::{BufRead,BufReader},path::Path};
fn count_samples(path:&Path)->usize{
    let mut n=0;
    for line in BufReader::new(File::open(path).expect("Missing original sensor file")).lines(){
        let line=line.expect("Malformed UTF-8");if line.trim().is_empty(){continue;}
        let x:Vec<_>=line.split_whitespace().collect();
        assert_eq!(x.len(),9,"Exactly wrist/hip/ankle xyz expected");
        for s in x {assert!(s.parse::<f64>().expect("Sensor not numeric").is_finite());}
        n+=1;
    }
    n
}
fn count_reference(path:&Path,n:usize)->(usize,usize,usize,Vec<(usize,String)>) {
    let mut steps=0;let mut shifts=0;let mut labels=0;let mut invalid=Vec::new();
    let mut last=None;
    for line in BufReader::new(File::open(path).expect("Missing publisher video event annotations")).lines(){
        let line=line.expect("Bad reference text");if line.trim().is_empty(){continue;}
        let parts=line.split_whitespace().collect::<Vec<_>>();assert_eq!(parts.len(),2);
        let i:usize=parts[0].parse().unwrap();let kind=parts[1].to_owned();
        assert!(matches!(kind.as_str(),"left"|"right"|"leftshift"|"rightshift"));
        if let Some(x)=last{assert!(i>x,"Publisher annotations not chronologically ordered");}last=Some(i);
        if i>=n{invalid.push((i,kind.clone()));}
        else if kind.ends_with("shift"){shifts+=1;}
        else{steps+=1;}
        labels+=1;
    }
    (steps,shifts,labels,invalid)
}
fn receipt(path:&Path){
    let mut rows=0;let mut totals=BTreeMap::new();
    for line in BufReader::new(File::open(path).expect("Missing P7 conditional-overlap CSV receipt")).lines(){
        let text=line.unwrap();if rows==0{assert_eq!(text,"participant,condition,sensor_pair,steps,detected_x,detected_y,detected_by_both,frechet_lower,frechet_upper,empirical_overlap_under_independence");rows+=1;continue;}
        let q=text.split(',').collect::<Vec<_>>();assert_eq!(q.len(),10);
        let n:usize=q[3].parse().unwrap();let a:usize=q[4].parse().unwrap();let b:usize=q[5].parse().unwrap();let both:usize=q[6].parse().unwrap();let lo:usize=q[7].parse().unwrap();let hi:usize=q[8].parse().unwrap();
        assert!(a<=n && b<=n && both<=a && both<=b);
        assert_eq!(lo,a.saturating_add(b).saturating_sub(n));
        assert_eq!(hi,a.min(b));assert!(lo<=both && both<=hi);
        let t=totals.entry(q[2].to_string()).or_insert((0_usize,0_usize,0_usize,0_usize));
        t.0+=n;t.1+=a;t.2+=b;t.3+=both;
        rows+=1;
    }
    assert_eq!(rows,136); // 45 held-out participant×condition rows × 3 pairs + header
    assert_eq!(totals["wrist_hip"],(28697,15870,19900,11411));
    assert_eq!(totals["wrist_ankle"],(28697,15870,14059,8308));
    assert_eq!(totals["hip_ankle"],(28697,19900,14059,10615));
    println!("P7_RUST_VIDEO_CONDITIONAL_OVERLAP_BOUNDS=PASS rows=135 annotated_heldout_steps=28697");
}
fn main(){
    let args:Vec<_>=env::args().skip(1).collect();
    assert_eq!(args.len(),2,"Usage: p7_source_reference_rust EXTRACTED_SOURCE_ROOT P7_OVERLAP_CSV");
    let root=Path::new(&args[0]);let mut total_steps=0;let mut total_shifts=0;let mut all_labels=0;let mut heldout_steps=0;
    let mut out_of_bounds=Vec::new();let mut all_conds=BTreeSet::new();
    for id in 1..=30{
        for condition in ["Regular","SemiRegular","Irregular"]{
            let path=root.join(format!("P{id:03}")).join(condition);
            let sensor=std::fs::read_dir(&path).unwrap().map(|d|d.unwrap().path())
                .find(|p|p.extension().is_some_and(|x|x=="txt") && p.file_name().unwrap()!="steps.txt").unwrap();
            let n=count_samples(&sensor);let ann=path.join("steps.txt");
            let (steps,shift,entries,invalid)=count_reference(&ann,n);
            total_steps+=steps;total_shifts+=shift;all_labels+=entries;
            if id>=16{heldout_steps+=steps;}
            for (ix,typ) in invalid{out_of_bounds.push((id,condition.to_owned(),ix,typ,n));}
            all_conds.insert(condition.to_owned());
        }
    }
    assert_eq!(all_conds.len(),3);
    assert_eq!((total_steps,total_shifts,all_labels,heldout_steps),(56668,4131,60801,28697));
    assert_eq!(out_of_bounds.len(),2);
    assert_eq!(out_of_bounds[0],(10,"Regular".to_string(),9233,"leftshift".to_string(),9192));
    assert_eq!(out_of_bounds[1],(19,"Irregular".to_string(),10092,"leftshift".to_string(),9968));
    println!("P7_RUST_ORIGINAL_VIDEO_ANNOTATION_CONTRACT_PASS 90_pairs steps=56668 valid_shifts=4131 total_labels=60801 anomalies=2");
    receipt(Path::new(&args[1]));
    println!("P7_SCIENTIFIC_SCOPE=ANNOTATION_CONDITIONAL_ONLY; LATENT_TRUE_EVENTS=UNOBSERVED");
}
#[cfg(test)]mod test{
    #[test]fn frechet_witness(){for n in 1_usize..15{for a in 0..=n{for b in 0..=n{
        let lo=a.saturating_add(b).saturating_sub(n);let hi=a.min(b);assert!(lo<=hi);
        for x in lo..=hi {assert!(x<=a&&x<=b&&a+b<=n+x);}
    }}}}
}
