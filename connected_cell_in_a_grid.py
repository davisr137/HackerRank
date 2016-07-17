#!/bin/python3

import sys
from collections import Counter

# https://www.hackerrank.com/challenges/connected-cell-in-a-grid

m = int(input().strip())
n = int(input().strip())

list1 = list()

for i in range(m):
    list1.append([int(q_temp) for q_temp in input().strip().split(' ')])

# largest component - how to keep track of size of component? 

# label each item part of a component? 

x = list()
y = list()

# number of connected component
comp = 1

# initialize grid; all zeros
grid = [[0]*n for _ in range(m)]

# iterate through items in grid
for i in range(m):
    for j in range(n):
        if list1[i][j]:
            mark = 0
            # check up and to the left first; these are already examined
            
            # upper
            if i > 0:
                if list1[i-1][j]:
                    mark = 1
                    grid[i][j] = grid[i-1][j]                    
            # upper left
            if i > 0 and j > 0:
                if list1[i-1][j-1]:
                    if mark:
                        valto = grid[i][j]
                        valfrom = grid[i-1][j-1]
                        for k in range(0,i+1):
                            grid[k] = [valto if v == valfrom else v for v in grid[k]]
                    else:
                        mark = 1
                        grid[i][j] = grid[i-1][j-1]
            # upper right
            if i > 0 and j < n-1:
                if list1[i-1][j+1]:
                    if mark:
                        valto = grid[i][j]
                        valfrom = grid[i-1][j+1]
                        for k in range(0,i+1):
                            grid[k] = [valto if v == valfrom else v for v in grid[k]]
                    else:
                        mark = 1
                        grid[i][j] = grid[i-1][j+1]
            # left
            if j > 0:
                if list1[i][j-1]:
                    if mark:
                        valto = grid[i][j]
                        valfrom = grid[i][j-1]
                        for k in range(0,i+1):
                            grid[k] = [valto if v == valfrom else v for v in grid[k]]
                    else:
                        mark = 1
                        grid[i][j] = grid[i][j-1]
            if mark == False:
                grid[i][j] = comp
                comp = comp+1
     
# flatten sublists into single list
grid2 = [item for sublist in grid for item in sublist]

# find largest connected component
ugrid = list(set(grid2))
ct = Counter(grid2)
largest = 0
for i in range(1,len(ugrid)):
    if ct[ugrid[i]] > largest:
        largest = ct[ugrid[i]]

print(largest)
        
    
    

        
            
        




