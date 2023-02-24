class Solution:
    def trap(self, heights: List[int]) -> int:
        ret = 0 
        mono_stack = []
        
        for ind, val in enumerate(heights):
            
            while mono_stack and heights[mono_stack[-1]] < val:
                poppedIndex = mono_stack.pop()
                
                if mono_stack:
                    length = ind - mono_stack[-1] - 1
                    height = min(heights[mono_stack[-1]],val) - heights[poppedIndex]
                else:
                    break
                    
                ret+=height*length
            mono_stack.append(ind)
        
        return ret
                    
        