#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/mars-exploration

# function to find number of altered letters
def process_string(s):
    alt_let = 0
    for i in range(len(s)):
        rem = i % 3
        if rem == 0 or rem == 2:
            if s[i] != 'S':
                alt_let += 1
        elif rem == 1:
            if s[i] != 'O':
                alt_let += 1
    return(alt_let)

# process inputs
s = input().strip()
alt_let = process_string(s)
# print number of altered letters
print(alt_let)
