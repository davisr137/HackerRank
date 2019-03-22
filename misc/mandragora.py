#!/bin/python3

import sys
from collections import Counter
        
# https://www.hackerrank.com/challenges/mandragora   

# set parameters

# number of input cases
T = int(input().strip())

for i in range(T):
    
    N = int(input().strip())
    H = [int(q_temp) for q_temp in input().strip().split(' ')]

    # sort H
    h = H.copy()
    h.sort()
    hsize = len(h)
        
    # intitial conditions
    S = 1 
    P = 0
    
    # do we start from the end? 
    max_score = 0
    battle = 0
    
    for i in range(hsize):
        cut = hsize - 1 - i
        eat = h[0:cut]
        battle+= h[cut]
        score = sum(battle)*(1+cut)
        if score > max_score:
            max_score = score 
    
    print(max_score)

# strategy to eat first, then battle
# can we prove that it is never optimal to eat after battling? I think so. Can always increase the score by changing an eat to a battle (or switching the eat to an earlier place)



