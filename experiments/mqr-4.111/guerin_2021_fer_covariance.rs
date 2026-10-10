//! MQR 4.111 P6 — published illustrative covariance matrices (Guérin et al. 2021).
//!
//! Source: Guérin et al., Geochronology 3, 229–245 (2021).
//! DOI: 10.5194/gchron-3-229-2021
//! Supplement ZIP (original, non-experimental examples):
//! https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip
//! File paths: PracticalGuideToBayLum_Data/data/CovarianceMatrix_22_{SimplisticExample,RealisticExample}.csv
//! The two matrices illustrate alternative covariance assumptions, NOT two
//! independently observed physical covariance regimes or new MQR evidence.
//! The arithmetic is exact as integer nanounits where possible.
#![forbid(unsafe_code)]
const A: i64 = 9_191_746;
const B: i64 = 7_991_537;
const SIMPLISTIC_COV: i64 = 7_616_071;
const REALISTIC_COV: i64 = 2_152_365;
const NANOUNIT: f64 = 1_000_000_000.0;
fn diff_variance_nano(cov: i64) -> i64 { A + B - 2 * cov }
fn correlation(cov: i64) -> f64 {
    cov as f64 / ((A as f64) * (B as f64)).sqrt()
}
fn diff_sd(cov: i64) -> f64 {
    ((diff_variance_nano(cov) as f64) / NANOUNIT).sqrt()
}
fn main() {
    println!("MQR-4.111 P6: 2 ORIGINAL SOURCE *ILLUSTRATIVE* COVARIANCE MATRICES");
    println!("Simplistic: variance_difference={:.9}; sd={:.9}; correlation={:.9}",
        (diff_variance_nano(SIMPLISTIC_COV) as f64) / NANOUNIT,
        diff_sd(SIMPLISTIC_COV), correlation(SIMPLISTIC_COV));
    println!("Realistic:  variance_difference={:.9}; sd={:.9}; correlation={:.9}",
        (diff_variance_nano(REALISTIC_COV) as f64) / NANOUNIT,
        diff_sd(REALISTIC_COV), correlation(REALISTIC_COV));
    println!("No BayLum posterior/MCMC executed; nonintervention physical inference HOLD");
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn exact_original_matrix_cells_are_positive() {
        assert!(A > 0 && B > 0 && SIMPLISTIC_COV > 0 && REALISTIC_COV > 0);
        assert_eq!(A, 9_191_746);
        assert_eq!(B, 7_991_537);
        assert_eq!(SIMPLISTIC_COV, 7_616_071);
        assert_eq!(REALISTIC_COV, 2_152_365);
    }
    #[test]
    fn both_2_by_2_covariance_matrices_positive_definite() {
        assert!((A as i128) * (B as i128) > (SIMPLISTIC_COV as i128).pow(2));
        assert!((A as i128) * (B as i128) > (REALISTIC_COV as i128).pow(2));
    }
    #[test]
    fn exact_difference_variances_on_same_marginals() {
        assert_eq!(diff_variance_nano(SIMPLISTIC_COV), 1_951_141);
        assert_eq!(diff_variance_nano(REALISTIC_COV), 12_878_553);
        assert!(diff_variance_nano(REALISTIC_COV) > diff_variance_nano(SIMPLISTIC_COV));
    }
    #[test]
    fn bounded_effect_of_shared_error_on_reported_difference() {
        assert!((correlation(SIMPLISTIC_COV) - 0.88862150555).abs() < 1e-9);
        assert!((correlation(REALISTIC_COV) - 0.25113182726).abs() < 1e-9);
        assert!((diff_sd(SIMPLISTIC_COV) - 0.04417172172).abs() < 1e-9);
        assert!((diff_sd(REALISTIC_COV) - 0.11348371249).abs() < 1e-9);
        let variance_ratio = (diff_variance_nano(REALISTIC_COV) as f64)
            / (diff_variance_nano(SIMPLISTIC_COV) as f64);
        assert!((variance_ratio - 6.60052400108).abs() < 1e-9);
    }
}