#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/sherlock-and-array

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    arr = [int(q_temp) for q_temp in input().strip().split(' ')]
    right = sum(arr)
    left = 0
    found = 0
    for i in range(N):
        elt = arr[i]
        right = right - elt
        if left == right:
            found = 1
            break 
        left = left + elt
    if found:
        print('YES')
    else:
        print('NO')
        
        

