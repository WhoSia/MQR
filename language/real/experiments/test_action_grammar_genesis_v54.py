"""MQR chat42 independent negative controls for action grammar generation."""
import unittest
from itertools import product
from action_grammar_genesis_v54 import ActionLanguage, NamedAction, GeneratorTrial

OBS=("dark","dark","bright","bright")
FLIP=NamedAction("internal_flip",(1,0,3,2))
BRIDGE=NamedAction("cross_swap",(0,2,1,3))
INVISIBLE=NamedAction("within_group_swap",(1,0,2,3))
LAB=ActionLanguage(OBS,(FLIP,))

class ActionGenesisTests(unittest.TestCase):
    def test_old_partition_and_closure(self):
        self.assertEqual(LAB.equivalence_classes(),((0,1),(2,3)))
        self.assertEqual(len(LAB.closure_with_words()),2)

    def test_new_executable_action_produces_new_discrimination(self):
        r=GeneratorTrial(LAB,BRIDGE,True).analyze()
        self.assertTrue(r["novel"])
        self.assertTrue(r["strict_refinement"])
        self.assertEqual(r["new_blocks"],((0,),(1,),(2,),(3,)))
        self.assertIn("cross_swap",r["witness"]["word"])

    def test_novel_action_can_be_observationally_uninformative(self):
        r=GeneratorTrial(LAB,INVISIBLE,True).analyze()
        self.assertTrue(r["novel"])
        self.assertFalse(r["strict_refinement"])
        self.assertEqual(r["new_blocks"],LAB.equivalence_classes())

    def test_renamed_old_action_is_not_new_capability(self):
        r=GeneratorTrial(LAB,NamedAction("alias",FLIP.mapping),True).analyze()
        self.assertFalse(r["novel"])
        self.assertFalse(r["strict_refinement"])

    def test_lack_of_physical_certification_blocks_new_claim(self):
        r=GeneratorTrial(LAB,BRIDGE,False).analyze()
        self.assertFalse(r["certified"])
        self.assertFalse(r["strict_refinement"])
        self.assertIsNone(r["witness"])

    def test_constant_sensor_cannot_discriminate_under_any_one_new_action(self):
        base=ActionLanguage(("x",)*4)
        for g in product(range(4),repeat=4):
            self.assertFalse(GeneratorTrial(base,NamedAction("g",g),True)
                             .analyze()["strict_refinement"])

    def test_exhaustive_four_to_four_maps_preserve_refinement_monotonicity(self):
        old=LAB.equivalence_classes()
        for g in product(range(4),repeat=4):
            r=GeneratorTrial(LAB,NamedAction("g",g),True).analyze()
            self.assertTrue(all(
                any(set(new_block) <= set(old_block) for old_block in old)
                for new_block in r["new_blocks"]))

    def test_invalid_action_and_duplicate_name_rejected(self):
        with self.assertRaises(ValueError):
            GeneratorTrial(LAB,NamedAction("bad",(0,1)),True).analyze()
        with self.assertRaises(ValueError):
            GeneratorTrial(LAB,NamedAction("internal_flip",(0,1,2,3)),True).analyze()

    def test_noninvertible_action_valid(self):
        r=GeneratorTrial(ActionLanguage(OBS),NamedAction("erase",(0,0,0,2)),True).analyze()
        self.assertTrue(r["novel"])
        self.assertEqual(r["new_blocks"],((0,1),(2,),(3,)))

    def test_distinguish_analyst_ground_truth_from_agent_knowledge(self):
        # Model assumes shared state indexes supplied by its analyst.
        self.assertEqual(len(LAB.observation),4)
        self.assertNotIn("physical_certificate",GeneratorTrial(LAB,BRIDGE,True).analyze())

if __name__=="__main__":
    unittest.main()
