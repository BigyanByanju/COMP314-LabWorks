import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        input_data = [3, 1, 2, 8, 5, 4]
        sorted_data = selection_sort(input_data)
        expected_data = [1, 2, 3, 4, 5, 8]
        self.assertEqual(sorted_data, expected_data)


if __name__ == "__main__":
    unittest.main()
