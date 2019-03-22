#!/bin/python3

import sys
        
# https://www.hackerrank.com/challenges/beautiful-pairs
    
# function to build dictionary for where each element is 
def buildDictionary(A,B):
    
    dA = dict()
    A1 = A.copy()
    setA = list(set(A))
    for i in range(len(setA)):
        dA[setA[i]] = list()
    
    dB = dict()
    B1 = A.copy()
    setB = list(set(B))
    for i in range(len(setB)):
        dB[setB[i]] = list()
    
    for i in range(N):
        dA[A[i]].append(i)
        dB[B[i]].append(i)

    return([dA,dB])
    
# function to compute number of pairwise disjoint beautiful pairs
def countPairs(dA,dB):
    dAc = dA.copy()
    dBc = dB.copy()
    setA = list(set(A))
    total = 0
    for i in range(len(setA)):
        elt = setA[i]
        appA = dAc[elt]
        if elt in dBc:
            appB = dBc[elt]
        else:
            appB = list()
        # same number of appearances
        if len(appA) ==  len(appB):
            dAc[elt] = list()
            dBc[elt] = list()
            total+=len(appA)
        # A has more appearances
        elif len(appA) >  len(appB):
            dBc[elt] = list()
            del dAc[elt] [:len(B)]
            total+=len(appB)
        # B has more appearances
        else:
            dAc[elt] = list()
            del dBc[elt] [:len(A)]
            total+=len(appA)
    return(total)
    
N = int(input().strip())
A = [int(q_temp) for q_temp in input().strip().split(' ')]
B = [int(q_temp) for q_temp in input().strip().split(' ')]

sA = A.copy()
sA.sort()
sB = B.copy()
sB.sort()

# Arrays are the same; are we allowed to not change any elements? 
if sA == sB:
    print(len(A)-1)
else:
    [dA,dB] = buildDictionary(A,B)
    total = countPairs(dA,dB)
    print(total+1)




    