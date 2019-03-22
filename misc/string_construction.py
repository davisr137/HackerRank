#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/string-construction

# function to find the cost to copy string
def process_string(s):
    found = set()
    cost = 0
    for i in range(len(s)):
        if s[i] not in found:
            cost +=1 
            found.add(s[i])
    return(cost)

# process inputs
N = int(input().strip())
for i in range(N):
    s = input().strip()
    cost = process_string(s)
    # print total cost
    print(cost)
    
