import sys
from math import factorial

# https://www.hackerrank.com/challenges/sherlock-and-anagrams

def nCk(n,k):
    val = factorial(n) / (factorial(k) * factorial(n-k))
    return(val)

def search(s):
    
    total = 0
    l = len(s)
    
    # build initial dictionary
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = list([i])
    
    # single character anagrams
    keys = d.keys()
    remove = list()
    for key in keys:
        if len(d[key]) > 1:
            total += nCk(len(d[key]),2)
        else:
            remove.append(key)
            
    # remove keys
    d = {key: d[key] for key in d if key not in remove}
            
    # anagrams of length greater than one
    sub_len = 2
    
    while len(d) > 0:
    
        keys = d.keys()    
        d2 = dict()
    
        # iterate through keys
        for key in keys:
            before = dict()
            after = dict()
            # iterate through each index where key appears
            for index in d[key]:
                if index > 0:
                    b_index = index-1
                    if s[b_index] in before:
                        before[s[b_index]].append(b_index)
                    else:
                        before[s[b_index]] = ([b_index])    
                if index < l-sub_len:
                    a_index = index+sub_len-1
                    if s[a_index] in after:
                        after[s[a_index]].append(a_index)
                    else:
                        after[s[a_index]] = ([a_index])  
                        
            # construct substrings of length one greater
            
            bkeys = before.keys()
            for bkey in bkeys:
                new_s = bkey + key
                if bkey in after:
                    if new_s not in d2:
                        d2[new_s] = set()
                    for bval in before[bkey]:
                        if bkey in after:
                            for aval in after[bkey]:
                                if bval != aval - sub_len + 1:
                                    d2[new_s].add(bval)
                                    
            for d2key in d2.keys():
                total += len(d2[d2key])
            
        d = d2.copy()
        sub_len += 1
    
    return(total)
            
# parse inputs

T = int(f.readline().strip())

for i in range(T):
    s = f.readline().strip()
    out = search(s)
    print(out)
    
            
        
        
    
    
    