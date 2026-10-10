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
}
const ROWS: [Row; 13] = [
    Row { name: "GWD-0", expected: 98, expected_sd: 10, lbg: 180, lbg_sd: 20, ebg: 160, ebg_sd: 20 },
    Row { name: "GWD-10", expected: 94, expected_sd: 9, lbg: 115, lbg_sd: 13, ebg: 89, ebg_sd: 9 },
    Row { name: "GWD-20", expected: 90, expected_sd: 9, lbg: 140, lbg_sd: 15, ebg: 110, ebg_sd: 10 },
    Row { name: "GWD-40", expected: 82, expected_sd: 8, lbg: 117, lbg_sd: 11, ebg: 86, ebg_sd: 8 },
    Row { name: "GWD-60", expected: 75, expected_sd: 7, lbg: 118, lbg_sd: 11, ebg: 98, ebg_sd: 9 },
    Row { name: "GWD-80", expected: 67, expected_sd: 7, lbg: 93, lbg_sd: 11, ebg: 72, ebg_sd: 8 },
    Row { name: "GWD-100", expected: 59, expected_sd: 6, lbg: 120, lbg_sd: 13, ebg: 94, ebg_sd: 10 },
    Row { name: "GWD-140", expected: 43, expected_sd: 4, lbg: 76, lbg_sd: 8, ebg: 65, ebg_sd: 9 },
    Row { name: "GWD-160", expected: 35, expected_sd: 4, lbg: 110, lbg_sd: 10, ebg: 97, ebg_sd: 9 },
    Row { name: "GWD-180", expected: 28, expected_sd: 3, lbg: 97, lbg_sd: 9, ebg: 77, ebg_sd: 7 },
    Row { name: "GWD-200", expected: 20, expected_sd: 2, lbg: 77, lbg_sd: 10, ebg: 60, ebg_sd: 8 },
    Row { name: "GWD-220", expected: 12, expected_sd: 1, lbg: 60, lbg_sd: 7, ebg: 40, ebg_sd: 5 },
    Row { name: "GWD-245", expected: 2, expected_sd: 1, lbg: 47, lbg_sd: 8, ebg: 34, ebg_sd: 3 },
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
}