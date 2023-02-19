class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10==0 and x!=0)): return False
    
        revertedNumber = 0
        while(revertedNumber<x):
            revertedNumber = revertedNumber*10+x%10
            x = x//10
            
        return x==revertedNumber or x==revertedNumber//10
        
        
        
        
#         if x<0: return False
        
#         newX = x
#         start = 0
        
#         while(newX):
#             rem = newX%10
#             newX = newX//10    
#             start = start*10+rem
        
#         return start == x
            