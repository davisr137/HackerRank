import sys 
import os

def search(a,b):
    set_b = set(b)
    # both strings are empty; return true
    if len(a) == 0 and len(b) == 0:
        return(True)
    # only b is empty; if all letters are lower case in a, return true, since 
    # we can delete them all, else return false
    elif len(b) == 0:
        all_lower = True
        for ll in a:
            if ll.isupper():
                all_lower = False
        if all_lower:
            return(1)
        else: 
            return(0)
    # a is empty; no letters left to match; return false
    elif len(a) == 0:
        return(0)
    let_a = a[0]
    let_b = b[0]
    if a == b:
        return(1)
    if let_a.islower(): # lower case letter
        if let_a.upper() in set_b:
            cap = search(a[1:],b[1:])
            no_cap = search(a[1:],b)
            return(max(cap,no_cap))
        else: # delete letter
            return(search(a[1:],b))
    else:
        if let_a == let_b:
            return(search(a[1:],b[1:]))
        else:
            return(0)
            
path = '/Users/ryandavis/Dropbox/HackerRank/Abbreviation'
os.chdir(path)
fname = 'in3.txt'

# open file
f = open(fname)

N = int(f.readline().strip())
for i in range(N):
    a = f.readline().strip()
    b = f.readline().strip()
    out = search(a,b)
    if out:
        print('YES')
    else:
        print('NO')

            