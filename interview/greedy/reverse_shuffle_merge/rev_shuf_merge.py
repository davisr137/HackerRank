#!/bin/python3

import os
import copy
from collections import Counter

def get_letter_index_dict0(s):
    """
    Get dictionary of indices at which letters appear
    in string. 

    Args:
        s (str): Our string.

    Returns:
        dict: Keys are letters. Each value is a set of 
            indices at which that letter appears.
    """
    index = dict()
    for i, letter in enumerate(s):
        if letter not in index:
            index[letter] = set()
        index[letter].add(i)
    return index

def get_letter_index_dict(s):
    """
    Get dictionary of indices at which letters appear
    in string.

    Args:
        s (str): Our string.

    Returns:
        dict: Keys are letters. Each value is a list of
            indices at which that letter appears (in 
            ascending order). 
    """
    index = dict()
    for i, letter in enumerate(s):
        if letter not in index:
            index[letter] = list()
        index[letter].append(i)
    return index

def get_letter_count(s):
    """
    Get counts of how many times each letter appears in s.

    Args:
        s (str): Our string.

    Returns:
        dict: Keys are letters. Each value is an int representing
            the number of times the letter appears in the string.
    """
    return dict(Counter(s))
    
def split_string(ct):
    """
    Split string into strings of like character counts. 

    Args:
        ct (dict): Keys are letters. Each value is an int 
            representing the number of times the letter appears 
            in the string.

    Returns:
        dict: Same as ct, but with each value divided by two.
    """
    ct = ct.copy()
    for letter in ct:
        if ct[letter] % 2 != 0:
            raise AssertionError("Letter count must be even!")
        ct[letter] = int(ct[letter] / 2)
    return ct

def valid_reverse_merge_str(rs, index, max_index=None):
    """
    Check if string rs is a valid merge substring of string
    represented by dict index.

    Args:
        rs (str): Our string.
        index (dict): Keys are letters. Each value is a list of
            indices at which that letter appears (in ascending order).

    Returns:
        bool: True if a valid merge substring, else False
    """
    index_s = copy.deepcopy(index)
    if max_index is None:
        max_index = 10**10
    i_last = max_index
    for li in range(len(rs)-1, -1, -1):
        letter = rs[li]
        if letter not in index_s:
            return [False, None, None]
        i = index_s[letter].pop()
        if i > i_last:
            return [False, None, None]
        i_last = i
    return [True, i_last, index]


# Example: s = "aaabeeba"
# Maintain a list of unique letters in order: "abe"
# Remove a letter once it has been used completely (e.g.
# if there were two original a's and we use two a's).
# Maintain a dict of counts of each letter.
# Use stack to represent substring in progress of being built?

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = reverseShuffleMerge(s)
    fptr.write(result + '\n')
    fptr.close()

