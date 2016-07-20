#!/bin/python3

import sys
import os 

# https://www.hackerrank.com/challenges/grid-walking

# recursive function to traverse space
def traverse_space(N,M,x,D,memo):
    out = 0
    if M > 0:
        for i in range(N):
            if x[i] - 1 > 0:
                xc = x.copy()
                xc[i]-=1
                key = tuple([tuple(xc),M-1])
                if key in memo:
                    val = memo[key]
                else:
                    val = traverse_space(N,M-1,xc,D,memo)
                    memo[key] = val
                out += val
            if x[i] + 1 <= D[i]:
                xc = x.copy()
                xc[i]+=1
                key = tuple([tuple(xc),M-1])
                if key in memo:
                    val = memo[key]
                else:
                    val = traverse_space(N,M-1,xc,D,memo)
                    memo[key] = val
                out += val
        return(out)
    else:
        return(1)

# number of test cases
T = int(input().strip())

# process inputs    
for i in range(T):
    N,M = [int(q_temp) for q_temp in input().strip().split(' ')]
    x = [int(q_temp) for q_temp in input().strip().split(' ')]
    D = [int(q_temp) for q_temp in input().strip().split(' ')]
    out = traverse_space(N,M,x,D)
    memo = dict()
    out = traverse_space(N,M,x,D,memo)
    print(out % 1000000007)