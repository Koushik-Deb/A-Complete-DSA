class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        arr = []
        def backTrack(n,left,right,result):
            if len(result)==2*n:
                arr.append(result)
                return
            if left<n:
                backTrack(n,left+1, right, result+'(')
            if right<left:
                backTrack(n,left,right+1, result+')')

                
        backTrack(n,0,0,'')
        return arr