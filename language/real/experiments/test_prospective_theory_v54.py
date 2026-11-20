from itertools import product, combinations
import unittest
from prospective_theory_v54 import Theory, TheoryFamily


class ProspectiveTests(unittest.TestCase):
    def setUp(self):
        self.family = TheoryFamily((
            Theory("inherit", (("adc", "7"), ("filter", "R"), ("temperature", "A"))),
            Theory("invented", (("adc", "7"), ("filter", "B"), ("temperature", "A"))),
            Theory("third", (("adc", "7"), ("filter", "B"), ("temperature", "C"))),
        ))

    def test_new_theory_can_fit_past_data_yet_predict_different_future_result(self):
        observed = (("adc", "7"),)
        self.assertEqual(len(self.family.viable(observed)), 3)
        self.assertEqual(self.family.discrimination_scores(observed), (("filter", 2), ("temperature", 2)))
        self.assertEqual(self.family.next_probe(observed), "filter")

    def test_new_measurement_refutes_some_but_not_all_models(self):
        new_obs, viable = self.family.revise((("adc", "7"),), "filter", "R")
        self.assertEqual(new_obs, (("adc", "7"), ("filter", "R")))
        self.assertEqual(viable, ("inherit",))

    def test_unexpected_outcome_refutes_whole_declared_family(self):
        _, viable = self.family.revise((("adc", "7"),), "filter", "unknown")
        self.assertEqual(viable, ())
        self.assertIsNone(self.family.next_probe((("adc", "unknown"),)))

    def test_zero_discrimination_abstains(self):
        family = TheoryFamily((Theory("a", (("x", "1"), ("y", "2"))),
                               Theory("b", (("x", "1"), ("y", "2")))))
        self.assertIsNone(family.next_probe((("x", "1"),)))
        self.assertEqual(family.discrimination_scores((("x", "1"),)), (("y", 0),))

    def test_nonsurjective_symbol_renaming_can_destroy_test_information(self):
        family = TheoryFamily((Theory("a", (("p", "red"),)),
                               Theory("b", (("p", "blue"),))))
        self.assertEqual(family.next_probe(()), "p")
        collapsed = TheoryFamily((Theory("a", (("p", "same"),)),
                                  Theory("b", (("p", "same"),))))
        self.assertIsNone(collapsed.next_probe(()))

    def test_invalid_inputs_and_domains_are_rejected(self):
        for theories in ((), (Theory("same", (("x", "0"),)), Theory("same", (("x", "1"),))),
                         (Theory("a", (("x", "0"),)), Theory("b", (("y", "0"),)))):
            with self.subTest(theories=theories), self.assertRaises(ValueError):
                TheoryFamily(theories)
        for pred in ((), (("x", "0"), ("x", "1")), (("", "0"),)):
            with self.subTest(pred=pred), self.assertRaises(ValueError):
                Theory("test", pred)
        with self.assertRaises(ValueError):
            self.family.viable((("missing", "1"),))
        with self.assertRaises(ValueError):
            self.family.viable((("adc", "7"), ("adc", "7")))
        with self.assertRaises(ValueError):
            self.family.revise((("adc", "7"),), "adc", "7")
        with self.assertRaises(ValueError):
            self.family.revise((), "missing", "1")

    def test_all_binary_three_theory_two_probe_tables_against_brute_pair_count(self):
        for bits in product("01", repeat=6):
            rows = [bits[0:2], bits[2:4], bits[4:6]]
            family = TheoryFamily(tuple(Theory(f"t{i}", (("p",row[0]), ("q",row[1])))
                                        for i,row in enumerate(rows)))
            scores = dict(family.discrimination_scores(()))
            for j,name in enumerate(("p", "q")):
                self.assertEqual(scores[name], sum(a[j] != b[j] for a,b in combinations(rows, 2)))
            expected = next((name for name in ("p", "q") if scores[name] == max(scores.values()) and scores[name] > 0),None)
            self.assertEqual(family.next_probe(()), expected)


if __name__ == '__main__':
    unittest.main()
