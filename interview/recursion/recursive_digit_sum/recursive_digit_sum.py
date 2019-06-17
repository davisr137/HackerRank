import math
import os
import random
import re
import sys

from typing import List

# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def intToList(n: int) -> List:
    """
    Convert integer to list of digits.
    """
    return [int(d) for d in str(n)]

def superDigit(n, k):
    """
    Given an integer x, find its super digit. If x has only 1 digit,
    then its super digit is x. Else, the super digit of x is equal to 
    the super digit of the sum of digits of x. The integer x is produced 
    by concatenating the string n k times.
    """
    N = sum(intToList(n)) * k
    L = intToList(N)
    return superDigitSearch(L)

def superDigitSearch(L: List[int]) -> int:
    """
    Recursively compute the super digit. 
    """
    if len(L) == 1:
        return L[0]
    else:
        N = sum(L)
        Ls = intToList(N)
        return superDigitSearch(Ls)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
