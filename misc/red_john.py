#!/bin/python3

import sys
import os 
from math import factorial, floor, sqrt

# https://www.hackerrank.com/challenges/red-john-is-back

# sieve to find primes less than M
def sieve(M):
    a = range(2,M+1)
    b = set(a)
    n = 2
    primes = set()
    m = min(b)
    while m <= floor(sqrt(M)):
        m = min(b)
        primes.add(m)
        cross_out = range(m,M+1,m)
        for elt in cross_out:
            if elt in b: 
                b.remove(elt)
    primes = primes.union(b)
    return(len(primes))

# find M
def find_M(N):
    all_num_hor = floor(N/4)
    M = 0
    for num_hor in range(all_num_hor+1):
        num_vert = N - num_hor*4
        val = factorial(num_hor + num_vert)/(factorial(num_hor) * factorial(num_vert))
        M += val
    return(M)

# find P 
def find_P(N):
    if N < 4:
        return(0)
    elif N == 4:
        return(1)
    M = find_M(N)
    P = sieve(int(M))
    return(P)
    
# number of test cases
T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    P = find_P(N)
    print(P)


    
