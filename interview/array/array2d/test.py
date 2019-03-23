#!/bin/python3

import hackerrank.utils.unit_test as hut
from submit import hourglassSum

class TestHourglassSum(hut.TestCase):
    """
    Test hourglass sum solution.
    """
    def test_hourglass_sum(self):
        input_fns = TestHourglassSum.get_input_filenames()
        output_fns = TestHourglassSum.get_output_filenames()
        test_names = TestHourglassSum.get_test_names(input_fns, output_fns)
        for test_name in test_names:
            input_fn = TestHourglassSum.build_input_filename(test_name)
            output_fn = TestHourglassSum.build_output_filename(test_name)
            arr = TestHourglassSum.read_input(input_fn)
            res = hourglassSum(arr)
            expected = TestHourglassSum.read_output(output_fn)
            self.assertEqual(res, expected)
