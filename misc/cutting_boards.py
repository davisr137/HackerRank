#!/bin/python3

import sys
from heapq import heappush, heappop, heapify  
        
# https://www.hackerrank.com/challenges/board-cutting       

T = int(input().strip())

for i in range(T):
    
    m,n = [int(q_temp) for q_temp in input().strip().split(' ')]
    x = [int(q_temp) for q_temp in input().strip().split(' ')]
    y = [int(q_temp) for q_temp in input().strip().split(' ')]
    
    h = list()
    for j in range(len(x)):
        heappush(h,(-x[j],0))
    for j in range(len(y)):
        heappush(h,(-y[j],1))
        
    hcuts = 1
    vcuts = 1
    
    cost = 0
    while len(h) > 0:
        cut = heappop(h)
        # horizontal cut
        if cut[1] == 0:
            cost += -cut[0]*vcuts
            hcuts += 1
        elif cut[1] == 1:
            cost += -cut[0]*hcuts
            vcuts += 1
    print(cost%(10**9+7))

            
