#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/new-year-chaos

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    # initialize list of bribes
    bribes = [0]*n
    moves = 0
    while len(q) > 1:
        minindex = q.index(min(q))
        while minindex != 0:
            prev = q[minindex-1]
            q[minindex-1] = min(q)
            q[minindex] = prev
            bribes[prev-1] = bribes[prev-1] + 1
            minindex = minindex - 1
            moves = moves+1
        q = q[1:len(q)]
    if max(bribes) > 2:
        print('Too chaotic')
    else:
        print(moves)