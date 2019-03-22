import numpy as np
import pandas as pd

# https://www.hackerrank.com/challenges/alternating-characters

T = int(input())

for j in range(0,T):
    
    sum = 0
    
    our_str = str(input())
    
    N = len(our_str)
    
    sum = 0
    for i in range(0,N-1):
        if our_str[i] == our_str[i+1]:
            sum = sum + 1
        
    print(sum)