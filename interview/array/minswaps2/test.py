#!/bin/python3

class Array(object):
    """
    Class to keep track of 'state' of task (i.e. the array).
    """
    def __init__(self, arr):
        """
        Initialize unordered array. Sort array to get.

        Args:
            arr (list of int): Our array
        """
        self.arr = arr
        self.arr_ordered = sorted(arr)
    
    @property
    def unordered_elements_index(self):
        """
        Get indices of unordered elements in array.
        
        Returns:
            list of int: Indices of unordered elements.
        """
        index_unordered = list()
        for i, val in enumerate(self.arr):
            if val != self.arr_ordered[i]:
                index_unordered.append(i)
        return index_unordered

    @property
    def unordered_elements_num(self):
        """
        Get number of unordered elements in array.

        Returns:
            int: Number of unordered elements.
        """
        return len(self.unordered_elements_index)

    def swap(self, i, j):
        """
        Swap elements i and j in array.

        Args:
            i (int): Index of first element to swap.
            j (int): Index of second element to swap.
        """
        tmp = self.arr[j]
        self.arr[j] = self.arr[i]
        self.arr[i] = tmp

def minimum_swaps(arr):
    pass
