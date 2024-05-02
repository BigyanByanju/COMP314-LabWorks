import unittest
from insertion_sort import insertion_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        print("Testing insertion sort with UnitTest")
        input_data = [3, 1, 2, 8, 5, 4]
        sorted_data = insertion_sort(input_data)
        expected_data = [1, 2, 3, 4, 5, 8]
        self.assertEqual(sorted_data, expected_data)


if __name__ == "__main__":
    unittest.main()
