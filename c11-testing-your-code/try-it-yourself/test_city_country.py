import unittest

from city_country import get_city_and_country

class CityCountryTestCase(unittest.TestCase):

    def test_get_city_and_country(self):
        function_value = get_city_and_country('santiago', 'chile', 50)
        self.assertEqual(function_value, "Santiago, Chile - 5")


if __name__ == "__main__":
    unittest.main()