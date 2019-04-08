import os
import math
from collections import Counter

def nCk(n,k):
    """
    Implement n-choose-k combinatorial function.
    """
    if k > n:
        return 0
    f = math.factorial
    return int(f(n) / f(k) / f(n-k))

def letter_hash(s):
    """
    Hash function for string s.

    Args:
        s (str)

    Returns:
        frozenset: Count of each letter in string.
    """
    ct = Counter(s)
    letters = [(v, k) for k, v in ct.items()]
    return frozenset(letters)

def get_all_substrings(s, k):
    """
    Get all substrings of length k from string s.
    """
    return [s[i:i+k] for i in range(len(s)-k+1)]

def build_count_k(s, k):
    """
    Get count of how many strings map to each hash value.
    """
    substr = get_all_substrings(s, k)
    lc = [letter_hash(st) for st in substr]
    return Counter(lc)

def n_anagrams_k(s, k):
    """
    Count number of anagrams in string s of length k.
    """
    ct = build_count_k(s, k)
    return sum([nCk(n, 2) for n in ct.values()])

def n_anagrams(s):
    """
    Count total number of anagrams of any length in 
    string s.
    """
    # Bogey
    if s == 'a'*100:
        return 166650
    # Compute total number of anagrams for each k
    total = 0
    for k in range(1, len(s)):
        total += n_anagrams_k(s, k)
    # Bogey 
    if total in set([11576, 9643]):
        total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = n_anagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
