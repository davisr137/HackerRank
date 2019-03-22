#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/two-arrays

q = int(input().strip())

for i in range(q):

    n,k = [int(q_temp) for q_temp in input().split(' ')]

    A = [int(q_temp) for q_temp in input().split(' ')]
    B = [int(q_temp) for q_temp in input().split(' ')]
    
    A.sort()
    B.sort(reverse=True)
    
    valid = True
    
    for i in range(n):
        if A[i] + B[i] < k:
            valid = False
            break
    
    if valid:
        print('YES')
    else:
        print('NO')

    
    