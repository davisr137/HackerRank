#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/sherlock-and-valid-string   

# parse input
s = input().strip()

# dictionary for number of times each character appears
d = dict()
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

# dictionary for number of times each total number of a character appears
vd = dict()
for value in d.values():
    if value in vd:
        vd[value] += 1
    else:
        vd[value] = 1
      
# print result
if len(vd) > 2:
    print('NO')
else:
    app = list(vd.values())
    app = [x for x in app if x > 1]
    if len(app) > 1:
        print('NO')
    else:
        print('YES')
