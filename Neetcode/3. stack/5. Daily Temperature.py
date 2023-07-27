class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for ind,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<val:
                poppedIndex = stack.pop()
                result[poppedIndex] = ind-poppedIndex
            
            stack.append(ind)
        return result