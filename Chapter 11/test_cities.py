import unittest
from city_functions import combine


class CityTestCase(unittest.TestCase):


    def test_city_country(self):
        self.assertEqual("Santiago, Chile", combine("santiago", "chile"))

    def test_weird_case(self):
        self.assertEqual("London, England", combine("LOndoN", "engLAND"))

    def test_population(self):
        self.assertEqual("Santiago, Chile - population 50000000", combine("santiago", "chile", 50000000))
