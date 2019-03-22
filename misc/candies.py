#!/bin/python3

import sys
        
# http://stackoverflow.com/questions/11292913/candies-interviewstreet     

# set parameters

N = int(input().strip())
arr = list()

for i in range(N):
    arr.append(int(input().strip()))

# Initialize candy array
candy = [1]*N

# Pass left to right
for i in range(1,N):
    if arr[i] > arr[i-1]:
       candy[i] = candy[i-1] + 1

# Pass right to left
for i in range(0,N-1):
    j = N-2-i
    if arr[j] > arr[j+1]:
       candy[j] = max(candy[j+1]+1,candy[j])

# Print result
print(sum(candy))