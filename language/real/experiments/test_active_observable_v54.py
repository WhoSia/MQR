"""Bounded exact regression tests for finite observation-class refinement."""

from itertools import product, combinations
import unittest

from active_observable_v54 import (
    Experiment,
    ObservationTable,
    pairs_separated_by_new_observable,
)


class ActiveObservableTests(unittest.TestCase):
    def test_quantized_adc_can_hide_two_states(self):
        initial = ObservationTable(
            ("red_solution", "blue_solution", "blank"),
            (Experiment("adc_bin", ("7", "7", "0")),),
        )
        self.assertEqual(initial.partition(), (("red_solution", "blue_solution"), ("blank",)))
        self.assertEqual(initial.unresolved_pairs(), (("red_solution", "blue_solution"),))
        extra = Experiment("filter_response", ("R", "B", "B"))
        self.assertEqual(pairs_separated_by_new_observable(initial, extra),
                         (("red_solution", "blue_solution"),))
        enriched = initial.add(extra)
        self.assertEqual(enriched.partition(), (("red_solution",), ("blue_solution",), ("blank",)))
        self.assertEqual(enriched.smallest_sufficient_set(), ("adc_bin", "filter_response"))

    def test_redundant_observable_does_not_create_new_distinctions(self):
        initial = ObservationTable(("a", "b", "c"), (Experiment("count", ("1", "1", "0")),))
        extra = Experiment("rescaled_count", ("10", "10", "0"))
        self.assertEqual(pairs_separated_by_new_observable(initial, extra), ())
        self.assertEqual(initial.add(extra).smallest_sufficient_set(), ("count",))

    def test_available_experiments_may_never_separate_worlds(self):
        table = ObservationTable(("hidden_a", "hidden_b"), (Experiment("readout", ("same", "same")),))
        self.assertEqual(table.smallest_sufficient_set(), ())
        self.assertEqual(table.unresolved_pairs(), (("hidden_a", "hidden_b"),))
        self.assertEqual(table.add(Experiment("repeat", ("same", "same"))).unresolved_pairs(),
                         (("hidden_a", "hidden_b"),))

    def test_consistent_outcome_renaming_preserves_partitions(self):
        base = ObservationTable(("a", "b", "c"),
                                (Experiment("one", ("0", "0", "1")),
                                 Experiment("two", ("left", "right", "right"))))
        renamed = ObservationTable(base.worlds,
                                   (Experiment("one", ("U", "U", "V")),
                                    Experiment("two", ("2", "5", "5"))))
        for subset in ((), ("one",), ("two",), ("one", "two")):
            self.assertEqual(base.partition(subset), renamed.partition(subset))
        self.assertEqual(base.smallest_sufficient_set(), renamed.smallest_sufficient_set())

    def test_empty_observation_family_and_single_world(self):
        table = ObservationTable(("a", "b"), ())
        self.assertEqual(table.partition(), (("a", "b"),))
        self.assertEqual(table.smallest_sufficient_set(), ())
        self.assertEqual(ObservationTable(("a",), ()).unresolved_pairs(), ())

    def test_invalid_experiment_names_worlds_and_lengths(self):
        for worlds, experiments in (
            ((), ()), (("a", "a"), ()),
            (("a",), (Experiment("x", ()),)),
            (("a",), (Experiment("x", ("0",)), Experiment("x", ("1",)))),
            (("a",), (Experiment("", ("0",)),)),
        ):
            with self.subTest(worlds=worlds, experiments=experiments):
                with self.assertRaises(ValueError):
                    ObservationTable(worlds, experiments)
        table = ObservationTable(("a",), (Experiment("x", ("0",)),))
        for selected in (("no",), ("x", "x")):
            with self.subTest(selected=selected), self.assertRaises(ValueError):
                table.partition(selected)
        with self.assertRaises(ValueError):
            table.add(Experiment("x", ("0",)))

    def test_exhaustive_three_world_three_experiment_binary_oracle(self):
        worlds = ("a", "b", "c")
        all_columns = tuple(product(("0", "1"), repeat=3))
        names = ("e0", "e1", "e2")
        for values in product(all_columns, repeat=3):
            table = ObservationTable(worlds,
                                     tuple(Experiment(name, col) for name, col in zip(names, values)))
            minimum = table.smallest_sufficient_set()
            full_pairs = set(table.unresolved_pairs())
            self.assertEqual(set(table.unresolved_pairs(minimum)), full_pairs)
            for smaller in range(len(minimum)):
                for selection in combinations(names, smaller):
                    self.assertNotEqual(set(table.unresolved_pairs(selection)), full_pairs)


if __name__ == "__main__":
    unittest.main()
