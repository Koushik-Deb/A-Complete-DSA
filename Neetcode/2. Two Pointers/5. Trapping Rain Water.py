class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2: return 0
        
        l,r = 0,len(height)-1
        lMax, rMax = height[l],height[r]
        res = 0
        while(l<r):
            
            if lMax<rMax:
                l+=1
                lMax = max(lMax,height[l])
                res+=lMax-height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                res+=rMax-height[r]

        return res
        
        
#         stack = []
#         ret = 0
        
#         for ind, val in enumerate(height):
            
#             while stack and height[stack[-1]]<val:
#                 popped_index = stack.pop()
                
#                 if stack:
#                     l = ind - stack[-1] - 1
#                     h = min(height[stack[-1]],val) - height[popped_index]
#                     ret += l*h
                
#             stack.append(ind)
        
#         return ret
            
        