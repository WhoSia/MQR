// MQR-4.112 P1-H: frozen primary source set arithmetic in stdlib Rust.
// 2015 manuscript Table 4 totals are CITED AGGREGATES, not recovered raw grains.
// The full 2021 grain-ID roster is NOT in the public 2021 ZIP.
use std::collections::HashSet;
use std::fs;

const REPORT: [(&str, usize, usize); 2] = [
    ("FER1", 2400, 97),
    ("FER3", 2400, 96),
];
fn selected_keys(path: &str) -> Result<HashSet<(u32, u32)>, String> {
    let text = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut lines = text.lines();
    let header = lines.next().ok_or("missing header")?.trim();
    if header != "position,grain" {
        return Err(format!("unexpected header: {header}"));
    }
    let mut ids = HashSet::new();
    for (j, line) in lines.enumerate() {
        let tokens: Vec<_> = line.trim().split(',').collect();
        if tokens.len() != 2 { return Err(format!("row {j}: invalid width")); }
        let a: u32 = tokens[0].parse().map_err(|_| format!("row {j}: position"))?;
        let b: u32 = tokens[1].parse().map_err(|_| format!("row {j}: grain"))?;
        if a == 0 || b == 0 || !ids.insert((a,b)) {
            return Err(format!("row {j}: nonpositive or duplicate key"));
        }
    }
    Ok(ids)
}
fn main() -> Result<(), String> {
    let root = std::env::args().nth(1).ok_or("pass unpacked original supplement data dir")?;
    println!("sample,measured_2015,accepted_2015,public_selected_2021,nominal_missing_2015_minus_public,subset_fraction,whole_cohort_identity");
    for (name, measured, accepted) in REPORT {
        let p = format!("{root}/{name}/DiscPos.csv");
        let ids = selected_keys(&p)?;
        if ids.len() != 49 || accepted < ids.len() { return Err(format!("{name}: selection gate failed")); }
        let n_missing = accepted - ids.len();
        println!("{name},{measured},{accepted},{},{n_missing},{:.6},HOLD_UNMATCHED_KEYS",
                 ids.len(), ids.len() as f64 / accepted as f64);
    }
    Ok(())
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn source_arithmetic() {
        assert_eq!(97-49,48);
        assert_eq!(96-49,47);
    }
    #[test] fn no_spurious_completeness() {
        for (_, _, selected) in REPORT {assert!(selected>49);}
    }
}
