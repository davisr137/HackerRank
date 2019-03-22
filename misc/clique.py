#!/bin/python3

import sys
from math import ceil, floor
        
# https://www.hackerrank.com/challenges/clique

T = int(input().strip())
    
# use binary search for O(log(N)) algorithm 

# For a graph G, Turan's theorem tells us the maximum number of edges for a number of vertices N such that G does not have a clique with r+1 vertices.  
def Turan(r,N):
    val = (1 - 1/r)*n**2/2
    return(val)
    
# From stackexchange
def Mstar(r,N):
    val = 0.5*(N**2 - (N % r)*ceil(N/r)**2 - (r - (N % r))*floor(N/r)**2)
    return(val)
    
# Binary search to find minimum size of the largest clique
def binarySearch(M,N):
    r = N
    search = True
    lower_bound = 0
    upper_bound = N
    while search:
        if Mstar(r-1,N) < M and Mstar(r,N) >= M:
            search = False
            break
        if Mstar(r,N) < M and Mstar(r+1,N) >= M:
            search = False
            r=r+1
            break
        if M < Mstar(r,N):
            if r < upper_bound:
                upper_bound = r
        else:
            if r > lower_bound:
                lower_bound = r
        r = round((upper_bound+lower_bound)/2)
    return(r)

# Process inputs    
for i in range(T):
    N,M = [int(q_temp) for q_temp in input().strip().split(' ')]
    val = binarySearch(M,N)
    print(val)
    
    







