#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/mark-and-toys

# parse inputs
N,K = [int(q_temp) for q_temp in input().split(' ')]
a = [int(q_temp) for q_temp in input().split(' ')]

# sort list of toys
a.sort()

# select toys in increasing order of price until limit
tot = 0
i=0
while tot <= K:
    tot += a[i]
    i += 1
    
# print result
print(i-1)






    
    