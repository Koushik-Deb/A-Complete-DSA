class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        main = [-1]*len(nums2)
        result = []
        mono_stack = []
        
        for ind, val in enumerate(nums2):
            
            while mono_stack and nums2[mono_stack[-1]] < val:
                poppedIndex = mono_stack.pop()
                
                main[poppedIndex] = val
            
            mono_stack.append(ind)
        
        
        dt = defaultdict(int)
        for ind, val in enumerate(nums2):
            dt[val] = ind
            
        for num in nums1:
            result.append(main[dt[num]])
        
        return result