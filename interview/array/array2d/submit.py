#!/bin/python3

import os
import itertools

def hourglassSum(arr):
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
    return(max(sums))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
