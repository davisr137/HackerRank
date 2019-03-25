#!/bin/python3

import unittest2 as unittest

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
        self.arr = arr
        if arr_ordered is None:
            self.arr_ordered = sorted(arr)
        else:
            self.arr_ordered = arr_ordered

    @property
    def unordered_elements_index(self):
        """
        Get indices of unordered elements in array.
        
        Returns:
            list of int: Indices of unordered elements.
        """
        index_unordered = list()
        for i, val in enumerate(self.arr):
            if val != self.arr_ordered[i]:
                index_unordered.append(i)
        return index_unordered

    @property
    def unordered_elements_num(self):
        """
        Get number of unordered elements in array.

        Returns:
            int: Number of unordered elements.
        """
        return len(self.unordered_elements_index)

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
        return Array(arr_swp)


class Array2(object):
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
        print(len(arr))
        if arr_ordered is None:
            arr_ordered = sorted(arr)
        print(len(arr_ordered))
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
        return Array2(arr_swp, arr_ordered=self.arr_ordered)

def generate_possible_swaps(arr):
    """
    Generate possible swaps for array.

    Args:
        arr (Array): Our array.
    """
    l = len(arr.arr)
    moves = dict()
    score = dict()
    for i in range(0, l):
        for j in range(i, l):
            swp_idx = tuple([i, j])
            moves[swp_idx] = arr.swap(i, j)            
            score[swp_idx] = moves[swp_idx].unordered_elements_num
    return score


def generate_possible_swaps2(arr):
    """
    Generate possible swaps for array.

    Args:
        arr (Array): Our array.
    """
    l = len(arr.arr)
    moves = dict()
    score = dict()
    for i in range(0, l):
        for j in range(i, l):
            print(i)
            print(j)
            swp_idx = tuple([i, j])
            moves[swp_idx] = arr.swap(i, j)
            score[swp_idx] = len(moves[swp_idx].arr)
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
    arr = Array(arr)
    swaps = 0
    while arr.unordered_elements_num > 0:
        score = generate_possible_swaps(arr)
        move = min(score, key=score.get)
        arr = arr.swap(move[0], move[1])
        swaps += 1
    return swaps


def minimum_swaps2(arr):
    """
    Get minimum number of swaps to sort array 'arr' in ascending
    order.

    Args:
        arr (list of int): Array to sort.

    Returns:
        int: Minimum number of swaps to sort.
    """
    arr = Array2(arr)
    swaps = 0
    while len(arr.arr) > 0:
        score = generate_possible_swaps2(arr)
        move = min(score, key=score.get)
        arr = arr.swap(move[0], move[1])
        print(arr.arr)
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
    def test_hourglass_sum(self):
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
            res = minimum_swaps2(arr)
            expected = hut.read_output(output_fn)
            self.assertEqual(res, expected)



