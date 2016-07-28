#!/bin/python3

import sys
import os 
from heapq import heappush, heappop, heapify 
from math import floor

# https://www.hackerrank.com/challenges/equal
        
# functions

def search(arr):   
    heap = []
    for item in arr:
        heappush(heap, -item)
    moves = 0
    min_val = max(heap)
    diff = 100
    while diff > 0:
        max_val = heappop(heap)
        diff = abs(max_val - min_val)
        if diff >= 5:
            times = floor(diff/5)
            heappush(heap,max_val+times*5)
        elif diff >=2:
            times = floor(diff/2)
            heappush(heap,max_val+times*2)
        else:
            times = 1
            heappush(heap,max_val+times)
        moves += times
    return(moves-1)          

T = int(input().strip())

for i in range(T):
    N = T = int(input().strip())
    arr = [int(q_temp) for q_temp in input().strip().split(' ')]
    moves = search(arr)
    print(moves)
    
    
    
