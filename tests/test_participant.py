import unittest
from participant import participant


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.person = participant.Participant(
            pa_name="Foo Bar",
            pa_has_somebody_to_gift=False
        )

    def test_doesnt_have_any_name(self):
        self.person.name = None
        self.assertIsNone(self.person.name)

    def test_has_a_name(self):
        self.assertIsNotNone(self.person.name)

    def test_doesnt_have_any_partner(self):
        self.assertFalse(self.person.has_somebody_to_gift)

    def test_has_a_partner(self):
        self.person.has_somebody_to_gift = True
        self.assertTrue(self.person.has_somebody_to_gift)
