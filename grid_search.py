#!/bin/python3

import sys
import os

# https://www.hackerrank.com/challenges/the-grid-search

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)
    
    found = 0
    for i in range(R):
        substr = P[0] in G[i]
        if substr:
            all_start_index = [m.start() for m in re.finditer('(?='+P[0]+')', G[i])]
            for k in range(0,len(all_start_index)):
                start_index = all_start_index[k]
                end_index = start_index + len(P[0])
                found = 1
                for j in range(1,r):
                    match = G[i+j][start_index:end_index] == P[j]
                    if match == 0:
                        found = 0
                if found:
                    break
        if found:
            break
   if found:
      print('YES')
   else:            
      print('NO')
         






