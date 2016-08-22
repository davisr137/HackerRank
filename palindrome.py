#!/bin/python3

# https://www.hackerrank.com/challenges/palindrome-index

import sys
from math import floor

# find character to change
def process_string(s):
    if s == s[::-1]:
        let = -1
    else:
        for i in range(len(s)):
            sc = s[0:i] + s[i+1:]
            if sc == sc[::-1]:
                let = i
                if let + 1 < N:
                    while s[let] == s[let+1] and let + 1 < N:
                        let += 1
                break
    return(let)
    
N = int(input().strip())
for i in range(N):
    s = input().strip()
    let = process_string(s)
    print(let)
    