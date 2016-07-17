#!/bin/python3

import sys
from collections import Counter       

class BSNode:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left_child = False   
        self.right_child = False 
    def add_left_child(self, left_child):
        self.left_child = left_child
    def add_right_child(self, right_child):
        self.right_child = right_child
    def update_index(self, index):
        self.index = index

class BSTree:
    # initialize
    def __init__(self, root):
        self.root = root
    # insert new node
    def insert(self, new_node):
        go = True
        node = self.root
        while go:
            # sum already found in BST - update index
            if new_node.value == node.value:
                go = False
                node.update_index(new_node.index)
                break
            # no children exist
            if node.left_child == False and node.right_child == False:
                go = False
                if new_node.value < node.value:
                    node.add_left_child(new_node)
                elif new_node.value > node.value:
                    node.add_right_child(new_node)
            # left child exists but right child does not
            elif node.left_child != False and node.right_child == False:
                if new_node.value < node.value:
                    node = node.left_child
                elif new_node.value > node.value:
                    node.add_right_child(new_node)
                    go = False
            # right child exists but left child does not
            elif node.left_child == False and node.right_child != False:  
                if new_node.value > node.value:
                    node = node.right_child
                elif new_node.value < node.value:
                    node.add_left_child(new_node)
                    go = False
            # both right and left children exist
            elif node.left_child != False and node.right_child != False:
                if new_node.value > node.value:
                    node = node.right_child
                elif new_node.value < node.value:
                    node = node.left_child
    # get minimum value larger than certain number
    def getMinimumValueLargerThan(self, lg_val):
        go = True
        node = self.root
        if node.value > lg_val:
            return_val = node.value
            return_index = node.index
        else:
            return_val = 10**100
            return_index = -1
        while go:
            # update min value
            if node.value < return_val and node.value > lg_val:
                return_val = node.value
                return_index = node.index
            # no children exist
            if node.left_child == False and node.right_child == False:
                go = False
                break
            # left child exists but right child does not
            elif node.left_child != False and node.right_child == False:
                if node.value > lg_val:
                    node = node.left_child
                elif node.value <= lg_val:
                    go = False
                    break
            # right child exists but left child does not
            elif node.right_child != False and node.left_child == False:
                if node.value > lg_val:
                    go = False
                    break
                elif node.value <= lg_val:
                    node = node.right_child
            # both left and right children exist
            elif node.right_child != False and node.left_child != False:
                if node.value > lg_val:
                    node = node.left_child
                elif node.value <= lg_val:
                    node = node.right_child
        arr = [return_val,return_index]
        return(arr)

T = int(input().strip())

for i in range(T):
    
    N,M = [int(q_temp) for q_temp in input().strip().split(' ')]
    a = [int(q_temp) for q_temp in input().strip().split(' ')]

    run_sum = [0]*N
    run_sum[0] = a[0]%M
    root = BSNode(run_sum[0],0)
    tree = BSTree(root)
    result = 0
    for i in range(1,N):
        run_sum[i] = (run_sum[i-1] + a[i])%M
        arr = tree.getMinimumValueLargerThan(run_sum[i])
        if arr[1] > -1:
            result = max((run_sum[i] - arr[0] + M) % M, result)
        else:
            result = max((run_sum[i] - 0 + M) % M, result)
        x = BSNode(run_sum[i],i)
        tree.insert(x)
        
    print(result)