#!/bin/python3

import os
from collections import Counter

def check_magazine(magazine, note):
    """
    Check if we can replicate the message in 'note' with 
    words in 'magazine'.

    Args:
        magazine (list of str): Words available in magazine.
        note (list of str): Words needed for note.

    Returns:
        str: 'Yes' if we can replicate the note with the 
            magazine, 'No' if not.
    """
    words_magazine = dict(Counter(magazine))
    for word in note:
        if word not in words_magazine:
            return 'No'
        if words_magazine[word] == 0:
            return 'No'
        words_magazine[word] = max(0, words_magazine[word]-1)
    return 'Yes'


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(check_magazine(magazine, note))
