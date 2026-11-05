"""MQR R46-G regression tests for historical-source transmission."""
import unittest
from mqr53_r46_g_source_provenance import (
    WEYL_1921_VIA_1998, BROUWER_ESTATE_VIA_1998,
    FRAENKEL_1923_VIA_KISH_2022,
    Evidence, Origin, Transmission, is_actor_position,
    original_wording_verified, available_at, can_attest_direct_original_letter,
)


class ProvenanceTests(unittest.TestCase):
    def test_translation_is_actor_origin(self):
        self.assertTrue(is_actor_position(WEYL_1921_VIA_1998))

    def test_translation_not_independent_original_wording(self):
        self.assertFalse(original_wording_verified(WEYL_1921_VIA_1998))

    def test_estate_is_actor_origin_but_not_public_original(self):
        self.assertTrue(is_actor_position(BROUWER_ESTATE_VIA_1998))
        self.assertFalse(can_attest_direct_original_letter(BROUWER_ESTATE_VIA_1998))

    def test_secondary_quote_not_direct_letter(self):
        self.assertFalse(is_actor_position(FRAENKEL_1923_VIA_KISH_2022))
        self.assertFalse(can_attest_direct_original_letter(FRAENKEL_1923_VIA_KISH_2022))

    def test_time_cutoff_does_not_use_edition_year(self):
        self.assertTrue(available_at(WEYL_1921_VIA_1998, 1921))
        self.assertFalse(available_at(WEYL_1921_VIA_1998, 1920))

    def test_actual_actor_access_not_inferred(self):
        # The positive value is only chronological eligibility.
        self.assertTrue(available_at(FRAENKEL_1923_VIA_KISH_2022, 1923))

    def test_unknown_authorship_date(self):
        e = Evidence('unknown', None, 2000, Origin.HISTORIAN,
                     Transmission.SECONDARY_QUOTATION)
        self.assertFalse(available_at(e, 1995))

    def test_collated_original_is_distinguishable(self):
        e = Evidence('verified original', 1921, 1921, Origin.ACTOR,
                     Transmission.ORIGINAL_EDITION, True)
        self.assertTrue(original_wording_verified(e))
        self.assertTrue(can_attest_direct_original_letter(e))


if __name__ == '__main__':
    unittest.main()
