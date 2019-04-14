#!/bin/python3

import os
from collections import Counter

def make_anagram(a, b):
    """
    Find minimum number of deletions required to make
    strings a and b anagrams. a and b can be of different
    length.

    Args:
        a (str)
        b (str)

    Returns:
        int: Number of deletions required
    """
    # Frequency count of each letter
    a_ct = dict(Counter(a))
    b_ct = dict(Counter(b))
    # Unique letters in either string
    letters = set(a_ct.keys()) | set(b_ct.keys())
    delete = 0
    for letter in letters:
        if letter not in a_ct: # Letter in b, not a 
            delete += b_ct[letter]
        elif letter not in b_ct: # Letter in a, not b
            delete += a_ct[letter]
        else: # Letter in a and b
            # Delete enough letters from larger frequency so
            # it equals smaller frequency.
            if a_ct[letter] >= b_ct[letter]:
                delete += a_ct[letter] - b_ct[letter]
            else:
                delete += b_ct[letter] - a_ct[letter]
    return delete


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = make_anagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()

