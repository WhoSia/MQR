//! MQR-4.103 internal P2: design positivity, finite identification, fallible labels.
//! Entirely synthetic. Fixed three-unit truth and label vectors; no QTDB truth.
use std::collections::BTreeMap;

#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd)]
struct Receipt { first: u8, second_index: usize, second: u8 }

fn bits(x: u8) -> [u8; 3] { [(x >> 2) & 1, (x >> 1) & 1, x & 1] }
fn total(x: u8) -> u8 { bits(x).iter().sum() }
fn xor_labels(truth: u8, errors: u8) -> [u8; 3] {
    let t = bits(truth);
    let e = bits(errors);
    [t[0] ^ e[0], t[1] ^ e[1], t[2] ^ e[2]]
}
fn indices(first: u8) -> (usize, usize) {
    if first == 0 { (1, 2) } else { (2, 1) }
}
/// The first label is read with certainty. At stage two the preferred index
/// receives weight 4 for deterministic choice, or weight 3 of 4 for random choice.
/// The other index receives weight 0 or 1 respectively. Always stop after 2.
fn law(a: [u8; 3], positive: bool) -> Vec<(Receipt, u8)> {
    let (fav, alt) = indices(a[0]);
    let mut paths = vec![(Receipt { first: a[0], second_index: fav, second: a[fav] },
                          if positive { 3 } else { 4 })];
    if positive {
        paths.push((Receipt { first: a[0], second_index: alt, second: a[alt] }, 1));
    }
    paths.sort();
    paths
}
fn truth_law_classes(positive: bool) -> BTreeMap<Vec<(Receipt, u8)>, Vec<u8>> {
    let mut classes = BTreeMap::new();
    for truth in 0..8u8 {
        classes.entry(law(bits(truth), positive))
            .or_insert_with(Vec::new).push(truth);
    }
    classes
}
/// Assumes labels equal truths. Exact expectation of an inverse-inclusion
/// total under conditional stage-two inclusion probabilities (3/4, 1/4).
/// Numerator/12 is the expected estimated total; no floating rounding.
fn ht_expectation_numerator(truth: u8) -> i32 {
    let t = bits(truth);
    let (fav, alt) = indices(t[0]);
    let first = t[0] as i32;
    let preferred = t[fav] as i32;
    let other = t[alt] as i32;
    // A chosen preferred value contributes preferred/(3/4)=4*preferred/3.
    // A chosen alternative contributes other/(1/4)=4*other.
    3 * (3 * first + 4 * preferred) + (3 * first + 12 * other)
}
/// Sharp finite-world total bounds for ONE realized receipt.
/// The optional error limit is an EXTERNAL, hypothetical bound on
/// the total number of differences between A and T among all three units.
fn receipt_bounds(receipt: Receipt, max_errors: Option<u32>) -> (u8, u8) {
    let mut min_t = 4;
    let mut max_t = 0;
    for truth in 0..8u8 {
        for errors in 0..8u8 {
            if max_errors.map_or(false, |k| errors.count_ones() > k) { continue; }
            let a = xor_labels(truth, errors);
            if law(a, true).iter().any(|(r, w)| *r == receipt && *w > 0) {
                min_t = min_t.min(total(truth));
                max_t = max_t.max(total(truth));
            }
        }
    }
    assert!(min_t <= max_t, "receipt outside declared design support");
    (min_t, max_t)
}
/// Sharp total bounds if the FULL probability law has recovered stable A=111,
/// not merely one realized receipt. Only T and error assignments vary.
fn full_label_bounds(a: [u8; 3], max_errors: Option<u32>) -> (u8, u8) {
    let mut min_t = 4;
    let mut max_t = 0;
    for truth in 0..8u8 {
        for errors in 0..8u8 {
            if max_errors.map_or(false, |k| errors.count_ones() > k) { continue; }
            if xor_labels(truth, errors) == a {
                min_t = min_t.min(total(truth));
                max_t = max_t.max(total(truth));
            }
        }
    }
    assert!(min_t <= max_t);
    (min_t, max_t)
}
pub(crate) fn run() {
    let deterministic = truth_law_classes(false);
    let positive = truth_law_classes(true);
    assert_eq!(deterministic.len(), 4);
    assert!(deterministic.values().all(|v| v.len() == 2));
    assert_eq!(positive.len(), 8);
    assert!(positive.values().all(|v| v.len() == 1));
    for t in 0..8u8 {
        assert_eq!(ht_expectation_numerator(t), 12 * total(t) as i32);
    }
    // A0=1, A2=1 was observed; A1 never read in this path.
    let r = Receipt { first: 1, second_index: 2, second: 1 };
    assert_eq!(receipt_bounds(r, Some(0)), (2, 3));
    assert_eq!(receipt_bounds(r, Some(1)), (1, 3));
    assert_eq!(receipt_bounds(r, None), (0, 3));
    assert_eq!(full_label_bounds([1, 1, 1], Some(1)), (2, 3));
    assert_eq!(full_label_bounds([1, 1, 1], None), (0, 3));
    // Observed-law equivalence despite different true prevalence:
    // T=000,E=000 versus T=111,E=111 both produce stable A=000.
    assert_eq!(law(xor_labels(0, 0), true),
               law(xor_labels(7, 7), true));
    assert_ne!(total(0), total(7));
    println!("MQR4103_P2_DETERMINISTIC_TRUTH_LAWS={} POSITIVE_TRUTH_LAWS={}",deterministic.len(),positive.len());
    println!("MQR4103_P2_ALL_8_TRUTHS_HT_DESIGN_EXPECTATION_EXACT_PASS");
    println!("MQR4103_P2_ONE_RECEIPT_TOTAL_BOUNDS_K0=2..3_K1=1..3_UNCERTIFIED=0..3");
    println!("MQR4103_P2_FULL_LABEL111_TOTAL_BOUNDS_K1=2..3_UNCERTIFIED=0..3");
    println!("MQR4103_P2_FINITE_DESIGN_AND_FALLIBLE_LABEL_COURT_PASS;EXTERNAL_TRUTH_HOLD");
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn zero_vs_positive_support() {
        assert_eq!(truth_law_classes(false).len(), 4);
        assert_eq!(truth_law_classes(true).len(), 8);
    }
    #[test] fn ht_is_design_unbiased_for_each_fixed_truth() {
        for t in 0..8u8 { assert_eq!(ht_expectation_numerator(t),12*total(t) as i32); }
    }
    #[test] fn positive_design_does_not_resolve_single_history() {
        let r=Receipt { first: 1, second_index: 2, second: 1 };
        assert_eq!(receipt_bounds(r,Some(0)),(2,3));
    }
    #[test] fn error_budget_is_external_and_sharp_by_exhaustion() {
        let r=Receipt { first: 1, second_index: 2, second: 1 };
        assert_eq!(receipt_bounds(r,Some(1)),(1,3));
        assert_eq!(receipt_bounds(r,None),(0,3));
        assert_eq!(full_label_bounds([1,1,1],Some(1)),(2,3));
        assert_eq!(full_label_bounds([1,1,1],None),(0,3));
    }
    #[test] fn even_positive_policy_cannot_repair_unrestricted_label_error() {
        assert_eq!(law(xor_labels(0,0),true),law(xor_labels(7,7),true));
        assert_eq!(total(0),0);
        assert_eq!(total(7),3);
    }
}
