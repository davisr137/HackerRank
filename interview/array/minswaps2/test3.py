#!/bin/python3

import unittest2 as unittest
import logging

import hackerrank.utils.unit_test as hut


def normalize_array(array, val):
    """
    Normalize array after a value is removed. For each element
    greater than 'val', subtract one from its value.

    Args: 
        array (list of int): Array post-removal of one element.
        val (int): Value removed from array.

    Returns:
        list of int: Normalized array of consecutive (not necessarily
            sorted) integers.
    """
    for i, _ in enumerate(array):
        if array[i] > val:
            array[i] -= 1
    return array


class Array(object):
    """
    Class to keep track of 'state' of task (i.e. the array).
    """
    def __init__(self, arr, arr_sorted=None):
        """
        Initialize unordered array. 

        Args:
            arr (list of int): Our array
            arr_sorted(list of int): Ordered version of array. If None,
                sort 'arr' to get ordered array.
        """
        if arr_sorted is None:
            arr_sorted = sorted(arr)
        removed = list()
        for i, val in enumerate(arr):
            if val == arr_sorted[i]:
                removed.append(val)
        if len(removed) > 0:
            removed = sorted(removed, reverse=True)
            for val in removed:
                arr.remove(val)
                arr_sorted.remove(val)
                arr = normalize_array(arr, val)
                arr_sorted = normalize_array(arr_sorted, val)
        self.arr = arr
        self.arr_sorted = arr_sorted

    def swap(self, i, j):
        """
        Swap elements i and j in array.

        Args:
            i (int): Index of first element to swap.
            j (int): Index of second element to swap.
        
        Returns:
            Array: Array with elements i and j swapped.
        """
        arr_swp = self.arr.copy()
        tmp = arr_swp[j]
        arr_swp[j] = arr_swp[i]
        arr_swp[i] = tmp
        return Array(arr_swp, arr_sorted=self.arr_sorted)


def increment_score(score, swp_idx):
    """
    Increment score by one. 

    Args:
        score (dict): Each key (int) represents an index
            in an array. Each value (int) repreents an increase 
            in sorted values from swapping.
        swp_idx (tuple)
    """
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
        if arr.arr[i] == i+1:
            score[i] = 2
        else:
            score[i] = 1
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
        i = max(score, key=score.get) 
        j = array.arr[i]-1
        array = array.swap(i, j)
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



