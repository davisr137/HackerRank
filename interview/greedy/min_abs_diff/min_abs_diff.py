#!/bin/python3

import os

def minimum_absolute_difference(arr):
    """
    Compute the minimum absolute difference between any
    two elements of the array arr.

    Args:
        arr (list of int): Our array.

    Returns:
        int: Min absolute difference.
    """
    arr = sorted(arr)
    diff = [abs(arr[i] - arr[i-1]) for i in range(1, len(arr))]
    return min(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimum_absolute_difference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

