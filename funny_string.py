import sys

# https://www.hackerrank.com/challenges/funny-string

# parse input data

T = int(input().strip())

# iterate through each string
for i in range(T):
    str = f.readline().strip()
    # reverse string
    rev = str[::-1]
    funny = True
    # entire string must satisfy funny condition
    for j in range(1,len(str)):
        if abs(ord(str[j]) - ord(str[j-1])) != abs(ord(rev[j]) - ord(rev[j-1])):
            # break if funny condition is violated
            funny = False
            break
    # print results
    if funny:
        print('Funny')
    else:
        print('Not Funny')