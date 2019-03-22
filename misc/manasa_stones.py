#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/manasa-and-stones

T = int(input().strip())
values = list()

for index in range(T):
    
    values = list()
    
    N = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
   
    steps = N-1
    for i in range(N):
        sum = i*a + (steps - i)*b
        values.append(sum)
    
    values = list(set(values))
    values.sort()
    print(' '.join([str(i) for i in values]))