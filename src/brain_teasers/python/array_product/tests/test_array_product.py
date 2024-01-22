import unittest

from src.array_product import array_product


class TestArrayProduct(unittest.TestCase):
    def test_array_product(self):
        input_array = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        actual = array_product(input_array)
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        input_array = []
        expected = []
        actual = array_product(input_array)
        self.assertEqual(actual, expected)

    def test_array_with_one_element(self):
        input_array = [1]
        expected = [1]
        actual = array_product(input_array)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
