#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/sam-and-substrings  

# parse inputs
s = input().strip()
l = list(s)
a = [int(x) for x in l]

# initialize variables
L = len(s)
mod_div = 10**9 + 7
prev = 0
m=10**(-1)
total = 0

# compute substring sum 
for i in range(0,L):
    jj = L-i
    # use properties of modulo operator to use less time and space
    m = m*10 % mod_div
    mult = (m + prev) % mod_div
    total += (a[jj-1] * mult * jj) % mod_div
    prev = mult

# output result
print(int(total % mod_div))
        


    
    
