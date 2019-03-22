#!/bin/python3

import sys
from collections import Counter
        
# https://www.hackerrank.com/challenges/coin-change    

# set parameters

N,M = [int(q_temp) for q_temp in input().strip().split(' ')]
coins = [int(q_temp) for q_temp in input().strip().split(' ')]
c = set(coins)

# dictionary for number of ways to make given set
d = dict()

for i in range(1,N+1):
    if i == 1:
        if i in c:
            d[i]=list()
            d[i].append(Counter([i]))
    else:
        tot = list()
        j1 = 1
        j2 = i-1
        while j1 <= j2:
            # found solutions for subproblems
            if j1 in d and j2 in d:
                for k in range(len(d[j1])):
                    for l in range(len(d[j2])):
                        combo = d[j1][k] + d[j2][l]
                        if combo not in tot:
                            tot.append(combo)
            j1+=1
            j2-=1
        if i in c:
            d[i] = tot
            d[i].append(Counter([i]))
        else:
            if len(tot) > 0:
                d[i] = tot
if N in d:
    print(len(d[N]))
else:
    print(0)