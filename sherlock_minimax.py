#!/bin/python3

import sys
from math import floor

# https://www.hackerrank.com/challenges/sherlock-and-minimax

# parse inputs
N = int(input().strip())
A = [int(q_temp) for q_temp in input().split(' ')]
P,Q = [int(q_temp) for q_temp in input().split(' ')]

# sort array
A.sort()

best_minimax = 0

# three cases

# 1) less than all elements in A

if min(A) - P > best_minimax:
    best_minimax = min(A) - P
    best_int = P
    
# 2) between the two consecutive elements in A for which there is the largest difference

for i in range(len(A)-1):
        
    this_diff = A[i+1] - A[i]
    
    if A[i] >= P and A[i+1] <= Q: 
        if floor(this_diff/2) > best_minimax:
            best_minimax = floor(this_diff/2)
            best_int = floor((A[i] + A[i+1])/2)
            
    elif A[i] >= P and A[i+1] > Q:
        if Q - A[i] < floor(this_diff/2):
            if Q - A[i] > best_minimax:
                best_minimax = Q - A[i]
                best_int = Q
        else:
            if floor(this_diff/2) > best_minimax:
                best_minimax = floor(this_diff/2)
                best_int = floor((A[i] + A[i+1])/2)
    
    elif A[i] < P and A[i+1] <= Q:
        if A[i+1] - P < floor(this_diff/2): 
            if A[i+1] - P > best_minimax:
                best_minimax = A[i+1] - P
                best_int = P
        else:
            if floor(this_diff/2) > best_minimax:
                best_minimax = floor(this_diff/2)
                best_int = floor((A[i] + A[i+1])/2)
    
# 3) greater than all elements in A
    
if Q - max(A) > best_minimax:
    best_minimax = Q - max(A) 
    best_int = Q

# print result

print(best_int)


