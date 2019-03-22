import sys

# https://www.hackerrank.com/contests/master/challenges/common-child

# parse inputs
a = input().strip()
b = input().strip()

# use dynamic programming to solve longest common subsequence problem

def LCS(a,b):
    n = len(a)
    line = [0]*(n+1)
    pl = line.copy()
    for ai in range(1,n+1):
        char_a = a[ai-1]
        nl = line.copy()
        for bi in range(1,n+1):
            if char_a == b[bi-1]:
                nl[bi] = pl[bi-1] + 1
            else:
                nl[bi] = max(pl[bi], nl[bi-1])
        pl = nl.copy()
    return(nl[n])

print(LCS(a,b))
        
        
    