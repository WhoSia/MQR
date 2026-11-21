import tempfile
import unittest
from pathlib import Path
from mqr_archive_prompt_profile_v54 import profile_directory, profile_text


class CorpusProfilerTests(unittest.TestCase):
    def test_quoted_continuation_is_marker_not_author_intent(self):
        text = '# MQR 1\n## Prompt:\n2026. 8. 26. 오후 2:35\n왜 물리학의 구조? ㄱㄱ\n## Response:\nGreat\n'
        result = profile_text(text, 1)
        self.assertEqual(result['prompt_blocks'], 1)
        self.assertEqual(result['continuation_marker'], 1)
        self.assertEqual(result['grand_concept_marker'], 1)

    def test_crlf_multiprompt_and_overlap(self):
        text = '## Prompt:\r\n2026. 8. 26. 오후 2:35\r\n미보유 문헌 복습 ㄱㄱ\r\n## Response:\r\nOK\r\n## Prompt:\r\n계속 연구\r\n## Response:\r\nOK\r\n'
        r = profile_text(text, 42)
        self.assertEqual(r['prompt_blocks'], 2)
        self.assertEqual(r['literature_intake_marker'], 1)
        self.assertEqual(r['archive_review_marker'], 1)
        self.assertEqual(r['continuation_marker'], 2)

    def test_unrecognized_export_fails_closed(self):
        with self.assertRaisesRegex(ValueError, 'No recognizable'):
            profile_text('missing user prompts', 3)

    def test_wrong_index_fails(self):
        with self.assertRaises(ValueError):
            profile_text('## Prompt:\nfoo\n## Response:\nbar', 43)

    def test_full_directory_requires_all_42_not_partial(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'MQR 1.md'
            p.write_text('## Prompt:\nfoo\n## Response:\nbar', encoding='utf-8')
            with self.assertRaises(FileNotFoundError):
                profile_directory(Path(d))

    def test_complete_directory_aggregates_and_excludes_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for n in range(1, 43):
                (root / f'MQR {n}.md').write_text('## Prompt:\n계속 ㄱㄱ\n## Response:\nok\n', encoding='utf-8')
            (root / 'MQR 6.pre-audit.md').write_text('## Prompt:\nextra\n## Response:\nok\n')
            result = profile_directory(root)
            self.assertEqual(result['total']['prompt_blocks'], 42)
            self.assertEqual(result['total']['continuation_marker'], 42)
            self.assertEqual(len(result['rows']), 42)
            self.assertEqual(result['three_epoch_totals'][0]['prompt_blocks'], 14)


if __name__ == '__main__':
    unittest.main()
