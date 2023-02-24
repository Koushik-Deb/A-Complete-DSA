class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        mono_stack = []
        
        for ind, val in enumerate(prices):
            
            while mono_stack and prices[mono_stack[-1]] >= val:
                poppedIndex = mono_stack.pop()
                
                result[poppedIndex] = prices[poppedIndex] - val
                
            mono_stack.append(ind)
        return result
        