import unittest
from .tips_2 import *

class TestSortPreservingIndex(unittest.TestCase):
    def test_1(self):
        n, q = 2, 1
        dinner_times = [2, 4]
        travel_times = [1, 2]
        changes = [[1, 3, 4]]
        calc = TipCalculator(dinner_times, travel_times)
        self.assertEqual(calc.get_tips(), 2)
        ch_idx, ch_dinner_time, ch_travel_time = changes[0]
        ch_idx -= 1
        calc.change(ch_idx, ch_dinner_time, ch_travel_time)
        self.assertEqual(calc.get_tips(), -1)
