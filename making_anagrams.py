import sys

# https://www.hackerrank.com/challenges/making-anagrams

# parse input data
str1 = sorted(input().strip())
str2 = sorted(input().strip())

num_del = 0

# iterate while at least one of the strings is non-empty
while len(str1) > 0 or len(str2) > 0:
    # check that string 1 is not empty
    if len(str1) > 0:
        char1 = str1[0]
    else:
        str2.remove(str2[0])
        num_del += 1
        continue
    # check that string 2 is not empty
    if len(str2) > 0:
        char2 = str2[0] 
    else:
        str1.remove(str1[0])
        num_del += 1
        continue
    # character in string 1 > character in string 2
    if char1 > char2:
        str2.remove(char2)
        num_del += 1
    # character in string 2 > character in string 1
    elif char2 > char1: 
        str1.remove(char1)
        num_del += 1
    else:
        str1.remove(char1)
        str2.remove(char2)

# print number of deleted characters
print(num_del)        