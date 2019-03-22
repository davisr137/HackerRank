import sys

# https://www.hackerrank.com/challenges/icecream-parlor

# search for ice cream combo
def search(m,n,c):
    # dicitonary for previously seen costs
    d = dict()
    i = 0
    while i < n:
        cost = c[i]
        need = m - c[i] 
        if need in d:
            # return first combination that works
            return([d[need]+1,i+1])
        else:
            d[cost] = i
        i += 1

# number of test cases
T = int(input().strip())

for i in range(T):
    m = int(input().strip())
    n = int(input().strip())
    c = [int(q_temp) for q_temp in input().strip().split(' ')]
    # compute result
    result = search(m,n,c)
    # format output string
    out = str(result[0]) + ' ' + str(result[1])
    print(out)

