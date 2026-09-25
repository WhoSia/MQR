use std::{env, process};
use unicode_normalization::UnicodeNormalization;

const BRIDGE: &[(&str, &[u32])] = &[
    ("B01", &[0x0041, 0x030A]),
    ("B02", &[0x0065, 0x0301]),
    ("B03", &[0x006F, 0x0308]),
    ("B04", &[0x0043, 0x0327]),
    ("B05", &[0x212B]),
    ("B06", &[0x1100, 0x1161]),
];

const DIRECT: &[(&str, &[u32])] = &[
    ("H01", &[0x16D69, 0x16D68]),
    ("H02", &[0x16D69, 0x16D67, 0x16D68]),
    ("H03", &[0x1138B, 0x113C5]),
    ("H04", &[0x113C2, 0x113C5]),
    ("H05", &[0x1138B, 0x113C7]),
    ("H06", &[0x113C2, 0x113C8]),
];

fn cases(mode: &str) -> &'static [(&'static str, &'static [u32])] {
    match mode {
        "bridge" => BRIDGE,
        "direct" => DIRECT,
        _ => {
            eprintln!("mode must be bridge or direct");
            process::exit(2);
        }
    }
}

fn to_string(cps: &[u32]) -> String {
    cps.iter()
        .map(|&cp| char::from_u32(cp).expect("valid frozen scalar"))
        .collect()
}

fn hexes(s: &str) -> String {
    s.chars()
        .map(|ch| format!("{:04X}", ch as u32))
        .collect::<Vec<_>>()
        .join("+")
}

fn main() {
    let mode = env::args().nth(1).unwrap_or_else(|| "bridge".to_owned());
    println!("case_id\tstate");
    for (id, cps) in cases(&mode) {
        let input = to_string(cps);
        let output: String = input.nfc().collect();
        println!("{id}\t{}", hexes(&output));
    }
}
