#!/bin/python3

import sys
import string

# https://www.hackerrank.com/challenges/gem-stones
        
# initialize set to all letters
ls = set(string.ascii_lowercase)

# process data
N = int(input().strip())
for i in range(N):
    line = set(input().strip())
    ls = ls.intersection(line)

# output result
print(len(ls))