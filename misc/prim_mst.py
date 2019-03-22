#!/bin/python3

import sys
import os 
from heapq import heappush, heappop, heapify  

# https://www.hackerrank.com/challenges/primsmstsub
        
# build classes for nodes and graph

class Node: 
    def __init__(self, value):
        self.value = value
        self.adjacent = list()
        self.weights = list()
    def add_adjacent(self, adj):
        self.adjacent.append(adj)
    def add_weight(self, weight):
        self.weights.append(weight)
        
N,M = [int(q_temp) for q_temp in input().strip().split(' ')]

nodes = list()
max_edge_wt = 10**5+1
for i in range(N):
    nodes.append(Node(i))

edges = list()
for i in range(M):
    x,y,r = [int(q_temp) for q_temp in input().strip().split(' ')]
    nodes[x-1].add_adjacent(nodes[y-1])
    nodes[y-1].add_adjacent(nodes[x-1])
    nodes[x-1].add_weight(r)
    nodes[y-1].add_weight(r)
    
st = int(input().strip())
start = nodes[st-1]

d = dict()
in_graph = dict()
for i in range(len(nodes)):
    d[nodes[i]] = max_edge_wt
    in_graph[nodes[i]] = False
    
h = list()
    
in_graph[start] = True
counter = 0
for i in range(len(start.adjacent)):
    heappush(h, (start.weights[i], counter, start.adjacent[i]))
    d[start.adjacent[i]] = start.weights[i]
    counter+=1
    
total_weight = 0
while len(h) > 0:
    stop = False
    valid_node = False
    while valid_node == False:
        if len(h) == 0:
            stop = True
            break
        node = heappop(h)
        if in_graph[node[2]] == False:
            valid_node = True
    if stop:
        break
    in_graph[node[2]] = True
    total_weight = total_weight + node[0]
    for i in range(len(node[2].adjacent)):
        if in_graph[node[2].adjacent[i]] == False and node[2].weights[i] < d[node[2].adjacent[i]]: 
            heappush(h, (node[2].weights[i], counter, node[2].adjacent[i]))
            counter+=1
            
print(total_weight)
