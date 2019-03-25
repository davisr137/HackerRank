#!/bin/python3

import unittest2 as unittest
import logging

import hackerrank.utils.unit_test as hut


class Array(object):
    """
    Class to keep track of 'state' of task (i.e. the array).
    """
    def __init__(self, arr, arr_ordered=None):
        """
        Initialize unordered array. Sort array to get.

        Args:
            arr (list of int): Our array
            arr_ordered(list of int): Ordered version of array. If None,
                sort 'arr' to get ordered array.
        """
        if arr_ordered is None:
            arr_ordered = sorted(arr)
        for i, val in enumerate(arr):
            if val == arr_ordered[i]:
                arr.remove(val)
                arr_ordered.remove(val)
        self.arr = arr
        self.arr_ordered = arr_ordered

    def swap(self, i, j):
        """
        Swap elements i and j in array.

        Args:
            i (int): Index of first element to swap.
            j (int): Index of second element to swap.
        """
        arr_swp = self.arr.copy()
        tmp = arr_swp[j]
        arr_swp[j] = arr_swp[i]
        arr_swp[i] = tmp
        return Array(arr_swp, arr_ordered=self.arr_ordered)

def increment_score(score, swp_idx):
    if swp_idx not in score:
        score[swp_idx] = 0
    score[swp_idx] += 1
    return score


def generate_possible_swaps(arr):
    """
    Generate possible swaps for array.

    Args:
        arr (Array): Our array.
    """
    l = len(arr.arr)
    score = dict()
    for i in range(0, l):
        for j in range(i+1, l):
            swp_idx = tuple([i, j])
            if arr.arr[i] == arr.arr_ordered[j]:
                score = increment_score(score, swp_idx)
            if arr.arr[j] == arr.arr_ordered[i]:
                score = increment_score(score, swp_idx)
    return score


def minimum_swaps(arr):
    """
    Get minimum number of swaps to sort array 'arr' in ascending
    order.

    Args:
        arr (list of int): Array to sort.

    Returns:
        int: Minimum number of swaps to sort.
    """
    array = Array(arr)
    swaps = 0
    while len(array.arr) > 1:
        score = generate_possible_swaps(array)
        move = max(score, key=score.get) 
        array = array.swap(move[0], move[1])
        swaps += 1
    return swaps


def read_input(filename):
    """
    Read input from file.

    Args: 
        filename (str): Path to file.

    Returns:
        list of int: Array to sort.
    """
    with open(filename, 'r') as f:
        n = f.readline()
        arr = f.readline()
    arr = [int(x) for x in arr.rstrip().split()]
    return arr


class TestCase(unittest.TestCase):
    """
    Test minimum swaps solution.
    """
    def test_min_swaps(self):
        """
        Read input files, compute solution, compare against 
        expected output.
        """
        input_fns = hut.get_input_filenames()
        output_fns = hut.get_output_filenames()
        test_names = hut.get_test_names(input_fns, output_fns)
        for test_name in test_names:
            input_fn = hut.build_input_filename(test_name)
            output_fn = hut.build_output_filename(test_name)
            arr = read_input(input_fn)
            res = minimum_swaps(arr)
            expected = hut.read_output(output_fn)
            self.assertEqual(res, expected)



