#!/bin/python3

import os

# First find all palindromes where all characters 
# are the same

# Next find all palindromes where all characters
# except the middle one are the same. Palindrome 
# must be of odd length. First find all length-3
# palindromes. Build up to find all length-n+2 
# palindromes. Each length-n+2 palindrome must contain 
# a length-n palindrome. 

def count_same_palindromes(s):
    """
    Count number of substrings in string s where 
    all characters are the same.

    Args: 
        s (str): Our string
    
    Returns:
        int: Number of palindromes
    """
    last_letter = s[0]
    len_seq = 1
    count = 1
    for letter in s[1:]:
        if letter == last_letter:
            len_seq += 1
        else:
            len_seq = 1
        count += len_seq
        last_letter = letter
    return count


def get_mid_palindromes_3(s):
    """
    Get indices of palindromes of length 3 where all 
    characters are the same except for a different letter
    in the middle.

    Args:
        s (str): Our string

    Returns:
        list of int: Ending indices of palindromes. 
    """
    index = list()
    for i in range(2, len(s)):
        if s[i-2] == s[i] and s[i] != s[i-1]:
            index.append(i-1)
    return index

def is_mid_palindrome(s, mid, side_l):
    """
    Check if substring s[mid-side_l:mid+side_l] is a mid 
    palindrome. 

    Args:
        s (str): Our string. 
        mid (int): Index of middle letter.
        side_l (int): Number of letters on either side of the 
            middle letter.

    Returns:
        int: 1 if substring is a mid palindrome, else 0. 
    """
    if mid - side_l < 0:
        return 0
    if mid + side_l >= len(s):
        return 0
    if s[mid-side_l] != s[mid+side_l]:
        return 0
    if s[mid-side_l+1] != s[mid-side_l]:
        return 0
    if s[mid+side_l-1] != s[mid+side_l]:
        return 0
    return 1


def count_mid_palindrome(s):
    """
    Count number of mid palindromes (string with all same letters except
    for middle letter) in string s.

    Args:
        s (str)

    Returns:
        int: Number of mid palindromes.
    """
    index = get_mid_palindromes_3(s)
    count_mid = len(index)
    side_l = 2
    while index:
        remove = list()
        for mid in index:
            if not is_mid_palindrome(s, mid, side_l):
                 remove.append(mid)
        for mid_r in remove:
            index.remove(mid_r)
        count_mid += len(index)
        side_l += 1
    return count_mid

# How to speed up code??
# Instead of the while loop, count the length of longest
# string (of all the same letter) beginning at i and the 
# length of the longest string ending at i and memoize.
# Get the length-3 palindromes and find the max length 
# string on either side.

# Complete the substrCount function below.
def count_palindrome(n, s):
    """
    Count total number of palindromes in string s.

    Args:
        n (int): Length of string.
        s (str): Our string.

    Returns:
        int: Total number of palindromes.
    """
    count_same = count_same_palindromes(s)
    count_mid = count_mid_palindrome(s)
    return count_same + count_mid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = count_palindrome(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
