#!/bin/python3

import sys
from heapq import heappush, heappop  

# https://www.hackerrank.com/challenges/jim-and-the-orders

n = int(input().strip())

h = list()

t = list()
d = list()
for i in range(n):
    ti,di = [int(q_temp) for q_temp in input().strip().split(' ')]
    t.append(ti)
    d.append(di)
    heappush(h,(ti+di,i+1))

val = heappop(h)
out = str(val[1])
while len(h) > 0:
    val = heappop(h)
    out=out+' '+str(val[1])
    
print(out)



    