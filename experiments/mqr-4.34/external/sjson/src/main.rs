use serde_json::Value;
use std::{env, process};

const BRIDGE: &[(&str, &str)] = &[
    ("B01", "null"),
    ("B02", "123.5"),
    ("B03", r#""alpha\nbeta""#),
    ("B04", "[1,2,3]"),
    ("B05", r#"{"a":1,"b":2}"#),
    ("B06", r#"{"outer":[1,{"k":"v"}]}"#),
];

const DIRECT: &[(&str, &str)] = &[
    ("H01", "true"),
    ("H02", "-7.25e2"),
    ("H03", r#""\u03b1\u03b2""#),
    ("H04", r#"[true,null,"x"]"#),
    ("H05", r#"{"x":false,"y":"z"}"#),
    ("H06", r#"{"items":[{"n":2},3],"ok":true}"#),
];

fn cases(mode: &str) -> &'static [(&'static str, &'static str)] {
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
    for (id, input) in cases(&mode) {
        let state = match serde_json::from_str::<Value>(input) {
            Ok(v) => format!("OK:{}", serde_json::to_string(&v).unwrap()),
            Err(_) => "ERR".to_owned(),
        };
        println!("{id}\t{state}");
    }
}
