#!/bin/python3

# https://www.hackerrank.com/challenges/cut-the-tree

import sys
from collections import Counter

class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []   
    def add_adjacent(self, adj):
        self.adjacent.append(adj)
        
class Tree:
    def __init__(self, root):
        self.root = root
        
class DFSNode:
    def __init__(self, value):
        self.value = value
        self.adjacent = []  
        self.visited = False
    def add_adjacent(self, adj):
        self.adjacent.append(adj)
    def visit(self):
        self.visited = True
        
class DFSTree:
    def __init__(self, root):
        self.root = root
        self.sum = 0
    def add(self,value):
        self.sum = self.sum + value

# number of nodes
N = int(input().strip())

# initialize lists of nodes and edges
nodes = list()
edges = list()

# populate nodes 
vals = [int(q_temp) for q_temp in input().strip().split(' ')]
for i in range(0,N):
    nodes.append(Node(vals[i]))

# record edges between nodes
for i in range(0,N-1):
    e = [int(q_temp) for q_temp in input().strip().split(' ')]
    node1 = nodes[e[0]-1]
    node2 = nodes[e[1]-1]
    node1.add_adjacent(node2)
    node2.add_adjacent(node1)
    edges.append(e)
    

def buildDFSTree(vals,edges):
    nodes = list()
    # populate nodes 
    for i in range(0,N):
        nodes.append(DFSNode(vals[i]))
        print(vals[i])
    # record edges between nodes
    for i in range(0,N-1):
        e = edges[i]
        node1 = nodes[e[0]-1]
        node2 = nodes[e[1]-1]
        node1.add_adjacent(node2)
        node2.add_adjacent(node1)
    tree = DFSTree(nodes[0])
    return(tree)
    

def tree_sums(root, current_sum):
    current_sum += root.value
    root.visited = True
    if len(root.adjacent) == 0:
        return(current_sum)
    subtree_sums = 0
    all_adj_visited = True
    for i in range(len(root.adjacent)):
        if root.adjacent[i].visited == False:
            all_adj_visited = False
            subtree_sums += tree_sums(root.adjacent[i], 0)
    if all_adj_visited:
        return(current_sum)
    else:
        return(current_sum+subtree_sums)
        
# consider graph abstraction with unordered edges

# do not necessarily need parent/child abstraction

# remove an edge

def buildDFSNodes(vals,edges):
    nodes = list()
    # populate nodes 
    for i in range(len(vals)):
        nodes.append(DFSNode(vals[i]))
    # record edges between nodes
    for i in range(len(edges)):
        e = edges[i]
        node1 = nodes[e[0]-1]
        node2 = nodes[e[1]-1]
        node1.add_adjacent(node2)
        node2.add_adjacent(node1)
    return(nodes)
    
def find_min_cut(vals,edges):
    min_cut = 10**100
    for i in range(0,len(edges)):
        # copy edges
        thisedges = edges.copy()
        # get indices for starting two graphs
        ind1 = thisedges[i][0]-1
        ind2 = thisedges[i][1]-1
        # remove edge of interest
        thisedges.remove(thisedges[i])
        # build graph
        nodesx = buildDFSNodes(vals,thisedges)
        # get difference in graph sums
        sum1 = tree_sums(nodesx[ind1],0)
        sum2 = tree_sums(nodesx[ind2],0)
        cut = abs(sum1-sum2)
        if cut < min_cut:
            min_cut = cut
    return(min_cut)
    
min_cut = find_min_cut(vals,edges)
print(min_cut)
    







