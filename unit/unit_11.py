"""Тестування коду"""

import unittest

# NOTE: Тестування функції
def get_format_name(first_name, last_name, middle_name=''):
    """Генерація відформатованого імені"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# full_name = get_format_name('ihor', 'sereda')
# print(full_name)

print("Enter 'q' foe exit")

# while True:
#     """Test func"""
#     first = input('\nPlease enter a first name: ')
#     if first == 'q':
#         break
#     last = input('\nPlease enter a last name: ')
#     if last == 'q':
#         break
#
#     f_name = get_format_name(first, last)
#     print(f"Format name: {f_name}")

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_format_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_format_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
