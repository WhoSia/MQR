//! MQR 4.111 — Costas et al. (2012) Table 2 published row-level *summary* replay.
//! Source: Quaternary Geochronology 10, 16–23, Table 2.
//! DOI: 10.1016/j.quageo.2012.03.007
//! No underlying aliquot measurements were obtained.
//! Ages are integer years; sigmas are the corresponding authors' 1-sigma values.
//! These summaries share natural/history and dose-rate uncertainties; NO independent
//! Gaussian significance claim or independent raw-data replication is made.
#![forbid(unsafe_code)]
#[derive(Clone, Copy, Debug)]
struct Row {
    name: &'static str,
    expected: i32,
    expected_sd: i32,
    lbg: i32,
    lbg_sd: i32,
    ebg: i32,
    ebg_sd: i32,
    expected_dose_mgy: i32,
    ebg_dose_mgy: i32,
}
const ROWS: [Row; 13] = [
    Row { name: "GWD-0", expected: 98, expected_sd: 10, lbg: 180, lbg_sd: 20, ebg: 160, ebg_sd: 20, expected_dose_mgy: 73, ebg_dose_mgy: 119 },
    Row { name: "GWD-10", expected: 94, expected_sd: 9, lbg: 115, lbg_sd: 13, ebg: 89, ebg_sd: 9, expected_dose_mgy: 56, ebg_dose_mgy: 52 },
    Row { name: "GWD-20", expected: 90, expected_sd: 9, lbg: 140, lbg_sd: 15, ebg: 110, ebg_sd: 10, expected_dose_mgy: 55, ebg_dose_mgy: 65 },
    Row { name: "GWD-40", expected: 82, expected_sd: 8, lbg: 117, lbg_sd: 11, ebg: 86, ebg_sd: 8, expected_dose_mgy: 54, ebg_dose_mgy: 56 },
    Row { name: "GWD-60", expected: 75, expected_sd: 7, lbg: 118, lbg_sd: 11, ebg: 98, ebg_sd: 9, expected_dose_mgy: 53, ebg_dose_mgy: 70 },
    Row { name: "GWD-80", expected: 67, expected_sd: 7, lbg: 93, lbg_sd: 11, ebg: 72, ebg_sd: 8, expected_dose_mgy: 50, ebg_dose_mgy: 55 },
    Row { name: "GWD-100", expected: 59, expected_sd: 6, lbg: 120, lbg_sd: 13, ebg: 94, ebg_sd: 10, expected_dose_mgy: 41, ebg_dose_mgy: 66 },
    Row { name: "GWD-140", expected: 43, expected_sd: 4, lbg: 76, lbg_sd: 8, ebg: 65, ebg_sd: 9, expected_dose_mgy: 31, ebg_dose_mgy: 46 },
    Row { name: "GWD-160", expected: 35, expected_sd: 4, lbg: 110, lbg_sd: 10, ebg: 97, ebg_sd: 9, expected_dose_mgy: 26, ebg_dose_mgy: 71 },
    Row { name: "GWD-180", expected: 28, expected_sd: 3, lbg: 97, lbg_sd: 9, ebg: 77, ebg_sd: 7, expected_dose_mgy: 19, ebg_dose_mgy: 51 },
    Row { name: "GWD-200", expected: 20, expected_sd: 2, lbg: 77, lbg_sd: 10, ebg: 60, ebg_sd: 8, expected_dose_mgy: 13, ebg_dose_mgy: 41 },
    Row { name: "GWD-220", expected: 12, expected_sd: 1, lbg: 60, lbg_sd: 7, ebg: 40, ebg_sd: 5, expected_dose_mgy: 8, ebg_dose_mgy: 28 },
    Row { name: "GWD-245", expected: 2, expected_sd: 1, lbg: 47, lbg_sd: 8, ebg: 34, ebg_sd: 3, expected_dose_mgy: 1, ebg_dose_mgy: 23 },
];

fn intervals_overlap_at_two_sd(r: Row) -> bool {
    let a_lo = r.expected - 2 * r.expected_sd;
    let a_hi = r.expected + 2 * r.expected_sd;
    let b_lo = r.ebg - 2 * r.ebg_sd;
    let b_hi = r.ebg + 2 * r.ebg_sd;
    a_lo <= b_hi && b_lo <= a_hi
}

fn young() -> &'static [Row] { &ROWS[6..] }
fn ebg_bias(r: Row) -> i32 { r.ebg - r.expected }
fn lbg_bias(r: Row) -> i32 { r.lbg - r.expected }


fn dose_difference(r: Row) -> f64 {
    f64::from(r.ebg_dose_mgy - r.expected_dose_mgy)
}
fn mean_difference(rs: &[Row]) -> f64 {
    rs.iter().copied().map(dose_difference).sum::<f64>() / rs.len() as f64
}
fn young_loo_rmse(additive: bool) -> f64 {
    let data = young();
    let mut squared = 0.0;
    for (i, row) in data.iter().copied().enumerate() {
        let mut numerator = 0.0;
        let mut denominator = 0.0;
        let mut n_train = 0_usize;
        for (j, train) in data.iter().copied().enumerate() {
            if i != j {
                let x = f64::from(train.expected_dose_mgy);
                let y = f64::from(train.ebg_dose_mgy);
                if additive {
                    numerator += y - x;
                } else {
                    numerator += x * y;
                    denominator += x * x;
                }
                n_train += 1;
            }
        }
        let x_test = f64::from(row.expected_dose_mgy);
        let y_test = f64::from(row.ebg_dose_mgy);
        let prediction = if additive {
            x_test + numerator / n_train as f64
        } else {
            x_test * numerator / denominator
        };
        squared += (y_test - prediction).powi(2);
    }
    (squared / data.len() as f64).sqrt()
}

fn main() {
    println!("MQR 4.111 P3: published Costas 2012 Table 2 summary ONLY");
    println!("Control experiment: LBG 1.019 +/- 0.004 (n=78), EBG 1.011 +/- 0.007 (n=78).");
    println!("GWD-0 excluded from comparably recent chronology (authors: sediment boundary).");
    for r in ROWS {
        println!("{} expected={}±{}, LBG={}±{}, EBG={}±{}, EBG bias={}",
            r.name, r.expected, r.expected_sd, r.lbg, r.lbg_sd, r.ebg, r.ebg_sd, ebg_bias(r));
        println!("{} LBG bias={} years", r.name, lbg_bias(r));
    }
    let n_young = young().len();
    let total_bias: i32 = young().iter().copied().map(ebg_bias).sum();
    let disjoint = young().iter().copied()
        .filter(|&r| !intervals_overlap_at_two_sd(r)).count();
    println!("young n={}, sum_bias={} years, mean_bias={:.3} years, disjoint 2-sigma band pairs={}",
        n_young, total_bias, f64::from(total_bias) / n_young as f64, disjoint);
    println!("young dose mean residual={:.3} mGy; older-five mean={:.3} mGy",
        mean_difference(young()), mean_difference(&ROWS[1..6]));
    println!("young one-parameter leave-one-out RMSE: additive={:.3} mGy, proportional={:.3} mGy",
        young_loo_rmse(true), young_loo_rmse(false));
    println!("MODERN-ANALOGUE SOURCE WITNESS: GWD-245 original EBG De=23±5 mGy; separately bleached aliquots residual=8±1 mGy, authors' contrast=15 mGy; historical expected De=1±1 mGy.");
    println!("These are different aliquots of the same source sample; no paired individual-grain restoration inferred.");
    println!("MODEL STATUS: descriptive summaries and post-hoc diagnostics, not fitted OSL mechanisms.");
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn all_thirteen_printed_rows_and_named_exclusion() {
        assert_eq!(ROWS.len(), 13);
        assert_eq!(ROWS[0].name, "GWD-0");
        assert_eq!(ROWS[0].expected, 98);
        assert_eq!(ROWS[0].ebg, 160);
        assert_eq!(ROWS[12].name, "GWD-245");
        assert_eq!(ROWS[12].expected, 2);
        assert_eq!(ROWS[12].ebg, 34);
    }
    #[test]
    fn all_young_recovered_control_passed_but_ages_biased() {
        // Control pass is the paper's aggregate n=78 experiment, not an aliquot-level replay.
        assert_eq!(young().len(), 7);
        assert!(young().iter().copied().all(|r| ebg_bias(r) > 0));
        assert_eq!(young().iter().copied().map(ebg_bias).sum::<i32>(), 268);
        assert!(ROWS.iter().copied().all(|r| r.lbg >= r.ebg));
    }
    #[test]
    fn six_of_seven_young_disjoint_as_individual_two_sigma_bands() {
        assert_eq!(young().iter().copied()
            .filter(|&r| !intervals_overlap_at_two_sd(r)).count(), 6);
        let special = young().iter().copied().find(|r| r.name == "GWD-140").unwrap();
        assert!(intervals_overlap_at_two_sd(special));
        assert_eq!(ebg_bias(special), 22);
    }
    #[test]
    fn historical_mismatch_at_three_named_examples() {
        assert_eq!(ebg_bias(ROWS[6]), 35);   // GWD-100
        assert_eq!(ebg_bias(ROWS[8]), 62);   // GWD-160
        assert_eq!(ebg_bias(ROWS[12]), 32);  // GWD-245
        assert_eq!(lbg_bias(ROWS[12]), 45);
    }
    #[test]
    fn source_printed_dose_endpoints_and_residuals() {
        assert_eq!(ROWS[0].expected_dose_mgy, 73);
        assert_eq!(ROWS[0].ebg_dose_mgy, 119);
        assert_eq!(ROWS[6].expected_dose_mgy, 41);
        assert_eq!(ROWS[6].ebg_dose_mgy, 66);
        assert_eq!(ROWS[12].expected_dose_mgy, 1);
        assert_eq!(ROWS[12].ebg_dose_mgy, 23);
        assert!((mean_difference(young()) - 187.0 / 7.0).abs() < 1e-10);
        assert!((mean_difference(&ROWS[1..6]) - 6.0).abs() < 1e-10);
    }
    #[test]
    fn source_table_descriptive_leave_one_out_dose_models() {
        let add = young_loo_rmse(true);
        let mult = young_loo_rmse(false);
        assert!((add - 10.5409255339).abs() < 1e-7);
        assert!((mult - 19.7591388094).abs() < 1e-7);
        assert!(add < mult);
    }
    #[test]
    fn authors_modern_analogue_intervention_is_unpaired() {
        // Costas et al. (2012), section 5: separate 24 aliquots of GWD-245
        // exposed to daylight for one week vs source natural signal.
        // Reported summary results in mGy. No within-aliquot pairing is claimed.
        let natural_ebg = 23;
        let following_bleach = 8;
        let historical_expected = 1;
        assert_eq!(natural_ebg - following_bleach, 15);
        assert_eq!(natural_ebg - historical_expected, 22);
        assert_eq!(natural_ebg - following_bleach - historical_expected, 14);
        assert_eq!(ROWS[12].ebg_dose_mgy, natural_ebg);
        assert_eq!(ROWS[12].expected_dose_mgy, historical_expected);
    }
    #[test]
    fn descriptive_age_group_contrast_is_robust_to_one_young_removal() {
        let baseline = mean_difference(&ROWS[1..6]);
        let youth = young();
        assert!((baseline - 6.0).abs() < 1e-12);
        for omit in 0..youth.len() {
            let residual_sum: f64 = youth.iter().enumerate()
                .filter(|(j,_)| *j != omit)
                .map(|(_,r)| dose_difference(*r)).sum();
            assert!(residual_sum / (youth.len() - 1) as f64 > baseline);
        }
        // Shared historical-age model, nonindependent grains and lack of raw
        // per-aliquot trajectories prevent causal or inferential interpretation.
    }
}