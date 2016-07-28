#!/bin/python3

import sys
import os 
from heapq import heappush, heappop, heapify  
        
# https://www.hackerrank.com/challenges/equal        
        
# functions

def update_array(arr,idx,add):
    arr = [x+add for x in arr]
    arr[idx]-=add
    return(arr)

def search(arr):    
    moves = 0
    min_val = min(arr)
    min_idx = arr.index(min_val)
    while len(set(arr)) > 1:
        # get min and max vals
        min_val = arr[min_idx]
        max_val = max(arr)
        max_idx = arr.index(max_val)
        diff = max_val - min_val
        # add 5
        if diff >= 5:
            arr = update_array(arr,max_idx,5)
        # add 2
        elif max_val - min_val >= 2:
            arr = update_array(arr,max_idx,2)
        # add 1
        else:
            arr = update_array(arr,max_idx,1)
        # increment count of moves
        moves += 1
    return(moves)          

T = int(input().strip())

for i in range(T):
    N = T = int(input().strip())
    arr = [int(q_temp) for q_temp in input().strip().split(' ')]
    moves = search(arr)
    print(moves)

    
    
    