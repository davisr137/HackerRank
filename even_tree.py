#!/bin/python3

import sys
import os 
from heapq import heappush, heappop, heapify  
        
# https://www.hackerrank.com/challenges/even-tree

# work up from leaves 

# no cycles

# keep a dictionary for how many untested adjacencies there are

# general graph node

class Node: 
    def __init__(self, value):
        self.value = value
        self.adjacent = list()
    def add_adjacent(self, adj):
        self.adjacent.append(adj)
    def remove_adjacent(self, adj):
        self.adjacent.remove(adj)

# tree node; we know explicitly what the parent/child structure is

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = False
        self.children = list()
        self.tree_sum = 0
    def add_parent(self, parent):
        self.parent = parent
    def add_child(self, child):
        self.children.append(child)
    def increase_sum(self,inc):
        self.tree_sum+=inc

N,M = [int(q_temp) for q_temp in input().strip().split(' ')]

nodes = list()
treenodes = list()

adj = dict()
adjl = list()
treesum = dict()
for i in range(N):
    nd = Node(i) 
    nodes.append(nd)
    adj[nd] = 0
    adjl.append(0)
    tnd = TreeNode(i)
    treenodes.append(tnd)
    treesum[tnd] = 0

# encode adjacency structure

for i in range(M):
    x,y = [int(q_temp) for q_temp in input().strip().split(' ')]
    nodes[x-1].add_adjacent(nodes[y-1])
    nodes[y-1].add_adjacent(nodes[x-1])
    adj[nodes[x-1]] = adj[nodes[x-1]]+1
    adj[nodes[y-1]] = adj[nodes[y-1]]+1
    adjl[x-1]+=1
    adjl[y-1]+=1
    
# build up tree starting from the bottom

adj2 = adj.copy()
adjl2 = adjl.copy()

# build tree

while len(adj2) > 2:
    #print('Sum')
    #print(treenodes[5].tree_sum)
    # get min adjacency count node
    n = min(adj2, key=adj2.get)
    # get index of node and parent
    node_index = n.value
    parent_index = n.adjacent[0].value
    p = n.adjacent[0]
    # add parent and child to tree nodes
    treenodes[node_index].add_parent(treenodes[parent_index])
    treenodes[parent_index].add_child(treenodes[node_index])
    # increase sum of node and parent
    treenodes[node_index].increase_sum(1)
    treesum[treenodes[node_index]]+=1
    treenodes[parent_index].increase_sum(treenodes[node_index].tree_sum)
    treesum[treenodes[parent_index]]+=1
    # decrement the adjacency count for node and parent
    adj2[nodes[parent_index]]-=1
    adj2[nodes[parent_index]]+=treenodes[node_index].tree_sum*10**(-10)
    adj2[nodes[node_index]]-=1
    # remove edge
    p.remove_adjacent(n)
    n.remove_adjacent(p)
    # remove node from dictionary if there are no more connecting edges
    if adj2[n] < 1:
        del adj2[n]
 
# only two left

n = min(adj2, key=adj2.get)
# get index of node and parent
node_index = n.value
parent_index = n.adjacent[0].value
p = n.adjacent[0]
# add parent and child to tree nodes
treenodes[node_index].add_parent(treenodes[parent_index])
treenodes[parent_index].add_child(treenodes[node_index])
# increase sum of node and parent
treenodes[node_index].increase_sum(1)
treesum[treenodes[node_index]]+=1
treenodes[parent_index].increase_sum(treenodes[node_index].tree_sum)
treenodes[parent_index].increase_sum(1)
treesum[treenodes[parent_index]]+=1
# remove edge
p.remove_adjacent(n)
n.remove_adjacent(p)
# remove node from dictionary if there are no more connecting edges
del adj2[n]
del adj2[p]

# set root of new tree
root = treenodes[parent_index]

# count number of nodes (not including root) with even tree sums
total = 0
for i in range(len(treenodes)):
    tnode = treenodes[i]
    if tnode != root:
        if treenodes[i].tree_sum % 2 == 0:
            total += 1

print(total)




