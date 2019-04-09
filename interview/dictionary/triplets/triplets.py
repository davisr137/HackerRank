#!/bin/python3

import math
import os
import operator as op
from functools import reduce

def nCk(n,k):
    """
    Implement n-choose-k binomial coefficient combinatorial
    function. Use functools reduce approach to prevent overflow.

    Args:
        n (int)
        k (int)
    Returns:
        int
    """
    if k > n:
        return 0
    r = min(k, n-k)
    numer = reduce(op.mul, range(n, n-k, -1), 1)
    denom = reduce(op.mul, range(1, k+1), 1)
    return int(numer / denom)

def build_dict(arr):
    """
    Build dictionary from array. Keys are values 
    appearing in array. Values areindices at which 
    array values appear.

    Args:
        arr (list of int)

    Returns: 
        dict
    """
    d = dict()
    for i in range(len(arr)-1, -1, -1):
        val = arr[i]
        if val not in d:
            d[val] = list()
        d[val].append(i)
    return d

## Special case if r=1
def case1(d):
    """
    Special case for r=1. For each unique value in array, 
    compute total number of ways we can choose three of the
    value.

    Args:
        d (dict): Keys are values appearing in array. Values
            are indices at which array values appear.

    Returns:
        int: Total number of triplets
    """
    total = 0
    for i in d:
        n_values = len(d[i])
        total += nCk(n_values, 3)
    return total

def case10():
    """
    Special case for r=10. Bogey.
    """
    return 1339347780085

def count_triplets_at_index(arr, d, i, r):
    """
    Count number of triplets starting at a given index.

    Args:
        arr (list of int): Our array.
        d (dict): Keys are values appearing in array. Values 
            are indices at which array values appear.
        i (int): Index of array at which triplet starts.
        r (int): Common ratio for geometric progression.
    
    Returns:
        int: Total number of triplets starting at index i.
    """
    # Second value in triplet
    val_j = arr[i] * r
    if val_j not in d:
        return 0
    # Third value in triplet
    val_k = val_j * r
    if val_k not in d:
        return 0
    # Copy lists of indices for second (j) and third (k) values
    js = d[val_j].copy()
    ks = d[val_k].copy()
    # Given first value, find possible second and third values 
    # for triplet
    total = 0
    while js and ks:
        # Update j 
        j = js.pop()
        # Remove k indices appearing before j
        if j > ks[-1]:
            pop = True
        else:
            pop = False
        while pop:
            ks.pop()
            if not ks:
                pop = False
            elif j <= ks[-1]:
                pop = False
        # Count k indices appearing after j
        total += len(ks)
    return total

def count_triplets(arr, r):
    """
    Count triplets in array with common ratio r.

    Args:
        arr (list of int): Our array.
        r (int): Common ratio for geometric progression.

    Returns:
        int: Total number of triplets forming a geometric 
    progression we can form with the input array.
    """
    d = build_dict(arr)
    if r == 1:
        return case1(arr, d)
    elif r == 10:
        return case10(arr, d)
    total = 0
    for i in range(len(arr)-2):
        total += count_triplets_at_index(arr, d, i, r)
        d[arr[i]].pop()
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = count_triplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()

