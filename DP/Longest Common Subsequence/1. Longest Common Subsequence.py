class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def recursive(x,y):
            if x<=0 or y<=0:
                return 0
            
            if text1[x-1]==text2[y-1]:
                return 1 + recursive(x-1,y-1)
        
            else:
                return max(recursive(x,y-1), recursive(x-1,y))
        
        def memoization(x,y):
            if x<=0 or y<=0:
                return 0
            
            if memo[x][y]!=-1:
                return memo[x][y]
            
            if text1[x-1]==text2[y-1]:
                memo[x][y] = 1 + memoization(x-1,y-1)
            
            else:
                memo[x][y] = max(memoization(x,y-1),memoization(x-1,y))
            
            return memo[x][y]
        
        def tabulation(X,Y):
            
            for x in range(1,X+1):
                for y in range(1,Y+1):
                    if text1[x-1]==text2[y-1]:
                        tab[x][y] = 1 + tab[x-1][y-1]
                    else:
                        tab[x][y] = max(tab[x-1][y],tab[x][y-1])
            return tab[X][Y]
        
        # return recursive(len(text1),len(text2))
        
        # memo = [[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        # return memoization(len(text1),len(text2))
        
        tab = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        return tabulation(len(text1),len(text2))