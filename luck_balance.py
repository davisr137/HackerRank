#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/luck-balance

# parse inputs; maintain lists of important and non-important contests
N,K = [int(q_temp) for q_temp in input().split(' ')]
important = list()
not_important = list()
for i in range(N):
    L,T = [int(q_temp) for q_temp in input().split(' ')]
    if T:
        important.append(L)
    else:
        not_important.append(L)

# sort list of important contests
important.sort(reverse = True)
    
# compute balance using greedy approach
# lose the first K important contests and win the rest
# lose all non-important contests
if K < len(important):
    balance = sum(important[0:K]) - sum(important[K:]) + sum(not_important)
else:
    balance = sum(important) + sum(not_important)
print(balance)
        
    
    


