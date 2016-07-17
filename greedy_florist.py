#!/bin/python3

import sys
from math import floor
        
# https://www.hackerrank.com/challenges/greedy-florist

N,K = [int(q_temp) for q_temp in input().strip().split(' ')]
cost = [int(q_temp) for q_temp in input().strip().split(' ')]

cost.sort()

# greedy solution 
# repeat buy at the lowest prices; buy higher priced items first

if N <= K:
    total = sum(cost[:N])
else:
    repeats = N-K
    extra = K/N
    # minimum number of flowers each person needs to buy
    ef = floor(N/K)
    # number of people who buy one more than the minimum
    ex = N % K
    index = ex
    # people who are buying largest quantities of flowers
    total = sum(cost[0:index]*(ef+1))  
    num = ef  
    # iterate over numbers of flowers to buy
    while num > 0:
        total += sum(cost[index:index+K]*num) 
        index += K
        num -= 1
        
print(total)
        
    
    


    