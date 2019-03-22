#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/two-strings

T = int(input().strip())

for i in range(T):
    A = input().strip()
    B = input().strip()
    a = list(set(A))
    b = list(set(B))
    c = list(set(a).intersection(b))
    if len(c) > 0:
        print('YES')
    else:
        print('NO')
