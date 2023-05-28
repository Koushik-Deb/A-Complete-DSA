from os import *
from sys import *
from collections import *
from math import *

def lcs(str1, str2):
    # Write your code here.
    def recursion(x, y, result):
        if x<=0 or y<=0: return result

        if str1[x-1]==str2[y-1]:
            result = recursion(x-1,y-1, result+1)
        return max(result, recursion(x-1,y,0),recursion(x,y-1,0))
        
    # def memoization(x,y,result):
    #     if x<=0 or y<=0: return result

    #     if (x,y,result) in memo and memo[(x,y,result)]!= -1:
    #         return memo[(x,y,result)]

    #     if str1[x-1]==str2[y-1]:
    #         result = 1 + memoization(x-1,y-1,result)

    #     result = max(result, memoization(x-1,y,0),
    #         memoization(x,y-1,0))

    #     memo[(x,y,result)] = result
    #     return memo[(x,y,result)]

    def memoization(x,y,result):
        # print(memo, x,y,result, (x,y,result) in memo)
        if x>len(str1) or y>len(str2): return result

        if (x,y,result) in memo and memo[(x,y,result)]!= -1:
            return memo[(x,y,result)]

        if str1[x-1]==str2[y-1]:
            result =  memoization(x+1,y+1,result+1)

        result = max(result, memoization(x+1,y,0),
            memoization(x,y+1,0))

        memo[(x,y,result)] = result
        return memo[(x,y,result)]


    # return recursion(len(str1),len(str2),0)

    memo = {}
    return memoization(1, 1, 0)

# return recursion(len(str1),len(str2),0)
str1 = 'abcjklp'#'bc'
str2 = "acjkp"#'cbccabcc'
memo = {}
print(memoization(1,1, 0))
print(memo)