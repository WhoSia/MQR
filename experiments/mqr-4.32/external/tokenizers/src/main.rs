use std::{env, process};

use tokenizers::{
    TokenizerBuilder, models::wordlevel::WordLevel, pre_tokenizers::whitespace::Whitespace,
};

const BRIDGE: &[(&str, &str)] = &[
    ("B01", "alpha beta"),
    ("B02", "alpha   gamma"),
    ("B03", "한글 테스트"),
    ("B04", "mix CASE 123"),
    ("B05", "alpha ! beta"),
    ("B06", "unknown beta"),
];

const HELDOUT: &[(&str, &str)] = &[
    ("H01", "beta gamma"),
    ("H02", "테스트 한글 alpha"),
    ("H03", "123 123 beta"),
    ("H04", "CASE unknown"),
    ("H05", "gamma ? alpha"),
    ("H06", ""),
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

fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let mode = env::args().nth(1).unwrap_or_else(|| "bridge".to_owned());
    let model = WordLevel::from_file(
        "experiments/mqr-4.32/external/tokenizers/vocab.json",
        "[UNK]".to_owned(),
    )?;

    let tokenizer = TokenizerBuilder::new()
        .with_model(model)
        .with_pre_tokenizer(Some(Whitespace))
        .build()?;

    println!("case_id\tids\ttokens");
    for (id, input) in cases(&mode) {
        let encoding = tokenizer.encode(*input, false)?;
        let ids = encoding
            .get_ids()
            .iter()
            .map(u32::to_string)
            .collect::<Vec<_>>()
            .join(",");
        let tokens = encoding.get_tokens().join("\u{001f}");
        println!("{id}\t{ids}\t{tokens}");
    }
    Ok(())
}
