import sys

# https://www.hackerrank.com/challenges/unbounded-knapsack

# search space of possible packings
def search(packed, max_pack, a, k):
    
    # iterate while it is possible to add to the knapsack
    while len(packed) > 0:
        new_pack = list()
        # add element from a to packing to form new packing
        for pack in packed:
            for elt in a:
                val = pack + elt
                if val <= k:
                    new_pack.append(val)
        # update best solution
        if len(new_pack) == 0:
            max_pack = max(max_pack,max(packed))
        else:
            max_pack = max(max_pack,max(new_pack))
        # set current packing to new packing
        packed = new_pack
    
    return(max_pack)

# run knapsack algorithm
def knapsack(n,k,a):
    
    # remove elements that are multiples of other elements
    # remove elements that are greater than k
    rem = set()
    for elt1 in a:
        for elt2 in a:
            if elt1 % elt2 == 0 and elt1 > elt2:
                rem.add(elt1)
            if elt1 > k: 
                rem.add(elt1)
    for eltr in rem:
        a.remove(eltr)
    
    # if no elements less than or equal to k, return 0
    if len(a) == 0:
        return(0)
        
    # return if we find solution of all of one element
    for elt in a:
        val = k % elt 
        if k % elt == 0:
            return(k)
            break
    
    # set initial packings and best solution
    packed = list(a)
    max_pack = max(a)
    
    # solve
    max_pack = search(packed, max_pack, a, k)
            
    return(max_pack)

# number of cases
T = int(input().strip())

for i in range(T):
    # parse inputs
    n,k = [int(q_temp) for q_temp in input().strip().split(' ')]
    a = set([int(q_temp) for q_temp in input().strip().split(' ')])
    # find solution
    out = knapsack(n,k,a)
    print(out)
    
    
