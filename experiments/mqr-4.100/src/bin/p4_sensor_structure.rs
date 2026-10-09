//! MQR-4.100 P4: independent Rust line/subject/128-sample contract for UCI HAR.
//! One-window-by-index alignment is asserted as UCI's published preprocessing contract,
//! not independently timestamp-verified instrument independence or causal inference.
use std::{collections::{BTreeMap,BTreeSet},env,fs::File,io::{BufRead,BufReader},path::Path};
fn numbers(file:&Path, width:usize)->Vec<Vec<f64>>{
    let stream=BufReader::new(File::open(file).expect("Required UCI original split file missing"));
    let mut rows=Vec::new();
    for line in stream.lines(){
        let line=line.expect("Broken source record");
        let nums=line.split_ascii_whitespace().map(|s|s.parse::<f64>().expect("Not numeric")).collect::<Vec<_>>();
        if nums.is_empty(){continue;}
        assert_eq!(nums.len(),width, "Source file row width drift: {}",file.display());
        assert!(nums.iter().all(|x|x.is_finite()));
        rows.push(nums);
    }
    rows
}
fn labels(file:&Path)->Vec<usize>{
    numbers(file,1).iter().map(|v|{
        let x=v[0];assert!(x>=1.0 && x<=30.0 && (x.round()-x).abs()<1e-12);
        x as usize
    }).collect()
}
fn main(){
    let path=env::args().nth(1).expect("Usage: p4_sensor_structure PATH_TO_INNER_ROOT");
    let root=Path::new(&path);
    let mut split_subjects=Vec::new();
    for (split,n) in [("train",7352_usize),("test",2947)]{
        let root_split=root.join(split);
        let subj=labels(&root_split.join(format!("subject_{split}.txt")));
        let acts=labels(&root_split.join(format!("y_{split}.txt")));
        assert_eq!(subj.len(),n);assert_eq!(acts.len(),n);
        assert_eq!(acts.iter().copied().collect::<BTreeSet<_>>(),(1..=6).collect());
        let subs=subj.iter().copied().collect::<BTreeSet<_>>();
        assert_eq!(subs.len(),if split=="train"{21}else{9});
        let mut counts=BTreeMap::<usize,usize>::new();
        for a in &acts { *counts.entry(*a).or_default()+=1; }
        for sensor in ["total_acc","body_gyro"] {
            for axis in ["x","y","z"] {
                let file=root_split.join("Inertial Signals").join(format!("{sensor}_{axis}_{split}.txt"));
                let win=numbers(&file,128);
                assert_eq!(win.len(),n, "Row-level sensor/subject pairing unavailable");
                // Each axis file has the same number and ordered row positions.
            }
        }
        println!("UCI_P4_RUST_SPLIT={split} WINDOWS={n} SUBJECTS={} LABELS={:?}",subs.len(),counts);
        split_subjects.push(subs);
    }
    assert!(split_subjects[0].is_disjoint(&split_subjects[1]),"Subject-leakage across UCI splits");
    println!("MQR4100_P4_RUST_SOURCE_NATIVE_SENSOR_ALIGNMENT=PASS;BIOLOGICAL_PARAMETER_KERNEL=HOLD");
}
