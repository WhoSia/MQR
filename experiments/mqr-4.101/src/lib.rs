//! MQR 4.101: sharp finite binary risk bounds with selective fallible references.
//! The upper bound assumes an EXTERNAL certificate of <=k errors among m rated
//! observations. Two expert reports alone never supply that certificate.
//! No independent-truth claim and no latent-population extrapolation.

/// Error counts in a finite population of n. `e` is h-versus-fallible-label
/// mismatch count on m observed reference labels. k is an *externally certified*
/// maximum number of erroneous reference labels in those m cases.
pub fn sharp_error_counts(n: u64, m: u64, e: u64, k: u64) -> Option<(u64,u64)> {
    if m>n || e>m || k>m { return None; }
    let lower=e.saturating_sub(k);
    let upper=e + k.min(m-e) + (n-m);
    Some((lower,upper))
}

pub fn risk_dominance(n:u64, a:(u64,u64), b:(u64,u64))->Option<&'static str>{
    if n==0 || a.0>a.1 || b.0>b.1 || a.1>n || b.1>n{return None}
    if a.1<b.0 {Some("A strictly less true error than B for all allowed completions")}
    else if b.1<a.0 {Some("B strictly less true error than A for all allowed completions")}
    else {Some("NO risk ordering is identified by these separate scalar intervals")}
}

#[cfg(test)]mod tests {
    use super::*;
    #[test]fn corner_cases_and_no_external_reference_budget(){
        assert_eq!(sharp_error_counts(487,402,76,0),Some((76,161)));
        assert_eq!(sharp_error_counts(487,402,76,10),Some((66,171)));
        assert_eq!(sharp_error_counts(487,402,76,402),Some((0,487)));
        assert_eq!(sharp_error_counts(11,11,3,0),Some((3,3)));
        assert_eq!(sharp_error_counts(11,0,0,0),Some((0,11)));
        assert!(sharp_error_counts(3,4,2,1).is_none());
    }
    #[test]fn exhaustive_sharpness_binary_truth() {
        let mut tested=0;
        for n in 1_u64..=6 {
            let states=3_u64.pow(n as u32);
            for mut mask in 0..states{
                let mut obs=vec![None;n as usize];
                for a in &mut obs {let digit=mask%3;mask/=3;*a=match digit{0=>None,1=>Some(false),_=>Some(true)}}
                let m=obs.iter().filter(|x|x.is_some()).count() as u64;
                for pred in 0..(1<<n) {
                    let errors=obs.iter().enumerate().filter(|(i,v)|{
                        v.map(|truth|truth!=((pred>>i)&1==1)).unwrap_or(false)
                    }).count() as u64;
                    for k in 0..=m{
                        let mut actual_lo=n+1;let mut actual_hi=0;
                        for possible_truth in 0..(1<<n){
                            let incorrect_ref=obs.iter().enumerate().filter(|(i,v)|{
                                v.map(|r|r!=((possible_truth>>i)&1==1)).unwrap_or(false)
                            }).count() as u64;
                            if incorrect_ref>k {continue}
                            let loss=(0..n).filter(|i|((pred>>i)&1)!=((possible_truth>>i)&1)).count() as u64;
                            actual_lo=actual_lo.min(loss);actual_hi=actual_hi.max(loss);
                        }
                        assert_eq!(sharp_error_counts(n,m,errors,k),Some((actual_lo,actual_hi)));
                        tested+=1;
                    }
                }
            }
        }
        assert!(tested>30000);
    }
    #[test]fn risk_interval_overlap_does_not_prove_ranking(){
        assert_eq!(risk_dominance(100,(0,20),(30,40)),Some("A strictly less true error than B for all allowed completions"));
        assert_eq!(risk_dominance(100,(0,30),(20,45)),Some("NO risk ordering is identified by these separate scalar intervals"));
    }
}
