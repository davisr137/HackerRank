#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-6/challenges/bear-and-steady-gene

import sys
from collections import Counter

n = int(input().strip())
s = input().strip()

ct = Counter(list(s))
tgt = n/4

A = ct['A']
T = ct['T']
G = ct['G']
C = ct['C']

mA = int(ct['A'] - tgt)
mT = int(ct['T'] - tgt)
mG = int(ct['G'] - tgt)
mC = int(ct['C'] - tgt)

m = {'A' : mA, 'T' : mT, 'G' : mG, 'C': mC}

# minimum string length; constant time improvement
start_len = max(mA,mT,mG,mC)

start_index = 0
end_index = start_len
min_len = len(s)

s1 = s[start_index:end_index]
ct1 = Counter(list(s1))

# get first substring
while ct1['A'] < mA or ct1['T'] < mT or ct1['G'] < mG or ct1['C'] < mC:
    #print(end_index)
    end_index = end_index + 1
    s1 = s[start_index:end_index]
    key = s[end_index-1]
    ct1[key] = ct1[key] + 1

# remove characters that do not need reduction
key = s[start_index]
while ct1[s[start_index]] - 1 >= m[s[start_index]]:
    key = s[start_index]
    ct1[key] = ct1[key] -1
    start_index = start_index + 1

# update min index    
if end_index-start_index < min_len:
    min_len = end_index-start_index

# move forward in string
while end_index < len(s)-1:
    end_index = end_index + 1
    s1 = s[start_index:end_index]
    k = s[end_index-1]
    ct1[k] = ct1[k]+1
    # check if new character is repeated from beginning of substring
    if s[end_index-1] == s[start_index]:
        l = s[start_index]
        ct1[l] = ct1[l] - 1
        start_index = start_index + 1
        # remove extra characters at beginning of substring
        key = s[start_index]
        while ct1[key] - 1 >= m[key]:
            ct1[key] = ct1[key] -1
            start_index = start_index + 1
            key = s[start_index]
            if end_index-start_index < min_len:
                min_len = end_index-start_index
                
# should not be getting negatives in ct1
print(min_len)

