from os import *
from sys import *
from collections import *
from math import *

# def lcs(str1, str2):
# Write your code here.
def recursion(x, y, result):
    if x<=0 or y<=0: return result

    if str1[x-1]==str2[y-1]:
        result = recursion(x-1,y-1, result+1)
    return max(result, recursion(x-1,y,0),recursion(x,y-1,0))
    

def memoization(x,y,result):
    if x<=0 or y<=0: return result
    ret = result

    if (x,y,result) in memo and memo[(x,y,result)]!= -1:
        return memo[(x,y,result)]

    if str1[x-1]==str2[y-1]:
        result =  memoization(x-1,y-1,result+1)

    result = max(result, memoization(x-1,y,0),
        memoization(x,y-1,0))

    memo[(x,y,ret)] = result
    return memo[(x,y,ret)]




# def memoization(x,y,result):
#     if x>len(str1) or y>len(str2): return result
#     ret = result

#     if (x,y,result) in memo and memo[(x,y,result)]!= -1:
#         return memo[(x,y,result)]

#     if str1[x-1]==str2[y-1]:
#         result =  memoization(x+1,y+1,result+1)

#     result = max(result, memoization(x+1,y,0),
#         memoization(x,y+1,0))

#     memo[(x,y,ret)] = result
#     return memo[(x,y,ret)]


def tabulation(X,Y):
    result = 0

    for x in range(1,X+1):
        for y in range(1,Y+1):
            if str1[x-1]==str2[y-1]:
                tab[(x,y)] = 1 + tab.get((x-1,y-1),0)
                result = max(result, tab[(x,y)])
            else:
                tab[(x,y)] = 0
    return result


# return recursion(len(str1),len(str2),0)

# memo = {}
# print(memoization(len(str1), len(str2), 0))

str1 = 'abcjklp'
str2 = 'acjkp'

tab = {}
result = tabulation(len(str1),len(str2))
print(result)