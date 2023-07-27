class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0,len(height)-1
        
        result = 0
        
        while(i<j):
            h = min(height[i],height[j])
            result = max(result, h*(j-i))
            
            if h==height[i]:
                i+=1
            else:
                j-=1
        
        return result
            