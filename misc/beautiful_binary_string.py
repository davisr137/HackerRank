import sys

# https://www.hackerrank.com/challenges/beautiful-binary-string

# parse inputs
N = int(input().strip())
s = input().strip()

steps = 0
last_index = None

# iterate over string
for i in range(0,N-2):
    # found bad substring
    if s[i:i+3] == '010':
        # check that bad substring does not overlap with previous bad substring
        if last_index == None or i > last_index+2:
            last_index = i
            steps += 1
print(steps)