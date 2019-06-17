#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# https://www.hackerrank.com/challenges/crossword-puzzle

# Use similar backtracking approach as N-Queens.

M = 10

def readPuzzleInput(fn: str) -> List:
    """
    Read crossword puzzle and words from file.
    """
    crossword = []
    with open(fn, 'r') as f:
        # Read first ten lines as crossword puzzle
        for _ in range(M):
            crossword += [f.readline().strip()]
        words = f.readline().strip().split(';')
    return [crossword, words]

def findHorizonalBlanks(crossword: List[List[str]]) -> List:
    """
    Find horizontal blanks in crossword puzzle.
    """
    B = []
    for i in range(M):
        start = None
        for j in range(1, M):
            if crossword[i][j] == '-' and crossword[i][j-1] == '-':
                if start is None:
                    start = j-1
                elif j == M - 1:
                    end = j
                    B += [['H', i, start, end]]
            elif start is not None:
                end = j-1 
                B += [['H', i, start, end]]   
                start = None
    return B

def findVerticalBlanks(crossword: List[List[str]]) -> List:
    """
    Find vertical blanks in crossword puzzle.
    """
    B = []
    for j in range(M):
        start = None
        for i in range(1, M):
            if crossword[i-1][j] == '-' and crossword[i][j] == '-':
                if start is None:
                    start = i-1
                elif i == M-1:
                    end = i
                    B += [['V', j, start, end]]
            elif start is not None:
                end = i-1
                B += [['V', j, start, end]]
                start = None
    return B

def findBlanks(crossword: List[List[str]]) -> List:
    return findHorizonalBlanks(crossword) + findVerticalBlanks(crossword)

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    crossword = []
    for _ in range(M):
        crossword_item = input()
        crossword.append(crossword_item)
    words = input()
    result = crosswordPuzzle(crossword, words)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
