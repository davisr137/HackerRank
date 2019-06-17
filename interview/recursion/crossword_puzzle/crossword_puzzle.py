#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# https://www.hackerrank.com/challenges/crossword-puzzle

## Use backtracking to solve crossword puzzle. 

M = 10

def readPuzzleInput(fn: str) -> List:
    """
    Read crossword puzzle and words from file.
    """
    crossword = []
    with open(fn, 'r') as f:
        # Read first ten lines as crossword puzzle
        for _ in range(M):
            crossword += [list(f.readline().strip())]
        words = f.readline().strip().split(';')
    return [crossword, words]

def findHorizonalBlanks(crossword: List[List[str]]) -> List:
    """
    Find horizontal blanks on board.
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
    Find vertical blanks on board.
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
    """
    Find horizontal and vertical contiguous blank
    spaces on board.
    """
    return findHorizonalBlanks(crossword) + findVerticalBlanks(crossword)

def writeWord(crossword: List[List[str]], word: str, blank: List) -> List[List[str]]:
    """
    Write word to board.
    """
    start = blank[2]
    end = blank[3]
    if blank[0] == 'H':
        i = blank[1]
        k = 0
        for j in range(start, end+1):
            crossword[i][j] = word[k]
            k += 1
    elif blank[0] == 'V':
        j = blank[1]
        k = 0
        for i in range(start, end+1):
            crossword[i][j] = word[k]
            k += 1
    return crossword

def writeBlank(crossword: List[List[str]], blank: List) -> List[List[str]]:
    """
    Write blank spaces to board.
    """
    start = blank[2]
    end = blank[3]
    if blank[0] == 'H':
        i = blank[1]
        for j in range(start, end+1):
            crossword[i][j] = '-'
    elif blank[0] == 'V':
        j = blank[1]
        for i in range(start, end+1):
            crossword[i][j] = '-'
    return crossword

def validWord(crossword: List[List[str]], word: str, blank: List) -> bool:
    """
    Check that word can be placed in blank in valid way.
    """
    Lw = len(word)
    start = blank[2]
    end = blank[3]
    if Lw != end - start + 1:
        return False
    if blank[0] == 'H':
        i = blank[1]
        k = 0
        for j in range(start, end+1):
            if crossword[i][j] not in set([word[k], '-']):
                return False
            k += 1
    elif blank[0] == 'V':
        j = blank[1]
        k = 0
        for i in range(start, end+1):
            if crossword[i][j] not in set([word[k], '-']):
                return False
            k += 1
    return True

def solveg(crossword, words, blanks):
    """
    Solve using a generator function with recursion.
    """
    if words:
        # Continue filling in crossword
        word = words[0]
        for j in range(len(blanks)):
            blank = blanks[j]
            if validWord(crossword, word, blank):
                crossword = writeWord(crossword, word, blank)
                blanks_sm = blanks[:j] + blanks[j+1:]
                for sol in solveg(crossword, words[1:], blanks_sm):
                    yield sol
                crossword = writeBlank(crossword, blank) 
    else:
        # No words or blanks left - done!
        yield crossword


def solve(crossword: List[List[str]], words: List[str], blanks: List) -> List[List[str]]:
    """
    Solve crossword puzzle using backtracking. 

    If it is possible to solve puzzle, return solution board. Else, 
    return False.
    """
    # No words or blanks left - done!
    if not words:
        return crossword

    # Continue filling out board by inserting 
    # first word in list.
    word = words[0]

    # Try each remaining blank space.
    for j in range(len(blanks)):
        blank = blanks[j]

        # If word placement is valid, recursively call 
        # to insert remaining words.
        if validWord(crossword, word, blank):

            # Write word to crossword
            crossword = writeWord(crossword, word, blank)
            
            # Recurse with word and blank removed
            blanks_sm = blanks[:j] + blanks[j+1:]
            sol = solve(crossword, words[1:], blanks_sm)
            if sol:    
                return sol

            # If word placement does not lead to a solution, write
            # blank back.
            crossword = writeBlank(crossword, blank)

    return False

## Utility functions to convert str <-> List

def strToList(s: str) -> List[str]:
    return [list(l) for l in s]

def listToStr(L: List) -> str:
    return ["".join(l) for l in L]

def crosswordPuzzle(crossword: List[List[str]], words: List[str]) -> List[List[str]]:
    """
    Complete the crossword puzzle.
    """
    crossword = strToList(crossword)
    blanks = findBlanks(crossword)
    crossword = solve(crossword, words, blanks)
    crossword = listToStr(crossword)
    return crossword

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    crossword = []
    for _ in range(M):
        crossword_item = input()
        crossword.append(crossword_item)
    words = input().strip().split(';')
    result = crosswordPuzzle(crossword, words)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
