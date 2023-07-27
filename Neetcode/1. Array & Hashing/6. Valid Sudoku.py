class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(r):
            s = set()
            for i in range(9):
                val = board[r][i]
                if val!='.' and val in s:
                    return False
                s.add(val)
            return True
        
        def checkCol(c):
            s = set()
            for i in range(9):
                val = board[i][c]
                if val!='.' and val in s:
                    return False
                s.add(val)
            return True
        
        def checkMat(r,c):
            s = set()
            for row in range(r,r+3):
                for col in range(c, c+3):
                    val = board[row][col]
                    if val!='.' and val in s:
                        return False
                    s.add(val)
            return True
        
        for i in range(9):
            for j in range(9):
                if not checkRow(i) or not checkCol(j) or not checkMat((i//3)*3, (j//3)*3):
                    return False
        return True