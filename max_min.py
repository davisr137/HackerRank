#!/bin/python3

import sys
        
# https://www.hackerrank.com/challenges/angry-children    

# set parameters

N = int(input().strip())
K = int(input().strip())

arr = list()

for i in range(N):
    arr.append(int(input().strip()))
    
arr.sort()
unfairness = arr[K-1] - arr[0]
for i in range(N-K+1):
    if arr[i + K-1] - arr[i] < unfairness:
        unfairness = arr[i + K-1] - arr[i]

print(unfairness)
    


