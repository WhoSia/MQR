use std::{env, process};

const BRIDGE: &[(&str, &str)] = &[
    ("B01", "answer = 42\n"),
    ("B02", "values = [1, 2.5, 3]\n"),
    ("B03", "[server]\nhost = \"localhost\"\nport = 8080\n"),
    ("B04", "point = { x = 1, y = 2 }\n"),
    ("B05", "time = 07:32:00\n"),
    ("B06", "text = \"\"\"\nhello\nworld\n\"\"\"\n"),
];

const HELDOUT: &[(&str, &str)] = &[
    ("H01", "tbl = {\n  a = 1,\n  b = 2,\n}\n"),
    (
        "H02",
        r#"s = "\x61"
"#,
    ),
    (
        "H03",
        r#"s = "\e[31m"
"#,
    ),
    ("H04", "time = 07:32\n"),
];

fn cases(mode: &str) -> &'static [(&'static str, &'static str)] {
    match mode {
        "bridge" => BRIDGE,
        "heldout" => HELDOUT,
        _ => {
            eprintln!("mode must be bridge or heldout");
            process::exit(2);
        }
    }
}

fn main() {
    let mode = env::args().nth(1).unwrap_or_else(|| "bridge".to_owned());
    println!("case_id\tstate");
    for (id, input) in cases(&mode) {
        let state = if input.parse::<toml::Value>().is_ok() {
            "OK"
        } else {
            "ERR"
        };
        println!("{id}\t{state}");
    }
}
