#!/bin/python3

import unittest2 as unittest
import os

def get_input_filenames():
    """
    Get all input filenames.

    Returns:
        list of str
    """
    return os.listdir('input/')

def get_output_filenames():
    """
    Get all output filenames.

    Returns:
        list of str
    """
    return os.listdir('output/')

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

def build_input_filename(test_name):
    """
    Build input filename. 
    Args:
        test_name (str): Name of test.
    Returns:
        str: Filename corresponding to test input.
    """
    return 'input/input%s.txt' % test_name

def build_output_filename(test_name):
    """
    Build output filename.
    Args:
        test_name (str): Name of test.
    Returns:
        str: Filename corresponding to test expected output.
    """
    return 'output/output%s.txt' % test_name

def read_input(filename):
    """
    Read input data (array-like).

    Args: 
        filename (str): Path to input file.

    Returns:
        list of list of int: Input data.
    """
    with open(filename, 'r') as f:
        arr = f.readlines()
    arr = [list(map(int, x.rstrip().split())) for x in arr]
    return arr

def read_output(filename):
    """
    Read output data (integer).

    Args:
        filename (str): Path to output file.

    Returns:
        int: Output data.
    """
    with open(filename, 'r') as f:
        out = int(f.readlines()[0])
    return out
