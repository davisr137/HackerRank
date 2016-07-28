#!/bin/python3

import sys
import os 
from heapq import heappush, heappop, heapify  

# https://www.hackerrank.com/challenges/equal
        
# functions

def update_array(heap,min_val):
    max_val = heappop(heap)
    diff = abs(max_val - min_val)
    if diff >= 5:
        add = 5
    # add 2
    elif diff >= 2:
        add = 2
    # add 1
    else:
        add = 1
    heap = [x-add for x in heap]
    heappush(heap,max_val)
    min_val -= add
    return([heap,min_val])

def search(arr):   
    heap = []
    for item in arr:
        heappush(heap, -item)
    heap1 = []
    for item in arr:
        heappush(heap1, item)
    moves = 0
    min_val = max(heap)
    while len(set(heap)) > 1:
        [heap,min_val] = update_array(heap,min_val)
        moves += 1
    return(moves)          

T = int(input().strip())

for i in range(T):
    N = T = int(input().strip())
    arr = [int(q_temp) for q_temp in input().strip().split(' ')]
    moves = search(arr)
    print(moves)
    
    
    
