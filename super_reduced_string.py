import sys
import os

# IO
# s = input().strip()
s = 'aa'

# start index at zero
index = 0

# 'D' terminates the string
s = s + 'D'

def parse(s):
    index = 0
    num_del = 0
    while s[index] != 'D':
        # same letter
        if s[index] == s[index+1]:
            s = s[0:index] + s[index+2:]
            num_del += 1
        else:
            index += 1
    return([s,num_del])

nd = 1
while nd > 0:
    [s,nd] = parse(s)
    

# remove 'D' at end
s = s.replace("D", "")
if len(s) > 0:
    # print result
    print(s)
else:
    print('Empty string')