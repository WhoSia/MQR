//! MQR-4.111 P7 — original published Costas same-site rival audit and provenance gate.
//! Sources: Costas et al. (2012), doi:10.1016/j.quageo.2012.03.007,
//! Table 2; Discussion sections 5-6, pages 20–22.
//! Original Guérin et al. (2021) supplemental Rmd Example 5: C14age <- c(43400).
//! NOT individual aliquot data. NOT a postulated new physical measurement law.
#![forbid(unsafe_code)]

#[derive(Clone, Copy, Debug)]
struct PublishedSite {
    name: &'static str,
    expected_dose: i32, expected_sd: i32,
    natural_ebg_180: i32, natural_sd: i32,
    natural_ebg_160: i32, lower_sd: i32,
}
const SITES: [PublishedSite; 3] = [
    PublishedSite {name:"GWD-80", expected_dose:50, expected_sd:5, natural_ebg_180:55, natural_sd:5, natural_ebg_160:56, lower_sd:2},
    PublishedSite {name:"GWD-140", expected_dose:31, expected_sd:3, natural_ebg_180:46, natural_sd:3, natural_ebg_160:50, lower_sd:2},
    PublishedSite {name:"GWD-245", expected_dose:1, expected_sd:1, natural_ebg_180:23, natural_sd:5, natural_ebg_160:18, lower_sd:2},
];
fn intervals_disjoint(a: i32, sigma_a: i32, b: i32, sigma_b: i32, k: i32) -> bool {
    a + k * sigma_a < b - k * sigma_b || b + k * sigma_b < a - k * sigma_a
}
fn age_bias(ebg_years: i32, expected_years: i32) -> i32 {ebg_years-expected_years}
const YOUNG_AGE_PAIRS: [(i32,i32);7] = [
    (94,59),(65,43),(97,35),(77,28),(60,20),(40,12),(34,2),
];

// A record with only sample/site-level custody is NOT an original aliquot observation.
// P7 is an authority gate over proposed joins, not a replacement for source radiocarbon.
#[derive(Debug,Clone,Copy,PartialEq,Eq)]
enum MeasurementKind { Natural, Cleared, HistoricalAnchor, IllustrativeRadiocarbon }
#[derive(Debug,Clone,Copy)]
struct Witness {
    study: &'static str, site: Option<&'static str>,
    aliquot: Option<&'static str>, kind: MeasurementKind,
}
fn same_measured_aliquot(a: Witness,b: Witness) -> bool {
    a.study == b.study && a.site.is_some() && a.site == b.site
        && a.aliquot.is_some() && a.aliquot == b.aliquot
}
// A site-level source chronology join is an admissible published SUMMARY contrast;
// it is not same-aliquot pairing, raw chronometric reconstruction or mechanism.
fn published_site_contrast(a: Witness,b: Witness) -> bool {
    a.study == b.study && a.site.is_some() && a.site == b.site &&
        (a.kind == MeasurementKind::HistoricalAnchor || b.kind == MeasurementKind::HistoricalAnchor) &&
        a.kind != MeasurementKind::IllustrativeRadiocarbon &&
        b.kind != MeasurementKind::IllustrativeRadiocarbon
}
fn main() {
    println!("P7: same-site published dose comparisons (mGy), not paired original aliquots");
    for row in SITES {
        let change=row.natural_ebg_160-row.natural_ebg_180;
        println!("{}: expected={}±{}, original 180={}±{}, source lower preheat 160={}±{}, change={:+}",
            row.name,row.expected_dose,row.expected_sd,row.natural_ebg_180,row.natural_sd,row.natural_ebg_160,row.lower_sd,change);
    }
    println!("At 2 individual 1-sigma bounds, GWD140 and GWD245 160-condition observations remain disjoint from source's expected dose.");
    println!("Guérin FER illustrative C14 43400±400 yr has no verified same-layer raw join; BayLum posterior not run.");
    let disjoint_two_sd: Vec<&str> = SITES.iter()
        .filter(|s| intervals_disjoint(s.expected_dose, s.expected_sd, s.natural_ebg_160, s.lower_sd, 2))
        .map(|s| s.name).collect();
    println!("2SD individual marginal intervals disjoint: {:?}", disjoint_two_sd);
    let biases: Vec<i32> = YOUNG_AGE_PAIRS.iter().map(|(a,b)| age_bias(*a, *b)).collect();
    println!("Published young-seven age residuals (years): {:?}; values above 40: {}",
        biases, biases.iter().filter(|&&x| x>40).count());
    let natural = Witness {study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::Natural};
    let bleached = Witness {study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::Cleared};
    let historic = Witness {study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::HistoricalAnchor};
    let c14example = Witness {study:"Guerin2021",site:None,aliquot:None,kind:MeasurementKind::IllustrativeRadiocarbon};
    println!("Costas natural vs cleared same original aliquot? {}; site/history summary join? {}; FER illustrative join? {}",
        same_measured_aliquot(natural,bleached),
        published_site_contrast(natural,historic),
        published_site_contrast(natural,c14example));
    println!("No original GWD aliquot trace, raw GPR chronology covariance, or unique component attribution available.");
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn three_origins_and_distinct_reported_lower_temperature_values() {
        assert_eq!(SITES.len(),3);
        assert_eq!(SITES[0].natural_ebg_160,56);
        assert_eq!(SITES[1].natural_ebg_160,50);
        assert_eq!(SITES[2].natural_ebg_160,18);
    }
    #[test]
    fn lower_preheat_is_not_uniformly_lower_than_original_180_condition() {
        let changes:Vec<i32>=SITES.iter().map(|s|s.natural_ebg_160-s.natural_ebg_180).collect();
        assert_eq!(changes, vec![1,4,-5]);
    }
    #[test]
    fn two_source_intervals_remain_disjoint_at_two_times_reported_one_sigma() {
        let rejections:Vec<&str>=SITES.iter().filter(|s|
            intervals_disjoint(s.expected_dose,s.expected_sd,s.natural_ebg_160,s.lower_sd,2))
            .map(|s|s.name).collect();
        assert_eq!(rejections,vec!["GWD-140","GWD-245"]);
        // These are individual marginal bands, never a covariance-aware significance test.
    }
    #[test]
    fn seven_printed_age_differences_exceed_papers_approximate_prose_upper_bound_twice() {
        let d:Vec<i32>=YOUNG_AGE_PAIRS.iter().map(|(a,b)|age_bias(*a,*b)).collect();
        assert_eq!(d,vec![35,22,62,49,40,28,32]);
        assert_eq!(d.iter().filter(|&&v|v>40).count(),2);
        // 10–40 years in the article abstract/discussion is approximate and internally
        // inconsistent with the direct age differences for two rows.
    }
    #[test]
    fn same_site_same_source_does_not_create_same_aliquot_witness() {
        let a=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::Natural};
        let b=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::Cleared};
        assert!(!same_measured_aliquot(a,b));
        let c=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:Some("verified_a1"),kind:MeasurementKind::Natural};
        let d=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:Some("verified_a1"),kind:MeasurementKind::Cleared};
        assert!(same_measured_aliquot(c,d));
        assert!(!same_measured_aliquot(c,a));
    }
    #[test]
    fn historical_summary_anchor_is_joinable_only_at_admissible_site_level() {
        let natural=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::Natural};
        let model=Witness{study:"Costas2012",site:Some("GWD-245"),aliquot:None,kind:MeasurementKind::HistoricalAnchor};
        assert!(published_site_contrast(natural,model));
        assert!(!same_measured_aliquot(natural,model));
        let illustrative=Witness{study:"Guerin2021",site:None,aliquot:None,kind:MeasurementKind::IllustrativeRadiocarbon};
        let fer=Witness{study:"Guerin2021",site:Some("FER1"),aliquot:None,kind:MeasurementKind::Natural};
        assert!(!published_site_contrast(fer,illustrative));
        assert!(!published_site_contrast(model,fer));
    }
}
