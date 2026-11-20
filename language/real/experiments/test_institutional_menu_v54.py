from itertools import combinations, product
import unittest
from active_observable_v54 import Experiment, ObservationTable
from institutional_menu_v54 import InstitutionalMenu


class MenuTests(unittest.TestCase):
    def setUp(self):
        self.table = ObservationTable(("A","B","C"),(
            Experiment("routine",("0","0","1")),
            Experiment("unusual",("red","blue","blue"))))

    def test_restricted_questions_hide_real_finite_discrimination(self):
        menu = InstitutionalMenu(self.table,("routine",))
        self.assertEqual(menu.hidden_distinctions(),(("A","B"),))
        self.assertEqual(menu.smallest_readmission(),("unusual",))

    def test_full_menu_keeps_no_avoidable_ignorance(self):
        m=InstitutionalMenu(self.table,("routine","unusual"))
        self.assertEqual(m.hidden_distinctions(),())
        self.assertEqual(m.smallest_readmission(),())

    def test_readmission_does_not_need_redundant_experiment(self):
        t=self.table.add(Experiment("copy",("0","0","1")))
        m=InstitutionalMenu(t,("routine",))
        self.assertEqual(m.smallest_readmission(),("unusual",))

    def test_two_missing_axes_require_both(self):
        t=ObservationTable(("00","01","10","11"),(
            Experiment("x",("0","0","1","1")),
            Experiment("y",("0","1","0","1"))))
        m=InstitutionalMenu(t,())
        self.assertEqual(m.smallest_readmission(),("x","y"))
        self.assertEqual(len(m.hidden_distinctions()),6)

    def test_sanctioned_must_be_subset_without_duplicates(self):
        for names in (("none",),("routine","routine")):
            with self.subTest(names=names),self.assertRaises(ValueError):
                InstitutionalMenu(self.table,names)

    def test_exhaustive_binary_three_world_two_test_oracle(self):
        outcomes=tuple(product("01",repeat=3))
        for a,b in product(outcomes,repeat=2):
            t=ObservationTable(("A","B","C"),(
                Experiment("routine",a),Experiment("unusual",b)))
            for sanctioned in ((),("routine",),("unusual",),("routine","unusual")):
                m=InstitutionalMenu(t,sanctioned)
                recovered=m.smallest_readmission()
                self.assertEqual(t.partition(sanctioned+recovered),t.partition())
                excluded=tuple(e.name for e in t.experiments if e.name not in sanctioned)
                for k in range(len(recovered)):
                    for subset in combinations(excluded,k):
                        self.assertNotEqual(t.partition(sanctioned+subset),t.partition())


if __name__ == '__main__':
    unittest.main()
