#!/bin/python3

import sys
        
# https://www.hackerrank.com/challenges/crush  

# set parameters

N,M = [int(q_temp) for q_temp in input().strip().split(' ')]

arr = [0]*N

steps = list()
for i in range(M):
    vals = [int(q_temp) for q_temp in input().strip().split(' ')]
    for j in range(vals[0]-1,vals[1]):
        arr[j]+=vals[2]
    steps.append(vals)
    
print(max(arr))


