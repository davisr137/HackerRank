#!/bin/python3

import itertools
import os

import unittest2 as unittest
import pytest

def read_input(filename):
    """
    Read input file and parse into list of int.
    """
    with open(filename) as f:
        arr = f.readlines()
    arr = [list(map(int, x.rstrip().split())) for x in arr]
    return arr

def get_hourglass_sum(arr):
    """
    Find max hourglass sum in `arr`.

    Args:
        arr (list of list of int): Input array.

    Returns
        int: Maximum sum of hourglasses in `arr`.
    """
    glasses = list()
    # Iterate over rows 0-4
    for row in range(0, 4):
        # Iterate over columns 1-5
        for col in range(1,5):
            # Top, middle, bottom rows
            top = arr[row][col-1:col+2]
            mid = [arr[row+1][col]]
            bot = arr[row+2][col-1:col+2]
            # Represent hourglass as flattened list 
            glasses.append(list(itertools.chain.from_iterable([top, mid, bot])))
    sums = [sum(glass) for glass in glasses]
    return max(sums)

class TestCase(unittest.TestCase):
    """
    Shell class for unit test test case.
    """
    @staticmethod
    def get_input_filenames():
        """
        Get all input filenames.

        Returns:
            list of str
        """
        return os.listdir('input/')

    @staticmethod
    def get_output_filenames():
        """
        Get all output filenames.

        Returns: 
            list of str
        """
        return os.listdir('output/')

    @staticmethod
    def get_test_names(input_fn, output_fn):
        """
        Get all names of tests. Define a 'name' as the number given
        to the test (e.g. filenames 'input03.txt' and 'output03.txt'
        correspond to a test name '00.txt'). 

        Args:
            input_fn (list of str): Input filenames (e.g. ['input00.txt'])
            output_fn (list of str): Output filenames (e.g. ['output00.txt'])

        Returns:
            list of str: Names of common tests.
        """
        input_names = [fn.replace('.txt', '').replace('input','') for fn in input_fn]
        output_names = [fn.replace('.txt', '').replace('output','') for fn in output_fn]
        test_names = list((set(input_names) & set(output_names)))
        return test_names
   
    @staticmethod
    def build_input_filename(test_name):
        """
        Build input filename. 

        Args:
            test_name (str): Name of test.

        Returns:
            str: Filename corresponding to test input.
        """
        return 'input/input%s.txt' % test_name

    @staticmethod
    def build_output_filename(test_name):
        """
        Build output filename.

        Args:
            test_name (str): Name of test.

        Returns:
            str: Filename corresponding to test expected output.
        """
        return 'output/output%s.txt' % test_name

    @staticmethod
    def read_input(filename):

        with open(filename, 'r') as f:
            arr = f.readlines()
        arr = [list(map(int, x.rstrip().split())) for x in arr]
        return arr

    @staticmethod
    def read_output(filename):
        with open(filename, 'r') as f: 
            out = int(f.readlines()[0])
        return out

    def test_challenge(self):
        input_fns = TestCase.get_input_filenames()
        output_fns = TestCase.get_output_filenames()
        test_names = TestCase.get_test_names(input_fns, output_fns)
        for test_name in test_names:
            input_fn = TestCase.build_input_filename(test_name)
            output_fn = TestCase.build_output_filename(test_name)
            arr = TestCase.read_input(input_fn)
            res = get_hourglass_sum(arr)
            expected = TestCase.read_output(output_fn)
            self.assertEqual(res, expected)
