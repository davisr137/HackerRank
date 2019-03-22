#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/larrys-array

def larry_rotate(x):
    a = x[0]
    b = x[1]
    c = x[2]
    return([b,c,a])

T = int(input().strip())

for t in range(T):
        
    n = int(input().strip())
   
    A = input().strip()
    b = list(map(int,A.split()))
    bsort = b.copy()
    bsort.sort()
    borig = b.copy()
    stop = 0
    index = 0
    balg = b.copy()
    
    # we can sort all but the last three numbers in all cases
    while len(balg) > 3:
        minindex = balg.index(min(balg))
        while minindex > 0:
            # min at end of array
            if minindex == len(balg) - 1:
                balg[minindex-2:minindex+1] = larry_rotate(balg[minindex-2:minindex+1])
            # min not at end of array
            else:                
                balg[minindex-1:minindex+2] = larry_rotate(balg[minindex-1:minindex+2])
            # decrement minindex
            minindex = minindex-1
        balg = balg[1:len(balg)]
        
    # determine if we can sort the last three numbers
    balgsort = balg.copy()
    balgsort.sort()
    balgrev = balgsort[::-1]
    resolved = 0
    while resolved == 0:
        if balg == balgsort:
            resolved = 1
            print('YES')
            break
        elif balg == balgrev:
            resolved = 1
            print('NO')
            break
        balg = larry_rotate(balg)
    
    
    
    
    
    
                
        
        
    