#!/bin/python3

import math
import os
import random
import re
import sys

def build_dict(arr):
    """
    Build dictionary from array.
    """
    d = dict()
    for i, val in enumerate(arr):
        if val not in d:
            d[val] = list()
        d[val].append(i)
    return d

# Use memoization to store "couples" in dict
# e.g. for array 1 1 1 1 5 25 25
# store (4, 1) = 2 to represent index 4 and n=1, two "couples" 
# same couple used for four different triplets

def find_triplets(arr, d, i, r, n):

    val = arr[i] * r
    if val not in d:
        return 0

    js = d[val]
    js = [j for j in js if j > i]
    
    if n == 1:
        return len(js)
    elif n == 0:
        total = 0
        for j in js:
            total += find_triplets(arr, d, j, r, 1)
        return total

def count_triplets(arr, r):
    """
    Count triplets in array with common ratio r.

    Args:
        arr (list of int):
        r (int): common ratio
    """
    # Only keep multiples of common ratio
    d = build_dict(arr)
    total = 0
    for i in range(len(arr)-2):
        total += find_triplets(arr, d, i, r, 0)
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

