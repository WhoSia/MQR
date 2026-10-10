//! MQR 4.110: exact-published-table reproducibility, not reconstructed raw measurements.
//! Regnault (1847), printed pp. 240-241: graphical reductions, 250 C air row.
//! Strong rivals GUM/VIM/Tal/Chang remain; arithmetic alone provides no traceability certificate.
fn main() {
    const T_CENTI: i64 = 25_000;
    const READINGS: [(&str, i64); 4] = [
        ("Choisy-crystal", 25_300),
        ("ordinary-glass-5", 25_005),
        ("green-glass-10", 25_185),
        ("Swedish-glass-11", 25_144),
    ];
    let mut min = i64::MAX;
    let mut max = i64::MIN;
    for (name, indicated) in READINGS {
        assert!(indicated >= T_CENTI);
        println!("{name}: indicated={} centi-C; offset={} centi-C", indicated, indicated - T_CENTI);
        min = min.min(indicated);
        max = max.max(indicated);
    }
    assert_eq!(max - min, 295);
    println!("MQR4110_P2_REGNAULT_PUBLISHED_GRAPH_TABLE_PASS;TRACEABILITY_HOLD;NOVELTY_HOLD");
}
#[cfg(test)]
mod tests {
    #[test]
    fn identical_reported_value_is_not_a_certificate() {
        let numerical_table = [25005_i64, 25005_i64];
        assert_eq!(numerical_table[0], numerical_table[1]);
        // Documentary chain evidence is not derivable from table equality.
        let independently_verified_chain = [false, false];
        assert!(independently_verified_chain.iter().all(|x| !x));
    }
    #[test]
    fn published_four_glass_spread_in_centi_celsius() {
        let r = [25300_i64, 25005, 25185, 25144];
        assert_eq!(r.iter().max().unwrap() - r.iter().min().unwrap(), 295);
    }
}
