#!/bin/python3

import os

def max_subset_sum(arr):
    """
    Find the subset of non-adjacent elements with the maximum
    sum.

    Args:
        arr (list of int): Our array.

    Returns:
        int: Maximum subset sum.
    """
    # Max sum is the rolling maximum sum of non-adjacent
    # elements.
    max_sum = 0
    # At arr[i], adj is True if the max sum used arr[i-1],
    # False otherwise.
    adj = False
    # At max_non_adj_sum is the maximum sum available not
    # using arr[i-1].
    max_non_adj_sum = 0
    prev_max_sum = 0
    # Iterate over values in array
    for val in arr:
        # Positive value - add to one of the rolling sums
        if val > 0:
            # Current max sum is adjacent to element.
            if adj:
                # Possible new max sum = max non-adjacent sum
                # plus new array value
                new_sum = max_non_adj_sum + val
                # Update max sum. New max sum is adjacent to 
                # next element.
                if new_sum > max_sum:
                    max_sum = new_sum
                    adj = True
                # Do not update max sum. Max sum is not adjacent
                # to next element.
                else:
                    adj = False
            # Always add positive value to max sum if not 
            # adjacent. Max sum now adjacent to next element
            else:
                max_sum += val
                adj = True
        # Negative value. Not included in max subset. Max sum
        # is not adjacent to next element.
        else:
            adj = False
        # Max non-adjacent sum is the previous max sum.
        max_non_adj_sum = prev_max_sum
        prev_max_sum = max_sum
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = max_subset_sum(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
