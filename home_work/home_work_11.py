"""HW_11"""

import unittest

def get_city_info(city, country, population=0):
    """Return formatted city name"""
    if population == 0:
        f_name = f"{city}, {country}"
    else:
        f_name = f"{city}, {country}, {population}"
    return f_name.title()

class NamesTestCase(unittest.TestCase):
    """Test for functions 'get_city_info'"""
    def test_city_counry(self):
        """Перевірка на найменування міст"""
        f_name = get_city_info('lviv', 'ukraine')
        self.assertEqual(f_name, 'Lviv, Ukraine')

    def test_city_counry_population(self):
        """Перевірка на найменування міст та к-сті населення"""
        f_name = get_city_info('lviv', 'ukraine', 455000)
        self.assertEqual(f_name, 'Lviv, Ukraine, 455000')

if __name__ == '__main__':
    unittest.main()
