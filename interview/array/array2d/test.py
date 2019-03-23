#!/bin/python3

import unittest2 as unittest

import hackerrank.utils.unit_test as hut
from submit import hourglassSum

class TestCase(unittest.TestCase):
    """
    Test hourglass sum solution.
    """
    def test_hourglass_sum(self):
        input_fns = hut.get_input_filenames()
        output_fns = hut.get_output_filenames()
        test_names = hut.get_test_names(input_fns, output_fns)
        for test_name in test_names:
            input_fn = hut.build_input_filename(test_name)
            output_fn = hut.build_output_filename(test_name)
            arr = hut.read_input(input_fn)
            res = hourglassSum(arr)
            expected = hut.read_output(output_fn)
            self.assertEqual(res, expected)
