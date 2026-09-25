use regex::Regex;
use std::{env, process};

const BRIDGE: &[(&str, &str, &str)] = &[
    ("B01", "abc", "xxabcxx"),
    ("B02", "^[a-z]+$", "mosaic"),
    ("B03", "^(cat|dog)$", "dog"),
    ("B04", "^ab*c$", "abbbc"),
    ("B05", "^[0-9]{2,4}$", "314"),
    ("B06", "^(ha)+!$", "hahaha!"),
];

const DIRECT: &[(&str, &str, &str)] = &[
    ("H01", r"^\p{Greek}+$", "ΔΩ"),
    ("H02", r"^\p{Script=Han}+$", "漢字"),
    ("H03", r"^\p{Letter}+$", "Ångström"),
    ("H04", r"^\p{Nd}+$", "١٢٣"),
    ("H05", r"^\w+$", "한글42"),
    ("H06", r"^[\p{Latin}\p{Greek}]+$", "AΩ"),
];

fn cases(mode: &str) -> &'static [(&'static str, &'static str, &'static str)] {
    match mode {
        "bridge" => BRIDGE,
        "direct" => DIRECT,
        _ => {
            eprintln!("mode must be bridge or direct");
            process::exit(2);
        }
    }
}

fn main() {
    let mode = env::args().nth(1).unwrap_or_else(|| "bridge".to_owned());
    println!("case_id\tstate");
    for (id, pattern, text) in cases(&mode) {
        let state = match Regex::new(pattern) {
            Ok(re) => {
                if re.is_match(text) {
                    "MATCH_1"
                } else {
                    "MATCH_0"
                }
            }
            Err(_) => "COMPILE_ERR",
        };
        println!("{id}\t{state}");
    }
}
