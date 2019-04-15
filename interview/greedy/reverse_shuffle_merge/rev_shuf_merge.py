#!/bin/python3

import os
import copy
from collections import Counter


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
    return [True, i_last, index_s]


class State():
    """
    A class to represent the 'state' of the substring being built and
    the string of letters still available..
    """
    def __init__(self, used=None, needed=None, needed_l=None, available=None, i_last=10**10):
        """
        Initialize state. 

        Args:
            used (str): String built thus far.
            needed (dict): Letters needed to complete string. Each key is 
                a letter. Each value is an integer representing the 
                number of times the letter needs to be used to complete the 
                word.
            available (dict): Letters available to complete string. Each 
                keys is a letter. Each value is a list of integers representing
                indices at which letters are available. 
            i_last (int): Index of last letter used.
        """
        if used is None:
            used = ''
        self.used = used 
        self.needed = needed
        if not needed_l:
            self.needed_l = sorted(self.needed, reverse=True)
        self.available = available
        self.i_last = i_last

    @classmethod
    def from_string(cls, s):
        """
        Initialize from string. 

        Args:
            s (str): Raw string given.
        """
        ct = get_letter_count(s)
        kwargs = {
            'available' : get_letter_index_dict(s),
            'needed' : split_string(ct),
        }
        return cls(**kwargs)

    def add_letter(self, letter):
        """
        Add letter to string. Update available and needed 
        letters dictionaries.

        Args:
            letter (str): Letter to add.

        Returns:
            State: New state after letter is added.
        """ 
        # Add letter to array representing word
        used = self.used + letter
        # Return None if letter not available
        if letter not in self.available: # Letter not available
            return None
        available = copy.deepcopy(self.available)
        
        # Find index of next letter
        # Return None if we run out of available letters
        if not available[letter]:
            return None
        i_letter = available[letter].pop()
        # Index of letter must be less than index of previous letter
        while i_letter >= self.i_last:
            if not available[letter]:
                return None
            i_letter = available[letter].pop()

        # Available letters exhausted
        if not available[letter]:
            del available[letter]

        needed = copy.deepcopy(self.needed)
        needed[letter] -= 1 # Decrement count of letter
        # If count of letter is zero, remove from dict
        if not needed[letter]:
            del needed[letter]
        
        kwargs = {
            'used' : used,
            'needed' : needed,
            'available' : available,
            'i_last' : i_letter
        }
        return State(**kwargs)

    @property
    def is_complete(self):
        """
        Return True if word is complete, else return False.
        """
        if not self.needed:
            return True
        else:
            return False
        

def search(state):
    """
    Recursive 'greedy' approach to search the space of 
    words in lexicographic order. Find lexicographically 
    smallest word that can be merged given how much the word
    is built already. If no word can be built using the current
    state, return 0. 

    Args:
        state (State): Current state of word search. 

    Returns:
        str representing word if word found, else 0
    """
    # No available letters left to complete word
    if state is None:
        return 0

    # We have found a complete "merge-able" word!! Return
    # the word.
    if state.is_complete:
        return state.used

    # Iterate through letters 
    while len(state.needed_l) > 0:
        letter = state.needed_l.pop()
        state_next = state.add_letter(letter)
        # Recursively call search after adding letter
        result = search(state_next)
        if result:
            return result
    return 0

# Use memoization to store results
# Hash by letter counts needed and index
# Pass 'needed_l' instead of doing O(n*logn) sorting every time

def reverse_shuffle_merge(s):
    state = State.from_string(s)
    result = search(state)
    return result

# Check if any work; get min value? Just stop at first that works

# Example: s = "aaabeeba"
# Maintain a list of unique letters in order: "abe"
# Remove a letter once it has been used completely (e.g.
# if there were two original a's and we use two a's).
# Maintain a dict of counts of each letter.
# Use stack to represent substring in progress of being built?

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = reverse_shuffle_merge(s)
    fptr.write(result + '\n')
    fptr.close()

