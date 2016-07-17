#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/cavity-map

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)

x = list()
y = list()

for row in range(len(grid)):
   for col in range(len(grid[row])):
      depth = int(grid[row][col])
      # not on an edge
      edge = row == 0 or row == max(range(len(grid))) or col == 0 or col == len(grid[row]) - 1;
      if (edge == False):
         above = int(grid[row-1][col]) < depth
         below = int(grid[row+1][col]) < depth
         left = int(grid[row][col-1]) < depth
         right = int(grid[row][col+1]) < depth
         if (above and below and left and right):
            x.append(row)
            y.append(col)
            
for i in range(len(x)):
   row = x[i]
   col = y[i]
   grid[row] = grid[row][0:col] + 'X' + grid[row][col+1:len(grid[row])]

# print changed grid
for i in range(len(grid)):
    print(grid[i])