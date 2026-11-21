"""Offline lexical profile of exported MQR Chat Archives (1..42).

Deliberately stores category counts only, never copies private prompt text into
public aggregate JSON. Regex categories overlap and include pasted text.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CAPTURE = re.compile(r'(?:^|\n)## Prompt:\s*\n([\s\S]*?)(?=\n## Response:|\n## Prompt:|$)')
STAMP = re.compile(r'^20\d\d[.\-년\s\d월일오전후:]+')
MARKERS = {
    'continuation_marker': r'(^|\s)(ㄱㄱ|가자|가보자|계속|진행해|쭉)',
    'archive_review_marker': r'복습|아카이브|archive|이전 채팅|독트린|역추적|계보|초심',
    'literature_intake_marker': r'미보유|00_INTAKE|00 폴더|원문|문헌|읽어|읽고|정독|논문|intake|harvest',
    'repo_record_marker': r'커밋|깃헙|github|노션|notion|Drive|저장소|Real Lang',
    'direction_change_marker': r'초심|방향|매몰|독창|야심|지엽|본질|패러다임의 패러다임|반성|성찰|연구 태도',
    'grand_concept_marker': r'외계|상대성|원시항|패러다임|쿤|수학의|수학적 존재|물리학|법칙|다른 과학|과학 자체|아리스토텔레스|우주',
}
REGEX = {k: re.compile(v, re.IGNORECASE) for k, v in MARKERS.items()}
FIELDS = ('prompt_blocks', 'short_prompt_le110_chars', 'long_prompt_gt1500_chars', *MARKERS)


def profile_text(text: str, archive_number: int) -> dict[str, int]:
    if not 1 <= archive_number <= 42:
        raise ValueError('Only the original 42 archives are in scope')
    # Provider text fetches already normalize CRLF. Raw exported .md may not.
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    captured = [m.group(1).strip() for m in CAPTURE.finditer(text)]
    if not captured:
        raise ValueError(f'No recognizable Prompt blocks in MQR {archive_number}.md')
    normalized = [re.sub(r'\s+', ' ', STAMP.sub('', p)).strip() for p in captured]
    result = {
        'archive_number': archive_number,
        'prompt_blocks': len(normalized),
        'short_prompt_le110_chars': sum(len(p) <= 110 for p in normalized),
        'long_prompt_gt1500_chars': sum(len(p) > 1500 for p in normalized),
    }
    result.update({k: sum(bool(rx.search(p)) for p in normalized) for k, rx in REGEX.items()})
    return result


def profile_directory(root: Path) -> dict:
    if not root.is_dir():
        raise NotADirectoryError(root)
    rows = []
    for number in range(1, 43):
        path = root / f'MQR {number}.md'
        if not path.is_file():
            raise FileNotFoundError(f'Missing one of 42 canonical archives: {path}')
        rows.append(profile_text(path.read_text(encoding='utf-8-sig'), number))

    def total(chunk):
        return {key: sum(row[key] for row in chunk) for key in FIELDS}

    return {
        'protocol': 'MQR_5_4_prompt_corpus_42_lexical_v1',
        'status': 'EXPLORATORY_NONEXCLUSIVE_LEXICAL_PROFILE',
        'num_archives': len(rows),
        'total': total(rows),
        'three_epoch_totals': [
            {'range': f'{lo}-{hi}', **total(rows[lo-1:hi])}
            for lo, hi in ((1, 14), (15, 28), (29, 42))
        ],
        'rows': rows,
        'limitations': [
            'Copied assistant replies inside user prompts can trigger false-positive markers.',
            'Marker overlaps are intentional; category percentages cannot be summed.',
            'Prompt block extraction is not a certified exact count of all user turns.',
            'The archive 43 live chat and duplicate/old export versions are excluded.',
            'A short continue message delegates autonomy; it is not approval of a topic.',
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive_dir', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = profile_directory(args.archive_dir)
    data = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data, encoding='utf-8')
    else:
        print(data, end='')


if __name__ == '__main__':
    main()
