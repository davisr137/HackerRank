#!/bin/python3

import sys
from heapq import heappush, heappop

# https://www.hackerrank.com/challenges/hexagonal-grid
    
def search(h,a):
    if len(h) == 0:
        return(1)
    
    d = heappop(h)
    y = d[1]
    x = d[2]
    
    hc = h.copy()
    ac = a.copy()
    
    move = list([0])
    
    if y == 0:
        if x > 0:
            # block going left
            if a[y][x-1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y][x-1] = 1
                hc.remove((0,y,x-1))
                move.append(search(hc,ac))
            else:
                move.append(0)
            
            # block going left down
            if a[y-1][x-1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y+1][x-1] = 1
                hc.remove((0,y+1,x-1))
                move.append(search(hc,ac))
            else:
                move.append(0)
        
        # block going down
        if a[y+1][x] == 0:
            hc = h.copy()
            ac = a.copy()
            ac[y][x] = 1
            ac[y+1][x] = 1
            hc.remove((0,y+1,x))
            move.append(search(hc,ac))
        else:
            move.append(0)
            
        if x < N-1:
    
            # block going right
            if a[y][x+1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y][x+1] = 1
                hc.remove((0,y,x+1))
                move.append(search(hc,ac))
            else:
                move.append(0)
                
    
    elif y == 1:
        if x > 0:
            # block going left
            if a[y][x-1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y][x-1] = 1
                hc.remove((0,y,x-1))
                move.append(search(hc,ac))
            else:
                move.append(0)
        
        # block going up
        if a[y-1][x] == 0:
            hc = h.copy()
            ac = a.copy()
            ac[y][x] = 1
            ac[y-1][x] = 1
            hc.remove((0,y-1,x))
            move.append(search(hc,ac))
        else:
            move.append(0)
            
        if x < N-1:
            # block going right up 
            if a[y-1][x+1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y-1][x+1] = 1
                hc.remove((0,y-1,x+1))
                move.append(search(hc,ac))
            else:
                move.append(0)
    
            # block going right
            if a[y][x+1] == 0:
                hc = h.copy()
                ac = a.copy()
                ac[y][x] = 1
                ac[y][x+1] = 1
                hc.remove((0,y,x+1))
                move.append(search(hc,ac))
            else:
                move.append(0)
    
    return(max(move))
    
     
T = int(input().strip())

for i in range(17):
    N = int(input().strip())
    a = list()
    a.append([int(x) for x in list(input().strip())])
    a.append([int(x) for x in list(input().strip())])

    h = []
    for j in range(2):
        for k in range(N):
            if a[j][k] == 0:
                heappush(h,tuple((a[j][k],j,k)))
    
    out = search(h,a)
    if out:
        print('YES')
    else:
        print('NO')
    
    


