# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:02:40 2022

Testing pi estimation using monte carlo simulation code snippet
"""
import pi_monte_carlo_edits as pi_mc
import unittest
import numpy as np


class test_pi_estimate(unittest.TestCase):
    def test_pi_estimate(self):
        # check for count input the return is a tuple
        self.assertIsInstance(pi_mc.pi_estimate(100), tuple)
        # check if a type error raised for erroneous count variable type
        self.assertRaises(TypeError, pi_mc.pi_estimate(10), None)

    def test_random_number(self):
        a = pi_mc.generate_random_number(-1, -1)
        self.assertGreaterEqual(a, -1)
        self.assertLessEqual(a, 1)

    def test_varying_counts(self):
        count_array = [5, 10, 15]
        self.assertIsInstance(pi_mc.pi_varying_counts(count_array), np.ndarray)

    def test_radius(self):
        self.assertEqual(pi_mc.find_radius(3, 4), 5)
        self.assertIsInstance(pi_mc.find_radius(1, 1), float)


if __name__ == "__main__":
    unittest.main()
