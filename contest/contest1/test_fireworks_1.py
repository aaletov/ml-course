import unittest
from .fireworks_1 import *

class TestSortPreservingIndex(unittest.TestCase):
    def test_one(self):
        arr = [1]
        preserve_idx = 0
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, arr)
        self.assertEqual(new_idx, preserve_idx)

    def test_two_first(self):
        arr = [2, 1]
        preserve_idx = 0
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, list(sorted(arr)))
        self.assertEqual(sorted_arr[new_idx], arr[preserve_idx])

    def test_two_second(self):
        arr = [2, 1]
        preserve_idx = 1
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, list(sorted(arr)))
        self.assertEqual(sorted_arr[new_idx], arr[preserve_idx])

    def test_long_first(self):
        arr = [4, 3, 1, 2]
        preserve_idx = 0
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, list(sorted(arr)))
        self.assertEqual(sorted_arr[new_idx], arr[preserve_idx])

    def test_long_last(self):
        arr = [4, 3, 1, 2]
        preserve_idx = 3
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, list(sorted(arr)))
        self.assertEqual(sorted_arr[new_idx], arr[preserve_idx])

    def test_long_mid(self):
        arr = [4, 3, 1, 2]
        preserve_idx = 1
        sorted_arr, new_idx = sort_preserving_index(arr, preserve_idx)
        self.assertEqual(sorted_arr, list(sorted(arr)))
        self.assertEqual(sorted_arr[new_idx], arr[preserve_idx])


class TestCalculateWindowBounds(unittest.TestCase):
    def test_equal(self):
        arr_size = 4
        window_size = 4
        pivot = 1
        l_idx, r_idx = calculate_window_bounds(pivot, window_size, arr_size)
        self.assertEqual(l_idx, 0)
        self.assertEqual(r_idx, 3)

    def test_left_fixed(self):
        arr_size = 6
        window_size = 3
        pivot = 0
        l_idx, r_idx = calculate_window_bounds(pivot, window_size, arr_size)
        self.assertEqual(l_idx, 0)
        self.assertEqual(r_idx, 2)

    def test_right_fixed(self):
        arr_size = 6
        window_size = 3
        pivot = 5
        l_idx, r_idx = calculate_window_bounds(pivot, window_size, arr_size)
        self.assertEqual(r_idx, pivot)
        self.assertEqual(l_idx, pivot - window_size + 1)

class TestCalculateMinWindowDelta(unittest.TestCase):
    def test_equal(self):
        arr = [1, 2, 6]
        l_idx = 0
        r_idx = 2
        pivot_idx = 2
        delta = calculate_min_window_delta(arr, l_idx, r_idx, pivot_idx)
        self.assertEqual(delta, 5)

    def test_plain(self):
        arr = [1, 2, 6, 7, 8]
        l_idx = 0
        r_idx = 2
        pivot_idx = 2
        delta = calculate_min_window_delta(arr, l_idx, r_idx, pivot_idx)
        self.assertEqual(delta, 2)

class TestMinimalHeightDelta(unittest.TestCase):
    def test1(self):
        N, K, t = 6, 4, 2
        heights = [
            1,
            2,
            1,
            2,
            2,
            2,
        ]
        min_height_delta = calculate_minimal_height_delta(heights, K, t)
        self.assertEqual(min_height_delta, 0)

    def test2(self):
        N, K, t = 5, 3, 1
        heights = [
            4,
            1,
            5,
            6,
            2,
        ]
        min_height_delta = calculate_minimal_height_delta(heights, K, t)
        self.assertEqual(min_height_delta, 2)

    def test_unary_window(self):
        N, K, t = 5, 1, 1
        heights = [
            4,
            1,
            5,
            6,
            2,
        ]
        min_height_delta = calculate_minimal_height_delta(heights, K, t)
        self.assertEqual(min_height_delta, 0)

if __name__ == '__main__':
    unittest.main()