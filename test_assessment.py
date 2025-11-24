import unittest

from assessment import (
    cube_number, 
    check_even_or_odd, 
    combine_names, 
    get_last_item, 
    sum_all_numbers, 
    get_country_code
)

class TestBasics(unittest.TestCase):

    def test_cube_number(self):
        print("\nTesting Exponents...")
        self.assertEqual(cube_number(2), 8)
        self.assertEqual(cube_number(3), 27)

    def test_check_even_or_odd(self):
        print("Testing Modulo Logic...")
        self.assertEqual(check_even_or_odd(10), "Even")
        self.assertEqual(check_even_or_odd(7), "Odd")
        self.assertEqual(check_even_or_odd(0), "Even")

    def test_combine_names(self):
        print("Testing String Formatting...")
        self.assertEqual(combine_names("John", "Doe"), "Doe, John")
        self.assertEqual(combine_names("Alice", "Smith"), "Smith, Alice")

    def test_get_last_item(self):
        print("Testing List Indexing...")
        self.assertEqual(get_last_item([10, 20, 30]), 30)
        self.assertEqual(get_last_item(["A", "B"]), "B")

    def test_sum_all_numbers(self):
        print("Testing Loops/Sum...")
        self.assertEqual(sum_all_numbers([1, 1, 1]), 3)
        self.assertEqual(sum_all_numbers([10, 20]), 30)
        self.assertEqual(sum_all_numbers([]), 0)

    def test_get_country_code(self):
        print("Testing Dictionary Access...")
        data = {"ZA": "South Africa", "JP": "Japan", "BR": "Brazil"}
        self.assertEqual(get_country_code(data, "ZA"), "South Africa")
        self.assertEqual(get_country_code(data, "JP"), "Japan")

if __name__ == '__main__':
    # Failfast stops the tests at the first error so the student isn't overwhelmed
    unittest.main(failfast=True, verbosity=0)
