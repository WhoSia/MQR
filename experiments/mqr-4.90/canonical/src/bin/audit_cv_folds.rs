//! Preserve the fixed source/fold objects to distinguish fold-selected
//! CV f_fold from the separately fitted final cross-region predictor.
use std::{collections::{BTreeMap,BTreeSet},env,fs};
fn main(){
    let args:Vec<_>=env::args().collect();
    if args.len()!=2{eprintln!("usage: audit_cv_folds <published-cv-folds.csv>");std::process::exit(2)}
    let data=fs::read_to_string(&args[1]).expect("missing source-fold score rows");
    let mut lines=data.lines();
    let header="source_calibration,fold,training_count,test_count,background_points,reported_fold_test_auc,original_cv_a4_mean";
    assert_eq!(lines.next(),Some(header),"source fold header mismatch");
    let mut grouped:BTreeMap<String,Vec<(String,f64,usize)>>=BTreeMap::new();
    let mut folds=BTreeSet::new();
    for row in lines{
        if row.is_empty(){continue}
        let c:Vec<_>=row.split(',').collect();
        assert_eq!(c.len(),7);
        assert!(folds.insert((c[0].to_owned(),c[1].to_owned())),"duplicated fold");
        for i in 2..5{assert!(c[i].parse::<usize>().unwrap()>0)}
        let auc:f64 = c[5].parse().unwrap();
        assert!((0.0..=1.0).contains(&auc));
        let published:f64=c[6].parse().unwrap();
        grouped.entry(c[0].to_string()).or_default()
            .push((c[1].to_string(),auc as f64,(published*100.0).round() as usize));
    }
    assert_eq!(grouped.len(),3,"exact three source cohort families required");
    let mut count=0;
    for (name,items) in &grouped{
        assert_eq!(items.len(),4,"fourfold cohort incomplete");
        let (taxon,ref_mean)=match name.as_str(){
            "Oxalis_latifolia_America"=>("Oxalis_latifolia",87_usize),
            "Digitaria_sanguinalis_Europe"=>("Digitaria_sanguinalis",82_usize),
            "Amaranthus_retroflexus_NorthAmerica"=>("Amaranthus_retroflexus",85_usize),
            _=>panic!("unregistered native-only source calibration")
        };
        let labels:BTreeSet<_>=items.iter().map(|x|x.0.clone()).collect();
        let expected:BTreeSet<_>=(0..4).map(|i|format!("{taxon}_{i}")).collect();
        assert_eq!(labels,expected);
        assert!(items.iter().all(|x|x.2==ref_mean));
        let foldmean=items.iter().map(|x|x.1).sum::<f64>()/4.;
        let paper=ref_mean as f64/100.;
        assert!((foldmean-paper).abs()<=0.005001,"original 4fold/A4 metric mismatch");
        println!("MQR490_P8_CV_FOLD_RUST={name} MEAN={foldmean:.8} PAPER={paper:.2}");
        count+=items.len();
    }
    assert_eq!(count,12);
    println!("MQR490_P8_CV_FOLD_SOURCE_REPRODUCTION=PASS");
    println!("MQR490_P8_CV_TRAINED_PREDICTOR_EQUIVALENCE_TO_TARGET=NOT_ESTABLISHED");
    println!("MQR490_P8_CV_NEGATIVE_REFERENCE_EQUIVALENCE_TO_TARGET=NOT_ESTABLISHED");
}

