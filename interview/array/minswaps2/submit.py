#!/bin/python3

import math
import os
import random
import re
import sys

class Array(object):
    """
    Class to keep track of 'state' of task (i.e. the array).
    """
    def __init__(self, arr):
        """
        Initialize unordered array. Sort array to get.

        Args:
            arr (list of int): Our array
        """
        self.arr = arr
        self.arr_ordered = sorted(arr)

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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimum_swaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
