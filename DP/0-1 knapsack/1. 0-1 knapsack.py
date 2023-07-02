# Problem Statement
# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def recursion(index, weight):
    if index<=0: return 0
    
    taken, notTaken = 0,0 
    
    if weights[index-1]<=weight:
        taken = values[index-1] + recursion(index-1, weight - weights[index-1])
    notTaken = recursion(index-1, weight)

    return max(taken, notTaken)    

def memoization(index, weight):
    if index<=0: return 0
    if memo[index][weight] != -1: return memo[index][weight]

    taken, notTaken = 0,0
    
    if weights[index-1]<=weight:
        taken = values[index-1] + memoization(index-1, weight-weights[index-1])
    notTaken = memoization(index-1, weight)
    memo[index][weight] = max(taken, notTaken)
    
    return memo[index][weight]

def tabulation(INDEX, WEIGHT):
    for index in range(1,INDEX+1):
        for weight in range(1,WEIGHT+1):
            taken, notTaken = 0,0
            if weights[index-1]<=weight:
                taken = values[index-1] + tab[index-1][weight-weights[index-1]]
            notTaken = tab[index-1][weight]
            tab[index][weight] = max(taken, notTaken)
                    
    return tab[INDEX][WEIGHT]
    
def spaceOptimization(INDEX, WEIGHT):
    toggleIndex = 1

    for index in range(1, INDEX+1):
        for weight in range(1, WEIGHT+1):
            taken, notTaken = 0, 0
            if weights[index-1]<=weight:
                taken = values[index-1] + twoRows[toggleIndex^1][weight-weights[index-1]]
            notTaken = twoRows[toggleIndex^1][weight]
            twoRows[toggleIndex][weight] = max(taken, notTaken)
        toggleIndex ^= 1
    return twoRows[toggleIndex^1][WEIGHT]

def superSpaceOptimization(INDEX, WEIGHT):
    for index in range(1, INDEX+1):
        for weight in range(WEIGHT,-1,-1):
            taken, notTaken = 0, 0
            if weights[index-1]<=weight:
                taken = values[index-1] + oneRow[weight-weights[index-1]]
            notTaken = oneRow[weight]
            oneRow[weight] = max(taken, notTaken)
    return oneRow[WEIGHT]


T = int(input())
for i in range(T):
    N = int(input())
    weights = [int(i) for i in input().split()]
    values = [int(i) for i in input().split()]
    W = int(input())


    # print(recursion(N, W))
    
    # memo = [[-1]*(W+1) for i in range(N+1)]
    # print(memoization(N, W))

    # tab = [[0]*(W+1) for i in range(N+1)]
    # print(tabulation(N, W))

    # twoRows = [[0]*(W+1) for i in range(2)]
    # print(spaceOptimization(N, W))
    
    oneRow = [0]*(W+1)
    print(superSpaceOptimization(N,W))
