#!/bin/python3

import sys
import os 

# https://www.hackerrank.com/challenges/array-splitting

# function to solve game 
def solve_game(N,A):
    sum_lr = list()
    sum_lr.append(A[0])
    for i in range(1,N):
        sum_lr.append(sum_lr[i-1] + A[i])
    out = search_game(sum_lr)
    return(out)

# use DP to search for solutions recursively
def search_game(sum_lr):
    # all numbers are the same
    if len(set(sum_lr)) == 1:
        return(len(sum_lr)-1)
    sum_lrs = set(sum_lr)
    half = sum_lr[-1]/2
    if half in sum_lrs:
        idx = sum_lr.index(half)
        left = sum_lr[0:idx+1]
        right = sum_lr[idx+1:]
        right = [x - half for x in right]
        return(1 + max(search_game(left),search_game(right)))
    else:
        return(0)

# open file

T = int(input().strip())

# process inputs    
for i in range(T):
    N = int(input().strip())
    A = [int(q_temp) for q_temp in input().strip().split(' ')]
    out = solve_game(N,A)
    print(out)
