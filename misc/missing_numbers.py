#!/bin/python3

import sys
from collections import Counter

# https://www.hackerrank.com/challenges/missing-numbers

n = int(input().strip())
list1 = [int(q_temp) for q_temp in input().strip().split(' ')]
count1 = Counter(list1)
m = int(input().strip())
list2 = [int(q_temp) for q_temp in input().strip().split(' ')]
count2 = Counter(list2)

list2a = list(set(list2))

miss = list()

for i in range(len(list2a)):
    x = list2a[i]
    if count1[x] != count2[x]:
        miss.append(x)

miss.sort()
miss1 = ' '.join(str(x) for x in miss)
print(miss1)
        




