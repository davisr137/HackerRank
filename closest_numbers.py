#!/bin/python3
import sys
    
# https://www.hackerrank.com/challenges/closest-numbers    

# parse data
L = int(input().strip())
line = input().strip().split(' ')
a = [int(item) for item in line]

# sort array
a.sort()

# find closest numbers
closest = 10**10
out = list()
for i in range(L-1):
    if a[i+1] - a[i] < closest:
        closest = a[i+1] - a[i] 
        out = list()
        out.append(a[i])
        out.append(a[i+1])
    elif a[i+1] - a[i] == closest:
        out.append(a[i])
        out.append(a[i+1])
    
# print output
print(' '.join(str(x) for x in out))
        
    
    
    