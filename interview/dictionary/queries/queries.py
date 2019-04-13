#!/bin/python3

import os

def read_input(test_number):
    """
    Read input corresponding to test number.

    Args:
        test_number (str): e.g. '01','07', etc.

    Returns:
        list of lists of int
    """
    filename = 'input/input%s.txt' % test_number
    with open(filename, 'r') as f:
        n = f.readline()
        arr = f.readlines()
    queries = [list(map(int, s.strip().split())) for s in arr]
    return queries


def freq_query(queries):
    """
    Compute output of frequency queries.

    Args:
        queries (list of list of int): List of queries. For each
            query (n, m), n is 1, 2, or 3. 

    Returns:
        list of int: Output of queries.
    """
    # m_freq is a dictionary.
    #   Keys are values of queries[i][1]
    #   Each value is the frequency up to i of queries[i][1]
    m_freq = dict()
    # freq_ct is a dictionary.
    #   Keys are frequencies.
    #   Values are the number of unique values of queries[i][1]
    #       with given frequency.
    freq_ct = dict()
    out = list()
    # Iterate over queries
    for query in queries:
        [n, m] = query
        if m not in m_freq:
            m_freq[m] = 0
        if n == 3:
            if m in freq_ct:
                if freq_ct[m] > 0:
                    val = 1
                else:
                    val = 0
            else:
                val = 0
            out.append(val)
        else:    
            curr_freq = m_freq[m] # Current frequency of m
            # Either add or subtract to update frequency
            if n == 1:
                updated_freq = curr_freq + 1
            else:
                updated_freq = max(0, curr_freq - 1)
            # Increment new frequency
            if updated_freq not in freq_ct:
                freq_ct[updated_freq] = 0
            freq_ct[updated_freq] += 1
            # Decrement old frequency
            if curr_freq > 0:
                freq_ct[curr_freq] = max(0, freq_ct[curr_freq]-1) 
            m_freq[m] = updated_freq
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freq_query(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
