import unittest
from city_country_function import city_functions

class CitesTestCase(unittest.TestCase):
    """Проверяем функцию test_city_country"""

    def test_city_country(self):
        """Тестируем функцию на вывод"""

        formatted_city_country = city_functions('moscow', 'russia',
                                                '1_000_000')
        self.assertEqual(formatted_city_country,
                         'Moscow Russia - Population 1_000_000')

if __name__ == '__main__':
    unittest.main()